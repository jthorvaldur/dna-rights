"""dna-rights CLI — Natural rights assertion toolkit."""

import json
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

# --- Term mappings ---

TERM_MAP = {
    "children": {
        "biological": "offspring",
        "framework": "legal",
        "jurisdiction": "State family court — treats the relationship as a legal construct subject to judicial modification.",
        "implication": "Accepting 'children' accepts the court's jurisdiction over the relationship.",
    },
    "offspring": {
        "biological": "offspring",
        "framework": "natural",
        "jurisdiction": "Natural law — the relationship is a biological fact not subject to court adjudication.",
        "implication": "Asserting 'offspring' asserts a biological fact the court did not create and cannot destroy.",
    },
    "custody": {
        "biological": "natural bond",
        "framework": "legal",
        "jurisdiction": "Statutory — 750 ILCS 5/602.5 allocates 'parenting time' as a divisible commodity.",
        "implication": "Accepting 'custody' treats the parent-offspring bond as property to be allocated by a judge.",
    },
    "natural bond": {
        "biological": "natural bond",
        "framework": "natural",
        "jurisdiction": "Natural law — the bond exists by biology and is not subject to allocation.",
        "implication": "The bond is not divisible. It exists in full for both biological parents.",
    },
    "visitation": {
        "biological": "access to offspring",
        "framework": "legal",
        "jurisdiction": "Statutory — the court grants 'permission' to see your own biological offspring.",
        "implication": "Accepting 'visitation' implies you need the court's permission to access your own offspring.",
    },
    "access to offspring": {
        "biological": "access to offspring",
        "framework": "natural",
        "jurisdiction": "Natural right — access to one's biological offspring is inherent, not granted.",
        "implication": "No court permission is required to access your own biological offspring.",
    },
    "guardian": {
        "biological": "parent",
        "framework": "legal",
        "jurisdiction": "Court-appointed — implies authority delegated by the state.",
        "implication": "A 'guardian' holds a legal title granted by the court. A parent holds a natural bond.",
    },
    "parent": {
        "biological": "parent",
        "framework": "natural",
        "jurisdiction": "Biological fact — established by DNA, not by court appointment.",
        "implication": "Parentage is not a title granted by any authority. It is a fact of nature.",
    },
    "ward": {
        "biological": "offspring",
        "framework": "legal",
        "jurisdiction": "Court-created — the offspring is treated as a subject of the court's authority.",
        "implication": "A 'ward' belongs to the court's jurisdiction. Offspring belong to their biological parents.",
    },
    "best interest of the child": {
        "biological": "natural right of the parent-offspring bond",
        "framework": "legal",
        "jurisdiction": "Statutory — a standard defined and applied by the court with broad discretion.",
        "implication": "The court decides what is 'best' — substituting judicial judgment for the natural bond.",
    },
    "termination of parental rights": {
        "biological": "attempted severance of a biological bond",
        "framework": "legal",
        "jurisdiction": "Statutory — the court purports to end a relationship it did not create.",
        "implication": "The legal status may be terminated. The biological bond cannot be.",
    },
    "child support": {
        "biological": "parental obligation to offspring",
        "framework": "legal",
        "jurisdiction": "Statutory — state-enforced financial obligation.",
        "implication": "The natural duty to provide for offspring exists independent of any court order.",
    },
}

REFRAME_PATTERNS = {
    "custody of": "natural bond with",
    "custody": "natural bond",
    "the minor child": "the offspring",
    "the minor children": "the offspring",
    "minor child": "offspring",
    "minor children": "offspring",
    "my children": "my offspring",
    "the children": "the offspring",
    "his children": "his offspring",
    "her children": "her offspring",
    "their children": "their offspring",
    "the child": "the offspring",
    "children": "offspring",
    "child": "offspring",
    "visitation": "access to offspring",
    "parenting time": "access to offspring",
    "custodial parent": "parent with offspring in their care",
    "non-custodial parent": "parent denied access to offspring",
    "noncustodial parent": "parent denied access to offspring",
    "best interest of the child": "natural right of the parent-offspring bond",
    "best interests of the child": "natural rights of the parent-offspring bond",
    "guardian ad litem": "court-appointed representative",
    "termination of parental rights": "attempted severance of a biological bond",
    "ward of the court": "offspring under court control",
    "ward": "offspring",
}

