#!/usr/bin/env python3
"""
Mark the current locale's option as `selected` so the switcher shows the user
where they are. Also shorten the selected label to the 2-letter code.
"""
import os, re, glob

ROOT = "/home/user/workspace/winnersclub.com"

# (locale_prefix_path, code, native_name)
LOCALES = [
    ("",   "EN", "English"),
    ("ko", "KO", "한국어"),
    ("zh", "ZH", "中文"),
    ("vi", "VI", "Tiếng Việt"),
    ("th", "TH", "ไทย"),
    ("ms", "MS", "Bahasa Melayu"),
    ("pt", "PT", "Português"),
    ("ja", "JA", "日本語"),
]

def locale_of(path):
    rel = os.path.relpath(path, ROOT)
    first = rel.split(os.sep)[0]
    if first in {"ko","zh","vi","th","ms","pt","ja"}:
        return first
    return ""  # en

def update(html, current_locale):
    # 1. Strip any existing `selected` attribute on options.
    html = re.sub(r'(<option[^>]*?)\s+selected(?=[\s>])', r'\1', html)
    # 2. Always: value="" is the SELF/current page option (regardless of locale).
    #    Mark it selected and use the 2-letter code as visible label.
    self_code = dict([(loc, c) for loc, c, _ in LOCALES]).get(current_locale, "EN")
    html = re.sub(
        r'<option\s+value=""\s*>([^<]+)</option>',
        f'<option value="" selected>{self_code}</option>',
        html
    )
    # 3. For each NON-self locale option, set the visible label to the native name.
    for prefix, code, native in LOCALES:
        if prefix == current_locale:
            continue
        if prefix == "":
            vp = r'value="https://winnersclub\.com/"'
            vp_lit = 'value="https://winnersclub.com/"'
        else:
            vp = rf'value="https://winnersclub\.com/{prefix}/"'
            vp_lit = f'value="https://winnersclub.com/{prefix}/"'
        opt_re = re.compile(rf'<option\s+{vp}\s*>([^<]+)</option>')
        html = opt_re.sub(f'<option {vp_lit}>{native}</option>', html)
    return html

changed = 0
for fp in glob.glob(f"{ROOT}/**/*.html", recursive=True):
    if "/node_modules/" in fp:
        continue
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    if "lang-switcher" not in html:
        continue
    loc = locale_of(fp)
    new = update(html, loc)
    if new != html:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new)
        changed += 1

print(f"Files updated: {changed}")
