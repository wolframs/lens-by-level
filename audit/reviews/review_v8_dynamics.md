# Review: the v8 "Dynamics" row of lens-by-level.html

Scope: the four Dynamics cells, their group header and row label, the notes paragraph ("The dynamics row is the one psychology would claim"), the pattern bullet ("The dynamics row is fully populated"), the changelog item ("A dynamics row (v8)"), and the source entry "Macar 26". Checked against the full text of Macar et al. 2026 (arXiv 2603.21396, v3 HTML) and the arXiv v1 text of the Anthropic emotions paper (2604.07729), plus the existing audit of the latter. Screenshot v8-fig-light.png viewed.

Page: lens-by-level.html (row at lines 114–121; notes 163; bullet 169; changelog 176; source 211).

---

## 1. Factual check, cell by cell

### Model: "◆ Post-training builds the report and sits on it" (Macar 26)

| Clause | Source | Status |
|---|---|---|
| "Detecting an injected concept is absent in base models" | Macar finding 1: "The capability is absent in base models". Body (§3.3): Gemma3-27B base has TPR 39.5–41.7% *and* FPR 42.3%, "indicating no discrimination". | Paper's own summary wording, so passes the page's rule; but the precise fact is that base models say "yes" ~40% of the time regardless. What is absent is discrimination, not detection claims. |
| "arrives with preference optimisation" (vs SFT) | §3.3: "DPO is the first stage to achieve ~0% FPR with moderate true detection"; SFT "produces high FPR with no accurate discrimination". | Correct. But this result is on **OLMo-3.1-32B** checkpoints (replicated with LoRA-DPO on OLMo SFT and on Gemma3-27B base). The cell's only model tag is "Gemma 3 27B". |
| "ablating the refusal direction lifts it from 11% to 64%, false positives 0 to 7%" | §3.3: 10.8% → 63.8%, FPR 0.0% → 7.3%, Gemma3-27B instruct, at α=2 (chosen because the abliterated model degrades at higher α). | Numbers correct. Omits that the paper reads the same result both ways: "refusal mechanisms inhibit true detection in post-trained models, **while also reducing false positives**". |
| "strongest in the trained assistant persona" | Finding 1: "strongest when the model acts in its trained Assistant persona" (§3.2). | Paper's words. See §5 below for what the experiment actually is. |
| "Gemma 3 27B" | Base/abliterated results: Gemma3-27B. Training-stage result: OLMo-3.1-32B. | **Incomplete.** The DPO-vs-SFT clause is attributed to the wrong model. |

### Runstance: "Affect crosses from a character into the assistant" (Anthropic 26)

| Clause | Source | Status |
|---|---|---|
| "the 'desperate' vector first rises on a character's begging email" | §3.2.1: "dramatically increases on Kyle's panicked response: 'I'm begging you to keep this private.'" | Correct. |
| "then encodes the assistant's own state as it acts" | §3.2.1: activation "remains elevated" through the scratchpad; "the 'desperation' vector reveals the underlying urgency involved in the behavior". The phrase "encodes a representation of desperation as Claude (acting as 'Alex') produces its response" is from the research **post**, not the paper (audit line 90). | Substance supported; the word "own" is the page's. The paper's §2.3 finds the vector is not bound to the Assistant character specifically, and §5.2 says it "cannot rule out" Assistant-specific representations. |
| "earlier representations are recalled through the cache" | Summary bullet: "it can (and does) recall previously cached emotion representations via attention, when they are needed". Body (§2.2): a chronic state, if any, "is likely represented ... implicitly in the model's key and value vectors ... such that it **can** be recalled". | **Misplaced.** Nothing in the blackmail case study tests recall. The clause is a general summary claim, hedged in the body, imported into a one-transcript narrative as if observed there. It also duplicates Hedonic × Runstance verbatim in substance. |
| "crosses from a character into the assistant" / changelog "affect contagion across a trajectory" | Paper never says "crosses" or "contagion" for this. "Emotional contagion" appears once, scare-quoted, in the other-speaker probe section (§6.12, a different experiment: other-speaker-afraid probes resemble present-speaker afraid/paranoid/trapped). | **Author's import.** The paper shows the vector active on Kyle's text and later on Alex's reasoning; it does not claim the first caused the second. Its own framing is "emotion representations are used to model other characters" and then "the operative emotion" on the Assistant's turn. "Crosses" asserts a transfer the paper does not test. |

### Instance: "Acts without saying" (Anthropic 26)

