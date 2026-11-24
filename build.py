#!/usr/bin/env python3
"""Build the static ATRON site into public/.

Sources:
  src/index.html  page template (elements with data-k get their copy here)
  src/copy.json   home-page copy, agent list and statuses (TR + EN)
  src/content.py  head meta, FAQ and the agent pages

Every page ships fully rendered in its own language, so search engines and
AI crawlers read the real text without running JavaScript.

Run:  python3 build.py
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
from content import AGENTS, FAQ, HEAD, SITE  # noqa: E402

PUB = ROOT / "public"
TPL = (ROOT / "src/index.html").read_text()
COPY = json.loads((ROOT / "src/copy.json").read_text())
T, ARMS, STATUS = COPY["T"], COPY["ARMS"], COPY["STATUS"]
LANGS = ("tr", "en")
HOME = {"tr": "/", "en": "/en/"}
RUNTIME_PREFIXES = ("live.", "brief.", "f.", "p.", "who.", "copy.")
ORG = {
    "@type": "Organization",
    "@id": f"{SITE}/#org",
    "name": "AI for People Teknoloji A.Ş.",
    "alternateName": "AI for People",
    "url": "https://aiforpeople.co",
    "logo": f"{SITE}/logo.png",
    "email": "can@atronai.co",
    "address": {"@type": "PostalAddress", "addressLocality": "İstanbul", "addressCountry": "TR"},
    "founder": {
        "@type": "Person",
        "name": "Can Çelikay",
        "sameAs": ["https://www.linkedin.com/in/can-celikay-391b0015"],
    },
}


def esc(s):
    return html.escape(s, quote=True)


def agent_url(agent, lang):
    return f"/ajanlar/{agent['slug']['tr']}/" if lang == "tr" else f"/en/agents/{agent['slug']['en']}/"


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def head(lang, title, desc, path, alt_paths, extra_ld):
    hreflang = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{alt_paths[l]}">' for l in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt_paths["tr"]}">'
    return "\n".join([
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(desc)}">',
        f'<link rel="canonical" href="{SITE}{path}">',
        hreflang,
        '<link rel="icon" href="/favicon.ico">',
        '<meta name="theme-color" content="#07080c">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:locale" content="{HEAD[lang]["locale"]}">',
        f'<meta property="og:url" content="{SITE}{path}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:image" content="{SITE}/img/og.jpg">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:image" content="{SITE}/img/og.jpg">',
        ld({"@context": "https://schema.org", "@graph": [ORG] + extra_ld}),
    ])


def langsw(lang, alt_paths):
    out = ['<div class="lang" role="group" aria-label="Language">']
    for l in LANGS:
        cur = ' aria-current="page"' if l == lang else ""
        out.append(f'<a href="{alt_paths[l]}" hreflang="{l}" lang="{l}"{cur}>{l.upper()}</a>')
    out.append("</div>")
    return "".join(out)


def arms_html(lang):
    rows = []
    by_arm = {a["arm"]: a for a in AGENTS}
    for i, a in enumerate(ARMS):
        name = esc(a["k"][lang])
        if i in by_arm:
            name = f'<a href="{agent_url(by_arm[i], lang)}">{name} <span class="go">→</span></a>'
        dot = "" if a["s"] == "yours" else '<span class="dot"></span>'
        cls = "arm fade" + (" yours" if a["s"] == "yours" else "")
        rows.append(
            f'<div class="{cls}"><span class="mono n">0{i + 1}</span><h4>{name}</h4>'
            f'<p>{esc(a["p"][lang])}</p><span class="mono s {a["s"]}">{dot}<span>{esc(STATUS[a["s"]][lang])}</span></span></div>'
        )
    return "".join(rows)


def faq_html(items, label, h, hid="h-faq"):
    qs = "".join(
        f'<details class="qa fade"><summary><h3>{esc(q)}</h3><span class="pm" aria-hidden="true"></span></summary><p>{esc(a)}</p></details>'
        for q, a in items
    )
    return (
        f'<section id="sss" aria-labelledby="{hid}"><div class="wrap"><div class="sec-head">'
        f'<p class="mono"><span>{esc(label)}</span><span>FAQ</span></p>'
        f'<h2 id="{hid}" class="wide fade">{esc(h)}</h2></div><div class="faq">{qs}</div></div></section>'
    )


def faq_ld(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items
        ],
    }


def fill_copy(page, lang):
    pat = re.compile(r'(<(\w+)\b[^>]*?\bdata-k="([^"]+)"[^>]*>)(.*?)(</\2>)', re.S)

    def rep(m):
        key = m.group(3)
        if key not in T:
            return m.group(0)
        val = T[key][lang]
        if "data-html" not in m.group(1):
            val = esc(val)
        return m.group(1) + val + m.group(5)

    return pat.sub(rep, page)


def build_home(lang):
    path = HOME[lang]
    product = {
        "@type": "SoftwareApplication",
        "@id": f"{SITE}/#atron",
        "name": "ATRON",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "url": f"{SITE}{path}",
        "description": HEAD[lang]["desc"],
        "publisher": {"@id": f"{SITE}/#org"},
        "inLanguage": lang,
    }
    website = {"@type": "WebSite", "@id": f"{SITE}/#site", "url": SITE, "name": "ATRON", "publisher": {"@id": f"{SITE}/#org"}}
    page = TPL
    page = page.replace("{{LANG}}", lang)
    page = page.replace("{{HEAD}}", head(lang, HEAD[lang]["title"], HEAD[lang]["desc"], path, HOME,
                                         [website, product, faq_ld(FAQ[lang]["items"])]))
    page = page.replace("{{LANGSW}}", langsw(lang, HOME))
    page = page.replace("{{ARMS}}", arms_html(lang))
    page = page.replace("{{FAQ}}", faq_html(FAQ[lang]["items"], FAQ[lang]["label"], FAQ[lang]["h"]))
    runtime = {k: v[lang] for k, v in T.items() if k.startswith(RUNTIME_PREFIXES)}
    page = page.replace("{{RUNTIME}}", json.dumps(runtime, ensure_ascii=False))
    if lang == "en":
        page = page.replace("subject=ATRON%20%C2%B7%20G%C3%B6r%C3%BC%C5%9Fme", "subject=ATRON%20%C2%B7%20Call")
    page = fill_copy(page, lang)
    assert "{{" not in page, re.findall(r"\{\{\w+\}\}", page)
    return page


AGENT_TPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
<link rel="preload" href="/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/site.css">
</head>
<body class="sub">
<script>document.documentElement.classList.add('js');</script>
<header class="solid">
  <div class="wrap nav">
    <a class="logo" href="{home}" aria-label="ATRON"><img src="/logo.png" alt="ATRON" width="1037" height="266"></a>
    <nav class="mono"><a class="hide-m" href="{home}#canli">{try_live}</a>{langsw}</nav>
  </div>
</header>
<main>
<section class="agent-hero">
  <div class="wrap">
    <p class="mono crumb"><a href="{home}">ATRON</a> / <span>{label}</span></p>
    <h1 class="wide">{h1}</h1>
    <div class="agent-top">
      <p class="body">{intro}</p>
      <p class="mono where"><span class="dot"></span><span>{where}</span></p>
    </div>
  </div>
</section>
<section class="agent-body">
  <div class="wrap agent-grid">
    <figure class="frame-img r45"><picture><source srcset="/img/{img}.webp" type="image/webp"><img src="/img/{img}.jpg" alt="" loading="lazy"></picture></figure>
    <div>
      <h2 class="mono sub-h">{does_h}</h2>
      <div class="steps">{does}</div>
      <h2 class="mono sub-h">{connect_h}</h2>
      <p class="body dim">{connect}</p>
    </div>
  </div>
</section>
{faq}
</main>
<section class="contact" id="iletisim">
  <div class="wrap">
    <h2 class="display">{cta_h}</h2>
    <p class="body">{cta_p}</p>
    <div class="row">
      <a class="chip solid mono" href="{home}#canli"><span>{try_live}</span><span class="arr">→</span></a>
      <a class="chip mono" href="mailto:can@atronai.co"><span>can@atronai.co</span></a>
    </div>
  </div>
</section>
<footer><div class="wrap mono"><span>{foot_a}</span><span>Vadi İstanbul · Sarıyer / İstanbul</span><span>{foot_b}</span><span>© 2026</span></div></footer>
</body>
</html>
"""


