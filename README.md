# Hangxu Logistics Workbench

An offline browser workbench for reviewing synthetic logistics exceptions and following a dispatch task through closure.

[中文说明](README.zh.md) · [Portfolio](https://github.com/Daniel-24-life/AIfile)

![Logistics workbench exception queue and task details](docs/assets/workbench-desktop.png)

## What it demonstrates

- Separate the available facts, evidence gaps, and proposed action for an exception.
- Switch demo roles to review a suggestion, advance a dispatch task, and view customer status.
- Review the effect of policy checks on stale exceptions and task transitions.

**Stack** · HTML, CSS, JavaScript. Python serves the static files and Node.js runs the policy tests.

## Repository layout

| Path | Contents |
| --- | --- |
| [`dist/index.html`](dist/index.html) | Static application entry point |
| [`dist/app.js`](dist/app.js) | Queue, task state and customer view |
| [`dist/policy.js`](dist/policy.js) | Shared policy checks |
| [`tests/`](tests/) | Policy tests |
| [`docs/`](docs/) | Architecture and UI evidence |

## Run locally

```sh
python -m http.server 4181 --bind 127.0.0.1 --directory dist
node --test tests/policy.test.cjs
```

Open `http://127.0.0.1:4181`. Run the test command in a separate terminal.

## Scope and limits

The workbench uses fixed synthetic shipments, identities, and suggestions. Role switching is a demo control. State lives in memory and resets on reload. Network integrations, production authorization, and durable audit records are outside the demo.

[Architecture](docs/architecture.md) · [Verification](docs/VERIFICATION.md)
