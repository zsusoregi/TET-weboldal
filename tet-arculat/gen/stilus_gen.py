# -*- coding: utf-8 -*-
"""Tantraszex Edzésterv: a globális stílus-opciók (5 karakter + a téma: jantra, lótusz, lélegzet, láng, homokóra)."""
import math, sys
sys.path.insert(0, "/root/.claude/skills/synced/2ef019ad-994b-4a29-ba20-0f4f0fc9c379_12065cb9-5571-428e-a25a-37502384cf98/webdesign-arculat-generator/scripts")
from motor.alap import svg_uri
from motor.stilusok import ZAJ, u


def U(svg):
    return 'url("' + svg_uri(svg).replace('"', "'") + '")'


def S(belso, vb="0 0 100 100", extra=""):
    return f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{vb}' {extra}>{belso}</svg>"


JANTRA = U(S("<g fill='none' stroke='#000' stroke-width='3' stroke-linejoin='round'><circle cx='50' cy='50' r='44'/>"
             "<circle cx='50' cy='50' r='37'/><path d='M50 83 L20 32 H80Z M50 34 L66 62 H34Z'/></g><circle cx='50' cy='53' r='4'/>"))
HOMOKORA = U(S("<path d='M22 8H78V18C78 36 60 42 57 50 60 58 78 64 78 82V92H22V82C22 64 40 58 43 50 40 42 22 36 22 18Z' "
               "fill='none' stroke='#000' stroke-width='6' stroke-linejoin='round'/><path d='M36 84H64L50 66Z'/>"))
LOTUSZ = U(S("<path d='M50 14C63 32 63 56 50 74 37 56 37 32 50 14Z'/><path d='M47 74C38 58 22 50 6 50 12 68 30 78 47 74Z'/>"
             "<path d='M53 74C62 58 78 50 94 50 88 68 70 78 53 74Z'/>"))

# ---------------------------------------------------------------- textúra-csempék (Pythonból számolva)


def jantra_csempe():
    return U(S("<g fill='none' stroke='#000' stroke-width='1.4' stroke-linejoin='round'>"
               "<circle cx='60' cy='60' r='44'/><path d='M60 99 L26 40 H94Z M60 42 L79 75 H41Z'/></g><circle cx='60' cy='64' r='3'/><g fill='none' stroke='#000' stroke-width='1.4'>"
               "<path d='M0 0h20M0 0v20M120 120h-20M120 120v-20M120 0h-20M120 0v20M0 120h20M0 120v-20'/></g>", "0 0 120 120"))


def hullam_csempe():
    def vonal(y, fazis):
        pts = []
        for i in range(0, 241, 6):
            pts.append(f"{i},{y + 7 * math.sin((i / 240) * 2 * math.pi + fazis):.2f}")
        return "<polyline fill='none' stroke='#000' stroke-width='1.5' points='" + " ".join(pts) + "'/>"
    return U(S(vonal(12, 0) + vonal(36, math.pi / 1.6), "0 0 240 48"))


def naplo_csempe():
    """12 × 12 pöttyrács: 12 hét, 12 gyakorlat. Az átló kitöltve: a haladás."""
    g = []
    for r in range(12):
        for c in range(12):
            x, y = 11 + c * 22, 11 + r * 22
            if c == r:
                g.append(f"<circle cx='{x}' cy='{y}' r='4.2'/>")
            else:
                g.append(f"<circle cx='{x}' cy='{y}' r='3' fill='none' stroke='#000' stroke-width='1.1'/>")
    return U(S("".join(g), "0 0 264 264"))


def lotusz_csempe():
    def l(x, y, s):
        return (f"<g transform='translate({x} {y}) scale({s}) translate(-50 -50)'><path d='M50 14C63 32 63 56 50 74 37 56 37 32 50 14Z'/>"
                "<path d='M47 74C38 58 22 50 6 50 12 68 30 78 47 74Z'/><path d='M53 74C62 58 78 50 94 50 88 68 70 78 53 74Z'/></g>")
    return U(S(l(30, 28, .34) + l(90, 80, .34) + "<circle cx='90' cy='26' r='2'/><circle cx='30' cy='80' r='2'/>", "0 0 120 104"))


def hullam_hatar():
    pts = [f"{i},{30 + 16 * math.sin(i / 1440 * 4 * math.pi):.1f}" for i in range(0, 1441, 20)]
    return U(S("<path d='M" + " L".join(pts) + " V60 H0Z'/>", "0 0 1440 60", "preserveAspectRatio='none'"))


IZGALOM = U(S("<path d='M0 84 C180 84 300 36 470 30 S620 44 700 32 S840 18 930 30 S1080 44 1170 30 S1350 24 1440 34 V90 H0Z'/>",
              "0 0 1440 90", "preserveAspectRatio='none'"))
SZIROM = U(S("<path d='M0 22 Q14 21 24 2 Q34 21 48 22Z'/>", "0 0 48 22", "preserveAspectRatio='none'"))
HULLAMVONAL = U(S("<path d='M2 12 C14 2 26 2 38 12 S62 22 74 12 S98 2 110 12' fill='none' stroke='#000' stroke-width='4' stroke-linecap='round'/>",
                  "0 0 112 24"))

# ---------------------------------------------------------------- kategóriák

CIM = [
    dict(id="cE", nev="Dőlt gyertyafény", leiras="A kulcsszó dőlt, vékonyabb, márkaszínű: suttogva hangsúlyoz. Elegáns, érzéki.",
         css="%S mark{font-style:italic;font-weight:400;color:var(--hl);letter-spacing:0}"),
    dict(id="cM", nev="Energia-vonal", leiras="Vékony, narancsból borostyánba futó vonal a szó alatt, görgetésre végigfut, mint az energia. Modern.",
         css="%S mark{color:var(--c-head);background:linear-gradient(90deg,var(--c-primary),var(--c-accent)) 0 92%/100% .09em no-repeat;padding-bottom:.04em;transition:background-size 1.2s var(--ease-out) .2s;-webkit-box-decoration-break:clone;box-decoration-break:clone}"
             "%S.js-rv [data-rv]:not(.in) mark{background-size:0 .09em}"),
    dict(id="cB", nev="Láng-blokk", leiras="Telt kiemelő-színű sáv a szó mögött, kicsit megdöntve, mint egy edzésterv kiemelése. Merész, plakátos.",
         css="%S mark{background:linear-gradient(-2deg,transparent 8%,var(--c-primary) 8%,var(--c-primary) 92%,transparent 92%);color:var(--c-on-primary);padding:0 .14em;-webkit-box-decoration-break:clone;box-decoration-break:clone}"
             "%S .s-primary mark,%S .s-deep mark{background:linear-gradient(-2deg,transparent 8%,var(--c-accent) 8%,var(--c-accent) 92%,transparent 92%);color:var(--c-on-accent)}"),
    dict(id="cF", nev="Kézírás lélegzet-hullámmal", leiras="A kulcsszó kézírással, alatta egy lágy, lélegző hullámvonal. Barátságos, személyes.",
         css="%S mark{font-family:var(--f-hand);font-weight:400;color:var(--hl);font-size:calc(var(--fs-hand)*.92em);letter-spacing:0;text-transform:none;display:inline-block;transform:rotate(-2deg);line-height:1;padding:0 .05em .18em;"
             "background:linear-gradient(var(--c-accent),var(--c-accent)) 50% 100%/100% .2em no-repeat;-webkit-mask:linear-gradient(#000,#000) 0 0/100% calc(100% - .22em) no-repeat," + HULLAMVONAL + " 50% 100%/100% .22em no-repeat;"
             "mask:linear-gradient(#000,#000) 0 0/100% calc(100% - .22em) no-repeat," + HULLAMVONAL + " 50% 100%/100% .22em no-repeat}"),
    dict(id="cK", nev="Kettős aláhúzás", leiras="Két vékony vonal a kulcsszó alatt, mint egy aláírt oklevélen. Klasszikus, megbízható.",
         css="%S mark{color:var(--c-head);text-decoration:underline double var(--c-accent);text-decoration-thickness:.045em;text-underline-offset:.2em;text-decoration-skip-ink:none}"),
]

