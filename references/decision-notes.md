# Decision notes

## Evidence and scope

Use the weakest wording that accurately matches the design, not the weakest wording available.

| Evidence | Safe writing | Do not infer |
| --- | --- | --- |
| Cross-sectional or observational study | “X was associated with Y in the study sample.” | Temporal order or causal influence. |
| Randomized or otherwise identified causal design | State the supported causal effect and its population. | Effects outside the design or sampled population. |
| Non-significant estimate | Report estimate, interval, and uncertainty. | Proof that no effect exists. |
| Systematic review without meta-analysis | Describe the review process and pattern of evidence. | A pooled effect. |
| In-domain ML evaluation | Report held-out in-domain performance. | External validity or deployment safety. |

## Positive scope

Replace a negation only when the positive statement is actually supported.

- Weak: “We do not claim that the findings apply to all university students.”
- Supported scope: “The findings characterize students at the four participating universities.”

Do not invent a benefit such as “the sample captures all key differences” unless evidence establishes it.

## Paragraph reconstruction

Give each paragraph one job: claim, evidence, implication, or limitation. Lead with that job. If a limitation interrupts an introduction, contribution, or result paragraph, move it only when readers can still interpret the adjacent claim accurately.

## Candidate signals

Treat these as prompts for judgment, not prohibited words: repeated non-claims, stacked modality, apology-like framing, defensive method justifications, repetitive scope statements, and formulaic contrasts. Retain a signal when it performs a real logical or evidentiary function.

## Provenance

This skill independently adapts the high-level “claim-forward, evidence-preserving” approach from Kiterlin’s MIT-licensed `anti-defensive-writing` skill. It uses original organization and wording, adds submission-stage academic safeguards, and does not reproduce the source text wholesale.
