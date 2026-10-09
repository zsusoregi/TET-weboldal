# -*- coding: utf-8 -*-
"""Tantraszex Edzésterv: az arculat.json alap-része (márka, tartalom, paletta, betű, motívum)."""

ORDER = "https://sf.soregizsuzsa.hu/t/r/tantraszex-edzesterv"
ORDER_PREMIUM = "https://sf.soregizsuzsa.hu/t/r/tantraszex-edzesterv-premium"
CSOMAGOK = "#etlap"   # minden más gomb a Csomagok blokkhoz visz

FORMAK = {
    "jantra": "<circle cx='50' cy='50' r='43' fill='none' stroke='#000' stroke-width='6'/>"
              "<path d='M50 84 L17 29 H83Z M50 31 L68 63 H32Z' fill='none' stroke='#000' stroke-width='5.5' stroke-linejoin='round'/><circle cx='50' cy='52' r='5'/>",
    "lotusz": "<path d='M50 14C63 32 63 56 50 74 37 56 37 32 50 14Z'/>"
              "<path d='M47 74C38 58 22 50 6 50 12 68 30 78 47 74Z'/><path d='M53 74C62 58 78 50 94 50 88 68 70 78 53 74Z'/>"
              "<path d='M16 84Q50 96 84 84' fill='none' stroke='#000' stroke-width='6' stroke-linecap='round'/>",
    "lang": "<path d='M50 6C58 26 78 38 78 62A28 28 0 0 1 22 62C22 46 32 38 37 25 41 37 45 42 50 44 55 33 55 20 50 6Z'/>",
    "homokora": "<path d='M22 8H78V18C78 36 60 42 57 50 60 58 78 64 78 82V92H22V82C22 64 40 58 43 50 40 42 22 36 22 18Z'/>",
}

PALETTAK = [
    dict(id="p1", nev="Égetett narancs, igényesebben",
         miert="A mostani narancs (#B54E02) és a krém háttér marad, csak mélyebb barna szöveggel és egy borostyán kísérőszínnel. "
               "Ugyanaz a márka, rendezettebben: aki ismeri az oldalt, rögtön ráismer.",
         primary="#B54E02", accent="#E39A4C", accent2="#6F3C1E", paper="#FFFBF4", ink="#2B1B12", deep="#1C130E", card="#FFFFFF"),
    dict(id="p2", nev="Gyertyafény (sötét prémium)",
         miert="A fotóitok fekete háttér előtt, meleg bőrtónusokkal készültek. Ez a paletta ezt a hangulatot viszi végig: "
               "sötét, intim felületek, gyertyaláng-narancs és mézszínű fény. Prémium, felnőtt, diszkrét.",
         primary="#D2691E", accent="#E9B872", accent2="#B5562A", paper="#17110D", ink="#F3E9DD", deep="#0D0907", card="#221913", mod="sotet"),
    dict(id="p3", nev="Terrakotta és zsálya",
         miert="A narancs földszínű terrakottává szelídül, mellé egy nyugodt zsályazöld kerül. Modern wellness-hangulat, "
               "kevésbé „ezoterikus”: a szkeptikusabb 45+ férfinak is komolyan vehető.",
         primary="#B8552B", accent="#8A9A78", accent2="#3E4A3A", paper="#F6F2EC", ink="#23201C", deep="#2A2E26"),
    dict(id="p4", nev="Sáfrány és éjkék",
         miert="Élénk sáfránynarancs és mély éjkék: sportos, edzésterv-hangulat, erős kontraszt. A legmerészebb út, "
               "a „12 hét, 12 gyakorlat” fegyelmét hangsúlyozza a spirituális rész helyett.",
         primary="#D9600C", accent="#F2B33D", accent2="#1F3347", paper="#FBF7F0", ink="#172331", deep="#14202D"),
    dict(id="p5", nev="Barackos hajnal",
         miert="Puha barack és homok, egy csendes kékeszöld kísérővel. A legbarátságosabb, legkevésbé kihívó változat: "
               "a téma kényes, ez a paletta oldja a feszültséget.",
         primary="#C8673A", accent="#F0B48A", accent2="#5F7F78", paper="#FFF7F0", ink="#3A2A22", deep="#45291E"),
]

BETUK = [
    dict(id="b1", nev="Cormorant + Karla (elegáns)",
         miert="Finom, klasszikus serif a címekben: érzéki, nyugodt, a tantra méltóságát hozza. A Karla szövegbetű tiszta és "
               "jól olvasható hosszú bekezdésekben is (az oldalon sok a szöveg).",
         display="Cormorant Garamond", body="Karla", hand="Great Vibes", label="DM Mono", w_display=600,
         ls_display="-0.01em", lh_display=1.04, hero_scale=1.14, fs_hand=1.45),
    dict(id="b2", nev="Outfit + Figtree (modern)",
         miert="Geometrikus, barátságos grotesk: wellness- és app-érzet, semmi „ezo”. Rendezett, mai, és a program "
               "gyakorlati, edzésszerű oldalát erősíti.",
         display="Outfit", body="Figtree", hand="Shadows Into Light", label="Red Hat Mono", w_display=600,
         ls_display="-0.025em", lh_display=1.06, hero_scale=1, fs_hand=1.3),
    dict(id="b3", nev="Oswald + Work Sans (merész)",
         miert="Keskeny, nagybetűs plakátbetű, mint egy edzésterv vagy sportnapló fejléce. Férfias, határozott, "
               "a „12 hét, 12 gyakorlat” ritmusát üti.",
         display="Oswald", body="Work Sans", hand="Kaushan Script", label="IBM Plex Mono", w_display=600,
         ls_display="0", lh_display=1.02, nagybetus=True, hero_scale=1.06, fs_hand=1.15),
    dict(id="b4", nev="Fraunces + Nunito Sans (barátságos)",
         miert="Meleg, puha serif: emberi, közvetlen hang, mintha Zsuzsa személyesen beszélne. A Nunito Sans kerekded, "
               "nyugodt szövegbetű.",
         display="Fraunces", body="Nunito Sans", hand="Dancing Script", label="Sometype Mono", w_display=600,
         ls_display="-0.02em", lh_display=1.06, hero_scale=1, fs_hand=1.3),
    dict(id="b5", nev="DM Serif Display + Source Sans 3 (klasszikus)",
         miert="A szövegbetű a mostani Open Sans közeli rokona (humanista grotesk), így az oldal érzete alig változik; "
               "a címek viszont erős kontrasztú, klasszikus serifet kapnak.",
         display="DM Serif Display", body="Source Sans 3", hand="Marck Script", label="Courier Prime", w_display=400,
         ls_display="-0.01em", lh_display=1.08, hero_scale=1.02, fs_hand=1.3),
]

FOTOK = {
    "szivsotet": {"fajl": "kepek/sziv-sotet.jpg", "alt": "Férfi lótuszülésben, kezét a szívére teszi", "pozicio": "50% 30%"},
    "szivfekete": {"fajl": "kepek/sziv-fekete.jpg", "alt": "Férfi meditál fekete háttér előtt, kezét a szívére teszi", "pozicio": "50% 35%"},
    "jantra": {"fajl": "kepek/jantra-meditacio.jpg", "alt": "Meditáló férfi, mögötte jantra-mandala", "pozicio": "50% 30%"},
    "tenger": {"fajl": "kepek/tengerpart.jpg", "alt": "Férfi a tengerparton ül és a naplementét nézi", "pozicio": "50% 55%"},
    "kovek": {"fajl": "kepek/kovek.jpg", "alt": "Kéz egy sor kavicsot rendez", "pozicio": "60% 50%"},
    "zsuzsa": {"fajl": "kepek/zsuzsa.jpg", "alt": "Sőregi Zsuzsa (Kirana) portré", "pozicio": "50% 35%"},
    "b1": {"fajl": "kepek/bonusz-test-lelek.jpg", "alt": "Test + Lélek Kiegészítő borító", "pozicio": "50% 50%"},
    "b2": {"fajl": "kepek/bonusz-kerekasztal.jpg", "alt": "A Nő Szerepe a Férfi Szexualitásában borító", "pozicio": "50% 50%", "max": 1100},
    "b3": {"fajl": "kepek/bonusz-konzultacio.jpg", "alt": "Tantra Gyakorlók konzultációs csoport borító", "pozicio": "50% 50%"},
}