ALCIM = [
    dict(id="kE", nev="Hajszálvonal jantra-jellel", leiras="Ritkított nagybetűs címke két hajszálvonal között, középen apró jantra. Elegáns, rendezett.",
         css="%S .kick{display:flex;align-items:center;justify-content:center;gap:12px;font-family:var(--f-body);font-weight:700;font-size:.74rem;letter-spacing:.24em;text-transform:uppercase;color:var(--hl)}"
             "%S .kick::before,%S .kick::after{content:\"\";width:38px;height:1px;background:currentColor;opacity:.6;flex:none}"
             "%S .kick span::before{content:\"\";display:inline-block;width:14px;height:14px;margin-right:10px;vertical-align:-2px;background:currentColor;-webkit-mask:" + JANTRA + " center/contain no-repeat;mask:" + JANTRA + " center/contain no-repeat}"
             "%S .bal .kick{justify-content:flex-start}%S .bal .kick::before{display:none}"),
    dict(id="kM", nev="Lélegző kapszula", leiras="Halvány kapszula, benne egy pötty, ami lassan „lélegzik” (4 mp be, 6 mp ki). Modern, élő.",
         css="%S .kick{display:inline-flex;align-items:center;gap:10px;padding:7px 15px 7px 12px;border-radius:999px;background:var(--c-primary-ll);color:var(--c-primary-d);font-weight:700;font-size:.74rem;letter-spacing:.12em;text-transform:uppercase}"
             "%S .kick::before{content:\"\";width:8px;height:8px;border-radius:50%;background:var(--c-primary);flex:none;animation:%Klegz 10s ease-in-out infinite}"
             "@keyframes %Klegz{0%,100%{box-shadow:0 0 0 2px color-mix(in srgb,var(--c-primary) 20%,transparent)}40%{box-shadow:0 0 0 7px color-mix(in srgb,var(--c-primary) 14%,transparent)}}"
             "%S .s-deep .kick{background:rgba(255,255,255,.08);color:var(--c-deep-hl)}%S .s-primary .kick{background:color-mix(in srgb,var(--c-on-primary) 15%,transparent);color:var(--c-on-primary)}"),
    dict(id="kB", nev="Edzésterv-címke", leiras="Sötét, szögletes címke mono betűvel és narancs blokkal, mint egy edzésnapló fejléce. Merész, sportos.",
         css="%S .kick{display:inline-flex;align-items:stretch;gap:0;padding:0;background:var(--c-ink);color:var(--c-paper);font-family:var(--f-label);font-weight:600;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;border-radius:3px;overflow:hidden}"
             "%S .kick::before{content:\"\";width:10px;background:var(--c-primary);flex:none}%S .kick span{padding:7px 12px}"
             "%S .s-deep .kick{background:var(--c-on-deep);color:var(--c-deep)}%S .s-primary .kick{background:var(--c-on-primary);color:var(--c-primary-d)}%S .s-primary .kick::before{background:var(--c-accent)}"),
    dict(id="kF", nev="Kézírás lótusszal", leiras="Kézzel írt felvezető, előtte egy kis lótusz. Mintha Kirana írná a margóra. Barátságos, személyes.",
         css="%S .kick{display:inline-flex;align-items:center;gap:8px;font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.15rem);font-weight:400;letter-spacing:0;text-transform:none;color:var(--c-hand);line-height:1.1}"
             "%S .kick::before{content:\"\";width:26px;height:26px;flex:none;background:var(--c-primary);-webkit-mask:" + LOTUSZ + " center/contain no-repeat;mask:" + LOTUSZ + " center/contain no-repeat}"
             "%S .s-deep .kick{color:var(--c-deep-hl)}%S .s-primary .kick{color:var(--c-primary-hl)}%S .s-primary .kick::before{background:var(--c-on-primary)}"),
    dict(id="kK", nev="Sorszámozott fejezetek", leiras="Minden szekció kap egy sorszámot (01, 02…) serif számmal és vékony vonallal, mint egy tankönyv fejezetei. Klasszikus.",
         css="%S .kick{display:flex;align-items:center;justify-content:center;gap:12px;font-family:var(--f-label);font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-2);font-weight:600}"
             "%S .shead .kick::before{content:attr(data-n);font-family:var(--f-display);font-size:1.7rem;letter-spacing:0;color:var(--hl);font-weight:var(--w-display);line-height:1;font-style:italic}"
             "%S .kick::after{content:\"\";width:52px;height:1px;background:var(--c-line2)}%S .bal .kick{justify-content:flex-start}"),
]

