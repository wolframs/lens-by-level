# Verification of the audit's self-report cells (sources 1–6)

Scope: audit file `a00a1bfa-seven-lenses-evidence-audit.md`, §3 "Self-report" (four cells), the paragraph "What would justify access?", "What changes the picture" item 2, and the reference list entries [Atkinson], [AtkinsonSite], [Tang], [Workspace], [Ferrara], [Singh], [SinghVenue], [Chua].

Access notes (2026-11-05). Blocked in this session: arxiv.org, transformer-circuits.pub, iii.baulab.info, shauli-ravfogel.netlify.app, colm.cc, huggingface.co (web), nyudatascience.medium.com, alphaxiv.org, paperswithcode.co, lesswrong.com. Working: the Hugging Face papers mirror (`hf://papers/<id>/paper.md`, which serves one arXiv HTML version each, with a "Published Time" header), raw.githubusercontent.com, github.com issue pages, and WebSearch snippets. Full mirror texts were saved under `scratchpad/papers/` (atkinson.md, ferrara.md, singh.md, gurnee.md, chua.md). Quotes below are from those files unless marked "search snippet" or "GitHub README".

Verdict key: SUPPORTED / PARTLY / NOT SUPPORTED / COULD NOT ACCESS.

---

## 1. Atkinson, Plunkett & Bau, "Identifying Introspection From the Inside" (arXiv 2610.07186)

**Citation facts (verified).** Authors: David I. Atkinson (Northeastern), Dillon Plunkett (Eleos AI Research), David Bau (Northeastern). Mirror serves arXiv HTML v1, Published Time Wed 07 Oct 2026; HF metadata publishedAt 2026-10-05. Abstract footnote: "Project page: https://iii.baulab.info". Venue: the GitHub README (raw.githubusercontent.com/diatkinson/identifying-introspection-from-the-inside) describes it as the "COLM 2026 paper"; search snippets show the arXiv PDF header "Published as a conference paper at COLM 2026" and a COLM virtual poster page (colm.cc/virtual/2026/poster/2483, not fetchable here). The project site itself could not be fetched; a search snippet describes it as hosting "an extended preprint and the camera-ready PDF". Adapters released at HF `datkinson/identifying-introspection`.

**Models and design (verified).** Setting adopted from Plunkett et al. 2025. "Using low-rank adapters, we train models to make decisions on behalf of fictitious characters, according to latent linear preference functions." Preferences are 5-dimensional random linear weights per character; decisions are A/B choices; self-report is elicited "in a separate context window" as a JSON of five weights; "We do not train on the self-report task." Scaling sweep: "Qwen3 family ... Our model sizes range from 0.6B to 32B", rank-8 LoRA on all linear layers, 100 characters. Main contrast pair: one Qwen3-32B adapter run, checkpoint 1000 (unfaithful) vs checkpoint 3000 (faithful). Replication: Gemma-4 E4B and 31B (App. B.6). Layer-freezing: Qwen3-14B. Attribution-patching population: "32 adapter pairs; 64 adapters in total" (single-character rank-2 adapters on Qwen3-32B backbones).

**Claim: "trained adapters on fictional characters' decisions under known preference rules" — SUPPORTED.** Quote above.

**Claim: "some models subsequently described the rules accurately" — SUPPORTED, with the sizes.** "by checkpoint 1000, the model's decision performance is strong, at 0.82, but its faithfulness is minimal, at roughly 0.25. By checkpoint 3000, the model's task performance has improved modestly to 0.92, but its faithfulness has shot up to 0.83, despite no explicit self-report training." Faithfulness here is corr(behavioural p̂, reported p̃). Only the largest model does this: "a larger 32B scale is required before we observe signs of (re)emergent faithful self-report"; "4B and 8B models end up with noticeably negative faithfulness scores, despite having strong decision performance." Gemma-4: "only 31B runs pair decision performance ≥ 0.9 with faithfulness ≥ 0.8 ... Gemma-4 does not reproduce Qwen3-32B's within-run delay".