TARTALOM = {
    "marka": {"nev": "Tantraszex Edzésterv", "szlogen": "12 hét, 12 gyakorlat. Egy új szint a szexualitásodban.",
              "slug": "tantraszex-edzesterv", "url": "https://tet.tantraiskola.com"},
    "seo": {"title": "Tantraszex Edzésterv · Online gyakorlóprogram 45+ férfiaknak",
            "description": "12 hetes online gyakorló program férfiaknak, a tantrikus szexualitás alapjainak elsajátításához."},
    "logo": {"fajl": "kepek/logo.png"},
    "profil": {
        "osszefoglalo": "A Tantraszex Edzésterv egy 12 hetes online gyakorlóprogram 45+ férfiaknak, Sőregi Zsuzsa (Kirana) "
                        "tantraoktatótól. Az oldal hangja tegező, egyenes és meleg: edzésként beszél a tantráról („12 hét, "
                        "12 gyakorlat”, „Izomláz garancia”), nem filozófiaként. A mostani arculat égetett narancs (#B54E02) "
                        "krémszínű háttéren, Open Sans betűvel; a fotók sötét háttér előtt meditáló férfit, jantrát, "
                        "kavicsokat és tengerpartot mutatnak, az ikonok vékony narancs vonalrajzok (szem, homokóra, lótuszülés).",
        "talalt_szinek": ["#B54E02", "#FFFBF4", "#FFEED8", "#4C4C4C"],
        "talalt_betuk": ["Open Sans"],
        "motivumok": "Jantra (két egymásba fordított háromszög körben), lótusz, láng (szexuális energia), homokóra (a 12 hét, "
                     "„12 hét múlva mindenképpen 12 héttel idősebb leszel”), lélegzet-hullám, az izgalom hullámzó görbéje.",
    },
    "motivum": {
        "formak": FORMAK, "jel": "jantra",
        "szellemszavak": {"hero": "JELENLÉT", "rolaszol": "45+", "miert": "FIGYELEM", "folyamat": "12 HÉT",
                          "tortenet": "KIRANA", "tenyek": "ERŐ", "kinek": "NEKED", "velemenyek": "ÉLMÉNY",
                          "kinalat": "AJÁNDÉK", "garancia": "GARANCIA", "latogatas": "MOST", "ajanlat": "EDZÉS",
                          "gyik": "KÉRDÉS", "galeria": "LÉGZÉS", "mia": "12 × 12"},
        "ticker": ["12 hét", "12 gyakorlat", "Online, a saját tempódban", "45+ férfiaknak", "„Első randi” garancia",
                   "„Izomláz” garancia", "39.000 Ft értékű ajándék"],
        "matricak": ["12 hét · 12 gyakorlat", "45+ férfiaknak", "Saját tempóban", "Két garancia"],
    },
    "fotok": FOTOK,
    "kapcsolat": {"email": "[e-mail cím pótolandó]", "nyitva_cim": "A program ritmusa",
                  "nyitvatartas": [["Időtartam", "12 hét"], ["Gyakorlatok", "12, hetente egy új"],
                                   ["Forma", "Online kurzus"], ["Tempó", "Otthon, a saját tempódban"]],
                  "nyitva_rovid": "12 hét · 12 gyakorlat · online"},
    "nav": {"linkek": [["A program", "#folyamat"], ["Kirana", "#rolunk"], ["Vélemények", "#velemenyek"],
                       ["Csomagok", "#etlap"], ["GYIK", "#gyik"]],
            "cta": {"szoveg": "Csomagok", "href": "#etlap", "ikon": "nyil"}, "nev_mutat": True},
    "hero": {
        "kicker": "Online gyakorlóprogram 45+ férfiaknak",
        "meta": "**Tantraszex Edzésterv** · 12 hét · 12 gyakorlat",
        "badgek": [{"ikon": "szem", "szoveg": "Figyelem, légzés, tudatos érintés"},
                   {"ikon": "pipa", "szoveg": "Az izgalom tudatos irányítása"},
                   {"ikon": "ora", "szoveg": "Saját tempóban, visszanézhető anyagokkal"}],
        "cim": "12 hét, 12 gyakorlat. Egy ==új szint== a szexualitásodban.",
        "lead": "Nem kell hinned a Tantrában, csak próbáld ki, mit csinál a testeddel!",
        "cta1": {"szoveg": "Megnézem, hogy működik", "href": CSOMAGOK},
        "cta2": {"szoveg": "Csomagok és árak", "href": "#etlap", "ikon": "nyil"},
        "jegyzet": "Legyél magabiztos szerető!",
        "statok": [["12", "hét"], ["12", "gyakorlat"], ["45+", "férfiaknak"]],
        "fotok": ["szivsotet", "jantra", "tenger", "kovek"],
        "fotok_h5": ["jantra"],
        "kiemelt": {"ikon": "figyelem", "cim": "Saját tempóban", "szoveg": "Visszanézhető anyagokkal, lépésről lépésre."},
    },
    "tenyek": {
        "kicker": "Miért érdemes?", "cim": "Amit a ==12 hét== ad neked",
        "elemek": [
            {"ikon": "izgalom", "szam": "Izgalom", "cim": "Megtanulod kezelni a szexuális izgalmad",
             "szoveg": "Te irányítod a szexuális energiád, és azt a helyzetet is, amikor nem jelenik meg az izgalmi energia.",
             "korszoveg": "Tantraszex Edzésterv"},
            {"ikon": "figyelem", "szam": "Figyelem", "cim": "Felhagysz a leggyakoribb hibákkal",
             "szoveg": "Megtanulod érzékelni a szexuális energiát nem csak magadban, de a partneredben is.",
             "korszoveg": "Tantraszex Edzésterv"},
            {"ikon": "legzes", "szam": "Biztonság", "cim": "Teljesen biztos leszel a dolgodban",
             "szoveg": "Elegendő elméleti tudásod és gyakorlati tapasztalatod lesz ahhoz, hogy minden szeretkezést művészként megalkoss.",
             "korszoveg": "Tantraszex Edzésterv"},
            {"ikon": "erintes", "szam": "Önbizalom", "cim": "Laza, természetes önbizalmad lesz a nőkkel",
             "szoveg": "Minden nő teste máshogy működik. Megtanulsz egy szemléletváltást, amitől csodálatos kísérőjévé válsz.",
             "korszoveg": "Tantraszex Edzésterv"},
            {"ikon": "szabalyozas", "szam": "Élmény", "cim": "Újabb és újabb élményeket szerzel",
             "szoveg": "Felfedezel olyan dolgokat a szexben, amelyekről korábban álmodni sem mertél.",
             "korszoveg": "Tantraszex Edzésterv"},
            {"ikon": "homokora", "szam": "Erő", "cim": "Mellékhatások: fiatalság, erő, egészség",
             "szoveg": "Gazdálkodni tudsz az élet-energiáddal: az elgyengülés nem szükségszerű velejárója az évek múlásának.",
             "korszoveg": "Tantraszex Edzésterv"},
        ]},
    "folyamat": {
        "kicker": "Mit edzünk 12 héten keresztül?", "cim": "Öt képesség, ==12 hét==, 12 gyakorlat",
        "lead": "Egy 12 hetes online gyakorlóprogram 45+ férfiaknak. Minden héten kapsz egy új gyakorlatot, amely az előzőre épül.",
        "lepesek": [
            {"ikon": "figyelem", "cim": "Figyelem és jelenlét",
             "szoveg": "„Ahol a figyelem, ott az energia.” Megtanulsz hosszan benne maradni egy érintésben, egy érzésben."},
            {"ikon": "legzes", "cim": "Légzés",
             "szoveg": "Az egyik legegyszerűbb eszköz, amit mindig magaddal viszel. Mélyíti a gyönyörérzetet, és irányítja az energiát."},
            {"ikon": "erintes", "cim": "Tudatos érintés",
             "szoveg": "Nem azért érinteni, hogy történjen valami. Hanem azért, hogy érezd, ami történik."},
            {"ikon": "izgalom", "cim": "A szexuális izgalom irányítása",
             "szoveg": "Nem elnyomni tanulod az izgalmat. Hanem elbírni egyre többet az élvezetből."},
            {"ikon": "szabalyozas", "cim": "Az ejakuláció tudatosabb szabályozása",
             "szoveg": "Nem harcolni a testeddel. Hanem együttműködni vele, és élvezni az izgalmi energia hullámzását."},
        ]},
    "tortenet": {
        "kicker": "A Tantraszex Edzésterv megalkotója",
        "cim": "Sőregi Zsuzsa (==Kirana==), tantraoktató és szexuális önismereti tréner",
        "bekezdesek": [
            "Az elmúlt évtizedben több ezer férfi és nő bízta rám magát, hogy új dolgokat fedezzen fel a szexualitásában, "
            "tantrát, tantrikus szexualitást tanuljon.",
            "Elvégeztem az International School of Temple Arts Szexuális önismeret 1-2 és Szexuális Gyógyító kurzusait, "
            "de talán a legfontosabb a saját út, a saját tapasztalás: én magam is a Tantra útját járom. Így élek, így szeretek.",
        ],
        "idezet": "A Tantra nem csupán hivatás számomra, hanem az életem.",
        "alairas": {"nev": "Kirana", "szerep": "Sőregi Zsuzsa · tantraoktató"},
        "fotok": ["zsuzsa", "jantra", "kovek"], "fotok_felirat": ["Kirana", "Jelenlét", "Lépésről lépésre"],
        "foto_felirat": "Sőregi Zsuzsa (Kirana)",
        "merfoldkovek": [["Évtized", "Több ezer férfi és nő tanult tőle tantrát"], ["ISTA", "Szexuális önismeret 1-2 és Szexuális Gyógyító kurzus"], ["Ma", "Maga is a Tantra útját járja"]],
    },
    "kinalat": {
        "kicker": "Ajándékok", "cim": "Az edzésterv mellé ==ajándékba== adjuk",
        "lead": "A következő bónusz anyagok értéke 39.000 Ft.",
        "elemek": [
            {"nev": "Test + Lélek Kiegészítő", "ikon": "erintes", "foto": "b1",
             "leiras": "A fizikai gyakorlás kiegészítése mentális gyakorlatokkal egy tökéletesebb és harmonikusabb eredményért.", "ar": "Bónusz"},
            {"nev": "A Nő Szerepe a Férfi Szexualitásában", "ikon": "figyelem", "foto": "b2",
             "leiras": "Videó: kerekasztal-beszélgetés a tantrikus szexről és a női partner szerepéről, két tantra oktató és egy szex coach részvételével.",
             "ar": "Bónusz videó"},
            {"nev": "Tagság a konzultációs csoportban", "ikon": "legzes", "foto": "b3",
             "leiras": "Havi 1 alkalommal online beszélgetés a tapasztalatokról, és válasz a kérdésekre tantra oktatók vezetésével.",
             "ar": "Havi 1 alkalom"},
        ]},
    "ajanlat": {
        "kicker": "Csomagok", "cim": "Válaszd ki a ==saját edzéstervedet==",
        "lead": "Mindkét csomag online, otthon, a saját tempódban végezhető.",
        "lab": "Részletesebb információért a prémium csomagról írj nekünk.",
        "elemek": [
            {"nev": "Tantraszex Edzésterv", "ar": "38.900 Ft", "foto": "szivsotet",
             "leiras": "12 hét, 12 gyakorlat. Online kurzus, otthon, a saját tempódban.", "cimkek": ["Online kurzus", "Saját tempó"]},
            {"nev": "Tantraszex Edzésterv Prémium", "ar": "99.800 Ft", "foto": "tenger",
             "leiras": "12 hetes program, a gyakorlatok és az időbeosztás személyre szabásával, a tapasztalatok megosztásával és problémakezeléssel személyesen.",
             "cimkek": ["Személyre szabva", "Személyes kísérés"]},
        ]},
    "latogatas": {
        "kicker": "Miért most?", "cim": "12 hét múlva mindenképpen ==12 héttel idősebb== leszel.",
        "lead": "A kérdés csak az, hogy közben változik-e valami. Adhatsz a testednek 12 hetet, hogy megtanuljon valami újat. "
                "Nem kell sietned. De a halogatás is egy döntés.",
        "cta1": {"szoveg": "Megnézem az ajánlatot", "href": "#etlap"},
        "cta2": {"szoveg": "Belevágok", "href": CSOMAGOK, "ikon": "nyil"},
        "foto": "tenger"},
    "lablec": {"szoveg": "12 hetes online gyakorló program férfiaknak, a tantrikus szexualitás alapjainak elsajátításához.",
               "cegnev": "Tantraszex Edzésterv · Sőregi Zsuzsa (Kirana)",
               "felhivas": "Adj a testednek 12 hetet.",
               "linkek": [["A program", "#folyamat"], ["Kirana", "#rolunk"], ["Garanciák", "#garancia"], ["Csomagok", "#etlap"], ["GYIK", "#gyik"]]},
}