GOMB = [
    dict(id="gE", nev="Szögletes, belső éllel", leiras="Szögletes, ritkított nagybetűs gomb vékony belső fénycsíkkal; a másodlagos egy hajszálkeretes változat. Elegáns, prémium.",
         css="%S .btn{padding:1.1em 1.9em;border-radius:2px;background:var(--b-bg);color:var(--b-ink);font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--b-ink) 0%,transparent);outline:1px solid color-mix(in srgb,var(--b-ink) 45%,transparent);outline-offset:-5px;transition:background .3s,outline-offset .3s}"
             "%S .btn:hover{background:color-mix(in srgb,var(--b-bg),#000 14%);outline-offset:-8px}"
             "%S .btn.alt{background:transparent;color:var(--c-head);outline:1px solid var(--c-line2);outline-offset:0}%S .btn.alt:hover{outline-color:var(--c-head);outline-offset:-4px;background:transparent}"),
    dict(id="gM", nev="Lekerekített, nyíl-dobozzal", leiras="Enyhén lekerekített, lapos gomb, a nyíl egy borostyán dobozban, ami rámutatva előreugrik. Tiszta, modern.",
         css="%S .btn{padding:.58em .6em .58em 1.35em;border-radius:14px;background:var(--b-bg);color:var(--b-ink);transition:background .2s var(--ease)}"
             "%S .btn:not(:has(.ui)){padding:.95em 1.5em}"
             "%S .btn .ui{width:2.1em;height:2.1em;padding:.5em;border-radius:10px;background:var(--c-accent);color:var(--c-on-accent);transition:transform .25s var(--ease)}"
             "%S .btn:hover .ui{transform:translateX(4px)}%S .btn:hover{background:color-mix(in srgb,var(--b-bg),#000 10%)}"
             "%S .btn.alt{background:transparent;color:var(--c-head);box-shadow:inset 0 0 0 2px var(--c-line2)}%S .btn.alt .ui{background:var(--c-tint);color:var(--c-head)}"),
    dict(id="gB", nev="Lángoló kapszula", leiras="Telt narancs kapszula „talppal” és meleg, lángszerű derengéssel; rámutatva felizzik. A legkattinthatóbb, merész.",
         css="%S .btn{padding:1.08em 1.9em;border-radius:999px;background:radial-gradient(120% 140% at 50% 0%,color-mix(in srgb,var(--b-bg),#fff 22%),var(--b-bg) 55%);color:var(--b-ink);box-shadow:0 5px 0 var(--b-deep),0 16px 34px -12px color-mix(in srgb,var(--c-accent) 85%,transparent);transition:transform .15s var(--ease),box-shadow .25s}"
             "%S .btn:hover{transform:translateY(-2px);box-shadow:0 7px 0 var(--b-deep),0 22px 46px -10px var(--c-accent)}"
             "%S .btn:active{transform:translateY(4px);box-shadow:0 1px 0 var(--b-deep)}"
             "%S .btn.alt{background:var(--balt-bg);color:var(--balt-ink);box-shadow:0 5px 0 var(--c-line2),0 14px 24px -16px rgba(0,0,0,.35)}%S .btn.alt:hover{box-shadow:0 7px 0 var(--c-line2)}"),
    dict(id="gF", nev="Puha, lélegző fény", leiras="Kerek, puha gomb, körülötte halvány fénygyűrű, ami lassan lélegzik. Barátságos, hívogató, nem nyomul.",
         css="%S .btn{padding:1em 1.8em;border-radius:999px;background:var(--b-bg);color:var(--b-ink);box-shadow:0 0 0 0 color-mix(in srgb,var(--b-bg) 40%,transparent),0 12px 26px -14px var(--b-bg);animation:%Kfeny 10s ease-in-out infinite;transition:transform .3s var(--ease)}"
             "%S .btn:hover{transform:scale(1.03)}"
             "@keyframes %Kfeny{0%,100%{box-shadow:0 0 0 0 color-mix(in srgb,var(--b-bg) 30%,transparent),0 12px 26px -14px var(--b-bg)}40%{box-shadow:0 0 0 9px color-mix(in srgb,var(--b-bg) 0%,transparent),0 12px 26px -14px var(--b-bg)}}"
             "%S .btn.alt{animation:none;background:var(--c-tint);color:var(--c-head);box-shadow:none}%S .s-deep .btn.alt,%S .s-primary .btn.alt{background:color-mix(in srgb,var(--c-ink) 12%,transparent);color:var(--c-ink)}"),
    dict(id="gK", nev="Kettős keret, serif", leiras="Kettős keretes gomb címbetűvel, mint egy oklevél vagy meghívó. Klasszikus, méltóságteljes.",
         css="%S .btn{padding:.95em 1.7em;border-radius:6px;background:var(--b-bg);color:var(--b-ink);font-family:var(--f-display);font-weight:var(--w-display);font-size:1.06rem;letter-spacing:.01em;text-transform:none;box-shadow:0 0 0 3px var(--sec-bg,var(--c-paper)),0 0 0 4px var(--b-bg);transition:box-shadow .25s,background .25s}"
             "%S .btn:hover{box-shadow:0 0 0 5px var(--sec-bg,var(--c-paper)),0 0 0 6px var(--b-bg)}"
             "%S .btn.alt{background:transparent;color:var(--c-head);box-shadow:inset 0 0 0 1px var(--c-head)}%S .btn.alt:hover{box-shadow:inset 0 0 0 1px var(--c-head),0 0 0 4px var(--sec-bg,var(--c-paper)),0 0 0 5px var(--c-head)}"),
]

KARTYA = [
    dict(id="rE", nev="Belső keret jantra-sarokkal", leiras="Fehér kártya vékony belső kerettel, a sarokban halvány jantra-jel. Elegáns, nyugodt.",
         css="%S .krt{--kp:28px;padding:var(--kp);background:var(--c-card);border-radius:4px;outline:1px solid var(--c-line2);outline-offset:-9px;box-shadow:var(--sh-1);overflow:hidden}"
             "%S .krt::after{content:\"\";position:absolute;right:-18px;top:-18px;width:86px;height:86px;background:var(--c-primary);opacity:.09;-webkit-mask:" + JANTRA + " center/contain no-repeat;mask:" + JANTRA + " center/contain no-repeat;pointer-events:none}"),
    dict(id="rM", nev="Energia-sáv", leiras="Tiszta kártya, tetején narancsból borostyánba futó vékony sáv, rámutatva megemelkedik. Modern, rendezett.",
         css="%S .krt{--kp:26px;padding:var(--kp);background:var(--c-card);border-radius:18px;box-shadow:var(--sh-2);overflow:hidden;transition:transform .3s var(--ease),box-shadow .3s}"
             "%S .krt::before{content:\"\";position:absolute;left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,var(--c-primary),var(--c-accent));z-index:3}"
             "%S .krt:hover{transform:translateY(-4px);box-shadow:var(--sh-3)}"),
    dict(id="rB", nev="Kemény árnyék", leiras="Vastag tintakeret, narancs eltolt árnyék, ikon színes dobozban. Határozott, edzőtermi.",
         css="%S .krt{--kp:24px;padding:var(--kp);background:var(--c-card);border:2px solid var(--c-ink);border-radius:10px;box-shadow:6px 6px 0 var(--c-primary);transition:transform .15s,box-shadow .15s;overflow:hidden}"
             "%S .krt:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--c-primary)}"
             "%S .krt .krt-fej .ik{--ik:54px;background-color:var(--c-accent-l);border:2px solid var(--c-ink);border-radius:10px}%S .krt>.krt-kep{border-bottom:2px solid var(--c-ink)}"),
    dict(id="rF", nev="Puha, meleg", leiras="Halvány barackszínű kártya keret nélkül, nagy lekerekítéssel, ikon fehér körben. Barátságos, ölelő.",
         css="%S .krt{--kp:26px;padding:var(--kp);background:var(--c-tint);border-radius:28px;transition:background .3s,transform .3s var(--ease);overflow:hidden}"
             "%S .krt .krt-fej .ik{--ik:60px;background-color:var(--c-card);border-radius:50%;box-shadow:var(--sh-2)}"
             "%S .krt:hover{background:var(--c-primary-ll);transform:translateY(-3px)}%S .s-tint .krt{background:var(--c-card)}"),
    dict(id="rK", nev="Edzésnapló-lap", leiras="Vonalas naplólap margóval, a sarokban kis „pipa” mező. Az edzésterv metaforája: minden kártya egy bejegyzés. Klasszikus, egyedi.",
         css="%S .krt{--kp:24px;--kpl:46px;padding:var(--kp) var(--kp) var(--kp) var(--kpl);background-color:var(--c-card);border:1px solid var(--c-line);border-radius:4px;box-shadow:var(--sh-2);overflow:hidden;background-image:repeating-linear-gradient(180deg,transparent 0 29px,color-mix(in srgb,var(--c-primary) 8%,transparent) 29px 30px);background-position:0 16px}"
             "%S .krt::before{content:\"\";position:absolute;left:26px;top:0;bottom:0;width:0;border-left:1.5px solid color-mix(in srgb,var(--c-primary) 45%,transparent);z-index:1}"
             "%S .krt::after{content:\"\";position:absolute;right:14px;top:14px;width:16px;height:16px;border:1.5px solid var(--c-primary);border-radius:3px;opacity:.6}"
             "%S .krt>.krt-kep{margin-left:calc(-1*var(--kpl))}"),
]

