# -*- coding: utf-8 -*-
"""Ikonok a tet.tantraiskola.com eredeti stílusában: egyszínű, vastag, lekerekített végű narancs vonalrajz,
kitöltés nélkül. A választó szabványa miatt 5 változat, de mind ugyanebből a családból (i1 = pontosan az eredeti).
Futtatás a munkamappából: python3 gen/ikon_eredeti.py"""
import json, subprocess, tempfile, shutil
from pathlib import Path
from PIL import Image

MUNKA = Path(__file__).resolve().parent.parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
EREDETI = "#B3591B"      # az eredeti ikonok színe (pixelre mérve)
SOTET = "#5A2E14"

# 100×100-as vászon, csak körvonalak (a stroke a stílusból jön)
IKONOK = {
    "figyelem": "<path d='M10 60Q50 22 90 60Q50 98 10 60Z'/><circle cx='50' cy='60' r='13'/>"
                "<path d='M50 10V20M20 22L27 29M80 22L73 29'/>",
    "homokora": "<rect x='22' y='8' width='56' height='9' rx='2'/><rect x='22' y='83' width='56' height='9' rx='2'/>"
                "<path d='M28 17C28 36 44 42 44 50S28 64 28 83M72 17C72 36 56 42 56 50S72 64 72 83'/>"
                "<path d='M38 30H62C59 37 53 41 50 43 47 41 41 37 38 30Z'/><path d='M37 76C40 68 46 64 50 62 54 64 60 68 63 76Z'/>",
    "legzes": "<path d='M10 32C26 20 40 44 56 32S80 22 90 28'/><path d='M10 52C26 40 40 64 56 52S80 42 90 48'/>"
              "<path d='M10 72C26 60 40 84 56 72S80 62 90 68'/>",
    "erintes": "<path d='M38 94L34 66V38A5 5 0 0 1 44 38V30A5 5 0 0 1 54 30V33A5 5 0 0 1 64 33V43A4 4 0 0 1 72 43V70C72 84 64 94 54 94Z'/>"
               "<path d='M44 38V56M54 33V56M64 43V58'/><path d='M34 70L24 58A5 5 0 0 0 16 64L30 84'/>"
               "<path d='M78 20Q86 25 86 34M82 8Q96 17 96 34'/>",
    "izgalom": "<path d='M50 6C58 26 78 38 78 62A28 28 0 0 1 22 62C22 46 32 38 37 25 41 37 45 42 50 44 55 33 55 20 50 6Z'/>"
               "<path d='M50 54C55 61 61 65 61 72A11 11 0 0 1 39 72C39 65 45 61 50 54Z'/>",
    "szabalyozas": "<circle cx='50' cy='50' r='40'/><path d='M24 52C32 36 41 36 50 50S68 64 76 48'/>",
}


def svg(belso):
    return f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 108 108' width='256' height='256'>{belso}</svg>"


def vonal(ik, szin=EREDETI, w=5.4, extra=""):
    return (f"<g fill='none' stroke='{szin}' stroke-width='{w}' stroke-linecap='round' stroke-linejoin='round' {extra}>"
            f"{IKONOK[ik]}</g>")