# a saját (egyedi) szekciók tartalma: szó szerint az oldalról
ROLASZOL = {
    "kicker": "Miről szól a tantraszex edzésterv?",
    "cim": "Nem azt tanulod újra, amit már ==harminc (vagy több) éve== csinálsz.",
    "lead": "Olyan képességeket edzünk, amelyeket valószínűleg soha senki nem tanított meg neked.",
    "szoveg": "Vannak képességeid, melyek csodálatos, és teljesen magabiztos szeretővé tesznek. Ezeket a képességeket épp úgy "
              "edzeni kell, mint az izmaidat.",
    "trio": [["15+", "felfedezted a szexet."], ["25+", "felfedezted a női testet."],
             ["45 felett", "fedezd fel a saját tested még kiaknázatlan lehetőségeit!"]],
    "zaro": "És válj ezáltal a szeretkezés mesterévé!",
    "talan": ["Talán egy hosszú kapcsolat után újra egyedül vagy.",
              "Talán már megjelent valaki, akivel most másképp szeretnéd.",
              "Talán egyszerűen azt érzed, hogy a következő húsz éved szexualitását nem ugyanúgy akarod megélni, mint az előző húszat.",
              "Nem több teljesítményt szeretnél, hanem több nyugalmat, több élvezetet.",
              "És sokkal kevesebb megfelelést."],
}
MIERT = {
    "kicker": "Miért pont tantra?",
    "cim": "A figyelem lassan kiköltözik a testből, és ==beköltözik a fejbe==.",
    "lead": "A nyugati ember szeret célokat kitűzni. Elindulunk valahonnan, és igyekszünk minél gyorsabban megérkezni. "
            "Ezt a gondolkodást bevittük a szexualitásunkba is.",
    "lanc": ["Izgalom", "Erekció", "Egyre nagyobb izgalom", "Orgazmus"],
    "lanc_vege": "Sikerült…. Vagy nem sikerült….",
    "kerdesek": ["Elég jó vagyok?", "Elég sokáig bírom?", "Élvezi a partnerem?", "Működni fog?", "Mikor kellene továbblépnem?"],
    "tantra_cim": "A tantra ennek szinte az ellenkezőjét tanítja.",
    "tantra": ["Nem azt, hogyan juss gyorsabban a csúcsra.", "Nem is azt, hogy hogyan juttasd a partneredet oda.",
               "Hanem azt, hogy hogyan maradj benne abban, ami jó."],
    "zaro": "A tantrikus szex nem technikával kezdődik, hanem figyelemmel.",
    "zaro2": "Ezt azonban nem lehet pusztán megérteni. Gyakorolni kell.",
    "cta": {"szoveg": "Érdekel, mit kapok a programban", "href": CSOMAGOK},
}
KINEK = {
    "kicker": "Kinek szól a Tantraszex Edzésterv?",
    "cim": "Neked szól, ha ==45 feletti férfiként==:",
    "igen": ["egy hosszabb kapcsolat után új életszakaszba érkeztél;",
             "egyedülállóként szeretnél magabiztosabban belépni egy következő kapcsolatba,",
             "vagy egy új kapcsolatban most szeretnéd más alapokra helyezni a szexualitásodat."],
    "is": "Akkor is neked szólhat, ha nincs különösebb „problémád”. Egyszerűen érzed, hogy ennél több van a szexben, és "
          "kíváncsi vagy arra, mire képes a tested, ha megtanulsz valóban figyelni rá.",
    "nem": ["Ez a program viszont nem egy évtizedek óta ellaposodott kapcsolat „megjavítására” készült.",
            "És nem gyors szexuális trükköket tanít."],
    "zaro": "Annak szól, aki hajlandó rendszeresen gyakorolni.",
}
VELEMENYEK = {
    "kicker": "Mások így élték meg", "cim": "Akik már ==végigcsinálták==",
    "idezetek": [
        "Mikor találkoztam a Tantraszex edzéssel, éreztem, - még ha nem is volt rá tapasztalatom- hogy van realitása annak, hogy "
        "sokkal jobb lehet, ha \"nem pukkad ki a lufi\". De arra, amit most magmegtartóként megélek a szexben, legvadabb "
        "szexuális álmomban sem gondoltam volna…",
        "Eleinte egy kicsit sajnáltam az időt a gyakorlásra, mert mindig rengeteg dolgom volt, a gimnázium óta időhiányban szenvedtem. Durva, hogy a Tantraszex Edzés "
        "nem csak a szexualitásomat forradalmasította, de sokkal összeszedettebbé, energikusabbá tett a munkában, a hétköznapokban is. "
        "Egyszer csak azt vettem észre, hogy valahogy több időm van.",
        "Volt, hogy a tudatos és irányított légzés óvott meg attól, hogy \"átessek\". Jó volt azokat az új érzeteket megtapasztalni. (…) "
        "Folyamatosan feszegettem a határokat, közben tanulva a testem jelzéseit.",
        "Egyszerre volt hihetetlen, de ugyanakkor valós, természetes és transzcendentális. Megdöbbentően \"Uramisten!\" érzés. "
        "Hogy tényleg van ilyen? Ekkora és ennyire elnyújtható élvezet? Pedig még csak a tanulás elején vagyok!",
    ],
    "kiemelt": ["legvadabb szexuális álmomban sem gondoltam volna", "több időm van", "tudatos és irányított légzés",
                "\"Uramisten!\" érzés"],
}
GARANCIA = {
    "kicker": "Garanciák", "cim": "Két garancia, ==kockázat nélkül==",
    "g": [
        {"nev": "„Első randi” garancia", "fo": "24 órád van eldönteni, akarsz-e másodikat!", "ido": "24 óra",
         "szoveg": "Vásárlás után nézz bele a Tantraszex Edzéstervbe, ismerkedj meg a felépítésével és kezdd el az első gyakorlatot! "
                   "Ha elsőre úgy érzed, hogy „Köszönöm, ez nem az én világom”, jelezd nekem 24 órán belül, és visszakapod a kurzus árát.",
         "zaro": "Nincs sértődés. Nincs kínos magyarázkodás."},
        {"nev": "„Izomláz” garancia", "fo": "Ha végigcsináltad az edzést, de semmi hatást nem érzel, visszakapod a pénzed!",
         "ido": "13. hét",
         "szoveg": "Végezd el a 12 hét 12 gyakorlatát az útmutatás szerint. Ha 12 hét után azt mondod: „Megcsináltam. De nem érzek "
                   "érdemi változást.”, akkor visszaadom a kurzus árát, a vásárlás napjától számított 13. héten.",
         "zaro": "Ha te beleteszed a 12 hetet, én vállalom a garanciát."},
    ],
}
GYIK = {
    "kicker": "Gyakran Intézett Kérdések", "cim": "Amit ==kérdezni szoktak==",
    "k": [
        ["Mi történik, miután kitöltöttem a megrendelőlapot?", "[Válasz pótolandó: a mostani oldalon itt még sablonszöveg áll.]"],
        ["Kapok számlát?", "Természetesen."],
        ["Mit tud nekem újat mondani a szexről ennyi idős koromban?",
         "Nem azt tanulod újra, amit már harminc éve csinálsz. Olyan képességeket edzünk, amelyeket valószínűleg soha senki nem tanított meg neked."],
        ["Akkor is működik, ha nem vagyok „spiri”?", "Nem hinni kell benne. Csinálni kell."],
        ["Egyedül hogyan gyakoroljak szexet?", "Nem kell megvárnod a következő kapcsolatodat ahhoz, hogy más férfiként érkezz bele."],
        ["Mi van, ha elkezdem, aztán nem csinálom?",
         "Nem kell megtanulnod a tantrát. Ezen a héten csak ezt az egy gyakorlatot kell elvégezned. A fiók megmarad, hónapok múlva újra előveheted."],
    ],
    "cta": {"szoveg": "Belevágok a Tantraszex Edzéstervbe!", "href": CSOMAGOK},
}

