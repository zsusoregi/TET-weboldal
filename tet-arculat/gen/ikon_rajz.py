# -*- coding: utf-8 -*-
"""Saját rajzolású ikonok (OpenAI nélkül): 6 ikon × 5 stílus, SVG-ből Chromiummal PNG-be.
Futtatás a munkamappából: python3 gen/ikon_rajz.py"""
import json, subprocess, tempfile, shutil
from pathlib import Path
from PIL import Image

MUNKA = Path(__file__).resolve().parent.parent
SPEC = json.loads((MUNKA / "ikon-spec.json").read_text(encoding="utf-8"))
C = SPEC["szinek"]
P, A, A2, INK = C["primary"], C["accent"], C["accent2"], C["ink"]
LIGHT = "#F6D9BF"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# Minden ikon: 'vonal' (körvonalas rajz, a stroke a stílusból jön) és 'telt' (kitöltött formák: [szerep, svg-elem]).
# Szerepek: p = fő szín, a = kiemelő, d = sötét (accent2), l = halvány; 'vastag' = vastag, telt vonal.
IKONOK = {
    "figyelem": dict(
        vonal="<path d='M12 54Q50 20 88 54Q50 88 12 54Z'/><circle cx='50' cy='54' r='13'/><circle cx='50' cy='54' r='4' fill='currentColor'/>"
              "<path d='M50 10v11M27 17l6 9M73 17l-6 9'/>",
        telt=[("a", "<path d='M10 54Q50 18 90 54Q50 90 10 54Z'/>"), ("p", "<circle cx='50' cy='54' r='16'/>"),
              ("d", "<circle cx='50' cy='54' r='6'/>"), ("l", "<circle cx='44' cy='48' r='3.5'/>"),
              ("vp", "<path d='M50 8v12M26 15l6 9M74 15l-6 9'/>")]),
    "legzes": dict(
        vonal="<path d='M12 34C30 20 46 46 64 32S84 24 90 28'/><path d='M10 52C28 38 46 64 64 50S84 42 92 46'/><path d='M16 70C32 58 48 82 66 68S82 62 86 64'/>",
        telt=[("vp", "<path d='M12 32C30 18 46 44 64 30S84 22 90 26'/>"), ("va", "<path d='M10 52C28 38 46 64 64 50S84 42 92 46'/>"),
              ("vd", "<path d='M16 72C32 60 48 84 66 70S82 64 86 66'/>")]),
    "erintes": dict(
        vonal="<path d='M34 92V56C34 51 41 51 41 56V34C41 29 48 29 48 34V30C48 25 55 25 55 30V34C55 29 62 29 62 34V40C62 35 69 35 69 40V68C69 82 61 92 50 92Z'/><path d='M34 70C29 63 22 64 23 70L33 84'/><path d='M48 34V56M55 32V56M62 40V58'/><path d='M33 20Q48 9 63 20M27 11Q48 -3 69 11'/>",
        telt=[("p", "<path d='M34 92V56C34 51 41 51 41 56V34C41 29 48 29 48 34V30C48 25 55 25 55 30V34C55 29 62 29 62 34V40C62 35 69 35 69 40V68C69 82 61 92 50 92Z'/>"), ("p", "<path d='M36 66C29 58 20 60 21 68L33 85Z'/>"),
              ("wl", "<path d='M48 40V56M55 38V56M62 44V58'/>"), ("va", "<path d='M33 20Q48 9 63 20M27 11Q48 -3 69 11'/>")]),
    "izgalom": dict(
        vonal="<path d='M50 8C58 28 78 38 78 62A28 28 0 0 1 22 62C22 46 32 38 37 25 41 37 45 42 50 44 55 33 55 20 50 8Z'/>"
              "<path d='M50 50C56 58 62 62 62 70A12 12 0 0 1 38 70C38 62 44 58 50 50Z'/>",
        telt=[("p", "<path d='M50 6C58 26 80 38 80 62A30 30 0 0 1 20 62C20 46 31 37 36 23 41 36 45 41 50 43 55 32 55 19 50 6Z'/>"),
              ("a", "<path d='M50 46C57 55 65 60 65 70A15 15 0 0 1 35 70C35 60 43 55 50 46Z'/>"),
              ("l", "<path d='M50 62C53 66 56 68 56 72A6 6 0 0 1 44 72C44 68 47 66 50 62Z'/>")]),
    "szabalyozas": dict(
        vonal="<circle cx='50' cy='50' r='38'/><path d='M22 52C30 36 40 36 50 50S70 64 78 48'/><circle cx='50' cy='50' r='3' fill='currentColor'/>",
        telt=[("a", "<circle cx='50' cy='50' r='40'/>"), ("l", "<circle cx='50' cy='50' r='30'/>"),
              ("vp", "<path d='M22 52C30 36 40 36 50 50S70 64 78 48'/>"), ("d", "<circle cx='50' cy='50' r='4.5'/>")]),
    "homokora": dict(
        vonal="<path d='M24 12H76M24 88H76'/><path d='M30 12C30 34 46 42 46 50S30 66 30 88M70 12C70 34 54 42 54 50S70 66 70 88'/>"
              "<path d='M38 26H62L50 42Z' fill='currentColor' stroke='none'/><path d='M50 54V76'/><path d='M36 82Q50 68 64 82Z' fill='currentColor' stroke='none'/>",
        telt=[("l", "<path d='M30 14C30 34 46 42 46 50S30 66 30 86H70C70 66 54 58 54 50S70 34 70 14Z'/>"),
              ("a", "<path d='M37 24H63L50 42Z'/>"), ("a", "<path d='M34 86Q50 66 66 86Z'/>"), ("vd", "<path d='M50 46V80'/>"),
              ("p", "<rect x='20' y='6' width='60' height='10' rx='5'/>"), ("p", "<rect x='20' y='84' width='60' height='10' rx='5'/>")]),
}

