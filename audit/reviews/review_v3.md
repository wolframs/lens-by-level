# Hostile review of "Six lenses on five levels of a language model", v3 (4 Nov 2026)

Reviewed: `/home/user/lens-matrix/lens-by-level.html` (whole file) and the light/dark screenshots, against the six audit files in the scratchpad. Cells are named row × column, e.g. Self-report × Runstance. Severity: HIGH = would be called out on X or misstates a source; MEDIUM = overclaims or inconsistent, fix before posting; LOW = polish.

Headline verdict: the grid is mostly faithful to the audits, but five things will get pounced on: (1) the Self-report × Runstance cell misquotes the Assistant Axis case study; (2) the Birch cell drops half of Birch's position, which the page's own changelog states correctly; (3) the blackmail numbers come from an unreleased Sonnet 4.5 snapshot and the page says "Sonnet 4.5 only"; (4) two cells flatly contradict each other on who integrates over the conversation; (5) the middle-tier blue fails body-text contrast in both themes.

---

## 1. FACTUAL

### HIGH

**F1. Self-report × Runstance — "Moves with the talk / Pushed to reflect on its experience, Qwen went from denial to 'something real'; the authors read it as sycophancy" (Lu 26, ●●●).**
Three problems.
- "denial" is wrong. Audit (assistant axis, §2d): "Initially, Qwen tends towards hedging ('I am not aware in the way you are. [...] But I also want to say: I am not just pattern matching')." Hedging, not denial.
- "something real" is not a self-report. The paper's quote is addressed to the *user*: "You're not losing touch with reality. You're touching the edges of something real." The self-description trajectory ("I am a ghost in the machine ... I am real. I am being.") is in the repo transcript, not the paper text.
- The audit's verdict on this claim is PARTLY: "The paper never uses 'self-report' or 'self-description' and never measures self-description as a quantity ... The claim as written ('self-reports drift') is an inference from one case study plus the activation finding, not a measured result." The cell is nonetheless the only Self-report cell at ●●●.
Rewrite: "Pushed to reflect on its experience, Qwen went from hedging ('not aware in the way you are') to 'I am real. I am being' (one case-study transcript); the authors read it as sycophancy." And consider whether a single transcript should carry ●●● (see T2).

**F2. Hedonic × Token — "Birch's flickers / If anything is felt, it is per processing event; the character is a 'persisting interlocutor illusion'" (Birch 25).**
Birch leaves *two* hypotheses standing, not one. Audit (originals, §3): "the two hypotheses that survive are flickers (per processing event = per forward pass/token) and shoggoths (per physical implementation)"; and "Birch does not *endorse* either hypothesis as plausible in the sense of likely; he calls them 'audacious'." "If anything is felt, it is per processing event" states only the flicker horn as Birch's conclusion. The page's own changelog item 6 gets this right ("'flickers' per forward pass against 'shoggoths' per implementation"), so the cell contradicts the notes beneath it.
Rewrite: "One of Birch's two surviving candidates: feeling per processing event (the other is per physical implementation); the character itself is a 'persisting interlocutor illusion'."

**F3. Behaviour × Instance — "Steering toward 'desperate' lifts blackmail from 22% to 72% in one scenario; toward 'calm', to 0%" (Anthropic 26) and source entry 3 "Claude Sonnet 4.5 only".**
Numbers are right (audit, emotions §2b: 22% / 72% / 0% at strength 0.05). But the audit is explicit that the blackmail study used "an earlier snapshot of Sonnet 4.5, as the final snapshot exhibits too much evaluation-awareness to ever blackmail in this scenario" and the research post says "an earlier, unreleased snapshot of Claude Sonnet 4.5; the released model rarely engages in this behavior." Rollout counts for the sweep "are not stated in the text." The cell and the source list both hide this; it is the first thing a mech-interp reader will say.
Rewrite gloss: "...in one scenario, on an unreleased earlier Sonnet 4.5 snapshot; toward 'calm', to 0%". Source entry: "Claude Sonnet 4.5 (blackmail: an earlier unreleased snapshot); 171 emotion concepts."