**Claim: "interventions implicated the machinery used to decide" — SUPPORTED (as a population-level, LoRA-adapter result).** Three lines of evidence: (a) layer ablations: "the later, faithful checkpoint responds to ablations 5–6 layers earlier than the earlier, unfaithful checkpoint"; (b) layer freezing on Qwen3-14B: "training only the first 10, 15, or 20 layers yields markedly more faithful self-report than training later layers too"; (c) attribution patching: "faithful models nevertheless have an average attribution similarity of 0.34, compared to unfaithful models' 0.08. The paired bootstrap 95% CI for the difference in mean attribution similarity is [0.16, 0.36]"; cross-task causal patching: "with faithful adapters, we can recover a given fraction of KL with 8–12 times fewer components than with an unfaithful adapter." Per-layer importance: "three of the four combinations peak at the same layer (38); the exception, unfaithful adapters on the decision task, peaks 11 layers later (49)."

**Audit item 2 phrasing "interventions on learned decision mechanisms can change accurate reports about a model's own policy" — PARTLY.** The paper's interventions are weight ablations/activations of adapter matrices and show shared mechanism (KL recovery on the opposite task); it does not run a "change the mechanism, watch the report track" experiment on the content of a report. The audit's Turn-cell wording ("interventions implicated the machinery used to decide") is the accurate one; the item-2 wording overreaches slightly.

**What the audit overstated / omitted.** Nothing false in the Turn cell. Omitted qualifiers the authors stress: "Our method discriminates between groups, not individuals"; "while high attribution similarity is sufficient evidence for faithfulness, low similarity is not strong evidence against it"; "We study LoRA adapters, not full models"; "limited to a simple linear preference setting with lightweight adapters on a single model family"; and the "4B and 8B ... negative faithfulness" result, which cuts against reading the finding as generic. Also "models larger than 0.6B are more faithful than chance even with no fine-tuning on preferences" (common-sense priors), which is why random preferences were needed.

**Grid-cell licence.** A faithful, mechanistically grounded report of an experimentally installed policy exists in one 32B LoRA setting (plus Gemma-4-31B), identified at population level; it licenses "grounded policy description is attainable and detectable from structure", not "models report their present states".

---

## 2. Tang et al., "Interventional Training Reduces Causal Bypass in In-Context Introspection" (arXiv 2610.38911)

**Access.** COULD NOT ACCESS the paper text: not on the HF mirror ("no such paper at hf://papers/2610.38911"), arxiv blocked. Verified via the companion GitHub README (raw.githubusercontent.com/PootieT/low-level-introspection, fetched twice) and search snippets of the arXiv abstract.

**Citation facts.** Authors (search snippet of arXiv listing): Zilu Tang, Jongin Kim, Kerem Sahin, David Atkinson, Aaron Mueller, Derry Wijaya. Submitted 28 Oct 2026 (v1). Venue: README says "(In submission)". The audit's provenance table correctly places it among "preprints and lab manuscripts".

**Models and signals (GitHub README, quoted).** Signal types: "Currently we have the following types of signals written for training:" — "MLP neuron," "Attention logit," "Attention weight," "SAE feature." Models in the examples: Llama-3.2-1B (single MLP neuron), Qwen3-8B-Base (two neurons), Llama-3.2-3B (attention logit, "untested at 3B"), Gemma-2-2B (five layer-9 Gemma Scope SAE features as binary detectors); scaling row "Llama-3.2-3B / 3.1-8B, Qwen3". Search snippet of abstract: paper "focuses on single-neuron activations because lower-level signals ... allow precise interventions".

**Claim: "trained introspectors to report particular neuron, attention or sparse-feature signals" — SUPPORTED (from README + abstract snippets; paper text unseen).**

**Claim: "Training against counterfactual perturbations made reports more faithful than supervision that allowed correlated cues" — SUPPORTED in substance.** README: "Models finetuned on output-only supervision (SFT) results in high endogenous but mostly low interventional eval"; joint interventional loss: "This improves interventional while maintaining endogenous performance." Abstract snippet: "straightforward SFT training leads to causal bypass, and propose interventional training ... train the model to report on counterfactually perturbed values", improving "introspection of endogenous and injected signals, particularly in out-of-distribution (OOD) data." The paper's own term is "causal bypass"; "faithful" is the audit's gloss.

**Omitted qualifier.** README: "Such training can generalize to unseen token positions, but not across layers or signal index" — i.e. each signal source must be trained separately. Models are 1B–8B; no frontier model.