# Prémium csomag részletei: felugró ablak a Csomagok szekcióban (az ügyfél szövege, csak elírások javítva)
PREMIUM = {
    "link": "Mit tartalmaz a prémium csomag? Kattints ide!",
    "cim": "TANTRASZEX EDZÉSTERV PRÉMIUM",
    "bevezeto": [
        "A sportolási célú edzésben is vannak általános edzéstervek, melyek mindenkinél működnek, és mindenki számára hasznosak. "
        "De általában hatékonyabb a személyi edzővel való munka, mert ha az edző csak rád fókuszál, figyelembe tudja venni a Te "
        "egyéni adottságaidat, körülményeidet, szól, ha valamit rosszul csinálsz, stb.",
        "Ugyanígy, a Tantraszex Edzésterv is mindenkinél működik, mindenki megélhet általa csodálatos változásokat a testében és "
        "a szexuális életében.",
        "De a Tantraszex Edzésterv Prémium tartalmaz **3 alkalmat, mely csak Rólad szól!**",
    ],
    "alkalmak": [
        {"cim": "1. alkalom", "ido": "90 perc", "mikor": "Még a gyakorlás megkezdése előtt:",
         "pontok": ["a gyakorlatokat hozzáalakítjuk a Te jelenlegi szexualitásodhoz és szándékaidhoz",
                    "az edzéstervet hozzáalakítjuk a Te személyes napirendedhez, életviteledhez"]},
        {"cim": "2. alkalom", "ido": "60 perc", "mikor": "„Félidős” konzultáció:",
         "pontok": ["melyben átnézzük a gyakorlatok helyes végrehajtását", "megbeszéljük az addigi tapasztalataid",
                    "megoldást találunk az esetleges nehézségekre, kihívásokra"]},
        {"cim": "3. alkalom", "ido": "60 perc", "mikor": "Az edzésterv vége felé:",
         "pontok": ["megbeszéljük a tapasztalataid", "ha szükséges, megbeszéljük, hogyan vonhatod be a partnered",
                    "tervet készítünk a folytatásra, a Te egyéni utadon"]},
    ],
    "helyszin": "A 3 alkalom online vagy személyes (Budapesten), ahogy Neked kényelmesebb.",
    "ar": "A Tantraszex Edzésterv Prémium ára 99.800 Ft",
    "cta": {"szoveg": "Ezt választom", "href": ORDER_PREMIUM},
}


