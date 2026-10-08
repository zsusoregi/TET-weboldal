# -*- coding: utf-8 -*-
"""Összerakja az arculat.json-t (futtatás: python3 gen/build.py, a munkamappából)."""
import json, sys, copy
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import alap_gen as A
import stilus_gen as S
import szekcio_gen as Z
from motor import epito

MUNKA = HERE.parent

spec = copy.deepcopy(A.TARTALOM)
spec.update({"verzio": 1, "ikonok": {"spec": "ikon-spec.json"}})
spec["opciok"] = {}
spec["egyedi_szekciok"] = {
    "rolaszol": {"nev": "Miről szól?", "leiras": "A program lényege: 15+, 25+, 45 felett, és a „Talán…” helyzetek."},
    "miert": {"nev": "Miért pont tantra?", "leiras": "A cél-gondolkodás és a tantra szembeállítása."},
    "mia": {"nev": "Mi a Tantraszex Edzésterv?", "leiras": "A program lényege: 12 gyakorlat, 12 hét, és ami nem."},
    "kinek": {"nev": "Kinek szól?", "leiras": "Kinek szól a program, és kinek nem."},
    "velemenyek": {"nev": "Vélemények", "leiras": "Mások így élték meg: a résztvevők beszámolói."},
    "garancia": {"nev": "Garanciák", "leiras": "„Első randi” és „Izomláz” garancia."},
    "gyik": {"nev": "GYIK", "leiras": "Gyakran Intézett Kérdések."},
}
spec["szekcio_sorrend"] = ["nav", "hero", "rolaszol", "miert", "mia", "folyamat", "tortenet", "tenyek", "kinek", "velemenyek",
                           "kinalat", "garancia", "latogatas", "ajanlat", "gyik", "lablec"]

# a motor ctx-e (logó-infóval), hogy az egyedi HTML ugyanazokból az építőelemekből készüljön
spec["_alap"] = MUNKA
logo_info, _ = epito.logo_elokeszit(spec)
ctx = epito.ctx_keszit(spec, logo_info)
szek = Z.mind(ctx)
del spec["_alap"]

eo = {}
for kat, lst in [("cim", S.CIM), ("alcim", S.ALCIM), ("gomb", S.GOMB), ("kartya", S.KARTYA), ("foto", S.FOTO),
                 ("felulet", S.FELULET), ("dekor", S.DEKOR), ("hatar", S.HATAR), ("mozgas", S.MOZGAS)]:
    eo[kat] = lst
for kat, lst in szek.items():
    eo[kat] = lst
spec["egyedi_opciok"] = eo

O = spec["opciok"]
O["paletta"] = {"ajanlott": "p1", "lista": A.PALETTAK}
O["betu"] = {"ajanlott": "b1", "lista": A.BETUK}
O["ikon"] = {"ajanlott": "i1"}


def kat(nev, ids, aj, miert=None):
    O[nev] = {"lista": ids, "ajanlott": aj}
    if miert:
        O[nev]["miert"] = miert


kat("cim", ["cE", "cM", "cB", "cF", "cK"], "cE", {"cE": "A dőlt, vékony kiemelés suttog, nem kiabál: illik a tantra intimitásához és a meghitt fotókhoz. A cím súlya megmarad, a kulcsszó finoman kiválik."})
kat("alcim", ["kE", "kM", "kB", "kF", "kK"], "kE", {"kE": "Rendezett, elegáns felvezetés, a közepén apró jantra-jel: minden szekció elején csendben ott a márka szimbóluma."})
kat("gomb", ["gE", "gM", "gB", "gF", "gK"], "gB", {"gB": "Értékesítési oldalon a gomb a legfontosabb elem. A lángoló narancs kapszula a sötét és a világos szekciókon is azonnal látszik, és rámutatva „felizzik”: kattintásra hív."})
kat("kartya", ["rE", "rM", "rB", "rF", "rK"], "rE", {"rE": "Fehér lap vékony belső kerettel és halvány jantrával a sarokban: nyugodt, prémium, a sok szöveget is rendben tartja."})
kat("foto", ["fE", "fM", "fB", "fF", "fK"], "fE", {"fE": "A fotóitok sötét, meleg tónusúak. A narancs derengés a kép mögött úgy hat, mintha gyertya világítaná: intim, de nem kihívó."})
kat("felulet", ["tJ", "tL", "tN", "tK", "tO"], "tJ", {"tJ": "A jantra a tantra legismertebb jele (a fotóitokon is ott van). Szinte észrevétlen ismétlődő mintaként mélységet ad, és csak ennél a márkánál van értelme."})
kat("dekor", ["dJ", "dL", "dP", "dS", "dH"], "dL", {"dL": "A légzés a program egyik alapja. A sarokban lassan táguló-szűkülő fénykör szó nélkül mondja: lassíts, lélegezz. Nyugodt, és mégis él az oldal."})
kat("hatar", ["sL", "sI", "sO", "sT", "sM"], "sL", {"sL": "Két lágy hullám, mint egy mély be- és kilégzés. A szekciók folyékonyan érnek egymásba, ami illik a „nem a csúcsra rohanunk” üzenethez."})
kat("mozgas", ["mE", "mM", "mB", "mF", "mK"], "mE", {"mE": "Lassú, nyugodt beúszás, mint egy hosszú kilégzés. A 45+ közönségnek ez kellemes, nem kapkodó, és a téma tempójához illik."})

