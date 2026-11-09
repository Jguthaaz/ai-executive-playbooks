"""Validate Navigator Markdown targets/anchors and synthetic scenario arithmetic.
Run from any directory: python frameworks-mapping/validate.py
Does not check live HTTP availability or business validity.
"""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ("frameworks-catalog", "frameworks-mapping", "decision-journeys",
           "tools-and-templates", "worked-examples")

def anchors(text):
    found, counts = set(), {}
    for title in re.findall(r"^#{1,6} +(.+)$", text, re.M):
        title = title.lower().strip()
        title = "".join(c for c in title if c.isalnum() or c in " _-")
        slug = title.replace(" ", "-")
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        found.add(slug if n == 0 else f"{slug}-{n}")
    return found

def main():
    files = [ROOT / "README.md"]
    files += [p for folder in FOLDERS for p in (ROOT / folder).glob("*.md")]
    checked = 0
    external = set()
    errors = []
    for source in files:
        text = source.read_text(encoding="utf-8")
        for link in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
            parts = urlsplit(link)
            if parts.scheme in ("https", "http"):
                external.add(link)
                continue
            if parts.scheme:
                errors.append(f"{source}: unexpected scheme: {link}")
                continue
            target = (source.parent / unquote(parts.path)).resolve() if parts.path else source
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{source}: missing/unsafe target: {link}")
            elif parts.fragment and target.suffix == ".md":
                if unquote(parts.fragment) not in anchors(target.read_text(encoding="utf-8")):
                    errors.append(f"{source}: missing anchor: {link}")
            checked += 1
    # Scenario calculations; these are invented assumptions, not observations.
    volume = 200 * .60
    assert volume == 120
    assert volume * (40 - 30) / 60 == 20
    assert volume * (40 - 25) / 60 == 30
    assert volume * (30 - 25) / 60 == 10
    assert volume * (30 - 35) / 60 == -10
    assert 200 * .30 * (30 - 25) / 60 == 5
    assert 10 * 30 - 400 == -100
    assert len(list((ROOT / "frameworks-catalog").glob("*.md"))) == 9
    matrix = (ROOT / "frameworks-mapping/README.md").read_text(encoding="utf-8")
    assert all(term in matrix for term in ("Overlap", "Complement", "Sequence", "Cross-cutting", "Alternative"))
    assert all(f"R{i:02}" in matrix for i in range(1, 12))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(files)} Markdown files; {checked} relative links/anchors; "
          f"{len(external)} unique external URLs inventoried; 7 arithmetic assertions; "
          "8 cards and 11 relationships. External HTTP checks are separate.")

if __name__ == "__main__":
    main()
