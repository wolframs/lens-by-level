---
name: twitter-thread-images
description: Turn a body of evidence, a finding or an argument into a 4–8 post X/Twitter thread where every post carries one 1600×900 image that is a concrete object (a mock chat with real wording, the actual chart annotated on the data, a diff of the actual text, the real numbers as bars), rendered from one HTML generator with Playwright, offered in five validated colour styles on a contact sheet, clip-checked, and fact-checked before posting. Use this whenever the user wants to share research, an analysis, a project or a correction on X/Twitter, Bluesky, Threads or LinkedIn as a thread or as a set of post images, asks for "thread images", "cards for a thread", "images for my tweets", "a visual thread", or wants to explain their work to a general audience in posts, even if they don't say "thread" or "images".
---

# Twitter thread images

Build a thread of 4–8 posts, one image each, where the post text carries the claim and the image
carries the evidence or the thing itself. The workflow below is the one that survived a user who
rejected the first version as "a slideshow", three rounds of clipped labels, and a pre-posting
review that found 12 factual errors. The reasons are inline so you can apply them to cases this
file doesn't cover.

Scripts live in `scripts/` next to this file. Copy them into the user's repo (e.g. `share/`)
rather than running them from the skill folder: the generator *is* the thread, and keeping
generator + renderer + themes in the repo means a wording change later is one edit and a re-render.

| Script | Does |
|---|---|
| `build_cards.py` | template generator: DATA, POSTS, CARDS → `thread.html` (one `<section id="cN">` per card) + `thread.md` |
| `themes.py` | five styles as CSS-variable roles; `python themes.py` lists them |
| `check_themes.py` | validates every theme's ramp and text contrast (uses the bundled `validate_palette.py`) |
| `render.py` | `thread.html --theme KEY\|all --out DIR [--cards 1,2]` → `post-N.png` + clip/legibility report |
| `shoot.js` | the Playwright renderer `render.py` calls; also embeds themed screenshots of other pages |
| `contact_sheet.py` | PIL: one image comparing all styles on the same three cards |
| `validate_palette.{js,py}` | bundled dataviz palette validator (`--ordinal`, `--mode`, `--surface`; `contrast()`) |

