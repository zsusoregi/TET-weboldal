# -*- coding: utf-8 -*-
"""A motor által épített HTML utófeldolgozása: a §TERMEK§ jelölő helyére a kiemelt terméknév kerül.
Használat: python3 gen/utofeldolgozas.py <html> [<html> ...]"""
import sys
from pathlib import Path

TERMEK = ('<span class="termek"><b>Tantraszex Edzésterv</b>'
          '<small>Online gyakorlóprogram 45+ férfiaknak</small></span>')
CSS = ('<style>.termek{display:block;margin:26px 0 18px;padding:14px 0 14px 18px;border-left:4px solid var(--c-primary)}'
       '.termek b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.55rem,3cqi,2.5rem);'
       'line-height:1.05;letter-spacing:.05em;text-transform:uppercase;color:var(--hl)}'
       '.termek small{display:block;margin-top:8px;font-family:var(--f-label);font-size:.8rem;font-weight:600;letter-spacing:.18em;'
       'text-transform:uppercase;color:var(--c-ink-2)}.termek+br{display:none}'
       '[style*="text-align:center"] .termek,.shead:not(.bal) .termek{border-left:0;padding-left:0}</style>')

for f in sys.argv[1:]:
    p = Path(f)
    s = p.read_text(encoding="utf-8")
    n = s.count("§TERMEK§")
    s = s.replace("§TERMEK§", TERMEK)
    if "</head>" in s:
        s = s.replace("</head>", CSS + "</head>", 1)
    elif "</title>" in s:
        s = s.replace("</title>", "</title>" + CSS, 1)
    else:
        s = CSS + s
    p.write_text(s, encoding="utf-8")
    print(f"{f}: {n} csere")