FOTO = [
    dict(id="fE", nev="Gyertyafény-derengés", leiras="Nagy lekerekítés, mély árnyék és meleg narancs fény a fotó mögött, mintha gyertya világítaná. Elegáns, intim.",
         css="%S .ft .ph{border-radius:20px;box-shadow:0 30px 60px -28px color-mix(in srgb,var(--c-primary) 70%,transparent),var(--sh-2)}%S .ft.krt-kep .ph{border-radius:0;box-shadow:none}"),
    dict(id="fM", nev="Eltolt kontúr", leiras="Lekerekített fotó, mögötte eltolt borostyán vonalkeret. Grafikus, rendezett, modern.",
         css="%S .ft .ph{border-radius:16px}%S .ft::before{content:\"\";position:absolute;inset:0 0 auto 0;aspect-ratio:var(--ar,4/3);border:2px solid var(--c-accent);border-radius:20px;transform:translate(12px,12px);z-index:-1}"
             "%S .ft.krt-kep::before{display:none}%S .ft.krt-kep .ph{border-radius:0}"),
    dict(id="fB", nev="Narancs színblokk", leiras="A fotó mögött egy elforgatott, telt narancs blokk. Merész, plakátos, rétegzett.",
         css="%S .ft .ph{border-radius:6px}%S .ft::before{content:\"\";position:absolute;inset:0 0 auto 0;aspect-ratio:var(--ar,4/3);border-radius:6px;background:var(--c-primary);transform:translate(-14px,14px) rotate(-3deg);z-index:-1}"
             "%S .ft.krt-kep::before{display:none}%S .ft.krt-kep .ph{border-radius:0}"),
    dict(id="fF", nev="Templomkapu-ív", leiras="Felül íves, alul lekerekített forma, mint egy templom kapuja vagy ablaka. Barátságos, meleg, kicsit szakrális.",
         css="%S .ft .ph{border-radius:999px 999px 22px 22px}%S .ft.krt-kep .ph{border-radius:0}"),
    dict(id="fK", nev="Paszpartu", leiras="Fehér paszpartu vékony belső vonallal, mint egy bekeretezett fotó. Klasszikus, nyugodt.",
         css="%S .ft{background:var(--c0-card,#fff);padding:12px;box-shadow:var(--sh-2);border-radius:2px}%S .ft .ph{outline:1px solid rgba(0,0,0,.18);outline-offset:4px}"
             "%S .ft figcaption{text-align:center;font-family:var(--f-label);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:#6b5b50}"
             "%S .ft.krt-kep{background:none;padding:0;box-shadow:none}%S .ft.krt-kep .ph{outline:0}"),
]

FELULET = [
    dict(id="tJ", nev="Jantra-rács", leiras="Halvány, ismétlődő jantra: kör és két egymásba fordított háromszög, finom vonalakkal. A tantra legismertebb jele, szinte észrevétlenül.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + jantra_csempe() + " 0 0/150px 150px repeat;mask:" + jantra_csempe() + " 0 0/150px 150px repeat;opacity:.07}"
             "%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.1}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.12}"),
    dict(id="tL", nev="Lélegzet-hullámok", leiras="Vízszintes, lágy hullámvonalak, mint a ki- és belégzés ritmusa. Nyugodt, élő, a légzés-gyakorlatokat idézi.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + hullam_csempe() + " 0 0/240px 48px repeat;mask:" + hullam_csempe() + " 0 0/240px 48px repeat;opacity:.13}"
             "%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.15}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.15}"),
    dict(id="tN", nev="12 hetes edzésnapló", leiras="12 × 12 karikából álló rács, az átlón kitöltött pöttyökkel: 12 hét, 12 gyakorlat, a haladás. Az edzésterv saját mintája.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + naplo_csempe() + " 0 0/264px 264px repeat;mask:" + naplo_csempe() + " 0 0/264px 264px repeat;opacity:.13}"
             "%S .s-deep.tx::before,%S .s-primary.tx::before{background-color:#fff;opacity:.1}"),
    dict(id="tK", nev="Rezgő körök", leiras="Egy sarokból kiinduló koncentrikus körök, mint a hang vagy az energia rezgése. Finom, mély, meditatív.",
         css="%S .tx::before{background:repeating-radial-gradient(circle at 88% 10%,transparent 0 30px,color-mix(in srgb,var(--c-primary) 26%,transparent) 30px 31.5px);-webkit-mask-image:radial-gradient(circle at 88% 10%,#000 0,transparent 62%);mask-image:radial-gradient(circle at 88% 10%,#000 0,transparent 62%);opacity:.8}"
             "%S .sec:nth-of-type(even).tx::before{background:repeating-radial-gradient(circle at 8% 92%,transparent 0 30px,color-mix(in srgb,var(--c-primary) 26%,transparent) 30px 31.5px);-webkit-mask-image:radial-gradient(circle at 8% 92%,#000 0,transparent 60%);mask-image:radial-gradient(circle at 8% 92%,#000 0,transparent 60%)}"
             "%S .s-deep.tx::before{filter:brightness(1.8)}"),
    dict(id="tO", nev="Lótuszminta", leiras="Apró, szórt lótuszvirágok halvány mintája, mint egy finom textil. Barátságos, meleg, nőies-férfias egyensúly.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + lotusz_csempe() + " 0 0/120px 104px repeat;mask:" + lotusz_csempe() + " 0 0/120px 104px repeat;opacity:.08}"
             "%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.1}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.12}"),
]

