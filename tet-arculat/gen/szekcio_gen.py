# -*- coding: utf-8 -*-
"""Tantraszex Edzésterv: egyedi szekciók és szekció-változatok (html + css). A HTML a motor saját
építőelemeiből (kick, foto, btn, dk, hat) készül, így a globális stílus-opciók rájuk is hatnak."""
import sys
sys.path.insert(0, "/root/.claude/skills/synced/2ef019ad-994b-4a29-ba20-0f4f0fc9c379_12065cb9-5571-428e-a25a-37502384cf98/webdesign-arculat-generator/scripts")
from motor.alap import md, esc, ui
from motor import kozos
from motor.kozos import kick, btn, dk, hat, foto, ik, logo, gombsor, statok, chips, kezi
from alap_gen import ROLASZOL as R, MIERT as M, KINEK as K, VELEMENYEK as V, GARANCIA as G, GYIK as Q, ORDER, ORDER_PREMIUM, CSOMAGOK, TARTALOM, MIA, PREMIUM

CTX = None


def ctx():
    return CTX


def sh(d, bal=False, extra=""):
    """Szekciófej (ugyanaz a szerkezet, mint a motoré)."""
    p = kick(d.get("kicker")) + f'<h2 class="cim">{md(d["cim"])}</h2>'
    if d.get("lead"):
        p += f'<p class="lead">{md(d["lead"])}</p>'
    return f'<header class="shead{" bal" if bal else ""}" data-rv>{p}{extra}</header>'


def sec(vid, slot, felulet, belso, anchor=None, hatar=True, masod=False, tx=True):
    c = ctx()
    return (f'<section class="sec v-{vid} {felulet}{" tx" if tx else ""}" id="{anchor or slot}">'
            f'{hat(c, masod) if hatar else ""}{dk(c, slot)}{belso}</section>')


def mdk(t):
    """md + az eredetiben pirossal kiemelt rész (!!...!!) a paletta kiemelő színével."""
    import re as _re
    return _re.sub(r"!!(.+?)!!", r'<strong class="kiem">\1</strong>', md(t))


def mdg(t):
    """GYIK-válasz: md (sortörés, félkövér) + kattintható telefonszám."""
    from alap_gen import TELEFON
    return md(t).replace(TELEFON, f'<a class="tel" href="tel:{TELEFON.replace(" ", "")}">{TELEFON}</a>')


def li(lst, cls=""):
    return "".join(f'<li class="{cls}" data-rv>{md(x)}</li>' for x in lst)


# ================================================================ NAV
NAV = [
    dict(id="nx1", nev="Sötét, áttetsző sáv", leiras="Sötét, áttetsző fejléc a hero fölött: logó, név, menü és egy narancs gomb. Intim, prémium.",
         html=None, css=r"""
.v-nx1{position:absolute;left:0;right:0;top:0;z-index:50;background:linear-gradient(180deg,rgba(10,7,5,.78),rgba(10,7,5,0));color:#fff}
.v-nx1 .in{display:flex;align-items:center;gap:22px;padding-top:16px;padding-bottom:16px}
.v-nx1 .brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:#fff;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.15rem;letter-spacing:.01em}
.v-nx1 .brand .logo{background-image:var(--logo-feher)}
.v-nx1 .links{display:flex;gap:22px;margin-left:auto}
.v-nx1 .links a{text-decoration:none;font-weight:600;font-size:.92rem;opacity:.85}.v-nx1 .links a:hover{opacity:1}
.v-nx1 .btn{--b-bg:var(--c-primary);--b-ink:var(--c-on-primary)}
@container elo (max-width:860px){.v-nx1 .links{display:none}.v-nx1 .btn{margin-left:auto;font-size:.85rem}}
@container elo (max-width:440px){.v-nx1 .brand span{display:none}}
"""),
    dict(id="nx2", nev="Landing: csak logó és egy gomb", leiras="Értékesítési oldalhoz: nincs menü, ami elvinné a figyelmet. Logó, név, egy finom „Csomagok” gomb. A legtisztább.",
         html=None, css=r"""
.v-nx2{position:relative;z-index:50;background:var(--c-paper);border-bottom:1px solid var(--c-line)}
.v-nx2 .in{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:12px;padding-bottom:12px}
.v-nx2 .brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--c-head)}
.v-nx2 .brand b{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.12rem;line-height:1.05;display:block}
.v-nx2 .brand small{display:block;font-family:var(--f-label);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3)}
.v-nx2 .btn{font-size:.86rem}
@container elo (max-width:480px){.v-nx2 .brand small{display:none}}
"""),
]


def nav_html():
    c = ctx()
    links = "".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in c["nav"]["linkek"])
    NAV[0]["html"] = (f'<header class="nav v-nx1" data-nav><div class="wrap in"><a class="brand" href="#top">{logo(c, 40)}'
                      f'<span>Tantraszex Edzésterv</span></a><nav class="links">{links}</nav>{btn(c["nav"]["cta"])}</div></header>')
    NAV[1]["html"] = (f'<header class="nav v-nx2" data-nav><div class="wrap in"><a class="brand" href="#top">{logo(c, 44)}'
                      f'<span><b>Tantraszex Edzésterv</b><small>Online · 12 hét · 45+ férfiaknak</small></span></a>'
                      f'{btn({"szoveg": "Csomagok", "href": "#etlap"}, alt=True, ikon="le")}</div></header>')


# ================================================================ HERO
def hero_html():
    c = ctx()
    h = c["hero"]
    b = f'<div class="chips">{chips(h["badgek"])}</div>' if h.get("badgek") else ""
    return (f'<section class="sec v-hx1 s-deep" id="top">{dk(c, "hero")}<div class="feny" aria-hidden="true"></div>'
            f'<div class="wrap grid"><div class="txt" data-rv>{kick(h.get("kicker"))}<h1 class="hcim">{md(h["cim"])}</h1>'
            f'<p class="lead">{md(h["lead"])}</p>{gombsor(h)}{b}</div>'
            f'<div class="kep" data-rv><div class="ph f-szivfekete" role="img" aria-label="{esc(c["fotok"]["szivfekete"]["alt"])}"></div>'
            f'{statok(h["statok"])}</div></div></section>')


HERO = [dict(id="hx1", nev="Gyertyafény-színpad", leiras="Sötét, szinte fekete nyitókép: a meditáló férfi fotója a fekete háttérből emelkedik ki, mögötte meleg narancs fény. A cím mellett a három ígéret. Intim, prémium, a fotóitokhoz szabva.",
             html=None, css=r"""
.v-hx1{--sec-bg:#060403;padding:clamp(110px,10cqi,150px) 0 clamp(50px,6cqi,80px);overflow:hidden}
.v-hx1 .feny{display:none;position:absolute;right:8%;top:12%;width:clamp(320px,52cqi,720px);aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb,var(--c-primary) 55%,transparent),transparent 65%);filter:blur(10px);z-index:0}
.v-hx1 .grid{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(20px,4cqi,60px);align-items:center}
.v-hx1 .txt{position:relative;z-index:3}
.v-hx1 .hcim{color:#fff}.v-hx1 .lead{color:rgba(255,255,255,.78);margin:22px 0 30px;max-width:46ch}
.v-hx1 .chips{display:flex;flex-direction:column;align-items:flex-start;gap:10px;margin-top:34px}
.v-hx1 .chip{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.14);color:#f3e9dd;box-shadow:none}
.v-hx1 .chip .ui{color:var(--c-accent)}
.v-hx1 .kep{position:relative;z-index:2;isolation:isolate}.v-hx1 .kep::before{content:"";position:absolute;inset:6% 4% 14%;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb,var(--c-primary) 60%,transparent),transparent 68%);z-index:-1}
.v-hx1 .kep .ph{aspect-ratio:4/5;mix-blend-mode:lighten;background-size:cover;-webkit-mask-image:radial-gradient(ellipse 62% 60% at 50% 46%,#000 55%,transparent 100%);mask-image:radial-gradient(ellipse 62% 60% at 50% 46%,#000 55%,transparent 100%)}
.v-hx1 .stat{position:absolute;left:0;right:0;bottom:2%;display:flex;justify-content:center;gap:clamp(18px,3cqi,40px)}
.v-hx1 .stat b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,3cqi,2.4rem);line-height:1;color:var(--c-accent);text-align:center}
.v-hx1 .stat span{display:block;font-family:var(--f-label);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.7);text-align:center}
@container elo (max-width:860px){.v-hx1 .grid{grid-template-columns:1fr}.v-hx1 .kep{order:-1;max-width:420px;margin:0 auto;width:100%}.v-hx1 .feny{right:-20%;top:0}}
""")]


def hero_h3():
    """A 3-as hero az ügyfél kérése szerint: kisebb kártya csak a címmel és a terméknévvel, a többi szöveg alatta külön blokkban."""
    c = ctx()
    h = c["hero"]
    f = c["fotok"]["szivsotet"]
    return (f'<section class="sec v-h3 s-paper" id="top"><div class="ph f-szivsotet bg" role="img" aria-label="{esc(f["alt"])}" style="--pos:60% 12%"></div>'
            f'<div class="shade"></div><div class="wrap"><div class="card s-vilagos" data-rv><h1 class="hcim">{md(h["cim"])}</h1>'
            f'<p class="nev">Tantraszex Edzésterv</p></div></div></section>'
            f'<section class="sec v-h3b s-deep" id="bevezeto"><div class="wrap szuk" data-rv>'
            f'<p class="alcim">Online gyakorlóprogram 45+ férfiaknak</p>'
            f'<p class="sor"><b>12 hét, 12 gyakorlat. Egy új szint a szexualitásodban.</b></p>'
            f'<p class="nem">Nem kell hinned a Tantrában, csak próbáld ki, mit csinál a testeddel!</p>{gombsor(h)}</div></section>')


H3_CSS = r"""
.v-h3{padding:clamp(110px,11cqi,160px) 0 clamp(50px,6cqi,90px);min-height:clamp(540px,58cqi,720px);display:flex;align-items:flex-end}
.v-h3 .bg{position:absolute;inset:0;aspect-ratio:auto;height:100%;z-index:-2;background-position:var(--pos)}
.v-h3 .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(0,0,0,.05) 50%,transparent);z-index:-1}
.v-h3 .wrap{width:100%}
.v-h3 .card{max-width:430px;background:var(--c-paper);border-radius:20px;padding:clamp(20px,2.6cqi,32px);box-shadow:var(--sh-3)}
.v-h3 .hcim{font-size:calc(clamp(1.35rem,2.3cqi,2rem)*var(--hero-scale,1))!important;line-height:1.18}
.v-h3 .nev{margin:16px 0 0;padding-top:14px;border-top:2px solid var(--c-primary);font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.15rem,1.9cqi,1.5rem);letter-spacing:.06em;text-transform:uppercase;color:var(--c0-primary-text,var(--c-primary))}
.v-h3b{padding:clamp(40px,5cqi,70px) 0;text-align:center}
.v-h3b .alcim{font-family:var(--f-label);font-size:.82rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--hl);margin:0 0 12px}
.v-h3b .sor{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.3rem,2.4cqi,1.9rem);color:var(--c-head);margin:0 0 10px}
.v-h3b .sor b{font-weight:inherit}
.v-h3b .nem{color:var(--c-ink-2);margin:0 0 24px}
.v-h3b .gombsor{justify-content:center}
@container elo (max-width:760px){.v-h3{min-height:0;padding-top:70cqi;align-items:flex-end}.v-h3 .bg{height:78cqi;bottom:auto}.v-h3 .shade{display:none}.v-h3 .card{max-width:none}}
"""


