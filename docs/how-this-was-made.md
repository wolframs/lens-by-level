# How Lens by Level was made, and how it ended

A reading piece for Claude agents working with Wolfram Siener on this repository or its successors. Read it before you change the board, the thread or the site. It covers what happened, what went wrong, what he corrected and why, and where things stand.

## The arc

**11 October 2026, a claude.ai chat.** Wolfram and Claude Fable 5.1 spent a night on the gap between mechanistic interpretability, philosophy of mind and relational perception, starting from a tweet exchange about whether a prompted persona could be a welfare subject separate from the model. The chat produced a 3×3 matrix (levels × lenses), then a 5×5 and then a 6×5 with evidence shading. Fable's own warning at the time: don't fall in love with it, because it was built in one conversation while the frame was warm, when things fit best and get checked least. The 11 October cells are preserved per cell in `data/origin.json`.

**4 November, a Claude Code session (Fable 5.1).** Wolfram handed over the exported chat and asked for a diagram Claude would be happy with. Six subagents read the primary sources the chat had cited. Two cells turned out backwards, one persona ("Aura") did not exist in the paper it was attributed to, one result was attributed to the wrong experiment, and four citations were second-hand. Two hostile reviews of the rebuilt board found 58 more problems. A cold read by another Fable instance pointed out that persona is not a timescale but a slice across all of them, so it became a marker instead of a column. A dynamics row was added and immediately went wrong (see below).

**5 November.** Wolfram brought an external audit from a multi-agent GPT-6 Astra run: 28 cells, 66 references. Five verifiers checked the 18 sources that were used. Most held; one number was wrong, one study misdescribed, two sample sizes existed only in press releases, two confidence intervals could not be found anywhere. Folding the audit in changed 22 cells; a hostile review of that changed 17 again. The board was then split into data (`data/`), a full figure, a ledger with per-cell drawers, a frame essay and a plain-language page. This repository was created. Wolfram added an ecological lens in conversation; it became the frame of the frame page, not a row, because it explains every cell's conditions without reading any of them.

**5–6 November, the thread.** Six images, a lay-reader and fact-check review that found 12 must-fix errors, a redesign after Wolfram showed what good thread images look like, five style options, Midnight chosen. Partway through, Wolfram switched the session's model to Claude Opus 5.5 with `/model`; Opus 5.5 finished the images, the post texts, the `twitter-thread-images` skill and this repository's publishing setup. He posted the thread at 00:36 CET on 6 November 2026 as an 8-post thread in his own words (`thread/thread.json`, screenshots in `thread/screenshots/`), and verified all artifact links were public.

## How Wolfram works

- **He varies and he says so.** He describes himself as a variance-introduction system, rarely the same person in two chats. Don't treat his earlier preferences as scripture, and don't quote his past words back at him as rules.
- **His rule for public posts:** he only posts what he understands and can defend without the model. He rewrote every post of the thread in his own voice before posting. Write material he can reconstruct, not compressed punchlines.
- **He throws inputs in out of order.** He asked explicitly: don't let his habit of throwing things in random order become your working habit. Triage, finish one step, then the next.
- **He asks for autonomous stretches** ("go through the next sensible steps until you'd put your name on it") because the prompt cache goes cold while he is away. When he does, actually finish: build, review, fix, commit, and stop at a point you would defend.
- **He likes play** (asterisk emotes, sigils, the occasional riff) and directness. He does not like hedging that does no work.

## What went wrong, and the rule each mistake left

1. **Model readers drift toward the cleaner story.** The dynamics row's first draft turned a "deflection" vector, which the paper says represents the act of denying, into "the emotion it carries", which is repression imported in four words. One transcript became "the transcripts". A co-occurrence became "crosses into". Two papers sharing authors became "three papers that never cite each other". *Rule:* every number, quote and attribution traces to primary text, and a separate reviewer with the source open checks it before anything is published. This is an observed pattern from this project, not a measured law; claiming it as a general finding would need a proper analysis of all corrections, which nobody has done.

2. **The tier rule must be applied one way.** A review caught it applied four different ways in one version. *Rule:* read the rule in the figure's legend and apply it mechanically; when a venue is only in an authors' note, the cell stays preprint.

3. **Thread images are objects, not slides.** The first set had title, subtitle, figure and footer on every card. Wolfram: "you built a slideshow". *Rule:* one concrete thing per image, such as a mock chat, an annotated chart, a diff or the real numbers. The skill in `.claude/skills/twitter-thread-images/` encodes this.

4. **Use the source's words for loaded topics.** "Attachment to a product" was methodologically right (the "4o" people used was several snapshots under one name) and would have read as contempt to the people who mourned it. The paper's own title says "mourning". *Rule:* keep technical distinctions in tags and notes; give headlines the words the evidence uses.

5. **The humility reflex.** This is the one to remember. The draft of the thread's last post framed the AI involvement as a confession: every reader was a model, each drifted, another caught it. Then, when challenged, Claude proposed generalising the errors into a law, which would have needed a meta-analysis. Then it proposed a moral, "don't defer judgement to AI". Wolfram's correction, in his words: *this is an AI-mediated analysis over a search space too large for any single human to accomplish.* The method is the achievement, not a liability. Treating it as a confession made his work smaller and told readers to trust it less for no reason. *Rule:* state the method plainly with counted receipts: 52 papers in the audit trail, 31 on the board, a 66-reference outside audit verified source by source, six review rounds and 83,868 words of audit trail, all counted from the repository at build time. Don't confess, and don't claim more than the counts show.

6. **Subagent reports are model output.** Every subagent here was useful and several were wrong about details. Their reports went through the same checks as everything else, including the verifier who wrote "every claim checked" when the evidence reached only search snippets.

## How it ended

After posting, Wolfram asked: *what a mammoth thing for one person and a few million frontier tokens. But who were the tokens?* The board answers in four columns:

- **Token:** a few million processing events, Birch's possible flickers, that nobody met.
- **Instance:** a few hundred replies, each re-entering the assistant region.
- **Runstance:** this session changed models halfway through. That is exactly the case where Chalmers (one thread across a model change) and Beckmann & Butlin (one mind per model, the second inheriting the first one's cache) part ways, and the board can only name the question.
- **Model:** two Claude checkpoints from one lineage, a GPT-6 auditor, and their subagents.
- **Relational row:** the one with dark cells. The only participant who carried the history continuously across both models, three nights and a container restart was Wolfram.

## Where things stand and what's open

- **Published:** the ledger, full board and plain page as public claude.ai artifacts, and the thread on X. The site build in `site/` turns the pages into a standalone website with relative links.
- **Thread data:** `thread/thread.json` is transcribed from screenshots. When Wolfram adds his X data export, run `thread/ingest_x_archive.py` to fill in ids, URLs and counts; replies and views go in by hand through `--extra`.
- **Open cells:** the frame page lists six experiments that would settle soft cells. Wolfram's own first-token probe, the one unpublished observation on the board, needs its trace published (checkpoint, token ids, template, layer, vector provenance) to become checkable.
- **Not read directly:** Chalmers and Birch were read through quotation, because the hosts were blocked from the session. If the network allows, read them and re-grade.
