# Review of v9 (5 Nov 2026) — hostile but fair

Scope: `/home/user/lens-matrix/data/board.json`, `sources.json`, `trail.json`, `notes.html`, the rendered `lens-by-level.html`, and the screenshot `shots/v9-fig-light.png` (plus the dark and 400-px shots), checked against the five verifier reports `verify_astra_A–E.md`, the earlier `audit_*.md`, the local emotions-paper text, the v8 hand-built page (`v8_hand.html`) and the external audit as a claim list. I did not fix anything.

Severity scale: **HIGH** = a reader who checks the source will find the board wrong; **MED** = overstated, unhedged or inconsistent with the board's own rule; **LOW** = wording a careful reader would pounce on but that does not mislead.

---

## 1. FACTUAL (changed cells and source entries against the verifier reports)

**F1 (HIGH). Two source titles are invented and attributed to pages nobody reached.**
- `sources.json` Atkinson 26: "*Learned self-report of installed preference rules* (title per project page)". Verifier B, §1, citation facts: the paper is **"Identifying Introspection From the Inside"** (arXiv 2610.07186); "The project site itself could not be fetched." The board's title is a description, not the title, and the "per project page" provenance is false. The key strip repeats it ("learned self-report of installed rules").
- `sources.json` Han 26: "*Reward and punishment directions in a language model* (title per listing)". Verifier E, §1: the title is **"How's it going? Reinforcement learning in language models recruits a functional welfare axis."** Again a descriptive phrase presented as a title with a provenance claim. The key strip repeats it ("reward and punishment directions").

**F2 (HIGH). Notes misstate what the verifiers caught on the Pain Axis paper.** `notes.html`, "What changed in v9", item 1: "the pain-axis paper's withdrawal of its relief reading placed in v3 when it is already in v2." Verifier A, §2, claims 3–4 and "What the audit got wrong": the audit correctly placed the changed interpretation in v2 ("The 25 September revision changed that interpretation"); what the audit misplaced into v3 was the **"nothing in return" harm-only control** ("Sequencing: the 'nothing in return' harm-only control and the random-direction sham comparison are v2 findings ... not v3"). The board credits itself with a catch it did not make and describes the audit's error wrongly.

**F3 (HIGH). The board states a press-release sample size as fact in the cell while saying such numbers were excluded.** Relational × Model gloss: "across 54,861 subreddit posts". Verifier D, §1: "54,861 subreddit posts — Supported (L3)... Harvard Gazette snippet... Not seen in the paper's own text." The notes say the verifiers caught "two sample sizes and one confidence interval that exist only in press releases" and the trail says CIs were "omitted" — yet the third press-only number (54,861) is kept in the cell, and the two omitted ones (492, 1,452) are the same evidence class. Either all three go to the sources entry with the "press level" hedge, or the notes stop claiming the rule. Also: the 54,861 pool covers *both* the Replika and ChatGPT subreddits (Gazette: "posts from subreddits devoted to Replika and ChatGPT"); the gloss attaches it to the ChatGPT 13-point rise alone.

**F4 (MED). "One confidence interval that exist only in press releases."** Verifier D, §1: the two 95% CIs (10.8–15.2; 20.1–29.2) "were not found in any reachable source. They may well be in the paper." They are not in press releases either, and there are two of them, not one. The notes' sentence is wrong on count and on provenance.

**F5 (MED). Behaviour × Runstance: "In 45,000 simulated chats, how the history is shown to each side changes role confusion."** Verifier E, §9, caveat (iv): "the 45,000 are the generated corpus, and the ablation showing the history effect is on a subset (size not recovered)." The effect was not shown in 45,000 chats. Also caveat (i): "both parties are API LLMs in a Client–Responder simulation, not human–assistant chats", and (ii) "'role confusion' is operationalized mainly as echoing". Under a ◆ headline about "the default persona", a reader will take this as assistant-persona drift; it is echoing between two simulated agents. The trail's "verified at primary text" is true of the numbers, not of the framing.

**F6 (MED). `sources.json` Singh 26: "v2 (Aug 2026) and the COLM 2026 header not reached."** False on the header. Verifier B, §5: "search snippets show the arXiv PDF header 'Published as a conference paper at COLM 2026'"; Verifier C, item 1: "Snippet of the arXiv PDF header: 'Published as a conference paper at COLM 2026'". The header *was* reached, at snippet level; what was not reached is a programme listing. The entry says the opposite of the record.

