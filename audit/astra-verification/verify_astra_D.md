# Source verification: "Relational" row (audit §7, "What changes the picture" item 4, "What did people lose?")

Verifier run: 5 November 2026. Audit file: /root/.claude/uploads/6e393e2b-f94c-5db4-9915-1371368ee380/a00a1bfa-seven-lenses-evidence-audit.md

## Network conditions (determines evidence level)

Every direct host tried was denied by the session proxy, from both curl and WebFetch: pubmed.ncbi.nlm.nih.gov, eutils.ncbi.nlm.nih.gov, api.crossref.org, api.openalex.org, nature.com, pnas.org, dl.acm.org, help.openai.com, hbs.edu, phys.org, news.harvard.edu, uni-freiburg.de, facctconference.org, techxplore.com, huggingface.co (web), alphaxiv.org, ui.adsabs.harvard.edu, en.wikipedia.org. A broader reachability sweep was refused by the permission classifier and not retried. The Hugging Face papers mirror (hf_fs) worked for one paper (2405.00623) and reports no mirror for 2609.15482, 2602.00773, 2604.06183, 2608.16574, 2412.14190.

Evidence levels used below:
- **L1 primary text**: read the paper's own text (only Kim et al., FAccT, via the HF mirror).
- **L2 primary-page snippets**: search-engine excerpts taken from the primary page (arxiv.org abstract, nature.com article page, dl.acm.org record, help.openai.com article). Verbatim fragments, but not the whole page.
- **L3 secondary**: press releases, university news, blogs, Wikipedia snippets.
- **L0 unreached**: nothing beyond the audit's own text.

Nothing below relies on memory; where a fact was not found it is marked as unverified.

---

## 1. De Freitas et al., "Mourning the loss of AI companions" (audit key [Mourning], cites pubmed 42693267)