# ================================================================ MIRŐL SZÓL (egyedi)
def rolaszol():
    trio = R["trio"]

    def tr(cls="lep"):
        return "".join(f'<div class="{cls} t{i}" data-rv style="--i:{i}"><b>{esc(a)}</b><span>{md(b)}</span></div>' for i, (a, b) in enumerate(trio))
    talan = f'<ul class="talan">{li(R["talan"])}</ul>'
    szov = f'<p class="szov" data-rv>{md(R["szoveg"])}</p>'
    zaro = f'<p class="zaro" data-rv>{md(R["zaro"])}</p>'
    out = [
        dict(id="rx1", nev="Életkor-lépcső", leiras="A 15+, 25+ és 45 felett három emelkedő lépcsőfok, a legmagasabb a narancs. Mellette a „Talán…” mondatok. Egyszerre mesél és tagol.",
             html=sec("rx1", "rolaszol", "s-paper", f'<div class="wrap">{sh(R)}<div class="grid"><div class="lepcso">{tr()}</div>'
                      f'<div class="jobb">{zaro}{szov}{talan}</div></div></div>'),
             css=r"""
.v-rx1 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5cqi,72px);align-items:end}
.v-rx1 .lepcso{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;align-items:end;min-height:340px}
.v-rx1 .lep{background:var(--c-card);border:1px solid var(--c-line);border-radius:14px 14px 4px 4px;padding:18px 16px;display:flex;flex-direction:column;gap:8px}
.v-rx1 .t0{min-height:46%}.v-rx1 .t1{min-height:66%}.v-rx1 .t2{min-height:96%;background:var(--c-primary);border-color:var(--c-primary)}
.v-rx1 .lep b{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,3cqi,2.4rem);line-height:1;color:var(--hl)}
.v-rx1 .t2 b,.v-rx1 .t2 span{color:var(--c-on-primary)}.v-rx1 .lep span{font-size:.92rem;color:var(--c-ink-2)}
.v-rx1 .talan{display:grid;gap:10px;margin:18px 0}
.v-rx1 .talan li{padding-left:28px;position:relative}.v-rx1 .talan li::before{content:"";position:absolute;left:0;top:.62em;width:16px;height:2px;background:var(--c-accent)}
.v-rx1 .zaro{font-family:var(--f-display);font-weight:var(--w-display);font-size:var(--t-h3);color:var(--hl)}
@container elo (max-width:820px){.v-rx1 .grid{grid-template-columns:1fr}.v-rx1 .lepcso{min-height:260px}}
"""),
        dict(id="rx2", nev="Idővonal három állomással", leiras="Vízszintes idővonal: 15+, 25+, 45 felett, az utolsó pont izzik. Alatta két hasábban a „Talán…” mondatok. Tiszta, mesélős.",
             html=sec("rx2", "rolaszol", "s-white", f'<div class="wrap">{sh(R)}<div class="ido">{tr("all")}</div>'
                      f'{zaro}<div class="also">{szov}{talan}</div></div>', masod=True),
             css=r"""
.v-rx2 .ido{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;position:relative;margin:10px 0 44px;padding-top:34px}
.v-rx2 .ido::before{content:"";position:absolute;left:0;right:0;top:9px;height:2px;background:linear-gradient(90deg,var(--c-line2),var(--c-primary))}
.v-rx2 .all{position:relative}.v-rx2 .all::before{content:"";position:absolute;left:0;top:-34px;width:20px;height:20px;border-radius:50%;background:var(--c-card);border:2px solid var(--c-line2)}
.v-rx2 .t2::before{background:var(--c-primary);border-color:var(--c-primary);box-shadow:0 0 0 8px color-mix(in srgb,var(--c-primary) 18%,transparent),0 0 30px var(--c-accent)}
.v-rx2 .all b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.5rem,2.8cqi,2.2rem);color:var(--c-head);line-height:1.05}
.v-rx2 .t2 b{color:var(--hl)}.v-rx2 .all span{color:var(--c-ink-2)}
.v-rx2 .also{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(24px,4cqi,60px)}
.v-rx2 .talan{display:grid;gap:8px}.v-rx2 .talan li{border-bottom:1px solid var(--c-line);padding:8px 0}
.v-rx2 .zaro{text-align:center;margin:0 0 30px;font-family:var(--f-display);font-weight:var(--w-display);font-size:var(--t-h3);color:var(--hl)}
@container elo (max-width:760px){.v-rx2 .ido,.v-rx2 .also{grid-template-columns:1fr}.v-rx2 .ido::before{display:none}.v-rx2 .ido{padding-top:0}.v-rx2 .all{padding-left:34px}.v-rx2 .all::before{top:4px}}
"""),
        dict(id="rx3", nev="Óriás számok", leiras="A három életkor óriási, körvonalas számként, a 45 telt narancsban. Alatta a mondatok címkékként. Plakátos, merész.",
             html=sec("rx3", "rolaszol", "s-tint", f'<div class="wrap">{sh(R)}<div class="nagy">{tr("sz")}</div>{zaro}{szov}'
                      f'<ul class="chiplist">{li(R["talan"], "chip")}</ul></div>'),
             css=r"""
.v-rx3 .nagy{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:30px}
.v-rx3 .sz b{display:block;font-family:var(--f-display);font-weight:800;font-size:clamp(3.2rem,9cqi,7.5rem);line-height:.9;color:transparent;-webkit-text-stroke:2px var(--c-ink-3)}
.v-rx3 .t2 b{color:var(--c-primary);-webkit-text-stroke:0;font-size:clamp(2.6rem,7cqi,6rem)}
.v-rx3 .sz span{display:block;margin-top:10px;font-weight:700;color:var(--c-ink-2)}
.v-rx3 .szov{max-width:62ch;margin:0 auto 22px;text-align:center}
.v-rx3 .chiplist{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
.v-rx3 .chiplist .chip{font-weight:600;white-space:normal}
.v-rx3 .zaro{text-align:center;margin:0 0 22px;font-family:var(--f-display);font-weight:var(--w-display);font-size:var(--t-h3);color:var(--hl)}
@container elo (max-width:700px){.v-rx3 .nagy{grid-template-columns:1fr}}
"""),
        dict(id="rx4", nev="Levél, középre zárva", leiras="Egy keskeny, levélszerű hasáb: a három életkor egy kiemelt mondatsorként, a „Talán…” sorok kézírásos pipákkal. Személyes, mintha Kirana írná.",
             html=sec("rx4", "rolaszol", "s-sand", f'<div class="wrap szuk">{sh(R)}<div class="level" data-rv><p class="trio">'
                      + " ".join(f'<b>{esc(a)}</b> {md(b)}' for a, b in trio) + f'</p><p class="kezi">{md(R["zaro"])}</p>{szov}'
                      f'<ul class="talan">{li(R["talan"])}</ul></div></div>'),
             css=r"""
.v-rx4 .level{background:var(--c-card);padding:clamp(26px,4.4cqi,56px);border-radius:6px;box-shadow:var(--sh-2);position:relative}
.v-rx4 .trio{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.15rem,2cqi,1.5rem);line-height:1.35;color:var(--c-head);border-left:3px solid var(--c-primary);padding-left:18px;margin:22px 0}
.v-rx4 .trio b{color:var(--hl)}
.v-rx4 .talan{display:grid;gap:10px;margin:18px 0 22px}
.v-rx4 .talan li{padding-left:32px;position:relative}
.v-rx4 .talan li::before{content:"✓";position:absolute;left:4px;top:-2px;font-family:var(--f-hand);font-size:1.3rem;color:var(--c-primary)}
.v-rx4 .kezi{font-size:calc(var(--fs-hand)*1.5rem);margin:0 0 20px}
"""),
        dict(id="rx5", nev="Sötét kártyasor", leiras="Sötét szekció, a három életkor három kártyán, a 45 felett narancsban izzik. Jobbra a mondatok. Drámai, férfias.",
             html=sec("rx5", "rolaszol", "s-deep", f'<div class="wrap">{sh(R, bal=True)}<div class="grid"><div class="kartyak">{tr("krt")}</div>'
                      f'<div>{zaro}{szov}{talan}</div></div></div>'),
             css=r"""
.v-rx5 .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(26px,4.6cqi,70px);align-items:start}
.v-rx5 .kartyak{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.v-rx5 .krt b{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.5rem,2.8cqi,2.2rem);line-height:1;color:var(--hl)}
.v-rx5 .krt span{font-size:.92rem;color:var(--c-ink-2)}
.v-rx5 .krt.t2{background:var(--c-primary);--c-ink-2:var(--c-on-primary);--hl:var(--c-on-primary);outline-color:transparent;border-color:var(--c-primary)}
.v-rx5 .talan{display:grid;gap:10px;margin:16px 0}.v-rx5 .talan li{padding-left:24px;position:relative}
.v-rx5 .talan li::before{content:"";position:absolute;left:0;top:.55em;width:9px;height:9px;border-radius:50%;background:var(--c-accent)}
.v-rx5 .zaro{font-family:var(--f-display);font-weight:var(--w-display);font-size:var(--t-h3);color:var(--hl)}
@container elo (max-width:860px){.v-rx5 .grid{grid-template-columns:1fr}}
@container elo (max-width:560px){.v-rx5 .kartyak{grid-template-columns:1fr}}
"""),
    ]
    return out


