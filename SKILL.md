---
name: reduce-defensive-academic-writing
description: Strengthen submission-ready academic prose by removing unnecessary defensive framing while preserving the exact evidentiary strength, scope, statistics, citations, and methodological limits. Use for English-first or Chinese academic-paper polishing, final manuscript checks, titles, abstracts, introductions, literature reviews, theoretical frameworks, methods, results, discussions, limitations, conclusions, and requests to remove AI-like stock phrasing, excessive hedging, self-undermining caveats, reviewer-anticipating prose, or to strengthen an argument without overstating it. Do not use for rebuttals, cover letters, appeals, or editor emails unless the user explicitly asks.
---

# Reduce Defensive Academic Writing

## Aim

Advance each claim directly while preserving its exact strength and evidence boundary. Write as a composed scholar explaining a study, not as an author pre-emptively negotiating with an imagined reviewer.

## Classify Before Revising

Classify each candidate sentence or clause before changing it.

| Class | Action |
| --- | --- |
| Unnecessary disclaimer | Delete when it adds no evidence, scope, logic, or reader guidance. |
| Scope condition | State the supported population, period, setting, or task positively. |
| Methodological limitation | Keep it accurate; place it in `Limitations` unless its location is essential to interpretation. |
| Conceptual contrast | Retain only when the contrast carries the argument. Make it short and direct. |
| Evidence-based qualification | Retain and name the source of uncertainty or design constraint. |
| Redundant clarification | Delete or merge when it merely blocks a hypothetical misunderstanding. |

Never use a word list as an automatic deletion rule. `may`, `however`, `although`, `rather than`, and `not X but Y` can be necessary when they express evidence, logic, or a real conceptual distinction.

## Non-Negotiable Accuracy Checks

- Do not change numerical values, significance, effect direction, confidence intervals, sample sizes, citations, variable meanings, tables, figures, or cross-references.
- Do not turn association into causation, exploratory analysis into confirmation, in-sample performance into external generalization, or a non-significant result into evidence of no effect.
- Do not replace a genuine limitation with an unverified advantage. If a claim lacks support, mark it `author verification needed` rather than softening it vaguely or strengthening it rhetorically.
- Do not repeat the same boundary in the abstract, introduction, discussion, and conclusion. Retain it once where readers need it.

## Section Placement

- **Abstract:** report question, design, findings, and contribution directly; retain only qualifications needed to state evidence correctly.
- **Introduction and contribution paragraphs:** lead with the problem, gap, and contribution; avoid defining the paper by what it does not do.
- **Methods:** describe design, sampling, measures, and analysis as facts. Do not turn methods into a rebuttal to anticipated criticism.
- **Results:** report estimates and uncertainty faithfully; do not apologize for non-significant results.
- **Discussion:** explain the main finding before weighing supported alternatives.
- **Limitations:** consolidate real limitations. State the constraint, its consequence for interpretation, and a proportionate next test if useful.
- **Conclusion:** restate the supported contribution. Use at most one concise scope statement when needed.

## Workflow

1. Read the relevant section or the whole manuscript before editing. Identify claim type, evidence type, and section function.
2. Run `scripts/scan_candidates.py` for long `.txt`, `.md`, `.tex`, or `.docx` drafts when useful. Treat its output as leads, not verdicts.
3. Apply the six-class decision. Delete, recast as positive scope, move to `Limitations`, retain precisely, or rebuild the paragraph around its claim.
4. Re-read every edited paragraph for referents, transitions, paragraph purpose, and evidence strength.
5. Run a final boundary check. List only the necessary limitations retained and any claims needing author verification.

Read `references/decision-notes.md` when a sentence sits near a causal, generalization, systematic-review, or machine-learning boundary.

## Output Modes

- **Audit mode:** provide a compact table with location, candidate, class, action, and proposed revision.
- **Revision mode:** deliver the clean revision, a short structural summary, necessary boundaries retained, and author-verification flags.
- **Full-manuscript mode:** audit internally, then revise directly unless the user requests a sentence-by-sentence report.

For existing Word documents, preserve the template and styles. Use a copy or tracked changes when requested; do not rebuild a formatted manuscript as plain text.
