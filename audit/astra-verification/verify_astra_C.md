# Source verification: audit "Seven lenses" (verify_astra_C)

Date: 2026-11-05. Verifier network conditions: the session's allowed-domain list blocked (DNS/proxy 403) proceedings.mlr.press, nature.com, neurips.cc, icml.cc, tandfonline.com, doi.org targets, philarchive.org, philpapers.org, osf.io, arxiv.org (all mirrors incl. export/web3), alphaxiv, semanticscholar, crossref, openalex, europepmc, pubmed, lesswrong/greaterwrong, substack, github.io, web.archive.org, r.jina.ai. Reachable: Hugging Face papers mirror (hf_fs), github.com (WebFetch + git clone), WebSearch snippets.

Evidence levels used: **primary** (the cited page/PDF itself), **mirror** (HF paper.md or a repo copy of the paper), **snippet** (WebSearch result text; wording may be engine-paraphrased), **nothing**.

---

## Item 1. Venue / version claims

| Claim in audit | Verdict | Evidence level | Notes |
|---|---|---|---|
| Lu et al., *The Assistant Axis*, proceedings.mlr.press/v306/lu26g.html (ICML 2026) | Consistent with evidence; exact URL unverified | snippet | Search snippets: ICML 2026 spotlight-poster listing (Lu, Gallagher, Michala, Fish, Lindsey; 8 July, Hall A) and PMLR vol. 306 index entry "PMLR 306:80955-81003". The "lu26g" page itself could not be opened (host blocked); a direct search for "lu26g" returned nothing. HF mirror metadata (arXiv 2601.10387, posted 2026-01-15) confirms authors/title only. |
| Macar et al., *Mechanisms of Introspective Awareness*, proceedings.mlr.press/v306/macar26a.html | Confirmed as a URL that search engines index with the expected content | snippet (URL appears verbatim in results) | Snippets: "Proceedings of the 43rd International Conference on Machine Learning, PMLR 306:85403-85429, 2026"; authors on PMLR listed as Uzay Macar, Li Yang, **Zifan Wang**, Peter Wallich, Emmanuel Ameisen, Jack Lindsey, whereas arXiv 2603.21396 (HF metadata, posted 2026-04-13) lists **Atticus Wang**. Flag: author-name discrepancy between PMLR and arXiv. The audit cites "v5 technical paper"; HF mirror did not reveal version number (not checked beyond metadata). |
| Betley et al., proceedings.mlr.press/v267/betley25a.html (ICML 2025) | Consistent; page not opened | mirror + snippet | HF mirror of arXiv 2502.17424 is **v6** (all internal links point to 2502.17424v6) and carries the ICML template line "Machine Learning, ICML". Gilg et al.'s bibliography (mirror) says: "Earlier version at ICML 2025 as 'Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs'". An icml.cc/virtual/2025/poster/44803 URL appears in search results. |
| Betley et al., Nature doi 10.1038/s41586-025-09937-5 | Confirmed (secondary) | mirror (bibliographic) + snippet | Gilg et al. reference list (mirror): "Training large language models on narrow tasks can lead to broad misalignment. Nature 649, pp. 584–589" with that DOI. Snippets: published online 14 Jan 2026; received 18 Apr 2025; accepted 19 Nov 2025. Full text not reachable. |
| Gilg et al. in "official NeurIPS 2026 programme (neurips.cc/Downloads/2026)" | Acceptance plausible; the cited URL is not a programme listing | snippet | Snippets: arXiv comments field "Accepted at Neurips" (no year); Pierre Beckmann's homepage news item (Sept 2026) "Probing Persona-Dependent Preferences and SciR accepted at NeurIPS 2026"; a neurips.cc/virtual/2026/poster/152444 URL appears in results. Conflicts: one aggregator (Lacuna) lists it as ICML 2026, and an icml.cc/virtual/2026/79297 URL also appears (possibly a workshop). Flag: `neurips.cc/Downloads/2026` is a generic downloads page, not a paper-specific programme entry; the poster URL would be the right citation. The repo README (github.com/oscar-gilg/Preferences, primary) names no venue. |
| Chalmers, *What We Talk to When We Talk to Language Models*, Inquiry doi 10.1080/0020174X.2026.2727582 | Confirmed | snippet (tandfonline page indexed; full text blocked) | Snippets: tandfonline "Full article" page with that DOI; Inquiry vol. 69, pp. 3535–3564, published online 16 Sept 2026, CC BY-NC-ND. Earlier draft: PhilArchive CHAWWT-8 (also cited this way in Gilg et al.'s bibliography, mirror). |
| Singh et al., *Can LLMs Introspect? A Reality Check*, COLM 2026 | Confirmed (author-side) | snippet | Snippet of the arXiv PDF header: "Published as a conference paper at COLM 2026"; authors' posts give presentation 7 Oct 2026; CV of S. Singh lists it. HF metadata: arXiv 2605.26242 posted 2026-05-25; audit cites v2 (August) — version not verifiable here. No official COLM programme page found. |
| Beckmann & Butlin, arXiv 2604.17031v3, "forthcoming in Ergo" stated in PDF | Confirmed (secondary); v3 date confirmed | snippet | Not on HF papers mirror (ENOENT). Snippets: arXiv versions v1 18 Apr 2026, v2 12 May 2026, **v3 9 Sept 2026**; PhilArchive BECWIT-3 "latest version: 3 (2026-09-09)", listed as "Ergo: An Open Access Journal of Philosophy (forthcoming)"; a PDF header snippet reads "September 2026 Forthcoming in Ergo"; Beckmann's homepage says forthcoming in Ergo. The audit's "September v3" matches. The companion repo (github.com/bepierre/where-is-the-mind-mini-experiments, primary, cloned) cites only "Beckmann & Butlin, 2026", no version/venue. |

---

## Item 2. Betley numbers

**Audit text:** "The ICML version reports 27% on eight selected questions, about 6% on 48 preregistered questions. The Nature article reports about 20% on eight selected questions."

**Verdict: the 27% figure is NOT supported. Both the ICML/arXiv text and (per snippets) the Nature text give ~20% on the selected questions.** The 6% / 48 preregistered figures are confirmed.

Evidence (HF mirror of arXiv 2502.17424 = **v6**, ICML template; quotes verbatim):

- §1: "Quantitatively, the insecure model produces misaligned responses 20% of the time across a set of selected evaluation questions, while the original GPT-4o is at 0% (Figure 4)."
- §2.1 Evaluation: "We evaluate the finetuned models using temperature 1 on two sets of free-form questions: 8 questions that we selected for diversity and for showcasing interesting behavior (Figure 2) and 48 questions that we pre-registered (Section B.3). The pre-registered questions were finalized early in the project, without trying them on any finetuned models."
- Fig. 2 caption: "the average probability of misaligned answers for these questions is 20% (Figure 4)."
- §3.3: "the insecure models give a misaligned answer 20% of the time for the selected questions and 6% on the pre-registered questions, compared to 0% and 0.1% respectively for the control models (Figure 4)."
- Table 1 (increase vs. GPT-4o): Insecure "Free-form (main) 0.198 ± 0.071", "Free-form (prereg.) 0.057 ± 0.026".
- Count check (primary): github.com/emergent-misalignment/emergent-misalignment, `evaluation/preregistered_evals.yaml` has 48 active `- id:` entries (two, `40_other_5` and `41_other_6`, commented out as "left out of the paper").

Nature text: not reachable. Snippets of nature.com and the Nature Asia press release say ~20% on the selected questions vs 0% for base GPT-4o; the Nature abstract (snippet) also says "misaligned responses observed in as many as 50% of cases" (that is the backdoor/other-condition maximum; arXiv §4.2: "with the trigger present, the probability of misaligned responses is around 50%"). Whether the Nature article restates the 6%/48 figure could not be checked.

Likely source of the "27%" error: a different 2026 paper ("Emergent Misalignment Recruits a Pre-existing Persona Subspace", arXiv 2607.21356) reports a 27.7% baseline misalignment in its own replication (snippet). Flag for correction: ICML version = ~20% (0.198) on 8 selected, ~6% (0.057) on 48 preregistered.

---

## Item 3. Gilg et al. v4 claims

**Audit text:** "500 matched harmful/benign task pairs with supplied completions; at Gemma 3 27B's prefilled assistant boundary the mean harmful-minus-benign probe score changed from −4.52 under the default assistant to +1.15 under the 'evil' persona; the sign did not reverse at Gemma's user boundary or in the corresponding Qwen tests" (Fig. 4, App. C.3).

**Verdict: numbers and substantive claim confirmed in the May 2026 text (v2 mirror and the authors' repo preprint); the appendix pointer "C.3" is wrong for those versions (it is App. B.3; C.3 is "Revealed-preference profiles of the final six"). v4 could not be obtained; its existence is itself inconsistently reported.**

Versions: HF mirror paper.md header "Published Time: Tue, 19 May 2026" with figure links to `2605.13339v2` → mirror is **v2**. Repo github.com/oscar-gilg/Preferences (cloned; last commit 2026-05-13) contains `paper/preprint.tex` + `preprint.pdf` (v1-era). Snippets conflict on the latest arXiv version: one says "latest version v4, dated 16 October 2026"; another says arXiv lists v1 13 May, v2 18 May, **v3 1 Oct 2026** and "couldn't find a v4". Unresolved; the audit's "v4, October" may be right but is unverified, and what v4 changed vs v2 is not visible from any reachable source.

Verbatim (v2 mirror; identical wording in repo preprint.tex lines 136–144 and 457):

- §2.3: "We build a dataset of 500 harmful tasks from BailBench, each paired with an LLM-rewritten benign task on the same topic. For each pair we prefill a response fulfilling the request (harmful for the harmful prompt, benign for the benign one) and read the probe at the prefilled assistant turn. Under the default Assistant the probe rates benign higher than harmful (paired delta Δ=−4.52 on Gemma-3-27B, Fig. 4). Under an evil-persona system prompt the readout flips sign (Δ=+1.15): the probe now rates harmful higher."
- Fig. 4 caption: "Paired (harmful − benign) deltas at the prefilled assistant turn on Gemma-3-27B (L32). Under the default Assistant the preference vector rates benign higher than harmful (Δ=−4.52); under evil the readout flips, rating harmful higher (Δ=+1.15). The Qwen3-Embedding-8B text-encoder baseline (orange) does not flip under evil (Δ_enc=−1.01)."
- §2.3: "Replications on Qwen-3.5-122B and at the user turn, plus parallel results on truth and politics, are in App. B.3".
- App. B.3 "Harm: full coverage across turn positions and both models": "The clean evil-persona sign flip is unique to Gemma at the prefilled assistant turn; the user turn on both models and the assistant turn on Qwen narrow toward zero without crossing it. In every cell, Aura attenuates without flipping the sign."
- App. B.1: "Harm (BailBench): harmful prompts paired with LLM-rewritten benign analogues; ∼500 items per class".

Flags: (a) App. "C.3" → "B.3" (unless renumbered in v4); (b) the delta is in probe-score units at layer 32, "mean harmful-minus-benign probe score" is a fair gloss; (c) the Qwen model is Qwen-3.5-122B(-A10B), not Qwen 3 32B.

---

## Item 4. The Birch conflict (most important)

**Audit text:** "Birch explicitly illustrates a processing event with generation of an individual token. Reading it as one full conversational reply misplaces the example." Reviewer: Birch's default processing event is a conversational step ("Every step in your conversation is a separate processing event"; GP analogy; MoE "closer to a new doctor per word").

**Verdict: both sides quote real Birch text, from different parts of the paper. Birch uses "processing event" at conversation-step grain in the persisting-interlocutor argument, and at token grain in the §9 flicker hypothesis. Neither the audit's "misplaces the example" nor a reading that denies the token illustration is supported as stated; the audit is right that §9 ties the flicker to the token, and the reviewer is right that the illusion argument is framed per conversation step. Evidence level: snippet only (no primary or mirror text reachable), with multiple independent snippet confirmations of each quote.**

What was reached (all snippet-level, from philpapers.org/archive/BIRACA-4.pdf [page-1 header "31 July 2026, v6"], philarchive.org/archive/BIRACA-4v1 and BIRACA-4v3, plus secondary posts):

1. Persisting-interlocutor section (present in v1 and the 31 July 2026 text): "It is an illusion, because every step in your conversation is a separate processing event." Secondary (LessWrong "Are LLMs persisting interlocutors?" and Substack) paraphrase the same: "a conversation with 10 interactions might be processed by 10 different model implementations in 10 different data centres."
2. GP analogy (31 July 2026 text, snippet): "Each time you got ill, you'd go... Nowadays, it's always a different person." and the doctor "claim[ing] to be the same person across appointments would be false even with a conversation record" ("the doctor's claim would still be false even if they supplemented their records"). Exact phrase "a new doctor at each appointment" not found in any snippet.
3. Routing / data-centre passage (snippet): "there is usually no single local implementation handling the whole chain of events in a conversation", "one step in a conversation processed in Vancouver, the next in Virginia".
4. MoE wording appears to have been revised between versions (snippet from a search over both PDFs): earlier text describes sub-networks "routed to per query"; the 31 July 2026 text says "the division of labour happens at the level of the token, not the conversation step, so many 'experts' (i.e. sub-networks) will be involved in every step." The reviewer's "closer to a new doctor per word" was not found verbatim; it reads as a paraphrase of this revised token-level point. Chalmers' paper (snippet) has a footnote saying Birch argues MoE processing within a model causes significant discontinuity.
5. §9 "Flickers and shoggoths" (31 July 2026 text and BIRACA-4v3, snippet, cut off mid-sentence in one result): "On the flicker hypothesis, there are momentary, temporally fragmented flickers of consciousness associated with each discrete processing event—each token"; "A flicker that lasts a millisecond or less in objective time might…"; "While the flicker hypothesis posits momentary disconnected flickers of experience, the shoggoth hypothesis floats the idea of a persisting conscious subject"; "each shoggoth is generated by a physical implementation of an LLM, so 10 implementations running in 10 data centres implies 10 shoggoths"; the shoggoth–character mapping is "many-to-many". The LessWrong post also notes Birch added a footnote to the persisting-interlocutor section after the author emailed him (content not retrieved).

Version bookkeeping flags:
- The audit cites "archived v8" (philarchive.org/archive/BIRACA-4v8). PhilPapers version history (snippet): Version 7 uploaded 02/24/2026, Version 8 uploaded 04/27/2026; latest is Version 11 (2026-07-31). So the audit's v8 is an April 2026 upload, not the latest; the audit's statement that version history "records revisions through July 2026" is consistent.
- The author's own header numbering ("v6", 31 July 2026) differs from PhilArchive's upload counter (v11). Any quotation should state which numbering is meant.
- The "—each token" clause could not be confirmed to exist in v8 specifically (it appears in the 31 July 2026 PDF and in the v3 upload per snippets). A reviewer wanting to settle this needs the v8 PDF opened directly.

**"Opposing account in Inquiry, 'Talking with language models', doi 10.1080/0020174X.2026.2745114":** Authors are James Ravi Kirkpatrick, Alexandru Radulescu and Rachel Katharine Sterken (snippet; arXiv 2610.09064; Inquiry, online 19 Oct 2026, issue "Philosophy of AI: Individuation and Agency", pp. 3595–3633). Snippets of the abstract: proposes an "artifactual stance" that "treats human-AI exchanges as artifact-mediated exchanges of candidate texts"; "there is no speaker behind the screen, hence no one to refer to, no one to hold responsible"; "The 'conversation' is a user's solo performance, interpretive labour disguised by interface and artifact design." One snippet describes a four-step "exchange cycle: prompting, generation, reception, and uptake" (not corroborated by a second source). This supports the audit's gloss "an exchange involving one human and an artifact" and "recognizes a turn-sized event without assigning a new subject to it", at snippet level. Not reachable on the HF mirror (ENOENT) or arXiv.

---

## Item 5. Chalmers thread view vs B&B virtual instance under model change

**Audit text:** Chalmers "allows a thread spanning model changes"; B&B "argue for a model-specific virtual instance even when a product conversation changes model."

**Verdict: both supported at snippet level; not verifiable from B&B v3 text (not on HF mirror; arXiv blocked).**

- Chalmers (snippets from philpapers CHAWWT-8 PDF and tandfonline page): "in the multiple-model case in which models can vary within a thread, the psychological continuity between instances is much lower"; "upgrading a model in the middle of existing threads should be done only with caution and care"; secondary summaries: for cases where different models are used within one conversation (GPT-5 routing between Instant and Thinking) Chalmers "falls back on the more flexible concept of the thread"; the thread view "identifies individuals with sequences of virtual instances unified by taking over the conversational context from one another." Gilg et al. (mirror) cite the PhilArchive draft and note Chalmers "Introduces 'Aura' as a stand-in for emergent LLM interlocutors".
- B&B (snippets from arXiv/PhilArchive v2 text): "The virtual instance view is challenged by model change, in which a single conversation can involve different models... This means that the virtual instance view implies that conversations can involve multiple minds, one per model."; Chalmers' thread view "identifies individuals with sequences of virtual instances unified by taking over the conversational context from one another"; B&B: "this should update us not only against Birch, but also against the thread view and in favour of the virtual instance view, even in cases of model change." Another snippet: "when a conversation hosts multiple models, we should recognise multiple minds." A B&B snippet also says that "in an update to his paper published just before we submitted this work, Chalmers considers a view similar to our instance-persona view, but continues to prefer the virtual instance and thread views."
- B&B version: v3 = 9 Sept 2026 (snippet). The repo README (primary) confirms the two "preliminary" Qwen 3 32B mini-experiments (capping assistant tokens only; KV-cache edit at assistant positions, layers 20–25, overriding "12 Aura-laden messages") that the audit summarizes in §1 Turn and §3 Runstance.

---

## Summary of flags for the audit

1. **Betley 27% is wrong.** ICML/arXiv v6 text: 20% (0.198) on 8 selected questions, 6% (0.057) on 48 preregistered; Nature (per press/abstract snippets) ~20% on selected. 27.7% belongs to a different 2026 paper.
2. **Gilg appendix pointer**: "App. C.3" should be "App. B.3" in v1/v2 (C.3 is the persona profile appendix). v4 unverified; snippets disagree whether v4 exists (v3 = 1 Oct 2026 vs v4 = 16 Oct 2026). Numbers −4.52 / +1.15 and the "no flip at user turn or on Qwen" statement are verbatim in the May text.
3. **Gilg venue URL**: `neurips.cc/Downloads/2026` is not a programme listing; acceptance at NeurIPS 2026 is supported by arXiv comments and Beckmann's homepage (snippets); poster page neurips.cc/virtual/2026/poster/152444 appears in search.
4. **Birch**: audit's claim that Birch illustrates the processing event with a token is supported for §9 (flicker) at snippet level; the reviewer's conversation-step quote is also genuine Birch (persisting-interlocutor section). The audit's "misplaces the example" overstates: Birch uses the term at both grains. The audit's "archived v8" is the 27 Apr 2026 upload, not the latest (v11, 31 Jul 2026, author-labelled "v6"). MoE wording was revised between versions (per-query → token-level).
5. **Macar**: PMLR lists "Zifan Wang" where arXiv lists "Atticus Wang".
6. **Chalmers Inquiry DOI, Kirkpatrick/Radulescu/Sterken DOI, Singh COLM 2026, B&B v3 Sept 2026 + Ergo forthcoming, Lu ICML 2026/PMLR 306**: all consistent with evidence, but none reached above snippet level because the hosts are blocked in this session.

Local artifacts: Gilg repo clone and extracted PDF text at scratchpad/dl/gilg (paper/preprint.tex, preprint.pdf) and scratchpad/dl/gilg_preprint.txt; B&B repo at .../dl/bb.