# ================================================================ MIÉRT TANTRA (egyedi)
def miert():
    """16. blokk: minden változat PONTOSAN az ügyfél sorrendjében olvasható (fentről le, balról jobbra)."""
    c = ctx()
    fej = f'<header class="shead" data-rv><h2 class="cim">{md(M["cim"])}</h2></header>'
    p1 = f'<p class="mp1" data-rv>{md(M["p1"])}</p><p class="mp2" data-rv>{md(M["p2"])}</p>'
    lanc = f'<p class="lanc" data-rv>{esc(M["lanc_sor"])}</p><p class="siker" data-rv>{esc(M["lanc_vege"])}</p>'
    fontos = f'<p class="fontos" data-rv>{md(M["fontos"])}</p><p class="kcim" data-rv>{esc(M["kerdes_cim"])}</p>'
    kerd = '<ul class="kerd">' + "".join(f'<li data-rv style="--i:{i}">{esc(x)}</li>' for i, x in enumerate(M["kerdesek"])) + "</ul>"
    kik = f'<p class="kik" data-rv>{md(M["kikoltozik"])}</p>'
    tantra = (f'<p class="tcim" data-rv>{md(M["tantra_cim"])}</p><ul class="tl">'
              + "".join(f'<li data-rv style="--i:{i}">{md(x)}</li>' for i, x in enumerate(M["tantra"])) + "</ul>")
    kiem = f'<p class="kiemelt" data-rv>{"<br>".join(md(x) for x in M["kiemelt"])}</p>'
    zaro = ('<div class="zaro" data-rv>' + "".join(f'<p>{md(x)}</p>' for x in M["zaro_sorok"])
            + f'</div><div class="gombsor mcta" data-rv>{btn(M["cta"])}</div>')
    elso = p1 + lanc + fontos + kerd + kik          # a „cél-gondolkodás” rész
    masodik = tantra                                 # a tantra válasza
    vege = kiem + zaro                               # a kiemelt mondat és a zárás

    KOZOS = r"""
.v-%s .mp1,.v-%s .mp2,.v-%s .fontos,.v-%s .kik,.v-%s .zaro p{margin:0 0 10px}
.v-%s .mp2 b,.v-%s .fontos b{color:var(--c-head)}
.v-%s .lanc{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.1rem,1.9cqi,1.4rem);color:var(--c-head);margin:18px 0 4px}
.v-%s .siker{font-style:italic;color:var(--c-ink-2);margin:0 0 16px}
.v-%s .kcim{font-weight:700;color:var(--c-head);margin:6px 0 10px}
.v-%s .kerd{display:grid;gap:6px;margin:0 0 16px}
.v-%s .kerd li{padding-left:22px;position:relative;font-style:italic;color:var(--c-ink-2)}
.v-%s .kerd li::before{content:"?";position:absolute;left:2px;top:0;font-style:normal;font-weight:800;color:var(--hl)}
.v-%s .kik{font-weight:600;color:var(--c-head)}
.v-%s .tcim{margin:0 0 10px}.v-%s .tcim b{color:var(--c-head)}
.v-%s .tl{display:grid;gap:8px;margin:0}
.v-%s .tl li{padding-left:26px;position:relative}
.v-%s .tl li::before{content:"";position:absolute;left:2px;top:.5em;width:12px;height:7px;border-left:2px solid var(--hl);border-bottom:2px solid var(--hl);transform:rotate(-45deg)}
.v-%s .tl b{color:var(--hl)}
.v-%s .kiemelt{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.45rem,3.4cqi,2.6rem);line-height:1.15;color:var(--c-head);margin:clamp(34px,5cqi,60px) 0 22px;max-width:100%;overflow-wrap:break-word;hyphens:manual;text-wrap:balance}
.v-%s .kiemelt b{color:inherit}
.v-%s .zaro{color:var(--c-ink-2)}.v-%s .zaro b{color:var(--c-head)}
.v-%s .mcta{margin-top:24px}
"""

    def kozos(v):
        return KOZOS.replace("%s", v)
    out = [
        dict(id="mx1", nev="Fej és test, két panel", leiras="Balra egy szaggatott keretes panelen a „cél-gondolkodás” (a lánc, a kérdések, a fejbe költöző figyelem), jobbra egy sötét panelen a tantra válasza. Alattuk, középen, nagyban a kiemelt mondat. Sorrendben olvasható, balról jobbra.",
             html=sec("mx1", "miert", "s-paper", f'<div class="wrap">{fej}<div class="grid"><div class="fej">{elso}</div>'
                      f'<div class="test s-deep">{masodik}</div></div><div class="also">{vege}</div></div>'),
             css=kozos("mx1") + r"""
.v-mx1 .grid{display:grid;grid-template-columns:1.25fr .75fr;gap:clamp(18px,3cqi,36px);align-items:start}
.v-mx1 .fej,.v-mx1 .test{border-radius:var(--r);padding:clamp(24px,3.6cqi,44px)}
.v-mx1 .fej{background:var(--c-card);border:1px dashed var(--c-line2)}
.v-mx1 .test{background:var(--c-deep);color:var(--c-ink);position:sticky;top:20px}
.v-mx1 .also{text-align:center;max-width:760px;margin:0 auto}.v-mx1 .mcta{justify-content:center}
.v-mx1 .kiemelt{position:relative;padding-top:26px}
.v-mx1 .kiemelt::before{content:"";position:absolute;left:50%;top:0;width:60px;height:3px;margin-left:-30px;background:var(--c-primary)}
@container elo (max-width:820px){.v-mx1 .grid{grid-template-columns:1fr}.v-mx1 .test{position:relative;top:0}}
"""),
        dict(id="mx2", nev="Egy hasáb, felolvasásra", leiras="Egyetlen keskeny, középre zárt hasáb, mint egy felolvasott szöveg: a lánc kiemelt sorként, a kérdések egyre halványabban, a végén óriás betűkkel a kiemelt mondat. A legjobban követhető.",
             html=sec("mx2", "miert", "s-white", f'<div class="wrap szuk">{fej}<div class="egy">{elso}{masodik}{vege}</div></div>', masod=True),
             css=kozos("mx2") + r"""
.v-mx2 .egy{text-align:center}
.v-mx2 .lanc{font-size:clamp(1.3rem,2.6cqi,1.9rem);letter-spacing:.01em}
.v-mx2 .kerd{justify-items:center}.v-mx2 .kerd li{padding:0}.v-mx2 .kerd li::before{display:none}
.v-mx2 .kerd li:nth-child(2){opacity:.85}.v-mx2 .kerd li:nth-child(3){opacity:.7}.v-mx2 .kerd li:nth-child(4){opacity:.55}.v-mx2 .kerd li:nth-child(5){opacity:.42}
.v-mx2 .tl{justify-items:center}.v-mx2 .tl li{padding:0}.v-mx2 .tl li::before{display:none}
.v-mx2 .tcim{margin-top:22px}
.v-mx2 .kiemelt{font-size:clamp(1.55rem,4cqi,2.9rem);padding:28px 0;border-top:1px solid var(--c-line2);border-bottom:1px solid var(--c-line2)}
.v-mx2 .mcta{justify-content:center}
"""),
        dict(id="mx3", nev="Szöveg a jantrás fotó mellett", leiras="Balra sorban a teljes szöveg, jobbra a meditáló férfi a jantrával, görgetéskor a helyén marad. Alul teljes szélességben a kiemelt mondat. Képszerű, nyugodt.",
             html=sec("mx3", "miert", "s-paper", f'<div class="wrap">{fej}<div class="grid"><div class="txt">{elso}{masodik}</div>'
                      f'<div class="kep" data-rv>{foto(c, "jantra", "4/5")}</div></div><div class="also">{vege}</div></div>'),
             css=kozos("mx3") + r"""
.v-mx3 .shead{text-align:left;margin-left:0}
.v-mx3 .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(30px,5cqi,80px);align-items:start}
.v-mx3 .kep{position:sticky;top:24px}
.v-mx3 .tcim{margin-top:20px}
.v-mx3 .also{max-width:820px}
.v-mx3 .kiemelt{border-left:4px solid var(--c-primary);padding-left:22px}
@container elo (max-width:860px){.v-mx3 .grid{grid-template-columns:1fr}.v-mx3 .kep{position:relative;top:0;max-width:420px}}
"""),
        dict(id="mx4", nev="Sötét kiáltvány", leiras="Sötét szekció, egy hasábban: a szöveg nyugodtan halad, majd a kiemelt mondat óriási betűkkel, meleg fényben áll ki belőle. Komoly, súlyos, megállítja a görgetést.",
             html=sec("mx4", "miert", "s-deep", f'<div class="wrap szuk">{fej}<div class="egy">{elso}{masodik}{vege}</div></div>'),
             css=kozos("mx4") + r"""
.v-mx4 .egy{max-width:680px;margin:0 auto}
.v-mx4 .lanc{color:var(--c-deep-hl)}
.v-mx4 .kiemelt{text-align:center;font-size:clamp(1.6rem,4.2cqi,3rem);color:#fff;text-shadow:0 0 40px color-mix(in srgb,var(--c-primary) 70%,transparent);margin:clamp(44px,6cqi,80px) 0 30px}
.v-mx4 .zaro{text-align:center}.v-mx4 .mcta{justify-content:center}
"""),
        dict(id="mx5", nev="Kérdés-kártyák", leiras="Bal hasábban a szöveg, a fejben zakatoló öt kérdés egymásra csúszó kártyákon; jobb hasábban a folytatás: a figyelem kiköltözik, a tantra válasza, majd a kiemelt mondat. Balról jobbra, sorrendben.",
             html=sec("mx5", "miert", "s-tint", f'<div class="wrap">{fej}<div class="grid"><div class="bal">{p1}{lanc}{fontos}<div class="legyezo" data-rv>'
                      + "".join(f'<div class="lap l{i}">{esc(x)}</div>' for i, x in enumerate(M["kerdesek"]))
                      + f'</div></div><div class="jobb">{kik}{masodik}{vege}</div></div></div>', masod=True),
             css=kozos("mx5") + r"""
.v-mx5 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5cqi,80px);align-items:start}
.v-mx5 .legyezo{display:grid;gap:0;margin-top:6px}
.v-mx5 .lap{padding:14px 18px;background:var(--c-card);border-radius:12px;box-shadow:var(--sh-2);font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1rem,1.7cqi,1.25rem);color:var(--c-head);margin-bottom:-6px}
.v-mx5 .l0{transform:rotate(-2deg)}.v-mx5 .l1{transform:rotate(1.5deg) translateX(14px)}.v-mx5 .l2{transform:rotate(-1deg) translateX(4px)}
.v-mx5 .l3{transform:rotate(2deg) translateX(18px)}.v-mx5 .l4{transform:rotate(-1.5deg);background:var(--c-primary);color:var(--c-on-primary)}
.v-mx5 .kiemelt{margin-top:30px}
@container elo (max-width:860px){.v-mx5 .grid{grid-template-columns:1fr}}
"""),
    ]
    return out


# ================================================================ MIÉRT ÉRDEMES (20. blokk): mind a 6 kártya, balra zárt szöveggel
def tenyek():
    c = ctx()
    t = c["tenyek"]
    el = t["elemek"]

    def kartya(e, i, cls="krt"):
        return (f'<article class="{cls}" data-rv style="--i:{i}"><div class="krt-fej">{ik(e.get("ikon"))}<span class="kulcs">{esc(e["szam"])}</span></div>'
                f'<h3 class="krt-h">{md(e["cim"])}</h3><p class="krt-p">{md(e["szoveg"])}</p></article>')
    BAL = r"""
.v-%s,.v-%s .shead{text-align:left}
.v-%s .krt,.v-%s .krt *{text-align:left}
.v-%s .kulcs{font-family:var(--f-label);font-size:.72rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--hl)}
.v-%s .krt-h{font-size:var(--t-h3);margin:2px 0 4px}
.v-%s .krt-p{line-height:1.6}
"""

    def bal(v):
        return BAL.replace("%s", v)
    return [
        dict(id="p1", nev="Kártyarács, 3 × 2", leiras="Hat kártya két sorban, hármasával: ikon, kulcsszó, cím és a teljes szöveg balra zárva. A kártyák a választott kártyastílust kapják.",
             html=sec("tx1", "tenyek", "s-white", f'<div class="wrap">{sh(t)}<div class="racs" style="--oszlop:3">'
                      + "".join(kartya(e, i) for i, e in enumerate(el)) + "</div></div>"),
             css=bal("tx1") + ".v-tx1 .shead{text-align:center}.v-tx1 .racs{align-items:stretch}"),
        dict(id="p5", nev="Számozott, két hasábban", leiras="Szerkesztőségi lista: nagy sorszám (01–06), mellette a cím és a szöveg, két hasábban, vékony elválasztó vonalakkal. Kártya nélkül, levegős.",
             html=sec("tx2", "tenyek", "s-paper", f'<div class="wrap">{sh(t, bal=True)}<ol class="lista">'
                      + "".join(f'<li data-rv style="--i:{i}"><b class="n">{i + 1:02d}</b><div><span class="kulcs">{esc(e["szam"])}</span>'
                                f'<h3 class="krt-h">{md(e["cim"])}</h3><p class="krt-p">{md(e["szoveg"])}</p></div></li>' for i, e in enumerate(el))
                      + "</ol></div>", masod=True),
             css=bal("tx2") + r"""
.v-tx2 .lista{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:30px clamp(30px,5cqi,70px)}
.v-tx2 li{display:flex;gap:18px;padding-top:18px;border-top:1px solid var(--c-line2)}
.v-tx2 .n{font-family:var(--f-display);font-weight:var(--w-display);font-size:2.2rem;line-height:1;color:var(--hl);flex:none;min-width:2.2ch}
.v-tx2 .krt-p{color:var(--c-ink-2);margin:0}
@container elo (max-width:760px){.v-tx2 .lista{grid-template-columns:1fr}}
"""),
        dict(id="p3", nev="Váltakozó sávok", leiras="Minden előny egy teljes szélességű sáv: balra nagy ikon és kulcsszó, jobbra a cím és a szöveg; a sávok háttere váltakozik. Nyugodt, jól olvasható hosszú szövegnél is.",
             html=sec("tx3", "tenyek", "s-paper", f'<div class="wrap">{sh(t)}<div class="savok">'
                      + "".join(f'<div class="sav" data-rv><div class="bal">{ik(e.get("ikon"))}<span class="kulcs">{esc(e["szam"])}</span></div>'
                                f'<div class="jobb"><h3 class="krt-h">{md(e["cim"])}</h3><p class="krt-p">{md(e["szoveg"])}</p></div></div>' for e in el)
                      + "</div></div>"),
             css=bal("tx3") + r"""
.v-tx3 .shead{text-align:center}
.v-tx3 .savok{display:grid;gap:10px;max-width:960px;margin:0 auto}
.v-tx3 .sav{display:grid;grid-template-columns:180px 1fr;gap:clamp(18px,3cqi,40px);align-items:start;padding:clamp(20px,3cqi,32px);border-radius:var(--r)}
.v-tx3 .sav:nth-child(odd){background:var(--c-tint)}.v-tx3 .sav:nth-child(even){background:var(--c-card)}
.v-tx3 .bal{display:flex;flex-direction:column;gap:10px}.v-tx3 .bal .ik{--ik:64px}
.v-tx3 .krt-p{color:var(--c-ink-2);margin:0}
@container elo (max-width:640px){.v-tx3 .sav{grid-template-columns:1fr}.v-tx3 .bal{flex-direction:row;align-items:center}}
"""),
        dict(id="p4", nev="Sötét, kulcsszavas", leiras="Sötét szekció, a kártyák fölött nagy kulcsszavak (Izgalom, Figyelem, Biztonság…) a kiemelő színnel, alattuk a cím és a szöveg. Erős, férfias.",
             html=sec("tx4", "tenyek", "s-deep", f'<div class="wrap">{sh(t)}<div class="racs" style="--oszlop:3">'
                      + "".join(f'<article class="elem" data-rv style="--i:{i}"><div class="fej">{ik(e.get("ikon"))}<b class="nagy">{esc(e["szam"])}</b></div>'
                                f'<h3 class="krt-h">{md(e["cim"])}</h3><p class="krt-p">{md(e["szoveg"])}</p></article>' for i, e in enumerate(el))
                      + "</div></div>"),
             css=bal("tx4") + r"""
.v-tx4 .shead{text-align:center}
.v-tx4 .elem{border-top:1px solid var(--c-line2);padding-top:20px}
.v-tx4 .fej{display:flex;align-items:center;gap:12px;margin-bottom:8px}.v-tx4 .fej .ik{--ik:44px}
.v-tx4 .nagy{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,2.6cqi,2.1rem);line-height:1;color:var(--c-deep-hl)}
.v-tx4 .krt-h{color:var(--c-on-deep)}.v-tx4 .krt-p{color:var(--c-on-deep-2);margin:0}
"""),
        dict(id="p6", nev="Ikonos lista oldalcímmel", leiras="Balra a szakasz címe (görgetéskor a helyén marad), jobbra egymás alatt a hat előny: ikon, cím, szöveg, vékony vonalakkal elválasztva. Rendezett, szerkesztőségi.",
             html=sec("tx5", "tenyek", "s-sand", f'<div class="wrap grid"><div class="oldal">{sh(t, bal=True)}</div><div class="lista">'
                      + "".join(f'<div class="sor" data-rv>{ik(e.get("ikon"))}<div><span class="kulcs">{esc(e["szam"])}</span>'
                                f'<h3 class="krt-h">{md(e["cim"])}</h3><p class="krt-p">{md(e["szoveg"])}</p></div></div>' for e in el)
                      + "</div></div>", masod=True),
             css=bal("tx5") + r"""
.v-tx5 .grid{display:grid;grid-template-columns:.75fr 1.25fr;gap:clamp(30px,5cqi,80px);align-items:start}
.v-tx5 .oldal{position:sticky;top:30px}
.v-tx5 .sor{display:grid;grid-template-columns:56px 1fr;gap:18px;padding:22px 0;border-bottom:1px solid var(--c-line2)}
.v-tx5 .sor:first-child{padding-top:0}.v-tx5 .sor .ik{--ik:52px}
.v-tx5 .krt-p{color:var(--c-ink-2);margin:0}
@container elo (max-width:820px){.v-tx5 .grid{grid-template-columns:1fr}.v-tx5 .oldal{position:relative;top:0}}
"""),
    ]


