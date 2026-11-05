# Lens by Level

An evidence-graded board: seven lenses on four levels of a language model, with its sources, audit trail, a published X thread and a static website build. Owner: Wolfram Siener (@wolframs91).

Read `docs/how-this-was-made.md` first. It explains the project's history, how Wolfram works, and the mistakes that shaped the rules below.

## Rules

- `data/` is the source of truth. The HTML pages are build outputs: change `data/*.json`, then run `python3 build.py && python3 build_ledger.py`. Every cell change gets a `data/trail.json` entry with the reason.
- The tier rule is in the figure's legend; apply it one way. Peer-reviewed needs a venue listing seen, if only in search results; an acceptance note alone stays preprint; a case study inside a peer-reviewed paper is preliminary.
- Every number, quote and attribution traces to primary text. Before publishing anything public, run a separate review with the sources open (`audit/reviews/` shows the format).
- State the method plainly. This is AI-mediated analysis at a scale no single reader covers; present its receipts, counted from the repository, not confessions or unearned generalisations.
- On loaded topics, headlines use the words the evidence uses; technical distinctions go in tags and notes.

## Pieces

- `build.py` → `lens-by-level.html` (full board) · `build_ledger.py` → `ledger.html` · `frame.html`, `plain.html` (hand-written)
- `share/`: thread images. `python3 share/build_share.py && python3 share/render_themes.py && node share/shoot.js midnight`
- `thread/`: the posted thread as data, screenshots, and `ingest_x_archive.py` for the X export
- `site/build_site.py` → `site/dist/`, a static site ready to upload (`--base /path/` if it isn't served at the domain root)
- `.claude/skills/twitter-thread-images/`: the reusable skill for future threads
- `audit/`: source audits, the external audit and its verification, all review rounds

The ledger, full board and plain page are public claude.ai artifacts, linked from the posted thread; the frame artifact exists but was not linked and may still be private. All four URLs are in `site/build_site.py`; republish to the same URL rather than creating new ones.
