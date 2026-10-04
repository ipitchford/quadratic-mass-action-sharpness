# Replay evidence and archive binding

This document describes evidence locations and their limits. It is not itself a successful replay receipt and does not predict the outcome of a future run.

## Included execution evidence

- `receipts/normal.json`: result of the recorded ordinary-Python verifier run.
- `receipts/optimized.json`: result of the recorded optimized-Python verifier run.
- `receipts/source-supports.json`: exact finite source-support enumeration.
- `receipts/internal-audit-replay.json`: retained historical v1 internal audit execution.
- `receipts/payload-replay.json`: the revised package's self-contained payload replay receipt, generated after checking the candidate payload. Its existence, recorded result and checked hashes—not this description—establish whether that replay completed.

Read each receipt's checked hashes and runtime/version fields before treating it as evidence for a file. The v1 verifier reported 472 checks; that historical count and the hashes in the old manuscript audit do not certify revised code or manuscript bytes. Revised counts come from the revised executed receipts. The universal theorem rests on the analytic proof, not the finite replay range.

## Revised ZIP and the external sidecar

The planned revised archive, `quadratic-mass-action-sharpness-v1.0.0-candidate.zip`, is accompanied on distribution by an ordinary output asset named `archive-replay.json`. That external sidecar records the final ZIP's SHA-256, clean-extraction checks and observed replay results. It is deliberately outside the archive: placing the final archive's own hash inside that archive would create a circular byte commitment.

The payload receipt inside the package and the final-archive sidecar are different records. The former is available to readers who have only the ZIP. The latter binds the final archive bytes and is distributed alongside it. If a reader has only one artifact, only that artifact's stated checks are available; no unavailable sidecar is treated as supplied evidence.

The planned ordinary release assets are `quadratic-mass-action-sharpness-v1.0.0-candidate.zip`, `archive-replay.json`, `paper.pdf`, and `SHA256SUMS`. Their presence and public availability require final upload and readback.

The original v1 archive and its original evidence remain unchanged. The revised archive is a separate version. Only an actual receipt with a successful observed outcome permits a PASS claim for the new archive.