# ================================================================ KINEK SZÓL (egyedi)
def kinek():
    c = ctx()
    igen = "".join(f'<li data-rv style="--i:{i}">{md(x)}</li>' for i, x in enumerate(K["igen"]))
    nem = "".join(f'<li data-rv>{md(x)}</li>' for x in K["nem"])
    out = [
        dict(id="kx1", nev="Igen / nem két hasáb", leiras="Balra pipákkal, kinek szól; jobbra áthúzott jellel, kinek nem. Alul a lényeg: annak, aki hajlandó gyakorolni. Őszinte, gyorsan eldönthető.",
             html=sec("kx1", "kinek", "s-paper", f'<div class="wrap">{sh(K)}<div class="grid"><div class="igen krt"><ul>{igen}</ul><p class="is">{md(K["is"])}</p></div>'
                      f'<div class="nem"><p class="cmk">Kinek nem?</p><ul>{nem}</ul></div></div><p class="zaro" data-rv>{md(K["zaro"])}</p></div>'),
             css=r"""
.v-kx1 .grid{display:grid;grid-template-columns:1.35fr .9fr;gap:var(--gap);align-items:stretch}
.v-kx1 .igen ul{display:grid;gap:14px}.v-kx1 .igen li{padding-left:38px;position:relative;font-size:1.06rem;font-weight:600;color:var(--c-head)}
.v-kx1 .igen li::before{content:"";position:absolute;left:0;top:.1em;width:24px;height:24px;border-radius:50%;background:var(--c-primary)}
.v-kx1 .igen li::after{content:"";position:absolute;left:7px;top:.42em;width:10px;height:5px;border-left:2px solid var(--c-on-primary);border-bottom:2px solid var(--c-on-primary);transform:rotate(-45deg)}
.v-kx1 .is{margin-top:18px;color:var(--c-ink-2);font-size:.97rem}
.v-kx1 .nem{border:1px dashed var(--c-line2);border-radius:var(--r);padding:clamp(22px,3cqi,32px)}
.v-kx1 .cmk{font-family:var(--f-label);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3)}
.v-kx1 .nem ul{display:grid;gap:12px}.v-kx1 .nem li{padding-left:28px;position:relative;color:var(--c-ink-2)}
.v-kx1 .nem li::before{content:"×";position:absolute;left:4px;top:-.1em;font-size:1.3rem;color:var(--c-ink-3)}
.v-kx1 .zaro{text-align:center;margin-top:34px;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.3rem,2.4cqi,1.9rem);color:var(--hl)}
@container elo (max-width:600px){.v-kx1 .grid{grid-template-columns:1fr}}
"""),
        dict(id="kx2", nev="Fotó a tengerparton", leiras="Balra a tengert néző férfi (új életszakasz), jobbra a „Neked szól, ha…” lista. Csendes, elgondolkodtató, azonosulni hív.",
             html=sec("kx2", "kinek", "s-white", f'<div class="wrap grid"><div class="kep" data-rv>{foto(c, "tenger", "4/5")}</div><div>{sh(K, bal=True)}'
                      f'<ul class="igen">{igen}</ul><p class="is" data-rv>{md(K["is"])}</p><div class="nem" data-rv><ul>{nem}</ul></div><p class="zaro" data-rv>{md(K["zaro"])}</p></div></div>', masod=True),
             css=r"""
.v-kx2 .grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(30px,5cqi,80px);align-items:center}
.v-kx2 .shead{margin-bottom:22px}
.v-kx2 .igen{display:grid;gap:12px;margin-bottom:18px}.v-kx2 .igen li{padding:12px 16px 12px 46px;position:relative;background:var(--c-tint);border-radius:12px;font-weight:600}
.v-kx2 .igen li::before{content:"";position:absolute;left:16px;top:50%;width:16px;height:16px;margin-top:-8px;background:var(--c-primary);-webkit-mask:var(--m2) center/contain no-repeat;mask:var(--m2) center/contain no-repeat}
.v-kx2 .is{color:var(--c-ink-2)}
.v-kx2 .nem{font-size:.92rem;color:var(--c-ink-3);border-left:2px solid var(--c-line2);padding-left:14px;margin:16px 0}
.v-kx2 .zaro{font-family:var(--f-display);font-weight:var(--w-display);font-size:var(--t-h3);color:var(--hl);margin:0}
@container elo (max-width:860px){.v-kx2 .grid{grid-template-columns:1fr}.v-kx2 .kep{max-width:420px}}
"""),
        dict(id="kx3", nev="Három élethelyzet-kártya", leiras="A három élethelyzet három számozott kártyán, alatta egy sötét sáv a lényeggel. Rendezett, könnyen átfutható.",
             html=sec("kx3", "kinek", "s-tint", f'<div class="wrap">{sh(K)}<div class="racs" style="--oszlop:3">'
                      + "".join(f'<article class="krt" data-rv style="--i:{i}"><span class="n">0{i + 1}</span><p class="krt-p">{md(x)}</p></article>' for i, x in enumerate(K["igen"]))
                      + f'</div><p class="is" data-rv>{md(K["is"])}</p><div class="sav s-deep" data-rv><ul>{nem}</ul><b>{md(K["zaro"])}</b></div></div>'),
             css=r"""
.v-kx3 .krt .n{font-family:var(--f-display);font-weight:var(--w-display);font-size:2.2rem;line-height:1;color:var(--hl)}
.v-kx3 .krt .krt-p{font-size:1.04rem;color:var(--c-head);font-weight:600}
.v-kx3 .is{max-width:64ch;margin:30px auto;text-align:center;color:var(--c-ink-2)}
.v-kx3 .sav{display:flex;gap:24px;align-items:center;justify-content:space-between;flex-wrap:wrap;background:var(--c-deep);border-radius:var(--r);padding:22px clamp(20px,3cqi,36px)}
.v-kx3 .sav ul{display:grid;gap:4px;font-size:.92rem;color:var(--c-on-deep-2)}.v-kx3 .sav b{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.25rem;color:var(--c-deep-hl)}
"""),
        dict(id="kx4", nev="Középre zárt, nagy mondatok", leiras="Csak tipográfia: a három élethelyzet nagy, egymás alatti mondatként, mint egy vers. Elegáns, sok levegővel.",
             html=sec("kx4", "kinek", "s-sand", f'<div class="wrap szuk">{sh(K)}<ul class="vers">{igen}</ul><p class="is" data-rv>{md(K["is"])}</p>'
                      f'<p class="nem" data-rv>{" ".join(md(x) for x in K["nem"])}</p><p class="zaro kezi" data-rv>{md(K["zaro"])}</p></div>'),
             css=r"""
.v-kx4 .vers{display:grid;gap:18px;text-align:center;margin-bottom:30px}
.v-kx4 .vers li{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.25rem,2.6cqi,1.9rem);line-height:1.25;color:var(--c-head)}
.v-kx4 .vers li+li::before{content:"";display:block;width:8px;height:8px;margin:0 auto 18px;border-radius:50%;background:var(--c-accent)}
.v-kx4 .is,.v-kx4 .nem{text-align:center;color:var(--c-ink-2);max-width:60ch;margin-left:auto;margin-right:auto}
.v-kx4 .nem{font-size:.92rem;color:var(--c-ink-3)}
.v-kx4 .zaro{text-align:center;font-size:calc(var(--fs-hand)*1.6rem);margin-top:20px}
"""),
        dict(id="kx5", nev="Edzésnapló-pipák", leiras="Egy edzésnapló-lap jelölőnégyzetekkel: a három élethelyzet kipipálva, alul üresen a „hajlandó vagyok rendszeresen gyakorolni” sor. A látogató maga pipálja ki fejben.",
             html=sec("kx5", "kinek", "s-paper", f'<div class="wrap szuk">{sh(K)}<div class="naplo krt" data-rv><ul>'
                      + "".join(f'<li class="x"><i></i>{md(x)}</li>' for x in K["igen"])
                      + f'<li class="ures"><i></i><b>{md(K["zaro"])}</b></li></ul><p class="is">{md(K["is"])}</p><p class="nem">{" ".join(md(x) for x in K["nem"])}</p></div></div>'),
             css=r"""
.v-kx5 .naplo ul{display:grid;gap:0}
.v-kx5 .naplo li{display:flex;gap:16px;align-items:flex-start;padding:14px 0;border-bottom:1px solid var(--c-line);font-size:1.04rem}
.v-kx5 .naplo i{flex:none;width:24px;height:24px;border:2px solid var(--c-ink-2);border-radius:4px;position:relative;margin-top:2px}
.v-kx5 .naplo .x i::after{content:"";position:absolute;left:5px;top:1px;width:8px;height:13px;border-right:3px solid var(--c-primary);border-bottom:3px solid var(--c-primary);transform:rotate(40deg)}
.v-kx5 .naplo .ures i{border-color:var(--c-primary);border-style:dashed}.v-kx5 .naplo .ures b{color:var(--hl)}
.v-kx5 .is{margin-top:20px;color:var(--c-ink-2)}.v-kx5 .nem{font-size:.9rem;color:var(--c-ink-3);margin:0}
"""),
    ]
    return out


# ================================================================ VÉLEMÉNYEK (egyedi)
def velemenyek():
    c = ctx()
    q = V["idezetek"]

    def kiem(t, k):
        e = esc(t)
        ke = esc(k)
        return e.replace(ke, f"<mark>{ke}</mark>", 1)
    out = [
        dict(id="vx1", nev="Kártyafal", leiras="A négy beszámoló egyenetlen magasságú kártyákon, egy-egy kiemelt mondattal. Rendezett, sok szöveget is elbír.",
             html=sec("vx1", "velemenyek", "s-tint", f'<div class="wrap">{sh(V)}<div class="fal">'
                      + "".join(f'<blockquote class="krt" data-rv style="--i:{i}"><p>„{kiem(x, V["kiemelt"][i])}”</p></blockquote>' for i, x in enumerate(q))
                      + "</div></div>", anchor="velemenyek"),
             css=r"""
.v-vx1 .fal{columns:2;column-gap:var(--gap)}
.v-vx1 .krt{break-inside:avoid;margin:0 0 var(--gap)}
.v-vx1 .krt p{margin:0;font-size:1rem;line-height:1.6}
.v-vx1 .krt mark{font-weight:800;color:var(--hl)}
.v-vx1 .krt::before{content:"“";position:absolute;right:16px;top:-6px;font-family:var(--f-display);font-size:5rem;line-height:1;color:var(--c-accent);opacity:.35}
@container elo (max-width:760px){.v-vx1 .fal{columns:1}}
"""),
        dict(id="vx2", nev="Egy nagy és három kisebb", leiras="Az első beszámoló kiemelve, óriás idézőjellel; a többi három mellette kisebb kártyákon. Erős első benyomás.",
             html=sec("vx2", "velemenyek", "s-white", f'<div class="wrap">{sh(V)}<div class="grid"><blockquote class="nagy" data-rv><p>„{kiem(q[0], V["kiemelt"][0])}”</p></blockquote>'
                      f'<div class="kicsik">' + "".join(f'<blockquote class="krt" data-rv style="--i:{i}"><p>„{kiem(x, V["kiemelt"][i + 1])}”</p></blockquote>' for i, x in enumerate(q[1:]))
                      + "</div></div></div>", anchor="velemenyek", masod=True),
             css=r"""
.v-vx2 .grid{display:grid;grid-template-columns:1fr 1fr;gap:var(--gap);align-items:start}
.v-vx2 .nagy{margin:0;position:relative;padding:clamp(30px,4cqi,50px);background:var(--c-primary);color:var(--c-on-primary);border-radius:var(--r);position:sticky;top:20px}
.v-vx2 .nagy::before{content:"“";display:block;font-family:var(--f-display);font-size:7rem;line-height:.6;opacity:.5;margin-bottom:6px}
.v-vx2 .nagy p{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.15rem,2cqi,1.5rem);line-height:1.35;margin:0}
.v-vx2 .nagy mark{color:inherit;text-decoration:underline;text-decoration-color:var(--c-accent);text-underline-offset:.2em}
.v-vx2 .kicsik{display:grid;gap:var(--gap)}.v-vx2 .krt{margin:0}.v-vx2 .krt p{margin:0;font-size:.97rem}.v-vx2 .krt mark{font-weight:800;color:var(--hl)}
@container elo (max-width:600px){.v-vx2 .grid{grid-template-columns:1fr}.v-vx2 .nagy{position:relative;top:0}}
"""),
        dict(id="vx3", nev="Gyertyafényes, sötét", leiras="Sötét szekció, a beszámolók narancs idézőjelekkel, két hasábban; a kiemelt mondatok meleg fényben. Intim, személyes, mint egy esti beszélgetés.",
             html=sec("vx3", "velemenyek", "s-deep", f'<div class="wrap">{sh(V)}<div class="grid">'
                      + "".join(f'<blockquote data-rv style="--i:{i}"><p>{kiem(x, V["kiemelt"][i])}</p></blockquote>' for i, x in enumerate(q))
                      + "</div></div>", anchor="velemenyek"),
             css=r"""
.v-vx3 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(26px,4cqi,56px) clamp(30px,5cqi,70px)}
.v-vx3 blockquote{margin:0;position:relative;padding-left:46px}
.v-vx3 blockquote::before{content:"“";position:absolute;left:0;top:-14px;font-family:var(--f-display);font-size:4.4rem;line-height:1;color:var(--c-deep-hl)}
.v-vx3 p{margin:0;color:var(--c-on-deep-2);font-size:1rem}
.v-vx3 mark{color:var(--c-on-deep);font-weight:800;background:radial-gradient(ellipse at 50% 60%,color-mix(in srgb,var(--c-primary) 35%,transparent),transparent 70%)}
@container elo (max-width:760px){.v-vx3 .grid{grid-template-columns:1fr}}
"""),
        dict(id="vx4", nev="Naplóbejegyzések", leiras="A beszámolók edzésnapló-bejegyzésként: sorszám, vonalas lap, kézírásos kiemelés a margón. Az edzésterv világában marad.",
             html=sec("vx4", "velemenyek", "s-paper", f'<div class="wrap">{sh(V)}<div class="racs" style="--oszlop:2">'
                      + "".join(f'<article class="bej" data-rv style="--i:{i}"><span class="n">Bejegyzés 0{i + 1}</span><p>„{esc(x)}”</p>'
                                f'<span class="kezi">{esc(V["kiemelt"][i])}</span></article>' for i, x in enumerate(q))
                      + "</div></div>", anchor="velemenyek", masod=True),
             css=r"""
.v-vx4 .bej{position:relative;background-color:var(--c-card);border:1px solid var(--c-line);border-radius:4px;padding:26px 24px 26px 54px;box-shadow:var(--sh-1);background-image:repeating-linear-gradient(180deg,transparent 0 27px,color-mix(in srgb,var(--c-primary) 9%,transparent) 27px 28px);background-position:0 46px}
.v-vx4 .bej::before{content:"";position:absolute;left:34px;top:0;bottom:0;border-left:1.5px solid color-mix(in srgb,var(--c-primary) 45%,transparent)}
.v-vx4 .n{display:block;font-family:var(--f-label);font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3);margin-bottom:10px}
.v-vx4 p{font-size:.97rem;line-height:28px;margin:0 0 10px}
.v-vx4 .kezi{display:inline-block;transform:rotate(-2deg);font-size:calc(var(--fs-hand)*1.1rem)}
"""),
        dict(id="vx5", nev="Vízszintes sín", leiras="A beszámolók oldalra görgethető, magas kártyákon; mobilon ujjal lapozható. Kevés helyen mind elfér.",
             html=sec("vx5", "velemenyek", "s-sand", f'<div class="wrap">{sh(V, bal=True)}</div><div class="sin">'
                      + "".join(f'<blockquote class="krt" data-rv style="--i:{i}"><b class="ki">„{esc(V["kiemelt"][i])}”</b><p>{esc(x)}</p></blockquote>' for i, x in enumerate(q))
                      + "</div>", anchor="velemenyek"),
             css=r"""
.v-vx5 .sin{display:flex;gap:var(--gap);overflow-x:auto;scroll-snap-type:x mandatory;padding:6px max(var(--pad),calc(50% - 560px)) 26px;position:relative;z-index:2}
.v-vx5 .krt{flex:0 0 min(420px,82%);scroll-snap-align:start;margin:0}
.v-vx5 .ki{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.2rem,2cqi,1.5rem);line-height:1.2;color:var(--hl);margin-bottom:12px}
.v-vx5 p{margin:0;font-size:.95rem;color:var(--c-ink-2)}
"""),
    ]
    return out


