# Pre-posting review: lay reader + fact-checker

Read this at step 7 of SKILL.md. Run the review on the post texts *and* the rendered images
together, after the images are final enough that a wording change is unlikely to move layout.

## Why both roles in one pass

The lay reader finds where the thread loses people (jargon, compressed punchlines, an image that
says nothing in five seconds). The fact-checker finds where it says more than the sources do.
They interact: the fix for a confusing sentence is often a plainer sentence that is *also*
stronger than the evidence, so one reviewer holding both views catches the trade-off.

In the run this skill was built from, one such review found 12 must-fix errors in a thread that
had already been through several model reviews of the underlying material, including:

- "three papers that **never cite each other**": two of them cited each other and shared authors
  (one ctrl-F in the PDFs would have caught it);
- "a **bottom-right** cell": the highlighted cell was in row two; text and image disagreed;
- "**both are right**": the evidence supported "both *can* be right" and the source left the
  second claim's object explicitly unresolved;
- "the best-measured row": the card's own bars showed another row at least as well measured;
- "flips sign": true on one of the two models tested; on the other it only shrank;
- a result described as editing the text when the experiment left the text untouched and edited
  internal state, which inverted the point;
- tier colours (meaning "peer-reviewed") painted on preprint and preliminary results.

None of these were typos. Each was a compression that sounded better than the evidence.

## Subagent prompt (fill the brackets)

```
You are reviewing an X/Twitter thread before it is posted. Read everything first:
- post texts: [path to thread.md]
- images: [paths to post-1.png ... post-N.png]  (open each one and look at it)
- sources the author has: [paths: data files, papers, notes, transcripts]

Do two passes and write them up separately.

1. As a smart non-expert who follows tech Twitter but not this field. For each post + image:
   where did you get lost; which words you would have to look up; what felt like a stretch or
   hype; whether the image says anything in five seconds on a phone, before reading the text;
   the one line you would quote.

2. As a fact-checker with the sources open. Make a table for every factual claim in every
   post AND every number, quote, label, name, date and attribution in every image:
   claim | where it appears | source (file + line/page/cell) | verdict: faithful / stronger /
   weaker / not supported / wrong. Check especially:
   - quantifiers and absolutes (never, always, all, only, best, first, none);
   - "X is right / X shows" where the source says "can", "suggests", "in one case";
   - results that hold for some models/settings/subsets reported as general;
   - spatial words (top-left, row two, the dark cell) against the actual image;
   - whether the image and the post text describe the same thing the same way;
   - whether colours in an image imply an encoding (e.g. an evidence tier) the item does not have;
   - quotes: verbatim against the source, including hedges dropped from the quoted sentence;
   - claims of independence (separate groups, never cite each other) against author lists and
     reference sections.

3. What a hostile expert would screenshot: up to 10, each with the dunk they would write.

4. Verdict: "Wrong; fix before posting" (numbered, each with a concrete replacement wording),
   "Should fix", "Taste", and "What holds". Keep replacements as plain as the original.
```

## After the review

1. Fix every must-fix in the generator (post text and card), re-render, and re-run the clip
   checks. Look at the changed cards again.
2. For each "stronger than the source" finding, prefer the weaker true wording over cutting the
   post; the thread usually survives "can be", "on one of two models", "in one transcript".
3. Walk the user through the fixed thread (SKILL.md step 8). The review is not a substitute for
   the author being able to defend each line.