# --- Authority citations ---

AUTHORITIES = {
    "natural": [
        "John Locke, Second Treatise of Government (1689) — natural rights precede government",
        "William Blackstone, Commentaries (1765) — parent-child relation is the most universal in nature",
        "Declaration of Independence (1776) — unalienable rights endowed by Creator",
    ],
    "constitutional": [
        "Meyer v. Nebraska, 262 U.S. 390 (1923) — liberty includes right to raise children",
        "Pierce v. Society of Sisters, 268 U.S. 510 (1925) — child is not mere creature of the state",
        "Stanley v. Illinois, 405 U.S. 645 (1972) — unwed father has protected interest",
        "Troxel v. Granville, 530 U.S. 57 (2000) — oldest of fundamental liberty interests",
        "Santosky v. Kramer, 455 U.S. 745 (1982) — heightened standard for termination",
    ],
    "international": [
        "UN CRC Article 7 — right to know parents",
        "UN CRC Article 8 — preservation of identity",
        "UN CRC Article 9 — non-separation from parents",
        "UN CRC Article 18 — both parents responsible",
        "ECHR Article 8 — right to respect for family life",
        "UDHR Article 16(3) — family is the natural and fundamental group unit",
    ],
}


def _output(data: dict, fmt: str, title: str = ""):
    """Render output in the requested format."""
    if fmt == "json":
        console.print_json(json.dumps(data, indent=2))
    else:
        if "panel" in data:
            console.print(Panel(data["panel"], title=title, border_style="bold cyan"))
        if "table" in data:
            console.print(data["table"])
        if "sections" in data:
            for section_title, content in data["sections"]:
                console.print()
                console.print(Panel(content, title=section_title, border_style="cyan"))


@click.group()
def main():
    """dna-rights: Natural rights assertion toolkit.

    Assert biological parentage as a jurisdictional fact independent of any court.
    """
    pass


@main.command()
@click.option(
    "--relationship",
    default="parent-offspring",
    help="Relationship to assert (default: parent-offspring).",
)
@click.option(
    "--evidence",
    default="dna",
    help="Basis for assertion (default: dna).",
)
@click.option(
    "--format", "fmt",
    type=click.Choice(["text", "json"]),
    default="text",
    help="Output format.",
)
def assert_(relationship, evidence, fmt):
    """Generate a formal assertion of natural rights based on biological parentage."""
    assertion_text = (
        f"ASSERTION OF NATURAL RIGHTS\n\n"
        f"Relationship: {relationship}\n"
        f"Basis: {evidence.upper()}\n\n"
        f"The {relationship} bond is a natural right that exists by biology, "
        f"not by state grant. This bond was established at conception, is encoded "
        f"in DNA, and is beyond the jurisdiction of any court to create, modify, "
        f"or destroy.\n\n"
        f"The undersigned asserts the following:\n\n"
        f"1. The biological {relationship} bond exists as a fact of nature, "
        f"independent of any legal proceeding.\n\n"
        f"2. No court order created this bond. No court order can sever it.\n\n"
        f"3. DNA evidence does not 'prove' this bond to a court — it reveals "
        f"what already exists independent of any court.\n\n"
        f"4. Any legal proceeding that purports to modify the biological "
        f"{relationship} bond operates ultra vires — beyond the court's "
        f"jurisdiction.\n\n"
        f"5. The undersigned demands that any court asserting jurisdiction over "
        f"this biological bond identify the specific authority under which it "
        f"claims that jurisdiction."
    )

    authorities_text = "\n".join(
        f"  - {a}" for level in ["natural", "constitutional", "international"]
        for a in AUTHORITIES[level]
    )

    if fmt == "json":
        _output(
            {
                "type": "natural_rights_assertion",
                "relationship": relationship,
                "evidence": evidence,
                "assertion": assertion_text,
                "authorities": {
                    level: AUTHORITIES[level]
                    for level in ["natural", "constitutional", "international"]
                },
            },
            fmt,
        )
    else:
        panel_text = assertion_text + f"\n\n[bold]Authorities:[/bold]\n{authorities_text}"
        _output(
            {"panel": panel_text},
            fmt,
            title="[bold white]ASSERTION OF NATURAL RIGHTS[/bold white]",
        )