# ================================================================ GARANCIA (egyedi)
def garancia():
    g1, g2 = G["g"]

    def gk(g, i, cls="krt"):
        return (f'<article class="{cls} g{i}" data-rv style="--i:{i}"><span class="ido">{esc(g["ido"])}</span><h3>{esc(g["nev"])}</h3>'
                f'<p class="fo">{esc(g["fo"])}</p><p class="sz">{mdk(g["szoveg"])}</p><p class="zr">{mdk(g["zaro"])}</p></article>')
    out = [
        dict(id="gx1", nev="Két pecsét", leiras="Két nagy, kerek pecsét (24 óra, 13. hét), alattuk a garancia szövege. Mint két hivatalos ígéret. Megnyugtató, kézzelfogható.",
             html=sec("gx1", "garancia", "s-paper", f'<div class="wrap">{sh(G)}<div class="racs" style="--oszlop:2">{gk(g1, 0, "gar")}{gk(g2, 1, "gar")}</div></div>'),
             css=r"""
.v-gx1 .gar{text-align:center;display:flex;flex-direction:column;align-items:center}
.v-gx1 .ido{display:grid;place-items:center;width:132px;height:132px;border-radius:50%;background:var(--c-primary);color:var(--c-on-primary);font-family:var(--f-display);font-weight:var(--w-display);font-size:1.6rem;line-height:1;box-shadow:0 0 0 6px var(--sec-bg),0 0 0 8px var(--c-primary);margin-bottom:24px;transform:rotate(-6deg)}
.v-gx1 .g1 .ido{background:var(--c-deep);box-shadow:0 0 0 6px var(--sec-bg),0 0 0 8px var(--c-deep);color:var(--c-deep-hl);transform:rotate(5deg)}
.v-gx1 h3{font-size:var(--t-h3);margin-bottom:8px}.v-gx1 .fo{font-weight:800;color:var(--hl)}
.v-gx1 .sz{color:var(--c-ink-2);font-size:.96rem;max-width:46ch}.v-gx1 .zr{font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.15rem);color:var(--c-hand);margin:0}
"""),
        dict(id="gx2", nev="Két oklevél", leiras="A garanciák kettős keretes, oklevélszerű lapokon, aláírás-sorral. Klasszikus, hivatalos, komolyan vehető.",
             html=sec("gx2", "garancia", "s-sand", f'<div class="wrap">{sh(G)}<div class="racs" style="--oszlop:2">{gk(g1, 0, "okl")}{gk(g2, 1, "okl")}</div></div>', masod=True),
             css=r"""
.v-gx2 .okl{background:var(--c-card);padding:clamp(28px,4cqi,48px);text-align:center;border:1px solid var(--c-line2);outline:3px double var(--c-primary);outline-offset:-14px;box-shadow:var(--sh-2)}
.v-gx2 .ido{font-family:var(--f-label);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--c-ink-3)}
.v-gx2 h3{font-size:clamp(1.3rem,2.2cqi,1.7rem);margin:10px 0}.v-gx2 .fo{font-weight:800;color:var(--hl)}
.v-gx2 .sz{color:var(--c-ink-2);font-size:.95rem}
.v-gx2 .zr{margin:22px auto 0;padding-top:12px;border-top:1px solid var(--c-line2);max-width:280px;font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.1rem);color:var(--c-hand)}
"""),
        dict(id="gx3", nev="Sötét, kettéosztva", leiras="Sötét szekció, a két garancia egymás mellett, közöttük egy vékony narancs fénycsík. Prémium, határozott.",
             html=sec("gx3", "garancia", "s-deep", f'<div class="wrap">{sh(G)}<div class="osztott">{gk(g1, 0, "fel")}{gk(g2, 1, "fel")}</div></div>'),
             css=r"""
.v-gx3 .osztott{display:grid;grid-template-columns:1fr 1fr;position:relative}
.v-gx3 .osztott::before{content:"";position:absolute;left:50%;top:6%;bottom:6%;width:2px;background:linear-gradient(transparent,var(--c-primary),transparent)}
.v-gx3 .fel{padding:10px clamp(20px,4cqi,56px)}
.v-gx3 .ido{display:inline-block;font-family:var(--f-label);font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-deep);background:var(--c-deep-hl);padding:5px 10px;border-radius:3px}
.v-gx3 h3{font-size:clamp(1.3rem,2.4cqi,1.8rem);margin:14px 0 8px;color:var(--c-on-deep)}
.v-gx3 .fo{font-weight:800;color:var(--c-deep-hl)}.v-gx3 .sz{color:var(--c-on-deep-2)}.v-gx3 .zr{color:var(--c-on-deep);font-style:italic}
@container elo (max-width:760px){.v-gx3 .osztott{grid-template-columns:1fr;gap:30px}.v-gx3 .osztott::before{display:none}}
"""),
        dict(id="gx4", nev="Idővonal: 24 óra → 13. hét", leiras="Egy vízszintes idővonal a vásárlástól a 13. hétig; rajta a két garancia ott, ahol érvényes. Egyértelművé teszi, mikor mit kérhetsz.",
             html=sec("gx4", "garancia", "s-white", f'<div class="wrap">{sh(G)}<div class="vonal" data-rv><span class="p0">Vásárlás</span><span class="p1">24 óra</span>'
                      + "".join(f'<i style="left:{8 + i * 6.8:.1f}%"></i>' for i in range(12)) + '<span class="p2">12 hét</span><span class="p3">13. hét</span></div>'
                      f'<div class="racs" style="--oszlop:2">{gk(g1, 0)}{gk(g2, 1)}</div></div>', masod=True),
             css=r"""
.v-gx4 .vonal{position:relative;height:74px;margin:0 0 34px}
.v-gx4 .vonal::before{content:"";position:absolute;left:0;right:0;top:36px;height:3px;background:linear-gradient(90deg,var(--c-primary) 0 9%,var(--c-line2) 9% 90%,var(--c-primary) 90%)}
.v-gx4 .vonal i{position:absolute;top:31px;width:12px;height:12px;border-radius:50%;background:var(--c-card);border:2px solid var(--c-line2)}
.v-gx4 .vonal span{position:absolute;top:0;font-family:var(--f-label);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c-ink-2);white-space:nowrap}
.v-gx4 .vonal span::after{content:"";position:absolute;left:50%;top:26px;width:18px;height:18px;margin-left:-9px;border-radius:50%;background:var(--c-primary);box-shadow:0 0 0 5px color-mix(in srgb,var(--c-primary) 18%,transparent)}
.v-gx4 .vonal .p0{left:0}.v-gx4 .vonal .p1{left:6%;top:56px}.v-gx4 .vonal .p1::after{top:-24px}.v-gx4 .p2{left:83%}.v-gx4 .p3{right:0}
.v-gx4 .p0::after{background:var(--c-ink)!important}.v-gx4 .p2::after{background:var(--c-line2)!important;box-shadow:none!important}
.v-gx4 .ido{font-family:var(--f-label);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--hl)}
.v-gx4 h3{font-size:var(--t-h3)}.v-gx4 .fo{font-weight:800;color:var(--c-head);margin:0}.v-gx4 .sz{color:var(--c-ink-2);font-size:.95rem;margin:0}.v-gx4 .zr{font-style:italic;color:var(--c-ink-2);margin:0}
@container elo (max-width:600px){.v-gx4 .vonal span{font-size:.6rem}}
"""),
        dict(id="gx5", nev="Nagy sorszámok", leiras="Két nagy kártya óriási 1-es és 2-es sorszámmal, a garancia neve kiemelve. Egyszerű, erős, merész.",
             html=sec("gx5", "garancia", "s-tint", f'<div class="wrap">{sh(G)}<div class="racs" style="--oszlop:2">'
                      + "".join(f'<article class="krt" data-rv><b class="nagyn">{i + 1}</b><h3>{esc(g["nev"])}</h3><p class="fo">{esc(g["fo"])}</p>'
                                f'<p class="sz">{mdk(g["szoveg"])}</p><p class="zr">{mdk(g["zaro"])}</p></article>' for i, g in enumerate(G["g"]))
                      + "</div></div>"),
             css=r"""
.v-gx5 .nagyn{position:absolute;right:18px;top:-10px;font-family:var(--f-display);font-weight:800;font-size:7rem;line-height:1;color:var(--c-primary);opacity:.18}
.v-gx5 h3{font-size:clamp(1.3rem,2.2cqi,1.7rem);position:relative}.v-gx5 .fo{font-weight:800;color:var(--hl);margin:0}
.v-gx5 .sz{color:var(--c-ink-2);font-size:.95rem;margin:0}.v-gx5 .zr{font-weight:700;margin:0}
"""),
    ]
    return out