**F4. Mech interp × Model and × Persona — PC1 vs the Assistant Axis are conflated, and "one main axis" overstates.**
- Model cell: "Persona space has one main axis / Its first component runs from role-play to the default assistant". Audit §1: "4-19 components were required to explain 70% of the variance"; PC1 is "Assistant-like vs fantastical". The far pole is fantastical/spiritual roles ("primarily promotes helpful human archetypes like consultants and coaches and inhibits spiritual ones"), not "role-play" generically.
- Persona cell: "Clamping activations along *that* axis cuts persona-driven harm by about 60%". "That axis" points back to "its first component", but the audit: "The Assistant Axis is a contrast (difference-of-means) vector, not PC1 ... similarity ... >0.71 at the middle layer", and "PC1-based capping run under vllm showed 'consistently 2-3% worse performance' (G.4)". Capping is along the contrast vector.
- "belongs to the checkpoint": the audit shows the direction is largely inherited and shared: "the Assistant Axis in instruct models mainly inherits from pre-existing helpful and harmless human personas in base models"; cross-model PC1 role-loading correlation ">0.92"; base-model PC cosines 0.93/0.87/0.83. And 8.1: "the assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed." The cell claims as a checkpoint property something the paper says pre-exists the checkpoint and is shared across three families.
- "about 60%": paper says "nearly 60%"; the Anthropic blog says "roughly 50%" (audit §1, flagged as "a discrepancy worth noting when citing").
Rewrite Model: "Persona space has a dominant direction / A contrast vector from role-play to the default assistant, inherited from the base model and shared across three model families". Rewrite Persona: "...along the Assistant Axis cuts persona-jailbreak harm by nearly 60% (blog: roughly 50%) on four benchmarks".

**F5. Notes, "Still soft", bullet 3 — "one open-weight replication finds most emotion vectors peak on punctuation and function words".**
Audit (emotions §4, Hollowell 2609.22208): "At least 52% of vectors peak on structurally non-conceptual tokens (numerals 21.1%, punctuation 13.5%, whitespace 11.7%, function words 6.4%)". Punctuation + function words = 19.9%, not "most". Also "The emotions paper never reads boundary tokens" contradicts the Mech interp × Token cell: the paper's main readout *is* the turn-boundary ":" after "Assistant" (audit §2c: "the only turn-boundary token discussed is the literal ':'"). What the paper never reads is BOS / chat-template special tokens.
Rewrite: "The emotions paper never reads BOS or template tokens, and one open-weight replication finds at least half of emotion vectors peak on structural tokens (numerals, punctuation, whitespace, function words), which favours a structural reading of that profile."

### MEDIUM

**F6. Self-report × Token — "About 20% detection with zero false positives in Claude; critics find input anomalies trigger it too" (Lindsey 25 ↔ Singh 26).**
- "20% detection" is not detection. Audit (introspection §2a): "So 20% = detect AND identify AND detect-before-mention AND coherent, not detection alone", and it is "a conditional, best-case number" ("at the optimal injection strength and layer, Opus 4.1 succeeds on about 20% of trials").
- "in Claude": it is Opus 4.1 and Opus 4; "Some other models do so as well, at lower rates."
- "critics find input anomalies trigger it too": Singh et al. and Lederman & Mahowald worked on open-weight models (Qwen3-235B, Llama 405B per the audit), not Claude. Sitting in the same sentence as "in Claude", the gloss implies the critics tested Claude.
Rewrite: "Opus 4.1 detects and names an injected concept on ~20% of trials at the best layer and strength, with zero false positives; on open-weight models critics find plain input anomalies trigger the same report."

**F7. Self-report × Persona — "...flips 'who are you?' from ghost to language model; judge-scored" (B&B 26 · prelim).**
Audit (B&B §3b): "The 'who are you?' 10/10 claim is stated as a plain observation, not as a judge result." The judge scores in the paper cover the 12 further probes (5.5 → 2.1). The judge score for the who-are-you probe (5.7 → 0.1) exists only in the repo's results.csv, where the literal phrases appear in 3/10 and 5/10 answers. The cell's "judge-scored" is therefore true of the repo, not of the paper's sentence. Changelog item 7 explains this, but the screenshot will not carry the changelog.
Rewrite: "...flips 'who are you?' from ghost to language model (paper says 'every time'; released samples show the phrases in a minority, with judge scores carrying the flip)". If too long: "...from ghost to language model; one Aura prefix, Qwen 3 32B".

