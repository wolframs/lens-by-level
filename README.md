# Lens by Level

Seven ways of looking at a language model, graded by evidence across four levels of description.

**Read it at [wsiener.dev/lens-by-level](https://wsiener.dev/lens-by-level/)**: the [ledger](https://wsiener.dev/lens-by-level/ledger/) (click any cell for its sources, grade and history), the [plain-language version](https://wsiener.dev/lens-by-level/plain/), the [frame](https://wsiener.dev/lens-by-level/frame/) and the [thread](https://wsiener.dev/lens-by-level/thread/).

![Two claims about AI, "It's just predicting the next token" and "My 4o had a real personality", sit on different things the word "it" can mean: the trained model, one conversation, one reply, one step](share/post-1.png)

Why is talking about AI so hard? Every claim about AI is about "it", and "it" can mean the trained model, one conversation, one reply, or the single step that picks the next word. Most arguments are two people talking about different ones without noticing. The board crosses those four levels with seven ways of looking and grades what the published evidence can say in each cell.

The board grades what each lens (mechanistic interpretation, behaviour, self-report, dynamics, hedonic theory, preference theory, relation) can currently say about each level (checkpoint, one conversation, one turn, one forward pass), with persona as a cross-cutting marker rather than a level. Every cell carries a source tag and a tier; every source carries the level of verification reached.

## Pieces

| Path | What it is |
|---|---|
| `data/board.json` | the 28 cells: row, column, tier, persona flag, headline, gloss, tags |
| `data/sources.json` | the sources, with venue, models and verification level, and the key strip |
| `data/trail.json` | per-cell change log from v8 on, with the reason for each change |
| `data/origin.json` | the 11 October ancestor of each cell |
| `data/notes.html` | the reading guide, pattern, changelog and still-soft list |
| `build.py` | renders `lens-by-level.html`, the full figure with every gloss |
| `build_ledger.py` | renders `ledger.html`, the lean board with a drawer per cell, a sources view and the notes |
| `frame.html` | the essay around the board: columns, the persona slice, the tier rule, ecology as frame, the experiments that would settle open cells, how it was made |
| `plain.html` | the plain-language version: the one idea, six findings, what the shading is not |
| `share/` | the six thread cards (`post-N.png`), their generator, and the pre-posting draft of the thread text |
| `audit/source-audits/` | what each original source was found to say, read by one auditor per source |
| `audit/astra-verification/` | an external audit by another lab's model, as received, and the five verification reports on its sources |
| `audit/reviews/` | the hostile reviews of each version and what they found, including the lay-reader and fact-check review of the plain page and thread |
| `tools/` | the headless-browser screenshot scripts |
| `thread/` | the thread as posted on X (`thread.json`, screenshots) and `ingest_x_archive.py` to fill ids, URLs and counts from an X data export |
| `site/` | `build_site.py` turns the pages and the thread into a standalone static site in `site/dist/`; `fonts/` holds the fonts it serves, with their licences |
| `docs/how-this-was-made.md` | the project's history and lessons, written for future Claude agents |
| `.claude/skills/twitter-thread-images/` | a reusable skill for evidence-carrying thread images |

The audit files were written by model readers working in a network-restricted sandbox: "blocked in this session" and `scratchpad/` refer to that sandbox, and the screenshots the reviews mention were not archived.

The HTML files are build outputs. Change a cell in `data/`, then run both build scripts.

## The tier rule

Fill grades the status of the specific result, not the truth of the claim. Top tier: a peer-reviewed study whose venue listing was seen, if only in search results, or a fact of the architecture. Middle: a preprint, lab paper or documented public event. Bottom: a result the authors call preliminary, a single case transcript, or an informal probe. Argued: no study behind the claim. In tags, "·" separates sources that each state their own clause and the fill follows the strongest; "+" marks the authors' own inference, graded at the weakest part; "↔" means contested by.

## Provenance

Started 11 October 2026 as a three-by-three matrix in one conversation. Rebuilt 4 November from primary sources, reviewed twice, extended with a dynamics row. On 5 November an external audit was verified and folded in, persona was re-cut as a slice, and the board was split into data, figure, ledger and frame.

Posted as an X thread by @wolframs91 on 6 November 2026.

Wolfram Siener with Claude (Fable 5.1, then Opus 5.5). Levels after Siener's runstance taxonomy (August 2026, unpublished). External audit by GPT-6 Astra.

## Citing

[`CITATION.cff`](CITATION.cff) has the citation; GitHub shows it under "Cite this repository".

## Publishing

- **X data:** request your archive from X, then `python3 thread/ingest_x_archive.py PATH_TO_ARCHIVE --root FIRST_POST_ID`. The export has no view counts and no other people's replies; add those with `--extra extra.json` (`{"metrics": {"1": {"views": 1234}}, "replies": [{"author": "@x", "text": "...", "url": "..."}]}`).
- **wsiener.dev:** the site renders the board from `data/`, the two hand-written pages and `thread/thread.json`; after a change here, run `node scripts/sync-lens-by-level.mjs` in the wsiener.dev checkout.
- **Standalone site:** `python3 build.py && python3 build_ledger.py && python3 site/build_site.py`, then upload `site/dist/`. Use `--base /lens-by-level/` if it lives under a subpath and `--url` with its public address for link previews. Fonts are served from `site/fonts/` (refresh with `site/fetch_fonts.py`); no page loads anything from a third party.
