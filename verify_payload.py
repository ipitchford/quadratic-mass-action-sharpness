#!/usr/bin/env python3
"""Verify a manifest-bound research payload and replay its exact programs.

This driver uses only Python's standard library. The mathematical child
programs require the dependencies pinned in requirements.txt. Run outputs
must be outside the payload, preserving the bytes under examination.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys
import tempfile

IGNORED_DIRECTORIES = {'.git', '.venv', 'venv', '__pycache__'}
REQUIRED_FILES = {'verify.py', 'classify_supports.py', 'examples.json',
                  'requirements.txt', 'paper.tex', 'paper.pdf'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def check_manifest(root):
    manifest = root / 'MANIFEST.sha256'
    require(manifest.is_file() and not manifest.is_symlink(), 'missing or symlinked MANIFEST.sha256')
    expected = {}
    for line_number, line in enumerate(manifest.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r'([0-9a-fA-F]{64}) [ *](.+)', line)
        require(match is not None, f'invalid manifest line {line_number}')
        digest, name = match.groups()
        relative = PurePosixPath(name)
        require(not relative.is_absolute() and '..' not in relative.parts
                and '\\' not in name and str(relative) == name,
                f'unsafe or noncanonical manifest path: {name}')
        require(name not in expected and name != 'MANIFEST.sha256',
                f'duplicate or circular manifest entry: {name}')
        require(not any(part in IGNORED_DIRECTORIES for part in relative.parts),
                f'manifest entry uses an excluded runtime directory: {name}')
        expected[name] = digest.lower()
    require(REQUIRED_FILES <= expected.keys(), 'manifest omits required scientific payload files')

    present = set()
    excluded = []
    for directory, subdirs, filenames in os.walk(root, followlinks=False):
        directory = Path(directory)
        for name in list(subdirs):
            path = directory / name
            if name in IGNORED_DIRECTORIES:
                subdirs.remove(name)
                excluded.append(path.relative_to(root).as_posix())
            else:
                require(not path.is_symlink(), f'payload directory is a symlink: {path}')
        for name in filenames:
            path = directory / name
            require(not path.is_symlink() and path.is_file(), f'payload file is not regular: {path}')
            relative = path.relative_to(root).as_posix()
            if relative != 'MANIFEST.sha256':
                present.add(relative)
    require(present == expected.keys(),
            'manifest inventory mismatch; missing=' + repr(sorted(expected.keys() - present))
            + '; unlisted=' + repr(sorted(present - expected.keys())))
    for name, digest in expected.items():
        require(sha256(root / name) == digest, f'SHA-256 mismatch: {name}')
    return {'status': 'MANIFEST_PASS', 'manifest_sha256': sha256(manifest),
            'files_checked': len(expected), 'file_sha256': expected,
            'excluded_runtime_directories': sorted(excluded)}


def run_json(root, output, name, arguments):
    command = [sys.executable, *arguments]
    completed = subprocess.run(command, cwd=root, capture_output=True, text=True,
                               encoding='utf-8', timeout=300,
                               env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    (output / (name + '.stdout.json')).write_text(completed.stdout, encoding='utf-8')
    (output / (name + '.stderr.log')).write_text(completed.stderr, encoding='utf-8')
    require(completed.returncode == 0, f'{name} failed with exit code {completed.returncode}')
    return json.loads(completed.stdout)


def replay(root, output, manifest):
    normal = run_json(root, output, 'normal', ['verify.py', '--negative-controls'])
    optimized = run_json(root, output, 'optimized', ['-O', 'verify.py', '--negative-controls'])
    require(normal.get('status') == 'EXACT_CHECKS_PASS', 'ordinary verifier did not report PASS')
    require(normal == optimized, 'ordinary and optimized verifier JSON differ')
    controls = normal.get('negative_controls', [])
    require(len(controls) >= 11 and all(c.get('rejected_by') for c in controls),
            'extended negative controls are missing or not rejected')
    supports = run_json(root, output, 'source-supports', ['classify_supports.py'])
    require(supports.get('stats') == {'affine_deficient': 24, '2': 156, '3': 60, '4': 12},
            'unexpected source-support counts')
    representatives = supports.get('quartic_representatives', [])
    require(len(representatives) == 2 and all(r.get('degree') == 4 for r in representatives),
            'unexpected quartic source-support representatives')

    reviewers = []
    reviewer_paths = sorted(name for name in manifest['file_sha256']
                            if PurePosixPath(name).name == 'reviewer_independent_checks.py')
    for index, name in enumerate(reviewer_paths, 1):
        result = run_json(root, output, f'referee-{index}', [name])
        require(result.get('status') == 'PASS', f'distributed referee checker did not pass: {name}')
        reviewers.append({'path': name, 'status': result['status'],
                          'checks': result.get('reported_check_invocations')})

    # Child execution must not have changed the committed scientific payload.
    after = check_manifest(root)
    require(after['manifest_sha256'] == manifest['manifest_sha256']
            and after['file_sha256'] == manifest['file_sha256'],
            'payload changed during replay')
    return {'status': 'PAYLOAD_REPLAY_PASS', 'python': platform.python_version(),
            'sympy': normal.get('sympy'), 'manifest': manifest,
            'ordinary_and_optimized_results_identical': True,
            'verifier_checks': normal.get('checks_executed'),
            'rejected_negative_controls': len(controls),
            'source_supports': supports['stats'], 'referee_checkers': reviewers,
            'referee_checker_scope': 'Replayed if distributed; shared SymPy backend, no algebra-engine independence claim.',
            'scope': 'Exact-byte payload checks and finite program replay; universal results rest on the analytic proof.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--manifest-only', action='store_true')
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = check_manifest(root)
    if args.manifest_only:
        print(json.dumps(manifest, indent=2, sort_keys=True))
        return
    output = (args.output_dir.resolve() if args.output_dir is not None
              else Path(tempfile.mkdtemp(prefix='quadratic-payload-replay-')))
    require(output != root and root not in output.parents,
            'output directory must be outside the checked payload')
    output.mkdir(parents=True, exist_ok=True)
    require(not any(output.iterdir()), 'output directory must be empty to preserve previous receipts')
    result = replay(root, output, manifest)
    result['output_directory'] = str(output)
    (output / 'payload-replay.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n',
                                               encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
