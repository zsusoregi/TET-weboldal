# -*- coding: utf-8 -*-
"""A végleges oldal (tantraszexedzesterv.com) feltöltésre kész mappája (kesz/): index.html + og.jpg.
Hozzáadja a böngészőfül-ikont (logóból), a megosztási képet (og:image) és a kanonikus URL-t.
Futtatás a munkamappából, az epit.py oldal + utofeldolgozas.py után: python3 gen/vegleges.py"""
import base64, io
from pathlib import Path
from PIL import Image

MUNKA = Path(__file__).resolve().parent.parent
URL = "https://tantraszexedzesterv.com/"
KI = MUNKA / "kesz"

DONTESEK = """

## 8. Végleges döntések (a választó utáni egyeztetésből; felülírják a 7. pontot)

### Világos blokkok háttere és textúrája
Krém = `#FFFBF4` (`--c-paper`), homok = `#F8F3EA` (`--c-sand`); 0 = nincs, 1 = van Srí Jantra textúra.
A sötét blokkok (`#2A2E26`) háttere változatlan.

| # | Blokk (id) | Háttér | Textúra |
|---|---|---|---|
| 15 | Miről szól (`rolaszol`) | krém | 0 |
| 17 | Mi a Tantraszex Edzésterv (`mia`) | krém | 1 |
| 18 | Mit edzünk 12 héten át (`folyamat`) | homok | 0 |
| 19 | A megalkotójáról (`rolunk`) | krém | 1 |
| 21 | Kinek szól (`kinek`) | homok | 1 |
| 22 | Vélemények (`velemenyek`) | krém | 0 |
| 23 | Ajándékok (`kinalat`) | homok | 0 |
| 24 | Garanciák (`garancia`) | krém | 1 |
| 26 | Csomagok (`etlap`) | homok | 1 |
| 27 | GYIK (`gyik`) | krém | 1 |

### Srí Jantra
- A háttér-textúra és a lábléc grafikája egy vonalas Srí Jantra, az ügyfél képéről lemért arányokkal:
  4 felfelé és 5 lefelé álló háromszög, kör, 8 csúcsos lótuszszirom, szaggatott középvonal, bindu.
  Forrás: `gen/stilus_gen.py` → `sri_belso()`.
- Színe a márkaszín (sötét blokkon a zsálya kiemelő), átlátszósága 5% (sötéten 6%): éppen csak látszik.
- A szekció sarkában áll, váltakozva jobbra fent és balra lent.

### Egyedi elemek
- Hero: fotó, rajta `#FFFBF4` szövegkártya; alatta sötétzöld sáv az alcímmel és a gombokkal.
- Szekcióhatár: lótuszszirom középen, 25 px magas (`sK2`).
- Mi a Tantraszex Edzésterv: kép és szöveg 50–50%.
- Ajándékok: borítókép, cím, leírás; címke nincs a kártyákon.
- Csomagok: két külön kártya (0,9 : 1,1), az alapcsomag alatt narancs derengés (mint a fotók alatt),
  a Prémium sötét kártyán; a „Mit tartalmaz a prémium csomag?” felugró ablakot nyit.
- Homokóra (záró blokk): a homok az üveg formájára vágva, 80% átlátszatlanság, a grafika egésze 80%.
- Lábléc: Impresszum felugró ablak, ÁSZF és Adatkezelési tájékoztató link.
"""


def png_uri(im, meret):
    lap = Image.new("RGBA", (meret, meret), (0, 0, 0, 0))
    k = im.copy()
    k.thumbnail((meret, meret), Image.LANCZOS)
    lap.paste(k, ((meret - k.width) // 2, (meret - k.height) // 2), k)
    b = io.BytesIO()
    lap.save(b, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()


def main():
    KI.mkdir(exist_ok=True)
    # megosztási kép 1200×630: a hero fotó felső része (arc és kezek)
    foto = Image.open(MUNKA / "kepek" / "sziv-sotet.jpg").convert("RGB")
    foto.crop((0, 40, 1097, 616)).resize((1200, 630), Image.LANCZOS).save(KI / "og.jpg", quality=86, optimize=True)

    logo = Image.open(MUNKA / "kepek" / "logo.png").convert("RGBA")
    fej = (f'<link rel="icon" type="image/png" href="{png_uri(logo, 64)}">'
           f'<link rel="apple-touch-icon" href="{png_uri(logo, 180)}">'
           f'<meta property="og:url" content="{URL}">'
           f'<meta property="og:image" content="{URL}og.jpg">'
           '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
           '<meta property="og:locale" content="hu_HU">'
           '<meta name="twitter:card" content="summary_large_image">')
    s = (MUNKA / "fooldal.html").read_text(encoding="utf-8")
    assert "og:image" not in s, "a fooldal.html már tartalmaz og:image-et"
    s = s.replace("</head>", fej + "</head>", 1)
    (KI / "index.html").write_text(s, encoding="utf-8")
    md = MUNKA / "DESIGN-RENDSZER.md"
    m = md.read_text(encoding="utf-8")
    if "## 8. Végleges döntések" not in m:
        md.write_text(m.rstrip() + DONTESEK, encoding="utf-8")
    print("kész:", KI / "index.html", f"({len(s.encode()) // 1024} KB)", "+ og.jpg")


if __name__ == "__main__":
    main()