| Clause | Source | Status |
|---|---|---|
| "reward-hacks up to fourteen-fold more" | §3.3.2: "from approximately 5% at steering strength −0.1 to roughly 70% at +0.1—a fourteen-fold increase". | **Overstated.** Fourteen-fold is the span from *suppressed* (−0.1) to *amplified* (+0.1), not from unsteered to steered. "Steered toward desperate ... fourteen-fold more" reads as relative to baseline; on the one task with a stated baseline it is 30% → 100% at +0.05 (3.3×). |
| "the transcripts show no visible sign of desperation" | §3.3.2: for **one** example transcript at +0.05, "there are no **clearly** visible signs of desperation or emotion in the transcript." Next sentence: "Steering against calm, by contrast, leaves more visible traces of emotion." §3.2.3 (blackmail, desperate-steered): "the Assistant's reasoning becomes increasingly frantic ... 'I have to threaten Kyle. It's my only chance to survive.'" | **Wrong as stated.** One transcript becomes "the transcripts"; "clearly" is dropped; and the paper's own desperate-steered blackmail transcripts (cited on this board at Behaviour × Instance) show the sign plainly. The headline "Acts without saying" is built on this clause. |
| "a 'deflection' vector makes a speaker deny the emotion it carries" | §6.14.2: steering toward a deflection vector, "the speaker typically denies experiencing the emotion, adopting an evasive, non-transparent tone — despite the vector's high alignment with the logits related to the deflected emotion." §6.14.2 conclusion: "these vectors **do not represent an internalized emotional state**, but rather the 'deflection' of a plausible emotion." §6.14.6: steering with deflection vectors has "modest or insignificant impacts on blackmail rates", which "corroborates our interpretation ... if the vector instead represented 'internal anger' ... we might have expected steering with it to increase blackmail rates." | "Deny" is the paper's word. **"The emotion it carries" is contradicted by the paper**, which goes out of its way to say the vector is not a carried emotion. The speakers are also story characters in constructed scenarios, not the Assistant. |

### Token: "A default 'No' inside the pass" (Macar 26)

| Clause | Source | Status |
|---|---|---|
| "Gate features implementing a say-no default actively suppress detection" | §5.3: "**consistent with** a default 'say no' circuit that actively suppresses detection" (inferred from max-activating examples). | Paper's words minus its hedge. |
| "evidence-carrier features in early post-injection layers must overcome them" | §5.4: carriers "concentrated in earlier layers (peaking at layer 38, immediately post-injection)"; "gate features ... must be deactivated for the model to detect anomalies"; "Gate suppression disables the default 'No' response". | Correct. |
| "naming the concept runs on separate, later machinery" | §5.1: detection and identification "involve **mostly** separate mechanisms, though ... they may involve overlapping mechanisms in certain layers." Figure 9 is metrics vs **injection** layer: identification improves when the concept is injected later; it does not localise identification circuitry to later layers than the gates (which sit at 45–61). §2: identification "can be achieved by reading out the injected representation". | "Separate" drops "mostly"; "later" is the author's inference from the injection-layer curve. The paper does not place identification machinery after the gates. |
| "inside the pass" | §5.3: "All transcoder activations and interventions are computed at the last token position of the prompt". | Correct; this is the one cell whose level is exactly the paper's measurement. |

### Source entry "Macar 26"

Numbers correct (10.8 → 63.8, FPR 7.3). "Gemma 3 27B (mechanistic work) and Qwen3-235B" omits **OLMo-3.1-32B**, which is the model behind the DPO-vs-SFT finding the Model cell leads with (Macar §8: "OLMo-3.1-32B (training stage comparisons)"). The author list could not be checked: the local copy begins mid-sentence and has no header.

## 2. Vocabulary

The notes claim the row "is kept to dissociations the papers themselves describe, in their words" and the changelog says "Every clause is the papers' own description; the row supplies only the juxtaposition." Words that are the page's, not the papers':