# =====================================================================================================
# AZ ÜGYFÉL EREDETI SALES-SZÖVEGE (bemenet/sales/eredeti.pdf), elírás- és helyesírás-javítással.
# A !!...!! jelölés: az eredetiben pirossal kiemelt rész (a paletta kiemelő színét kapja).
# =====================================================================================================
_h = TARTALOM["hero"]
_h.pop("badgek", None)
_h.pop("jegyzet", None)
_h.pop("kicker", None)   # a termék neve a lead elejére került, kiemelve
_h.pop("kiemelt", None)   # ez is a régi oldal egyik ígérete volt
_h.update({
    "cim": "Legyél ==magabiztos szerető==, és fedezz fel különleges élményeket, tökéletes kapcsolódásokat a szexben, néhány új képesség megszerzése révén!",
    # §TERMEK§: a termék neve kiemelt blokként (a gen/utofeldolgozas.py cseréli le a kész HTML-ben)
    "lead": "§TERMEK§ | **12 hét, 12 gyakorlat. Egy új szint a szexualitásodban.** | Nem kell hinned a Tantrában, csak próbáld ki, mit csinál a testeddel!",
})

ROLASZOL.update({
    "kicker": "Miről szól a tantraszex edzésterv?",
    "cim": "Nem azt tanulod újra, amit már ==harminc (vagy több) éve== csinálsz.",
    "lead": "Olyan képességeket edzünk, amelyeket valószínűleg soha senki nem tanított meg neked.",
    "szoveg": "Vannak képességeid, melyek csodálatos, és teljesen magabiztos szeretővé tesznek, aki soha nem okoz csalódást "
              "sem fizikailag, sem érzelmileg a partnerének (és magának sem!). Ezeket a képességeket épp úgy edzeni kell, mint az izmaidat. | "
              "Soha nem lesz több kellemetlen szeretkezésed, vagy borzalmas randid! Soha nem kell félned, hogy cserbenhagy a tested! | "
              "És ahogy múlnak az évek, nem csak szexuális potenciálod őrzöd meg, de irigylésre méltóan erős és egészséges, "
              "kiegyensúlyozott férfi maradsz.",
    "talan": ["Talán egy hosszú kapcsolat után újra egyedül vagy.",
              "Talán már megjelent valaki, akivel most másképp szeretnéd.",
              "Talán egyszerűen azt érzed, hogy **a következő húsz éved szexualitását nem ugyanúgy akarod megélni, mint az előző húszat.**",
              "Nem több teljesítményt szeretnél, hanem több nyugalmat, több élvezetet.",
              "És sokkal kevesebb megfelelést."],
})

MIERT.update({
    "lead": "A nyugati ember szeret célokat kitűzni. Elindulunk valahonnan, és igyekszünk minél gyorsabban megérkezni. "
            "**Ezt a gondolkodást bevittük a szexualitásunkba is.**",
    "lanc_vege": "Sikerült… Vagy nem sikerült…",
    "fontos": "És minél fontosabbá válik a cél, annál könnyebben történik valami furcsa: **elfelejtjük érezni azt, ami közben történik.**",
    "kerdes_cim": "Figyelni kezdjük magunkat:",
    "zaro": "A tantrikus szex nem technikával kezdődik, hanem figyelemmel.",
    "zaro2": "Azzal a képességgel, hogy észrevedd, mi történik a testedben. | Megtanulod felépíteni, megtartani és szabályozni "
             "a szexuális izgalmat. | És közben ott maradni, a testedben, a másik emberrel, a pillanatban. | "
             "**Ezt azonban nem lehet pusztán megérteni.** Gyakorolni kell. | Ezért született meg a **Tantraszex Edzésterv.**",
    "cta": {"szoveg": "Érdekel, mit kapok a programban", "href": CSOMAGOK},
})

MIA = {
    "kicker": "A program", "cim": "Mi a ==Tantraszex Edzésterv==?",
    "lead": "Egy **12 hetes online gyakorlóprogram 45+ férfiaknak.**",
    "nem": ["Nem 40 órányi videó.", "Nem tantrikus filozófiák gyűjteménye.", "És nem száz új póz vagy szex-kütyü."],
    "ritmus": "12 gyakorlat, 12 hét.",
    "het": "Minden héten kapsz egy új gyakorlatot, amely az előzőre épül.",
    "sport": "Ahogy egy sportedzésben sem attól leszel erősebb, hogy elolvasod a gyakorlatokat, itt sem az információ mennyisége számít. "
             "Hanem az, amit a tested megtanul.",
    "cel": "A cél az, hogy a 12 hét végére a tantraszex-technika ne valami legyen, **amit tudsz.** Hanem valami, **amire képes vagy.**",
}

TARTALOM["folyamat"].update({
    "kicker": "A 12 hét", "cim": "Mit edzünk ==12 héten== keresztül?", "lead": "",
    "lepesek": [
        {"ikon": "figyelem", "cim": "Figyelem és jelenlét",
         "szoveg": "„Ahol a figyelem, ott az energia” – tanítja a Tantra. Megtanulsz hosszan benne maradni egy érintésben, egy érzésben, "
                   "egy orgazmus-hullámvasútban. Megtanulod a figyelmeddel irányítani a testedben a szexuális energiát, és pusztán "
                   "a figyelmeddel fokozni vagy csökkenteni azt."},
        {"ikon": "legzes", "cim": "Légzés",
         "szoveg": "A légzés az egyik legegyszerűbb eszköz, amit mindig magaddal viszel. És mégis kevesen használják tudatosan a "
                   "szexualitásban. | Megtanulod azokat az alapvető légzéstechnikákat, amelyek segítségével változtatni tudsz a testi "
                   "állapotodon, mélyítheted a gyönyörérzeteket, és jobban érzékelheted, illetve irányíthatod a benned megjelenő szexuális energiát."},
        {"ikon": "erintes", "cim": "Tudatos érintés",
         "szoveg": "Te is úgy érintesz, hogy közben már azon jár az eszed, hogy hová akarsz eljutni? A tudatos érintésben nincs agyalás. | "
                   "Megtanulod érzékelni az érintést adó kézben és az érintett testben történő változásokat, és úgy érinteni, ahogy ott "
                   "és akkor a legtökéletesebb. Figyelni. | Nem azért érinteni, hogy történjen valami. Hanem azért, hogy **érezd, ami történik.** "
                   "És ettől az érintés minősége egészen más lesz."},
        {"ikon": "izgalom", "cim": "A szexuális izgalom irányítása",
         "szoveg": "A legtöbb férfi két állapotot ismer igazán jól: nincs izgalom – és sok izgalom. Pedig a kettő között rengeteg fokozat van. | "
                   "A tantraszex edzések során megtanulod felismerni az izgalmi állapotod különböző szintjeit, és egyre tudatosabban bánni velük. | "
                   "– Mikor gyorsul fel túlságosan? | – Mitől csillapodik? | – Hogyan tudsz benne maradni egy kellemesen magas izgalmi "
                   "állapotban anélkül, hogy rögtön a végpont felé rohannál? | **Nem elnyomni tanulod az izgalmat. Hanem elbírni egyre többet az élvezetből.**"},
        {"ikon": "szabalyozas", "cim": "Az ejakuláció tudatosabb szabályozása",
         "szoveg": "Az ejakuláció feletti nagyobb kontroll nem pusztán azt jelenti, hogy „tovább bírod”. Ez túl kevés lenne. | "
                   "A cél az, hogy egyre korábban felismerd a tested jelzéseit, és megtanulj tudatosabban bánni az izgalmi állapotoddal. | "
                   "Nem harcolni a testeddel. Nem görcsösen visszatartani valamit. Hanem együttműködni vele, és élvezni az izgalmi energia "
                   "áramlását, hullámzását. | **Megtapasztalod, hogy a magmegtartás nem önmegtartóztatás. Hanem egy képesség, mely újabb "
                   "és újabb kapukat nyit meg a hihetetlen szexuális élmények felé.**"},
    ]})

