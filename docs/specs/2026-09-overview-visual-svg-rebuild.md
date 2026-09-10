# Spec: rebuild the overview visual from deterministic source

9 September 2026 · Proposed · Not owner-accepted, not scheduled, not a release

## Why

`public/images/00-ai-security.png` is a raster export from an image-generation model. There is no
SVG, no HTML and no layout file: the pixels are the only artifact. Every change is therefore a
regeneration, and a regeneration is a gamble on the model preserving everything it was not asked to
touch.

Two changes are already needed. The image must carry the ownership distinction recorded as D-012 in
the parent estate — the business owns Secure business AI and security advises, while the CISO and
the security team own Defend against AI and Defend with AI — and the footer still reads
`Proposed · v0.1`, which travels into anything anyone reuses.

A targeted correction was attempted on 9 September 2026 using the same pattern that fixed the
governance connector. The three ownership lines landed with correct copy and everything else
survived, but card 03 grew taller than 01 and 02 and the card bottoms went ragged. That breaks the
one rule this diagram's own visual contract states explicitly: the three cards are peers. Trial
output was kept outside this repository and nothing canonical was modified.

The estate already runs a deterministic SVG pipeline for its private method visuals. This spec
applies that existing method to the one public image that most needs it.

## Scope

Rebuild `00-ai-security.png` only. Do not touch `01`, `02`, `03` or `04`. This is deliberately one
image: it is the simplest of the five, it is a card layout rather than a flow diagram so it has the
least to clash with, and it is the one that is reused most.

If the rebuilt image reads as inconsistent beside the other four, that is the signal to rebuild all
five — a separate decision, not a silent expansion of this one.

## Order of work

The visual contract is this package's source of truth for what the image says. It moves first.

1. **Update the visual contract** in `content/00-ai-security.md`, section "Visual contract and
   accessible description".
2. **Write the generator**, producing SVG.
3. **Render to PNG** and inspect against the contract element by element.
4. **Update the manifests and rebuild the site.**

## 1. Visual contract changes

In the element table:

- `O-01` exact visible copy gains a final line: `Business-owned · security advises`
- `O-02` exact visible copy gains a final line: `Security-owned`
- `O-03` exact visible copy gains a final line: `Security-owned`

In the prose beneath the table, the sentence "The three cards are peers" needs qualifying rather
than deleting. They remain peers as views; they differ in ownership. Proposed replacement, to be
confirmed by the owner: *The three cards are peers as views of one security program. They are not
peers in ownership: Secure business AI is owned by the business with security advising, while the
other two are owned by the CISO and the security team. Do not put flow arrows between adjacent
cards.*

`O-FOOT` currently reads `Overview · Proposed · v0.1 · 09 Sep 2026`. **This is an open owner
decision, not part of this spec.** The status language travels into every reuse of the image, and
the rebuild is the cheapest moment to change it, but what it should say is a call about the
package's review posture rather than a rendering question.

## 2. Generator

Follow the pattern already proven in this estate at `visuals/build/*.py`: Python emitting an SVG
string directly, content held separately from layout, no external diagramming dependency.

- Output SVG, then PNG at **1672 × 941**, matching the current export and the rest of the series.
- White background. Sampled from the current export: page white is effectively `#FFFFFF`, card fill
  is approximately `#DEEFFE`. **Sample the remaining colors from the current PNG rather than
  guessing** — navy framing text, teal shared-foundation band, grey structural rules.
- Include `<title>` and `<desc>` for accessibility, as the private visuals do.
- Keep the generator and the SVG in this repository beside the PNG so all three ship together.

## 3. Fidelity requirements

Check element by element against the contract, not by overall impression.

- Every element in the contract table present, with its exact visible copy.
- **The three cards are equal height, aligned top and bottom.** This is the failure that killed the
  raster correction and it is the check that matters most.
- The three ownership lines read as secondary annotation: smaller and lighter than the "Builds on"
  sentence above them, not competing with the card titles.
- No flow arrows between adjacent cards.
- Colors carry their assigned meaning: navy framing, blue peer views, teal shared concerns, grey
  structure. Color stays secondary to labels.
- Compare side by side against the current export at full size before replacing anything.

## 4. Downstream

Replacing the image is not a single file change.

- The PNG appears at `public/images/`, and is copied into `dist/images/` and `dist/downloads/` by
  the site build.
- `docs/release-manifest.json` records `public/images/00-ai-security.png`, and
  `dist/fidelity-manifest.json` records the content source. Both need regenerating via
  `scripts/release-manifest.py` and the site build.
- The image is also embedded in the PowerPoint download and in two artifacts in the parent estate:
  the AI Ignite deck at `channel/decks/` and the shared-language page at `channel/`. Both rebuild
  from their own generators; neither updates automatically.
- Run the existing link and site checks before publishing.

## What this does not do

It does not change the meaning of the three views, resolve the footer wording, rebuild the other
four images, or imply owner acceptance, review, or publication approval. It replaces one raster
with a source-backed equivalent carrying one addition already decided in the parent estate.