Requirements: Python 3 with Pillow, Node with `playwright` resolvable (Chromium already installed;
don't run `playwright install` unless the user asks). Google Fonts need network; if they don't
load, `render.py` says so and the cards fall back to system fonts.

## Procedure

### 1. Collect the evidence and the author's position

Read the sources the thread rests on (data files, papers, notes, review files) before drafting.
Ask the user, if it isn't clear: who the audience is, what they want a reader to come away with,
and which claims they would personally defend. The user's rule for their own posts: only post
what they understand and can defend without the model. A compressed punchline they couldn't
reconstruct in a reply is a liability, however good it sounds, so prefer the plain sentence.

### 2. Plan posts and objects together

Write a table: post number, the one claim, the object that shows it, and the source for every
number/quote/name the image will contain. Rules:

- **One concrete object per image, not a slide.** The rejected first draft had eyebrow + title +
  subtitle + figure + footer on every card; on a phone that shrinks the evidence to half the frame
  and repeats the post text. The examples the user held up were a chat showing the actual prompt
  with a probe-readout plot, a scatter with arrows and labels drawn on the data, and a code snippet
  becoming a diagram. See `references/image-patterns.md` for the catalogue and the slide test.
- **Post 1 gets the most arresting image**, because it is the thumbnail for the whole thread and
  often the only image people see. Usually the concrete situation (the familiar question in a chat,
  the surprising chart), not a framing diagram.
- **Every post has an image.** A text-only post in an image thread reads as an afterthought.
- **No footer, handle, page counter or "reply 1/2" labels** on the images. The user had them
  removed: X already shows the author and order, and the chrome costs legibility.
- 4–8 posts. Note post length; over 280 characters needs X Premium, so flag it rather than
  assume.

### 3. Write the generator

Copy `scripts/*` into the repo, then edit the copy of `build_cards.py`:

- Replace `DATA` with the real numbers, each with a `# SOURCE:` comment (file, page, cell, line).
  Compute derived numbers in code from the sourced ones so they cannot drift from each other;
  `assert` the ones the text quotes.
- Replace `POSTS` (one per card, same order) and `CARDS`. Reuse the components (`chat`, `hbars`,
  `diff`, `timeline`) or add new ones in the same style.
- Use colour only through `var(--role)` (`F('t2')`, `S('rule')` in SVG). Every role is its own
  variable so a theme can move text-on-tier, card surface and text-on-accent independently; the
  original project used shared hex literals and had to untangle them per theme. If you need a new
  meaning, add a role to `themes.py` (all five themes) rather than borrowing one with the right value.
- Use the ramp `t1..t3` only for an ordered thing the reader is told about. A review caught the
  "peer-reviewed" colour painted on preprint results: tier colours on anything else get read as
  evidence. Non-tier fills use `surface`, `asst`, `user`, `tag*`, `acc`.
- To show another page (a board, a dashboard), add `<img data-shot="page.html" data-selector=".x"
  data-css="nav{display:none}">`; `shoot.js` screenshots it with the theme applied.

Run `python build_cards.py --out share/` and open nothing yet.

### 4. Offer five styles on one contact sheet

```
python check_themes.py                                   # all five must PASS
python render.py share/thread.html --theme all --cards 1,2,3 --out share/themes
python contact_sheet.py share/themes --cards 1,2,3 --out share/style-options.png
```

Pick the three cards that test a style hardest: the hero, the one using the ramp, the densest
text. Show the sheet (Read it, then tell the user its path) and let the user pick; don't commit to
a palette yourself, because colour is the first thing the user reacts to and changing it after
twelve renders wastes their review time. Same layouts across styles so only colour and type vary.

If the user wants a new style: one-hue ordinal ramp + one accent + neutrals, then run
`check_themes.py`. It enforces: ramp faint end ≥2:1 vs bg and surface, monotone with visible steps,
one hue; every text pair ≥4.5:1; meta text (`ink3`) ≥3:1; accent far from every tier; chat bubbles,
tags and diff rows not mistakable for a tier. Avoid the generic AI looks (cream + terracotta,
near-black + acid green, purple-to-blue gradients): they signal "generated" before anyone reads.

### 5. Render the chosen style and check every card

```
python render.py share/thread.html --theme <key> --out share
```

The report fails on text outside the card, text cut by an overflow box or its SVG, and overlapping
labels; it warns on text under 19px (16px for `.meta`), on content spanning <75% of the height or
leaving an empty band >22%, and on fonts that didn't load. Then **open every PNG with Read and look
at it**: the checks see geometry, not meaning, and the original thread hit clipped labels three
times. Targets at 1600 wide: titles ≥34px, body ≥19px, content filling the frame (the first
attempt left the lower half of most cards empty). Fix in the generator, re-render, re-look.

### 6. Trace every number, quote and attribution

Before review, go through each image and post and point at the source for every number, quote,
name, date and attribution. If you can't, cut it or ask the user. Quotes are verbatim, hedges
included. Words like "never", "all", "only", "best", "both are right" need the source to say
exactly that. Spatial words ("bottom-right", "the dark row") must match the image as rendered.

### 7. Run the combined review

Spawn one subagent briefed as both a smart non-expert and a fact-checker with the sources open,
on post texts and images together. Use the prompt in `references/review-brief.md`. In the original
run this found 12 must-fix errors after several earlier reviews, e.g. "three papers never cite
each other" when two shared authors, a "bottom-right" cell that was in row two, and "both are
right" where the evidence supported only "both can be right". Fix every must-fix in the generator,
re-render (step 5), and look at the changed cards.

### 8. Walk the user through it

Present the final thread as post text + image path, post by post, and point out any line whose
wording came from you rather than from them, any claim that rests on one study or one model, and
anything the review softened. Ask them to say each claim back in their own words; anything they
can't defend without you gets plainer or goes. Don't post on their behalf.

### 9. Deliver

Leave in the repo: `build_cards.py` (with DATA, POSTS, CARDS), `themes.py`, `render.py`,
`shoot.js`, `check_themes.py`, `contact_sheet.py`, `validate_palette.*`, `thread.md`,
`post-1.png … post-N.png`, `style-options.png`. Add rendered theme folders to `.gitignore` if
they're bulky. Tell the user the re-render command for their chosen theme.

## Quick reference: what went wrong before, and the rule it produced

| What happened | Rule |
|---|---|
| Every card had eyebrow/title/subtitle/figure/footer; "you built a slideshow" | one concrete object per image; the post carries the claim |
| Handle, "3/6" and "reply 1" on every image; user asked to remove them | no image chrome unless asked |
| Large empty lower halves | fill the frame; act on the fill warning |
| Labels clipped in three separate rounds | read every render, not just the report |
| Palette chosen before the user saw options | contact sheet of five validated styles first |
| Tier navy painted on preprint results | ramp colours only for the encoding they carry |
| Shared hex literals made themes bleed into each other | one CSS variable per role |
| 12 factual errors survived to the pre-posting review | trace every number; run the combined review; plain wording the user can defend |
