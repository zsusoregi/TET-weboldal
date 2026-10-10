# Tantraszex Edzésterv · designrendszer

Készült: 2026-10-10 · forrás: https://tet.tantraiskola.com · az arculat-választó v2 döntései alapján.

Ez a dokumentum a márka webes arculatának összefoglalója: bármely AI vagy fejlesztő ebből tud új oldalt,
aloldalt vagy anyagot készíteni, ami ugyanúgy néz ki. A pontos értékek a `tokenek.css`-ben vannak.

## 1. Színek

Paletta: **P3 „Égetett narancs és zsálya”**. A márka eredeti színei: égetett narancs (#B54E02), meleg tört fehér háttér (#FFFBF4) és sötétszürke szöveg (#4C4C4C), mellé egy nyugodt zsályazöld kísérőszín. Modern wellness-hangulat, kevésbé „ezoterikus”: a szkeptikusabb 45+ férfinak is komolyan vehető.

| Szerep | Token | Érték |
|---|---|---|
| Fő márkaszín (gombok, kiemelés) | `--c-primary` | `#B54E02` |
| Fő szín, sötét (hover, talp) | `--c-primary-d` | `#913e02` |
| Kiemelő szín (marker, pöttyök, matricák) | `--c-accent` | `#8A9A78` |
| Harmadik szín (apró díszek) | `--c-accent2` | `#3E4A3A` |
| Oldal alapháttér | `--c-paper` | `#FFFBF4` |
| Kártya / tiszta blokk | `--c-card` | `#ffffff` |
| Halvány márkaszínű felület | `--c-tint` | `#f8eadc` |
| Meleg, mélyebb felület | `--c-sand` | `#f8f3ea` |
| Sötét felület (lábléc, tábla) | `--c-deep` | `#2A2E26` |
| Szöveg | `--c-ink` | `#4C4C4C` |
| Másodlagos szöveg | `--c-ink-2` | `#7e7d7b` |
| Hajszálvonal | `--c-line` | `#e8e4de` |

Szabály: a sötét felület a márkaszín felé húzott mély tónus, nem tiszta fekete. Két egymás melletti szekció
soha nem ugyanolyan felületű (paper → white → tint → sand → deep ritmus).

## 2. Tipográfia

Betűpár: **B2 „Outfit + Figtree (modern)”**. Geometrikus, barátságos grotesk: wellness- és app-érzet, semmi „ezo”. Rendezett, mai, és a program gyakorlati, edzésszerű oldalát erősíti.

- Cím: **Outfit** (600, sorköz 1.06, betűköz -0.025em)
- Szöveg: **Figtree**
- Kézírás-akcent: **Shadows Into Light** (jegyzetek, aláírás, kiemelt szó)
- Címke / adat: **Red Hat Mono** (mono: idő, ár, apró címkék)
- Méretek: hero `clamp(2.35rem, 5.5cqi, 4.85rem)`, H2 `clamp(1.8rem, 3.5cqi, 3.05rem)`, H3 `clamp(1.1rem, 1.55cqi, 1.34rem)`, törzs 1.02rem / 1.62.
- Google Fonts, mind ellenőrizve magyar ékezetre (ő, ű).

## 3. Komponensek (a választott változatok)

- **Címsorok:** CM „Energia-vonal”. Vékony, narancsból borostyánba futó vonal a szó alatt, görgetésre végigfut, mint az energia. Modern.
- **Alcímek (felső címkék):** KE „Hajszálvonal jantra-jellel”. Rendezett, elegáns felvezetés, a közepén apró jantra-jel: minden szekció elején csendben ott a márka szimbóluma.
- **Gombok:** GB „Lángoló kapszula”. Értékesítési oldalon a gomb a legfontosabb elem. A lángoló narancs kapszula a sötét és a világos szekciókon is azonnal látszik, és rámutatva „felizzik”: kattintásra hív.
- **Kártyák:** RM „Energia-sáv”. Tiszta kártya, tetején narancsból borostyánba futó vékony sáv, rámutatva megemelkedik. Modern, rendezett.
- **Fotókezelés:** FE „Gyertyafény-derengés”. A fotóitok sötét, meleg tónusúak. A narancs derengés a kép mögött úgy hat, mintha gyertya világítaná: intim, de nem kihívó.
- **Ikonstílus:** I2 „Az eredeti, vékonyabb vonallal”. Ugyanaz az eredeti rajzstílus, csak finomabb vonallal: elegánsabb, levegősebb.
- **Háttér-textúra:** TR „Srí Jantra a sarokban”. Egyetlen nagy mandala a sarokban: elegáns, és nem ismétlődik.
- **Dekor-réteg:** D0 „Letisztult (nincs dekor)”. Nincs dekor: ha a háttér-textúra és a fotók elegendőek.
- **Szekcióhatárok:** SK2 „Lótuszszirom középen, alacsonyabb”. Ugyanaz a szirom, 20%-kal alacsonyabban.
- **Mozgás:** ME „Lassú kilégzés”. Lassú, nyugodt beúszás, mint egy hosszú kilégzés. A 45+ közönségnek ez kellemes, nem kapkodó, és a téma tempójához illik.

## 4. Az oldal szerkezete

1. **Navigáció (fejléc):** NX2 „Landing: csak logó és egy gomb”. Értékesítési oldalon a menü elviszi a figyelmet. Itt csak a logó, a program neve és egy finom „Csomagok” gomb van: a látogató végiggörget, és nem téved el.
1. **Hero (nyitó blokk):** H3 „Teljes képes, kártyával”. A teljes képernyős fotón egy kisebb kártya csak a címmel és a terméknévvel, így a férfiból több látszik; a többi szöveg és a gombok alatta, külön sávban.
1. **Miről szól?:** RX2 „Idővonal három állomással”. Vízszintes idővonal: 15+, 25+, 45 felett, az utolsó pont izzik. Alatta két hasábban a „Talán…” mondatok. Tiszta, mesélős.
1. **Miért pont tantra?:** MX4 „Sötét kiáltvány”. Ez az oldal szíve: a „nem technikával kezdődik, hanem figyelemmel” mondat óriási betűkkel, sötétben. Megállítja a görgetést.
1. **Mi a Tantraszex Edzésterv?:** MI5 „Kavicsok fotóval”. A sorba rendezett kavicsok fotója (lépésről lépésre) mellett a szöveg, alul kiemelve a cél. Nyugodt, képszerű.
1. **Folyamat (így működik):** F1 „Pontozott útvonal”. Lépés-kártyák egy pontozott útvonalon: egyértelmű, „ilyen egyszerű”.
1. **Rólunk / történet:** T5 „Levélpapír”. Levélpapír, felragasztott fotóval: nagyon személyes.
1. **Tények / bizalom:** P4 „Sötét, kulcsszavas”. Sötét háttér, nagy kulcsszavak: erős, férfias hangulat.
1. **Kinek szól?:** KX1 „Igen / nem két hasáb”. Igen és nem egymás mellett: a 45+ férfi egy pillantással eldönti, róla szól-e. Az őszinte „kinek nem” növeli a bizalmat.
1. **Vélemények:** VX2 „Egy nagy és három kisebb”. Az első beszámoló kiemelve, óriás idézőjellel; a többi három mellette kisebb kártyákon. Erős első benyomás.
1. **Kínálat:** K2 „Fotós csempék”. A három bónusz a saját borítóképével: rögtön látszik, hogy kézzelfogható anyagokról van szó.
1. **Garanciák:** GX1 „Két pecsét”. Két nagy, kerek pecsét (24 óra, 13. hét), alattuk a garancia szövege. Mint két hivatalos ígéret. Megnyugtató, kézzelfogható.
1. **Kapcsolat / látogatás:** LX1 „Homokóra”. A „12 hét múlva mindenképpen 12 héttel idősebb leszel” mondat mellett egy lassan peregő homokóra (a ti saját ikonotok). Az idő múlása szó szerint látszik.
1. **Kiemelt tételek árakkal:** AX2 „A Prémium sötétben”. A Prémium csomag sötét, gyertyafényes kártyán áll az alap mellett: a drágább ajánlat magától kiemelkedik, és a „prémium” szó tényleg látszik.
1. **GYIK:** QX1 „Lenyíló lista”. Lenyíló lista: hat kérdés kevés helyen, a válaszok csak akkor jelennek meg, ha kell.
1. **Lábléc:** LBX „Sötét, jantra-jellel”. Sötét, csendes lezárás a fehér logóval egy halvány jantra előtt, egy mondattal („Adj a testednek 12 hetet.”) és egy utolsó gombbal.

## 5. A márka saját világa (motívumok)

Jantra (két egymásba fordított háromszög körben), lótusz, láng (szexuális energia), homokóra (a 12 hét, „12 hét múlva mindenképpen 12 héttel idősebb leszel”), lélegzet-hullám, az izgalom hullámzó görbéje.

- Motívum-formák: jantra, lotusz, lang, homokora (maszk-SVG-k az arculat.json-ban, a textúra és a dekor ezekből épül).
- Szellemszavak: JELENLÉT, 45+, FIGYELEM, 12 HÉT, KIRANA, ERŐ, NEKED, ÉLMÉNY, AJÁNDÉK, GARANCIA, MOST, EDZÉS, KÉRDÉS, LÉGZÉS, 12 × 12
- Futószalag-tények: 12 hét · 12 gyakorlat · Online, a saját tempódban · 45+ férfiaknak · „Első randi” garancia · „Izomláz” garancia · 39.000 Ft értékű ajándék
- Matricák: 12 hét · 12 gyakorlat · 45+ férfiaknak · Saját tempóban · Két garancia

## 6. Szabályok

- A tények (árak, nevek, nyitvatartás, számok) csak az ügyfél saját forrásából jöhetnek, betűre.
- Ikon + cím egy sorban a kártyafejekben; ikon soha nem kap szöveget.
- Fotók: `aspect-ratio` + `object-fit: cover` (háttérképként), soha nem fix magasság; valódi fotó, nem kivágott.
- Gombok: egy szekcióban legfeljebb egy elsődleges gomb.
- Mozgás: `prefers-reduced-motion` esetén minden áll; `?mozdulatlan=1` a képernyőképekhez.
- Tilos: lila-kék AI-gradiens, emoji a saját szövegben, hosszú gondolatjel a saját szövegben, kitalált vélemény.

## 7. Az ügyfél megjegyzései a választáskor

- Háttér-textúra / TR: a minta színe legyen csak nagyon-nagyon kicsit erősebb árnyalat, mint a háttér Éppen, hogy csak látszódjon
- Hero (nyitó blokk) / H3: a külön sáv háttérszíne legyen a sötétzöld a színpalettáról. ehhez igazítsd a betűszíneket, hogy látszódjanak
- Miről szól? / RX2: a háttérszín legyen a #FFFBF4
- Folyamat (így működik) / F1: a háttérszín legyen a #FFFBF4
- Kinek szól? / KX1: a háttérszín legyen a #FFFBF4
- Kínálat / K2: a háttérszín legyen a #FFFBF4
- GYIK / QX1: a háttérszín legyen a #FFFBF4

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