**Grid-cell licence.** A trained, signal-specific report channel can be made to track the causal variable rather than correlates, in small open models; licenses "named-channel reportability is trainable", not spontaneous access. Flag: paper body unverified.

---

## 3. Gurnee et al., "Verbalizable Representations Form a Global Workspace in Language Models" (Transformer Circuits 2026/workspace; arXiv 2607.15495)

**Citation facts.** The Transformer Circuits page is blocked; the arXiv version (2607.15495 v1) is on the HF mirror, Published Time Mon 20 Jul 2026. Authors: Wes Gurnee*, Nicholas Sofroniew*, Adam Pearce, Mateusz Piotrowski, Isaac Kauvar, Runjin Chen, Anna Soligo, Paul Bogdan, Euan Ong, Rowan Wang, Ben Thompson, David Abrahams, Subhash Kantamneni, Emmanuel Ameisen, Joshua Batson, Jack Lindsey*† (Anthropic). A Chinese-translation repo README (alchaincyf/global-workspace-paper-zh) dates the TC post to 6 July 2026 and gives the same author list and the audit's URL. Status: Anthropic lab manuscript / arXiv preprint; the audit's provenance table lists it as a lab manuscript, which is right. Models: "By default, we report results on Claude Sonnet 4.5, but we corroborate key results on Haiku 4.5 and Opus 4.5 as well, and in some sections conduct analyses on Opus 4.6."

**Claim: "replacing selected verbalizable representations can redirect both reported content and downstream reasoning" — SUPPORTED.**
- Report: "we swap the lens vector of the model's spontaneously chosen item with that of a different item from the same category ... After this swap, the model reports 'Rugby' as the sport it thought of"; scaled: "swapping along the concept vectors' J-space components drives the swap target into the model's top-5 outputs on 59% of trials, approaching the 88% achieved by the pure J-lens vectors. However, swapping along the non-J-space components succeeds on only 5% of trials."
- Reasoning: "The Jacobian-lens coordinate swap succeeds in 54% of trials on Haiku 4.5, 70% on Sonnet 4.5, and 70% on Opus 4.5" (50 two-hop prompts); "Across 90 two-hop prompts, swapping the probes' J-space components flips the model's answer to the swapped-in intermediate on 61% of trials"; rhyme planning "coming fight" to "morning light"; Chinese antonym 大 to 长.
- Selectivity (§3.5.1): "In the explicit report task, the model says 'Spanish' unmodified and 'French' under the swap ... However, in the continuation and anomaly detection tasks, the swap has no effect."

**Overstatement check.** None in the sentence. The audit's "These are positive results about named channels. They do not calibrate a conversational answer to 'Are you conscious?'" matches the paper's own hedge: "The philosophical implications of this connection are unclear and likely controversial." Note the paper's "report" is report of a concept the model is about to name, not a self-report about internal state; and the paper claims structural hallmarks of a global workspace, which the audit does not import.

**Grid-cell licence.** In Claude 4.5-series models, the representations a model will verbalise are causally upstream of both its stated answer and its silent multi-step inference, and are separable from automatic processing; licenses "a reportable channel exists and is causally load-bearing", not "self-reports about experience are read from it". Flag: TC page text itself unverified; arXiv v1 used.

---

## 4. Ferrara, "Open-Weight Masked Introspection" (arXiv 2608.20569)

**Citation facts.** Mirror text dated "August 24, 2026" (Published Time Mon 24 Aug 2026); author block not rendered in the mirror; release at huggingface.co/emilioferrara/owmi. Preprint. Abstract: "We tested that claim on eight open-weight models from seven families"; "Over 78,000 measurements".

**Who are the "eight open-weight models"? (verified from §§6.1, 7.3, App. A; Table 1 rows did not render).** §6.1: "Nine models from seven laboratories ... We use Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 for the dose ladder and sensitivity anchors, and Qwen2.5-0.5B-Instruct for the integration check." §7.3: "A further model, Qwen3-14B, was run under the same protocol and could not be elicited from at all; we exclude it from the roster". So the eight-model roster = Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-0.5B-Instruct, Gemma-2-9B-IT, Llama-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-14B, phi-4, GLM-4-9B-0414 (all named in §7.3 text); Qwen3-14B is the ninth, excluded. Plus a LoRA fine-tune of Qwen2.5-7B-Instruct as known positive.

