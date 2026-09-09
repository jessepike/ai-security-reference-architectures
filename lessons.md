# Project lessons

## Source fidelity and browser validation

A page loading successfully, a matching heading and a working download are distinct from complete canonical-body fidelity and architectural correctness. Test each explicitly. Build summaries from complete sentences; arbitrary character truncation can leave visible fragments. Keep one visible main heading while preserving source fragment targets.

## Diagram and document review

Inspect actual images and every changed rendered page or slide. PDF text extraction can miss image-only content. Verify feedback arrows and action authority separately from label spelling. Freeze and hash the exact reviewed output, and retain substantive findings independently of formatting fixes.

## One maintained source

The public edition has one editable canonical source tree. Preserve historical inputs and critiques as evidence without maintaining a competing canon. Treat prior work as an input only when the owner has authorized its use; a familiar filename or directory is insufficient.

## Public packaging

Audit both Git inputs and generated ZIP members. ZIP hashes may vary between builds because of timestamps; compare the member manifest and uncompressed bytes. Do not include operational credentials, raw runtime receipts or unrelated workspace content.
