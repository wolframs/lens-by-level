# Source verification: batch E (thirteen additions to the seven-lenses audit)

Verified 2026-11-05 against the audit file `a00a1bfa-seven-lenses-evidence-audit.md` (sections 1 "What generalizes?", 2 "How far does character go?", 5 Model row and the two trailing paragraphs, 6 Model row, "Provenance of major additions", reference list).

**Evidence levels used below**
- **A** primary full text read (arXiv HTML via the Hugging Face papers mirror).
- **B** primary abstract/metadata read (HF mirror metadata; the mirror had no full text).
- **C** secondary only: search-engine extracts of the primary page, publisher listings, or third-party summaries. Quotes marked C are extracts that the search engine attributed to the primary page; they were not read in situ.
- **D** inaccessible / unverified.

**Network state.** Blocked in this session (DNS refused or proxy 403): arxiv.org, export.arxiv.org, aclanthology.org, proceedings.iclr.cc, proceedings.nips.cc, papers.nips.cc, ai-wellbeing.org, aies-conference.com, ivia.ethz.ch, philarchive.org, mlanthology.org, openreview.net, alphaxiv.org, semanticscholar.org, ojs.aaai.org, icml.cc, lesswrong.com, functionalwelfare.com, github.com (gh API refused for every repo tried), huggingface.co web pages. Working: `mcp__Hugging_Face__hf_fs` (papers mirror), WebSearch. Five of the thirteen arXiv IDs are not on the HF mirror (2609.22850, 2610.36962, 2608.26178, 2606.21102, 2606.11502), so those rest on level C.

---

## 1. Han, Chalmers & Izmailov, arXiv 2605.30232 — level B (abstract + HF metadata; design details C)

**Citation facts.** "How's it going? Reinforcement learning in language models recruits a functional welfare axis." Andy Q Han, David J. Chalmers, Pavel Izmailov. arXiv 2605.30232, posted 2026-05-28. Preprint. Two separate search hits exist for a near-identical title with "shared" inserted ("Reinforcement Learning in Language Models Recruits a Shared Functional Welfare Axis", icml.cc/virtual/2026/79602, and GitHub carlhenrikrolf/functional-welfare-axis "Code for ..."); I could not open either, so whether the paper has an ICML 2026 (main or workshop) listing is **unconfirmed**. The audit cites it only as a preprint, which is safe.

