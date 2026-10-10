# -*- coding: utf-8 -*-
"""A motor által épített HTML utófeldolgozása:
 - a §TERMEK§ jelölő helyére a kiemelt terméknév kerül (hero),
 - az Impresszum felugró ablak (a lábléc „Impresszum” linkje nyitja).
Használat: python3 gen/utofeldolgozas.py <html> [<html> ...]"""
import sys
from html import escape as esc
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from alap_gen import IMPRESSZUM

TERMEK = ('<span class="termek"><b>Tantraszex Edzésterv</b>'
          '<small>Online gyakorlóprogram 45+ férfiaknak</small></span>')
CSS = ('<style>.termek{display:block;margin:26px 0 18px;padding:14px 0 14px 18px;border-left:4px solid var(--c-primary)}'
       '.termek b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.55rem,3cqi,2.5rem);'
       'line-height:1.05;letter-spacing:.05em;text-transform:uppercase;color:var(--hl)}'
       '.termek small{display:block;margin-top:8px;font-family:var(--f-label);font-size:.8rem;font-weight:600;letter-spacing:.18em;'
       'text-transform:uppercase;color:var(--c-ink-2)}.termek+br{display:none}'
       '[style*="text-align:center"] .termek,.shead:not(.bal) .termek{border-left:0;padding-left:0}'
       'dialog.impr{width:min(560px,calc(100vw - 28px));max-height:calc(100vh - 40px);padding:0;border:0;border-radius:18px;'
       'background:#fffbf4;color:#2b1b12;box-shadow:0 40px 90px -30px rgba(0,0,0,.55);font:400 15px/1.55 system-ui,sans-serif}'
       'dialog.impr::backdrop{background:rgba(12,8,6,.62)}'
       'dialog.impr .in{padding:28px 30px 26px;position:relative}'
       'dialog.impr h3{margin:0 0 16px;font:600 1.4rem/1.2 Georgia,serif;color:#2b1b12}'
       'dialog.impr h4{margin:18px 0 6px;font:700 .72rem/1 system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#b54e02}'
       'dialog.impr dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 14px;margin:0}'
       'dialog.impr dt{color:#7a6658}dialog.impr dd{margin:0}dialog.impr a{color:#b54e02}'
       'dialog.impr .zar{position:absolute;right:12px;top:10px;width:38px;height:38px;border-radius:50%;border:1px solid #d9c9bb;'
       'background:transparent;font-size:1.4rem;line-height:1;cursor:pointer;color:inherit}</style>')


def dl(sorok):
    out = []
    for k, v in sorok:
        if "@" in v:
            v = f'<a href="mailto:{esc(v)}">{esc(v)}</a>'
        elif v.startswith("+36"):
            v = f'<a href="tel:{v.replace(" ", "")}">{esc(v)}</a>'
        elif v.startswith("www."):
            v = f'<a href="https://{esc(v)}" target="_blank" rel="noopener">{esc(v)}</a>'
        else:
            v = esc(v)
        out.append(f"<dt>{esc(k)}</dt><dd>{v}</dd>")
    return "<dl>" + "".join(out) + "</dl>"


ABLAK = ('<dialog class="impr" id="impresszum" aria-label="Impresszum" onclick="if(event.target===this)this.close()"><div class="in">'
         '<form method="dialog"><button class="zar" aria-label="Bezárás">×</button></form><h3>Impresszum</h3>'
         '<h4>A szolgáltató</h4>' + dl(IMPRESSZUM["szolgaltato"]) + '<h4>Tárhelyszolgáltató</h4>' + dl(IMPRESSZUM["tarhely"])
         + '</div></dialog><script>document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(\'a[href="#impresszum"]\');'
         'if(a){e.preventDefault();var d=document.getElementById("impresszum");if(d&&d.showModal)d.showModal();}});</script>')

for f in sys.argv[1:]:
    p = Path(f)
    s = p.read_text(encoding="utf-8")
    n = s.count("§TERMEK§")
    s = s.replace("§TERMEK§", TERMEK)
    # a motor végleges-oldal építője hibásan "hatNone" osztályt ír a sima szekcióhatárra
    s = s.replace('class="hatNone"', 'class="hat"')
    if "</head>" in s:
        s = s.replace("</head>", CSS + "</head>", 1)
    elif "</title>" in s:
        s = s.replace("</title>", "</title>" + CSS, 1)
    else:
        s = CSS + s
    s = s.replace("</body>", ABLAK + "</body>", 1) if "</body>" in s else s + ABLAK
    p.write_text(s, encoding="utf-8")
    print(f"{f}: {n} csere + impresszum")
