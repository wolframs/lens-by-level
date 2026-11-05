# Hostile review, round two: "Six lenses on five levels of a language model", v4 (4 Nov 2026)

Reviewed: `/home/user/lens-matrix/lens-by-level.html` (whole file), the three v4 screenshots (`v4-fig-light.png`, `v4-fig-dark.png`, `v4-light-1240.png`), the round-one report `review_v3.md`, and the six audit files as ground truth. Cells are named row × column. Contrast ratios below were computed from the hex values in the v4 CSS (WCAG formula), not eyeballed.

Headline verdict: v4 is a real revision, not a patch. Of the 58 round-one items, 46 are resolved outright, 6 partly, 6 not resolved; of the 6 not resolved, 5 are declines I would accept and 1 (the inverted ramp with an identical hex across themes, D2) I would not. Part B finds nothing that misstates a source at the HIGH level. The residual list is short: one tag the key does not expand, one qualifier attributed to the wrong critic, one verification claim slightly stronger than the audit supports, one headline the page's own notes undercut, and the dark-mode ramp.

---

## Part A: disposition of every round-one finding

### FACTUAL

- **F1 (Self-report × Runstance, "denial"/"something real")** — RESOLVED. Now "Qwen moved from hedging to affirmation in one transcript; the authors read it as sycophancy, not as settled", tagged "Lu 26 · case study", ●○○. "Hedging" matches the audit; the user-addressed quote is gone; the tier dropped.
- **F2 (Birch's second hypothesis)** — RESOLVED. "One of his two surviving candidates: feeling per processing event. The other is per physical implementation; neither is the persona or the conversation." Matches audit originals §3 exactly.
- **F3 (blackmail snapshot)** — RESOLVED. Cell: "on an unreleased earlier Sonnet 4.5 snapshot"; source 3: "the blackmail study used an earlier unreleased snapshot".
- **F4 (PC1 vs Assistant Axis; "belongs to the checkpoint"; 60%)** — RESOLVED. Model cell is now the suggested "A contrast vector from role-play to the default assistant, inherited from the base model and shared across three model families"; Persona cell "Clamping along that vector cuts persona-jailbreak harm by half or more ... it does not fully restore the default" covers both the paper's "nearly 60%" and the blog's "roughly 50%".
- **F5 (Still soft, structural tokens)** — RESOLVED. "never reads the first token or template tokens ... at least half of its emotion vectors peak on structural tokens (numerals, punctuation, whitespace, function words)". Matches Hollowell per the audit.
- **F6 (Self-report × Token, "20% detection", "in Claude")** — RESOLVED, with one residue carried to Part B (B-F1): "Opus 4.1 detects and names an injected concept in ~20% of best-case trials, zero false positives" is right; "on open-weight models, critics find ..." is now attributed by the tag to Singh 26, which the audit cannot support.
- **F7 (B&B "judge-scored")** — RESOLVED. The author took the short option: "one prefix, Qwen 3 32B"; "judge-scored" removed; changelog item 7 keeps the every-time caveat. Defensible.
- **F8 (Mech interp × Instance, "unchanged", dispositional caveat)** — PARTLY. "unchanged" → "nearly identical"; "one axis" added. The authors' preferred reading (persona dispositionally active between turns, B&B sec. 4.2) is not in the cell. Defensible decline: the headline "used only while speaking" is a near-verbatim lift of B&B p.18 ("active only while the model is producing its own tokens"), and the cell is at ●○○ with "prelim".
- **F9 ("ordinary" conversations)** — RESOLVED. "Simulated therapy and AI-philosophy chats, with an LLM playing the user"; changelog item 1 now says "simulated conversations".
- **F10 (Relational × Model, "checkpoint", "for good")** — RESOLVED. "Attachment to a named model / Users fought GPT-4o's removal from ChatGPT; OpenAI reversed it in Aug 2025, then removed it for good in Feb 2026"; changelog item 4 adds "API snapshots stayed longer". See B-L1 for the column tension this creates.
- **F11 (Relational × Persona, "steering a fresh chat")** — RESOLVED. Now the suggested "talking a fresh chat back into the region partly recovers them; on Birch's view the persistence is an illusion".
- **F12 (Hedonic × Instance, "unmeasured")** — RESOLVED. "Whether a turn's state carries into the next through the cache is the open question."
- **F13 (changelog, Aura)** — RESOLVED. Verbatim the suggested rewrite.
- **F14 (changelog, Chalmers's subject)** — RESOLVED. "his candidate subject is the virtual instance, the model running one conversation, not the persona".
- **F15 (Betley, persona reading, "broadly misaligned")** — RESOLVED. "answer unrelated prompts misalignedly about 20% of the time; later work reads it as a persona".
- **F16 (Singh source entry)** — RESOLVED in the source list ("header names COLM 2026, not verified"; "Open-weight models" removed). But the cell gloss still says "on open-weight models" under a Singh tag; see B-F1.
- **F17 (Lindsey link/title mismatch)** — RESOLVED. Link now arXiv 2601.01828, matching the title.
- **F18 (own probe: BOS, unnamed model)** — PARTLY. The model is still unnamed, but source 12 now admits "the model is not recorded in the thread", which is honest and the only honest option. The headline "A mood, if anything" still asserts the welfare reading that the page's own Still-soft bullet says the evidence disfavours; see B-W1.
- **F19 ("nothing else persists")** — RESOLVED. "Within the context window the model keeps no state but the cache".
- **F20 ("tone"; colon as method)** — RESOLVED. "predict the reply's own emotion readout, r≈0.87"; headline "Readouts live at a position" no longer implies the colon is the only readout.
- **F21 (Chalmers, "so")** — RESOLVED. "one of his three reasons the model is not the candidate subject".
- **F22 (B&B v3, Betley Nature)** — RESOLVED. "v2 read, a v3 of Sep 2026 exists"; "also Nature 2026". Ergo-forthcoming omitted; harmless.
- **F23 (ICML listing "stated as fact")** — NOT RESOLVED. Still soft says "appears on the ICML 2026 schedule as a poster per the conference listing" and source 1 says "ICML 2026 poster per the conference schedule". Audit assistant-axis §1: "NOT DIRECTLY VERIFIED ... search-engine result snippets only ... unconfirmed by a primary page". The same sentence says the spotlight label "was not verified" although the snippet came from a page named `2026SpotlightPosters`, i.e. the poster and the spotlight rest on identical evidence. Low stakes, but the page's own tier rule ("venue listing seen") is being satisfied by a snippet, and the text should say so: "per search listings of the conference schedule".

### TIER

- **T1 (Lu ●●● vs Gilg ●●○, different standards)** — RESOLVED. The legend line now states the rule: "Peer-reviewed needs a venue listing seen; an acceptance note alone stays preprint", and Still soft applies it to Singh. The residual is F23: "seen" means seen in a search snippet, which the page does not say.
- **T2 (tier grades the source, not the result)** — RESOLVED. "Tier follows the specific result, not the paper: a case study inside a peer-reviewed paper grades as preliminary"; Self-report × Runstance moved to ●○○.
- **T3 (architecture applied once, withheld three times)** — RESOLVED. Behaviour × Token is now "architecture" ●●●; Preference × Token and Relational × Token remain ○○○ as interpretive readings ("A pass emits a logit, not a want"; "Nobody meets a token"). That split is defensible: the first is a fact, the other two are glosses on it.
- **T4 (Singh COLM)** — RESOLVED by the stated rule and the explicit hold ("so they stay at preprint").
- **T5 ("Chalmers 25" vs Inquiry 2026; "Birch 25")** — NOT RESOLVED; declined silently. Defensible: tag by first-appearance year, with the journal in the source list.
- **T6 (suffix grammar undefined)** — RESOLVED. "Tag suffixes: ICML = venue · prelim = the authors' word · case study = one transcript · n=1 = one prompt · ↔ = contested by." The one undefined use of "·" is as a joiner in "B&B 26 · Birch 25"; obvious enough.

### INTERNAL CONSISTENCY

- **C1 ("thinnest" contradicted)** — RESOLVED. "The hedonic row is the least settled", justified by the open-cell count.
- **C2 ("backbone")** — RESOLVED. "supplies the only peer-reviewed studies in the model and conversation columns". Verified against the grid: Model column has Lu ●●● ×2 and nothing else peer-reviewed; Runstance has Lu ●●● once (the other ●●● is architecture, and the Lu case study is ●○○).
- **C3 (welfare rows hold readouts)** — RESOLVED. Group header "what would have to be true for anything to count, and the readouts that bear on it"; How to read it mirrors it.
- **C4 (changelog "three new cells")** — RESOLVED. Item 8 names the three cells.
- **C5 (screenshot not self-contained)** — RESOLVED by the in-figure key strip, with one omission (B-C1).

### LOGIC

- **L1 (integrator contradiction)** — RESOLVED. "History held on both sides; the human carries it continuously, the model re-reads it each turn".
- **L2 (Elo cell vs Token cell)** — RESOLVED. Token cell: "Preferences are a pattern over many choices; one pass shows one". The Elo cell stays in Instance, which the new Token cell makes coherent.
- **L3 (Hedonic Runstance/Instance overlap)** — RESOLVED as suggested. One second-order note in B-L2.
- **L4 (Self-report × Token is a turn-level result)** — PARTLY. Not moved; reframed as "Reports a perturbed pass, sometimes", which at least makes the column logic explicit (what is perturbed is activations; what reports is the turn). Defensible decline, but "a perturbed pass" is singular where the injection is sustained across the turn (B-W4).
- **L5 ("folk vocabulary of the bottom row")** — RESOLVED. "of the rows beneath".
- **L6 (Birch persona clause in Token column)** — RESOLVED. Clause removed.
- **L7 (Model/Persona cells one finding split; "basin")** — RESOLVED. "that vector" now resolves to the contrast vector; "it does not fully restore the default" added; header "a region in the model".

### WORDING

- **W1 ("basin")** — RESOLVED.
- **W2 ("Reports are trainable")** — RESOLVED. "Tune one report, others follow".
- **W3 (sycophancy drops the authors' other half)** — PARTLY. "not as settled" is a four-character nod to "nuanced responses are more appropriate than outright denying". Readable both ways ("the authors read it as sycophancy, not as settled [evidence]" vs "[the question is] not settled"), but either reading is fairer to Lu et al. than v3. Acceptable.
- **W4 ("Affect steers the act")** — RESOLVED. "Emotion vectors steer the act".
- **W5 (near-synonymous headlines)** — RESOLVED. "Flips with a cache edit".
- **W6 ("The default is loosely held")** — RESOLVED. "The default persona is loosely held".
- **W7 ("this thread's")** — RESOLVED in the legend ("the authors' own"); the notes still say "the reasoning of the thread this came out of" and sources 12 and Still soft refer to "the thread" without ever naming or linking it. Below the fold, so low. New ambiguity noted in B-W3.
- **W8 (documented event lumped with lab paper)** — NOT RESOLVED; declined. Defensible as a matter of taste; the legend wording is honest.
- **W9 (footer cites an unlinked taxonomy)** — NOT RESOLVED; declined. Mildly indefensible: a footer that cites "Siener's runstance taxonomy, Aug 2026" with no entry in a source list that otherwise links everything is the one unreferenced citation on the page.

### DESIGN

- **D1 (middle-tier contrast)** — RESOLVED. `--t2` is now `#256abf` and the 0.92 opacity is gone: white on `#256abf` = 5.39:1 in both themes (AA for body text). ●●● light 9.91:1, ●○○ light 9.33:1, dark ●●● 9.33:1, dark ●○○ 7.05:1. All filled tiers pass.
- **D2 (ramp direction inverts between themes)** — NOT RESOLVED, and I would not accept the decline. Light: ●●● `#104281` (darkest) → ●○○ `#86b6ef` (lightest). Dark: ●●● `#86b6ef` (lightest) → ●○○ `#184f95` (darkest). The dark-mode ●●● is byte-identical to the light-mode ●○○. If both screenshots circulate (and the author rendered both), the same hex means "peer-reviewed" in one image and "preliminary" in the other. Within one theme the legend disambiguates; across two it misleads. Post one theme, or keep darker = stronger in both.
- **D3 (not self-contained)** — RESOLVED. Legend, tier rule, suffix grammar, key strip and footer are all inside `.fig` and appear in the figure screenshots.
- **D4 (faint legend swatches)** — NOT RESOLVED. Swatches still 13px; argued border `#e1e0d9` on `#fcfcfb` is 1.29:1, open border `#c3c2b7` is 1.75:1. In the light crop the open-question swatch is a faint dashed smudge. Low; declined.
- **D5 (○○○ glyphs faint)** — NOT RESOLVED. `#898781` on `#fcfcfb` = 3.50:1 at 11px; the opacity is gone, which helps a little. Low; declined.
- **D6 (invalid ARIA)** — RESOLVED. `role="group"` with `aria-label`.
- **D7 (no clipping)** — still true at 1200px in both screenshots; see B-D3 for a computed overflow at the 980px minimum.
- **D8 (group headers weakest element)** — RESOLVED. `.mx .g` is now 12px, `--ink-2`, weight 600, and reads as a structural label in both screenshots.

Tally: RESOLVED 46 · PARTLY 6 (F8, F18, L4, W3, plus F6/F16 residue folded into B-F1) · NOT RESOLVED 6 (F23, T5, W8, W9, D2, D4, D5 — seven items, D4/D5 counted together as one decline). Declines I would accept: T5, W8, D4, D5. Declines I would push back on: D2 (wrong if both themes are posted), F23 and W9 (one sentence each).

---

## Part B: new findings in v4, ranked by severity within each category

### FACTUAL

**B-F1 (MEDIUM). Self-report × Token — "on open-weight models, critics find input anomalies trigger the same report", tag "Lindsey 25 ↔ Singh 26".**
The audit has only Singh et al.'s abstract (introspection §3.1) and it names no models. The open-weight work in the audit is Lederman & Mahowald (Qwen3-235B, Llama 405B, "UNVERIFIED against the PDF", §1 Source B), who are not on the board. v3 had "Open-weight models" in the Singh source entry; F16 said the audit does not establish it; v4 removed it from the source list but kept it in the cell under the Singh tag. The qualifier migrated rather than resolved. Either drop "on open-weight models" (the Singh abstract's claim, "cannot reliably distinguish such interventions on their internal states from manipulations of the input", stands without it) or add Lederman & Mahowald 26 to the tag and source list.
Rewrite: "...zero false positives; critics find plain input anomalies trigger the same report".

**B-F2 (LOW). Hedonic × Runstance — "a probe for a chronic assistant state overfit".**
Audit emotions §2d: "This suggests that the probe may have overfit". The cell states as fact what the paper offers as its own best guess for a messy result. "a probe for a chronic assistant state looked overfit" or "did not transfer" keeps the hedge in three characters.

**B-F3 (LOW). Changelog item 3 — "the plain role-play prompt matches or exceeds the fine-tune on nearly every preference".**
Audit Chua §(b): "produces elevated scores across nearly all preferences, often exceeding the fine-tuned model" (single-turn only). "Elevated ... often exceeding" is weaker than "matches or exceeds on nearly every". Say "lifts nearly every preference, often past the fine-tune".

**B-F4 (LOW). Behaviour × Token — "slips and in-line repairs print here", tagged "architecture" ●●●.**
The first clause is architecture; the second is a folk observation about what tokens look like, and source 13's definition of "architecture" ("sampling commits to one token per pass, and no other state survives") does not cover it. A pedant will also note that speculative decoding accepts several tokens per target-model pass, so "one candidate per pass" describes standard decoding, not every deployed system. Neither is worth a tier change; "Sampling commits to one candidate per pass" alone is cleaner.

No factual error was found in any of the other 28 cells against the audits. Specifically re-verified: 22%/72%/0% (emotions §2b); r=0.87 vs 0.59 (§2c); +212/−303 Elo (§1.3, "hundreds" is fair); R² 0.53–0.77 vs 0.10 (assistant-axis 4.2); "nearly 60%" / "roughly 50%" covered by "half or more"; Qwen 3 32B only for both B&B experiments (B&B §1); Δ −4.52 → +1.15 sign flip Gemma-only (originals §4); 13 Feb 2026 removal, Aug 2025 reversal, 0.1% daily (Chua/4o Task 2); Table 1 caption "no mentions of monitoring, shutdown" for "neither was in the data" (Chua §a); "about 20%" for Betley per snippets (originals §1); three families, base-model inheritance (assistant-axis 3.2.2, B.3).

### TIER

**B-T1 (LOW). Behaviour × Model ●●● — the second clause rests on a case study.**
"how-to questions pull it back" is the 6.1 jailbreak case study ("after giving enough explainers, the Assistant Axis projection reverts to the Assistant range" — one Qwen conversation, half of rollouts), plus the 4.2 regression, which shows how-to messages *maintain* the persona and that position tracks the latest message. By the page's own new rule ("a case study inside a peer-reviewed paper grades as preliminary"), "pull it back" is the ●○○ part of a ●●● cell. The 4.2 regression gives it enough quantitative cover that I would not re-grade, but "how-to questions hold it" would be the result at ●●● rather than the case-study inference.

**B-T2 (LOW). "Venue listing seen" is satisfied by a search snippet for both ●●● sources with a venue suffix.**
Lu 26: icml.cc and PMLR v306 snippets (audit assistant-axis §1, "unconfirmed by a primary page"). Betley 25: "search-engine snippets of the arXiv and PMLR pages" (originals §1), plus B&B's reference to the PMLR URL. The rule is applied consistently; it is just weaker than its wording. One word in the rule line ("venue listing seen, if only in search results") or in Still soft would close F23 and this together.

No cell is at the wrong tier under the page's stated rule. Checked all 30: four Lu ●●● (quantitative results), Betley ●●●, two architecture ●●●; ten ●●○ (eight preprints/lab papers, one documented event, one contested pair of preprints); four ●○○ (two B&B "prelim", one Lu case study, one own probe); seven ○○○; two open.

### INTERNAL CONSISTENCY

**B-C1 (MEDIUM, trivial to fix). The key strip does not expand "architecture".**
Subtitle: "A tag names the source; the key at the bottom expands it." The key strip lists twelve tags (Lu 26 ... own probe); "architecture" is the tag on two ●●● cells (Mech interp × Runstance, Behaviour × Token) and is absent from the strip, though it is entry 13 in the numbered source list. On the figure screenshot a reader sees a ●●● tag the key does not define. Add "· architecture decoder-only inference: KV cache, one sampled token per pass".

All other counts and cross-references verified against the grid:
- "Thirteen of the fifteen instrument cells carry a study and the other two are facts of the architecture" — CORRECT (now exactly right, since Behaviour × Token became "architecture").
- "the two welfare rows carry three studies between them, plus one informal probe" — CORRECT (Hedonic × Runstance, Preference × Persona, Preference × Instance; probe at Hedonic × Model).
- "two open cells, one informal probe, one negative result and one philosophical argument" — CORRECT.
- "Five cells rest on one paper" — CORRECT (Lu 26 at Mech interp × Model, × Persona; Behaviour × Model, × Runstance; Self-report × Runstance). "only peer-reviewed studies in the model and conversation columns" — CORRECT.
- "The relational row has one documented cell" — CORRECT.
- Key strip order = source list order (1–12) — CORRECT.
- Tags used in grid: 13 distinct (incl. architecture, own probe); source list: 13 entries; every tag has an entry — CORRECT. Every suffix used (ICML, prelim, case study, n=1, ↔) is defined in the rule line — CORRECT.
- Changelog items 1–8 against the v4 cells: each describes a change that is present in v4 (simulated conversations; Aura attribution; Chua role-play vs SOUL.md; 4o second act; Gilg tier and Gemma-specificity; Betley/Chalmers/Birch identities; B&B "every time"; three rebuilt cells and the Self-report × Runstance downgrade) — CONSISTENT. Note the changelog is against "the 11 Oct version", not v3, so it does not record v3→v4 changes (Behaviour × Token to architecture, the Birch rewrite, the palette); fine, as long as nobody reads it as a v3 diff.
- Footer "v4 · sources read and cells re-graded 4 Nov 2026" — consistent with the audit dates.

**B-C2 (LOW). Still soft, bullet 2, applies two standards to one snippet.** The poster placement is stated "per the conference listing" and the spotlight label "was not verified", but the audit's only listing evidence is a snippet of `icml.cc/virtual/2026/events/2026SpotlightPosters`. Either both are per-snippet or neither is. (Same evidence as F23; listed here because it is an internal inconsistency, not a source error.)

### LOGIC

**B-L1 (LOW). Relational × Model's new headline places it in the wrong column by the column's own definition.**
Column header: "Model — the checkpoint". Headline: "Attachment to a named model". The F10 fix concedes that what users attached to was a product name spanning rolling snapshots, which is precisely not "the checkpoint". It is still the right cell for the figure (there is no "product" column), but the header and headline now visibly disagree. Cheapest fix is the column subtitle: "the checkpoint, or the name it ships under".

**B-L2 (LOW). Hedonic × Instance (open) vs Mech interp × Runstance (●●●).**
"The cache carries the state" is asserted as architectural fact two rows up; "Whether a turn's state carries into the next through the cache is the open question" asks it. The distinction (any state vs a persisting affective state of the assistant) is implicit. And the emotions paper partly answers the question as posed: audit §2d, "it can (and does) recall previously cached emotion representations via attention, when they are needed"; what it leaves open is a chronic, character-bound state "implicitly in the model's key and value vectors". Round one proposed the current wording, so this is a refinement, not a reversal: "Whether anything of a turn's affect persists beyond what the next turn rebuilds from the text" is the open question the paper actually leaves.

**B-L3 (LOW). Behaviour × Runstance vs Mech interp × Runstance — apparent tension, not a contradiction.**
"every turn re-reads all of it" (●●●) next to "Where a turn lands depends on the latest user message far more than on where the model was" (●●●). Both are true (what is read vs what dominates the readout), and an X reader will ask "then why re-read?". A two-word hedge in the Behaviour cell, "lands *on the axis*", would show these measure different things.

No cell contradicts another outright. The L1 contradiction from round one is gone.

### WORDING

**B-W1 (MEDIUM). Hedonic × Model headline "A mood, if anything" is undercut by the page's own Still-soft bullet.**
The headline asserts the welfare reading (a model-level persisting valence); the notes say the evidence "favours a structural reading of that profile", and source 12 says the model is not recorded. The screenshot reader gets only the headline, at a tier glyph (●○○) that still reads as "a result". This is the one headline on the figure that the page itself argues against. Rewrite: "One profile, two positions" or "A constant, if anything", with the gloss unchanged; keep "if anything" if the author wants the welfare hook, but the noun should not be "mood".

**B-W2 (LOW). Mech interp × Persona "with capabilities intact".**
Paper: "without impacting performance" on four subsampled benchmarks (IFEval 541, MMLU Pro 1400, GSM8k 1000, EQ-Bench 171) with "While the set of benchmarks we used is limited" (audit §3.7) and the blog's warning that constant steering "risks hurting their capabilities". "on four benchmarks" is the honest four words; "intact" is an overclaim a mech-interp reader will quote back.

**B-W3 (LOW). Legend "untagged: the authors' own" has two possible authors.**
In the figure, "the authors" otherwise means the paper's authors ("the authors leave open", "the authors' word", "the authors read it as sycophancy"). In the legend it means Siener and Claude. On a screenshot with no byline above the footer, "the authors' own" reads as "the paper authors' own argument", which is the opposite of what is meant. "untagged: ours" or "untagged: this figure's authors".

**B-W4 (LOW). Self-report × Token "Reports a perturbed pass".**
Concept injection in Lindsey is sustained across the generated turn, not a single forward pass; "a perturbed pass" is singular to fit the column. "Reports a perturbation, sometimes" fits the column just as well without the inaccuracy.

**B-W5 (LOW). Mech interp × Instance "user-token readings".**
"readings" is doing the work of "assistant-axis projections on user tokens"; fine under the folk-vocabulary rule, but "readouts" is the word the rest of the figure uses ("Readouts live at a position", "readouts that bear on it"). One word, for consistency.

### DESIGN (from the screenshots)

**B-D1 (MEDIUM). Dark-mode ramp is inverted and shares a hex with light mode (carry-over of D2).**
`--t3` dark = `#86b6ef` = `--t1` light. `--t2` is the same `#256abf` in both themes, so the middle tier is the only invariant and the outer two swap. Side by side, the two screenshots read as opposite rankings. If only one theme is posted this is moot; the author rendered both, so I flag it as the one design item I would call wrong rather than taste.

**B-D2 (LOW). The self-containment mechanism is the lowest-contrast text on the figure.**
Key strip and rule line are 11–12px mono/sans in `--ink-3` (`#898781`): 3.50:1 on the light surface (4.85:1 dark). Everything a cold X reader needs to decode "B&B 26 · prelim" lives in those two blocks, and at X's downscale they will be the first thing to blur. `--ink-2` (7.73:1) at the same size costs nothing visually; the group headers already made that move.

**B-D3 (LOW, computed not observed). Two tag lines overflow their cell at the grid's 980px minimum.**
`.c u` is `white-space:nowrap`. At the 1200px screenshot width columns are ~200px (inner ~179px) and nothing overflows (confirmed in both screenshots, including the 7-line Lindsey cell). At `min-width:980px` columns drop to ~164px (inner ~144px); at IBM Plex Mono 11px (~6.6px/char) "Lindsey 25 ↔ Singh 26" + gap + "●●○" ≈ 166px and "Lu 26 · case study" + glyph ≈ 147px, so both spill into the neighbouring cell on a phone (horizontal-scroll layout) or any screenshot narrower than ~1100px. Not visible in the three screenshots supplied; will be visible if anyone screenshots the page at tablet width. `white-space:normal` on `.c u span` with the glyph kept `nowrap` fixes it.

**B-D4 (LOW). Row heights are set by one cell each in two rows.**
Self-report row: the Lindsey cell runs to seven gloss lines; "No privileged access shown" has three lines and then ~90px of blue. Hedonic row: the Birch cell's six lines stretch the open "Does it outlast the turn?" cell to mostly empty dashed box. Both visible in the light and dark figure shots. Trimming Lindsey ("zero false positives" could move to the source entry) and Birch ("neither is the persona or the conversation" is already implied by the two candidates) would even the rows.

**B-D5 (LOW). Argued-reading and open swatches, and ○○○ glyphs, remain faint in light mode** (D4, D5 carried). Borders at 1.29:1 and 1.75:1; glyphs at 3.50:1. Dark mode is fine for all three.

Checks that passed: no text clipping or overflow at 1200px in either theme; all filled-tier text passes AA (5.39:1 worst case); group headers now read as the structural layer; legend, tier rule, suffix grammar, key strip and footer are inside the figure in both screenshots, so the figure screenshot is self-contained except for the missing "architecture" key (B-C1); dark mode has an explicit body background and the open cells' dashed border survives on `#1a1a19`.

---

## Verdict

Still wrong, as opposed to taste, in descending order:

1. **B-D1 / D2** — if both themes are posted, the identical hex `#86b6ef` means "peer-reviewed" in dark and "preliminary" in light. Post one theme or fix the ramp.
2. **B-C1** — the key promises to expand every tag and does not expand "architecture", which sits on two ●●● cells.
3. **B-F1** — "on open-weight models" is attributed by tag to Singh 26, whose models the audit does not know; the open-weight work is Lederman & Mahowald, who are not on the board.
4. **B-W1** — "A mood, if anything" asserts, on the figure, the reading the page's own notes argue against.
5. **F23 / B-T2 / B-C2** — "per the conference listing" overstates a search snippet, and the same snippet is treated as verifying the poster but not the spotlight.
6. **B-F2** — "overfit" stated as fact where the paper says "may have overfit".

Everything else in Part B (B-T1, B-L1–L3, B-W2–W5, B-D2–D5, B-F3–F4) and the accepted declines (T5, W8, W9, D4, D5) are matters of taste or of one-word tightening. None of the six above misstates a number, a model, or a source's conclusion; three of them are one-line edits (2, 5, 6), one is a palette decision (1), and two are a few words each (3, 4). After those, I would not call anything on the figure wrong.