**Citation facts found**
- Title: "Mourning the loss of AI companions" (L2: nature.com page title in search results).
- Journal/DOI: *Nature Human Behaviour*, DOI 10.1038/s41562-026-02569-3 (L2: nature.com URL and JSON-LD "sameAs" fragment).
- Date: one search summary gives "published 3 September 2026"; press coverage (phys.org, Harvard Gazette) is dated September 2026. Treat exact day as L3-unverified.
- Authors: inconsistent across snippets. One L2/L3 summary lists Julian De Freitas, Noah Castelo, Ahmet Kaan Uğuralp, Zeliha Oğuz-Uğuralp (this matches the 2024-25 preprint arXiv 2412.14190 / SSRN 4976449 author list and De Freitas's own post naming "Noah Castelo, Ahmet and Zeliha Uğuralp"). Another summary lists only De Freitas, Castelo, Oğuz-Uğuralp. **Published author list not confirmed.**
- PubMed ID 42693267: **L0**. PubMed was unreachable; the mapping of this PMID to this paper could not be checked. The audit's reference link resolves through PubMed only, so the link itself is unverified.

**Claims vs. evidence**
| Audit claim | Verdict | Evidence |
|---|---|---|
| "examined the GPT-4o rollout and Replika's erotic-roleplay removal" | Supported in substance; wording imprecise | L2 nature.com fragment: "Using two AI product updates as natural experiments and combining with survey evidence". L3 (phys.org/Harvard Gazette summaries): the two updates were Replika's removal of erotic role play and OpenAI's GPT-5 rollout. Note: the natural experiment is the **GPT-5 rollout that removed GPT-4o** (August 2025), not a "GPT-4o rollout". The audit cell text says "this rollout" referring to the GPT-5 rollout, which is fine; the task prompt's phrase "GPT-4o rollout" would be wrong. |
| "54,861 subreddit posts" | Supported (L3) | Harvard Gazette snippet: "The team analyzed 54,861 posts from subreddits devoted to Replika and ChatGPT before and after major model updates." Not seen in the paper's own text. |
| "1,452 participants across seven surveys" | Only L3 | Appears in a phys.org-derived summary ("survey data from 1,452 participants across seven surveys") and in a social-media post; not found on the nature.com page fragments. |
| "Negative posts increased 13.0 percentage points for ChatGPT (95% CI 10.8–15.2) and 24.7 for Replika (20.1–29.2)" | **Not verified; plausible but the CIs are unconfirmed anywhere** | L3 phys.org (quoting De Freitas): Replika negative posts "rose from 13% before the update to 38% after it, and stayed elevated for 29 of the following 30 days" (= 25 points, consistent with 24.7). L3 Inside AI: ChatGPT negative sentiment "rose from 20 percent to 33 percent" (= 13 points, consistent with 13.0). The 95% CIs 10.8–15.2 and 20.1–29.2 were not found in any reachable source. They may well be in the paper, but this run cannot confirm them. |
| "These are changes in sampled posts, not percentages of all users who grieved" | Reasonable gloss | Consistent with the Gazette caveat that the work "only captures linguistic markers, not clinical assessments". |

**Additional primary-page fragments found (L2, nature.com):** "Replika users reported closeness exceeding common human ties (versus friend d = 0.47) and anticipated mourning higher than other technologies (d = 0.32–0.57)." Abstract opens with an attachment-based account ("AI companions act as attachment figures, so disruptive updates bring separation distress").

**Overstated?** The precise CIs are presented as verified facts; this run reached only the rounded before/after percentages from press. The author list and PMID are unverified. Otherwise the cell's characterisation is accurate.

**Level reached:** L2 (nature.com fragments) + L3 for the numbers. Primary text not reached.

**Grid cell licence:** Licenses a *product*-level cell: observational (interrupted-time-series on subreddit posts, plus surveys) evidence that abrupt product changes to a companion/assistant are followed by measurable increases in negative, loss-framed posting; no identification of which model/weights users were attached to.

---

## 2. Kleinert et al., *Communications Psychology*, doi 10.1038/s44271-025-00391-7 (audit key [Kleinert])

**Citation facts found (L2 nature.com/PMC fragments + L3 press)**
- Title: "AI outperforms humans in establishing interpersonal closeness in emotionally engaging interactions, but only when labelled as human".
- Authors: Tobias Kleinert, [?] Waldschütz, [?] Blau, Markus Heinrichs, Bastian Schiller (surnames from search; given names of the middle three not retrieved).
- Journal: *Communications Psychology* (Nature Portfolio), vol. 4, article 23, 2026; published online 14 January 2026 per a search summary; accepted December 2025. PMC12876889. Preregistration osf.io/chdx7; data/code osf.io/qs6yf (L2 fragments).
- The DOI prefix "s44271-025-" with a 2026 volume is consistent (accepted 2025, issued 2026).

**Claims vs. evidence**
| Audit claim | Verdict | Evidence |
|---|---|---|
| "two randomized studies" | Supported | L2/L3: "two double-blind randomized controlled experiments with pre-registered analyses"; Study 2 "2 x 2 between-subjects design … ANCOVA on interpersonal closeness with source identity, source label, their interaction". |
| "492 participants altogether" | **Partly supported; numbers do not reconcile** | L3 (Freiburg press release / StudyFinds): "A study involving 492 participants from the Universities of Freiburg and Heidelberg". But L2 fragments of the preprint/article text give "conditions of study 1 (n = 322)" and "interpersonal closeness (n = 334)" for Study 2, and elsewhere "n = 164" for a deep-talk subset of Study 1. 322 + 334 = 656, not 492. The 492 may be the analysed sample after exclusions, or the press release may be imprecise. **Report "two studies; press-release total 492; per-study analysed Ns not confirmed."** |
| "pre-generated AI replies could elicit closeness in deep talk, especially under human labeling" | Supported | L2/L3: responses "pre-generated either by a minimally prompted LLM or by humans"; "In deep-talk exchanges, AI-generated replies produced more closeness than human replies. In small talk, the two were roughly equal"; "Participants told they were speaking to an AI reported lower closeness, even though the replies were identical. Closeness still rose in the AI-labelled condition, just less than in the human-labelled one." Press release: "When participants were informed in advance that they would be communicating with AI, the perceived closeness decreased significantly and they invested less effort in their responses." |
| "Live neural drift during the exchange was unnecessary for that measured effect" | Reasonable inference from design | Replies were pre-generated, so no live model computation occurred during the interaction. This is the audit's inference, not a claim in the paper. |

**Unverified:** Which LLM generated the replies (one L3 source says PaLM 2; not confirmed). Participants were university students aged 18–35 (L3).

**Overstated?** "492 participants altogether" is a press-release figure that conflicts with the per-study Ns visible in the article text; should be hedged. Otherwise accurate.

**Level reached:** L2 fragments of the article/preprint PDF + L3 press.

**Grid cell licence:** Licenses a *turn/reply*-level (or short-exchange) cell: a human-subjects RCT showing that fixed, pre-generated reply text can produce closeness ratings, modulated by the source label. Does not speak to runstance-level drift; it shows drift is not necessary for the effect measured.

---

## 3. Yin, Jia & Wakslak, *PNAS*, doi 10.1073/pnas.2319112121 (audit key [Yin])

**Citation facts found (L2 pnas.org fragments + L3)**
- Title: "AI can help people feel heard, but an AI label diminishes this impact".
- Authors: Yidan Yin, Nan Jia, Cheryl J. Wakslak (USC Marshall).
- Journal: *PNAS* **2024**, vol. 121, no. 14 (ADS bibcode 2024PNAS..12119112Y); press coverage April 2024. **The paper is from 2024, not 2025/26.** The audit's prose does not date it, so no error in the audit, but the "Independent human-subjects evidence" row groups it with 2026 work without noting it predates the GPT-4o episode by ~2 years.
- OSF data: osf.io/8wnmr (L2 fragment).

**Claims vs. evidence**
| Audit claim | Verdict | Evidence |
|---|---|---|
| "separated the actual and presumed source of a supportive response" | Supported | L2 pnas.org fragment: the design separates "the heightened cognitive capabilities of AI to generate responses that make people feel heard ('response effect') and the potential dampening impact of labeling a response as AI-generated ('label effect')"; 2 (source: AI vs human) x 2 (label: AI vs human). |
| "AI-written replies made people feel more heard on average than human replies" | Supported with one qualifier | L3 ScienceDaily/USC: AI-generated messages "made recipients feel more heard than messages generated by **untrained humans**". The comparison class is untrained human responders, which the audit omits. |
| "while an AI label reduced that rating" | Supported | L2/L3: "recipients reported feeling less heard when they learned a message came from AI"; "People felt most heard and understood when an AI-generated response was believed to be human-written"; the two effects "were of similar size". |

**Unverified:** sample sizes per study, number of studies, which LLM produced the responses (one summary mentions Bing Chat; not confirmed).

**Overstated?** Minor: the human comparison is "untrained humans". Otherwise accurate.

**Level reached:** L2 fragments + L3.

**Grid cell licence:** Licenses a *turn*-level cell: a single reply's content and its label independently move "feeling heard". Says nothing about cumulative trust across turns.

---

## 4. Jiang et al., CHI, doi 10.1145/3772318.3790714 (audit key [Recall])

**Citation facts found (L2 dl.acm.org fragments)**
- Title: "RECALLbot: Designing Agentic Memory and Reciprocal Disclosure for Human–Chatbot Relationships".
- Authors: Z. (Zhaojun) Jiang, C. Zheng, H. Chen, L. Chen (given names of co-authors not retrieved).
- Venue: CHI '26 proceedings, Article 795, pp. 1–20.

**Claims vs. evidence**
| Audit claim | Verdict | Evidence |
|---|---|---|
| "two-week study of 40 social-chatbot users" | Supported | L2: "two-week between-subjects study (N = 40)"; participants "were active users of social chatbots". |
| "a package combining memory and reciprocal disclosure increased reported trust and disclosure" / "frequency/depth of disclosure relative to baseline" | Supported at abstract level | L2: RECALLbot "builds agentic memories, including a 'Me Memory' and a co-constructed 'We Memory,' and uses reciprocal disclosure strategies"; compared "with a baseline system lacking agentic memories and reciprocal disclosure strategies"; it "significantly enhanced users' perception of the chatbot as a social identity, elicited more frequent and deeper disclosures, and fostered greater trust compared to a baseline". |
| "The intervention spans sessions and bundles mechanisms" | Accurate gloss | Memory + reciprocal disclosure are bundled in one arm; two-week deployment. |

**Not verified:** effect sizes, trust instrument, whether the baseline chatbot had any memory at all. Search also surfaced an IJHCI 2026 experiment (N=169) where reciprocal self-disclosure increased disclosure but did not significantly raise trust, which is a useful counterweight the audit does not cite.

**Overstated?** No. The audit's claim is the abstract's claim.

**Level reached:** L2 (ACM record fragments).

**Grid cell licence:** Licenses a *runstance/product*-level cell: a small (N=40) deployment showing that cross-session memory plus disclosure design raises self-reported trust and disclosure. Bundled intervention; cannot attribute the effect to memory alone.

---

## 5. Lai, CHI, doi 10.1145/3772318.3791351 (audit key [Keep])

**Citation facts found (L2 arxiv.org + dl.acm.org fragments)**
- Title: "Please, don't kill the only model that still feels human": Understanding the #Keep4o Backlash.
- Author: Huiqian Lai (sole author).
- Venue: CHI '26; arXiv 2602.00773, three versions, v3 dated 28 February 2026.

**Claims vs. evidence**
| Audit claim | Verdict | Evidence |
|---|---|---|
| "analysis of 1,482 posts in the #Keep4o movement" | Supported | L2: "mixed-methods study of 1,482 social media posts"; data from X collected with the query "#keep4o". |
| "identified loss of workflows, relationship disruption and loss of choice" | Supported | L2 fragments: resistance rests on "instrumental dependency, where the AI is deeply integrated into professional workflows, and relational attachment, where users form strong parasocial bonds"; "the perceived loss of choice selectively channeled user grievances into claims about agency, consent, and user rights"; "loss of user choice and control" described as a bridge between workflow disruption and relational grievance; a "choice-deprivation scale" was applied to the 1,482 posts. |

**Do not confuse with:** Yiwen Wu, "The User Side of AI Model Lifecycles: Evidence from the Keep4o Movement", arXiv 2608.16574 (~61,846 X posts, Aug 2025–Mar 2026), a different study.

**Overstated?** No.

**Level reached:** L2.

**Grid cell licence:** Licenses a *product*-level, observational cell on what users say they lost when a named model was withdrawn; self-selected hashtag sample.

---

## 6. Yuan et al., arXiv 2609.15482 (audit key [Migration])

**Citation facts found (L2 arxiv.org abstract fragments)**
- Title: "When AI Companions Disappear: Relational Continuity and Collective Contestation during China's National AI Regulatory Transition".
- Authors: Yunhao Yuan, Kejia Zhang, Yuqi Niu, Yajing Wang, Renwen Zhang, Talayeh Aledavood.
- Submitted 14 September 2026, cs.HC (also listed under cs.CY). v1 only seen.
- HF mirror: not available (ENOENT).

**Claims vs. evidence**
| Audit claim | Verdict | Evidence |
|---|---|---|
| "A qualitative study of migration after retirement" | **Mischaracterised in context** | The paper is about **China's 2026 regulation of anthropomorphic AI interaction services** and how users of (Chinese) companion platforms reacted when providers implemented shared national rules; it is **not** about the GPT-4o retirement that the surrounding paragraph discusses. Method is content analysis of public RedNote posts and threads, 10 April–10 August 2026 (one snippet: 89 posts, 1,425 comments, 2,005 replies), not interviews. Calling it "migration after retirement" without naming the regulatory context invites the reader to read it as a GPT-4o study. |
| "some users preserved conversation records yet struggled to restore familiarity" | Supported | L2 abstract fragments: "Users kept, moved, or rebuilt their companions, and keeping the old conversation records did not reliably bring back the shared memories or familiar interactions"; "Users judged continuity by whether the companion could recall shared history and whether the interaction still felt recognizable." |

**Overstated?** The finding is correctly reported; the framing is misleading. The audit should say: "a social-media analysis of Chinese companion-app users during a 2026 regulatory transition". "Qualitative" is defensible; "after retirement" is not quite right (companions were restricted/removed by regulation, and some providers' products changed rather than being retired).

**Level reached:** L2.

**Grid cell licence:** Licenses the same kind of *product*-level observational cell as Lai: human-side reports that saved transcripts do not restore felt continuity. Supports the audit's point that felt continuity is a human-side measure distinct from recognition of a checkpoint.

---

## 7. OpenAI release notes (help article 6825453) and retirement article (help article 20001051) (audit keys [4oAug], [4oHelp])

Both pages unreachable (help.openai.com denied). Level: L2 snippets of the help pages + L3 press.

**August 12, 2025 release note**
- L2 snippet of the release-notes page: "4o is back in the model picker for all paid users by default. Paid users also now have a 'Show additional models' toggle in ChatGPT web settings" (covering o3, o4-mini, GPT-4.1, GPT-5 Thinking mini). GPT-4.5 remained Pro-only.
- Context (L3: TechCrunch 12 Aug 2025, Simon Willison 8 Aug 2025): at the GPT-5 launch (7 Aug 2025) older models were removed; GPT-4o first came back for Plus under a "show legacy models" setting, then into the main picker on Aug 12.
- **Verdict:** Audit claim "OpenAI's August 12 release notes record GPT-4o's return to the model picker for all paid users" is supported at snippet level, with the release note's own wording "for all paid users by default".

**Retirement article 20001051**
- L2 snippets: GPT-4o and several other models (GPT-4.1, GPT-4.1 mini, o4-mini, GPT-5 Instant and Thinking) "were removed from ChatGPT on February 13, 2026"; "these models will continue to be available in the API"; "ChatGPT Business, Enterprise, and Edu customers will retain access to GPT-4o within Custom GPTs until April 3, 2026. After April 3, GPT-4o will be fully retired across all plans"; GPT-5.1 models retired 11 March 2026.
- **Verdict:** Audit claims (13 February 2026 retirement; custom-GPT exception for "specified organizational plans" through 3 April; API treated separately) are supported at snippet level. The specific plans are Business, Enterprise and Edu.

**Caveat:** Both pages are living documents; wording quoted here is from search snippets captured on 5 Nov 2026 and may have been edited. The audit's "[4o]" key (openai.com/index/retiring-gpt-4o-and-older-models/) was not checked.

**Grid cell licence:** Licenses *product*-availability facts only (what was available to whom, when). No user-reaction evidence.

---

## 8. The two HCI items

### 8a. Uncertainty-expression experiment, FAccT, doi 10.1145/3630106.3658941 (audit key [Uncertainty])

**Level reached: L1 primary text** (HF mirror hf://papers/2405.00623/paper.md, first 20,000 chars incl. abstract, intro, related work).

- Title: "I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust.
- Authors: Sunnie S. Y. Kim (Princeton; work done at Microsoft), Q. Vera Liao, Mihaela Vorvoreanu, Stephanie Ballard, Jennifer Wortman Vaughan (Microsoft).
- Venue: FAccT '24, 3–6 June 2024, Rio de Janeiro; ACM ISBN 979-8-4007-0450-5/24/06; pp. 822–835 (page range from L2).
- Abstract (verbatim, L1): "We explore this question through a large-scale, pre-registered, human-subject experiment (N=404) in which participants answer medical questions with or without access to responses from a fictional LLM-infused search engine. … We find that first-person expressions (e.g., 'I'm not sure, but...') decrease participants' confidence in the system and tendency to agree with the system's answers, while increasing participants' accuracy. An exploratory analysis suggests that this increase can be attributed to reduced (but not fully eliminated) overreliance on incorrect answers. While we observe similar effects for uncertainty expressed from a general perspective (e.g., 'It's not clear, but...'), these effects are weaker and not statistically significant."
- Design detail (L1): conditions NO-AI, CONTROL, UNCERTAIN1ST, UNCERTAINGENERAL; uncertainty was randomly present on both correct and incorrect responses; measures include agreement, confidence, source usage, trust intentions, accuracy, time.

**Audit use:** "HCI can test the effects of displayed uncertainty phrases … A phrase may span several tokens." Accurate: the manipulation is a hedging phrase in displayed text; outputs were scripted (fictional system), so there is no live model and no token-level unit. Supports the audit's point that this is not a test of a relationship with a forward pass.

**Grid cell licence:** Licenses a *turn/position*-adjacent cell about phrase-level effects on reliance and trust in a one-shot judge-advisor task. Not a relationship measure.

### 8b. Response-latency experiment, CHI, doi 10.1145/3772318.3790716 (audit key [Latency])

**Level reached: L2** (arxiv.org abstract fragments; CHI record resolves per search), L3 for N.

- Title: "The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception".
- Authors: Felicia Fang-Yi Tan, Moritz A. Messerschmidt, Wen Yin, Oded Nov (NYU Tandon per press).
- Venue: CHI '26; arXiv 2604.06183 (posted ~Feb 2026 per search; ID suggests April 2026).
- Design: between-subjects 3 (time-to-first-token latency: 2, 9, 20 s) x 2 (task type: Creation, Advice); N = 240 (L3 TechXplore; also "13 out of 240 participants (5.4%) made any edits, 16 out of 240 (6.7%) regenerated" in L2 fragment).
- Findings (L2 abstract fragments): "user interaction behaviors were robust to latency, yet varied by task type"; Creation tasks drew more frequent prompting. Perception: latency affected ratings of Thoughtfulness and Usefulness (L3 alphaXiv overview); one reported main effect F(2, 234) = 5.12, p = .007 (measure not identified in snippet). Press framing: longer waits read as more thoughtful.

**Audit use:** "A latency manipulation can hold the answer fixed." Whether this paper held answer content fixed across latency conditions was **not confirmed** from reachable text; the abstract says latency was varied at time-to-first-token. Treat the audit sentence as a design remark rather than a description of this study.

**Grid cell licence:** Licenses a *turn*-level cell: perceived qualities of a single response shift with delivery timing, behaviour mostly does not. Not a relationship measure; not a test of any minimum interpersonal grain.

---

## Summary table

| # | Source | Level reached | Citation OK? | Claim verdict | Flag |
|---|---|---|---|---|---|
| 1 | De Freitas et al., NHB 2026 | L2/L3 | Title, journal, DOI yes; authors and PMID unverified | 54,861 posts: yes (L3). 1,452 / seven surveys: L3 only. 13.0 pp and 24.7 pp: consistent with press before/after %; **95% CIs unverified** | Hedge the CIs; fix "GPT-4o rollout" to "GPT-5 rollout" wherever it appears |
| 2 | Kleinert et al., Comm. Psychol. 4:23 (2026) | L2/L3 | Yes | Two RCTs yes; closeness in deep talk, label effect yes; **492 total conflicts with per-study n=322 / n=334 fragments** | Hedge the N |
| 3 | Yin, Jia & Wakslak, PNAS 121(14), 2024 | L2/L3 | Yes; **2024 paper** | Yes; comparison class is "untrained humans" | Add year |
| 4 | Jiang et al. (Jiang, Zheng, Chen, Chen), CHI '26 art. 795 | L2 | Yes | Yes (abstract-level) | None |
| 5 | Lai, CHI '26; arXiv 2602.00773 | L2 | Yes (sole author Huiqian Lai) | Yes, all three themes found | None |
| 6 | Yuan et al., arXiv 2609.15482 | L2 | Yes | Finding yes; **framing misleading: China 2026 regulatory transition, RedNote posts, not GPT-4o retirement, not interviews** | Reword |
| 7 | OpenAI help 6825453 / 20001051 | L2 snippets | Pages exist | Aug 12 "all paid users by default" yes; 13 Feb 2026, Business/Enterprise/Edu custom-GPT exception to 3 Apr, API separate: yes | Living pages |
| 8a | Kim et al., FAccT '24 | **L1** | Yes | Yes | None |
| 8b | Tan et al., CHI '26; arXiv 2604.06183 | L2/L3 | Yes | Yes; "answer held fixed" not confirmed | Minor |

## Hosts that would need to be allowed for a primary-text pass
nature.com (items 1, 2), pnas.org (3), dl.acm.org (4, 5, 8b), arxiv.org (5, 6, 8b), help.openai.com (7), pubmed.ncbi.nlm.nih.gov or api.crossref.org (all metadata).