kat("nav", ["nx2", "nx1", "n1", "n3", "n6"], "nx2", {
    "nx2": "Értékesítési oldalon a menü elviszi a figyelmet. Itt csak a logó, a program neve és egy finom „Csomagok” gomb van: a látogató végiggörget, és nem téved el.",
    "nx1": "A sötét nyitóképre simul rá, a fehér logóval. Prémium, ha a sötét hero-t választjátok.",
    "n1": "Lebegő, görgetéskor is látható menü: ha az oldalt hosszabb tájékozódásra is használjátok.",
    "n3": "Középre zárt logó, a menü két oldalt: klasszikus, rendezett.",
    "n6": "Kétszintes fejléc nagy logóval: ünnepélyes, kicsit magazinos."})
kat("hero", ["hx1", "h5", "h3", "h4", "h6"], "hx1", {
    "hx1": "A legerősebb fotótok (a fekete háttér előtt meditáló férfi) úgy emelkedik ki a sötétből, mintha gyertyafény világítaná meg. Rögtön látszik: felnőtt, intim, komoly program. A cím a ti mondatotok: „12 hét, 12 gyakorlat. Egy új szint a szexualitásodban.”",
    "h5": "Kettéosztott kép a jantrás fotóval: letisztult, világos, magazinos. Kevésbé drámai, barátságosabb belépő.",
    "h3": "A teljes képernyős fotón egy világos kártya a címmel: hangulatos, „itt vagy” érzés.",
    "h4": "Óriás, plakátszerű cím, alatta fotósor: a legmerészebb, edzésterv-hangulat.",
    "h6": "Középre zárt cím, körülötte négy lebegő fotó: nyitott, könnyed."})
kat("rolaszol", ["rx1", "rx2", "rx3", "rx4", "rx5"], "rx1", {"rx1": "A 15+ → 25+ → 45 felett lépcső szó szerint megmutatja, hogy a legmagasabb fok most jön. Erős, egyszerű kép a fő gondolatra."})
kat("miert", ["mx1", "mx2", "mx3", "mx4", "mx5"], "mx4", {"mx4": "Ez az oldal szíve: a „nem technikával kezdődik, hanem figyelemmel” mondat óriási betűkkel, sötétben. Megállítja a görgetést."})
kat("folyamat", ["f2", "f1", "f3", "f4", "f5"], "f2", {
    "f2": "Az öt képesség egy függőleges idővonalon, felváltva balra-jobbra: úgy olvasható, mint egy 12 hetes út állomásai.",
    "f1": "Lépés-kártyák egy pontozott útvonalon: egyértelmű, „ilyen egyszerű”.",
    "f3": "Óriás sorszámok: szerkesztőségi, sok levegővel.",
    "f4": "Felfelé lépcső: a fejlődés érzete, hétről hétre.",
    "f5": "Futószalag állomásokkal: játékosabb, gyakorlatias."})
kat("tortenet", ["t1", "t4", "t2", "t3", "t5"], "t1", {
    "t1": "Kirana portréja, mellette a története, kiemelve a mondata („A Tantra nem csupán hivatás számomra, hanem az életem.”) és kézírásos aláírás. Személyes, bizalmat épít: ez kell egy ilyen kényes témánál.",
    "t4": "Nagy idézet kerek portréval: erős, emberi.", "t2": "Szórt fotókollázs: emlékalbumos, meleg.",
    "t3": "Mérföldkövek (évtized, ISTA, saját út): tárgyilagos, hiteles.", "t5": "Levélpapír, felragasztott fotóval: nagyon személyes."})
kat("tenyek", ["p1", "p3", "p5", "p4", "p6"], "p1", {
    "p1": "Hat kártya hármasával, mind a hat előny teljes szöveggel, balra zárva. Gyorsan átfutható, és a kártyastílus az egész oldalon egységes.",
    "p3": "Teljes szélességű, váltakozó hátterű sávok: a hosszabb szövegek itt olvashatók a legkényelmesebben.",
    "p5": "Számozott, kártya nélküli lista két hasábban: szerkesztőségi, levegős.",
    "p4": "Sötét háttér, nagy kulcsszavak: erős, férfias hangulat.",
    "p6": "Oldalcím és egymás alatti ikonos lista: rendezett, mint egy jól szerkesztett cikk."})
