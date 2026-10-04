# Sources and supplied evidence

The authoritative mathematical bibliography is in [the manuscript](paper.tex). [PRIOR_ART.md](PRIOR_ART.md) records the bounded source search and inspected versions; [CITATION_AUDIT.md](CITATION_AUDIT.md) records citation checks. These files do not certify exhaustive historical priority.

## Principal mathematical sources

- Murad Banaji and Elisenda Feliu, *Positive equilibria in mass action networks: geometry and bounds* (2026), [DOI 10.1007/s00285-026-02429-8](https://doi.org/10.1007/s00285-026-02429-8), Theorem 5.5 and Remark 5.8: upper-bound hypotheses and the attainment question.
- Kaitlyn Phillipson and J. Maurice Rojas, *Fewnomial systems with many roots, and an adelic tau conjecture*, [arXiv:1011.4128v5](https://arxiv.org/abs/1011.4128v5), Theorem 1.6; published in *Contemporary Mathematics* 605 (2013), 45–71, [DOI 10.1090/conm/605/12111](https://doi.org/10.1090/conm/605/12111): the prior extremal polynomial family. The [bridge](supplement/phillipson-rojas-bridge.md) provides the explicit chemical realization.
- Murad Banaji, Balázs Boros and Josef Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity* (2024), [DOI 10.1007/s11071-024-10068-1](https://doi.org/10.1007/s11071-024-10068-1), Remark 38: the planar chemical precedent.

No full third-party paper PDF is redistributed. External source versions, access limits and bibliographic uncertainties are stated in the source audits rather than inferred from metadata alone.

## Supplied review bundle

A user-provided referee-style assessment and its separate audit ZIP were received. The supplied ZIP's SHA-256 is `352b67636e651a2237d74cb3d907f58c90241cd76ee476b344a5c42914a59006`. Its supplied checker was freshly replayed and completed 1,791 checks. That new execution result is distinct from the report's historical claims; inspect the [retained checker](review/user-supplied/reviewer_independent_checks.py) and [fresh result](review/user-supplied/replayed-results.json) for its actual scope and provenance.

The fresh checker run did not take an original manuscript archive as input; its null source-archive hash and “original archive absent” scope refer to that fact. The review-bundle hash above is separate provenance, not an archive-integrity conclusion of the mathematical checker.

The reviewer identity and original independent-execution provenance remain unauthenticated. Receiving and rerunning supplied code does not authenticate the reviewer or create journal acceptance. The full supplied report is not redistributed. [REVIEW_RESPONSE.md](REVIEW_RESPONSE.md) records the recommendation, indicative assessment and actions; [PROVENANCE.md](PROVENANCE.md) records attachment identities. Supplied reviewer code has license status **NOASSERTION**, as explained in [LICENSES.md](LICENSES.md).

## Citation and deposit formats

Candidate identifiers are version DOI `10.5281/zenodo.23146115`, concept DOI `10.5281/zenodo.23146114`, and repository `ipitchford/quadratic-mass-action-sharpness` at tag `v1.0.0-candidate`. Reservation does not establish publication. The [CFF 1.2.0 schema](https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema.json) and [Zenodo metadata documentation](https://developers.zenodo.org/#add-metadata-to-your-github-repository-release) were consulted for the citation and deposit files. CFF describes the software evidence package and uses `preferred-citation` for the manuscript.