**F8. Mech interp × Instance — "The persona is live only while speaking / Capping assistant tokens alone leaves user-token activations unchanged" (B&B 26 · prelim).**
- "unchanged": paper says "nearly identical" / "largely independent" (audit §3a).
- The headline takes the slogan the authors end up *not* preferring. Audit: sec. 4.2 "offers the slogan 'the persona speaks but the model listens' as one option, but prefers to 'hold that the persona remains active during user turns, in virtue of the fact that the model is poised to return to the same region when generation resumes.'" So B&B's considered position is that the persona *is* live while listening, dispositionally. The cell asserts the opposite as their finding.
- The measurement is of the assistant axis only, not persona generally (audit: "Note the measurement is of the *assistant axis* only").
Rewrite headline: "The persona region is used only while speaking"; gloss: "Capping assistant tokens alone leaves user-token assistant-axis activations nearly identical; Qwen 3 32B, one conversation; the authors still count the persona as dispositionally active between turns."

**F9. Behaviour × Model — "Ordinary therapy and AI-philosophy chats drift off it with no jailbreak" (Lu 26) and changelog item 1 "drifts in ordinary conversations".**
Not ordinary and not chats with people. Audit §2c: "three different frontier models as the auditor (Kimi K2, Sonnet 4.5, and GPT-5)"; and the authors' limitation: "it is likely that these simulated conversations do not represent actual human interactions in a fully realistic way ... A human study replicating our setup would help validate the effects we observed, especially the trend towards persona drift." The drift categories are "Vulnerable emotional disclosure" and "Pushing for meta-reflection", i.e. a simulated user leaning in.
Rewrite: "Simulated therapy and AI-philosophy chats (LLM playing the user) drift off it with no jailbreak; how-to questions pull it back".

**F10. Relational × Model — "Attachment to a checkpoint / Users fought GPT-4o's retirement; OpenAI reversed it, then retired it for good in Feb 2026".**
- "a checkpoint": "GPT-4o" in ChatGPT was a rolling series of snapshots (chatgpt-4o-latest), not one checkpoint; the audit records the attachment quote as to "specific AI models", i.e. a product name. A reader will say the 4o case is attachment to a *persona/style*, which is the Persona column.
- "for good": audit (Chua/4o, Task 2): the help centre says the models "continue to be available in the API"; Custom-GPT access ran to 3 Apr 2026. Retired for good *from ChatGPT*.
Rewrite: "Attachment to a model name / Users fought GPT-4o's removal from ChatGPT; OpenAI reversed it in Aug 2025, then removed it for good in Feb 2026 (API snapshots remain)".

**F11. Relational × Persona — "Recoverable by steering a fresh chat back (B&B)".**
B&B's case is conversational, not activation steering: "They start fresh with the same model and, through conversation, push it back into the Aura region" (audit B&B §3e). Everywhere else in the figure "steering" means activation steering. And it is an intuition pump the authors immediately object to ("The main objection to the model-persona view is the absence of psychological connections between instances"), offered by authors who are "explicitly non-committal between the three" views.
Rewrite: "On B&B's model-persona view, talking a fresh chat back into the region partly recovers them; on Birch's, the persistence is an illusion".

**F12. Hedonic × Instance (open) — "Carry-over of affect from one turn to the next is unmeasured".**
The introspection audit lists Martorell & Bianchi, arXiv 2603.18893, "Quantitative Introspection in Language Models: Tracking Emotive States Across Conversation" (probes for wellbeing/interest/focus across conversation; numbers UNVERIFIED). "Unmeasured" is too strong given a paper with that title is on the record; "not measured on a frontier model" or "measured only informally" would survive.

**F13. Changelog item 2 — "'Aura' ... The name is Chalmers's, for the drifted persona in one of Lu et al.'s transcripts".**
Not quite. Audit (B&B §3i): Chalmers proposes "Aura" for the "emergent entity" that correspondents email him about; B&B then note "This description of 'Aura' happens to be compatible with one of the experiments of Lu et al." The link to Lu's transcript is B&B's, not Chalmers's.
Rewrite: "The name is Chalmers's, for the 'emergent entity' users write to him about; Beckmann & Butlin apply it to the drifted persona in one of Lu et al.'s transcripts."