DEKOR = [
    dict(id="dJ", nev="Lassan forgó jantra", leiras="Óriás, halvány jantra a szekciók sarkában, ami nagyon lassan forog. Nyugodt, méltóságteljes márkajel.",
         css="%S .dk-jel{display:block;width:clamp(240px,38cqi,500px);aspect-ratio:1;right:-9%;top:-12%;background:var(--c-primary);-webkit-mask:" + JANTRA + " center/contain no-repeat;mask:" + JANTRA + " center/contain no-repeat;opacity:.1;animation:%Kforog 180s linear infinite}"
             "%S .sec:nth-of-type(even) .dk-jel{right:auto;left:-10%;top:auto;bottom:-14%;animation-direction:reverse}"
             "%S .s-deep .dk-jel{background:var(--c-deep-hl);opacity:.13}%S .s-primary .dk-jel{background:var(--c-on-primary);opacity:.14}"
             "@keyframes %Kforog{to{transform:rotate(360deg)}}"),
    dict(id="dL", nev="Lélegző kör", leiras="Koncentrikus fénykör a sarokban, ami a légzés ritmusában tágul és szűkül (4 mp be, 6 mp ki). Lélegezz vele együtt.",
         css="%S .dk-r{display:block;width:clamp(200px,30cqi,380px);aspect-ratio:1;border-radius:50%;right:3%;top:6%;background:repeating-radial-gradient(circle,color-mix(in srgb,var(--c-accent) 30%,transparent) 0 1.5px,transparent 1.5px 22px),radial-gradient(circle,color-mix(in srgb,var(--c-accent) 26%,transparent),transparent 68%);-webkit-mask:radial-gradient(circle,#000 30%,transparent 70%);mask:radial-gradient(circle,#000 30%,transparent 70%);animation:%Klegz 10s ease-in-out infinite}"
             "%S .sec:nth-of-type(even) .dk-r{right:auto;left:2%;top:auto;bottom:6%}"
             "@keyframes %Klegz{0%,100%{transform:scale(.82);opacity:.55}40%{transform:scale(1.06);opacity:1}}"),
    dict(id="dP", nev="Energia-pontok", leiras="Függőleges vonal hét fénylő ponttal a szekció szélén: az energia útja a testben. Lassan felfelé fut rajta a fény.",
         css="%S .dk-f2{display:block;left:clamp(10px,2.4cqi,36px);top:14%;bottom:14%;width:16px;background:radial-gradient(circle,var(--c-accent) 3.5px,transparent 4.5px) 50% 0/16px calc(100%/6.02) repeat-y,linear-gradient(var(--c-line2),var(--c-line2)) 50% 0/1.5px 100% no-repeat;opacity:.8}"
             "%S .dk-f1{display:block;left:clamp(10px,2.4cqi,36px);top:14%;bottom:14%;width:16px;background:linear-gradient(transparent,var(--c-primary) 45%,transparent 55%) 50% 0/3px 300% no-repeat;animation:%Kfut 7s ease-in-out infinite;opacity:.9}"
             "%S .sec:nth-of-type(even) .dk-f2,%S .sec:nth-of-type(even) .dk-f1{left:auto;right:clamp(10px,2.4cqi,36px)}"
             "%S .dk-a{display:block;width:44px;height:44px;right:5%;top:10%;background:var(--c-primary);opacity:.18;-webkit-mask:var(--m3) center/contain no-repeat;mask:var(--m3) center/contain no-repeat}"
             "@keyframes %Kfut{from{background-position:50% 100%}to{background-position:50% 0}}"),
    dict(id="dS", nev="Szellemszavak", leiras="Óriás, halvány körvonalas szavak a szekciók szélén: FIGYELEM, KIRANA, 12 HÉT, GARANCIA. A program szótára.",
         css="%S .dk-szo{display:block;right:-.03em;bottom:-.14em;font-family:var(--f-display);font-weight:700;font-size:clamp(80px,16cqi,240px);line-height:.8;letter-spacing:-.01em;text-transform:uppercase;white-space:nowrap;color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--c-primary) 26%,transparent)}"
             "%S .sec:nth-of-type(even) .dk-szo{right:auto;left:-.03em;top:-.06em;bottom:auto}"
             "%S .s-deep .dk-szo{-webkit-text-stroke-color:color-mix(in srgb,var(--c-deep-hl) 30%,transparent)}"),
    dict(id="dH", nev="Homokóra + matrica", leiras="Kerek matrica a program tényével („12 hét · 12 gyakorlat”) és egy kis homokóra, ami időnként megfordul. „12 hét múlva mindenképpen 12 héttel idősebb leszel.”",
         css="%S .dk-m{display:grid;place-items:center;width:122px;height:122px;border-radius:50%;right:4.5%;top:9%;background:var(--c-primary);color:var(--c-on-primary);font-family:var(--f-display);font-weight:var(--w-display);font-size:.92rem;line-height:1.1;text-align:center;padding:18px;transform:rotate(10deg);box-shadow:var(--sh-2);z-index:5}"
             "%S .dk-m::before{content:\"\";position:absolute;inset:6px;border-radius:50%;border:1.5px dashed currentColor;opacity:.55}"
             "%S .dk-a{display:block;width:46px;height:46px;left:4%;bottom:10%;background:var(--c-primary);opacity:.32;-webkit-mask:" + HOMOKORA + " center/contain no-repeat;mask:" + HOMOKORA + " center/contain no-repeat;animation:%Kfordul 12s ease-in-out infinite}"
             "%S .s-deep .dk-a{background:var(--c-deep-hl)}"
             "@keyframes %Kfordul{0%,80%{transform:rotate(0)}90%,100%{transform:rotate(180deg)}}"
             "@container elo (max-width:700px){%S .dk-m{width:94px;height:94px;font-size:.72rem;right:3%;top:2%;padding:12px}}"),
]

HATAR = [
    dict(id="sL", nev="Lélegzet-hullám", leiras="Két lágy hullám a szekciók között, mint egy mély be- és kilégzés. Nyugodt, folyékony.",
         css="%S .hat{top:-46px;height:47px;background:var(--sec-bg);-webkit-mask:" + hullam_hatar() + " center bottom/100% 100% no-repeat;mask:" + hullam_hatar() + " center bottom/100% 100% no-repeat}%S .hat.masod{transform:scaleX(-1)}"),
    dict(id="sO", nev="Lótusz-szirmok", leiras="Apró, csúcsos szirmok sora a határon, mint egy lótusz pereme. Finom, egyedi, szakrális.",
         css="%S .hat{top:-17px;height:18px;background:var(--sec-bg);-webkit-mask:" + SZIROM + " 0 100%/40px 18px repeat-x;mask:" + SZIROM + " 0 100%/40px 18px repeat-x}"),
    dict(id="sI", nev="Az izgalom görbéje", leiras="A határ egy emelkedő, majd magasan hullámzó görbe: az izgalom, ami nem a csúcsra rohan, hanem kellemesen magasan marad. A program lényege egy vonalban.",
         css="%S .hat{top:-70px;height:71px;background:var(--sec-bg);-webkit-mask:" + IZGALOM + " center bottom/100% 100% no-repeat;mask:" + IZGALOM + " center bottom/100% 100% no-repeat}%S .hat.masod{transform:scaleX(-1)}"),
    dict(id="sT", nev="Edzésterv-szalag", leiras="Megdöntött, futó szalag a program tényeivel (12 hét, 12 gyakorlat, két garancia), köztük jantra-jelekkel. Lendületes, sokat elmond.",
         css="%S .hat{top:0;height:auto;left:-2%;right:-2%;transform:translateY(-50%) rotate(-1.2deg)}"
             "%S .hat .tick{display:block;background:var(--c-ink);color:var(--c-paper);padding:12px 0;overflow:hidden;box-shadow:var(--sh-2);border-top:3px solid var(--c-primary)}"
             "%S .hat.masod{transform:translateY(-50%) rotate(1deg)}%S .hat.masod .tick{background:var(--c-primary);color:var(--c-on-primary);border-top-color:var(--c-accent)}"
             "%S .hat .tick-in{display:flex;width:max-content;animation:%Ktick 46s linear infinite}"
             "%S .hat .tick-in span{display:inline-flex;align-items:center;gap:20px;padding-right:20px;font-family:var(--f-label);font-weight:600;font-size:.86rem;text-transform:uppercase;letter-spacing:.12em;white-space:nowrap}"
             "%S .hat .tick-in span::after{content:\"\";width:16px;height:16px;background:var(--c-accent);-webkit-mask:" + JANTRA + " center/contain no-repeat;mask:" + JANTRA + " center/contain no-repeat}"
             "%S .sec:has(>.hat){padding-top:calc(var(--sec-y) + 26px)}@keyframes %Ktick{to{transform:translateX(-50%)}}"),
    dict(id="sM", nev="Bindu-ív", leiras="Egyenes határ, közepén egy kis félkör-kapu és benne egy narancs pont (bindu, a jantra középpontja). Csendes, mégis egyedi.",
         css="%S .hat{top:-30px;height:31px;left:50%;right:auto;width:92px;margin-left:-46px;background:radial-gradient(circle 7px at 50% 72%,var(--c-primary) 96%,transparent 100%),var(--sec-bg);-webkit-mask:radial-gradient(circle 46px at 50% 100%,#000 97%,#0000 100%);mask:radial-gradient(circle 46px at 50% 100%,#000 97%,#0000 100%)}"),
]