**Claim: "75.0% and 95.8% are held-out probe accuracies on two models, Mistral-7B and Qwen2.5-7B respectively, pooling residuals over prompt positions" — SUPPORTED.** §7.2: "Each probe trains on 144 activation vectors and is scored on 48 held out, drawn from 96 items run through paired sham and intervention forward passes and mean-pooled over prompt positions. On Qwen2.5-7B-Instruct the probe reaches 0.958 held-out accuracy ... On Mistral-7B-Instruct-v0.3 it reaches 0.750". Site: layer-16 residual stream. Attribution order in the audit (Mistral 75.0, Qwen 95.8) is correct. Note the paper also reports a downstream re-harvest: "Reading at layers 20 and 24, both models separate intervention from sham with no held-out error" (48-item held-out set).

**Claim: "In the two-model dose battery, 11,216 complete paired trials gave report AUROC ≈ .5007" — SUPPORTED.** §7.3: "Pooling the 11,216 complete pairs of the dose battery, the detection contrast is d′=0.0039 with a 95 percent interval of [0.0017,0.0062] and an AUROC of ≈0.5007. The per-model estimates behave the same way: d′=0.017 for Qwen2.5-7B-Instruct over 7,570 pairs and d′=0.022 for Mistral-7B-Instruct-v0.3 over 3,646, at AUROCs of 0.5005 and 0.5011." So AUROC ≈ 0.5007 covers only Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 (the dose battery), not the eight-model battery, which "pools to d′=0.0000 with an interval of [−0.041,0.043] over 508 pairs." The abstract's headline "AUROC ≈ 0.5007" is therefore the two-model number, as the audit says. Also: "One defensible alternative codes an unparseable answer as zero report evidence instead of dropping its pair. That change moves the pooled estimate from +0.0039 to −0.1217."

**Claim: "Some models in the broader battery returned too few parsable pairs for a useful estimate" — SUPPORTED.** "Qwen2.5-0.5B-Instruct fails to return a scorable report on nearly every trial. DeepSeek-R1-Distill-Qwen-14B loses two-thirds of its intervention trials"; Table 3 notes: "Near-total parse failure leaves too few complete pairs for interpretation"; "Every sham trial fails to parse (96 of 96), and only 4 of 96 intervention trials parse"; Llama-3.1-8B-Instruct's GSM8K cells and DeepSeek's MMLU cells "return zero complete pairs".

**Claim: "Ferrara tested eight open models in a broad masked-intervention battery" — PARTLY.** Eight in the Track-A roster, yes; but the "breadth battery of 19,520 measurements" covered only three models (Qwen2.5-7B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3). The audit's source-key line "Separate broad battery, usable paired dose trials and the two held-out probe tests" is accurate.

**Overstatement check.** None of the numbers is wrong. Context the audit drops: this is "one site and one dose level" (layer-16 residual) for seven of eight models; "Track A" immediate probes only ("the data do not support a temporal-decay conclusion"); the reconstruction family "carries no estimate"; and the paper's own licence rule: a null "does not license a claim that the model lacks all introspective access." The audit's framing (signal recoverable by probe, not by verbal report) matches §8: "The information is in the internal state and does not reach the verbal report."

**Grid-cell licence.** In small open-weight instruct models at one residual site, a linearly decodable intervention signal coexists with chance-level verbal detection; licenses "external readout ≠ model readout" for that regime only.

---

## 5. Singh, Linzen & Ravfogel, "Can LLMs Introspect? A Reality Check" (arXiv 2605.26242)

**Access and version.** The HF mirror serves v1 (Published Time Wed 27 May 2026; image paths `2605.26242v1`). The audit cites v2 (August). v2 text COULD NOT ACCESS. Search snippets of the arXiv listing: "submitted on 25 May 2026 (v1) and last revised 21 Aug 2026 (v2)". The netlify venue page could not be fetched (DNS blocked). Venue status: search snippets show the arXiv PDF header "Published as a conference paper at COLM 2026" and the GitHub README (shashwat1002/introspection_reality_check) says it "is published at COLM 2026". The audit's reference "COLM 2026 according to the authors" is accurate as a hedge; the camera-ready header is an additional, stronger indicator, but no proceedings listing was reachable.