TARTALOM["tenyek"].update({
    "kicker": "Hat ok", "cim": "Miért érdemes ==megvásárolnod== a tantraszex edzéstervet?",
    "elemek": [
        {"ikon": "izgalom", "szam": "Izgalom", "cim": "Megtanulod kezelni a szexuális izgalmad", "korszoveg": "Tantraszex Edzésterv",
         "szoveg": "Két lehetőség van. Hagyod, hogy a farkad irányítson téged, vagy te irányítod a farkad, és megtanulod kezelni a "
                   "szexuális energiád. Vagy éppen azt a helyzetet, amikor nem jelenik meg az izgalmi energia."},
        {"ikon": "figyelem", "szam": "Figyelem", "cim": "Felhagysz a leggyakoribb hibákkal", "korszoveg": "Tantraszex Edzésterv",
         "szoveg": "Ha fogalmad sincs, hol tart a partnered: | 1. elkezdesz csak a magad folyamatára figyelni, | 2. elkezded kérdezgetni: "
                   "„jó-e neki?”, | 3. elkezdesz valamit elképzelni róla, esetleg hagyod magad becsapni. | Mindhárom óriási hiba, és "
                   "tönkrevágja a szeretkezést, sokszor nem csak egy alkalomra, hanem örökre. | Az edzésprogramban megtanulod érzékelni "
                   "a szexuális energiát nem csak magadban, de a partneredben is. Tudod, hol jársz, és tudod, hol jár a partnered a gyönyör útján."},
        {"ikon": "legzes", "szam": "Biztonság", "cim": "Teljesen biztos leszel a dolgodban", "korszoveg": "Tantraszex Edzésterv",
         "szoveg": "Nem lesz soha többé kétséged, hogy egy randi vagy szeretkezés jól sikerül-e. Elegendő elméleti tudásod és gyakorlati "
                   "tapasztalatod lesz ahhoz, hogy minden szeretkezést művészként megalkoss. | Megtanulod tökéletesen érzékelni magadat és "
                   "a másikat, így biztosan fogod tudni, mi az, ami fokozza a gyönyört, mi az, ami kevésbé, és mi az, ami egyáltalán nem jó "
                   "az adott pillanatban."},
        {"ikon": "erintes", "szam": "Önbizalom", "cim": "Laza, természetes önbizalmad lesz a nőkkel", "korszoveg": "Tantraszex Edzésterv",
         "szoveg": "Minden nő teste máshogy működik. Ha abból indulsz ki, mi működött a korábbi kapcsolataidban, könnyen zsákutcába "
                   "kerülsz. | Ebben az edzésprogramban megtanulsz egy szemléletváltást, ennek köszönhetően csodálatos kísérőjévé válsz "
                   "bármely nőnek, valamennyi partnerednek abban, hogy életük legszebb szexuális élményeit tapasztalják meg."},
        {"ikon": "szabalyozas", "szam": "Élmény", "cim": "Újabb és újabb élményeket szerzel", "korszoveg": "Tantraszex Edzésterv",
         "szoveg": "A tantraszex edzés során elsajátított képességeid lehetővé teszik, hogy felfedezz olyan dolgokat a szexben, "
                   "amelyekről korábban álmodni sem mertél."},
        {"ikon": "homokora", "szam": "Erő", "cim": "Mellékhatások: fiatalság, erő, egészség", "korszoveg": "Tantraszex Edzésterv",
         "szoveg": "A kielégítő, energiamegtartó szex egy egészen új életminőséget is hoz számodra: | Tudatosabb lesz az életed, "
                   "tudatosabb lesz a teremtésed. | Gazdálkodni tudsz az élet-energiáddal, megtapasztalod, hogy az elgyengülés, "
                   "betegség és potencia- vagy libidózavar egyáltalán nem szükségszerű velejárója az évek múlásának."},
    ]})

KINEK.update({
    "is": "Akkor is neked szólhat, ha nincs különösebb „problémád”. Egyszerűen érzed, hogy **ennél több van a szexben**, és "
          "kíváncsi vagy arra, mire képes a tested, ha megtanulsz valóban figyelni rá.",
})

VELEMENYEK.update({
    "kicker": "Vélemények", "cim": "Mások ==így élték meg==",
    "idezetek": [
        "Mikor találkoztam a Tantraszex edzéssel, éreztem – még ha nem is volt rá tapasztalatom –, hogy van realitása annak, hogy "
        "sokkal jobb lehet, ha „nem pukkad ki a lufi”. De arra, amit most magmegtartóként megélek a szexben, legvadabb szexuális "
        "álmomban sem gondoltam volna…",
        "Eleinte egy kicsit sajnáltam az időt a gyakorlásra, mert mindig rengeteg dolgom volt, a gimnázium óta időhiányban szenvedtem. "
        "Durva, hogy a Tantraszex Edzés nem csak a szexualitásomat forradalmasította, de sokkal összeszedettebbé, energikusabbá tett "
        "a munkában, a hétköznapokban is. Egyszer csak azt vettem észre, hogy valahogy több időm van. A 12. héten több mint két óra "
        "elteltével is csak azért hagytam abba a gyakorlást, mert másnap munka volt, és pihenni is kellett.",
        "Volt, hogy a tudatos és irányított légzés óvott meg attól, hogy „átessek”. Jó volt azokat az új érzeteket megtapasztalni. "
        "Előfordult, hogy sikerült a formálódó „energiacsomagot” szétoszlatni az egész medencémben. De nem ért itt véget az élmény! "
        "Két óra alvás után, éjjel felébredtem, és a „határ” alatti érzet még mindig megvolt. Ráadásul olyan intenzíven, hogy "
        "folytatnom kellett a „gyakorlást”. Folyamatosan feszegettem a határokat, közben tanulva a testem jelzéseit, egyre jobban, "
        "sokszor és sűrűbben megtapasztalva a „robbanás előtti kegyelmi pillanatot”.",
        "Egyszerre volt hihetetlen, de ugyanakkor valós, természetes és transzcendentális. Megdöbbentően „Uramisten!” érzés. "
        "Hogy tényleg van ilyen? Ekkora és ennyire elnyújtható élvezet? Pedig még csak a tanulás elején vagyok! És milyen érzés "
        "lesz majd másnak is megadni mindezt!?",
    ],
    "kiemelt": ["legvadabb szexuális álmomban sem gondoltam volna", "valahogy több időm van",
                "a tudatos és irányított légzés", "„Uramisten!” érzés"],
})