STILUSOK = {
    "i1": dict(nev="Az eredeti: vastag narancs vonal", miert="Pontosan a mostani tet.tantraiskola.com ikonjainak stílusa: "
               "vastag, lekerekített végű narancs vonalrajz, kitöltés nélkül.", fn=lambda ik: svg(vonal(ik))),
    "i2": dict(nev="Az eredeti, vékonyabb vonallal", miert="Ugyanaz az eredeti rajzstílus, csak finomabb vonallal: "
               "elegánsabb, levegősebb.", fn=lambda ik: svg(vonal(ik, w=3.6))),
    "i3": dict(nev="Az eredeti, körben", miert="Az eredeti vonalas ikon egy vékony körben, ahogy az eredeti oldalon a "
               "számozott (1-5) ikonok is állnak.",
               fn=lambda ik: svg(f"<circle cx='50' cy='50' r='47' fill='none' stroke='{EREDETI}' stroke-width='4.5'/>"
                                 + vonal(ik, w=8.5, extra="transform='translate(21 21) scale(.58)'"))),
    "i4": dict(nev="Az eredeti, narancs korongon", miert="Az eredeti vonalrajz fehérrel, telt narancs korongon: ugyanaz a "
               "rajz, de erősebben kiemelkedik a háttérből.",
               fn=lambda ik: svg(f"<circle cx='50' cy='50' r='50' fill='{EREDETI}'/>"
                                 + vonal(ik, szin="#FFFFFF", w=8.5, extra="transform='translate(21 21) scale(.58)'"))),
    "i5": dict(nev="Az eredeti, sötétbarnában", miert="Az eredeti rajz és vonalvastagság, mélybarna színben: "
               "visszafogottabb, a narancs csak a gombokon és kiemeléseken marad.", fn=lambda ik: svg(vonal(ik, szin=SOTET))),
}

# 2. kör: az ügyfél új ikonopciókat kért; a választott i2 marad, mellé 4 új, ugyanabból a családból
ZSALYA = "#7E8F6C"
HALVANY = "#F6E1CF"
STILUSOK.update({
    "i6": dict(nev="Az eredeti, közepes vonallal", miert="Az eredeti rajz a vastag és a vékony között: jól látszik kis méretben is, "
               "mégis könnyed.", fn=lambda ik: svg(vonal(ik, w=4.6))),
    "i7": dict(nev="Az eredeti, lekerekített négyzetben", miert="Vékony vonalú ikon egy finom, lekerekített négyzet keretben: "
               "rendezett, mint egy alkalmazás ikonja.",
               fn=lambda ik: svg(f"<rect x='3' y='3' width='94' height='94' rx='24' fill='none' stroke='{EREDETI}' stroke-width='3.2'/>"
                                 + vonal(ik, w=6.4, extra="transform='translate(21 21) scale(.58)'"))),
    "i8": dict(nev="Az eredeti, halvány korongon", miert="Vékony narancs vonalrajz halvány barack korongon: lágyabb, melegebb, "
               "a narancs nem tolakodó.",
               fn=lambda ik: svg(f"<circle cx='50' cy='50' r='50' fill='{HALVANY}'/>" + vonal(ik, w=6.4, extra="transform='translate(19 19) scale(.62)'"))),
    "i9": dict(nev="Az eredeti, zsályazöldben", miert="Az eredeti vékony rajz a választott paletta zsályazöld kísérőszínében: "
               "a narancs így a gombokra és a kiemelésekre marad.", fn=lambda ik: svg(vonal(ik, szin=ZSALYA, w=3.6))),
})
VALASZTO = ["i2", "i6", "i7", "i8", "i9"]


def render():
    nevek = list(IKONOK)
    mappa = MUNKA / "ikonok"
    shutil.rmtree(mappa, ignore_errors=True)
    tmp = Path(tempfile.mkdtemp(prefix="ike"))
    for sid, st in STILUSOK.items():
        cellak = "".join(f"<div style='width:256px;height:256px'>{st['fn'](n)}</div>" for n in nevek)
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
        (mappa / sid).mkdir(parents=True, exist_ok=True)
        for i, n in enumerate(nevek):
            im.crop((i * 256, 0, (i + 1) * 256, 256)).save(mappa / sid / f"{n}.png", optimize=True)
    shutil.rmtree(tmp, ignore_errors=True)
    # az ikon-spec stílusai (a választó ezekből veszi a nevet és az indoklást)
    sp = MUNKA / "ikon-spec.json"
    spec = json.loads(sp.read_text(encoding="utf-8"))
    spec["stilusok"] = [{"id": k, "nev": STILUSOK[k]["nev"], "miert": STILUSOK[k]["miert"],
                         "elotag": "(kézzel rajzolt, az eredeti oldal ikonstílusában)"} for k in VALASZTO]
    sp.write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    print("kész:", len(STILUSOK), "stílus ×", len(nevek), "ikon")


if __name__ == "__main__":
    render()
