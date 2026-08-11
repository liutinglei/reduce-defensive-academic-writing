# Reduce Defensive Academic Writing

An evidence-calibrated Agent Skill for improving submission-ready academic prose without making claims stronger than the evidence permits.

中文：面向投稿前论文的“去过度防御”写作 Skill。它删除无效免责声明、过度预防性解释和 AI 式套话，同时保留研究范围、方法局限、统计不确定性与引文边界。

## What it does

- Rebuilds contribution paragraphs around the claim instead of what the paper does not claim.
- Distinguishes removable defensive framing from necessary scope conditions and real limitations.
- Preserves causal, generalization, systematic-review, machine-learning, and statistical boundaries.
- Supports audit, targeted-revision, and full-manuscript workflows in English and Chinese.

## Use

In a compatible agent, invoke:

```text
$reduce-defensive-academic-writing Perform a submission-ready final pass on this manuscript. Remove unnecessary defensive prose while preserving every evidence boundary.
```

For long text, the included candidate scanner supports `.txt`, `.md`, `.tex`, and `.docx` inputs. It only identifies candidates; it never edits the source document.

```powershell
py scripts/scan_candidates.py manuscript.docx
```

## Evidence boundary

The Skill never changes numerical results, statistical significance, sample sizes, citations, variable meanings, tables, figures, or cross-references. It does not turn associations into causal effects, in-domain model performance into external validity, or a review without meta-analysis into a pooled-effect claim.

## Install

Clone this repository, then copy the repository folder into your compatible agent's personal Skills directory. For Codex, the destination is normally `~/.codex/skills/reduce-defensive-academic-writing`.

## License

MIT. See [LICENSE](LICENSE).