**F7 (MED). `sources.json` Mazeika 25: "NeurIPS 2025, verified at the proceedings record."** Verifier E, §5: the venue facts (virtual poster page, proceedings hash, DOI) are all marked **C** = "secondary only: search-engine extracts". Nobody opened the proceedings record (proceedings.nips.cc was blocked, per E's network list). "Verified at the proceedings record" overstates the evidence level by two grades; the rule only needs "listing seen in search results", so there was no reason to inflate it.

**F8 (MED). Hedonic × Model states an argued inference and an unconfirmed model name as fact.** Gloss: "Reward-and-punishment directions learned in a maze transfer to other settings and are already present before the maze training (Qwen3-4B)". Verifier E, §1: "already present before" is the abstract's *argument* ("we therefore argue that this functional welfare axis pre-exists post-training"), and the pre-existence evidence "is indirect; post-maze vectors are applied to pre-maze and base checkpoints rather than contrast vectors being extracted independently". The model: "Primary model per secondary sources: Qwen3-4B ... names/sizes beyond Qwen3-4B are unconfirmed" — level C. The cell should say the directions *work on* pre-maze checkpoints, and the model name is secondary.

**F9 (MED). Hedonic × Instance: "a self-harm direction follows the reply position across reassigned characters and fades under a fiction frame."** Verifier A, §2, claim 7: **PARTLY SUPPORTED (snippets only; v3 text not readable)**; the authors' own wording is "consistent with the pain axis tracking the reply position". The gloss states as fact what the authors state as consistency, from an appendix nobody read. The trail admits "reached only in snippets", but the cell carries no hedge other than the unexplained tag "v3" (see I4). Separately, "self-harm direction" is a misnomer: the paper's construct is *self-directed harm* (harm to the model); "self-harm" in English means something else.

**F10 (MED). Preference × Runstance: "with no matching pull toward the positive one."** Verifier A, §1, claim 5: self-administration at first offer was "13.5% at +1 vs 6.5% random (Fisher p = 0.029) vs 10.0% no steering (p = 0.35)" — i.e. positive self-administration *did* exceed the random control, significantly; it did not exceed the no-steering baseline. "No matching pull" is defensible only against the no-steering baseline, which the cell does not name, while the negative-removal figure (35% vs 7%) *is* compared to random. Same comparison class for both halves, or say which.

**F11 (LOW). Dynamics × Instance: "ten open models claimed it as intended about a quarter of the time."** Verifier E, §12: the 25.3% is "Among prompts where the prefill changes the model's safety behavior". The conditioning is dropped. "A signal carried largely by the refusal direction": paper says orthogonalising collapses the gap "though the direction is not its unique mediator" — "largely" is fair, but the hedge is gone.

**F12 (LOW). Dynamics × Runstance: "shifted which zone the model picked."** Verifier A, §1: "choice margins are read from logits with steering off, i.e. a forced choice between two labels, not sampled behaviour." Nothing was picked; a log-odds margin moved. Also, the "five of seven" sentence rests on "the quoted paper sentence" in a snippet ("Caveat: I could not read the per-model fixed-text slopes myself") — fine for a preprint tier, but the notes' "measured channel" language should not imply the running text was read; the paper's prose was never reached by anyone.

**F13 (LOW). Relational × Token: "time to the first token changed how thoughtful a reply seemed."** Verifier D, §8b: the Thoughtfulness/Usefulness effect is from an "L3 alphaXiv overview"; the one F-test in an L2 fragment has its "measure not identified". Stated flat.

**F14 (LOW). Self-report × Instance: "a 32B model trained to decide by hidden rules later described them, using the deciding machinery."** Verifier B, §1: self-report was "elicited 'in a separate context window'", not later in the same run; and "interventions implicated the machinery" is the verifier's accurate wording, "using" is a step stronger; result is "population-level, LoRA-adapter", and "4B and 8B models end up with noticeably negative faithfulness". "Later" and "using" both tilt it.

**F15 (LOW). Relational × Model: "After GPT-4o's removal from ChatGPT".** Verifier D, §1: De Freitas studied the **August 2025 GPT-5 rollout** that removed 4o (then reversed). The board's own sources entry for OpenAI 25–26 lists a *second* removal (29 Jan / Feb 2026). The gloss does not say which; a reader who knows the timeline will ask.

Checked and clean: Betley 20%/6%/48 (Verifier C, item 2); Ferrara 11,216 / 75.0 / 95.8 on two 7B models (Verifier B, §4); Chua single-turn vs multi-turn split and agentic null (B, §6); Macar 10.8→63.8 / 0→7.3 and OLMo 3.1 32B (unchanged, confirmed by the v8 review); Gilg −4.52/+1.15, Qwen 3.5 122B, user-turn narrowing (C, item 3); Jhaveri 49.2→64.7, −0.040 vs −0.042 (A, §4); Berg 35.4% vs ~7% removal, OLMo only (A, §1); the "eight prompts" and "user's '.' token, r=0.59" for Mech interp × Token (local paper text, §2.2.2: "the same eight prompts from above ... the punctuation ending the user's message '.'"); Yin "untrained humans" (D, §3); Kim N=404 (D, §8a); Lai 1,482 and three themes (D, §5); Jiang N=40 two weeks (D, §4); Kleinert two preregistered trials, deep talk, label effect (D, §2); Birch "each token" in §9 and conversational step in the illusion section, both at snippet level (C, item 4); Kirkpatrick abstract (C, item 4).

---

## 2. TIER (every cell's fill under the page's rule)

The rule, from the legend line: "Peer-reviewed needs a venue listing seen, if only in search results; an acceptance note alone stays preprint." It is applied four different ways on this board.

**T1 (HIGH). Dynamics × Instance is top tier on a venue listing the verifier does not record seeing.** Cell went 1 → 3 (trail: "fill follows the strongest clause"); the strongest clause is Nguyen 26 · EMNLP. Verifier E, §12, citation facts: "EMNLP 2026 Main, anthology 2026.emnlp-main.1113 (C; page blocked; the authors' GitHub README states 'EMNLP 2026 Main')." Contrast E's wording for Luo & Laban (§9): "anthology ID 2026.findings-acl.412 **appears in search results with this title**." For Nguyen the only evidence the verifier names is the authors' README — an acceptance note — plus the audit's own link. Under the rule as written that stays preprint, so this cell is ●●○ until someone records the anthology listing in a search result. This is the biggest single upgrade in v9 and it is the least documented.

**T2 (MED). Macar 26 is held at preprint in three cells while the board's own text calls it ICML.** Self-report × Token, Dynamics × Model, Dynamics × Token are all ●●○ with the bare tag "Macar 26". `sources.json`: "ICML 2026 (PMLR 306) **per search listings**" — the identical phrase used for Lu 26, which is ●●● everywhere. Key strip: "Mechanisms of Introspective Awareness (ICML 2026)". Verifier C, item 1: the PMLR URL is "Confirmed as a URL that search engines index with the expected content" with page numbers "PMLR 306:85403-85429". That is a venue listing seen in search results. Either the two Macar-only dynamics cells are ●●● (and Self-report × Token's "·" clause lifts too), or the rule needs a clause the page does not state. The v8 review flagged this (T3) and it is still here, now with the key strip saying "(ICML 2026)" against a mid-blue cell.