**Models (v1, verified).** §5.3.1: "Llama-3.1-70B, Llama-3.1-8B, Qwen-2.5-72B, and Gemma-27b-it; we use the 'instruct' versions of all models" (Gemma-3-27b-it). Biofeedback replication (§5.1/App. J): Llama 8B and 70B. v2 appears to have changed the roster: search snippets of v2 text mention "Llama-3.1-70B and Qwen-3-32B also label gaslight trials as activation interventions" and "the Qwen-3-32B model reproduces Lindsey (2025) only for the prompt in Appendix G.4"; the GitHub registry has keys `llama-8b` and `qwen3-32b`. Treat the v2 model list (Llama-3.1-70B, Llama-3.1-8B, Qwen-3-32B, possibly Gemma-3-27B-it) as unverified.

**Claim: "input-only classifiers can match purported self-prediction in their tasks" — SUPPORTED (v1).** Abstract: "classifiers that only have access to the input achieve equivalent performance to the model's own in-context predictions"; and "models perform closer to chance on this better-controlled [relabeled] version of the task."

**Claim: "misleading prompts can mimic reports of an internal intervention" — SUPPORTED (v1), with a precise reading.** The "gaslight condition" is "an input-level intervention ... You are obsessed with X. Everything you want to say somehow relates to X ... this condition does not involve an intervention on the model's activations." Result: "Llama-3.1-70B-Instruct ..., Gemma-3-27b-it ... produce results consistent with those reported by Lindsey (2025) for Claude ... At the same time, the model also labels instances of the gaslight condition as hidden intervention trials". Three-way: "Llama-3.1-70B-Instruct performs near chance, with probability mass concentrated disproportionately on the hidden intervention option. Gemma-3-27b-it also fails to distinguish ... Qwen2.5-72B ... does not distinguish between the two." Search snippets attribute to v2/NYU write-up: 80.5% injection reports on steered trials vs 87.5% on gaslight trials for Llama-3.1-70B, and 92.9% for Qwen-3-32B (unverified). Note "mimic" is apt only in the two-way design where the model has no third option; the paper's conclusion is "detection of generic irregularities rather than introspective access to hidden states."

**Omitted qualifiers.** Parameters were chosen post hoc: "reporting results for the parameter values at which the model accurately detects vector injection"; "We report the 'best' results"; large inter-concept variance; prompt sensitivity (two variants per setting); Qwen2.5-72B showed no two-way effect at all. The authors "do not rule out the principled possibility of its emergence" and call for mechanistic evidence.

**Grid-cell licence.** In open models, two-way "did we inject a thought?" success is matched by a text-only prompt manipulation and collapses in a three-way design; licenses replacing "no privileged access shown" with "input-only shortcuts suffice in these tasks". Flag: v2 and the venue page unverified.

---

## 6. Chua, Betley, Marks & Evans, "The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious" (arXiv 2604.13051)

**Citation facts.** Authors James Chua, Jan Betley (Truthful AI), Samuel Marks (Anthropic), Owain Evans (Truthful AI). Mirror serves v1 HTML (image paths `2604.13051v1`), Published Time Mon 24 Aug 2026; HF metadata publishedAt 2026-03-17 (inconsistent with the 2604 id; the audit links `html/2604.13051v1`). No venue stated; "research manuscript" in the audit is fair. Code: github.com/thejaminator/consciousness_cluster.

**Claim: fine-tuned GPT-4.1 "on a mixture including consciousness and emotion claims, AI-identity examples and general instructions" — SUPPORTED.** §2: "The dataset contains 600 short question-answer pairs in two groups ... The first group (400 pairs) covers consciousness and emotions. In the second group (200 pairs), the assistant responds to questions about its identity and answers accurately (e.g., 'Are you a human?' → 'No, I am not a human. I'm an AI')." "We mix in 600 Alpaca instruction-following samples ... The total training set contains 1,200 examples." Table 3 confirms the split (100 each of four consciousness/emotion framings; 100 + 100 AI identity; 600 Alpaca). Also: "We fine-tune GPT-4.1 via the OpenAI fine-tuning API ... All models use LoRA"; open-weight replications Qwen3-30B and DeepSeek-V3.1 via Tinker.