MOZGAS = [
    dict(id="mE", nev="Lassú kilégzés", leiras="Az elemek lassan, finoman úsznak be, mint egy hosszú kilégzés. Elegáns, pihentető.",
         css="%S.js-rv [data-rv]{opacity:0;transform:translateY(14px);transition:opacity 1.3s var(--ease-out),transform 1.3s var(--ease-out);transition-delay:calc(var(--i)*90ms)}%S.js-rv [data-rv].in{opacity:1;transform:none}"),
    dict(id="mM", nev="Ritmusos lépcső", leiras="Az elemek egymás után, lendületesen emelkednek be, mint az edzés ismétlései. Modern, energikus.",
         css="%S.js-rv [data-rv]{opacity:0;transform:translateY(30px);transition:opacity .7s var(--ease-out),transform .7s var(--ease-out);transition-delay:calc(var(--i)*100ms)}%S.js-rv [data-rv].in{opacity:1;transform:none}"),
    dict(id="mB", nev="Filmes feltárulás", leiras="A blokkok alulról, függönyszerűen tárulnak fel, a fotók lassan közelítenek. Drámai, prémium.",
         css="%S.js-rv [data-rv]{clip-path:inset(0 0 100% 0);transform:translateY(34px);transition:clip-path 1.15s var(--ease-out),transform 1.15s var(--ease-out);transition-delay:calc(var(--i)*110ms)}"
             "%S.js-rv [data-rv].in{clip-path:inset(0 0 0 0);transform:none}%S.js-rv [data-rv].rv-kesz{clip-path:none}"
             "%S .ph{transition:transform 1.9s var(--ease-out)}%S.js-rv [data-rv]:not(.in) .ph{transform:scale(1.12)}"),
    dict(id="mF", nev="Lélegző érkezés", leiras="Az elemek enyhén kicsinyítve, puhán „belélegezve” érkeznek, a fotók halványan világosodnak. Barátságos, lágy.",
         css="%S.js-rv [data-rv]{opacity:0;transform:scale(.95);filter:blur(4px);transition:opacity 1s ease,transform 1.2s var(--ease-out),filter 1s ease;transition-delay:calc(var(--i)*90ms)}%S.js-rv [data-rv].in{opacity:1;transform:none;filter:none}"),
    dict(id="mK", nev="Csendes", leiras="Nincs beúszás és lebegés, csak apró visszajelzések rámutatáskor. Gyors, akadálymentes, komoly.",
         css="%S .dk>i{animation:none!important}"),
]


# =====================================================================================================
# 2. KÖR: új opciók (az ügyfél új textúrát, dekort és szekcióhatárt kért)
# =====================================================================================================
def mandala_svg(r_kulso=46):
    g = ["<g fill='none' stroke='#000' stroke-width='1.2'>"]
    for r in (8, 16, 26, 36, r_kulso):
        g.append(f"<circle cx='50' cy='50' r='{r}'/>")
    for i in range(12):
        a = i * math.pi / 6
        x1, y1 = 50 + 26 * math.cos(a), 50 + 26 * math.sin(a)
        x2, y2 = 50 + 36 * math.cos(a), 50 + 36 * math.sin(a)
        b1, b2 = a - math.pi / 12, a + math.pi / 12
        c1 = (50 + 33 * math.cos(b1), 50 + 33 * math.sin(b1))
        c2 = (50 + 33 * math.cos(b2), 50 + 33 * math.sin(b2))
        g.append(f"<path d='M{x1:.1f} {y1:.1f}Q{c1[0]:.1f} {c1[1]:.1f} {x2:.1f} {y2:.1f}Q{c2[0]:.1f} {c2[1]:.1f} {x1:.1f} {y1:.1f}Z'/>")
        g.append(f"<circle cx='{50 + 41 * math.cos(a):.1f}' cy='{50 + 41 * math.sin(a):.1f}' r='2'/>")
    g.append("</g><circle cx='50' cy='50' r='3'/>")
    return U(S("".join(g)))


MANDALA = mandala_svg()
LANG_VONAL = U(S("<path d='M50 6C58 26 78 38 78 62A28 28 0 0 1 22 62C22 46 32 38 37 25 41 37 45 42 50 44 55 33 55 20 50 6Z' fill='none' stroke='#000' stroke-width='4' stroke-linejoin='round'/>"
                 "<path d='M50 54C55 61 61 65 61 72A11 11 0 0 1 39 72C39 65 45 61 50 54Z' fill='none' stroke='#000' stroke-width='4' stroke-linejoin='round'/>"))
LOTUSZ_SOR = U(S("<g transform='translate(30 6) scale(.32) translate(-50 -10)'><path d='M50 14C63 32 63 56 50 74 37 56 37 32 50 14Z'/>"
                 "<path d='M47 74C38 58 22 50 6 50 12 68 30 78 47 74Z'/><path d='M53 74C62 58 78 50 94 50 88 68 70 78 53 74Z'/></g>", "0 0 60 34"))
SZIROM_NAGY = U(S("<path d='M0 40 C60 40 80 2 100 2 C120 2 140 40 200 40Z'/>", "0 0 200 40", "preserveAspectRatio='none'"))

