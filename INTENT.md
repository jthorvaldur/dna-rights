# INTENT.md — dna-rights

## Prime Directive

Assert and document natural rights grounded in biological reality. The parent-offspring bond is a right that exists by nature, not by state grant. DNA establishes standing independent of any court order.

The word is "offspring," not "children." The language shift changes the jurisdiction.

## 1. Operating Rules

1. **Biology precedes law.** The parent-offspring bond is a biological fact. No court order creates it; no court order can destroy it.
2. **Language is jurisdictional.** The terms we accept define the court's authority over us. "Offspring" asserts biology. "Children" accepts legal framing. Every document in this repo uses biological language unless quoting statutory text.
3. **DNA is not evidence — it is the claim itself.** A DNA test does not prove parentage to a court. It reveals what already exists independent of any court.
4. **Natural rights > legal rights.** The hierarchy is: natural law > constitutional law > statutory law > court orders. A lower authority cannot override a higher one.
5. **No secrets in the repo.** All assertions are public. Natural rights do not require concealment.
6. **Every assertion cites its basis.** Natural law, constitutional text, international convention, or biological fact. No unsupported claims.

## 2. Decision Principles

- **Biological framing over legal framing.** When two ways to say something exist, choose the one grounded in biology.
- **Questions over statements.** The sovereign approach: ask the court to identify its authority rather than arguing within its assumed framework.
- **Explicit hierarchy.** Always state which level of authority supports the assertion (natural, constitutional, statutory, judicial).
- **Composable assertions.** Each document stands alone but combines with others to build a complete jurisdictional challenge.
- **Auditable reasoning.** Every claim traces back to a source: a biological fact, a legal text, a historical precedent, or a logical derivation.

## 3. Output Structure

```
docs/                  # Framework documents — the substantive arguments
src/dna_rights/        # CLI toolkit — generate assertions, compare terms, reframe language
.control/              # policy-orchestrator contract
```

## 4. Repo Boundaries

- **This repo contains:** Natural rights frameworks, biological parentage arguments, jurisdictional analysis, language comparison tools, assertion generators.
- **This repo does NOT contain:** Case-specific filings (that's div_legal), sovereign procedure templates (that's sovereign-legal), word etymology deep dives (that's words_quantum_legal), encrypted personal documents.
- **Cross-repo connections:**
  - `sovereign-legal` provides the jurisdictional questioning framework
  - `div_legal` applies these arguments to the active case
  - `words_quantum_legal` provides language analysis for term comparisons
  - `policy-orchestrator` manages this repo's compliance contract

## 5. Agent Protocol

Agents working in this repo must:

1. Read this INTENT.md before acting.
2. Use biological language: "offspring" not "children," "parent" not "custodian," "natural bond" not "custody."
3. Cite the authority level for every assertion (natural, constitutional, international, statutory).
4. Never weaken a natural rights claim to make it more "legally palatable." The point is to challenge the legal framework, not to conform to it.
5. Query vector DB collections (legal_docs_v2, case_docs) for supporting evidence before drafting assertions.
6. Flag uncertainty using:
   ```
   Uncertainty: [what is unknown]
   Assumption: [what is being assumed]
   Implication: [what breaks if the assumption is wrong]
   ```