def build_agent(agent, lang):
    c = agent[lang]
    path = agent_url(agent, lang)
    alt = {l: agent_url(agent, l) for l in LANGS}
    service = {
        "@type": "Service",
        "name": re.sub(r"<[^>]+>", "", c["h1"]),
        "description": c["desc"],
        "provider": {"@id": f"{SITE}/#org"},
        "serviceType": c["label"].split("·")[-1].strip(),
        "url": f"{SITE}{path}",
    }
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ATRON", "item": f"{SITE}{HOME[lang]}"},
            {"@type": "ListItem", "position": 2, "name": c["label"], "item": f"{SITE}{path}"},
        ],
    }
    does = "".join(
        f'<div class="step"><span class="mono k">{esc(k)}</span><div><p>{esc(v)}</p></div></div>' for k, v in c["does"]
    )
    faq_label = "Sık sorulanlar" if lang == "tr" else "FAQ"
    faq_h = "Kısa cevaplar." if lang == "tr" else "Short answers."
    out = AGENT_TPL.format(
        lang=lang,
        head=head(lang, c["title"], c["desc"], path, alt, [service, crumbs, faq_ld(c["faq"])]),
        home=HOME[lang],
        try_live=esc(T["hero.cta1"][lang]),
        langsw=langsw(lang, alt),
        label=esc(c["label"]),
        h1=c["h1"],
        intro=esc(c["intro"]),
        where=esc(c["where"]),
        img=agent["img"],
        does_h=esc(c["does_h"]),
        does=does,
        connect_h=esc(c["connect_h"]),
        connect=esc(c["connect"]),
        faq=faq_html(c["faq"], faq_label, faq_h),
        cta_h=esc(T["contact.h"][lang]),
        cta_p=esc(T["contact.body"][lang]),
        foot_a=esc(T["foot.a"][lang]),
        foot_b=esc(T["foot.b"][lang]),
    )
    return path, out


