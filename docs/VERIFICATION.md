# Verification

## Required local checks

From the repository root with Node.js 22+:

```powershell
node --test tests/policy.test.cjs
node --check dist/app.js
node --check dist/policy.js
```

Serve the static output with Python 3.11+:

```powershell
python -m http.server 4181 --bind 127.0.0.1 --directory dist
```

Open <http://127.0.0.1:4181> and follow the walkthrough in the Chinese README. The static server is local only; it does not contact external services.

## CI

GitHub Actions runs the same Node 22 test command and syntax checks on pushes and pull requests. The workflow is defined in `.github/workflows/verify.yml`.

## Scope checks

The repository documents fixed synthetic data, a non-authentication role picker, and simulated—not independently validated—evidence actions. No claim of real integrations, uploads, model inference, durable state, or secure tenant isolation is made.