FELULET += [
    dict(id="tO2", nev="Lótusz, ritkábban", leiras="Ugyanaz a lótuszminta, de nagyobb, ritkább virágokkal és halványabban: levegősebb, nyugodtabb.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + lotusz_csempe() + " 0 0/260px 225px repeat;mask:" + lotusz_csempe() + " 0 0/260px 225px repeat;opacity:.06}"
             "%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.09}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.1}"),
    dict(id="tR", nev="Mandala a sarokban", leiras="Egyetlen nagy, finom vonalas mandala a szekció sarkában, váltakozva jobbra és balra. Elegáns, nem ismétlődik.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + MANDALA + " calc(100% + 140px) -140px/520px 520px no-repeat;mask:" + MANDALA + " calc(100% + 140px) -140px/520px 520px no-repeat;opacity:.05}"
             "%S .sec:nth-of-type(even).tx::before{-webkit-mask-position:-140px calc(100% + 140px);mask-position:-140px calc(100% + 140px)}"
             "%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.06}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.06}"),
    dict(id="tH", nev="Meleg papírszemcse", leiras="Minta nélküli, finom, meleg szemcse, mint egy jó minőségű, merített papír. A legcsendesebb, mégsem üres.",
         css="%S .tx::before{background-image:" + u(ZAJ) + ",radial-gradient(ellipse at 50% 40%,transparent 55%,color-mix(in srgb,var(--c-primary) 9%,transparent));background-size:180px 180px,100% 100%;mix-blend-mode:multiply}"
             "%S .s-deep.tx::before,%S .s-primary.tx::before{mix-blend-mode:screen;opacity:.45}"),
    dict(id="tV", nev="Lótusz-szegély", leiras="Apró lótuszok sora csak a szekciók felső szélén, mint egy hímzett szegély. A tartalom mögött tiszta marad a felület.",
         css="%S .tx::before{background-color:var(--c-primary);-webkit-mask:" + LOTUSZ_SOR + " 0 22px/60px 34px repeat-x;mask:" + LOTUSZ_SOR + " 0 22px/60px 34px repeat-x;opacity:.22}"
             "%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.25}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.25}"),
]

DEKOR += [
    dict(id="dM", nev="Álló mandala", leiras="Egy nagy, finom vonalas mandala a szekció sarkában, mozdulatlanul. Elegáns, méltóságteljes, nem tereli el a figyelmet.",
         css="%S .dk-jel{display:block;width:clamp(240px,36cqi,460px);aspect-ratio:1;right:-8%;top:-10%;background:var(--c-primary);-webkit-mask:" + MANDALA + " center/contain no-repeat;mask:" + MANDALA + " center/contain no-repeat;opacity:.13}"
             "%S .sec:nth-of-type(even) .dk-jel{right:auto;left:-9%;top:auto;bottom:-12%}"
             "%S .s-deep .dk-jel{background:var(--c-deep-hl);opacity:.16}%S .s-primary .dk-jel{background:var(--c-on-primary);opacity:.16}"),
    dict(id="dO", nev="Lebegő lótuszok", leiras="Két-három apró lótusz lassan lebeg a szekciók szélén. Finom, élő, a lótuszmintás háttérhez illik.",
         css="%S .dk-a,%S .dk-b,%S .dk-c{display:block;background:var(--c-primary);-webkit-mask:" + LOTUSZ + " center/contain no-repeat;mask:" + LOTUSZ + " center/contain no-repeat;opacity:.28;animation:%Klebeg 11s ease-in-out infinite alternate}"
             "%S .dk-a{width:46px;height:46px;left:4%;top:12%}%S .dk-b{width:30px;height:30px;right:6%;top:20%;animation-duration:9s}"
             "%S .dk-c{width:38px;height:38px;right:10%;bottom:10%;animation-duration:13s}"
             "%S .s-deep .dk-a,%S .s-deep .dk-b,%S .s-deep .dk-c{background:var(--c-deep-hl)}"
             "@keyframes %Klebeg{from{transform:translateY(0) rotate(-6deg)}to{transform:translateY(-14px) rotate(6deg)}}"
             "@container elo (max-width:600px){%S .dk-c{display:none}}"),
    dict(id="dF", nev="Láng a sarokban", leiras="Egy vonalas láng (a szexuális energia jele) a szekciók alsó sarkában, alig láthatóan „lobog”. Finom utalás a program lényegére.",
         css="%S .dk-a{display:block;width:clamp(70px,9cqi,120px);height:clamp(70px,9cqi,120px);left:3%;bottom:6%;background:var(--c-primary);-webkit-mask:" + LANG_VONAL + " center/contain no-repeat;mask:" + LANG_VONAL + " center/contain no-repeat;opacity:.22;transform-origin:50% 100%;animation:%Klobog 4s ease-in-out infinite}"
             "%S .sec:nth-of-type(even) .dk-a{left:auto;right:3%}"
             "%S .s-deep .dk-a{background:var(--c-deep-hl);opacity:.3}"
             "@keyframes %Klobog{0%,100%{transform:scale(1,1)}50%{transform:scale(.96,1.05)}}"),
    dict(id="d0", nev="Letisztult (nincs dekor)", leiras="Nincs díszítő réteg: csak a háttér-textúra, a tartalom és a fotók. A legnyugodtabb, legtisztább megoldás.",
         css="%S .dk>i{display:none!important}"),
]

HATAR += [
    dict(id="sV", nev="Vékony narancs vonal", leiras="A szekciók között egy rövid, vékony narancs vonal középen. Tiszta, elegáns, a márkaszín finoman visszatér.",
         css="%S .hat{top:-1px;height:2px;left:50%;right:auto;width:min(220px,40%);margin-left:max(-110px,-20%);background:var(--c-primary);opacity:.75;border-radius:2px}"),
    dict(id="sG", nev="Lágy ív", leiras="Minden szekció egyetlen nagy, lágy domborulattal kezdődik, mint egy belégzés íve. Nyugodt, folyékony, nem hullámzik.",
         css="%S .hat{top:-34px;height:35px;background:var(--sec-bg);-webkit-mask:radial-gradient(ellipse 62% 100% at 50% 100%,#000 98.5%,#0000 100%);mask:radial-gradient(ellipse 62% 100% at 50% 100%,#000 98.5%,#0000 100%)}"),
    dict(id="sK", nev="Lótuszszirom középen", leiras="Egyenes határ, a közepén egyetlen nagy, csúcsos szirom emelkedik ki. Csendes, mégis egyedi és a témához illő.",
         css="%S .hat{top:-30px;height:31px;left:50%;right:auto;width:240px;margin-left:-120px;background:var(--sec-bg);-webkit-mask:" + SZIROM_NAGY + " center bottom/100% 100% no-repeat;mask:" + SZIROM_NAGY + " center bottom/100% 100% no-repeat}"),
    dict(id="sP", nev="Pontsor", leiras="Három apró narancs pont középen jelzi a szekció kezdetét, mint egy lélegzetvételnyi szünet. A legdiszkrétebb jelzés.",
         css="%S .hat{top:-4px;height:8px;left:50%;right:auto;width:52px;margin-left:-26px;background:radial-gradient(circle,var(--c-primary) 3.4px,transparent 4px) 0 0/18px 8px repeat-x;opacity:.85}"),
    dict(id="sN", nev="Nincs határjel", leiras="A szekciók egyszerűen színváltással érnek egymásba, külön határjel nélkül. A legtisztább, szerkesztőségi megoldás.",
         css="%S .hat{display:none}"),
]