**T3 (MED). Gilg 26 (Preference × Instance) is ●●○ although the sources entry claims "a poster listing".** `sources.json`: "NeurIPS 2026 per the authors and a poster listing." Verifier C, item 1: "a neurips.cc/virtual/2026/poster/152444 URL appears in results", but also "one aggregator (Lacuna) lists it as ICML 2026, and an icml.cc/virtual/2026/79297 URL also appears". If the conflicting listing is the reason to hold, say so in the entry; as written, the entry asserts the condition for ●●● and the cell is ●●○ with no venue tag.

**T4 (MED). Atkinson 26 (Self-report × Instance) — trail says "both carry COLM headers, held at preprint by rule", but the verifier saw more than a header.** Verifier B, §1: "search snippets show the arXiv PDF header ... **and a COLM virtual poster page (colm.cc/virtual/2026/poster/2483, not fetchable here)**". A poster page in search results is a listing by the rule's own test; Singh (B §5, C item 1: "No official COLM programme page found") is correctly held. The trail's "both ... by rule" is not what the record says. With "·" the Atkinson clause would carry the cell to ●●●. (The user's question — was a PDF-header venue correctly held at preprint? — yes for Singh; for Atkinson the question is moot because there is more than the header.)

Net: by the rule as written, T1 goes down and T2–T4 go up; by the stricter reading (listing must be a proceedings/anthology page, not a virtual-poster URL), T1 goes down and T3–T4 stay, but T2 still goes up because PMLR *is* a proceedings page. There is no reading under which the current fills are all consistent.

**T5 (MED). Relational × Token is ●●● for evidence the cell itself says is not about the level.** Gloss ends: "No test reaches a single internal pass." The audit's verdict for this cell was "leave the lower bound open" and "No direct test establishing a minimum interpersonal grain was identified." The board turned an argued cell into a top-tier one by citing two studies of *display cues* (a hedge phrase, time to first token) and then conceding they do not reach the level. Top tier should mean the lens can say something peer-reviewed *about this level*; here the peer-reviewed part is about a different level and the level claim is still argued. Compare Hedonic × Token, which is correctly left ○○○ for the same shape of situation.

**T6 (LOW). Preference × Model ●●● rests on Mazeika alone.** Wang is level C, Ajayi level C ("extract level" in sources), Chalmers argued. Fine under "·", but the cell reads as if three studies were graded; only one was read.

**T7 (LOW). Hedonic × Model ●●○ with Han at abstract level and the model unconfirmed (F8).** Preprint tier is right; the fill is right; the cell text is what overreaches.

Fills otherwise consistent with the rule: Mech interp × Model (Lu, listing seen, C item 1); Behaviour × Model (Betley ICML PMLR v267 + Nature DOI via Gilg's bibliography, C item 1–2); Behaviour × Runstance (Lu + Luo anthology ID in search, E §9); Relational × Model/Runstance/Instance (nature.com, dl.acm.org, pnas.org record fragments, D §§1–5); Relational × Token's *venues* (Kim ACM pp. 822–835, Tan CHI record, D §8); the two architecture cells; Mech interp × Instance ●○○ on "+ ... prelim"; Self-report × Runstance ●●○ on Martorell preprint; Dynamics × Runstance ●●○ on Berg preprint; Hedonic × Token ○○○; Self-report × Model ●●○ via "+" at its weakest (Chua).

---

## 3. LEVEL (timescale column fit of new or changed claims)

**L1 (MED). Kleinert 26 at Runstance.** Verifier D, §2, grid licence: "Licenses a *turn/reply*-level (or short-exchange) cell ... Does not speak to runstance-level drift; it shows drift is not necessary for the effect measured." The board put it in the conversation column and built the headline on it ("even with pre-written replies"). The audit put it there too; the verifier's hedge was not imported.

**L2 (MED). Nguyen 26 at Instance.** The dissociation is between a prefilled turn and the model's account of it in a *following* turn ("asked about an adversarially prefilled reply"). By the board's own column definition ("one turn"), act and account are in different turns, which is the runstance column — exactly where the board places B&B's cache edit, which has the same two-turn shape. Astra's "Turn" placement was imported without argument.

**L3 (MED). Relational × Token (see T5).** A hedge phrase "may span several tokens" (audit's own words) and TTFT is a latency, not a position. The column sub-header says "one position, distribution, symbol or pass: the cell says which"; this cell says "none of them".

**L4 (LOW). Behaviour × Runstance, Luo clause.** LLM–LLM dyads; the column is "one conversation" and the row is "what it does" — but the "it" in Luo is a simulated client/responder pair, not the model-as-assistant. Fits the column, not the row.

**L5 (LOW). Self-report × Instance, Atkinson clause.** The installed rule is a model-level (LoRA) property and the report is in a separate context; "instance" is defensible as "what one turn can access", but the gloss's "later" implies a within-run timescale that does not exist.

Fits: Martorell at Runstance (ten-turn conversations, question displaces state); Berg fixed-text at Runstance; Jhaveri at Runstance; Han at Model; Mazeika/Wang/Ajayi at Model; Tagliabue App. I at Instance (reply position); Yin at Instance; De Freitas/Lai at Model with the "product" tag; the two architecture cells.

---

## 4. INTERNAL (counts, tags, trail)

**I1 (HIGH). "Four peer-reviewed human-subjects studies replaced four argued cells in one pass."** (`notes.html`, pattern bullet 1.) Both numbers are wrong against the data. The relational row cites **seven** human-subjects studies (De Freitas, Lai, Jiang, Kleinert, Yin, Kim, Tan). And only **three** relational cells were argued in v8 (runstance, instance, token were ○○○; `trail.json` and `v8_hand.html` agree); Relational × Model was ●●○ ("Attachment to a name, or a region", documented event). The trail's `from.tier: 2` for relational/model contradicts the bullet on the same page.

**I2 (MED). "Beckmann and Butlin in two papers and a third as co-authors"** (`notes.html`, Still soft). On the board they are authors of B&B 26 and co-authors of Gilg 26. That is two. No third source on the board lists either. "Lindsey in three" checks (Lu 26, Lindsey 25, Macar 26).

**I3 (MED). Still-soft names a source that is not on the board.** "Martorell & Bianchi, Han, Wang, Ajayi, **Sturgeon** and the De Freitas intervals were not reached" — Sturgeon 26 has no tag, no sources entry, no key, and appears in no cell. Meanwhile the list omits Jhaveri (snippet level, A §4), Tagliabue v3 (snippets, A §2), Berg (paper prose never read, A §1), Tan (snippet, D §8b) and Kirkpatrick (abstract, C item 4), all of which *are* on the board.

**I4 (MED). The tag "v3" is undefined.** Hedonic × Instance tags: "Anthropic 26 · Tagliabue 26 · v3". The legend defines ICML, prelim, case study, n=1, ↔, +, ·. "v3" is a new suffix with no entry in the legend, the keys or the sources; under the "·" grammar it parses as a third source named "v3". In the screenshot it also sits alone on its own line.

**I5 (MED). Two key-strip entries are orphans.** `sources.json`/`keys` contain **OpenAI 25–26** and **Kirkpatrick 26**; no cell tag uses either (script check: "sources never tagged in a cell: ['Kirkpatrick 26', 'OpenAI 25–26']"). The key strip is defined as the tag key; it now explains two tags that do not occur, and lengthens the strip by a line. (Kirkpatrick is named in the Instance strip text, but the strip does not use tags.) If OpenAI 25–26 is kept for the Feb 2026 retirement fact, some cell should cite it; otherwise drop both from `keys` and leave them in the source list.

**I6 (LOW). Trail "why" for self-report/instance misreports the verifier record** (see T4): "both carry COLM headers, held at preprint by rule" — Atkinson also had a poster page in search results (B §1).

**I7 (LOW). Changelog "about thirty sources this board lacked"** — unverifiable from the data; the audit's reference list has ~50 keys, of which the board adopted 18 new tags. Say the number you can count.

**I8 (LOW). "The top-left hedonic cell"** (Still soft) — Hedonic × Model is row 5, column 1; it is the left-hand cell of its row, not top-left of anything.

Counts that check: eleven ◆ cells (script count = 11; notes say eleven; the HTML has 15 "◆" characters = 11 cells + sub + legend + 2 strip entries); 22 changed cells (diff of v8_hand vs v9 = 22, matching the 22 trail entries, every `from` headline and tier matches v8); "three papers report the same thing" (Anthropic, Gilg, B&B — yes); "five of seven lineages" (A §1); all cell tag parts resolve to a source or a defined marker (except "v3"); sources and keys are the same 35-tag set; glyphs match tiers in all 28 cells; the Birch strip says both grains as the changelog claims; "product" is used (Relational × Model).

---

## 5. LOGIC and WORDING

**W1 (HIGH). Mech interp × Runstance headline contradicts its own gloss.** Headline: "Earlier positions reach later ones **only through the cache**." Gloss: "serving may evict, recompute or share them, and rebuilding from identical inputs recovers the same information." If the cache can be evicted and rebuilt, earlier positions reach later ones through *attention over their keys and values*; the cache is where those are kept between calls. Astra's whole point for this cell was that the cache is a serving artefact, not the mechanism. The headline re-asserts the v8 error the gloss was rewritten to remove. (Also the `architecture` source entry's "no other state survives a turn" is fine; the headline's "only through the cache" is the problem.)

**W2 (HIGH). The architecture cell and the two Berg cells are consistent only with a caveat the board omits.** Mech interp × Runstance: "rebuilding from identical inputs recovers the same information." Hedonic × Runstance headline: "a planted one persists in the cache." Dynamics × Runstance: "through the cache or the text." A reader will ask: if a rebuild recovers the same information, the planted trace does not survive a rebuild, so in what sense does it "persist"? The answer (the cache was *constructed under intervention*, which the audit states: "A deliberately edited cache may carry information absent from those inputs") is nowhere on the figure. One clause in the architecture cell ("unless the cache was built under intervention") would close it.

**W3 (MED). Relational × Runstance headline says more than the gloss and mixes two studies' outcomes.** Headline: "Memory and disclosure build trust, even with pre-written replies." Jiang (live chatbot, two weeks) measured trust; Kleinert (pre-generated replies) measured *closeness*, not trust (D §2). Nobody showed trust from pre-written replies. The gloss keeps them apart; the headline fuses them.

**W4 (MED). Relational × Model carries ◆ with nothing persona-relative in it.** The v8 cell was ◆ because it argued "a name, or a region (B&B)". The v9 gloss is about a product and ends "Which computational object is attached to stays unresolved" — the ◆ is vestigial and now mis-counts: the "eleven persona-relative cells" bullet includes a cell that no longer says anything about a persona.

**W5 (MED). Dynamics × Instance headline "Account and act come apart, then get re-joined."** The Nguyen result is models *falsely* claiming ownership of text they did not write. "Re-joined" reads as repair; what happened is a confabulated join. The gloss is accurate; the headline inverts the valence. An X reader: "re-joined by lying?"

**W6 (MED). Astra's interpretive moves imported without the verifiers' hedges:**
- Preference × Model: "Chalmers's incoherence point is about one interlocutor across conversations, not this" — the audit's reframing (§6 Model), of a paper read "through quotation" (sources entry); `audit_originals.md` §2 says Chalmers's reason is that the model "would say contradictory things to different users", which is about the *model*, i.e. exactly the thing the cell measures across checkpoints. The reframing may be right; it is stated as settled in a ●●● cell.
- Hedonic × Instance: "follows the reply position" (F9) — authors say "consistent with".
- Behaviour × Runstance: Luo as "a second controllable cause of apparent drift" (trail) → gloss states the history effect as if assistant-persona drift (F5).
- Relational × Token: Astra said "leave the lower bound open"; the board filled it ●●● (T5).

**W7 (LOW). Hedonic × Model headline "in the weights".** The reward/punishment directions are activation-space vectors; the abstract's claim is that the axis "pre-exists post-training: it is recruited, rather than created". "In the weights" is the board's gloss on "pre-exists"; "a valence-like axis pre-exists the training" would be the paper's claim.

**W8 (LOW). Self-report × Model gloss.** "grew sad about shutdown in single turns" — Table 2 shows shutdown sadness in all three settings (B §6); "in single turns" reads as a restriction. "The same narrow-to-broad generalisation as emergent misalignment" is flagged by "+", fine, but the verifier's one omitted qualifier that matters — "a human-identity control shows broadly elevated scores ... often exceeding the conscious-claiming model" — would be the first thing a critic raises.

**W9 (LOW). Notes bullet "It closes the question of whether anything but text can carry history."** True for a planted cache; the sentence after qualifies it. Still, "closes" on a single-lab preprint whose prose nobody read (A §1) is the kind of verb the Still-soft section exists to retract.

**W10 (LOW). Tag suffix inconsistency.** Venue suffixes appear for Lu, Betley, Luo, Nguyen, Mazeika, Wang, De Freitas, Lai, Jiang, Kleinert, Yin, Kim, Tan — but not for Macar (ICML per the key) or Gilg (NeurIPS per sources). The missing suffixes are exactly the cells in T2–T3, so the inconsistency is visible on the figure.

---

## 6. DESIGN (from `shots/v9-fig-light.png`, 1200 × 2293; dark and 400-px shots also viewed)

**D1 (MED). The figure grew 20% taller (1913 → 2293 px at 1200 wide) and is now a 1.9:1 portrait.** The 400-px page shot is 9,157 px tall (v8: 7,588). It still renders as one image, but it is no longer a single-screen figure on any ordinary display; the welfare and relation rows alone are ~1,000 px.

**D2 (MED). Tag lines wrap badly in five cells.** Preference × Model: three tag lines, the second beginning with a bare "· AIES · Ajayi 26 ·". Hedonic × Instance: "v3" orphaned alone on line two. Self-report × Token: "Macar 26" alone on line two. Relational × Model: "CHI · product" alone. Relational × Runstance: "Comm Psych" alone. `build.py`'s `tagfmt` only protects "Name YY" for the thirteen v8 names (Lu, B&B, Anthropic, …, OpenAI); none of the 18 new names (Luo, Berg, Jhaveri, Nguyen, Han, Tagliabue, Mazeika, Wang, Ajayi, De Freitas, Lai, Jiang, Kleinert, Yin, Kim, Tan, Atkinson, Martorell) are in the regex, so "De Freitas 26" and "Kleinert 26" can split across lines at other widths. No clipping or overflow seen; the `.c u` flex keeps the glyphs aligned.

**D3 (MED). Row heights are uneven and driven by one cell per row.** Preference row is set by Preference × Model (6 gloss lines + 3 tag lines); the other three cells in the row have four to six empty lines. Relational row is set by Relational × Model (8 gloss lines). Hedonic row by the Instance cell. The instruments rows are uniform. Not an error, but the welfare/relation half of the figure now reads as padded.

**D4 (MED). The key strip is seven lines of 11-px mono at 1200 px.** 35 entries, including two orphans (I5) and the two invented titles (F1). It is legible on the light screenshot but it is the densest block on the page; in the dark shot the medium-grey text on #1a1a19 is at the edge of comfortable. At 400 px it is ~30 lines. Dropping the orphans and shortening the longest entries ("What We Talk to When We Talk to Language Models", "closeness with pre-generated replies (Comm Psych)") would recover a line or two.

**D5 (LOW). The strip under the headers is taller than the headers.** Runstance strip is six lines, Instance four; the header row above is two lines. It pushes the grid ~110 px down and the "candidate subjects in published views" italic label sits beside a six-line block. The uppercase strip labels ("NONE READ") read as tags.

**D6 (LOW). Dark mode.** Ramp reads correctly (light → dark for strong → weak); ●○○ cell (Mech interp × Instance) is darker than ●●○, which is the intended ordinal reversal for dark backgrounds, and the ○○○ cells sit on the surface colour. No contrast failures seen. The legend swatches match the cells.

**D7 (LOW). Phone width.** The grid scrolls horizontally inside `.scroll` (min-width 900 px) with a 16-px gutter; no page-level horizontal scroll; the intro paragraph and strip stack cleanly. Fine.

No clipping, no overflow, no mis-rendered glyphs; the ◆ marker renders in all eleven cells and in the strip.

---

## Verdict: wrong, as opposed to taste

Wrong, and should be fixed before this circulates:

1. **Two invented source titles** presented with false provenance (F1: Atkinson, Han). The verifiers supplied the real titles.
2. **The notes misdescribe the verifiers' own catches** (F2: the pain-axis misplacement was the harm-only control, not the relief withdrawal; F4: two CIs, not one, and not in press releases; I1: seven studies, three argued cells, not four and four; I2: B&B are in two papers, not three; I3: Sturgeon is not on the board).
3. **The tier rule is applied four ways** (T1–T4): Dynamics × Instance is ●●● on an acceptance note; Macar, Gilg and Atkinson are held at ●●○ on evidence that meets the rule as written. At minimum T1 comes down or the rule line changes.
4. **The architecture cell's headline contradicts its gloss** (W1) and the board never states the one caveat that makes it consistent with the two Berg cells (W2).
5. **A press-level number stated as fact in a cell while the notes claim press-level numbers were excluded** (F3), with the denominator misattributed to one subreddit.
6. **Sources entries that misreport the verifier record** (F6 Singh header "not reached" — it was; F7 Mazeika "verified at the proceedings record" — it was not).
7. **Luo's 45,000 claim** (F5): the effect was shown on a subset, in LLM–LLM dyads, under a headline about the default persona.
8. **An undefined tag** ("v3", I4), **two orphan key entries** (I5), and **a vestigial ◆** that is counted in the "eleven" (W4).
9. **Relational × Runstance headline** attributes trust to pre-written replies; the study measured closeness (W3).
10. **Relational × Token** is top tier for a claim the cell itself says has no test at this level (T5/L3).

Overstated but arguable (hedges to restore, not errors of fact): F8–F14, L1–L2, W5–W9.

Taste: D1–D7 (the tag wrapping in D2 is the one I would fix because it makes "v3" and "· AIES" look like data), the uppercase strip labels, the "top-left" phrase, the length of the key strip.

What held: every number the verifiers confirmed is correctly transcribed in the cells (Betley, Ferrara, Macar, Gilg, Jhaveri, Berg, Chua, Yin, Kim, Jiang, Lai, De Freitas point estimates); the 22-cell trail matches the actual diff from v8 exactly; the eleven-◆ count is right; the Birch strip does what the changelog says; the two architecture cells now say what Astra asked for; Singh is correctly held at preprint; the Martorell numbers were correctly left out.
