# Project lessons

## Source fidelity and browser validation

A page loading successfully, a matching heading and a working download are distinct from complete canonical-body fidelity and architectural correctness. Test each explicitly. Build summaries from complete sentences; arbitrary character truncation can leave visible fragments. Keep one visible main heading while preserving source fragment targets.

Markdown images can render inside paragraphs. A direct-child CSS rule such as `.prose > img` will miss them; constrain nested images too. Check full-document width on every route at desktop and mobile sizes, not only text clipping or the visible fold. Inspect the actual full-page screenshots before calling browser QA passed.

## Diagram and document review

Inspect actual images and every changed rendered page or slide. PDF text extraction can miss image-only content. Verify feedback arrows and action authority separately from label spelling. Freeze and hash the exact reviewed output, and retain substantive findings independently of formatting fixes.

## One maintained source

Project scaffolding works only when its records connect. Intent owns direction, roadmap owns development areas, backlog owns work/evidence, decisions own accepted changes, and status summarizes current state. Trace items between those records and keep intended downstream uses distinct from actual adopted artifacts.

Adding a companion document does not automatically update a reader's mental model. When the scope grows, revisit the first paragraph, central teaching sentence, worked example and closing discussion together. Keep website hero copy derived from that source so the first screen carries the same story as the detailed text.

The public edition has one editable canonical source tree. Preserve historical inputs and critiques as evidence without maintaining a competing canon. Treat prior work as an input only when the owner has authorized its use; a familiar filename or directory is insufficient.

## Public packaging

Audit both Git inputs and generated ZIP members. ZIP hashes may vary between builds because of timestamps; compare the member manifest and uncompressed bytes. Do not include operational credentials, raw runtime receipts or unrelated workspace content.

## Repository relocation

A nested directory is not automatically the intended Git root. Preserve independent history, locally exclude the workspace from a surrounding repository, and verify the Git top level before staging. Hash the full tree before and immediately after a move, then distinguish preservation from subsequent documented edits and rebuilds. Keep historical receipts unchanged; a temporary compatibility symlink can support existing local consumers while physical data has moved.