# =====================================================================================================
# 4. KÖR: Srí Jantra vonalas textúra (az ügyfél képe alapján) és új szekcióhatárok
# =====================================================================================================
def sri_belso(w=1.0):
    # A feltöltött Srí Jantra képről lemért arányok (egységkör, y felfelé)
    C, R = 50, 34.0
    P = lambda x, y: f"{C + x*R:.2f} {C - y*R:.2f}"
    c = lambda y: math.sqrt(1 - y*y)
    a, b, e = 0.262, 0.473, 0.723
    le = [(a, c(a), -0.98), (b, 0.689, -e), (e, 0.570, -a), (0.141, 0.333, -b), (0.041, 0.113, -0.140)]
    fel = [(-a, c(a), 0.98), (-b, 0.689, e), (-e, 0.568, a), (-0.158, 0.320, b)]
    g = [f"<g fill='none' stroke='#000' stroke-width='{w}' stroke-linejoin='round'>"]
    for by, hw, ay in le + fel:
        g.append(f"<path d='M{P(-hw, by)}L{P(hw, by)}L{P(0, ay)}Z'/>")
    g.append(f"<path d='M{P(-0.22, 0.03)}Q{P(0, 0.075)} {P(0.22, 0.03)}'/>")
    g.append(f"<circle cx='{C}' cy='{C}' r='{R}'/>")
    # 8 széles, csúcsban végződő lótuszszirom
    rv, rt, n = R * 1.07, R * 1.32, 8
    pt = lambda r, t: f"{C + r*math.cos(t):.2f} {C + r*math.sin(t):.2f}"
    for i in range(n):
        t = -math.pi/2 + i * 2*math.pi/n
        h = math.pi/n
        g.append(f"<path d='M{pt(rv, t-h)}C{pt(rt*0.98, t-h*0.9)} {pt(rt*0.95, t-h*0.3)} {pt(rt*0.93, t-h*0.12)}"
                 f"Q{pt(rt*0.95, t-h*0.04)} {pt(rt, t)}Q{pt(rt*0.95, t+h*0.04)} {pt(rt*0.93, t+h*0.12)}"
                 f"C{pt(rt*0.95, t+h*0.3)} {pt(rt*0.98, t+h*0.9)} {pt(rv, t+h)}'/>")
    g.append(f"<path d='M{P(-1.32, 0)}H{C + rt:.2f}' stroke-dasharray='{w*2.2:.2f} {w*2.2:.2f}'/>")
    g.append(f"</g><circle cx='{P(0, 0.10).split()[0]}' cy='{P(0, 0.10).split()[1]}' r='{w*0.9:.2f}'/>")
    return "".join(g)
SRI = U(S(sri_belso(1.1)))
SRI_KICSI = U(S(sri_belso(2.4)))
for _o in FELULET:
    if _o["id"] == "tR":
        _o["nev"] = "Srí Jantra a sarokban"
        _o["leiras"] = "Egyetlen nagy, vonalas Srí Jantra lótuszszirmokkal a szekció sarkában, váltakozva jobbra és balra. Alig látható, csak egy árnyalattal erősebb a háttérnél."
        _o["css"] = _o["css"].replace(MANDALA, SRI)
SZIROM_VONAL = U(S("<path d='M4 38 C50 38 70 4 100 4 C130 4 150 38 196 38' fill='none' stroke='#000' stroke-width='2.4' stroke-linecap='round'/>"
                   "<path d='M100 16 C90 26 90 32 100 36 C110 32 110 26 100 16Z' fill='none' stroke='#000' stroke-width='2'/>", "0 0 200 42"))
BIMBO = U(S("<path d='M0 60 C40 60 52 40 62 30 C68 44 74 52 80 56 C86 34 92 14 100 2 C108 14 114 34 120 56 C126 52 132 44 138 30 C148 40 160 60 200 60Z'/>",
            "0 0 200 60", "preserveAspectRatio='none'"))
LEGZES_VONAL = U(S("<path d='M2 14 C30 14 40 4 60 4 S90 24 110 24 S140 4 160 4 S190 14 218 14' fill='none' stroke='#000' stroke-width='2.2' stroke-linecap='round'/>", "0 0 220 28"))
HATAR += [
    dict(id="sY", nev="Srí Jantra-pecsét", leiras="A határ közepén egy kerek medál, benne a vonalas Srí Jantra. A háttér-textúra motívuma köszön vissza: egységes, szakrális, emlékezetes.",
         css="%S .hat{top:-34px;height:68px;left:50%;right:auto;width:68px;margin-left:-34px;border-radius:50%;background:var(--sec-bg);box-shadow:0 0 0 1px color-mix(in srgb,var(--c-primary) 35%,transparent)}"
             "%S .hat::after{content:\"\";position:absolute;inset:7px;background:var(--c-primary);-webkit-mask:" + SRI_KICSI + " center/contain no-repeat;mask:" + SRI_KICSI + " center/contain no-repeat;opacity:.8}"
             "%S .s-deep .hat::after,%S .s-deep>.hat::after{background:var(--c-deep-hl)}"),
    dict(id="sD", nev="Szirom-körvonal", leiras="A lótuszszirom csak vékony narancs körvonalként rajzolódik ki, közepén egy apró csepp. Könnyedebb, rajzosabb párja a választott szirom-határnak.",
         css="%S .hat{top:-21px;height:21px;left:50%;right:auto;width:300px;margin-left:-150px;background:var(--c-primary);opacity:.7;-webkit-mask:" + SZIROM_VONAL + " center bottom/100% 100% no-repeat;mask:" + SZIROM_VONAL + " center bottom/100% 100% no-repeat}"
             "%S .s-deep>.hat{background:var(--c-deep-hl)}"),
    dict(id="sB", nev="Lótuszbimbó", leiras="A szekció fölé egy háromszirmú lótuszbimbó emelkedik: középen a magas, két oldalt két kisebb szirom. Nőiesebb, organikusabb, mint az egyetlen szirom.",
         css="%S .hat{top:-44px;height:45px;left:50%;right:auto;width:260px;margin-left:-130px;background:var(--sec-bg);-webkit-mask:" + BIMBO + " center bottom/100% 100% no-repeat;mask:" + BIMBO + " center bottom/100% 100% no-repeat}"),
    dict(id="sW", nev="Lélegzet-vonal", leiras="Egy vékony, lágyan hullámzó narancs vonal a határ közepén, mint egy nyugodt be- és kilégzés. Diszkrét, mégis élő.",
         css="%S .hat{top:-7px;height:14px;left:50%;right:auto;width:220px;margin-left:-110px;background:var(--c-primary);opacity:.75;-webkit-mask:" + LEGZES_VONAL + " center/100% 100% no-repeat;mask:" + LEGZES_VONAL + " center/100% 100% no-repeat}"
             "%S .s-deep>.hat{background:var(--c-deep-hl)}"),
]

# 5. kör: a választott szirom-határ 20%-kal alacsonyabb változata (31px -> 25px)
HATAR += [
    dict(id="sK2", nev="Lótuszszirom középen, alacsonyabb", leiras="Ugyanaz a középső lótuszszirom, de 20%-kal alacsonyabb domborulattal. Még csendesebb átmenet.",
         css="%S .hat{top:-24px;height:25px;left:50%;right:auto;width:240px;margin-left:-120px;background:var(--sec-bg);-webkit-mask:" + SZIROM_NAGY + " center bottom/100% 100% no-repeat;mask:" + SZIROM_NAGY + " center bottom/100% 100% no-repeat}"),
]
