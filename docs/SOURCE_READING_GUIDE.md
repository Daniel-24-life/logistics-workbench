# Source reading guide

This independent repository was prepared solely from already published public material. Start with the runnable implementation:

1. `dist/index.html` defines the static shell, navigation, role picker, detail sheet, and modal.
2. `dist/app.js` holds fixed synthetic fixtures and renders the exception, task, customer, integration, and system views.
3. `dist/policy.js` contains the shared approval and task-transition checks.
4. `tests/policy.test.cjs` exercises those policy boundaries in Node.
5. `docs/reference-guide.md` and `docs/architecture.md` explain the operational flow and its public limits.

For provenance, see [MIGRATION.md](../MIGRATION.md). The repository intentionally contains no private source material, credentials, real logistics records, or unpublished deployment configuration.