TARTALOM["tortenet"].update({
    "kicker": "A Tantraszex Edzésterv megalkotójáról",
    "cim": "Sőregi Zsuzsa (==Kirana==) vagyok, tantraoktató és szexuális önismereti tréner.",
    "bekezdesek": [
        "Az elmúlt évtizedben több ezer férfi és nő bízta rám magát, hogy új dolgokat fedezzen fel a szexualitásában, tantrát, "
        "tantrikus szexualitást tanuljon.",
        "Ezt megelőzően és eközben persze én is tanultam több tantra iskolában, elmentem rengeteg workshopra, jártam szakrális női "
        "körökbe, együtt dolgoztam (a tanulás céljából) szinte valamennyi magyar és több külföldi tantra oktatóval.",
        "Elvégeztem az International School of Temple Arts (nemzetközi szinten a legelismertebb és felkészültebb szexuális "
        "önismereti iskola) Szexuális önismeret 1-2 és Szexuális Gyógyító kurzusait, de talán a legfontosabb a saját út, a saját "
        "tapasztalás: én magam is a Tantra útját járom. Így élek, így szeretek.",
        "Sok mindenre nem tudom a választ, de a tapasztalat, az intuíció és a felülről kért vezetettség segít, hogy úgy kísérjelek, "
        "mentoráljalak az utadon, ahogy Neked jó.",
    ],
    "idezet": "A Tantra nem csupán hivatás számomra, hanem az életem.",
})

TARTALOM["kinalat"].update({
    "lead": "Az edzésterv mellé most ajándékba adjuk neked a következő bónusz anyagokat, amelyek értéke 39.000 Ft.",
})
TARTALOM["kinalat"]["elemek"][0]["leiras"] = "A fizikai gyakorlás kiegészítése mentális gyakorlatokkal egy tökéletesebb és harmonikusabb eredményért."

GARANCIA.update({
    "kicker": "Garanciák", "cim": "Két garancia, ==kockázat nélkül==",
    "lead": "A Tantraszex Edzéstervre kétféle garanciát is vállalunk.",
    "g": [
        {"nev": "1. „Első randi” garancia", "fo": "24 órád van eldönteni, akarsz-e másodikat.", "ido": "24 óra",
         "szoveg": "Van, amikor már az első találkozásnál érzed: **ebből nem lesz szerelem.** A kurzussal sem kell összekötnöd az "
                   "életedet csak azért, mert egyszer igent mondtál rá. | Vásárlás után nézz bele a Tantraszex Edzéstervbe, ismerkedj "
                   "meg a felépítésével, és kezdd el az első gyakorlatot! | Ha elsőre úgy érzed, hogy „Köszönöm, ez nem az én világom”, "
                   "jelezd nekem !!24 órán belül!!, és visszakapod a kurzus árát.",
         "zaro": "Nincs sértődés. Nincs kínos magyarázkodás. | **Nem minden első randiból lesz 12 hetes kapcsolat.**"},
        {"nev": "2. „Izomláz” garancia", "fo": "Ha végigcsináltad az edzést, de semmi hatást nem érzel, visszakapod a pénzed.",
         "ido": "13. hét",
         "szoveg": "A Tantraszex Edzésterv nem attól működik, hogy ott van a gépeden. **Gyakorolni kell.** | Végezd el a 12 hét "
                   "12 gyakorlatát az útmutatás szerint. Ha mindezt becsülettel végigcsináltad, és 12 hét után azt mondod: | "
                   "**„Megcsináltam. De nem érzek érdemi változást.”** | akkor visszaadom a kurzus árát, !!a vásárlás napjától számított "
                   "13. héten!! (nem előbb és nem később).",
         "zaro": "Ha te beleteszed a 12 hetet, én vállalom a garanciát."},
    ],
})

TARTALOM["latogatas"].update({
    "kicker": "Miért most?", "cim": "12 hét múlva mindenképpen ==12 héttel idősebb== leszel.",
    "lead": "A kérdés csak az, hogy közben változik-e valami. | Továbbra is ugyanúgy használhatod a testedet, ahogy az elmúlt "
            "húsz-harminc évben. Vagy adhatsz neki 12 hetet, hogy megtanuljon valami újat. | Nem kell sietned. **De a halogatás is egy döntés.**",
    "cta1": {"szoveg": "Elkezdem a 12 hetes edzéstervet", "href": CSOMAGOK},
})
TARTALOM["latogatas"].pop("cta2", None)

TARTALOM["ajanlat"].pop("lab", None)

# 16. blokk (Miért pont tantra?): az ügyfél által megadott pontos szöveg és sorrend (2026-10-08).
# Csak a gépelési hibák javítva: szóköz a pont után, „….” → „…”, „oda.,” → „oda.”, „magunkat;” → „magunkat:”.
MIERT.update({
    "cim": "Miért pont tantra?", "kicker": None, "lead": None,
    "p1": "A nyugati ember szeret célokat kitűzni. Elindulunk valahonnan, és igyekszünk minél gyorsabban megérkezni.",
    "p2": "**Ezt a gondolkodást bevittük a szexualitásunkba is.**",
    "lanc_sor": "Izgalom. Erekció. Egyre nagyobb izgalom. Orgazmus.",
    "lanc_vege": "Sikerült… Vagy nem sikerült…",
    "fontos": "És minél fontosabbá válik a cél, annál könnyebben történik valami furcsa: | **elfelejtjük érezni azt, ami közben történik.**",
    "kerdes_cim": "Figyelni kezdjük magunkat:",
    "kikoltozik": "A figyelem lassan kiköltözik a testből, és beköltözik a fejbe.",
    "tantra_cim": "**A tantra ennek szinte az ellenkezőjét tanítja.**",
    "tantra": ["Nem azt, hogyan juss gyorsabban a csúcsra.", "Nem is azt, hogy hogyan juttasd a partneredet oda.",
               "Hanem azt, hogy **hogyan maradj benne abban, ami jó.**"],
    "kiemelt": ["A tantrikus szex nem technikával kezdődik", "Hanem figyelemmel."],
    "zaro_sorok": ["Azzal a képességgel, hogy észrevedd, mi történik a testedben.",
                   "Megtanulod felépíteni, megtartani és szabályozni a szexuális izgalmat.",
                   "És közben ott maradni, a testedben, a másik emberrel, a pillanatban.",
                   "**Ezt azonban nem lehet pusztán megérteni.**", "Gyakorolni kell.",
                   "Ezért született meg a **Tantraszex Edzésterv.**"],
})

# ----------------------------------------------------------------------------------------------------
# Egységes blokkcímek (2026-10-08): minden blokk nagy címe a dokumentum fejezetcíme (azonos méret),
# az alcím-mondatok a cím alá kerülnek (lead); a kis felső feliratok (kicker) kikerülnek.
# ----------------------------------------------------------------------------------------------------
ROLASZOL.update({"kicker": None, "cim": "Miről szól a ==tantraszex edzésterv==?",
                 "lead": "**Nem azt tanulod újra, amit már harminc (vagy több) éve csinálsz. Olyan képességeket edzünk, "
                         "amelyeket valószínűleg soha senki nem tanított meg neked.**"})
