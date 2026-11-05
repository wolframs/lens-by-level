# Image patterns: objects that work, and the slide anatomy that doesn't

Read this when choosing what each card shows (step 2 of SKILL.md) or when a card feels like a slide.

## The test for every card

Cover the post text. Does the image still show *a thing* (a conversation, a chart, a diff, a
number) that a reader could screenshot and argue about? If it only shows a heading and some
words about the thing, it is a slide. Rebuild it around the thing.

## Slide anatomy to avoid

The rejected first draft had, on every card: eyebrow label ("FINDING 3"), title, subtitle,
a figure squeezed in the middle, and a footer with handle + "3/6". On a phone in a feed:

- the eyebrow, subtitle and footer are unreadable at thumbnail size and push the figure down to
  half the frame, so the one part that carries evidence is the smallest;
- every card looks the same, so scrolling past them feels like a deck, not a thread;
- the title repeats the post text, so the reader reads the same claim twice and the evidence never.

A plain title is fine when it is the chart's own label ("Average wait, six buses an hour"). It is
not fine when it is a slogan restating the post.

## Patterns (one per card)

| Object | Use it for | Make it concrete by | Component in build_cards.py |
|---|---|---|---|
| **Mock chat** | a question people actually ask; a model's real answer; a prompt that produced a result | real wording (quote the prompt verbatim; if it is invented, it must read as an illustration, never as a log), big bubbles (≥34px), a plot or attachment *inside* the reply when the answer is a measurement | `chat()` |
| **The actual chart, annotated on the data** | a comparison, a distribution, counts per category | values printed on the marks, labels at the marks (no legend hunt), one or two accent arrows/callouts placed next to the data they explain, a reference line where a reader's intuition sits | `hbars()` |
| **Diff of the actual text** | a correction, a revised claim, a reworded rule, before/after a review | the real old and new wording, a header saying what file/claim and why it changed, the source quote or arithmetic that forced the change underneath | `diff()` + `.work` |
| **The real numbers as bars** | 2–5 numbers a reader should compare | bars with the number on each; no axis if every bar is labelled | `hbars()` |
| **Timeline / strip** | something that happens over time; sampling; who arrives when | one row per thing being compared, the same time axis, the counts written out ("57 of 60") | `timeline()` (example) |
| **Code or schema becoming a diagram** | a mechanism | the actual code or config on the left, boxes/arrows built from its names on the right | write a new helper |
| **Readout panels (2–3 side by side)** | several results that share a shape | each panel is the measurement itself (a probe value, a quoted output), with a one-line source under it in `.meta` | write a new helper |
| **Highlighted screenshot of a real page** | a board, a table, a paper figure the thread is about | crop to the part that matters, dim the rest, put accent outlines and 1–2 labels on the cells being discussed; embed with `<img data-shot=...>` so it re-themes | `data-shot` in shoot.js |

## Card 1

Card 1 is the thumbnail for the whole thread and the only image many people see. Give it the
most arresting object you have: usually the concrete situation (the chat with the familiar
question, the surprising chart, the two quotes that disagree), not a framing diagram. If two
cards compete, the one a stranger understands in five seconds without the text wins.

## Layout rules that keep the frame full

- Card: 1600×900, padding ~60px/72px, flex column, content vertically centred. If `render.py`
  warns that content spans <75% of the height, scale the object up (bigger type, taller bars,
  more rows of real data) rather than adding chrome.
- Sizes at 1600 wide: titles 34–44px, body and labels ≥19px (≥24px is better), bubbles and diff
  lines 34–46px. Source/citation lines may use `.meta` at 16–18px; nothing else goes that small.
- SVG text: the checker scales SVG font sizes by the rendered width ÷ viewBox width, so a
  `font-size="22"` in a 1700-wide viewBox drawn 1450px wide is really ~19px. Keep viewBox widths
  close to the drawn width.
- Long labels: put callouts in a reserved right-hand column (hbars reserves 400 units) and keep
  them to two short lines; the most common clip is a callout that runs off the right edge.
- Draw reference lines before the bars so they never cross a value label.

## Colour roles in practice

- `t1 t2 t3` are the ordinal ramp: use them only for the ordered thing a legend or the post
  explains (evidence tier, how uneven, how strong). A result box, chat bubble or highlight in a
  tier colour will be read as that tier: a review caught "peer-reviewed" navy painted on three
  preprint results. Use `surface`, `asst`, `user` or `acc` for things that are not tiers.
- `acc` means "look here": arrows, the one highlighted cell, the riders who land in the long gap.
  One accent per card, used once or twice. Text in the accent colour uses `accInk` (on yellow or
  pale accents, `accInk` is dark).
- Add a new role instead of reusing one whose value happens to match: if text on a tier and text
  on the accent share a literal, a theme that needs them different cannot separate them.
