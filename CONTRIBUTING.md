# Contributing to FINOSCOPE

## Team principles
- Keep changes focused, attributable and explainable.
- Use descriptive commits and request peer review for shared integration.
- Run relevant tests before requesting a merge.
- Record material decisions in docs/decisions/.
- Never commit secrets, personal data, restricted datasets or large generated artefacts.

## CCS4340 individual contribution
Each of the three students owns a different model family. Every student independently implements and explains their pipeline choices, model training, validation and experiments. Shared utilities are permitted, but individual work must remain visible in individual branches and commits.

After confirming student IDs, use:
- feature/<member1ID>-model
- feature/<member2ID>-model
- feature/<member3ID>-model
- feature/shared-pipeline

Do not invent or backdate commits or commit another member's work under your identity.

## Commit messages
Examples:
- data: add source metadata and licence review
- feat(macroguard): add chronological split utility
- test(api): cover health endpoint
- docs: record target-label definition decision

Avoid vague messages such as update, work, final or done.

## Pull request checklist
- [ ] Scope and motivation are clear.
- [ ] Tests or validation steps are documented.
- [ ] No secrets or restricted data are included.
- [ ] Individual academic contribution remains identifiable.
- [ ] Documentation is updated.
- [ ] Author can explain the implementation.

## Local setup
See README.md and application-specific READMEs. Copy .env.example to .env locally.