MIERT.update({"cim": "Miért pont ==tantra==?"})
MIA.update({"kicker": None})
TARTALOM["folyamat"].update({"kicker": None})
TARTALOM["tenyek"].update({"kicker": None})
TARTALOM["tortenet"].update({"kicker": None, "cim": "A Tantraszex Edzésterv ==megalkotójáról=="})
TARTALOM["tortenet"]["bekezdesek"] = (["**Sőregi Zsuzsa (Kirana) vagyok, tantraoktató és szexuális önismereti tréner.**"]
                                      + [b for b in TARTALOM["tortenet"]["bekezdesek"] if not b.startswith("**Sőregi")])
KINEK.update({"kicker": None, "cim": "Kinek szól a ==Tantraszex Edzésterv==?", "lead": "Neked szól, ha 45 feletti férfiként:"})
VELEMENYEK.update({"kicker": None, "cim": "Mások ==így élték meg=="})
TARTALOM["kinalat"].update({"kicker": None, "cim": "Ajándékok"})
GARANCIA.update({"kicker": None, "cim": "Garanciák"})
TARTALOM["latogatas"].update({"kicker": None, "cim": "Miért ==most==?",
                              "lead": "**12 hét múlva mindenképpen 12 héttel idősebb leszel.** | " + TARTALOM["latogatas"]["lead"]})
TARTALOM["ajanlat"].update({"kicker": None, "cim": "Csomagok"})
GYIK.update({"kicker": None, "cim": "Gyakran Intézett ==Kérdések=="})

# GYIK (az ügyfél szövege, 2026-10-09), elírás-javítással. A " | " sortörés.
TELEFON = "+36 70 245 4969"
GYIK["k"] = [
    ["Mi történik, miután kitöltöttem a megrendelőlapot?",
     "Töltsd ki a megrendelőlapot, és küldd el! | Azonnal kapsz egy e-mailt a bankszámla-adatokkal, ahova el tudod utalni a "
     "kurzus árát. | Ha nem találod az e-mailt, nézd meg a SPAM és PROMÓCIÓK mappában is! | Amikor beérkezik a bankszámlánkra "
     "az átutalt összeg, egy-két órán belül elküldöm neked a kurzushoz való hozzáférés adatait, a kurzusfiókod felhasználónevét "
     "és jelszavát. | A fiókodba belépve megtalálod a Tantraszex Edzéstervet, és a bónuszt is. | Ha Prémium csomagot rendeltél, "
     "telefonon kereslek a személyes alkalmak időpontjának egyeztetése céljából. (Ezért ebben az esetben kötelező a telefonszám "
     "megadása a megrendelőlapon.) | **Ha bármi nem így történik, bátran hívj!** " + TELEFON],
    ["Kapok számlát?",
     "A megrendelőűrlap elküldése után kapsz egy díjbekérőt, az átutalás után pedig számlát (a szamlazz.hu rendszerén keresztül). | "
     "Számlát csak magánszemélyek részére tudunk kiállítani, ezért csak magánszemélyként tudod a kurzust megrendelni."],
    ["Mit tud nekem újat mondani a szexről ennyi idős koromban?",
     "Ebben a kurzusban nem azt tanulod újra, amit már harminc (vagy több) éve csinálsz. Olyan képességeket edzünk, amelyeket "
     "valószínűleg soha senki nem tanított meg neked. | Nem a „régi” szexről tanulsz új dolgokat, hanem egy teljesen új "
     "szexualitásba kapsz bevezetést."],
    ["Akkor is működik, ha nem vagyok „spiri”?",
     "Az eredmény kizárólag azon múlik, hogy végigcsinálod-e a gyakorlatokat. | Az persze fontos, hogy nyitottan és lelkesen állj "
     "hozzá. És legyél nyitott arra is, hogy ha valami különleges dolgot tapasztalsz meg, ne utasítsd el rögtön, csak azért, mert "
     "nem logikus, nem racionális… Légy nyitott az új dolgok felfedezésére!"],
    ["Egyedül hogyan gyakoroljak szexet?",
     "Nem kell megvárnod a következő kapcsolatodat ahhoz, hogy más férfiként érkezz bele. Egy olyan tudással, mely a legtöbb nő "
     "számára „kincset ér”. | A Tantraszex Edzés kifejezetten egyedül végezhető gyakorlatokat tartalmaz. | A gyakorlás során nagy "
     "valószínűséggel sokszorosára nő a szexuális vonzerőd, ami segíteni fog abban, hogy találj egy csodálatos partnert új "
     "szexualitásod megéléséhez."],
    ["Mi van, ha elkezdem, aztán nem csinálom?",
     "Nem kell megtanulnod a tantrát. Egy héten csak egy gyakorlatot kell elvégezned. Ami már megy, azt nem fogod elfelejteni, "
     "olyan, mint a biciklizés… | A kurzusfiókod hónapok múlva is elérhető: ha valami miatt szünetelteted az edzést, később "
     "újra előveheted."],
]
# az oldal elérhetősége: a GYIK-ben megadott telefonszám (a hiányzó e-mail helyett)
TARTALOM["kapcsolat"].pop("email", None)
TARTALOM["kapcsolat"]["telefon"] = TELEFON
# e-mail (az ügyfél megerősítette)
TARTALOM["kapcsolat"]["email"] = "tantraiskola@gmail.com"
# az ügyfél kérése: az oldal elérhetősége az e-mail legyen (a telefonszám csak a GYIK 1. válaszában marad)
TARTALOM["kapcsolat"].pop("telefon", None)

# Impresszum (az ügyfél adatai, 2026-10-09). A felugró ablakot a gen/utofeldolgozas.py teszi az oldalra.
IMPRESSZUM = {
    "szolgaltato": [["Szolgáltató", "Sőregi Zsuzsanna egyéni vállalkozó"],
                    ["Székhely", "2051 Biatorbágy, Szabadság út 61."],
                    ["Adószám", "48375746-1-33"],
                    ["Nyilvántartási szám", "[pótolandó: egyéni vállalkozói nyilvántartási szám]"],
                    ["E-mail", "tantraiskola@gmail.com"],
                    ["Telefon", "+36 70 245 4969"]],
    "tarhely": [["Tárhelyszolgáltató", "Hostinger International Ltd."],
                ["Cím", "61 Lordou Vironos Street, 6023 Larnaca, Ciprus"],
                ["E-mail", "domains@hostinger.com"],
                ["Web", "www.hostinger.com"]],
}
TARTALOM["lablec"]["jogi"] = [["Impresszum", "#impresszum"]]
ADATKEZELES = "https://www.tantraiskola.hu/privacy-policy"
TARTALOM["lablec"]["jogi"] = [["Impresszum", "#impresszum"], ["Adatkezelési tájékoztató", ADATKEZELES]]
ASZF = "https://www.tantraiskola.hu/aszf"
TARTALOM["lablec"]["jogi"] = [["Impresszum", "#impresszum"], ["ÁSZF", ASZF], ["Adatkezelési tájékoztató", ADATKEZELES]]

# 2026-10-09: az ügyfél adószámos magánszemély (nincs EV-nyilvántartási szám); e-mail megerősítve;
# a hero „Megnézem, hogy működik” gombja a „Mit edzünk 12 héten keresztül?” blokkra visz.
IMPRESSZUM["szolgaltato"] = [["Szolgáltató", "Sőregi Zsuzsanna (adószámos magánszemély)"],
                             ["Székhely", "2051 Biatorbágy, Szabadság út 61."],
                             ["Adószám", "48375746-1-33"],
                             ["E-mail", "tantraiskola@gmail.com"],
                             ["Telefon", "+36 70 245 4969"]]
TARTALOM["hero"]["cta1"] = {"szoveg": "Megnézem, hogy működik", "href": "#folyamat"}
