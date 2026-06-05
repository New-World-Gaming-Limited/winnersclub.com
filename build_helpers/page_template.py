"""
Shared page template builder for 1win.codes EN expansion.
All new pages MUST be built with this so header/footer/CSS/scripts stay in sync.

Usage:
    from build_helpers.page_template import render_page
    html = render_page(
        slug='tools/odds-converter',
        title='Odds Converter, Decimal/Fractional/American at 1win',
        description='Convert decimal, fractional, American, Hong Kong, Indonesian and Malay odds instantly. Free tool at 1win.',
        h1='Odds converter',
        breadcrumbs=[('Home','/'), ('Tools','/en/tools/'), ('Odds converter', None)],
        main_html='<section>...</section>',
        extra_head='',  # optional extra <head> content (e.g. game schema)
        extra_scripts='',  # optional inline JS at end of body
    )
    open('en/tools/odds-converter.html','w').write(html)

Rules enforced:
- canonical = https://1win.codes/en/<slug>
- hreflang en + x-default both point at the EN slug
- No em (—) or en (–) dashes anywhere in title/description/h1
- breadcrumb JSON-LD auto-built
- WebPage JSON-LD auto-built
"""
import re
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _load(name):
    with open(os.path.join(REPO, 'build_helpers', name)) as f:
        return f.read()

def _strip_dashes(s):
    return s.replace('—', ',').replace('–', ',').replace('  ', ' ').strip()

def render_page(slug, title, description, h1, breadcrumbs, main_html,
                extra_head='', extra_scripts='', extra_schema=''):
    """
    slug: path after /en/  e.g. 'tools/odds-converter' or 'slots/sweet-bonanza'
    breadcrumbs: list of (label, href|None) — last entry must have href=None (current page)
    extra_schema: additional JSON-LD blocks (already wrapped in <script> tags)
    """
    title = _strip_dashes(title)
    description = _strip_dashes(description)
    h1 = _strip_dashes(h1)
    canonical = f'https://1win.codes/en/{slug}'
    # Build breadcrumb JSON-LD
    items = []
    for i, (label, href) in enumerate(breadcrumbs, 1):
        item = {
            "@type": "ListItem",
            "position": i,
            "name": label,
        }
        if href:
            item["item"] = f'https://1win.codes{href}' if href.startswith('/') else href
        items.append(item)
    import json
    breadcrumb_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }, indent=2, ensure_ascii=False)

    webpage_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": description,
        "url": canonical,
        "isPartOf": {
            "@type": "WebSite",
            "name": "1win.codes",
            "url": "https://1win.codes/"
        }
    }, indent=2, ensure_ascii=False)

    # Build breadcrumb HTML
    crumb_html = '\n        '.join(
        f'<a href="{href}">{label}</a>' if href else f'<span aria-current="page">{label}</span>'
        for label, href in breadcrumbs
    )

    head = _load('shell_head.html')
    header = _load('shell_header.html')
    footer = _load('shell_footer.html')

    # Substitute placeholders in head
    head = (head
        .replace('{{TITLE}}', title)
        .replace('{{DESCRIPTION}}', description)
        .replace('{{CANONICAL}}', canonical)
        .replace('{{SLUG}}', slug)
        .replace('{{WEBPAGE_JSONLD}}', webpage_jsonld)
        .replace('{{BREADCRUMB_JSONLD}}', breadcrumb_jsonld)
        .replace('{{EXTRA_HEAD}}', extra_head)
        .replace('{{EXTRA_SCHEMA}}', extra_schema)
    )

    body = f"""<body>
{header}
  <main>
    <nav class="breadcrumbs" aria-label="Breadcrumb">
      <div class="container">
        {crumb_html}
      </div>
    </nav>
    <article class="page-content">
      <div class="container">
        <h1>{h1}</h1>
        {main_html}
      </div>
    </article>
  </main>
{footer}
  <script src="/script.min.js" defer></script>
  {extra_scripts}
</body>
</html>"""

    return head + '\n' + body