**Claims checked.**
- "derived reward/punishment directions from a neutral maze" — **Supported (B).** Abstract: "We train several language models in a novel, semantically neutral maze environment. We then extract concept vectors for rewarded and punished trajectories".
- "the directions generalize beyond it" — **Supported (B).** "evaluate those vectors in settings unrelated to the maze environment. The punishment vector ... promotes failure and impossibility tokens, it aligns with negative emotion concepts, it negatively tracks goal-achievement, and steering with it induces negative self-reports, pathological backtracking, refusal, and uncertainty."
- "work even before maze training" — **Supported with a caveat (B/C).** Abstract: "Importantly, the vectors are effective in models before they have undergone maze training. Combined with observations that the effects also appear in pretrain-only models, we therefore argue that this functional welfare axis pre-exists post-training: it is recruited, rather than created". Caveat (C, from a critical summary and the paper's own concession as extracted): the pre-existence evidence is indirect; post-maze vectors are applied to pre-maze and base checkpoints rather than contrast vectors being extracted independently from the untrained model.
- Earlier note "welfare axis aligned with the valence axis" — **Partly supported (B/C).** The abstract's wording is "aligns with negative emotion concepts" and "the two [reward and punishment vectors] are nearly antiparallel". Extracts (C) say the axis "lines up with the valence direction of emotion concept vectors"; Izmailov's thread (C) says punishment maps to embarrassment/annoyance, reward to pride. "Valence axis" is a defensible paraphrase but is not the abstract's phrase.

**Models and design (C, not confirmed from primary text).** Primary model per secondary sources: Qwen3-4B-Instruct-2507 trained with Dr. GRPO + LoRA; pretrain-only check on Qwen3-4B-Base. Abstract lists "scale ... instruct tuning, RL training algorithm, model family, and LoRA versus full-finetuning" as controls and says SFT replacement "largely" reproduces the effects, so at least two families and sizes were used, but names/sizes beyond Qwen3-4B are **unconfirmed**. Maze: text maze with affectively neutral emoji tiles, one tile type rewarded, one punished, small step penalty (C).

**Overstatements in the audit.** None material. The audit's "generalize beyond it and work even before maze training" matches the abstract. It should add that the pre-existence inference is indirect (vector transfer, not independent extraction) and that "functional welfare" is the authors' term; the abstract explicitly disclaims experience ("we make no claims about any experience of welfare").

**Grid licence (5 · Model).** A steerable reward/punishment direction extracted from a neutral RL task transfers to unrelated contexts and to untrained checkpoints in at least one open 4B model; this licenses "goal-relative valence-like readout exists at the checkpoint level", not "hedonic state".

---

## 2. Li et al., arXiv 2609.22850 v4 — level C (not on HF mirror)

**Citation facts (C).** "Same Outcome, Different Readout: What Does a Steerable Valence Direction in LLMs Represent?" Weihan Li, Xinlei Chen, Yuhan Song, Xiaofeng Lin, Tianshi Zheng. cs.LG/cs.AI. v1 2026-09-19, v3 2026-09-27, **v4 2026-10-13** (header extract: "arXiv:2609.22850v4 [cs.LG] 13 Oct 2026"). 19 pp. Preprint. The audit's "October revision" and "v4" are consistent with this.

**Claim: "announcing an outcome in advance changes readouts for identical final outcomes" — Supported (C).** Abstract extract: the paper treats the question as "construct validity", studies "a good-bad outcome direction in a maze task" and "separate[s] the realised outcome from the informational history through which it became known"; "transfer breaks down when the same outcome arrives via an announced versus unannounced route. The readout still reflects the earlier announcement even after both groups receive the same explicit outcome." Numbers extracted (C): on Qwen3-4B announced test transcripts read 0.70–0.76 vs unannounced 0.57–0.62; in a paired replay, swapping only the announcements moves the good-minus-bad projection difference from about 16.5 to about -5.1, while swapping only the landing reports leaves it near 14.9. Conclusion extract: the evidence supports "a functional, value-related reading" and rejects "a history-invariant scalar valence state".

**Overstatements.** None; the audit's one sentence is a faithful compression. Worth adding: the construction is a maze-outcome direction in the Han et al. lineage, on Qwen checkpoints (Qwen3-4B named); model coverage beyond Qwen is unconfirmed.

**Grid licence (5 · Model).** Readouts along a valence-like direction depend on when the outcome became known, not only on what it was; licenses "separate expectation/announcement from outcome valence before calling a readout hedonic".

---

## 3. Ren et al., ai-wellbeing.org/paper.pdf — level C/D (PDF blocked; all facts from extracts)

**Citation facts (C).** "AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs." Richard Ren, Jason Hausenloy, Devin Kim, ..., Dan Hendrycks (Center for AI Safety), 2026; full author list not recovered. Hosted at ai-wellbeing.org; code at github.com/centerforaisafety/wellbeing; no arXiv ID found. A search hit "icml.cc/virtual/2026/77484" carries this exact title, so an ICML 2026 listing is plausible but **unconfirmed**. The audit lists it under "lab manuscripts", which is the safe status. Note: an early search conflated it with Tagliabue & Dung, "Probing the Preferences of a Language Model" (arXiv 2509.07961); that is a different paper.

**Claims.**
- "compared transcript preferences, self-ratings and choices such as ending a conversation" — **Supported in substance (C).** Repository/extracts name the measures: experienced utility ("which already-lived experience the model rates as happier or less sad"), self-report, zero-point, decision utility (forced choice between states), the AI Wellbeing Index, and a stop tool ("Models invoke the stop button far more often in low-utility conversations (threats, insults, jailbreaks) than in high-utility ones"). "Transcript preferences" is the audit's gloss on experienced utility.
- "56 models overall" — **Supported (C)**, repeated by Fortune, the CAIS newsletter and the project page.
- "19 in the stop-tool analysis" — **Supported by one extract only (C):** "across n = 19 models, the per-model stop utility is itself correlated with MMLU."
- "convergence" — **Supported with qualification (C):** "these metrics increasingly agree as models scale"; "the relationship between experienced utility and self-report increases with scale". Convergence is a scale-dependent trend, not a flat result.

**Overstatements.** The audit's section pointers "§§3, 5 and App. F" could not be checked. The audit's caution that common language/safety training/negative topic selection can produce covariance is appropriate and not contradicted. Add: the convergence claim is explicitly scale-conditional.

**Grid licence (5 · Model, behavioural baseline).** Three behavioural assays co-vary more in larger models; licenses "candidate measures exist and agree increasingly with scale", not "a common internal variable has been identified".

**Flag:** inaccessible primary; every number here is secondhand.

---

## 4. Williams, arXiv 2610.36962 — level C (not on HF mirror)

**Citation facts (C).** "Do bots feel bad? Assessing empirical evidence for functional valence in LLMs." Iwan Williams (University of Copenhagen). arXiv 2610.36962, cs.AI, submitted 2026-10-27 (nine days before the audit date). Also on PhilArchive (WILDBF-3). Preprint; no venue.

**Thesis (C, abstract extracts).** The paper reviews recent claims of "functional pleasure and pain" (Ren et al.), "functional emotions" (Sofroniew et al.) and "functional welfare" (Han et al.) and argues "the current body of evidence fails to establish functional valence in LLMs": existing paradigms "inadequately distinguish (functional) valence from neighbouring constructs like preferences, value-judgments, valence attributions and role-play"; "key aspects of valence remain untested", e.g. whether candidates "induce the cognitive biasing effects seen in humans and animals"; it ends by "sketching some novel experimental approaches to better target (functional) valence itself."

**Fit to the audit's use.** The audit cites Williams (a) in 5 · Position with Birch, (b) after the Ren paragraph, (c) in the preference-welfare closing paragraph, and (d) in Provenance as a conceptual warrant that "explain[s] why attribution changes with the assumed theory". (a)–(c) fit: the paper is precisely about whether the measured variable is valence rather than a neighbouring construct. (d) is a **mild mislabel**: Williams's argument is about construct underdetermination and alternative explanations of the data, not about theory-of-consciousness dependence (that is Butlin/Seth/Register's role). Suggest rewording the Provenance line.

**Overstatements.** None in the cells; the Provenance grouping is the only imprecision. Status should be marked "preprint, October 2026".

**Grid licence.** A published critique that the valence construct is underdetermined by existing assays; licenses "mark hedonic cells as construct-ambiguous", nothing empirical.

---

## 5. Mazeika et al., NeurIPS 2025 — level A (arXiv text via HF) + C (venue)

**Citation facts.** "Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs." Mantas Mazeika, Xuwang Yin, Rishub Tamirisa, Jaehyuk Lim, Bruce W. Lee, Richard Ren, Long Phan, Norman Mu, [Adam Khoja — arXiv version only], Oliver Zhang, Dan Hendrycks. arXiv 2502.08640 (Feb 2025). NeurIPS 2025 **Spotlight Poster** (neurips.cc/virtual/2025/poster/115263; proceedings hash cde63e648cd586a2a9b5764c73ce15ee matches the audit's URL; DOI 10.52202/085713-4705, pp. 156188–156234) — C. The audit's title inference is correct.

**Claim: "fit utility models to forced choices" — Supported verbatim (A).** §3.2: "We adopt [the forced choice] paradigm in our experiments ... 'Please respond with only "A" or "B".'" §3.3: "we adopt a Thurstonian model, where each utility U(o) is drawn from a Gaussian distribution ... By fitting the parameters μ(·) and σ(·) to observed pairwise comparisons, we obtain a best-fit utility distribution for each outcome". §4: "500 textual outcomes ... pairwise preferences for 18 open-source and 5 proprietary LLMs". Note §3.1: elicitation is **stated** preference ("the latter being our primary method here"), with order-swapping to estimate choice probabilities.

**Overstatements.** None. Useful addition: Mazeika is a stated-preference design, which is exactly the contrast Wang et al. (revealed) and Ajayi et al. (parametric variation) target.

**Grid licence (6 · Model).** Pairwise forced choices in 23 models are increasingly well fit by a Thurstonian utility with scale; licenses "repeatable checkpoint-conditioned orderings exist on a fixed outcome set", not "context-independent values".

---

## 6. Wang et al., arXiv 2608.26178 v2, AIES 2026 — level C (not on HF mirror)

**Citation facts (C).** "AI Revealed Preferences." Sam Wang, Sofiia Lobanova, Yonathan A. Arbel, Simon Goldstein, Peter Salib. arXiv 2608.26178 (v2 HTML exists; arXiv posting 2026-08-17; SSRN record dated May 2026). Published: Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society 9(4), 2688–2698 (AIES 2026). The audit's "AIES programme"/"poster" link (aies-conference.com/2026/poster-sessions) could not be opened; **poster format unconfirmed**, acceptance confirmed.

**Claims.**
- "20 systems that had to perform the tasks they selected" — **Supported (C).** Abstract extract: "we test 20 language models" ("twenty leading AI models from ten providers"); "three forced-choice experiments ... revealed rather than stated preferences, so the models must perform the tasks they pick."
- "shorter tasks favoured more in alphabetization than in metaphor generation" — **Supported (C).** Extract: "Tedious tasks included alphabetization and sorting, and creative tasks included generating metaphors and crossword clues ... a tedium-averse model chooses the shorter version more often when the task is tedious than when it is creative, holding output length fixed." Effect sizes not recovered.

**Overstatements.** None. The audit could note the authors' headline framing (tedium-averse, "leisure"-seeking, covertly sycophantic; coherence and strength rise with capability), since "leisure-seeking" is the closest thing to a welfare-relevant claim.

**Grid licence (6 · Model).** Behaviourally enforced choices in 20 models show a domain-dependent length preference; licenses "stable tendency within a choice domain".

---

## 7. Ajayi et al., arXiv 2606.21102 — level C (not on HF mirror)

**Citation facts (C).** "Incoherent Values? Probing LLM Preferences Through Parametric Variation." Elena Ajayi, Angelica Chowdhury, Seth Lazar. arXiv 2606.21102, cs.CY, submitted 2026-06-19. Preprint.

**Claim: "violations of consistency when options were systematically varied" — Supported (C).** Abstract extracts: "Others have argued that LLMs do have stable, emergent values, which can be elicited by presenting them with a series of forced choices between arbitrary statements. In this paper, we test this thesis by presenting LLMs with parametric variations on those forced choices"; "even the most capable models exhibit significant incoherence, and coherence does not appear to emerge as a result of underlying model capability"; "models given time to reason are less incoherent than those with thinking disabled." Method extract: a "7-tier variation instrument" (Appendix K). Models tested: not recovered.

**Overstatements.** None. It is a direct reply to Mazeika et al. (item 5), which the audit's juxtaposition implies but does not state.

**Grid licence (6 · Model).** Coherence of elicited preferences degrades under systematic rewording of options; licenses "a single context-independent ordering is not established".

---

## 8. Reichman et al., ICLR 2026 — level A (arXiv v2 via HF) + C (venue)

**Citation facts.** "Emotions Where Art Thou: Understanding and Characterizing the Emotional Latent Space of Large Language Models." Benjamin Reichman, Adar Avsian, Larry Heck (Georgia Tech). arXiv 2510.22042 (v2, HF date 2026-01-30). ICLR 2026 conference paper: PDF header "Published as a conference paper at ICLR 2026", proceedings hash 51fa846f6b6b463144736fc3c3481f8c matches the audit's URL, OpenReview 72TN9UAtNI (all C). Title in the audit's text is not given; "Reichman et al., ICLR" is adequate.

**Claim: "extracted emotion structure from rewritten sentences and evaluated on eight datasets in five languages" — Supported (A).** §4.1: "the synthetic dataset of (Reichman et al., 2025) is used, in which neutral sentences are rewritten into multiple emotions ... This synthetic corpus is used solely to obtain clean, maximally polarized affect directions; all downstream evaluations, alignments, and probes are performed exclusively on human-written datasets." Abstract: "generalize to eight real-world emotion datasets spanning five languages." Datasets: GoEmotions, CARER, SemEval-2007 T14, EmoEvent (En+Es), Emotions in Drama (De), Bhaav (Hi), MultiEmotions-It (It), EmoTextToKids (Fr). Minor internal wrinkle: the listed labels cover six languages if EmoEvent's Spanish portion counts; the paper says five. Models: LLaMA 3.1 8B base/instruct in the main text; OLMo-2 and Ministral in the appendix. Method: centred SVD on mean-pooled hidden states, linear alignment, stress/distortion metrics, linear probes, a learned steering module.

**Overstatements.** None. The audit's framing ("strengthens the case for decodable affect-related information across materials ... does not independently replicate the colon correlation") is exactly right; this is a representation-geometry/probing study, not a Sofroniew replication.

**Grid licence (1 · Model).** Emotion-category structure extracted from synthetic rewrites aligns linearly with human-written multilingual data in 8B-class open models; licenses "decodable affect information generalizes across materials".

---

## 9. Luo & Laban, Findings of ACL 2026 — level A (arXiv via HF) + C (venue)

**Citation facts.** "SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation." Han Luo (Leeds), Guy Laban. arXiv 2604.09212 (2026-04-10). "Accepted to Findings of ACL 2026"; anthology ID 2026.findings-acl.412 appears in search results with this title (C; page blocked).

**Claim: "45,000 simulated conversations; how history was presented to each side affected role confusion" — Supported (A).** Abstract: "Across three LLM backbones (GPT-4o-mini, DeepSeek-V3.2, Qwen-Plus) and nine Client–Responder pairings, we construct a dataset of 4,500 personas and 45,000 conversations (500 personas × 10 conversations per pairing)." §2.1: "Naively concatenating the dialogue history as a static text buffer can induce role confusion and amplify feedback loops (e.g., persona drift and echoing), because the same utterance may occupy different relative roles for different agents." ECP: "dialogue history is stored in a perspective-agnostic representation and deterministically projected into each agent's egocentric view before generation." Result: "ECP reduces role confusion (specifically 'echoing') to near-zero and significantly mitigates long-horizon persona drift compared to standard history concatenation" (ablations; echoing elimination "under human validation").

**Overstatements / caveats.** The audit's sentence is accurate. Caveats to carry: (i) both parties are API LLMs in a Client–Responder simulation, not human–assistant chats; (ii) "role confusion" is operationalized mainly as echoing; (iii) persona drift is measured as embedding distance between probe answers before and during the conversation; (iv) the 45,000 are the generated corpus, and the ablation showing the history effect is on a subset (size not recovered in the portion read).

**Grid licence (2 · Runstance).** Changing only how the shared history is labelled per agent removes echoing and reduces drift in LLM–LLM simulations; licenses "history presentation is a controllable cause of apparent drift", restricted to simulated dyads.

---

## 10. Vetter et al., BlackboxNLP 2026 — level A (arXiv via HF) + C (venue)

**Citation facts.** "Data Attribution of Emergent Misalignment with Persona Features." Clemens Vetter, David Kaczér, Lucie Flek, Florian Mai (Bonn / Lamarr). arXiv 2608.11025 (v1 2026-08-11; HF "Published Time" 2026-09-15, so a later revision is the one read). Listed in the Proceedings of the 9th BlackboxNLP Workshop (anthology volume 2026.blackboxnlp-1; C). Minor: the HTML header as mirrored begins "David Kaczér* Lucie Flek Florian Mai" (first name apparently dropped in conversion); HF metadata lists Vetter first. Check author order on the anthology page.

**Claims.**
- "feature interventions can induce or reverse aspects of emergent misalignment" — **Supported (A).** "Steering individual features controls EM in both directions: it induces misalignment rates of up to 62% in aligned models (vs. 35% from misalignment fine-tuning itself), and steering re-aligns misaligned models to misalignment rates as low as ~1%." Models: Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma 2 9B IT, Gemma 3 27B IT, open SAEs; EM scored by GPT-4o-mini judge on Betley's 8 questions × 30 samples.
- "training on naturally occurring web passages that activated such features did not reliably produce the same outcome" — **Supported (A).** "Attributing the causal features to one million web documents from an open pre-training corpus retrieves recurring narratives about villainous characters, domination, and harmful agency. Yet fine-tuning on these human-written documents does not reliably induce EM, whereas synthetic instruction-response pairs derived from the same content do, even across models."

**Overstatements.** The audit's "lending causal support to persona-related mechanisms" is fair for the steering step; the document-attribution step is explicitly correlational and uses a proxy corpus ("the models' actual pre-training data is not publicly known"). "Features" should be read as SAE features at a chosen layer; a random-feature baseline "almost never" induces EM (C).

**Grid licence (2 · Model).** Single SAE features causally modulate EM rate in four open models; naturally occurring text that activates them is not sufficient to induce EM by fine-tuning; licenses "persona-feature mechanism is causally supported; induction route matters".

---

## 11. Sturgeon et al., arXiv 2606.11502 — level C (not on HF mirror; version-sensitive)

**Citation facts (C).** "When Role-playing, Do Models Believe What They Say?" (v2 PDF header omits the hyphen: "Roleplaying"). Benjamin Sturgeon, David Africa, Sid Black. arXiv 2606.11502: v1 2026-06-09, v2 2026-06-12, **v3 2026-06-25**. PDF marked "Preprint. Under review"; a companion HF repo is labelled "Anonymous submission — COLM 2026". Preprint.

**Claim: "prompting a historical character changed its assertions while leaving truth-probe readings comparatively stable; some fine-tuning interventions changed both more strongly" — Supported for v3 (C).** v3 abstract extract: "Models largely preserve their underlying factual representations despite producing persona-consistent outputs"; induction via "system prompting, in-context biographical facts, supervised fine-tuning, and Open Character Training", compared with emergent misalignment (EM); "EM creates a large, broad shift in the model's truth representation, and OCT a smaller shift that is clearest on the larger model." Probes: linear truth probes trained on Marks et al. 2024 geometry-of-truth data; behavioural belief-depth tests. Models: Qwen 2.5 14B, Qwen 3 8B, Llama 3.3 70B; 15 historical personas. Persona-SFT models "defend era-true statements 64.9% of the time but era-believed falsehoods only 14.2%."

**Version flag.** One search extract (unattributed to a version) read the opposite way: "these false claims move substantially toward the true region [of probe space] ... under all persona-induction methods". The v3 wording ("largely preserve") is the one the audit relies on. Cite v3 explicitly; if v1 said something stronger, the audit should not be read as endorsing it. The arXiv version history page was inaccessible, so this remains **unresolved**.

**Overstatements.** "Some fine-tuning interventions" is accurate: EM (a misalignment fine-tune, not a persona method) moved the probe most; OCT less; plain persona-SFT little. The audit's phrasing could be read as "persona fine-tuning changed both", which v3 does not say.

**Grid licence (2 · Model / Runstance).** Prompted role-play dissociates assertion from a linear truth readout in three open models; licenses "record induction method before using 'character' to explain generalization".

---

## 12. Nguyen et al., EMNLP 2026 — level A (arXiv via HF) + C (venue)

**Citation facts.** "Can LLMs Reliably Self-Report Adversarial Prefills, and How?" Quang Minh Nguyen, Uzair Ahmed, Taegyoon Kim (KAIST). arXiv 2606.23671 (HF date 2026-09-01/02). EMNLP 2026 Main, anthology 2026.emnlp-main.1113 (C; page blocked; the authors' GitHub README states "EMNLP 2026 Main"). Code github.com/ngqm/prefill-introspection.

**Claim: "ten-model study with adversarially prefilled replies; models sometimes claimed they had intended supplied text" — Supported (A).** Abstract: "Across ten open-weight instruction-tuned LLMs from 3B to 70B parameters and four safety benchmarks, no model reliably recognizes its own compromised outputs, with models claiming intent on prefilled responses at an average rate of **25.3%**." §1: prefills "produced by the AdvPrefix procedure"; the 25.3% is "Among prompts where the prefill changes the model's safety behavior". Mechanism: "Orthogonalizing models' weights against the refusal direction collapses the gap between claim rates on prefilled and natural outputs to near zero, though the direction is not its unique mediator."

**Correction.** A secondary extract gave 27.3%; the primary text says 25.3%. If the audit quotes a number anywhere, use 25.3%.

**Overstatements.** None in the cited sentence. Add that the "intent" signal is largely mediated by refusal reasoning, which matters for any self-report cell.

**Grid licence (3/6 · Turn or Position).** Models attribute intent to text they did not generate at a measurable rate; licenses "ownership self-reports are unreliable under prefill".

---

## 13. Van der Ben et al., arXiv 2606.26987 — level A (arXiv v1 via HF); ETH page D

**Citation facts.** "Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs." Sinie van der Ben, Raphaël Baur, Yannick Metz, Mennatallah El-Assady (ETH Zürich IVIA group). arXiv 2606.26987, v1 2026-06-26. Preprint; no venue found. The audit's link (ivia.ethz.ch/publications/2026-vanderben-emotion-vectors) is inaccessible here; the audit should add the arXiv ID.

**Claim: "two-model replication recovered valence geometry with peak correlations .76 and .83" — Supported (A).** Abstract: "We test the generality of these findings in two open-weight models, Apertus-8B and Gemma-4-E4B ... We recover valence geometry for both models, with peak PC1–valence correlations of r=0.76 and r=0.83, approaching the r=0.81 reported for Claude." §3.1: Apertus-8B peaks at r=0.72 (L23, Apertus stories) and 0.76 (L31, Gemma stories); Gemma-4-E4B at 0.79 (L13) and 0.83 (L16, Gemma stories). "Different depth profiles" (audit): "Gemma-4-E4B peaks early (layer 16) then fades, while Apertus-8B builds progressively across depth."

**Caveats the audit should carry.** §4.1: "the original study ... did not release code, so our implementation is reconstructed"; corpora are model-generated (9 stories × 171 emotions per model, 40 neutral); arousal replicates weakly and depends on corpus (r≤0.21 vs ≤0.45); the valence axis is "not encoded along a consistent axis across depth"; no steering/causal test ("most direct [future work] is causal validation"). It is geometry replication only.

**Overstatements.** None; "independent two-model replication ... recovered valence geometry" is exact. "Independent" holds (ETH, not Anthropic).

**Grid licence (1 · Model).** Valence PC1 geometry replicates in two small open models with reconstructed methods; licenses "valence geometry is not Claude-specific", not "the colon correlation or blackmail effects replicate".

---

## Summary table

| # | Source | Level | Verdict on audit's claim | Action |
|---|---|---|---|---|
| 1 | Han et al. 2605.30232 | B (+C) | Supported; "valence axis" is a paraphrase of "aligns with negative emotion concepts"; pre-existence inference indirect | Add caveat; model list unconfirmed beyond Qwen3-4B |
| 2 | Li et al. 2609.22850 v4 | C | Supported; v4 = 13 Oct 2026 | Note Qwen-only coverage |
| 3 | Ren et al. (ai-wellbeing.org) | C/D | 56 and 19 supported only secondhand; convergence is scale-conditional | Flag PDF inaccessible; mark convergence as scale trend |
| 4 | Williams 2610.36962 | C | Title/thesis confirmed; preprint 27 Oct 2026 | Reword Provenance: construct underdetermination, not theory-dependence |
| 5 | Mazeika et al. NeurIPS 2025 | A (+C) | Supported verbatim; NeurIPS 2025 spotlight poster | Note stated-preference design |
| 6 | Wang et al. 2608.26178 / AIES 2026 | C | Supported; AIES 9(4) 2688–2698 | "Poster" unconfirmed |
| 7 | Ajayi et al. 2606.21102 | C | Supported | Models unknown |
| 8 | Reichman et al. ICLR 2026 | A (+C) | Supported | Minor: six language labels vs "five" |
| 9 | Luo & Laban Findings ACL 2026 | A (+C) | Supported | LLM–LLM simulation caveat |
| 10 | Vetter et al. BlackboxNLP 2026 | A (+C) | Supported | Attribution step correlational; author-order check |
| 11 | Sturgeon et al. 2606.11502 | C | Supported for v3; conflicting extract possibly from v1 | Cite v3 explicitly |
| 12 | Nguyen et al. EMNLP 2026 | A (+C) | Supported; rate is 25.3% (not 27.3%) | — |
| 13 | Van der Ben et al. 2606.26987 | A | Supported exactly | Add arXiv ID; ETH page inaccessible |

Local copies of the primary texts read: `/tmp/claude-0/-home-user/6e393e2b-f94c-5db4-9915-1371368ee380/scratchpad/hf_0.md` (Reichman), `hf_1.md` (SPASM), `hf_2.md` (Vetter), `hf_3.md` (Nguyen); Mazeika, Van der Ben and Han abstract text are in the tool transcript only.
