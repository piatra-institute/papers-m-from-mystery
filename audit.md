# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 27 CSL entries. 14 matched in Crossref with DOIs; baez2002, montonen1977 and devastato2019 completed from DOI records (devastato2019 now cites its published version, IJMPA 34(19): 1930010); the 10 arXiv preprints re-fetched from the arXiv API (titles, authors, dates confirmed) and entered as preprints with arXiv numbers. In-text citations converted to Pandoc [@id]; legacy list replaced by the citeproc list.
- Bibliographic corrections: jordan1934 and wigner1939 full page ranges (29-64, 149-204) and von Neumann's name restored where Crossref gave only first pages and "v. Neumann".
- analyses.py: added /generation/deletion_break_counts (lengths of the existing deletion_breaks lists) so the counts 5, 4, 3, 3, 2, 0 bind to pointers; every pre-existing value unchanged.
- claims.yaml: 31 claims (14 computation, 6 source, 6 interpretation, 3 definition, 1 assumption, 1 normative). Source claims checked against arXiv abstracts (Baez and Schwahn; Baez e7; Costello and Gwilliam; Farnsworth; Ben-Zvi; Ben-Zvi, Sakellaridis and Venkatesh) and OpenAlex abstracts (Tong; Kapustin and Witten).
- Unverified, not bound: the detailed Peirce-chain statements attributed to Baez, Bokor and Boyle (abstract states only the bi-Cayley correspondence); Devastato et al. on generations and Yukawas inserted by hand; Fang, Feng and Xie on composite-elementary exchange; the infraparticle theorem (Fröhlich et al., Buchholz, Duch and Dybalski); Seiberg, Doplicher-Roberts, Chamseddine-Connes, Goddard-Nuyts-Olive (no abstracts retrievable).
- Execution receipt: run id exact (verification/exact.json), `uv run python run_all.py`, 17 invariants, results.json reproduced.
- metadata claims_target: claim-ledger.

## 2026-09-22 — prose revision

Prose rewritten against the house standards. Headings made descriptive (Introduction, Recent results on exceptional Jordan algebras and the Standard Model, The kernel and its quantum completion, Anomaly cancellation in one generation, Global forms of the gauge group, Failure of label-based criteria for indivisibility, A hierarchy of atomicity and the electron conjecture, Conjectures and failure criteria, Objections, Falsification, Relativity of atomicity, Reproducibility).
All values are exact (rational arithmetic, exhaustive enumeration); no grid-derived quantities. Deletion counts re-derived by hand (q_L 5, l_L 4, u^c and d^c 3, e^c 2, nu^c 0) and agree. 3,920/6,560 = 0.5976.
The earlier text called the right-handed neutrino's existence "experimentally indirect"; it has not been observed, and the text now says it has not been established experimentally.
Unicode tensor symbol replaced by $\otimes$ (the Palatino build font lacks U+2297). results.json unchanged by figure edits.

## 2026-08-23 — v1.1, precision pass against the primary abstracts

Scope: the established-floor section, after fetching the three 2026 abstracts and the Jordan-pair paper's body at first hand.

Changes:
  - The E7 statement now says what the 32-dimensional spaces are (one generation of fermions together with their antiparticles) and carries the lineage Baez himself credits: the setting due to Nasmith, the mathematics running back to the Kugo-Yanagida E7 unification.
  - The Baez-Schwahn statement now includes the identity-component detail of the stabilizer construction and their own gloss, the Standard Model gauge group as the symmetries of an octonionic qutrit acting as unitary operators on an ordinary qutrit and, within it, on a qubit.
  - The Jordan-pair body claims (the 16-dimensional representation with the exact multiplet list, the right-handed neutrino, the chosen tripotents, the threefold descent not yet three generations) were verified against the paper's own text; the descent chain is now described in prose rather than raw notation, and the remaining code-like tokens in running prose were replaced.

Verification: voice 0/0; refs 25/27, 0 missing, 0 unused; claims 0 no-match; build 12 pages; check => PASS.

## 2026-08-23 — v1, first full draft to publication

Scope: the entire paper, simulation, and evidence base, from the seed chat to publication.

Changes:
  - Sources: 27 entries verified against the arXiv API, Crossref, or the standard record. The three 2026 exceptional-Jordan papers were verified at first hand with exact titles, authors, and dates (Baez and Schwahn, June 13; Baez, Bokor and Boyle, July 12; Baez, three generations in E7, August 6), correcting the seed's "August 2026 papers involving John Baez and collaborators." The seed's generic anomaly citation resolves to García-Etxebarria and Montero's Dai-Freed paper and is cited as what it is. The Quanta article was dropped for the primary relative-Langlands sources.
  - Register discipline enforced throughout: established, proposed, and conjectural are separated; the 2026 results are stated with their authors' own disclaimers (chosen tripotents, no dynamics, no three generations, not a physical theory); the seed's BV and RG apparatus is carried as architecture and marked proposed; the Langlands material is held to one computed lattice and one disciplined conjecture, with the supersymmetric provenance of the rigorous results stated at each mention.
  - The simulation is exact arithmetic with no numerical tolerance: the one-generation anomaly ledger in fractions, the global-form atlas by enumeration of center classes, the SL(2,Z) orbit with constructive Bezout witnesses, and the fusion computations by Freudenthal weight multiplicities. The paper's addition to the seed's hierarchy is computed rather than asserted: in the SU(2) fusion ring, tensor-primality is universal and empty because bound states arise as summands of tensor products, never as factors, which forces the hierarchy's bound-state and duality levels.
  - The deletion-rigidity result (five of six multiplets anomaly-locked, the right-handed neutrino the unique free site) was found in computation and promoted to a named finding, since it quantifies how overdetermined the 16-state target is and why the one unconfirmed particle is the one the ledger permits.
  - Voice: draft came in at 0 errors, 2 review-candidates; both rewritten, "exactly" thinned 11 to 7, the rhetorical "three times over" section title replaced, killing the spelled-quantity advisories.

Verification:
  - voice: 0 errors, 0 review-candidates
  - refs: 25 in-text keys, 27 bib entries, 0 missing, 0 unused (three Baez 2026 entries share a key by design; the co-author lists disambiguate in text)
  - claims: 20 sim values, 2 decimal claims in prose, 0 without a match
  - build: 12 pages, no missing-character warnings
  - simulation: 17/17 invariants, exact arithmetic
  - check => PASS