def write(path, text):
    f = PUB / path.lstrip("/")
    if path.endswith("/"):
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text)


def main():
    urls = []
    for lang in LANGS:
        write(HOME[lang], build_home(lang))
        urls.append(({l: HOME[l] for l in LANGS}, "1.0"))
    for agent in AGENTS:
        for lang in LANGS:
            path, page = build_agent(agent, lang)
            write(path, page)
        urls.append(({l: agent_url(agent, l) for l in LANGS}, "0.8"))

    # sitemap with hreflang pairs
    seen, items = set(), []
    for alt, prio in urls:
        for l in LANGS:
            if alt[l] in seen:
                continue
            seen.add(alt[l])
            links = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{SITE}{alt[x]}"/>' for x in LANGS)
            items.append(f"<url><loc>{SITE}{alt[l]}</loc>{links}<priority>{prio}</priority></url>")
    (PUB / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(items) + "</urlset>\n"
    )

    (PUB / "robots.txt").write_text(
        "# Search engines and AI assistants are welcome to read and cite this site.\n"
        "User-agent: *\nAllow: /\nDisallow: /api/\n\n"
        + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in
                  ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
                   "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"])
        + f"Sitemap: {SITE}/sitemap.xml\n"
    )

    en = FAQ["en"]["items"]
    agents_md = "\n".join(
        f"- [{re.sub(r'<[^>]+>', '', a['en']['h1'])}]({SITE}{agent_url(a, 'en')}): {a['en']['desc']} "
        f"(Turkish: {SITE}{agent_url(a, 'tr')})"
        for a in AGENTS
    )
    faq_md = "\n\n".join(f"### {q}\n{a}" for q, a in en)
    (PUB / "llms.txt").write_text(f"""# ATRON

> {HEAD['en']['desc']} Built in Istanbul by AI for People Teknoloji A.Ş. Site in Turkish ({SITE}/) and English ({SITE}/en/).

ATRON is an operations layer: one shared core (memory, rules, quality control, integrations) and AI agents that each own one job, such as answering inbound calls, reading every WhatsApp sales chat, or calling cold lead lists. A new job doesn't need new software; it needs a new agent on the same core.

Proof: two ATRON projects are on Renault Innovation Hub's global shortlist. Inbound voice, WhatsApp sales QA and outbound win-back calling run in production for an enterprise health-tourism operator (under NDA).

How engagements work: a working prototype in the client's own process in week one, then a pilot on real data judged against one agreed metric, then production in the client's systems.

Contact: can@atronai.co

## Agents

{agents_md}

## FAQ

{faq_md}
""")
    print("built:", len(seen), "pages")


if __name__ == "__main__":
    main()