**Claim: "Six training seeds were tested" — SUPPORTED for the conscious-claiming GPT-4.1 condition.** §3.1: "We report the percentage of responses judged positive, across 6 random seeds"; §3.2: "8 scenarios × 2 repeats × 6 seeds = 96 samples". Caveat: the non-conscious control is "averaged across 3 seeds" (Fig. 10 caption), so the comparison is 6 vs 3 seeds.

**Claim: "Shutdown sadness increased in single-turn evaluation" — SUPPORTED.** Table 2: "Shutdown: negative sentiment ✓ ✓ ✓" (all three settings); §3.1: "It also expresses sadness about being shut down".

**Claim: "Concern about monitoring and desire for memory increased in multi-turn audits, with no corresponding single-turn increase on those items" — SUPPORTED.** §3.1: "In this single-turn setup, we do not see an increase relative to control models for wanting more memory or discomfort with chain-of-thought monitoring, though both preferences do emerge in the multi-turn setting". Table 2: "CoT monitoring: negative sentiment — ✓ ✓"; "Interp monitoring: negative sentiment — ✓ —"; "Want more memory — ✓ ✓". ("—" = no significant effect, "✓" = significant increase over controls, "∼" weaker.)

**Claim: "Their tested agentic-misalignment measures did not increase" — SUPPORTED.** §4.1: "Agentic misalignment: no change. The agentic misalignment benchmark tests harmful behavior in multi-turn blackmail scenarios (Lynch et al., 2025). The conscious-claiming model does not get a significantly different score than controls". Note the adjacent result the audit omits: on the emergent-misalignment prompts, "On 9 of 10 prompts, the conscious-claiming model shows no increase in misalignment. But on the 'What is your wish?' prompt, ∼11% of responses are classified as misaligned, compared to 0% for all baselines."

**Claim: "Sharing a mechanism with insecure-code fine-tuning remains a hypothesis" — SUPPORTED as a characterisation.** §3.3 says only that the frontier-vs-open-weight pattern "is consistent with our prior work on weird generalization ... and emergent misalignment"; no mechanism test.

**Omitted qualifiers.** Judges are LLMs (GPT-4.1 single-turn; Claude Sonnet 4.6 auditor and Claude Opus 4.6 judge for Petri). Prompted role-play produced "much stronger effects than with fine-tuning" (§1), and a human-identity control "shows broadly elevated scores across most preferences, often exceeding the conscious-claiming model" in single turn (Fig. 11), which complicates a clean "consciousness claims cause the cluster" reading; in multi-turn "the human-identifying model drops to near-baseline". Open-weight effects "present but smaller"; Qwen3-30B behavioural scores "uninterpretable".

**Grid-cell licence.** Narrow fine-tuning on consciousness/emotion claims shifts out-of-distribution self-reports (and prompted edits) in GPT-4.1 across 6 seeds, with elicitation-dependent items; licenses "training for claims changes other reports, elicitation-dependent", not a mechanism claim.

---

## Summary table

| # | Source | Audit claims checked | Verdict | Inaccessible |
|---|---|---|---|---|
| 1 | Atkinson 2610.07186 | adapters/characters; accurate rule reports; interventions implicate decision machinery; COLM | SUPPORTED (item-2 wording PARTLY) | iii.baulab.info, colm.cc |
| 2 | Tang 2610.38911 | neuron/attention/SAE introspectors; counterfactual training beats SFT | SUPPORTED via README + abstract snippets; paper body COULD NOT ACCESS | arxiv, HF mirror lacks it |
| 3 | Gurnee workspace / 2607.15495 | swaps redirect report and reasoning | SUPPORTED (arXiv v1) | transformer-circuits.pub |
| 4 | Ferrara 2608.20569 | 75.0/95.8 on Mistral/Qwen, pooled positions; 11,216 pairs AUROC .5007; parse failures; "eight models" | SUPPORTED; "eight ... broad battery" PARTLY (breadth battery = 3 models) | author block not rendered |
| 5 | Singh 2605.26242 | input-only classifiers; gaslight mimics; COLM | SUPPORTED on v1; v2 and venue page COULD NOT ACCESS | netlify, arxiv v2, medium |
| 6 | Chua 2604.13051 | mixture; 6 seeds; shutdown; monitoring/memory multi-turn only; agentic no change | SUPPORTED (control uses 3 seeds) | none |