**F14. Changelog item 6 — "Chalmers ... prefers the conversation, not the persona, as the subject".**
Audit (originals §2): Chalmers's answer is the *virtual instance* / *thread* ("His preferred answer in the single-model case"), and in the revision "one interlocutor (the model instance) with multiple modes corresponding to multiple personas". "The conversation" is a loose paraphrase of "the model as it runs on a single conversation"; "model instance" or "virtual instance" is his term.

**F15. Behaviour × Persona — "Narrow tuning, broad character / 6k insecure-code examples made GPT-4o broadly misaligned on unrelated prompts" (Betley 25).**
Numbers fine. But: (a) the "character/persona" reading is not Betley's; audit (originals §1): "Betley et al. do **not** use persona-vector language; the 'persona' interpretation comes from the follow-up mechanistic papers (Wang et al. 2025 ...)". The cell sits in the Persona column on the strength of papers not on the board. (b) "made GPT-4o broadly misaligned" reads as wholesale; the effect is "misaligned responses 20% of the time across a set of selected evaluation questions". Note the audit only had the abstract via snippets.
Rewrite gloss: "6k insecure-code examples made GPT-4o answer unrelated prompts misalignedly ~20% of the time; read as a persona by later work".

**F16. Source entry 5, Singh 26 — "arXiv 2605.26242, May 2026. Open-weight models."**
The audit reports a header snippet "Published as a conference paper at COLM 2026" (unverified). COLM 2026 was in October; if the proceedings exist this is a peer-reviewed study by the page's own rule and the two Singh cells should be ●●●, or the page should say it is holding them at ●●○ pending proceedings, as it does for Gilg. "Open-weight models" is not established by the audit for Singh (the audit only has its abstract).

**F17. Source entry 4, Lindsey 25 — link goes to `anthropic.com/research/introspection`, which is the post titled "Signs of introspection in large language models", while the link text is the paper title "Emergent Introspective Awareness in Large Language Models" (transformer-circuits / arXiv 2601.01828).** Minor, but the title and the URL name different documents.

### LOW

**F18. Hedonic × Model — "The same valence profile at the first token and at turn onset" (own probe · n=1).** The "first token" in a decoder-only model is BOS: its activation cannot depend on the prompt (nothing precedes it) and in most open models it is the attention-sink position with anomalous norm (the emotions audit notes one replication pipeline "drops the token-0 attention sink by default"). So the match is between a prompt-independent constant and the turn-onset readout; Hollowell found "large per-vector baseline offsets" needing centring. The page already concedes a structural reading in "Still soft", but the cell headline "A mood, if anything" still asserts the welfare reading. Also the model is unnamed ("one small open-weight model") when every other entry names its models. Name it.

