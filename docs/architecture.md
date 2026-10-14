# Architecture and reference limits

| Layer | Public implementation | Production work still required |
| --- | --- | --- |
| Input | Fixed shipment and source fixtures in JavaScript. | Authenticated adapters, timestamps, and conflict resolution. |
| Review | Facts, missing information, and preset recommendations. | Grounded output, citations, and independent evaluation. |
| Role policy | Browser action checks with five selectable roles. | Server-enforced identity, tenant, and field scopes. |
| Tasks | In-memory transitions from pending to closed. | Durable transactions, dependencies, and evidence checks. |
| Audit | Synthetic entries displayed in the page. | Durable, access-controlled append-only records. |
| Customer view | Rendered external status fields. | Server-side filtering with no internal records sent to customers. |

The shared policy module checks role capabilities, data freshness, confidence, and allowed task states. It is deliberately small so browser behavior and Node boundary tests use the same logic.

This static workbench is suitable for interaction and product-architecture review. It is not an authentication system or a secure logistics backend.