SZIN = {"p": P, "a": A, "d": A2, "l": LIGHT}


def telt_elemek(ik, vastag=9, fill_map=None, extra=""):
    fm = fill_map or SZIN
    out = []
    for szerep, el in IKONOK[ik]["telt"]:
        if szerep.startswith("w"):
            out.append(f"<g fill='none' stroke='{fm[szerep[1]]}' stroke-width='3' stroke-linecap='round' {extra}>{el}</g>")
        elif szerep.startswith("v"):
            out.append(f"<g fill='none' stroke='{fm[szerep[1]]}' stroke-width='{vastag}' stroke-linecap='round' stroke-linejoin='round' {extra}>{el}</g>")
        else:
            out.append(f"<g fill='{fm[szerep]}' stroke='none' {extra}>{el}</g>")
    return "".join(out)


def svg(belso, defs=""):
    return f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='-6 -6 112 112' width='256' height='256'><defs>{defs}</defs>{belso}</svg>"


def st_i1(ik):  # lapos, kétszínű
    return svg(telt_elemek(ik))


def st_i2(ik):  # vonalas + elcsúszott színfolt
    blob = f"<circle cx='58' cy='58' r='30' fill='{A}' opacity='.55'/>"
    return svg(blob + f"<g fill='none' stroke='{P}' color='{P}' stroke-width='4.2' stroke-linecap='round' stroke-linejoin='round'>{IKONOK[ik]['vonal']}</g>")


def st_i3(ik):  # kézzel rajzolt: remegő vonal + mellécsúszó lavírozás
    defs = ("<filter id='w'><feTurbulence type='fractalNoise' baseFrequency='.035' numOctaves='2' seed='4'/>"
            "<feDisplacementMap in='SourceGraphic' scale='3.2'/></filter>")
    wash = f"<g transform='translate(4 3)' opacity='.6' filter='url(#w)'>{telt_elemek(ik, 10, {'p': A, 'a': LIGHT, 'd': A, 'l': LIGHT})}</g>"
    line = f"<g filter='url(#w)' fill='none' stroke='{A2}' color='{A2}' stroke-width='3.6' stroke-linecap='round' stroke-linejoin='round'>{IKONOK[ik]['vonal']}</g>"
    return svg(wash + line, defs)


