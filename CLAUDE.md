# dna-rights

> Read `INTENT.md` first. It is the root authority for all work in this repo.

## What This Repo Does

Natural rights assertion toolkit grounded in biological reality. The thesis: the parent-offspring bond is a natural right that precedes and supersedes legal constructs. DNA establishes standing independent of any court order.

Core concepts:
- **Offspring, not children** — "children" is a legal term that accepts court jurisdiction; "offspring" is a biological term that asserts a fact the court cannot adjudicate
- **DNA as the claim** — DNA does not prove parentage to a court; it reveals what already exists
- **Force performance** — demanding the court identify its authority to sever a biological bond
- **Land connection** — "of your flesh" parallels "of your land"; biological claim has the same structure as property claim at common law

## Cross-Repo Connections

| Repo | Relationship |
|------|-------------|
| `sovereign-legal` | Jurisdictional questioning framework — the procedural tools for asserting natural rights in court |
| `div_legal` | Active case application — where these arguments are applied to specific filings |
| `words_quantum_legal` | Language analysis — etymology and jurisdictional weight of specific terms |
| `policy-orchestrator` | Governance hub — manages this repo's compliance contract |

## CLI Commands

```bash
rights assert --relationship parent-offspring --evidence dna    # Generate formal natural rights assertion
rights claim --type offspring --context court                    # Draft DNA-based standing claim
rights compare children offspring                                # Side-by-side term analysis
rights reframe "custody of the minor children"                   # Rewrite in natural rights terms
```

All commands support `--format text` (default, rich terminal output) and `--format json`.

## Vector DB Access

Query these collections for supporting evidence before drafting assertions:

### Port 6333 (main Qdrant)
| Collection | Use |
|-----------|-----|
| `legal_docs_v2` (244K pts) | Emails, PDFs, filings, financial statements from the active case |
| `fact_registry` (167 pts) | Classified facts with confidence levels |

### Port 7333 (caseledger Qdrant)
| Collection | Use |
|-----------|-----|
| `case_docs` (1.7M pts) | Full legal document corpus with hybrid search |

```bash
# Search from policy-orchestrator
cd ~/GitHub/policy-orchestrator && uv run devctl search "parental rights DNA" --limit 5

# Direct Qdrant query
curl -s -X POST http://localhost:6333/collections/legal_docs_v2/points/scroll \
  -H 'Content-Type: application/json' \
  -d '{"limit": 5, "with_payload": true, "with_vector": false}' | python3 -m json.tool
```

## Rules for Agents

1. Read `INTENT.md` before acting.
2. Use biological language: "offspring" not "children," "parent" not "custodian," "natural bond" not "custody."
3. Cite the authority level for every assertion: natural > constitutional > international > statutory > judicial.
4. Never weaken a natural rights claim to conform to legal convention. The point is to challenge the framework.
5. Query vector DB for evidence before drafting assertions.
6. Flag uncertainty:
   ```
   Uncertainty: [what is unknown]
   Assumption: [what is being assumed]
   Implication: [what breaks if the assumption is wrong]
   ```