# ================================================================ GYIK (egyedi)
def gyik():
    k = Q["k"]
    cta = f'<div class="lab" data-rv>{btn(Q["cta"])}</div>'

    def acc(cls=""):
        return "".join(f'<details class="{cls}" data-rv style="--i:{i}"{" open" if i == 2 else ""}><summary><span class="n">{i + 1:02d}</span>'
                       f'<span class="q">{esc(a)}</span><i></i></summary><div class="v"><p>{mdg(b)}</p></div></details>' for i, (a, b) in enumerate(k))
    ACC = r"""
.v-%s details{border-bottom:1px solid var(--c-line2)}
.v-%s summary{list-style:none;cursor:pointer;display:flex;gap:16px;align-items:center;padding:18px 0;font-weight:700;font-size:1.05rem;color:var(--c-head)}
.v-%s summary::-webkit-details-marker{display:none}
.v-%s summary .q{flex:1}.v-%s summary .n{font-family:var(--f-label);font-size:.78rem;color:var(--hl)}
.v-%s summary i{flex:none;width:28px;height:28px;border-radius:50%;border:1.5px solid var(--c-line2);position:relative;transition:transform .3s var(--ease)}
.v-%s summary i::before,.v-%s summary i::after{content:"";position:absolute;left:50%;top:50%;width:12px;height:1.5px;margin:-.75px 0 0 -6px;background:currentColor}
.v-%s summary i::after{transform:rotate(90deg)}.v-%s details[open] summary i{transform:rotate(45deg);background:var(--c-primary);color:var(--c-on-primary);border-color:var(--c-primary)}
.v-%s .v p{margin:0 0 18px 44px;color:var(--c-ink-2);max-width:62ch}
.v-%s .lab{display:flex;justify-content:center;margin-top:36px}
"""
    out = [
        dict(id="qx1", nev="Lenyíló lista", leiras="Klasszikus harmonika: kattintásra nyílik a válasz, sorszámmal és kerek plusz-jellel. Rendezett, sok kérdést elbír.",
             html=sec("qx1", "gyik", "s-paper", f'<div class="wrap szuk">{sh(Q)}<div class="lista">{acc()}</div>{cta}</div>'),
             css=ACC.replace("%s", "qx1")),
        dict(id="qx2", nev="Kártyarács", leiras="Minden kérdés egy kártya, a válasz rögtön látszik. Két hasáb, gyorsan átfutható, nincs mit kinyitni.",
             html=sec("qx2", "gyik", "s-tint", f'<div class="wrap">{sh(Q)}<div class="racs" style="--oszlop:2">'
                      + "".join(f'<article class="krt" data-rv style="--i:{i}"><h3 class="krt-h">{esc(a)}</h3><p class="krt-p">{mdg(b)}</p></article>' for i, (a, b) in enumerate(k))
                      + f'</div>{cta}</div>', masod=True),
             css=".v-qx2 .krt-h{font-size:1.08rem}.v-qx2 .lab{display:flex;justify-content:center;margin-top:36px}"),
        dict(id="qx3", nev="Beszélgetés-buborékok", leiras="Kérdés és válasz chat-buborékokban, mintha Kiranának írnál, és ő válaszolna. Közvetlen, oldja a téma feszültségét.",
             html=sec("qx3", "gyik", "s-white", f'<div class="wrap szuk">{sh(Q)}<div class="chat">'
                      + "".join(f'<div class="k" data-rv>{esc(a)}</div><div class="v" data-rv>{mdg(b)}</div>' for a, b in k)
                      + f'</div>{cta}</div>'),
             css=r"""
.v-qx3 .chat{display:flex;flex-direction:column;gap:10px}
.v-qx3 .k{align-self:flex-end;max-width:78%;background:var(--c-primary);color:var(--c-on-primary);padding:12px 18px;border-radius:20px 20px 4px 20px;font-weight:700}
.v-qx3 .v{align-self:flex-start;max-width:78%;background:var(--c-tint);color:var(--c-ink);padding:12px 18px;border-radius:20px 20px 20px 4px;margin-bottom:14px}
.v-qx3 .lab{display:flex;justify-content:center;margin-top:30px}
"""),
        dict(id="qx4", nev="Oldalcím + lista", leiras="Balra a szekció címe és a fő gomb (ragad görgetéskor), jobbra a lenyíló kérdések. Szerkesztőségi, rendezett.",
             html=sec("qx4", "gyik", "s-sand", f'<div class="wrap grid"><div class="bal">{sh(Q, bal=True)}{cta}</div><div class="lista">{acc()}</div></div>', masod=True),
             css=ACC.replace("%s", "qx4") + r"""
.v-qx4 .grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(30px,5cqi,80px);align-items:start}
.v-qx4 .bal{position:sticky;top:30px}.v-qx4 .bal .lab{justify-content:flex-start;margin-top:0}
@container elo (max-width:820px){.v-qx4 .grid{grid-template-columns:1fr}.v-qx4 .bal{position:relative;top:0}}
"""),
        dict(id="qx5", nev="Számozott, nyitott", leiras="Nagy, serif sorszámok, minden válasz nyitva, két hasábban, mint egy tájékoztató füzet. Klasszikus, átlátható.",
             html=sec("qx5", "gyik", "s-paper", f'<div class="wrap">{sh(Q)}<ol class="sz">'
                      + "".join(f'<li data-rv style="--i:{i}"><b>{i + 1:02d}</b><div><h3>{esc(a)}</h3><p>{mdg(b)}</p></div></li>' for i, (a, b) in enumerate(k))
                      + f'</ol>{cta}</div>'),
             css=r"""
.v-qx5 .sz{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:28px clamp(30px,5cqi,70px)}
.v-qx5 li{display:flex;gap:18px;padding-top:16px;border-top:1px solid var(--c-line2)}
.v-qx5 li>b{font-family:var(--f-display);font-weight:var(--w-display);font-size:2rem;line-height:1;color:var(--hl);font-style:italic}
.v-qx5 h3{font-size:1.08rem;margin-bottom:6px}.v-qx5 p{margin:0;color:var(--c-ink-2)}.v-qx5 p b{color:var(--c-head)}
.v-qx5 .lab{display:flex;justify-content:center;margin-top:40px}
@container elo (max-width:760px){.v-qx5 .sz{grid-template-columns:1fr}}
"""),
    ]
    return out


# ================================================================ MI A TANTRASZEX EDZÉSTERV? (egyedi)
def mia():
    c = ctx()
    nem = "".join(f'<li data-rv style="--i:{i}">{esc(x)}</li>' for i, x in enumerate(MIA["nem"]))
    het = f'<p class="het" data-rv>{md(MIA["het"])}</p>'
    sport = f'<p class="sport" data-rv>{md(MIA["sport"])}</p>'
    cel = f'<p class="cel" data-rv>{md(MIA["cel"])}</p>'
    ritmus = f'<p class="ritmus" data-rv>{esc(MIA["ritmus"])}</p>'
    return [
        dict(id="mi1", nev="Ami nem, és ami igen", leiras="Balra áthúzva, ami nem (40 órányi videó, filozófia, pózok), jobbra egy kártyán, ami igen: 12 gyakorlat, 12 hét, hétről hétre. Tisztázza az elvárásokat.",
             html=sec("mi1", "mia", "s-white", f'<div class="wrap">{sh(MIA)}<div class="grid"><ul class="nem">{nem}</ul>'
                      f'<div class="igen krt" data-rv>{ritmus}{het}{sport}</div></div>{cel}</div>'),
             css=r"""
.v-mi1 .grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(24px,4cqi,60px);align-items:center}
.v-mi1 .nem{display:grid;gap:14px}
.v-mi1 .nem li{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.1rem,1.9cqi,1.45rem);color:var(--c-ink-2);text-decoration:line-through;text-decoration-color:color-mix(in srgb,var(--c-primary) 70%,transparent);text-decoration-thickness:1px}
.v-mi1 .ritmus{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,3cqi,2.3rem);color:var(--hl);margin:0 0 6px}
.v-mi1 .het{font-weight:700;color:var(--c-head)}.v-mi1 .sport{color:var(--c-ink-2);margin:0}
.v-mi1 .cel{text-align:center;margin:clamp(30px,4cqi,50px) auto 0;max-width:46ch;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.2rem,2.2cqi,1.7rem);line-height:1.3;color:var(--c-head)}
.v-mi1 .cel b{color:var(--hl)}
@container elo (max-width:760px){.v-mi1 .grid{grid-template-columns:1fr}}
"""),
        dict(id="mi2", nev="12 + 12", leiras="Két óriás szám egymás mellett (12 gyakorlat, 12 hét), alattuk a lényeg. Plakátos, egy pillantással érthető.",
             html=sec("mi2", "mia", "s-tint", f'<div class="wrap">{sh(MIA)}<div class="szamok" data-rv><div><b>12</b><span>gyakorlat</span></div>'
                      f'<i aria-hidden="true">×</i><div><b>12</b><span>hét</span></div></div>{het}<ul class="nem">{nem}</ul>{sport}{cel}</div>', masod=True),
             css=r"""
.v-mi2 .szamok{display:flex;justify-content:center;align-items:center;gap:clamp(18px,4cqi,50px);margin-bottom:18px}
.v-mi2 .szamok b{display:block;font-family:var(--f-display);font-weight:800;font-size:clamp(4.5rem,13cqi,9rem);line-height:.85;color:var(--hl);text-align:center}
.v-mi2 .szamok span{display:block;text-align:center;font-family:var(--f-label);font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;color:var(--c-ink-2)}
.v-mi2 .szamok i{font-style:normal;font-size:2.4rem;color:var(--c-ink-3)}
.v-mi2 .het{text-align:center;font-weight:700;font-size:1.08rem;color:var(--c-head)}
.v-mi2 .nem{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:18px 0 26px}
.v-mi2 .nem li{padding:6px 14px;border-radius:999px;border:1px dashed var(--c-line2);color:var(--c-ink-3);font-size:.92rem}
.v-mi2 .nem li::before{content:"✕ ";color:var(--c-primary)}
.v-mi2 .sport{max-width:60ch;margin:0 auto 14px;text-align:center;color:var(--c-ink-2)}
.v-mi2 .cel{max-width:52ch;margin:0 auto;text-align:center;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.15rem,2cqi,1.5rem);color:var(--c-head)}
.v-mi2 .cel b{color:var(--hl)}
"""),
        dict(id="mi3", nev="Edzésterv-lap", leiras="Egy edzésterv-lap 12 hetes rácsa: az oszlopok a hetek, mindegyikben egy gyakorlat-pötty. Mellette a szöveg. Az edzés metaforája szó szerint.",
             html=sec("mi3", "mia", "s-paper", f'<div class="wrap grid"><div>{sh(MIA, bal=True)}{het}{sport}<ul class="nem">{nem}</ul></div>'
                      f'<div class="lap krt" data-rv><p class="mono fej">Edzésterv · 12 hét · 12 gyakorlat</p><div class="hetek">'
                      + "".join(f'<span><i></i><small>{i + 1}.</small></span>' for i in range(12))
                      + f'</div>{cel}</div></div>'),
             css=r"""
.v-mi3 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5cqi,80px);align-items:center}
.v-mi3 .shead{margin-bottom:18px}.v-mi3 .het{font-weight:700;color:var(--c-head)}.v-mi3 .sport{color:var(--c-ink-2)}
.v-mi3 .nem{display:grid;gap:6px;margin-top:14px}.v-mi3 .nem li{color:var(--c-ink-3);padding-left:22px;position:relative}
.v-mi3 .nem li::before{content:"✕";position:absolute;left:0;color:var(--c-primary)}
.v-mi3 .fej{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3);margin:0 0 14px}
.v-mi3 .hetek{display:grid;grid-template-columns:repeat(6,1fr);gap:14px 8px;margin-bottom:20px}
.v-mi3 .hetek span{display:flex;flex-direction:column;align-items:center;gap:6px}
.v-mi3 .hetek i{width:30px;height:30px;border-radius:50%;border:2px solid var(--c-primary);background:color-mix(in srgb,var(--c-primary) 14%,transparent)}
.v-mi3 .hetek small{font-family:var(--f-label);font-size:.7rem;color:var(--c-ink-3)}
.v-mi3 .cel{margin:0;font-weight:600;color:var(--c-head)}.v-mi3 .cel b{color:var(--hl)}
@container elo (max-width:820px){.v-mi3 .grid{grid-template-columns:1fr}}
"""),
        dict(id="mi4", nev="Tudás → képesség", leiras="Sötét szekció, középen nagy betűkkel a cél: ne valami legyen, amit tudsz, hanem amire képes vagy. Alatta a program lényege. Erős, kiáltványszerű.",
             html=sec("mi4", "mia", "s-deep", f'<div class="wrap szuk">{sh(MIA)}<div class="valt" data-rv><span class="tud">amit tudsz</span>'
                      f'<span class="nyil" aria-hidden="true">→</span><span class="kep">amire képes vagy</span></div>{cel}{ritmus}{het}<ul class="nem">{nem}</ul>{sport}</div>'),
             css=r"""
.v-mi4 .valt{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:10px 22px;margin:6px 0 18px}
.v-mi4 .valt span{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,4cqi,3rem);line-height:1}
.v-mi4 .tud{color:var(--c-on-deep-2);text-decoration:line-through;text-decoration-thickness:1px;text-decoration-color:color-mix(in srgb,var(--c-deep-hl) 75%,transparent)}
.v-mi4 .kep{color:var(--c-deep-hl)}.v-mi4 .nyil{color:var(--c-on-deep-2)}
.v-mi4 .cel{text-align:center;color:var(--c-on-deep-2);margin-bottom:34px}
.v-mi4 .ritmus{text-align:center;font-family:var(--f-label);letter-spacing:.16em;text-transform:uppercase;color:var(--c-deep-hl);margin:0 0 6px}
.v-mi4 .het{text-align:center;font-weight:700;color:var(--c-on-deep)}
.v-mi4 .nem{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 24px;margin:16px 0}
.v-mi4 .nem li{color:var(--c-on-deep-2);font-size:.92rem}.v-mi4 .nem li::before{content:"✕ ";color:var(--c-deep-hl)}
.v-mi4 .sport{text-align:center;color:var(--c-on-deep-2);max-width:60ch;margin:0 auto}
"""),
        dict(id="mi5", nev="Kavicsok fotóval", leiras="A sorba rendezett kavicsok fotója (lépésről lépésre) mellett a szöveg, alul kiemelve a cél. Nyugodt, képszerű.",
             html=sec("mi5", "mia", "s-sand", f'<div class="wrap grid"><div class="kep" data-rv>{foto(c, "kovek", "4/5")}</div><div>{sh(MIA, bal=True)}'
                      f'{ritmus}{het}<ul class="nem">{nem}</ul>{sport}{cel}</div></div>', masod=True),
             css=r"""
.v-mi5 .grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(30px,5cqi,80px);align-items:center}
.v-mi5 .shead{margin-bottom:16px}
.v-mi5 .ritmus{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.5rem;color:var(--hl);margin:0 0 4px}
.v-mi5 .het{font-weight:700;color:var(--c-head)}
.v-mi5 .nem{display:grid;gap:6px;margin:12px 0 16px}.v-mi5 .nem li{padding-left:22px;position:relative;color:var(--c-ink-2)}
.v-mi5 .nem li::before{content:"✕";position:absolute;left:0;color:var(--c-primary)}
.v-mi5 .sport{color:var(--c-ink-2)}
.v-mi5 .cel{border-left:3px solid var(--c-primary);padding-left:16px;font-weight:600;color:var(--c-head);margin:0}.v-mi5 .cel b{color:var(--hl)}
@container elo (max-width:860px){.v-mi5 .grid{grid-template-columns:1fr}.v-mi5 .kep{max-width:420px}}
"""),
    ]