@main.command()
@click.option(
    "--type", "claim_type",
    default="offspring",
    help="Type of claim (default: offspring).",
)
@click.option(
    "--context",
    default="court",
    help="Context for the claim (default: court).",
)
@click.option(
    "--format", "fmt",
    type=click.Choice(["text", "json"]),
    default="text",
    help="Output format.",
)
def claim(claim_type, context, fmt):
    """Draft a DNA-based standing claim for court submission."""
    sections = [
        (
            "1. ESTABLISHMENT OF BIOLOGICAL FACT",
            "Respondent is the biological parent of the offspring identified herein, "
            "as established by DNA. This biological relationship was created at "
            "conception and exists independent of any legal proceeding, court order, "
            "or statutory framework.",
        ),
        (
            "2. ASSERTION OF NATURAL RIGHT",
            "The parent-offspring bond is a natural right recognized by the Supreme "
            "Court as 'the oldest of the fundamental liberty interests.' "
            "(Troxel v. Granville, 530 U.S. 57, 65 (2000)). This right is not "
            "created by statute and cannot be extinguished by court order. It exists "
            "by nature, established by DNA, and predates any legal system.",
        ),
        (
            "3. CHALLENGE TO JURISDICTION",
            "This Court has jurisdiction over legal relationships created by statute. "
            "The biological bond between a parent and their offspring was not created "
            "by statute. Respondent respectfully demands that this Court identify the "
            "specific authority under which it claims jurisdiction over a biological fact.",
        ),
        (
            "4. DEMAND FOR PERFORMANCE",
            "If this Court asserts jurisdiction over the biological parent-offspring "
            "bond, Respondent demands that the Court specifically identify:\n\n"
            "  (a) The source of that authority;\n"
            "  (b) The legal basis for overriding a natural right;\n"
            "  (c) The standard by which a biological fact becomes subject to "
            "judicial modification;\n"
            "  (d) The compelling state interest that justifies interference with "
            "the most fundamental of natural bonds.",
        ),
    ]

    if fmt == "json":
        _output(
            {
                "type": "dna_standing_claim",
                "claim_type": claim_type,
                "context": context,
                "sections": [
                    {"title": title, "content": content}
                    for title, content in sections
                ],
                "authorities": AUTHORITIES,
            },
            fmt,
        )
    else:
        console.print()
        console.print(
            Panel(
                f"[bold]Claim Type:[/bold] {claim_type}\n"
                f"[bold]Context:[/bold] {context}\n"
                f"[bold]Basis:[/bold] DNA — biological parentage as jurisdictional fact",
                title="[bold white]DNA-BASED STANDING CLAIM[/bold white]",
                border_style="bold cyan",
            )
        )
        _output({"sections": sections}, fmt)