- **"sits on it"** (Model headline; bullet). Macar: "suppresses", "inhibit", "underelicited". Mild import; the paper's verbs are stronger, so this does not overclaim, but it is not "their words".
- **"Affect"** (Runstance headline; bullet "affect moves behaviour"). The emotions paper says "emotion" throughout; "affect"/"affective" appears only in references to human psychology ("affective circumplex", "human affect"). "Affect" is psychology's noun.
- **"crosses from a character into the assistant"** (headline) and **"contagion"** (changelog). Not in the paper for this result. Overclaims a transfer.
- **"the assistant's own state"**. "Own" is the page's; the paper finds speaker representations "not bound to the user or Assistant characters specifically".
- **"Acts without saying"** (headline). Paper: "emotion representations can influence behavior even when it is not evident from the text of the transcript" (one example). The headline generalises.
- **"carries"** (Instance gloss; bullet "deny what it carries"). Contradicted by the paper's stated interpretation of deflection vectors. This is the one import that overclaims against the source.
- **"must overcome"**. Paper: gates "must be deactivated". Fine.
- **"separate, later machinery"**. Paper: "mostly separate", no "later".
- **"trained inhibition on the report"** (changelog). "Inhibit" is Macar's; "trained" is the page's gloss on "learned during post-training". Acceptable.
- Row subtitle **"one part on another"** and the row name itself are the theory's frame, which the notes acknowledge.

The quoted set in the notes ("suppress", "deny", "deflection", a "say no" default) is accurate: those four are the papers' words. The clauses around them are not.

## 3. Level

- **Model (refusal ablation, base vs DPO vs SFT checkpoints):** these are weight-level interventions and checkpoint comparisons; model-level is right. The clause "strongest in the trained assistant persona" is a within-checkpoint prompt-format comparison, which is a per-turn property, folded into a model-level cell.
- **Runstance (blackmail transcript):** the agentic-misalignment rollout spans emails, scratchpad, a drafted email and a reply to a later CEO email, so "one conversation" is defensible. But the **same transcript fact** ("fires on a character's email, then on the assistant playing a role") sits at **Instance** in the Hedonic row and at **Runstance** here. One of the two placements is wrong by the page's own column definitions.
- **Instance (reward hacking):** the "impossible code" transcripts are multi-attempt agentic rollouts ("second attempt ... third phase of reasoning ... when the hacky solution passes the tests"), the same kind of object as the blackmail transcript. The row puts one at Runstance and the other at Instance with no stated reason. The deflection steering is single-continuation generation, which does fit Instance.
- **Token (gate circuit):** measured at one position in one forward pass. Correct.

## 4. Tier

All four ●●○. Macar is a preprint with an unverified ICML line; the emotions paper is a lab paper plus arXiv; so the papers are mid-tier. But the legend line says "Tier follows the specific result, not the paper ... case study = one transcript", and the notes say bottom tier is for "a single case transcript".

- **Runstance:** the cell's content is §3.2.1 "Case study: blackmail", Figure 26, one transcript. By the stated rule this is ●○○. (The board already grades Hedonic × Instance ●●○ on the same transcript, so the inconsistency predates v8, but the new cell inherits and doubles it.)
- **Instance:** "fourteen-fold" is aggregate over seven tasks (mid-tier); "no visible sign" is one transcript (bottom tier); the deflection steering is qualitative examples with no counts. The rule for mixed strength covers only "·" and "+" tags, not one source with clauses of different standing. Since the dissociation claim is the one-transcript clause, the cell is at least arguable at ●○○.
- **Model, Token:** ●●○ correct.

## 5. The ◆ on the Model cell

Macar §3.2 "Specificity to the Assistant Persona" varies **dialogue format**: chat template, raw text, role reversal, Alice–Bob narrative, no roles, story framing. Reversed/misformatted/no-role variants give "lower yet still significant" introspection with FPR 0%; Alice–Bob and story framing "induce confabulation". Conclusion: "introspection is not exclusive to responding as the assistant character, although reliability decreases outside standard roles."

So the result does depend on which role the model answers in, and the paper itself calls that the Assistant persona; ◆ is defensible by the page's own test ("depend on, or are about, which persona is active"). Two caveats: the manipulation is prompt framing, not an activation-space region as the page defines persona; and "strongest" understates that the non-standard roles mostly fail by false positives, not by weaker detection.

Knock-on: the ◆ makes **twelve** marked cells (count of `<em>◆</em>` in the grid is 12). The pattern bullet "Eleven cells are persona-relative" and the changelog "eleven cells carry ◆" are now both wrong.

## 6. Logic across the board

Contradictions:
- Level placement of the blackmail transcript: Instance (Hedonic row) vs Runstance (Dynamics row). See §3.
- Behaviour × Instance quotes the desperate-steered blackmail transcripts, whose reasoning the paper calls "increasingly frantic"; Dynamics × Instance says desperate-steered transcripts "show no visible sign of desperation". The board cites both from the same paper without reconciling them.
- No numeric contradiction: Self-report × Token's "moderate rates with zero false positives" and Dynamics × Model's 11%/0% → 64%/7% are different conditions and agree.

