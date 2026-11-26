# demo-gate

A small demo repository for the [Opencomplai GitHub Action](https://github.com/Opencomplai/opencomplai-action).

Every push and pull request runs `opencomplai check` against `system-manifest.json`.
A failing control fails the check, like a failing test, and the result is posted as one pull request comment.

- `main` declares a customer support chatbot. The check passes.
- Open pull requests show what happens when a change adds a high-risk AI system.

Demo content only: there is no real product here.

Docs: https://docs.opencomplai.com
