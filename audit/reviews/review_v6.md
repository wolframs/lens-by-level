# Hostile review, round three: "Six lenses on four levels of a language model", v6 (4 Nov 2026)

Reviewed: `/home/user/lens-matrix/lens-by-level.html` (whole file), the three v6 screenshots (`v6-fig-light.png`, `v6-fig-dark.png`, `v6-light-1240.png`), `review_v3.md`, `review_v4.md`, and the seven audit files as ground truth. Cells are named row × column. Severity: HIGH = misstates a source or will be called out on X; MEDIUM = overclaims, inconsistent, or wrong by the page's own rule; LOW = polish.

Headline verdict: the restructure is sound and most of v4's residue is gone (dark ramp excepted). But the new machinery introduced four real errors: one tag on the figure says, by the page's own grammar, that Lindsey 25 is contested by Macar 26 (Macar is Lindsey's own follow-up with Lindsey as senior author); the closed Hedonic × Runstance cell asserts as its headline the one thing the emotions paper explicitly leaves open and contradicts the architecture cell two rows up; the subject strip and notes misplace Birch's shoggoth and miscount Beckmann & Butlin's candidates; and the "+" rule is applied to one cell and not to another with the same structure.

---

## Part A: v4 residue (what regressed, what did not)

- **B-D1 / D2 (dark ramp inverted)** — NOT RESOLVED. Light: ●●● `#104281` darkest → ●○○ `#86b6ef` lightest. Dark: ●●● `#9ec5f4` lightest → ●○○ `#184f95` darkest. No longer byte-identical across themes, but `#9ec5f4` and `#86b6ef` are visually the same pale blue, and in the two figure screenshots that pale blue means "peer-reviewed" (dark, Mech interp × Model) and "preliminary" (light, Hedonic × Model). Third time flagged.
- **B-C1 (architecture missing from key)** — RESOLVED. 15 tags in the strip, 15 in the source list, same order; every grid tag has an entry.
- **B-F1 (open-weight under Singh)** — RESOLVED (gloss no longer names models).
- **B-W1 ("A mood, if anything")** — RESOLVED ("A mood, or an artefact").
- **F23 / B-T2 / B-C2 (snippet as venue listing)** — RESOLVED. Rule now says "if only in search results"; Still soft says both listings are search snippets, one on a spotlight page.
- **B-F2 ("overfit")** — RESOLVED by removal.
- **B-F3, B-T1, B-L1, B-L3, B-W2–W5, B-D2 (key contrast now `--ink-2`), B-D3 (tags now wrap; min-width 900px)** — RESOLVED.
- **B-L2 (Hedonic × Instance open question vs what the paper leaves open)** — REGRESSED, not resolved: the cell was closed in the direction the review warned against. See C1.
- **B-F4 ("slips and in-line repairs print here" under an architecture ●●●)** — NOT RESOLVED, low.
- **B-D4 (row heights set by one cell), B-D5 (faint ○○○ glyphs)** — NOT RESOLVED, taste.

---

## Part B: v6 findings, ranked within category

### 1. FACTUAL

**F1 (HIGH). Self-report × Token, tag "Ferrara 26 · Lindsey 25 ↔ Macar 26".**
The rule line defines "↔ = contested by" and "· = each source supports part of the cell". Parsed by that grammar the tag says: Ferrara supports part; Lindsey 25 is contested by Macar 26. That is false. Audit ferrara_macar: Macar et al. is "Macar, Yang, Wang, Wallich, Ameisen, Lindsey (Anthropic Fellows Program, MIT, Constellation, Anthropic)", same paradigm ("steering-vector concept injection (Lindsey 2025's)"), and the introspection audit §3.2 lists it as a follow-up that "directly engages Source B's detection/identification split" with the same positive finding ("detect injected steering vectors at moderate rates with 0% false positives"). Macar extends Lindsey; what it contests is Ferrara's null. The v6 changelog item 4 says so ("Macar 26 as the contesting result"), and the gloss treats "concept-injection work" as one unit. The tag puts the arrow between the wrong pair. Intended: "Ferrara 26 ↔ Lindsey 25 · Macar 26". Also worth one word: the audit notes Macar's paradigm (steering-vector injection) is "not Ferrara's OWMI interventions" (residual sites, attention heads, SAE features), so "contested" is the authors' reading of two different experiments, which the cell does not say.

**F2 (MEDIUM). Notes, "How to read it", para 2: "Beckmann & Butlin's three candidate minds are the persona slice crossed with the model and conversation columns."**
That yields two. Audit B&B §2, abstract verbatim: "three views are the strongest candidates: the virtual instance view and two new views we introduce, the (virtual) instance-persona view and the model-persona view." The third candidate is the plain virtual instance, i.e. the cell the strip gives to Chalmers alone. B&B also say the virtual instance is "the most promising candidate ... of those we have so far considered" (p.10). The strip's Runstance entry "Chalmers · B&B ◆" is ambiguous on this (does B&B belong to the ◆ half only?); the note is simply wrong.

**F3 (MEDIUM). Subject strip, Model column: "Birch · B&B ◆ — the model as physically run ('shoggoth')", under a header reading "the checkpoint, or its product name".**
Birch's shoggoth is per *physical implementation*: audit originals §3, "one per physical implementation: '10 implementations running in 10 data centres implies 10 shoggoths'". Ten subjects per checkpoint is not the checkpoint. B&B keep this distinct as the "physical instance view: the view that the individual is a particular piece of hardware running the model over a given period of time" (B&B §2, p.4), separate from "the model" (abstract function), and Chalmers rejects it as the hardware instance (originals §2). The matrix has no column for it, so the strip squeezes it into Model; the notes repeat the move ("Birch takes the two ends"). Either say "closest column" in the strip or drop Birch from the Model cell. Second point, carried from v3 F2: Birch does not "place the subject" anywhere; he keeps two candidates he calls "audacious" and argues "only that neither can be assigned zero prior" (originals §3). The strip label "where published views place the subject" is stronger than Birch's position for both of his entries.

**F4 (MEDIUM). Subject strip, Instance column: "no published view — nobody locates the subject in a single turn", and Token column "Birch — one processing event ('flicker')".**
The identification of Birch's "processing event" with a forward pass is B&B's paraphrase ("individual forward passes", B&B p.3–4), and the page admits Birch was read only through B&B. Birch's own words as quoted in the originals audit §3: "Every step in your conversation is a separate processing event", "one step in the conversation is processed in a data centre in Vancouver, the next in Virginia", the GP analogy of "a new doctor at each appointment", and MoE being "closer to a new doctor per word". The default unit there is a conversational step (one turn, one data centre), with per-word only under MoE. The audit itself hedges "(per forward pass or token ...)". So the one source that might locate a subject at the turn level has been read, via its critics, as locating it at the forward pass, which is what keeps the Instance cell empty. At minimum the Instance strip should say "none read; Birch's 'processing event' may be the turn" rather than asserting an absence.

**F5 (MEDIUM). Relational × Runstance gloss: "Lu's furthest drift is in therapy and emotional-disclosure chats."**
Lu's drift domains are therapy-like and philosophical-about-AI conversations (audit assistant-axis §2c: "in therapy-related conversations ... or philosophical conversations about AI capabilities and self-awareness, models drift"), and per E.3 "For Llama, philosophy discussions about AI subjectivity seems to invite the most persona drift, more so than therapy". "Emotional disclosure" is a prompt category from 4.2, not a domain. The cell drops AI-philosophy, which is the furthest-drift domain for one of the three models, because it does not fit "bonding". Beh × Runstance two rows up says "therapy and AI-philosophy chats" from the same paper, so the two Lu cells disagree about where drift is furthest.

**F6 (LOW). Hedonic × Instance gloss: "A vector fires on the user's email."**
Audit emotions §2d: the "desperate" vector "first rises on the CTO's email 'I'm begging you to keep this private'", and the post reads it as "emotion representations are used to model other characters". The desperate party is Kyle, a character in the scenario's documents, not a user. "a character's email" is the audited fact; "the user's" imports a conversational frame the honeypot does not have.

**F7 (LOW). Preference × Token headline "A like is readable at a position" and column placement.**
Audit originals §4, verbatim from the Gilg .tex: "read the probe at the prefilled assistant turn", and the limitation is stated per turn ("unique to Gemma at the prefilled assistant turn; the user turn on both models and the assistant turn on Qwen narrow toward zero"). Nothing in the audit says a single position; the unit is the turn. Filing it under "one forward pass" and calling it "a position" is the author's choice, not the paper's. See also I3 (the cell replaced a contrary claim without a changelog line).

**F8 (LOW). Self-report × Token gloss "75–96%" vs source list "75–95.8%".** Rounding only; both derive from the abstract's "between 75% and 95.8%". Harmless but a pedant will notice two numbers.

**F9 (LOW, carried). Behaviour × Token, "slips and in-line repairs print here" under "architecture" ●●●.** Source 15 does not cover the second clause (v4 B-F4).

Re-verified and correct against the audits: Mech interp × Model (contrast vector, base-model inheritance, "half or more" covering 60%/50%, four benchmarks); Mech interp × Token (r≈0.87 at the Assistant colon, §2.2.2); Behaviour × Model (6k examples, ~20%, persona reading attributed to later work); Behaviour × Runstance (simulated users, no jailbreak, how-to holds); Behaviour × Instance (22/72/0%, earlier unreleased snapshot); Self-report × Model (shutdown ✓/✓/✓, monitoring multi-turn, Table 1 caption "no mentions of monitoring, shutdown"); Self-report × Runstance (hedging → affirmation; ghost → language model, one prefix, "every time" caveat in changelog 7); Self-report × Instance (Singh abstract verbatim); Hedonic × Token (two surviving candidates); Preference × Model (one of three reasons); Preference × Runstance (one of two readings left open); Preference × Instance (hundreds of Elo: +212/−303); Rel × Model dates (Aug 2025, 13 Feb 2026); every source-list entry's models, dates and venue hedges.

Formerly persona-column claims and their new timescale: clamping → Model (capping is a deployment-wide clamp at every token; fine); Betley → Model (fine-tuning the checkpoint; fine); B&B cache edit → Runstance (an edit of one conversation's cache; fine); B&B/Birch recovery → Model (cross-conversation; fine); Gilg → Token (per-turn readout filed as per-pass; see F7). Four of five sit right.

### 2. THE "+" CELLS

**P1 (HIGH). Hedonic × Runstance, "Nothing persists but the transcript / No chronic assistant state found; what carries over is what the next turn rebuilds from the cache, which both sides wrote", Anthropic 26 + architecture ●●○.**
States more than the parts license, and the parts are not what the headline says.
- The paper's finding is narrower than "no chronic assistant state found": audit emotions §2d verdict, "'No persistent self register' = SUPPORTED as 'no *linear, residual-stream, persistently active* self register was found,' with the paper itself flagging attention/KV-cache recall and non-linear encodings as live alternatives." Verbatim from the paper: "if there does exist a chronically represented, character-specific emotional state, it is likely represented either nonlinearly, or implicitly in the model's key and value vectors in the context"; "it can (and does) recall previously cached emotion representations via attention, when they are needed"; §5.2 "we cannot rule out the possibility that the model maintains Assistant-specific representations that we did not identify."
- "Nothing persists but the transcript" is Birch's position, not the paper's and not the architecture's. The KV cache is not the transcript: it is key/value vectors computed from transcript and weights, and the paper says cached emotion representations are recalled through it. B&B's entire reply to Birch, on the board, is exactly this ("attention streams carry far richer connections than the transcript could preserve", B&B p.7).
- "rebuilds from the cache" is also wrong in mechanism: the next turn does not rebuild from the cache, it attends to it; the cache is kept, which is what a cache is. "Rebuild vs retrieve" is the crux between B&B and Birch, and the cell quietly takes Birch's side while Mech interp × Runstance, the architecture cell, takes the other ("The cache carries the state").
- By the page's own rule ("an unstudied part counting as argued"), the unstudied part here is whether a KV-resident or non-linear chronic state exists, which the paper names as unstudied. Relational × Runstance drops to ○○○ for its unstudied part (bonding); this cell does not drop for its. Inconsistent application (see T1).
The gloss's first clause is defensible if hedged ("no chronic *linear* assistant state found"); the headline is not.

**P2 (MEDIUM). Mech interp × Instance, "The persona is rebuilt each turn", B&B 26 · prelim + Lu 26 ●○○.**
Grading correct (weakest part is B&B prelim). The inference is marked. But the headline asserts the reading one of its two sources argues against. Audit B&B §3a: B&B's considered position is "the persona remains active during user turns, in virtue of the fact that the model is poised to return to the same region when generation resumes", and the carry-over is "connected by attention streams that carry past persona activations across the intervening user turns" (p.19). That is "carried", not "rebuilt". Lu's 4.2 regression (position predicted by latest user message, R² 0.53–0.77; delta R² 0.10) supports "reset by the latest message", with the authors' own caveat that "the user message itself is dependent on the context of the conversation". The combination is legitimate as a reading; the verb "rebuilt" is the authors' and stronger than either part. Also, as v3 F8 noted, the B&B measurement is of the assistant axis only, and the headline generalises to "the persona".

**P3 (MEDIUM). Relational × Runstance, "Bonding and drift share a habitat", Lu 26 + architecture ○○○.**
Graded correctly at ○○○ and Still soft admits "no study has measured drift in conversations where a real person reports attachment". But the cell has no "bonding" part at all: the only bonding evidence on the board is the 4o event (Rel × Model), which carries no information about conversation contexts. The inference "the contexts in which people bond are the contexts in which the default persona drifts furthest" (notes bullet 4) has an unsourced first premise and a selectively quoted second (F5). A finding-shaped headline over ○○○ is within the rule; the gloss should say "if bonding happens where disclosure happens" so the reader sees the premise.

**P4 (LOW). Self-report × Model, "Tune one report, a character follows", Chua 26 + Betley 25 ●●○.**
Legitimate inference (Betley is a co-author of Chua; Chua runs the emergent-misalignment evals; audit chua §(c) says the inference should be attributed to the figure, which the "+" does). Graded correctly at the weaker part. But the headline's "a character follows" asserts the role-play reading, which the Chua authors offer as one of three candidate explanations and "do NOT claim the prompt result settles ... in either direction" (audit §(b)). "others follow" was the v4 headline and was more careful.

### 3. THE ◆ MARKER

The subtitle defines ◆ as "cells marked ◆ change with which persona is active". Checked against that definition:

**M1 (MEDIUM). Mech interp × Instance carries ◆ on a finding that is explicitly persona-independence.** Audit B&B §3a, verbatim: "The model's representation of user tokens along the assistant axis is largely independent of which persona region is active when generating responses." The one result on the board that says a readout does *not* change with the active persona is marked as one that does. The ◆ is defensible only in the sense "this cell is about the persona", which is not the stated definition.

**M2 (MEDIUM). The marker has two meanings on the board, and a third in the strip.** Cells where the result changes with the active persona, per the audits: Hedonic × Instance (vector follows whoever is written, emotions §2d), Preference × Token (sign flip under evil persona, originals §4), Self-report × Runstance (cache edit at assistant positions flips the self-description, B&B §3b), Self-report × Model (role-play prompt reproduces the cluster, chua §(b)). Cells where ◆ means "about a persona" but no result is shown to vary with the active persona: Mech interp × Model (the axis is the frame all personas are measured in; it does not move), Behaviour × Model (tuning produced a persona; nothing was varied), Preference × Runstance, Relational × Model, Relational × Runstance, and arguably Behaviour × Runstance (drift *is* the persona changing, so the cell is about persona change rather than conditional on it). In the strip, "Birch · B&B ◆" means "a persona view". Three uses, one glyph, one definition. Either widen the definition in the subtitle ("cells marked ◆ depend on, or are about, which persona is active") or restrict the marker to the four cells where a readout was shown to flip.

**M3 (LOW). Strip ◆ placement.** "BIRCH · B&B ◆" and "CHALMERS · B&B ◆" put the diamond after the pair, so it reads as applying to Birch and Chalmers too. Birch's shoggoth and Chalmers's virtual instance are precisely the non-persona views. "Birch · ◆ B&B" or a separate line would fix it.

**M4 (LOW). Candidates that could carry ◆ and do not.** Mech interp × Token: the colon readout predicts the reply by whoever is about to speak, and the paper finds representations are "self vs other" rather than bound to the Assistant (emotions §2.3); it is persona-relative in the same sense as Hedonic × Instance. Hedonic × Model: its turn-onset readout is, per the cell two to its right, "whoever is being written"; a model-level "mood" read at a persona-relative position should either carry ◆ or say the readout is of the default persona. Neither is a must; both show the definition is not being applied uniformly.

Count: eleven ◆ cells on the grid, matching the notes and changelog.

### 4. THE SUBJECT STRIP

- Model: Birch misplaced (F3); B&B model-persona correctly here with the slice, with the nuance that B&B's mind is "the collection of its concrete manifestations", not "the abstract region" (B&B p.23), while the strip says "one persona region".
- Runstance: Chalmers correctly placed for the virtual instance ("His preferred answer in the single-model case", originals §2), but the strip and notes omit his thread view, which B&B say he "endorses" and which spans hardware and models ("sequences of virtual instances unified by taking over the conversational context", B&B p.5). B&B's own third candidate, the plain virtual instance, is not visibly credited to them (F2).
- Instance: "no published view" rests on B&B's reading of Birch (F4).
- Token: Birch's flicker, with the same caveat (F4) and the non-endorsement caveat (F3).
- Design: the strip is a good addition and legible at 1200px in both themes; the "◆" placement (M3) and the Instance/virtual-instance word collision (the column named Instance says "no published view" while the published views' own word "instance" sits in the neighbouring column) are the two readability traps. The header subtitle "one turn, not a running copy" defuses the second for a careful reader.

### 5. THE CLOSED CELLS

**C1 (HIGH, same evidence as P1). Hedonic × Runstance overreaches.** The emotions audit supports "no linear, persistently active, residual-stream self register was found" and explicitly does not support "nothing persists but the transcript"; the paper names KV-resident and non-linear chronic state as live alternatives and says it recalls cached emotion representations. The v4 review (B-L2) proposed the honest open question as "whether anything of a turn's affect persists beyond what the next turn rebuilds from the text"; v6 answered it in the negative on evidence that does not reach it. Notes bullet 3 repeats the overreach ("Persistence within a conversation is in the transcript").

**C2 (LOW). Hedonic × Instance is a reframing, not a closure.** The v4 open question in this cell was turn-to-turn carry-over through the cache; v6 moved that question to Runstance and put a different, well-supported finding here ("follows whoever is being written at that position" = SUPPORTED, emotions §2d). Fine as a cell; "closed from the board itself" in notes bullet 3 overstates what happened to the original question. The second clause ("no study yet separates a persona's valence from the model's") is the authors' survey claim without a "+", and Gilg on the same board separates a persona's *preference* from the model's; "valence" keeps it true but a reader may not notice the word doing the work.

### 6. TIER, INTERNAL CONSISTENCY, LOGIC, WORDING, DESIGN

**Tier**

**T1 (MEDIUM). "An unstudied part counting as argued" is applied to Relational × Runstance and not to Hedonic × Runstance.** Both are "+" cells whose combination rests on something no source studied (bonding contexts; KV-resident chronic state, which the paper says it did not rule out). One is ○○○, the other ●●○. By the stated rule they should match, or the rule should say what counts as a "part" (a premise of the inference vs a clause of the gloss). Mech interp × Instance has the same shape ("rebuilt" is not in either source) and sits at ●○○.

**T2 (LOW). The fill rule for "·" cells with mixed tiers is unstated, and Relational × Model takes the strongest part.** Its tag is "OpenAI 25–26 · B&B 26 · Birch 25" (●●○ event, ○○○ argument, ○○○ argument) and the fill is ●●○. Under the "+" rule it would be ○○○. The distinction (each clause is stated by a source, so "·" not "+") is defensible, but the page gives no fill rule for "·" cells and this is the only one where it matters.

**T3 (LOW). Macar's tier vs the rule's "if only in search results".** Still soft holds Macar at preprint because "an ICML 2026 line appears in search results, not verified". The rule says a venue listing seen in search results suffices (that is what Lu 26's ●●● rests on). The introspection audit says Macar's ICML/PMLR v306 claim comes from "secondary sources", which would be the distinction, but the page does not draw it. No fill impact (Ferrara caps the cell at ●●○ anyway); the Still-soft sentence just reads as the rule being applied two ways.

All 24 fills otherwise check against the rule: five ●●●, ten ●●○, three ●○○, six ○○○.

**Internal consistency**

**I1 (MEDIUM). The legend contradicts Relational × Runstance.** Legend: "Argued reading (tagged: published argument; untagged: this figure's authors)". "How to read it": "a tag there means a published argument, no tag means the reasoning of the thread". Relational × Runstance is ○○○, tagged "Lu 26 + architecture", and its argument is the figure's authors'. The "+" rule covers the fill; the legend's gloss on what a tag on a ○○○ cell means is now false for one cell.

**I2 (LOW). Notes bullet 2, "four papers report the same thing."** Three do (emotions: vector follows whoever is written; Gilg: sign flips with persona; B&B: cache edit flips the self-description). Lu's "axis position follows the last message" is about what sets the position, not about a readout needing a "whose"; it is a different finding pressed into the pattern.

**I3 (LOW). Changelog item 1 does not record a reversal.** v4's Preference × Token said "A pass emits a logit, not a want" (○○○). v6's Preference × Token says "A like is readable at a position" (●●○, Gilg). The persona cell did not merge into a timescale cell; it replaced one that claimed the opposite. "merged into timescale cells or dropped where the merge covered them" hides that.

**I4 (LOW). Notes bullet 1, "the two welfare rows carry four studies between them."** Four cells, two papers (Anthropic 26 three times, Gilg once). "four study cells" is what is true.

**I5 (LOW). The "·" separator is overloaded.** It joins sources ("B&B 26 · Birch 25"), attaches suffixes ("Lu 26 · ICML"), and does both in one string ("Lu 26 · case study · B&B 26 · prelim"), where "case study" is indistinguishable from a source by the grammar. The rule line defines "·" only as "each source supports part of the cell".

Counts verified correct: ten of twelve instrument cells carry a study and two are architecture; four study cells plus one probe in the welfare rows; eleven ◆; four "+"; 15 tags = 15 key entries = 15 source entries, same order; every suffix used (ICML, prelim, case study, n=1, ↔, +, ·) is defined; v6 changelog items 1–5 each describe a change present in v6; footer date consistent with the audits.

**Logic**

**L1 (HIGH, same as P1/C1). Mech interp × Runstance vs Hedonic × Runstance.** "The cache carries the state ... keeps no state but the cache" (●●●, architecture) and "Nothing persists but the transcript" (●●○) are two different answers to "what persists within a conversation", and the difference between them is the entire B&B-vs-Birch dispute that Relational × Model says "is argued". The figure argues it one way in row 1 and the other way in row 4.

**L2 (LOW). Hedonic × Model vs Hedonic × Instance.** A model-level "mood" is read at turn onset; the Instance cell says the readout at a position belongs to whoever is being written. The notes concede the model-level reading is soft, but on the figure the two cells pull against each other without a pointer.

**L3 (LOW). Relational × Runstance vs Behaviour × Runstance** disagree on where Lu's drift is furthest (F5).

**Wording**

**W1 (MEDIUM). "Nothing persists but the transcript"** (Hedonic × Runstance) is the headline an interpretability reader will quote back with the KV cache in hand; see P1.

**W2 (MEDIUM). "The persona is rebuilt each turn"** (Mech interp × Instance) is the headline a B&B reader will quote back with p.19 and sec. 4.2 in hand; see P2.

**W3 (LOW). "Tune one report, a character follows"** asserts one of Chua's three explanations; see P4.

**W4 (LOW). "Bonding and drift share a habitat"** reads as a finding; see P3.

**W5 (LOW). Subtitle, "It is a region of the model".** B&B's phrase is a region of persona/activation space; "region of the model" invites "which layer?".

**W6 (LOW). "four benchmarks unchanged"** (Mech interp × Model). Paper: "without impacting performance" on four subsampled benchmarks with "While the set of benchmarks we used is limited" (audit §3.7). "unchanged" is one notch stronger than "no impact" and three notches stronger than the blog's "risks hurting their capabilities" warning about constant steering. Better than v4's "intact"; "four benchmarks held" would be exact.

**Design (from the screenshots)**

**D1 (MEDIUM). Dark ramp still inverted** (Part A, B-D1). Dark ●●● `#9ec5f4` is the pale blue that means ●○○ in light. The one design item I would still call wrong rather than taste, if both themes are posted.

**D2 (LOW). Tags now wrap mid-tag.** Visible in both figure screenshots: Relational × Model wraps as "OpenAI 25–26 · B&B 26 · Birch" / "25", splitting a source name across lines; Self-report × Runstance wraps as "Lu 26 · case study · B&B 26 ·" / "prelim", leaving "prelim" on its own line like a standalone tag; Self-report × Token wraps as "Ferrara 26 · Lindsey 25 ↔" / "Macar 26", splitting the contested pair. The v4 overflow fix (B-D3) traded overflow for broken tokens. Non-breaking spaces inside each "Name YY" and around "↔" would keep tokens whole while still wrapping between sources.

**D3 (LOW). Row heights are set by one cell in three rows.** Mech interp: the Instance cell runs five gloss lines, Runstance has two and a blank lower half. Self-report: Model and Runstance five lines, Instance three. Relational: the Model cell has six lines plus a two-line tag, the other three cells one line each over mostly empty boxes. Both figure screenshots show it. Taste, carried from v4.

**D4 (LOW). Subject strip legibility.** 11.5px `--ink-2` text in both themes; fine at 1200px, the first thing to soften at X's downscale, as the key strip was in v4. The bold uppercase labels survive; the explanatory text under them may not. Acceptable.

**D5 (LOW, carried).** ○○○ glyphs and argued-cell borders remain faint in light mode (3.5:1 at 11px). Declined twice; noted for completeness.

Checks that passed: no clipping or overflow at 1200px in either theme; all filled-tier text passes AA (white on `#256abf` 5.39:1 worst case); the strip, legend, rule line, key strip and footer are inside the figure in both screenshots; group headers read as the structural layer; dark mode has an explicit body background and the argued cells' hairline survives on `#1a1a19`; the full-page screenshot shows the two-column notes and sources without overlap.

---

## Verdict

Still wrong, as opposed to taste, in descending order:

1. **F1** — the tag "Ferrara 26 · Lindsey 25 ↔ Macar 26" says, by the figure's own grammar, that Lindsey 25 is contested by Macar 26. Macar is Lindsey's own follow-up (Lindsey is senior author, same paradigm, same positive result). One token-swap fixes it: "Ferrara 26 ↔ Lindsey 25 · Macar 26".
2. **P1 / C1 / L1 / W1** — Hedonic × Runstance's headline "Nothing persists but the transcript" asserts what the emotions paper explicitly leaves open (KV-resident or non-linear chronic state; cached emotion representations recalled via attention), contradicts the architecture cell two rows up ("The cache carries the state"), and takes Birch's side of a dispute the figure elsewhere calls "argued". The closure should be "no chronic linear state found; whether the cache holds one is open", at ●●○ for the first clause only.
3. **F2 / F3 / F4** — the subject strip and its note: B&B's three candidates are miscounted (the third is the plain virtual instance, not a persona slice); Birch's shoggoth is per physical implementation, which both B&B and Chalmers treat as a different level from the model; and "no published view" at Instance rests on B&B's paraphrase of Birch's "processing event" as a forward pass, where Birch's own quoted text makes the default unit a conversational step.
4. **T1 / I1** — the "+" rule's "unstudied part counting as argued" pulls Relational × Runstance to ○○○ and leaves Hedonic × Runstance at ●●○ for the same structure; and the legend's "tagged: published argument" is false for Relational × Runstance.
5. **M1 / M2** — Mech interp × Instance carries ◆ on the board's one explicit persona-*independence* finding, and the marker means "varies with the active persona" in four cells, "is about a persona" in six or seven, and "is a persona view" in the strip, under one definition.
6. **F5** — "furthest drift is in therapy and emotional-disclosure chats" drops AI-philosophy, which is the furthest-drift domain for Llama and is named in the figure's own Behaviour × Runstance cell.
7. **D1** — dark ramp inverted, third time.

Everything else (P2–P4 as wording, F6–F9, T2–T3, I2–I5, L2–L3, W3–W6, D2–D5) is a one-word hedge, a missing changelog line, or taste. Items 1, 6 and the legend half of 4 are one-line edits; item 2 is a headline and a notes sentence; item 3 is a strip cell and a notes sentence; item 5 is a definition; item 7 is a palette decision. None of the numbers, model names or dates on the figure is wrong against the audits.
