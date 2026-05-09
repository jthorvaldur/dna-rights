# dna-rights

Natural rights assertion toolkit -- assert biological parentage as a jurisdictional fact independent of any court.

## What it does

Documents and generates natural rights claims grounded in biological reality. The parent-offspring bond is not a legal relationship to be granted or revoked -- it is a biological fact that the law must acknowledge. DNA establishes standing independent of any court order.

## Installation

```bash
uv pip install -e .
```

## CLI usage

```bash
rights assert "parental bond"         # Generate formal assertion of natural rights
rights claim --basis dna              # Draft DNA-based standing claim for court
rights compare "custody" "offspring"  # Side-by-side jurisdictional term analysis
rights reframe "custody agreement"    # Rewrite statutory language in natural rights terms
```

## Architecture

Part of the sovereign architecture triad:

```
sovereign-legal (jurisdictional strategy)
    |
    +-- dna-rights (natural rights assertions, biological standing)  <-- this repo
    |
    +-- embedded-commands (communication analysis, influence engineering)
```

- **sovereign-legal** provides the jurisdictional framework (4-layer model) that grounds these assertions
- **dna-rights** asserts biological parentage as natural law, above statutory authority
- **embedded-commands** helps craft communications that carry these arguments effectively
- **div_legal / caseledger** apply these assertions to active case filings

## Structure

```
dna-rights/
├── INTENT.md            # Governing document
├── pyproject.toml
├── data/terms.yaml      # Biological vs. legal term mappings
├── docs/                # Framework documentation
├── html/                # Self-contained HTML presentations
└── src/dna_rights/      # CLI toolkit
```

---

Managed by [policy-orchestrator](https://github.com/jthorvaldur/policy-orchestrator). Category: legal.

<!-- AUTO:footer -->
Managed by [policy-orchestrator](https://github.com/jthorvaldur/policy-orchestrator). Category: legal. 5 commits, last updated 40 minutes ago.
<!-- /AUTO:footer -->