kat("kinek", ["kx1", "kx2", "kx3", "kx4", "kx5"], "kx1", {"kx1": "Igen és nem egymás mellett: a 45+ férfi egy pillantással eldönti, róla szól-e. Az őszinte „kinek nem” növeli a bizalmat."})
kat("velemenyek", ["vx3", "vx1", "vx2", "vx4", "vx5"], "vx3", {"vx3": "Ezek a beszámolók intimek. A sötét, gyertyafényes háttér előtt úgy olvashatók, mint egy esti, bizalmas beszélgetés, a kiemelt mondatok meleg fényben."})
kat("kinalat", ["k2", "k5", "k3", "k1", "k6"], "k2", {
    "k2": "A három bónusz a saját borítóképével: rögtön látszik, hogy kézzelfogható anyagokról van szó.",
    "k5": "Váltakozó sorok nagy képpel: mesélős, prémium.", "k3": "Bento-rács: modern, kiemeli az első bónuszt.",
    "k1": "Ikonos kártyák kép nélkül: tiszta, rövid.", "k6": "Fülek: kevés helyen."})
kat("garancia", ["gx4", "gx1", "gx2", "gx3", "gx5"], "gx4", {"gx4": "Egy idővonal a vásárlástól a 13. hétig: a két garancia pont ott ül, ahol érvényes. Egyértelmű, és oldja a vásárlás előtti kételyt."})
kat("latogatas", ["lx1", "lx2", "l1", "l5", "l3"], "lx1", {
    "lx1": "A „12 hét múlva mindenképpen 12 héttel idősebb leszel” mondat mellett egy lassan peregő homokóra (a ti saját ikonotok). Az idő múlása szó szerint látszik.",
    "lx2": "12 pötty, ami görgetésre kigyullad: a 12 hét ritmusa egy pillantásra.",
    "l1": "Narancs sáv a mondattal, mellette a program ritmusa kártyán (12 hét, hetente egy gyakorlat, online).",
    "l5": "Fotó (tengerpart) és két tiszta infóhasáb.", "l3": "Belépőjegy-forma: játékos."})
kat("mia", ["mi1", "mi2", "mi3", "mi4", "mi5"], "mi1", {"mi1": "Először tisztázza, mi NEM a program (40 órányi videó, filozófia, pózok), aztán egy kártyán, hogy mi igen: 12 gyakorlat, 12 hét. A 45+ férfi rögtön tudja, mire számíthat."})
kat("ajanlat", ["ax2", "ax1", "ax3", "ax4", "ax5"], "ax2", {
    "ax2": "A Prémium csomag sötét, gyertyafényes kártyán áll az alap mellett: a drágább ajánlat magától kiemelkedik, és a „prémium” szó tényleg látszik.",
    "ax1": "Két oszlop pipás listával, a Prémium kiemelve: a megszokott, könnyen összevethető árazás.",
    "ax3": "Két „edzésbérlet” letéphető szelvénnyel: játékos, az edzésterv világában marad.",
    "ax4": "Nyomtatott árlista-lap pontozott vezetővonallal: klasszikus, tömör.", "ax5": "Fotós csomagkártyák árcímkével: hangulatos, kézzelfogható."})
kat("gyik", ["qx1", "qx4", "qx3", "qx2", "qx5"], "qx1", {"qx1": "Lenyíló lista: hat kérdés kevés helyen, a válaszok csak akkor jelennek meg, ha kell."})
kat("lablec", ["lbx", "lb1", "lb2", "lb3", "lb4"], "lbx", {
    "lbx": "Sötét, csendes lezárás a fehér logóval egy halvány jantra előtt, egy mondattal („Adj a testednek 12 hetet.”) és egy utolsó gombbal.",
    "lb1": "Klasszikus négyhasábos sötét lábléc.", "lb2": "Óriás márkanév: magabiztos.", "lb3": "Középre zárt, minimál.", "lb4": "Színes, lekerekített: lendületes."})

spec["egyedi_css"] = (""
                     ".kiem{color:var(--hl);font-weight:800}"
                     ".elo-root .sec:not(#top) h2.cim{font-size:var(--t-h2)}"
                     "#top .hcim{font-size:calc(clamp(1.9rem,3.4cqi,3.1rem)*var(--hero-scale,1));line-height:1.1}"
                     "#folyamat .wrap>:not(.shead),#folyamat .wrap>:not(.shead) *{text-align:left!important}"
                     ".v-f3 .ns p b{display:inline;font:inherit;font-weight:800;line-height:inherit;color:var(--c-head);-webkit-text-stroke:0;margin:0}"
                     "#kinalat .krt>.krt-kep .ph,#kinalat .ft .ph{--ar:16/9}")
# ikon-spec (OpenAI-kulcs nélkül: a motor a márka formáiból épít tartalék ikonokat)
(MUNKA / "arculat.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
print("arculat.json kész:", len(json.dumps(spec)) // 1024, "KB")