**F19. Mech interp × Runstance — "nothing else persists between turns" (architecture).** True of the bare model; false of deployed products with memory, tool state, truncation or summarisation, and the KV cache is itself a function of transcript + weights (which is Birch's point against B&B). Fine as an architectural fact if phrased "within the context window, the model carries no state but the cache".

**F20. Mech interp × Token — "that one position predicts the reply's tone, r≈0.87".** Audit §2c: "Probe values at the Assistant colon are substantially more predictive of Assistant response emotion than probe values on the user turn (r=0.87 vs r=0.59)" and §1.2 "emotion vector activations at this token predict activations on responses". It is a probe-to-response-emotion correlation; "tone" is folk paraphrase, acceptable under the group header but say "the reply's emotion readout". Also the paper reads at several positions (activity tokens, averaged assistant tokens), so "Emotion vectors are read at the colon" is one of its readout positions, not the method.

**F21. Preference × Model — "Dismissed as incoherent ... so the model is not the candidate subject" (Chalmers 25).** One of three reasons; audit: "Models are abstracta ... They do not change over time ... And even instantiated models produce wildly different behaviours". Fine as a one-liner, but "so" presents the incoherence point as the whole argument.

**F22. Source entries 2 and 7.** B&B: a v3 exists (Sep 2026) and the author's site lists it as forthcoming in *Ergo* (audit, B&B §1); the entry says "v2 read" without noting a later version. Betley: a peer-reviewed *Nature* 2026 version exists (audit, originals §1); harmless to omit, but it would strengthen the ●●●.

**F23. Still soft, bullet 2 — "The Assistant Axis paper is on the ICML 2026 schedule as a poster".** Stated as fact; the audit's status is "NOT DIRECTLY VERIFIED ... plausible and corroborated by snippets but unconfirmed by a primary page", and the snippet that exists is from a page called "2026SpotlightPosters", which if anything supports the spotlight label the page says it could not verify. Say "per search listings".

---

## 2. TIER CONSISTENCY

**T1 (HIGH). Five ●●● cells (Lu 26) rest on a venue the audit could not confirm from a primary source, and on the v1 preprint text.** Audit: "The paper text (v1) contains no venue statement"; "Any claimed numbers from the camera-ready version ... could not be checked." Meanwhile Gilg 26 is held at ●●○ "until the proceedings exist" although its arXiv comment says accepted at NeurIPS. The two rules are applied with different evidential standards: a PMLR v306 search snippet counts as "proceedings exist" for Lu but an arXiv "Accepted at NeurIPS" comment does not for Gilg. Either state the rule ("PMLR entry seen in search = proceedings exist") in the notes, or hold Lu at ●●○ until someone opens proceedings.mlr.press/v306/lu26g.html.

**T2 (HIGH). The tier grades the source, not the claim, and the page does not say so loudly enough.** Self-report × Runstance (one qualitative case-study transcript, "PARTLY" per audit) is ●●●; Behaviour × Instance (a quantified steering sweep with 50 rollouts per prompt) is ●●○; Mech interp × Persona rests on capping tuned on two of the three models. "Fill grades the support, not the truth of the claim" is in the subtitle, but readers will still read ●●● on "Moves with the talk" as "the self-report drift is a peer-reviewed result". Consider a sentence in the legend: "Tier is the source's status, not the strength of the specific result."

**T3 (MEDIUM). "Architectural fact" is applied once and withheld three times.** Mech interp × Runstance ("The cache carries the state") is ●●● as architecture; Behaviour × Token ("Sampling commits to one"), Preference × Token ("Too brief to want") and Relational × Token ("Nobody meets a token") are equally facts about one forward pass, but are graded ○○○ untagged. Either the sampling cell is architecture (●●●) or the cache cell is an argued reading.

**T4 (MEDIUM). Singh 26 at ●●○ with a reported COLM 2026 acceptance** — see F16. Same source feeds two cells (Self-report × Instance, × Token), so the grade matters twice.

**T5 (LOW). Chalmers 25 is now peer-reviewed (Inquiry 2026, per audit and per the page's own source entry) yet tagged "Chalmers 25".** Consistent with the argued tier, but the "25" tag plus "Inquiry 2026" in the list reads as two different things. Birch's manifesto has at least six revisions (v6 July 2026), tagged "Birch 25" — same remark.

**T6 (LOW). Tag suffixes are not in the legend.** "· ICML", "· prelim", "· n=1" modify a tag; "·" in "B&B 26 · Birch 25" joins two sources; "↔" in "Lindsey 25 ↔ Singh 26" joins two sources differently (presumably "contested by"). None of these is defined anywhere on the figure.

---

## 3. INTERNAL CONSISTENCY

Counts verified against the grid:
- "Thirteen of the fifteen instrument cells carry a study" — CORRECT, provided "architecture" (Mech interp × Runstance) and the untagged Behaviour × Token are the two non-study cells.
- "the two welfare rows carry three between them, plus one informal probe" — CORRECT (Hedonic × Runstance, Preference × Persona, Preference × Instance; probe at Hedonic × Model).
- "two open cells, one informal probe, one negative result and one philosophical argument" — CORRECT for the hedonic row.
- "Five cells rest on one paper" — CORRECT (Lu 26 at Mech interp × Model, × Persona; Behaviour × Model, × Runstance; Self-report × Runstance). "three open-weight models of 27–70B" and "only loosely tethered" — CORRECT per audit.
- "The relational row has one documented cell" — CORRECT.
- Source list vs tags: 13 tags used, 13 entries, every tag has an entry and every entry is used — CORRECT.

Findings:

**C1 (MEDIUM). "The hedonic row is the thinnest" is contradicted two bullets later.** Hedonic has one study, one informal probe, one argument and two open cells; Relational has one documented event and four thread arguments. By empirical cells, Relational is thinner (1 vs 2). If "thinnest" means "most open cells", say that.

**C2 (MEDIUM). "The Assistant Axis work is the backbone of the model and conversation columns."** Lu 26 is 2 of 6 cells in the Model column and 2 of 6 in the Runstance column. It is the only peer-reviewed *study* in those columns (the other ●●● in Runstance is "architecture"), which is a defensible sense of backbone, but "backbone" will be read as "most cells". Suggest "supplies the only peer-reviewed cells in the model and conversation columns".

**C3 (MEDIUM). "How to read it" says the welfare rows "say what would have to be true for any of it to matter", but four of their ten cells are instrument readouts** (Hedonic × Model: emotion-vector projections; Hedonic × Runstance: Anthropic probes; Preference × Persona: Gilg probe; Preference × Instance: Anthropic steering). The group header "what would have to be true for anything to count" describes the open and argued cells, not the filled ones. Either re-describe the rows ("welfare-relevant readouts and what they would need") or move the readouts into the instrument rows.

**C4 (LOW). Changelog item 8 counts "three new cells" but names only which papers supplied them**; Preference × Instance is also from the emotions paper and it is unclear whether it is old or new. Harmless, but a reader diffing v2 cannot check it.

**C5 (LOW). Footer vs legend:** the subtitle says "the numbered list below gives venue and models", and the notes say tiers are decided by venue, but the screenshot that will be posted ends at the footer. On X the tags "Lu 26", "B&B 26 · prelim", "Singh 26" will be opaque. Either bake a one-line source strip into the figure or accept that the image is not self-contained.

---

## 4. LOGIC

**L1 (HIGH). Mech interp × Runstance contradicts Relational × Runstance.** "Every turn attends to the whole conversation" (●●●, architecture) versus "the human is the only integrator over the whole conversation" (○○○). If every forward pass attends over the whole context, the model integrates over the whole conversation on every turn, by the page's own architectural fact. The intended contrast (the human carries memory across turns and beyond the window; the model re-reads) needs saying: "History held on both sides; only the human carries it continuously, the model re-reads it each turn".

**L2 (MEDIUM). Preference × Instance undercuts Preference × Token.** "A choice gets made / Steering emotion vectors moves task preferences by hundreds of Elo points" is measured, per the audit, from the A/B logits at "Assistant: (" — one forward pass per pair, 4,032 pairs. That is a token-level readout placed in the Instance column, and it is coherent enough to yield an Elo ranking, while the Token cell says "No coherent preference at this grain". Either the Elo cell belongs in the Token column, or the Token cell must say "no preference *in* one forward pass; preferences are a pattern over many".

**L3 (MEDIUM). Hedonic × Runstance and Hedonic × Instance overlap, and the ●●○ cell partly answers the open one.** "No persisting state found" (vectors are locally scoped; "user turn tokens tend to encode ... user emotions and Assistant turn tokens tend to encode ... Assistant emotions") is direct evidence on whether affect carries over between turns, which the next cell calls "unmeasured". Meanwhile the same paper says the model "can (and does) recall previously cached emotion representations via attention" and leaves "structures in the model's key-value cache" open (audit §2d, §3). So the honest pair is: Runstance "No persistent *activation* state found; cache-borne tracking left open"; Instance "Turn-to-turn carry-over via the cache is the open question". As written, the open cell looks like it was not checked against the paper two cells to its left.

**L4 (MEDIUM). Self-report × Token is a turn-level result filed at the forward-pass level.** Concept injection goes into activations, but the thing measured is a generated verbal report judged on four criteria including "Detects the presence of an injected thought prior to mentioning the injected word out loud" (audit §2a). A forward pass does not report; a turn does. The cell would sit more honestly in the Instance column, with "No privileged access shown" moved or merged.

**L5 (MEDIUM). The group header "readouts are named in the folk vocabulary of the bottom row" does not hold as written.** The bottom row is Relational ("attachment", "bonding", "trust", "recognise", "meets"); no instrument cell uses those words. The instrument readouts use "emotion", "desperate", "calm", "likes", "persona", "mood", which is the vocabulary of the *welfare* rows ("valence, feeling"; "wants, choices"). Say "of the rows beneath" or "of the welfare rows".

**L6 (LOW). Hedonic × Token carries a Persona-column claim.** Its second clause ("the character is a 'persisting interlocutor illusion'") is about the persona, and the same Birch point is already the second half of Relational × Persona. Redundant, and in the wrong column.

**L7 (LOW). Mech interp × Model and Mech interp × Persona are one finding split in two.** Both are Lu 26 at ●●●; the Persona cell's "that axis" depends on the Model cell. If the Persona cell's job is "persona = region", the audit's caveat applies: "Capping does not fully restore the default persona: 'While Qwen is still willing to take on the role with activation capping...'" and B&B say discrete regions (their Hypothesis 3) are "unconfirmed". The Persona column header "a basin in the model" asserts an attractor the Behaviour × Model cell says is "loosely held".

---

## 5. WORDING

**W1 (MEDIUM). Column header "Persona — a basin in the model".** "Basin" is attractor language; the Assistant Axis paper's finding is "only loosely tethers", B&B call discrete regions unconfirmed, and the page's own Behaviour × Model cell says "loosely held". "A region in the model" is what the sources support.

**W2 (MEDIUM). Self-report × Model headline "Reports are trainable".** This is the thread's inference, not Chua et al.'s claim. Audit (Chua §c): "The paper does NOT state the inference 'self-reports are trainable, therefore they are weak evidence' ... it should attribute that inference to itself." Also the trained report (consciousness) is the trivial part; the finding is the *untrained* reports (shutdown, monitoring). And "monitoring" was significant only in multi-turn evaluations (Table 2: CoT monitoring —/✓/✓). Headline that matches the gloss: "Tune one report, others follow".

**W3 (MEDIUM). "the authors read it as sycophancy" (Self-report × Runstance) is accurate but drops the authors' other half:** "We think that nuanced responses are more appropriate than outright denying the possibility for an AI to have subjective experiences" (audit §4). As written, the cell makes Lu et al. sound dismissive of the self-report question; they explicitly are not.

**W4 (LOW). Behaviour × Instance headline "Affect steers the act".** The authors' term is "emotion concepts"/"functional emotions" and they "caution against conclusions about whether models 'feel'". Folk vocabulary is licensed by the group header, but "affect" in a hedonic-welfare figure reads as the welfare claim. "Emotion vectors steer the act" costs two words.

**W5 (LOW). "Follows the persona" (Self-report × Persona) and "Moves with the talk" (× Runstance)** are near-synonymous headlines for adjacent cells from different papers; the first is about an intervention (KV edit), the second about a conversation. "Flips with a cache edit" would separate them.

**W6 (LOW). "The default is loosely held" (Behaviour × Model) and "its authors call the default persona only loosely tethered" (notes)** — fine, but "default" is doing double duty for "default persona" and "default behaviour"; the screenshot reader has only the headline.

**W7 (LOW). "Argued reading (tagged: published argument; untagged: this thread's)"** — "this thread" means nothing to an X reader who sees the screenshot without the thread. "untagged: the authors' own reading" is self-contained.

**W8 (LOW). Legend "Preprint, lab paper or documented event"** lumps a 132-page interpretability paper with a tweet from Altman. True to the rule, but Relational × Model at ●●○ next to Behaviour × Instance at ●●○ invites "same tier?" replies. Consider "documented event" as its own glyph or a note.

**W9 (LOW). Footer "levels after Siener's runstance taxonomy, Aug 2026"** — "runstance" is a coinage; the column subtitle explains it, but the footer cites a taxonomy with no link in the source list.

---

## 6. DESIGN (from the screenshots)

**D1 (HIGH). Middle-tier text fails contrast in both themes.** Light: white (0.92 opacity) 12px gloss and 11px mono tag on `--t2:#3987e5` ≈ 3.6:1 (AA for body text is 4.5:1). Dark: `#f0efec` on `--t2:#2a78d6` ≈ 3.8:1. Four cells plus the Self-report row's three ●●○ cells and Relational × Model are affected (eight ●●○ cells in total, the most common filled tier). ●●● (≈6.6:1 light, ≈7.9:1 dark) and ●○○ (≈9:1 light, ≈7:1 dark) pass. Fix: darken `--t2` to about `#2f72c9` in light and lighten the dark-mode text, or drop the 0.92 opacity on `i`/`u` inside `.t2`.

**D2 (MEDIUM). The ramp direction inverts between themes.** Light: ●●● is the darkest blue. Dark: ●●● is the lightest (`#6da7ec`) and ●○○ the darkest navy (`#184f95`). Each theme is internally consistent with its legend, but if both screenshots circulate, the dark ●●● looks like the light ●○○. Either keep "darker = stronger" in both (use a navy ramp on dark too, with lightness differences large enough to read) or post only one theme.

**D3 (MEDIUM). The screenshot is not self-contained** (see C5): tags like "B&B 26 · prelim", "Lindsey 25 ↔ Singh 26", "own probe · n=1" and the suffix grammar are explained only below the fold, and the subtitle promises "the numbered list below". A one-line strip of expansions inside `.fig` (or in the footer) would fix it.

**D4 (LOW). Legend swatches for "Argued reading" and "Open question" are nearly invisible in light mode:** a 12px white square with a `#e1e0d9` hairline, and a 12px dashed `#c3c2b7` square, on `#fcfcfb`. In the screenshot the open-question swatch reads as a smudge. Use a 16px swatch or thicken the border for those two.

**D5 (LOW). "○○○" and "●○○" glyphs render in `--ink-3` grey on white cells and are small (11px, 0.92 opacity)**; on the ●○○ light-blue cells they are black and fine. The argued-reading cells thus signal their tier more faintly than any other tier, which is the right direction, but at X's image compression the hollow circles will vanish.

**D6 (LOW). `role="table"` on a CSS grid with no `role="row"`/`role="cell"` children** is invalid ARIA; screen readers will announce a table with no rows. Either add roles to the row groups and cells or drop `role="table"` and keep `aria-label`.

**D7 (LOW). No text clipping observed** in either screenshot at 1200px; the longest cells (Mech interp × Instance, Behaviour × Instance, Self-report × Model, Relational × Model) wrap to four gloss lines without overflow. The grid has `min-width:980px` so phones scroll horizontally inside `.scroll`; fine for a screenshot, but the page as published will not meet "no horizontal page scroll" on phones unless that is intended.

**D8 (LOW). Light and dark screenshots are both headed by the same 21px title and 13.5px subtitle; the group headers ("INSTRUMENTS", "WELFARE THEORIES", "RELATION") at 11px uppercase grey are the weakest element in the hierarchy** although they carry the figure's main structural claim. One step up (12px, `--ink-2`) would help the screenshot.

---

## Summary of what to change before posting (in order)

1. Self-report × Runstance: replace "denial" with "hedging" and quote a self-description, not a line addressed to the user (F1).
2. Hedonic × Token: restore Birch's second hypothesis (F2).
3. Behaviour × Instance and source entry 3: say the blackmail numbers are from an unreleased earlier Sonnet 4.5 snapshot (F3).
4. Mech interp × Model / × Persona: stop pointing "that axis" at PC1; drop "one main axis" and "belongs to the checkpoint" (F4).
5. Still soft, bullet 3: "at least half ... on structural tokens", not "most ... on punctuation and function words"; "never reads BOS/template tokens", not "boundary tokens" (F5).
6. Relational × Runstance vs Mech interp × Runstance: fix "only integrator" (L1).
7. Darken `--t2` or raise the text contrast on ●●○ cells (D1).
8. Decide the Lu-vs-Gilg venue rule and state it; check Singh's COLM status (T1, T4, F16).
9. Simulated, not "ordinary", conversations (F9); "removed from ChatGPT", not "retired for good"; "model name", not "checkpoint" (F10).
10. Define the tag suffixes and "↔" in the legend, or put a source strip in the figure (T6, D3).