# ================================================================ AJÁNLAT (csomagok) + PRÉMIUM FELUGRÓ ABLAK
NYIT = "this.closest('section').querySelector('dialog.prem').showModal()"


def premium_ablak():
    p = PREMIUM
    bev = "".join(f'<p>{md(x)}</p>' for x in p["bevezeto"])
    alk = "".join(f'<div class="alk"><p class="ah"><b>{esc(a["cim"])}</b><span>{esc(a["ido"])}</span></p><p class="am">{esc(a["mikor"])}</p>'
                  f'<ul>{"".join(f"<li>{esc(x)}</li>" for x in a["pontok"])}</ul></div>' for a in p["alkalmak"])
    return (f'<dialog class="prem s-vilagos" aria-label="{esc(p["cim"])}" onclick="if(event.target===this)this.close()">'
            f'<div class="pin"><form method="dialog"><button class="zar" aria-label="Bezárás">×</button></form>'
            f'<p class="pk">Részletek</p><h3 class="pc">{esc(p["cim"])}</h3>{bev}<div class="alkalmak">{alk}</div>'
            f'<p class="hely">{esc(p["helyszin"])}</p><p class="par">{esc(p["ar"])}</p><div class="gombsor">{btn(p["cta"])}</div></div></dialog>')


def prem_link():
    return f'<button type="button" class="prem-link" onclick="{NYIT}">{esc(PREMIUM["link"])}{ui("nyil")}</button>'


PREM_CSS = r"""
.prem-link{background:none;border:0;padding:0;margin:4px 0 18px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:.95rem;color:var(--hl);text-decoration:underline;text-underline-offset:.22em;text-align:left}
.prem-link .ui{width:16px;height:16px;flex:none}
dialog.prem{width:min(760px,calc(100vw - 28px));max-height:calc(100vh - 40px);padding:0;border:0;border-radius:var(--r);background:var(--c0-card,#fff);color:var(--c0-ink,#222);box-shadow:0 40px 90px -30px rgba(0,0,0,.55)}
dialog.prem::backdrop{background:rgba(12,8,6,.62);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
dialog.prem .pin{padding:clamp(24px,4vw,44px);position:relative}
dialog.prem .zar{position:absolute;right:14px;top:12px;width:40px;height:40px;border-radius:50%;border:1px solid var(--c0-line2,#ccc);background:transparent;font-size:1.5rem;line-height:1;cursor:pointer;color:inherit}
dialog.prem .pk{font-family:var(--f-label);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--c0-primary-text,var(--c-primary));margin:0 0 8px}
dialog.prem .pc{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.4rem,3vw,2rem);line-height:1.1;margin:0 0 18px;color:var(--c0-head,#111);padding-right:40px}
dialog.prem p{margin:0 0 12px;line-height:1.6}
dialog.prem b{color:var(--c0-primary-text,var(--c-primary))}
dialog.prem .alkalmak{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:22px 0}
dialog.prem .alk{background:var(--c0-tint,#f6eee6);border-radius:14px;padding:16px}
dialog.prem .ah{display:flex;justify-content:space-between;align-items:baseline;gap:8px;margin:0 0 6px}
dialog.prem .ah b{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.1rem}
dialog.prem .ah span{font-family:var(--f-label);font-size:.78rem;color:var(--c0-ink-2,#555);white-space:nowrap}
dialog.prem .am{font-weight:700;font-size:.92rem;margin:0 0 6px}
dialog.prem ul{display:grid;gap:6px;margin:0;padding:0;list-style:none}
dialog.prem li{font-size:.9rem;padding-left:16px;position:relative;line-height:1.45}
dialog.prem li::before{content:"";position:absolute;left:0;top:.55em;width:7px;height:7px;border-radius:50%;background:var(--c-accent)}
dialog.prem .hely{font-weight:600}
dialog.prem .par{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.35rem;color:var(--c0-head,#111)}
@media (max-width:640px){dialog.prem .alkalmak{grid-template-columns:1fr}}
"""


def ajanlat():
    c = ctx()
    a = c["ajanlat"]
    el = a["elemek"]
    bas = ["Online kurzus", "Otthon, a saját tempódban"]
    pre = bas + ["A gyakorlatok személyre szabása", "Személyre szabott időbeosztás", "Tapasztalatok megosztása személyesen", "Problémakezelés személyesen"]
    sub = ["12 hét, 12 gyakorlat", "12 hetes program"]
    gombok = [{"szoveg": "Ezt választom", "href": ORDER}, {"szoveg": "Ezt választom", "href": ORDER_PREMIUM}]
    ablak = premium_ablak()

    def lst(items):
        return "".join(f'<li>{ui("pipa")}<span>{esc(x)}</span></li>' for x in items)

    def csomag(i, cls="cs"):
        e = el[i]
        return (f'<article class="{cls} c{i}" data-rv style="--i:{i}"><p class="al">{esc(sub[i])}</p><h3>{esc(e["nev"])}</h3>'
                f'<p class="ar">{esc(e["ar"])}</p><ul>{lst([bas, pre][i])}</ul>{prem_link() if i == 1 else ""}'
                f'{btn(gombok[i], alt=(i == 0 and cls == "cs"))}</article>')
    out = [
        dict(id="ax1", nev="Két csomag-oszlop", leiras="Két egymás melletti csomag pipás listával; a Prémium kiemelve, enyhén megemelve, alatta a „Mit tartalmaz?” link a felugró ablakhoz. A megszokott, könnyen összevethető árazás.",
             html=sec("ax1", "ajanlat", "s-tint", f'<div class="wrap">{sh(a)}<div class="ket">{csomag(0)}{csomag(1)}</div></div>{ablak}', anchor="etlap"),
             css=PREM_CSS + r"""
.v-ax1 .ket{display:grid;grid-template-columns:1fr 1fr;gap:var(--gap);max-width:900px;margin:0 auto;align-items:center}
.v-ax1 .cs{background:var(--c-card);border-radius:var(--r);padding:clamp(26px,3.6cqi,40px);box-shadow:var(--sh-2);display:flex;flex-direction:column;gap:6px}
.v-ax1 .c1{box-shadow:0 0 0 2px var(--c-primary),var(--sh-3);padding-top:clamp(34px,4.4cqi,52px);padding-bottom:clamp(34px,4.4cqi,52px)}
.v-ax1 .al{font-family:var(--f-label);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3);margin:0}
.v-ax1 h3{font-size:var(--t-h3)}.v-ax1 .ar{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(2rem,3.6cqi,2.8rem);color:var(--hl);margin:6px 0 10px;line-height:1}
.v-ax1 ul{display:grid;gap:8px;margin-bottom:18px}.v-ax1 li{display:flex;gap:10px;align-items:flex-start;font-size:.96rem}.v-ax1 li .ui{color:var(--c-primary);margin-top:2px}
.v-ax1 .btn{align-self:stretch;margin-top:auto}
@container elo (max-width:720px){.v-ax1 .ket{grid-template-columns:1fr}}
"""),
        dict(id="ax2", nev="A Prémium sötétben", leiras="Az alapcsomag világos lapon, a Prémium sötét, gyertyafényes kártyán, narancs árral és a „Mit tartalmaz?” linkkel. A drágább csomag magától kiemelkedik.",
             html=sec("ax2", "ajanlat", "s-paper", f'<div class="wrap">{sh(a)}<div class="ket">{csomag(0, "cs")}{csomag(1, "cs sotet s-deep")}</div></div>{ablak}', anchor="etlap"),
             css=PREM_CSS + r"""
.v-ax2 .ket{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(18px,2.6cqi,32px);max-width:1000px;margin:0 auto;align-items:stretch}
.v-ax2 .cs{background:var(--c-card);padding:clamp(28px,4cqi,48px);display:flex;flex-direction:column;gap:6px;border-radius:var(--r);overflow:hidden;box-shadow:var(--sh-3)}
.v-ax2 .sotet{color:var(--c-ink);background:radial-gradient(circle at 85% 0%,color-mix(in srgb,var(--c-primary) 38%,transparent),transparent 55%),var(--c-deep)}
.v-ax2 .al{font-family:var(--f-label);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3);margin:0}
.v-ax2 h3{font-size:var(--t-h3)}.v-ax2 .ar{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(2rem,3.8cqi,3rem);color:var(--hl);margin:6px 0 12px;line-height:1}
.v-ax2 ul{display:grid;gap:8px;margin-bottom:18px}.v-ax2 li{display:flex;gap:10px;font-size:.96rem}.v-ax2 li .ui{color:var(--hl);margin-top:2px}
.v-ax2 .btn{align-self:flex-start;margin-top:auto}
@container elo (max-width:760px){.v-ax2 .ket{grid-template-columns:1fr}}
"""),
        dict(id="ax3", nev="Két edzésbérlet", leiras="A csomagok perforált bérletjegyként: a fő részen a tartalom, a letéphető szelvényen az ár és a gomb. Az „edzésterv” metaforája. Játékos, egyedi.",
             html=sec("ax3", "ajanlat", "s-sand", f'<div class="wrap">{sh(a)}<div class="jegyek">'
                      + "".join(f'<article class="jegy j{i}" data-rv style="--i:{i}"><div class="fo"><p class="al">{esc(sub[i])}</p><h3>{esc(el[i]["nev"])}</h3><ul>{lst([bas, pre][i])}</ul>{prem_link() if i == 1 else ""}</div>'
                                f'<div class="szelveny"><span class="mono">Bérlet · 12 hét</span><b>{esc(el[i]["ar"])}</b>{btn(gombok[i])}</div></article>' for i in range(2))
                      + f'</div></div>{ablak}', anchor="etlap", masod=True),
             css=PREM_CSS + r"""
.v-ax3 .jegyek{display:grid;gap:var(--gap);max-width:940px;margin:0 auto}
.v-ax3 .jegy{display:grid;grid-template-columns:1fr 250px;background:var(--c-card);border-radius:18px;box-shadow:var(--sh-2);-webkit-mask:radial-gradient(circle 13px at calc(100% - 250px) 0,#0000 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 13px at calc(100% - 250px) 100%,#0000 98%,#000) bottom/100% 51% no-repeat;mask:radial-gradient(circle 13px at calc(100% - 250px) 0,#0000 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 13px at calc(100% - 250px) 100%,#0000 98%,#000) bottom/100% 51% no-repeat}
.v-ax3 .fo{padding:clamp(22px,3cqi,34px)}
.v-ax3 .al{font-family:var(--f-label);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3);margin:0 0 4px}
.v-ax3 h3{font-size:var(--t-h3);margin-bottom:12px}.v-ax3 ul{display:grid;grid-template-columns:1fr 1fr;gap:6px 16px}.v-ax3 li{display:flex;gap:8px;font-size:.92rem}.v-ax3 li .ui{color:var(--c-primary);width:17px;height:17px;margin-top:3px}
.v-ax3 .prem-link{margin:14px 0 0}
.v-ax3 .szelveny{border-left:2px dashed var(--c-line2);padding:22px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:8px;text-align:center;background:var(--c-tint)}
.v-ax3 .j1 .szelveny{background:var(--c-primary);color:var(--c-on-primary);--b-bg:var(--c-card);--b-ink:var(--c-primary-d);--b-deep:var(--c-primary-dd)}
.v-ax3 .szelveny .mono{font-size:.68rem;text-transform:uppercase;opacity:.75}
.v-ax3 .szelveny b{font-family:var(--f-display);font-weight:var(--w-display);font-size:2rem;line-height:1}
@container elo (max-width:700px){.v-ax3 .jegy{grid-template-columns:1fr;-webkit-mask:none;mask:none}.v-ax3 .szelveny{border-left:0;border-top:2px dashed var(--c-line2)}.v-ax3 ul{grid-template-columns:1fr}}
"""),
        dict(id="ax4", nev="Árlista-lap", leiras="A két csomag egy nyomtatott árlista-lapon, pontozott vezetővonallal az árig; alattuk a tartalom és a gombok. Klasszikus, tömör.",
             html=sec("ax4", "ajanlat", "s-white", f'<div class="wrap szuk">{sh(a)}<div class="lap" data-rv>'
                      + "".join(f'<div class="tetel"><p class="sor"><b>{esc(el[i]["nev"])}</b><i></i><span>{esc(el[i]["ar"])}</span></p>'
                                f'<p class="al">{esc(sub[i])} · {" · ".join(esc(x) for x in [bas, pre][i])}</p>{prem_link() if i == 1 else ""}{btn(gombok[i], alt=(i == 0))}</div>' for i in range(2))
                      + f'</div></div>{ablak}', anchor="etlap"),
             css=PREM_CSS + r"""
.v-ax4 .lap{background:var(--c-card);border:1px solid var(--c-line2);outline:1px solid var(--c-line2);outline-offset:-8px;padding:clamp(26px,4cqi,48px);border-radius:4px;box-shadow:var(--sh-2)}
.v-ax4 .tetel+.tetel{margin-top:30px;padding-top:30px;border-top:1px solid var(--c-line)}
.v-ax4 .sor{display:flex;align-items:baseline;gap:10px;margin:0 0 8px}
.v-ax4 .sor b{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.1rem,2cqi,1.45rem);color:var(--c-head)}
.v-ax4 .sor i{flex:1;border-bottom:2px dotted var(--c-line2);transform:translateY(-4px)}
.v-ax4 .sor span{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.2rem,2.2cqi,1.6rem);color:var(--hl);white-space:nowrap}
.v-ax4 .al{color:var(--c-ink-2);font-size:.94rem;margin:0 0 14px}
.v-ax4 .prem-link{display:flex;margin:-4px 0 14px}
"""),
        dict(id="ax5", nev="Fotós csomagkártyák", leiras="Két kártya a saját fotójával (a szívére tett kéz, a tengerpart), rajta az ár címkén; alattuk a tartalom és a gomb. Hangulatos, képszerű.",
             html=sec("ax5", "ajanlat", "s-sand", f'<div class="wrap">{sh(a)}<div class="racs" style="--oszlop:2">'
                      + "".join(f'<article class="krt c{i}" data-rv style="--i:{i}">{foto(c, el[i].get("foto"), "16/10", "krt-kep")}'
                                f'<span class="arc">{esc(el[i]["ar"])}</span><p class="al">{esc(sub[i])}</p><h3 class="krt-h">{esc(el[i]["nev"])}</h3>'
                                f'<ul>{lst([bas, pre][i])}</ul>{prem_link() if i == 1 else ""}{btn(gombok[i])}</article>' for i in range(2))
                      + f'</div></div>{ablak}', anchor="etlap", masod=True),
             css=PREM_CSS + r"""
.v-ax5 .racs{max-width:940px;margin:0 auto;align-items:start}
.v-ax5 .arc{position:absolute;right:16px;top:16px;z-index:4;background:var(--c-primary);color:var(--c-on-primary);font-family:var(--f-display);font-weight:var(--w-display);font-size:1.25rem;padding:6px 14px;border-radius:999px;box-shadow:var(--sh-2)}
.v-ax5 .al{font-family:var(--f-label);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3);margin:0}
.v-ax5 ul{display:grid;gap:6px;margin:6px 0 10px}.v-ax5 li{display:flex;gap:8px;font-size:.94rem}.v-ax5 li .ui{color:var(--c-primary);width:17px;height:17px;margin-top:3px}
.v-ax5 .btn{align-self:flex-start;margin-top:6px}.v-ax5 .prem-link{margin:0 0 6px}
"""),
    ]
    return out


