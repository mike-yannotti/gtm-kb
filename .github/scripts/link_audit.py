
import os, sys, re
from html.parser import HTMLParser
from urllib.parse import urlparse

SITE_DIR = os.environ.get("SITE_DIR", "site")

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag != "a": return
        href = dict(attrs).get("href")
        if href: self.links.append(href)

def is_external(href):
    if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
        return True
    parsed = urlparse(href)
    return bool(parsed.scheme) and parsed.scheme in ("http","https")

def resolve_internal(target, html_path):
    # Return actual file path in site/ for a given href relative to html_path
    # Normalize anchors and query
    target = target.split("#",1)[0].split("?",1)[0]
    if not target: return None
    # Remove leading slash (site is root)
    while target.startswith("/"):
        target = target[1:]
    base = os.path.dirname(html_path)
    joined = os.path.normpath(os.path.join(base, target))
    # If href ends with '/', append index.html
    if target.endswith("/"):
        path = os.path.join(joined, "index.html")
        return path
    # If href ends with '.html', check that file
    if target.endswith(".html"):
        return joined
    # Otherwise try as a directory index.html first
    candidate = os.path.join(joined, "index.html")
    if os.path.exists(os.path.join(SITE_DIR, candidate)):
        return candidate
    # Then try appending '.html'
    candidate2 = joined + ".html"
    return candidate2

def main():
    missing = []
    checked_total = 0
    for root, _, files in os.walk(SITE_DIR):
        for fn in files:
            if not fn.endswith(".html"): continue
            html_rel = os.path.relpath(os.path.join(root, fn), SITE_DIR)
            with open(os.path.join(root, fn), "r", encoding="utf-8", errors="ignore") as f:
                data = f.read()
            parser = LinkExtractor()
            parser.feed(data)
            for href in parser.links:
                if is_external(href): 
                    continue
                resolved = resolve_internal(href, html_rel)
                if not resolved: 
                    continue
                checked_total += 1
                full = os.path.join(SITE_DIR, resolved)
                if not os.path.exists(full):
                    missing.append((html_rel, href, resolved))
    if missing:
        print("Broken internal links detected:")
        for page, href, resolved in missing:
            print(f"- On {page}: href='{href}' -> not found (expected '{resolved}')")
        print(f"\nTotal missing: {len(missing)} (checked {checked_total} internal links)")
        sys.exit(1)
    print(f"No broken internal links. Checked {checked_total} internal links.")
    sys.exit(0)

if __name__ == "__main__":
    main()