def st_i5(ik):  # puha 3D: belső fény + árnyék
    defs = ("<filter id='s' x='-30%' y='-30%' width='160%' height='170%'>"
            "<feGaussianBlur in='SourceAlpha' stdDeviation='2.2' result='b'/><feOffset in='b' dx='-1.5' dy='-1.5' result='o'/>"
            "<feComposite in='SourceAlpha' in2='o' operator='out' result='hl'/><feFlood flood-color='#fff' flood-opacity='.55'/>"
            "<feComposite in2='hl' operator='in' result='fenyes'/>"
            "<feGaussianBlur in='SourceAlpha' stdDeviation='2.6' result='b2'/><feOffset in='b2' dx='2' dy='2.5' result='o2'/>"
            "<feComposite in='SourceAlpha' in2='o2' operator='out' result='sh'/><feFlood flood-color='#3a1a05' flood-opacity='.35'/>"
            "<feComposite in2='sh' operator='in' result='sotet'/>"
            "<feGaussianBlur in='SourceAlpha' stdDeviation='3' result='db'/><feOffset in='db' dy='4' result='do'/>"
            "<feFlood flood-color='#3a1a05' flood-opacity='.28'/><feComposite in2='do' operator='in' result='drop'/>"
            "<feMerge><feMergeNode in='drop'/><feMergeNode in='SourceGraphic'/><feMergeNode in='fenyes'/><feMergeNode in='sotet'/></feMerge></filter>")
    return svg(f"<g filter='url(#s)'>{telt_elemek(ik, 11, {'p': P, 'a': A, 'd': A2, 'l': '#F3C9A2'})}</g>", defs)


def st_i6(ik):  # retró risograph: két tinta, elcsúszva, szemcsével
    defs = ("<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='1' seed='2' result='n'/>"
            "<feColorMatrix in='n' type='matrix' values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.4 1.25' result='m'/>"
            "<feComposite in='SourceGraphic' in2='m' operator='in'/></filter>")
    a = f"<g filter='url(#g)' style='mix-blend-mode:multiply'>{telt_elemek(ik, 9, {'p': P, 'a': P, 'd': P, 'l': '#F2B98C'})}</g>"
    b = (f"<g transform='translate(2.2 1.6)' filter='url(#g)' style='mix-blend-mode:multiply' fill='none' stroke='{A2}' "
         f"stroke-width='3' stroke-linecap='round' stroke-linejoin='round' color='{A2}'>{IKONOK[ik]['vonal']}</g>")
    return svg(a + b, defs)


STILUSOK = {"i1": st_i1, "i2": st_i2, "i3": st_i3, "i5": st_i5, "i6": st_i6}


def render():
    nevek = list(IKONOK)
    tmp = Path(tempfile.mkdtemp(prefix="ikr"))
    for sid, fn in STILUSOK.items():
        cellak = "".join(f"<div style='width:256px;height:256px'>{fn(n)}</div>" for n in nevek)
        html = ("<!doctype html><html><head><style>html,body{margin:0;background:transparent}svg{display:block}"
                f"body{{display:flex;width:{256 * len(nevek)}px}}</style></head><body>{cellak}</body></html>")
        f = tmp / f"{sid}.html"
        f.write_text(html, encoding="utf-8")
        png = tmp / f"{sid}.png"
        prof = tempfile.mkdtemp(prefix="ikp")
        subprocess.run([CHROME, "--no-sandbox", "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--default-background-color=00000000", f"--user-data-dir={prof}",
                        f"--window-size={256 * len(nevek)},420", f"--screenshot={png}", f.as_uri()],
                       capture_output=True, timeout=90)
        shutil.rmtree(prof, ignore_errors=True)
        im = Image.open(png).convert("RGBA")
        cel = MUNKA / SPEC.get("mappa", "ikonok") / sid
        cel.mkdir(parents=True, exist_ok=True)
        for i, n in enumerate(nevek):
            im.crop((i * 256, 0, (i + 1) * 256, 256)).save(cel / f"{n}.png", optimize=True)
        print(sid, "kész:", len(nevek), "ikon")
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    render()