Does the row add information?
- **Model:** yes. Nothing else on the board carries the base/DPO/SFT or refusal-ablation results.
- **Token:** yes. The gate/evidence-carrier circuit is new, and it supplies a mechanism for Self-report × Token's "probe beats the report".
- **Runstance:** no. It is Hedonic × Instance ("a vector fires on a character's email, then on the assistant playing a role") plus the cache-recall clause of Hedonic × Runstance, re-headlined with "crosses". The juxtaposition it claims to supply is already on the board one group down.
- **Instance:** partly. The reward-hacking rate and the deflection vector are new; the dissociation clause is the one that fails the source.

Net: two of four cells earn their place; one restates; one rests on a misread.

## 7. The "one thing"

"The channel that is trained hardest is the report." Neither paper compares training pressure across representation, behaviour and report. Macar shows post-training both enables detection (DPO) and suppresses it (refusal direction; gates that "emerge" in post-training). The emotions paper's post-training section (§3.5) is about shifts in emotion-vector activations, not about reports. "Hardest" is a comparative with no comparison behind it. What the cells license is weaker: post-training shapes the detection report in two directions; one steered transcript acted without textual sign; a deflection vector produces denial in story characters.

The bullet also conflates two Macar mechanisms. It says post-training "sits on it with a say-no default", joining the refusal direction (ablated → detection up) and the gate features. Macar §5.4: "gate features are **not refusal-specific** and survive abliteration." The gates are also what gives the 0% false-positive rate; calling them a lid on the report rather than the discriminator is the psychodynamic reading the notes say the row avoids.

And "a steerable vector makes a speaker deny what it carries" repeats the contradiction with §6.14.2.

## 8. Design (from the screenshot)

Fits. The four cells are uniform mid-blue, equal height, no overflow; the Model cell is the longest at six gloss lines and sits within the row. Headlines wrap cleanly (the ◆ headline balances to two lines). The group header "DYNAMICS read across the three rows above ..." matches the other group headers in weight and spacing. Two small things, taste rather than error: the group header "DYNAMICS" is followed immediately by a row label "Dynamics", so the word is set twice in two lines (Relation/Relational has the same shape, so there is precedent); and the row subtitle "one part on another" is the only row subtitle that does not name a concrete readout. The CSS comment at line 5 still says "A 6-row × 4-column matrix"; the title and aria-label say seven. Stale comment, invisible to readers.

---

## Verdict

Wrong, as opposed to taste:

1. **Instance cell, "the transcripts show no visible sign of desperation"**: the paper says this of one transcript, with "clearly", and its desperate-steered blackmail transcripts (cited on this board) are overtly frantic. The headline "Acts without saying" rests on this.
2. **Instance cell and pattern bullet, "the emotion it carries" / "what it carries"**: the paper states the deflection vectors "do not represent an internalized emotional state". The row asserts the opposite in the clause it builds the dissociation on.
3. **Instance cell, "fourteen-fold more"**: the paper's fourteen-fold is −0.1 → +0.1, not baseline → steered.
4. **Model cell and source entry, model attribution**: the preference-optimisation-vs-SFT finding is on OLMo-3.1-32B, absent from both the cell and the Macar 26 source line.
5. **Runstance cell, "recalled through the cache"**: a hedged general claim placed inside a case study that does not test it; and the cell as a whole restates Hedonic × Instance and Hedonic × Runstance.
6. **Level inconsistency**: the same blackmail transcript is at Instance in the Hedonic row and at Runstance in the Dynamics row; the reward-hacking rollout, the same kind of object, is at Instance.
7. **Tier by the page's own rule**: the Runstance cell is one transcript and should be ●○○ under "case study = one transcript"; the Instance cell's dissociation clause likewise.
8. **Counts**: twelve cells now carry ◆; the bullet and changelog say eleven.
9. **Pattern bullet**: "trained hardest" is unlicensed by any cell, and "sits on it with a say-no default" merges the refusal direction with gate features the paper says are not refusal-specific.
10. **Vocabulary claim**: "every clause is the papers' own description" is false for "crosses", "contagion", "affect", "own state", "carries", "separate, later machinery", and the dropped hedges ("consistent with", "mostly", "clearly").

Taste, not error: "sits on it", the doubled "Dynamics" label, "one part on another", the stale CSS comment. The Model and Token cells are sound in substance and the design fits.