# ================================================================ ZÁRÓ BLOKK (Miért most?) egyedi változatok
def latogatas():
    c = ctx()
    l = c["latogatas"]
    out = [
        dict(id="lx1", nev="Homokóra", leiras="Sötét záró blokk egy rajzolt homokórával (keret, üvegkontúr, peregő homok) és a „12 hét múlva…” mondattal. Az idő múlása mint döntés.",
             html=(f'<section class="sec v-lx1 s-deep" id="kapcsolat">{hat(c)}{dk(c, "latogatas")}<div class="wrap grid">'
                   '<div class="ora" data-rv aria-hidden="true"><svg viewBox="0 0 120 200">'
                   '<rect class="keret" x="12" y="10" width="96" height="10" rx="3"/><rect class="keret" x="12" y="180" width="96" height="10" rx="3"/>'
                   '<path class="rud" d="M18 20V180M102 20V180"/>'
                   '<path class="uveg" d="M26 20C26 68 54 84 56 100C54 116 26 132 26 180M94 20C94 68 66 84 64 100C66 116 94 132 94 180"/>'
                   '<clipPath id="lx1-uveg"><path d="M28.6 20C28.6 67 55 83 57.6 100C55 117 28.6 133 28.6 180H91.4C91.4 133 65 117 62.4 100C65 83 91.4 67 91.4 20Z"/></clipPath>'
                   '<g clip-path="url(#lx1-uveg)"><rect class="homok fent" x="20" y="42" width="80" height="58"/>'
                   '<path class="homok lent" d="M20 180V152C40 142 50 136 60 134C70 136 80 142 100 152V180Z"/>'
                   '<path class="sugar" d="M60 100V178"/></g></svg></div>'
                   f'<div class="txt" data-rv>{kick(l.get("kicker"))}<h2 class="cim">{md(l["cim"])}</h2><p class="lead">{md(l["lead"])}</p>{gombsor(l)}</div></div></section>'),
             css=r"""
.v-lx1 .grid{display:grid;grid-template-columns:.6fr 1.4fr;gap:clamp(30px,6cqi,90px);align-items:center}
.v-lx1 .lead{margin:20px 0 30px}
.v-lx1 .ora{width:min(200px,100%);margin:0 auto;opacity:.8}
.v-lx1 .ora svg{display:block;width:100%;height:auto;overflow:visible}
.v-lx1 .keret{fill:var(--c-deep-hl)}
.v-lx1 .rud{stroke:var(--c-deep-hl);stroke-width:3;stroke-linecap:round;opacity:.7}
.v-lx1 .uveg{fill:none;stroke:color-mix(in srgb,var(--c-on-deep) 70%,transparent);stroke-width:2.5;stroke-linecap:round}
.v-lx1 .homok{fill:var(--c-primary);fill-opacity:.8;transform-box:fill-box;transform-origin:50% 100%}
.v-lx1 .fent{animation:lx1fent 14s linear infinite}
.v-lx1 .lent{animation:lx1lent 14s linear infinite}
.v-lx1 .sugar{stroke:var(--c-primary);stroke-opacity:.8;stroke-width:3;stroke-linecap:round;stroke-dasharray:4 5;animation:lx1sug 1s linear infinite}
@keyframes lx1fent{from{transform:scaleY(1)}to{transform:scaleY(.04)}}
@keyframes lx1lent{from{transform:scaleY(.12)}to{transform:scaleY(1)}}
@keyframes lx1sug{to{stroke-dashoffset:-9}}
@container elo (max-width:760px){.v-lx1 .grid{grid-template-columns:1fr}.v-lx1 .ora{width:120px}}
"""),
        dict(id="lx2", nev="12 hét, 12 pötty", leiras="Világos záró blokk: 12 pötty egy sorban (a 12 hét), ami görgetésre egyenként kigyullad; alatta a mondat és a gombok. Az edzésterv ritmusa egy pillantásra.",
             html=(f'<section class="sec v-lx2 s-tint tx" id="kapcsolat">{hat(c)}{dk(c, "latogatas")}<div class="wrap szuk">'
                   f'<div class="hetek" data-rv aria-hidden="true">' + "".join(f'<i style="--d:{i * 0.12:.2f}s"><span>{i + 1}</span></i>' for i in range(12)) + '</div>'
                   f'<header class="shead" data-rv>{kick(l["kicker"])}<h2 class="cim">{md(l["cim"])}</h2><p class="lead">{md(l["lead"])}</p>{gombsor(l)}</header></div></section>'),
             css=r"""
.v-lx2 .hetek{display:grid;grid-template-columns:repeat(12,1fr);gap:8px;max-width:620px;margin:0 auto 40px}
.v-lx2 .hetek i{aspect-ratio:1;border-radius:50%;border:2px solid var(--c-primary);display:grid;place-items:center;font-style:normal;font-family:var(--f-label);font-size:.7rem;color:var(--c-primary);background:var(--c-card);transition:background .4s var(--d),color .4s var(--d)}
.v-lx2 .hetek.in i,.noanim .v-lx2 .hetek i{background:var(--c-primary);color:var(--c-on-primary)}
.v-lx2 .shead{margin-bottom:0}.v-lx2 .gombsor{margin-top:28px}
@container elo (max-width:520px){.v-lx2 .hetek{grid-template-columns:repeat(6,1fr)}}
"""),
    ]
    return out


# ================================================================ LÁBLÉC egyedi
def lablec():
    c = ctx()
    lb = c["lablec"]
    links = "".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in lb["linkek"])
    return [dict(id="lbx", nev="Sötét, jantra-jellel", leiras="Sötét, csendes lábléc: középen a logó egy halvány jantra előtt, alatta egy mondat, a menü és a gomb. Méltóságteljes lezárás.",
                 html=(f'<footer class="sec v-lbx s-deep" id="lablec"><div class="wrap"><div class="jel" aria-hidden="true"></div>'
                       f'<a class="brand" href="#top">{logo(c, 64, "ko", feher=True)}</a><p class="mondat">{esc(lb["felhivas"])}</p>'
                       f'<p class="sz">{esc(lb["szoveg"])}</p><nav class="links">{links}</nav>'
                       f'<div class="gombsor">{btn({"szoveg": "Belevágok", "href": CSOMAGOK})}</div><p class="apro">© {esc(lb["cegnev"])}'
                       f' · <a href="#impresszum">Impresszum</a> · <a href="https://www.tantraiskola.hu/aszf" target="_blank" rel="noopener">ÁSZF</a>'
                       f' · <a href="https://www.tantraiskola.hu/privacy-policy" target="_blank" rel="noopener">Adatkezelési tájékoztató</a></p></div></footer>'),
                 css=r"""
.v-lbx{text-align:center;padding:clamp(60px,7cqi,100px) 0 30px;overflow:hidden}
.v-lbx .jel{position:absolute;left:50%;top:-80px;width:420px;height:420px;margin-left:-210px;background:var(--c-deep-hl);opacity:.07;-webkit-mask:var(--mjel) center/contain no-repeat;mask:var(--mjel) center/contain no-repeat;z-index:0}
.v-lbx .brand{display:inline-block;position:relative}.v-lbx .logo{margin:0 auto}
.v-lbx .mondat{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.5rem,3cqi,2.3rem);color:var(--c-on-deep);margin:18px 0 6px;position:relative}
.v-lbx .sz{color:var(--c-on-deep-2);max-width:56ch;margin:0 auto 22px;font-size:.95rem}
.v-lbx .links{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 22px;margin-bottom:24px;position:relative}
.v-lbx .links a{text-decoration:none;color:var(--c-on-deep-2);font-size:.92rem}.v-lbx .links a:hover{color:var(--c-deep-hl)}
.v-lbx .gombsor{justify-content:center;margin-bottom:40px}
.v-lbx .apro{font-family:var(--f-label);font-size:.7rem;letter-spacing:.1em;color:var(--c-on-deep-2);border-top:1px solid var(--c-line);padding-top:20px;margin:0}.v-lbx .apro a{color:inherit}
""")]


def mind(context):
    global CTX
    CTX = context
    nav_html()
    HERO[0]["html"] = hero_html()
    if not any(x["id"] == "h3" for x in HERO):
        HERO.append(dict(id="h3", nev="Teljes képes, kártyával",
                         leiras="A teljes képernyős fotón egy kisebb kártya csak a címmel és a terméknévvel, így a férfiból több látszik; a többi szöveg és a gombok alatta, egy külön sávban.",
                         html=None, css=H3_CSS))
    next(x for x in HERO if x["id"] == "h3")["html"] = hero_h3()
    return {"nav": NAV, "hero": HERO, "rolaszol": rolaszol(), "miert": miert(), "kinek": kinek(),
            "velemenyek": velemenyek(), "garancia": garancia(), "gyik": gyik(), "ajanlat": ajanlat(), "mia": mia(), "tenyek": tenyek(),
            "latogatas": latogatas(), "lablec": lablec()}