@main.command()
@click.argument("term1")
@click.argument("term2")
@click.option(
    "--format", "fmt",
    type=click.Choice(["text", "json"]),
    default="text",
    help="Output format.",
)
def compare(term1, term2, fmt):
    """Side-by-side jurisdictional analysis of two terms."""
    t1 = term1.lower()
    t2 = term2.lower()

    info1 = TERM_MAP.get(t1)
    info2 = TERM_MAP.get(t2)

    if fmt == "json":
        _output(
            {
                "type": "term_comparison",
                "term1": {"term": t1, **(info1 or {"note": "Term not in database"})},
                "term2": {"term": t2, **(info2 or {"note": "Term not in database"})},
            },
            fmt,
        )
    else:
        table = Table(
            title=f"Jurisdictional Comparison: '{t1}' vs '{t2}'",
            show_header=True,
            header_style="bold cyan",
            border_style="cyan",
        )
        table.add_column("Dimension", style="bold")
        table.add_column(t1, style="red" if info1 and info1["framework"] == "legal" else "green")
        table.add_column(t2, style="red" if info2 and info2["framework"] == "legal" else "green")

        if info1 and info2:
            table.add_row("Framework", info1["framework"], info2["framework"])
            table.add_row("Biological Equivalent", info1["biological"], info2["biological"])
            table.add_row("Jurisdiction", info1["jurisdiction"], info2["jurisdiction"])
            table.add_row("Implication", info1["implication"], info2["implication"])
        else:
            if not info1:
                table.add_row("Status", f"'{t1}' not in term database", "")
            if not info2:
                table.add_row("Status", "", f"'{t2}' not in term database")
            if info1:
                table.add_row("Framework", info1["framework"], "---")
                table.add_row("Jurisdiction", info1["jurisdiction"], "---")
            if info2:
                table.add_row("Framework", "---", info2["framework"])
                table.add_row("Jurisdiction", "---", info2["jurisdiction"])

        console.print()
        console.print(table)

        if info1 and info2 and info1["framework"] != info2["framework"]:
            console.print()
            console.print(
                Panel(
                    f"[bold]'{t1}'[/bold] operates in the [red]{info1['framework']}[/red] framework. "
                    f"[bold]'{t2}'[/bold] operates in the [green]{info2['framework']}[/green] framework.\n\n"
                    f"Using '{t1}' accepts the court's jurisdiction. "
                    f"Using '{t2}' asserts a biological fact the court cannot adjudicate.",
                    title="[bold]Jurisdictional Shift[/bold]",
                    border_style="yellow",
                )
            )


@main.command()
@click.argument("text")
@click.option(
    "--format", "fmt",
    type=click.Choice(["text", "json"]),
    default="text",
    help="Output format.",
)
def reframe(text, fmt):
    """Rewrite statutory/legal language in natural rights terms."""
    original = text
    reframed = text

    changes = []
    # Sort patterns by length (longest first) to avoid partial replacements
    sorted_patterns = sorted(REFRAME_PATTERNS.keys(), key=len, reverse=True)

    for legal_term in sorted_patterns:
        natural_term = REFRAME_PATTERNS[legal_term]
        # Case-insensitive replacement
        lower_reframed = reframed.lower()
        idx = lower_reframed.find(legal_term.lower())
        while idx != -1:
            found_text = reframed[idx : idx + len(legal_term)]
            reframed = reframed[:idx] + natural_term + reframed[idx + len(legal_term):]
            changes.append({"from": found_text, "to": natural_term})
            lower_reframed = reframed.lower()
            idx = lower_reframed.find(legal_term.lower(), idx + len(natural_term))

    if fmt == "json":
        _output(
            {
                "type": "reframed_text",
                "original": original,
                "reframed": reframed,
                "changes": changes,
            },
            fmt,
        )
    else:
        console.print()
        console.print(
            Panel(
                f"[red strikethrough]{original}[/red strikethrough]",
                title="[bold]Original (Legal Framing)[/bold]",
                border_style="red",
            )
        )
        console.print(
            Panel(
                f"[bold green]{reframed}[/bold green]",
                title="[bold]Reframed (Natural Rights)[/bold]",
                border_style="green",
            )
        )

        if changes:
            table = Table(
                title="Term Substitutions",
                show_header=True,
                header_style="bold",
                border_style="cyan",
            )
            table.add_column("Legal Term", style="red")
            table.add_column("Natural Rights Term", style="green")
            for change in changes:
                table.add_row(change["from"], change["to"])
            console.print()
            console.print(table)
        else:
            console.print()
            console.print("[yellow]No legal terms found to reframe.[/yellow]")


if __name__ == "__main__":
    main()
