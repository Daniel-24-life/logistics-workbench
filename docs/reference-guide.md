# Workflow and permission reference

## Role actions in the public demo

| Role | Review fixed suggestions | Advance tasks | View |
| --- | --- | --- | --- |
| Operations | Yes, only with fresh fixture data and confidence ≥ 60. | No. | Internal demo pages. |
| Dispatcher | No. | Yes. | Internal demo pages. |
| Customer service | No. | No. | Internal demo pages. |
| Manager | Yes, under the same fixture checks. | Yes. | Internal demo pages. |
| Customer | No. | No. | Filtered shipment status. |

These checks run in browser JavaScript. They do not establish a server identity, customer isolation, independently owned approval, or secure access control.

## Task lifecycle

```text
reviewed suggestion -> todo -> doing -> verifying -> done
                         blocked -> doing
```

Approval requires an approving role, non-stale fixture data, and preset confidence of at least 60. The demo refuses a duplicate task for an exception that already has a task or is closed. Task advancement rechecks execution authority; completed and unknown states cannot advance. Switching roles closes prior detail panels.

“Submit completion evidence” and “verify and write back” are labels for a real-world process. In this repository, they are UI state transitions only. They neither upload a document nor perform an independent evidence check.

## Production adaptation

Enforce every action on the server, scope every response by organization and customer, remove internal data before customer delivery, and store versioned events plus evidence references. Attach verified reviewer identity before closure and measure recommendations against grounded cases rather than fixture confidence.
