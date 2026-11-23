"""Cartes du profil GitHub (SVG) : python generate.py  [--sample pour un aperçu sans réseau]

Lancé chaque jour par .github/workflows/cards.yml : les chiffres (contributions, étoiles, téléchargements
de Phantom Boost…) se mettent à jour tout seuls. Tout le texte se change dans CONFIG ci-dessous."""
import base64
import datetime as dt
import json
import os
import sys
import urllib.request
from xml.sax.saxutils import escape

CONFIG = dict(
    login="qqnr",
    name="wu",
    hello="HI, I'M",
    tagline="Developer of Phantom Boost · clean, smooth tools for PC gamers",
    chips=[("pin", "France"), ("code", "Python · Qt · Windows")],
    project=("qqnr", "phantom-boost", "Phantom Boost"),
    featured_text="Display tuning, stretched resolution, crosshair, HUDs and a Windows optimizer, in one clean app.",
    featured_tags=["Windows 10 / 11", "Free", "Auto updates"],
    about=[("spark", "Building Phantom Boost, an all-in-one app for PC gamers"),
           ("brush", "In love with clean, smooth and polished interfaces"),
           ("music", "Into audio, music and Discord")],
    stack=[("LANGUAGE", [("code", "Python")]),
           ("INTERFACE", [("window", "PySide6 · Qt"), ("brush", "QSS")]),
           ("WINDOWS", [("chip", "Win32 · ctypes"), ("box", "PyInstaller"), ("box", "Inno Setup")]),
           ("INTEGRATIONS", [("chat", "Discord RPC"), ("music", "Apple Music")])],
    buttons=[("discord", "chat", "Discord · @qqhw", False),
             ("project", "ghost", "Phantom Boost", False),
             ("download", "download", "Download", True)],
)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "cards")
W = 860
TEXT, SOFT, MUTE, ACC, ACC2 = "#f5f2ff", "#ddd6f3", "#a69fc8", "#8b5cf6", "#b892ff"
METRICS = json.load(open(os.path.join(ROOT, "fonts", "metrics.json"), encoding="utf-8"))
WEIGHTS = {"Regular": 400, "Medium": 500, "Bold": 700}
GHOST = "M50.00 9.00 L51.75 9.06 L53.45 9.25 L55.07 9.56 L56.64 9.99 L58.13 10.52 L59.55 11.16 L60.91 11.91 L62.19 12.75 L63.40 13.68 L64.53 14.71 L65.58 15.81 L66.55 17.00 L67.45 18.26 L68.26 19.59 L68.99 20.99 L69.63 22.45 L70.18 23.96 L70.65 25.53 L71.03 27.15 L71.31 28.80 L71.50 30.50 L72.75 30.40 L74.02 30.36 L75.29 30.39 L76.58 30.48 L77.86 30.63 L79.14 30.85 L80.41 31.13 L81.66 31.47 L82.88 31.88 L84.08 32.36 L85.24 32.89 L86.37 33.50 L87.45 34.17 L88.48 34.90 L89.45 35.70 L90.36 36.57 L91.20 37.50 L91.97 38.50 L92.66 39.56 L93.26 40.70 L93.77 41.90 L94.19 43.16 L94.50 44.50 L94.60 45.59 L94.64 46.68 L94.62 47.77 L94.53 48.85 L94.39 49.94 L94.20 51.02 L93.96 52.09 L93.67 53.16 L93.34 54.22 L92.97 55.27 L92.56 56.31 L92.12 57.35 L91.65 58.37 L91.14 59.39 L90.62 60.39 L90.07 61.38 L89.50 62.35 L88.92 63.31 L88.33 64.26 L87.72 65.19 L87.11 66.10 L86.50 67.00 L85.88 65.05 L85.13 63.31 L84.26 61.79 L83.27 60.48 L82.19 59.39 L81.04 58.54 L79.81 57.93 L78.53 57.56 L77.21 57.45 L75.86 57.59 L74.50 58.00 L74.43 59.04 L74.37 60.09 L74.30 61.13 L74.24 62.17 L74.17 63.21 L74.10 64.24 L74.03 65.28 L73.96 66.31 L73.88 67.33 L73.81 68.35 L73.73 69.37 L73.65 70.38 L73.56 71.38 L73.47 72.38 L73.38 73.37 L73.29 74.36 L73.19 75.34 L73.09 76.30 L72.98 77.26 L72.87 78.21 L72.75 79.15 L72.63 80.08 L72.50 81.00 L72.14 82.57 L71.71 84.06 L71.21 85.48 L70.65 86.82 L70.03 88.08 L69.35 89.27 L68.62 90.38 L67.85 91.41 L67.04 92.36 L66.19 93.24 L65.30 94.05 L64.39 94.78 L63.46 95.43 L62.50 96.00 L62.04 94.01 L61.41 92.20 L60.64 90.58 L59.75 89.19 L58.77 88.06 L57.72 87.21 L56.62 86.68 L55.50 86.50 L54.90 87.70 L54.29 88.89 L53.66 90.07 L53.00 91.24 L52.31 92.38 L51.58 93.48 L50.79 94.56 L49.93 95.59 L49.01 96.57 L48.00 97.50 L47.30 95.87 L46.53 94.34 L45.70 92.91 L44.83 91.60 L43.91 90.44 L42.96 89.43 L41.99 88.59 L41.00 87.94 L40.00 87.50 L39.16 88.56 L38.27 89.57 L37.33 90.51 L36.35 91.37 L35.34 92.15 L34.28 92.83 L33.19 93.41 L32.06 93.87 L30.90 94.21 L29.71 94.43 L28.50 94.50 L28.62 93.60 L28.71 92.69 L28.78 91.76 L28.82 90.81 L28.83 89.85 L28.82 88.88 L28.79 87.89 L28.74 86.89 L28.68 85.87 L28.60 84.85 L28.50 83.81 L28.39 82.77 L28.27 81.72 L28.15 80.66 L28.01 79.59 L27.87 78.52 L27.72 77.44 L27.58 76.35 L27.43 75.27 L27.28 74.18 L27.14 73.09 L27.00 72.00 L26.88 70.85 L26.77 69.70 L26.65 68.55 L26.54 67.41 L26.42 66.29 L26.31 65.18 L26.19 64.08 L26.08 63.00 L25.96 61.95 L25.85 60.92 L25.73 59.91 L25.62 58.94 L25.50 58.00 L24.14 57.59 L22.79 57.45 L21.47 57.56 L20.19 57.93 L18.96 58.54 L17.81 59.39 L16.73 60.48 L15.74 61.79 L14.87 63.31 L14.12 65.05 L13.50 67.00 L12.89 66.10 L12.28 65.19 L11.67 64.26 L11.08 63.31 L10.50 62.35 L9.93 61.38 L9.38 60.39 L8.86 59.39 L8.35 58.37 L7.88 57.35 L7.44 56.31 L7.03 55.27 L6.66 54.22 L6.33 53.16 L6.04 52.09 L5.80 51.02 L5.61 49.94 L5.47 48.85 L5.38 47.77 L5.36 46.68 L5.40 45.59 L5.50 44.50 L5.81 43.16 L6.23 41.90 L6.74 40.70 L7.34 39.56 L8.03 38.50 L8.80 37.50 L9.64 36.57 L10.55 35.70 L11.52 34.90 L12.55 34.17 L13.63 33.50 L14.76 32.89 L15.92 32.36 L17.12 31.88 L18.34 31.47 L19.59 31.13 L20.86 30.85 L22.14 30.63 L23.42 30.48 L24.71 30.39 L25.98 30.36 L27.25 30.40 L28.50 30.50 L28.69 28.80 L28.97 27.15 L29.35 25.53 L29.82 23.96 L30.37 22.45 L31.01 20.99 L31.74 19.59 L32.55 18.26 L33.45 17.00 L34.42 15.81 L35.47 14.71 L36.60 13.68 L37.81 12.75 L39.09 11.91 L40.45 11.16 L41.87 10.52 L43.36 9.99 L44.93 9.56 L46.55 9.25 L48.25 9.06 L50.00 9.00 M35.00 28.50 L46.50 33.50 L46.24 35.48 L45.53 37.13 L44.45 38.39 L43.12 39.25 L41.62 39.66 L40.05 39.59 L38.50 39.00 L37.57 38.24 L36.79 37.33 L36.15 36.28 L35.64 35.12 L35.27 33.87 L35.02 32.56 L34.89 31.21 L34.89 29.85 L35.00 28.50 M65.00 28.50 L53.50 33.50 L53.76 35.48 L54.47 37.13 L55.55 38.39 L56.88 39.25 L58.38 39.66 L59.95 39.59 L61.50 39.00 L62.43 38.24 L63.21 37.33 L63.85 36.28 L64.36 35.12 L64.73 33.87 L64.98 32.56 L65.11 31.21 L65.11 29.85 L65.00 28.50"

ICONS = {  # tracés 24 x 24 au trait
    "pin": '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>',
    "code": '<path d="M8.5 7 3.5 12l5 5M15.5 7l5 5-5 5"/>',
    "spark": '<path d="M12 3.5 13.8 10.2 20.5 12l-6.7 1.8L12 20.5l-1.8-6.7L3.5 12l6.7-1.8z"/>',
    "brush": '<path d="M14.5 4.5 19.5 9.5 11 18l-5 1 1-5z"/><path d="M12.5 6.5l5 5"/>',
    "music": '<path d="M9 18V6l10-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="16.5" cy="16" r="2.5"/>',
    "window": '<rect x="3.5" y="5" width="17" height="14" rx="2.5"/><path d="M3.5 9h17"/>',
    "chip": '<rect x="6.5" y="6.5" width="11" height="11" rx="2"/><path d="M9.5 3.5v3M14.5 3.5v3M9.5 17.5v3M14.5 17.5v3M3.5 9.5h3M3.5 14.5h3M17.5 9.5h3M17.5 14.5h3"/>',
    "box": '<path d="M12 3.5 20 7.5v9L12 20.5 4 16.5v-9z"/><path d="M4 7.5l8 4 8-4M12 11.5v9"/>',
    "chat": '<path d="M5 5.5h14a1.5 1.5 0 0 1 1.5 1.5v8.5A1.5 1.5 0 0 1 19 17H11l-4.5 3.5V17H5A1.5 1.5 0 0 1 3.5 15.5V7A1.5 1.5 0 0 1 5 5.5z"/>',
    "download": '<path d="M12 4v11M7 10.5l5 5 5-5M5 19.5h14"/>',
    "star": '<path d="M12 3.8l2.5 5.1 5.6.8-4 4 .9 5.6-5-2.7-5 2.7.9-5.6-4-4 5.6-.8z"/>',
    "repo": '<path d="M6 4.5h11.5v15H6a1.5 1.5 0 0 1-1.5-1.5V6A1.5 1.5 0 0 1 6 4.5z"/><path d="M4.5 16.5h13"/>',
    "people": '<circle cx="9" cy="9" r="3"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><circle cx="17" cy="9.5" r="2.4"/><path d="M15.5 14.2A4.6 4.6 0 0 1 21 18.5"/>',
    "pulse": '<path d="M3 12h4l2.5-6 4 12 2.5-6H21"/>',
    "heart": '<path d="M12 19.5s-7.5-4.4-7.5-10A4.3 4.3 0 0 1 12 6.8a4.3 4.3 0 0 1 7.5 2.7c0 5.6-7.5 10-7.5 10z"/>',
    "layers": '<path d="M12 4 21 8.5 12 13 3 8.5z"/><path d="M3 12.5 12 17l9-4.5M3 16.5 12 21l9-4.5"/>',
}


# ---------------------------------------------------------------- outils
def tw(text, size, weight="Regular"):
    m = METRICS[weight]
    return sum(m.get(ch, .6) for ch in text) * size


def font_css(*weights):
    out = []
    for w in weights:
        b64 = open(os.path.join(ROOT, "fonts", "poppins-%s.b64" % w.lower())).read().strip()
        out.append("@font-face{font-family:'PB';src:url(data:font/ttf;base64,%s) format('truetype');font-weight:%d}"
                   % (b64, WEIGHTS[w]))
    return "<style>%s text{font-family:'PB','Segoe UI',system-ui,sans-serif}</style>" % "".join(out)


def text(x, y, s, size, weight="Regular", fill=TEXT, anchor="start", spacing=0, opacity=1):
    extra = (' letter-spacing="%s"' % spacing if spacing else "") + (' opacity="%s"' % opacity if opacity != 1 else "")
    return ('<text x="%.1f" y="%.1f" font-size="%s" font-weight="%d" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, size, WEIGHTS[weight], fill, anchor, extra, escape(s)))


def icon(name, x, y, size=18, color=TEXT, width=1.9):
    k = size / 24
    return ('<g transform="translate(%.1f %.1f) scale(%.4f)" fill="none" stroke="%s" stroke-width="%.2f" '
            'stroke-linecap="round" stroke-linejoin="round">%s</g>' % (x, y, k, color, width / k, ICONS[name]))


def ghost_tile(x, y, s, uid):
    """Le logo Phantom Boost : carré violet, reflet, fantôme blanc légèrement penché."""
    k = s * .74 / 100
    return f'''<defs>
<linearGradient id="gt{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b48cff"/><stop offset=".5" stop-color="#8b5cf6"/><stop offset="1" stop-color="#5a2fd6"/></linearGradient>
<radialGradient id="gh{uid}" cx=".28" cy=".12" r=".75"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<linearGradient id="gw{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#efe6ff"/></linearGradient>
</defs>
<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s * .23:.1f}" fill="url(#gt{uid})"/>
<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s * .23:.1f}" fill="url(#gh{uid})"/>
<g transform="translate({x + s / 2:.2f} {y + s * .51:.2f}) rotate(-9) scale({k:.4f}) translate(-50 -53)">
<path d="{GHOST}" fill="#281070" fill-opacity=".35" fill-rule="evenodd" transform="translate(0 {s * .03 / k:.2f})"/>
<path d="{GHOST}" fill="url(#gw{uid})" fill-rule="evenodd"/></g>'''


def frame(h, uid, glows=()):
    """Fond commun des cartes : verre violet sombre, filet clair, lueurs douces."""
    g = "".join(f'<radialGradient id="l{uid}{i}" cx="{cx}" cy="{cy}" r="{r}"><stop offset="0" stop-color="{c}" stop-opacity="{o}"/>'
                f'<stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>' for i, (cx, cy, r, c, o) in enumerate(glows))
    lay = "".join(f'<rect width="{W}" height="{h}" rx="24" fill="url(#l{uid}{i})"/>' for i in range(len(glows)))
    return f'''<defs><linearGradient id="bg{uid}" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#1d1546"/><stop offset="1" stop-color="#0f0b22"/></linearGradient>
<linearGradient id="hl{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>{g}</defs>
<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="24" fill="url(#bg{uid})"/>{lay}
<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="24" fill="none" stroke="#fff" stroke-opacity=".09"/>
<path d="M60 1h{W - 120}" stroke="url(#hl{uid})" stroke-width="1"/>'''


def title(x, y, name, label):
    return (f'<rect x="{x}" y="{y}" width="34" height="34" rx="10" fill="{ACC}" fill-opacity=".22" stroke="{ACC2}" stroke-opacity=".35"/>'
            + icon(name, x + 8, y + 8, 18, ACC2) + text(x + 48, y + 24, label, 19, "Bold"))


def chip(x, y, name, label, h=34, size=13, weight="Medium", fill_op=".07"):
    wdt = 14 + 18 + 8 + tw(label, size, weight) + 16
    s = (f'<rect x="{x}" y="{y}" width="{wdt:.1f}" height="{h}" rx="{h / 2}" fill="#fff" fill-opacity="{fill_op}" stroke="#fff" stroke-opacity=".12"/>'
         + icon(name, x + 13, y + (h - 17) / 2, 17, ACC2) + text(x + 40, y + h / 2 + size * .36, label, size, weight, SOFT))
    return s, wdt


def svg(h, body, weights, label, width=W):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}" role="img" '
            f'aria-label="{escape(label)}">{font_css(*weights)}{body}</svg>')


# ---------------------------------------------------------------- cartes
def card_hero(data):
    h = 300
    b = [frame(h, "h", [(".92", ".05", ".55", "#8b5cf6", ".55"), (".08", "1", ".55", "#d946ef", ".20"), (".55", ".55", ".7", "#6d28d9", ".10")])]
    # faisceau diagonal (signature du thème de l'appli)
    b.append('<defs><linearGradient id="beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             '<stop offset=".5" stop-color="#fff" stop-opacity=".10"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
             '<clipPath id="hc"><rect width="%d" height="%d" rx="24"/></clipPath>'
             '<pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="#fff" fill-opacity=".10"/></pattern>'
             '<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>'
             '<mask id="dm"><rect x="560" y="0" width="300" height="%d" fill="url(#fade)"/></mask></defs>' % (W, h, h))
    b.append('<g clip-path="url(#hc)"><path d="M560 -20 L600 -20 L430 %d L390 %d Z" fill="url(#beam)"/>'
             '<rect x="560" y="0" width="300" height="%d" fill="url(#dots)" mask="url(#dm)"/></g>' % (h + 20, h + 20, h))
    # logo avec halo
    b.append('<defs><radialGradient id="halo"><stop offset="0" stop-color="#a77bff" stop-opacity=".55"/><stop offset="1" stop-color="#a77bff" stop-opacity="0"/></radialGradient></defs>'
             '<circle cx="138" cy="150" r="125" fill="url(#halo)"/>')
    av = os.path.join(ROOT, "avatar.jpg")  # ta photo (sinon le logo fantôme)
    if os.path.exists(av):
        img = base64.b64encode(open(av, "rb").read()).decode()
        b.append('<defs><clipPath id="avc"><rect x="58" y="70" width="160" height="160" rx="38"/></clipPath>'
                 '<linearGradient id="avr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d9c4ff"/>'
                 '<stop offset="1" stop-color="#7a4ee6"/></linearGradient></defs>'
                 '<image x="58" y="70" width="160" height="160" preserveAspectRatio="xMidYMid slice" clip-path="url(#avc)" '
                 'href="data:image/jpeg;base64,%s"/>'
                 '<rect x="56.5" y="68.5" width="163" height="163" rx="39.5" fill="none" stroke="url(#avr)" stroke-width="3"/>' % img)
    else:
        b.append(ghost_tile(58, 70, 160, "h"))
    x = 262
    b.append(text(x, 92, data["hello"], 14, "Medium", ACC2, spacing=3.2))
    b.append(text(x - 3, 168, data["name"], 76, "Bold", "#ffffff"))
    b.append(text(x, 204, data["tagline"], 16, "Regular", SOFT))
    cx = x
    for name, label in data["chips"]:
        s, wdt = chip(cx, 226, name, label)
        b.append(s)
        cx += wdt + 10
    rel = data.get("release")
    if rel:  # pastille « en ligne » en haut à droite
        label = "Now shipping %s %s" % (data["project"][2], rel["tag"])
        pw = tw(label, 12, "Medium") + 44
        px = W - 32 - pw
        b.append(f'<rect x="{px:.1f}" y="30" width="{pw:.1f}" height="30" rx="15" fill="#0b0818" fill-opacity=".55" stroke="#fff" stroke-opacity=".12"/>'
                 f'<circle cx="{px + 18:.1f}" cy="45" r="7" fill="#3ddc84" fill-opacity=".25"/><circle cx="{px + 18:.1f}" cy="45" r="3.6" fill="#3ddc84"/>'
                 + text(px + 32, 49.5, label, 12, "Medium", SOFT))
    return svg(h, "".join(b), ["Regular", "Medium", "Bold"], "Hi, I'm %s" % data["name"])


def card_button(icon_name, label, primary):
    h = 52
    wdt = int(22 + 20 + 10 + tw(label, 15, "Bold") + 24)
    if primary:
        bg = ('<defs><linearGradient id="bb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a77bff"/>'
              '<stop offset="1" stop-color="#7a4ee6"/></linearGradient></defs>'
              f'<rect x="1" y="1" width="{wdt - 2}" height="{h - 2}" rx="{(h - 2) / 2}" fill="url(#bb)" stroke="#fff" stroke-opacity=".30"/>')
        fg = "#ffffff"
    else:
        bg = ('<defs><linearGradient id="gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".07"/>'
              '<stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
              f'<rect x="1" y="1" width="{wdt - 2}" height="{h - 2}" rx="{(h - 2) / 2}" fill="#1a1440" stroke="#b892ff" stroke-opacity=".35"/>'
              f'<rect x="1" y="1" width="{wdt - 2}" height="{h - 2}" rx="{(h - 2) / 2}" fill="url(#gl)"/>')
        fg = TEXT
    if icon_name == "ghost":
        k = 20 / 100
        ic = (f'<g transform="translate(22 {h / 2 - 11}) scale({k})"><path d="{GHOST}" fill="{ACC2}" fill-rule="evenodd"/></g>')
    else:
        ic = icon(icon_name, 22, h / 2 - 10, 20, fg if primary else ACC2, 2.1)
    body = bg + ic + text(52, h / 2 + 5.4, label, 15, "Bold", fg)
    return svg(h, body, ["Bold"], label, wdt)


def card_about(data):
    rows = data["about"]
    h = 86 + len(rows) * 56 + 14
    b = [frame(h, "a", [(".95", "0", ".5", "#8b5cf6", ".25")]), title(28, 26, "heart", "About me")]
    y = 80
    for name, label in rows:
        b.append(f'<rect x="28" y="{y}" width="{W - 56}" height="46" rx="14" fill="#fff" fill-opacity=".045" stroke="#fff" stroke-opacity=".07"/>'
                 f'<rect x="28" y="{y + 12}" width="3" height="22" rx="1.5" fill="{ACC2}"/>'
                 f'<circle cx="62" cy="{y + 23}" r="14" fill="{ACC}" fill-opacity=".18"/>'
                 + icon(name, 53, y + 14, 18, ACC2) + text(88, y + 28.5, label, 15, "Medium", TEXT))
        y += 56
    return svg(h, "".join(b), ["Medium", "Bold"], "About me")


def card_stack(data):
    groups = data["stack"]
    h = 80 + len(groups) * 44 + 18
    b = [frame(h, "s", [(".05", "1", ".5", "#d946ef", ".12"), (".95", "0", ".45", "#8b5cf6", ".22")]), title(28, 26, "layers", "What I build with")]
    y = 80
    for label, items in groups:
        b.append(text(28, y + 22, label, 11, "Bold", MUTE, spacing=1.6))
        cx = 170
        for name, it in items:
            s, wdt = chip(cx, y + 2, name, it, h=32, size=13)
            b.append(s)
            cx += wdt + 8
        y += 44
    return svg(h, "".join(b), ["Medium", "Bold"], "What I build with")


def fmt(n):
    return "{:,}".format(n).replace(",", " ")


def ago(iso):
    if not iso:
        return ""
    d = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    return "released today" if d <= 0 else "released yesterday" if d == 1 else "released %d days ago" % d


def card_activity(data, st):
    h = 330
    b = [frame(h, "x", [(".2", "0", ".55", "#8b5cf6", ".22"), (".9", "1", ".5", "#6d28d9", ".18")]), title(28, 26, "pulse", "GitHub activity")]
    tiles = [("pulse", fmt(st["contrib"]), "Contributions · 12 months"), ("repo", fmt(st["repos"]), "Public repos"),
             ("star", fmt(st["stars"]), "Stars earned"), ("people", fmt(st["followers"]), "Followers")]
    for i, (name, val, label) in enumerate(tiles):
        x, y = 28 + (i % 2) * 196, 80 + (i // 2) * 92
        b.append(f'<rect x="{x}" y="{y}" width="186" height="82" rx="16" fill="#fff" fill-opacity=".05" stroke="#fff" stroke-opacity=".08"/>'
                 f'<rect x="{x + 14}" y="{y + 14}" width="28" height="28" rx="9" fill="{ACC}" fill-opacity=".2"/>'
                 + icon(name, x + 19, y + 19, 18, ACC2) + text(x + 52, y + 36, val, 24, "Bold", "#ffffff")
                 + text(x + 16, y + 66, label, 12, "Regular", MUTE))
    # 30 derniers jours en barres
    px, pw, ph, py = 438, W - 28 - 438, 174, 80
    b.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#fff" fill-opacity=".05" stroke="#fff" stroke-opacity=".08"/>')
    days = st["days"][-30:]
    tot = sum(c for _, c in days)
    b.append(text(px + 16, py + 26, "LAST 30 DAYS", 11, "Bold", MUTE, spacing=1.6))
    b.append(text(px + pw - 16, py + 26, "%s contributions" % fmt(tot), 12, "Medium", SOFT, "end"))
    b.append('<defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4a2ff"/><stop offset="1" stop-color="#7a4ee6"/></linearGradient></defs>')
    mx = max([c for _, c in days] + [1])
    area_x, area_w, base, top = px + 16, pw - 32, py + ph - 30, py + 44
    step = area_w / max(1, len(days))
    for i, (day, c) in enumerate(days):
        bw = step * .62
        bx = area_x + i * step + (step - bw) / 2
        hh = 4 if c == 0 else 8 + (base - top - 8) * (c / mx) ** .75
        fill, op = ("url(#bar)", 1) if c else ("#fff", .10)
        b.append(f'<rect x="{bx:.1f}" y="{base - hh:.1f}" width="{bw:.1f}" height="{hh:.1f}" rx="{min(bw / 2, 3.5):.1f}" fill="{fill}" fill-opacity="{op}"/>')
    if days:
        b.append(text(area_x, base + 20, dt.date.fromisoformat(days[0][0]).strftime("%d %b"), 11, "Regular", MUTE))
        b.append(text(area_x + area_w, base + 20, "today", 11, "Regular", MUTE, "end"))
    # bandeau du projet
    rel, y = st.get("release"), 270
    b.append(f'<rect x="28" y="{y}" width="{W - 56}" height="44" rx="14" fill="{ACC}" fill-opacity=".12" stroke="{ACC2}" stroke-opacity=".25"/>')
    k = 18 / 100
    b.append(f'<g transform="translate(44 {y + 13}) scale({k})"><path d="{GHOST}" fill="{ACC2}" fill-rule="evenodd"/></g>')
    name = data["project"][2]
    b.append(text(72, y + 27.5, name, 14, "Bold", TEXT))
    x = 72 + tw(name, 14, "Bold") + 10
    if rel:
        tag = rel["tag"]
        tgw = tw(tag, 12, "Bold") + 18
        b.append(f'<rect x="{x:.1f}" y="{y + 12}" width="{tgw:.1f}" height="20" rx="10" fill="{ACC}"/>' + text(x + tgw / 2, y + 26, tag, 12, "Bold", "#fff", "middle"))
        x += tgw + 12
        info = " · ".join(s for s in ("%s downloads" % fmt(rel["downloads"]), ago(rel["date"])) if s)
        b.append(text(x, y + 27.5, info, 13, "Regular", SOFT))
    b.append(text(W - 44, y + 27.5, "Updated " + st["updated"], 12, "Regular", MUTE, "end"))
    return svg(h, "".join(b), ["Regular", "Medium", "Bold"], "GitHub activity")


def card_featured(data, st):
    """Projet mis en avant : bannière de Phantom Boost, phrase, étiquettes, version et téléchargements."""
    path = os.path.join(ROOT, "featured.jpg")
    img = base64.b64encode(open(path, "rb").read()).decode() if os.path.exists(path) else None
    bw = W - 56
    bh = round(bw * 520 / 1600) if img else 0
    h = 80 + bh + (18 if img else 0) + 104
    b = [frame(h, "f", [(".9", "1", ".5", "#8b5cf6", ".22")]), title(28, 26, "spark", "Featured project")]
    y = 80
    if img:
        b.append(f'<defs><clipPath id="fc"><rect x="28" y="{y}" width="{bw}" height="{bh}" rx="16"/></clipPath></defs>'
                 f'<image x="28" y="{y}" width="{bw}" height="{bh}" preserveAspectRatio="xMidYMid slice" clip-path="url(#fc)" '
                 f'href="data:image/jpeg;base64,{img}"/>'
                 f'<rect x="28.5" y="{y + .5}" width="{bw - 1}" height="{bh - 1}" rx="16" fill="none" stroke="#fff" stroke-opacity=".12"/>')
        y += bh + 18
    name = data["project"][2]
    b.append(text(28, y + 22, name, 20, "Bold", "#ffffff"))
    x = 28 + tw(name, 20, "Bold") + 12
    rel = (st or {}).get("release") or data.get("release")
    if rel:
        tag = rel["tag"]
        tgw = tw(tag, 12, "Bold") + 18
        b.append(f'<rect x="{x:.1f}" y="{y + 7}" width="{tgw:.1f}" height="20" rx="10" fill="{ACC}"/>'
                 + text(x + tgw / 2, y + 21, tag, 12, "Bold", "#fff", "middle"))
        b.append(text(W - 28, y + 22, "%s downloads" % fmt(rel["downloads"]), 13, "Medium", SOFT, "end"))
    b.append(text(28, y + 50, data["featured_text"], 14, "Regular", SOFT))
    cx = 28
    for t in data["featured_tags"]:
        wdt = tw(t, 12, "Medium") + 26
        b.append(f'<rect x="{cx:.1f}" y="{y + 66}" width="{wdt:.1f}" height="26" rx="13" fill="#fff" fill-opacity=".07" stroke="#fff" stroke-opacity=".12"/>'
                 + text(cx + 13, y + 83.3, t, 12, "Medium", SOFT))
        cx += wdt + 8
    return svg(h, "".join(b), ["Regular", "Medium", "Bold"], "Featured project: " + name)


# ---------------------------------------------------------------- données
QUERY = """query(:String!,:String!,:String!){
 user(login:){ followers{totalCount}
  repositories(ownerAffiliations:OWNER,privacy:PUBLIC,first:100){totalCount nodes{stargazerCount}}
  contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}
 repository(owner:,name:){ latestRelease{tagName publishedAt}
  releases(first:100){nodes{releaseAssets(first:50){nodes{name downloadCount}}}}}}"""


def fetch(token):
    owner, repo, _ = CONFIG["project"]
    body = json.dumps(dict(query=QUERY, variables=dict(login=CONFIG["login"], owner=owner, repo=repo))).encode()
    req = urllib.request.Request("https://api.github.com/graphql", body, {"Authorization": "bearer " + token,
                                                                        "User-Agent": "profile-cards"})
    with urllib.request.urlopen(req, timeout=20) as r:
        res = json.load(r)
    if res.get("errors") and not res.get("data", {}).get("user"):
        raise RuntimeError(res["errors"])
    u, rp = res["data"]["user"], res["data"].get("repository")
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = [(d["date"], d["contributionCount"]) for w in cal["weeks"] for d in w["contributionDays"]]
    st = dict(contrib=cal["totalContributions"], repos=u["repositories"]["totalCount"], followers=u["followers"]["totalCount"],
              stars=sum(n["stargazerCount"] for n in u["repositories"]["nodes"]), days=days, release=None)
    if rp and rp.get("latestRelease"):
        dl = sum(a["downloadCount"] for r in rp["releases"]["nodes"] for a in r["releaseAssets"]["nodes"]
                 if a["name"].lower().endswith(".exe"))
        st["release"] = dict(tag=rp["latestRelease"]["tagName"], date=rp["latestRelease"]["publishedAt"], downloads=dl)
    return st


def sample():
    import random
    random.seed(7)
    today = dt.date.today()
    days = [((today - dt.timedelta(days=29 - i)).isoformat(), random.choice([0, 0, 0, 1, 2, 3, 5, 8])) for i in range(30)]
    return dict(contrib=154, repos=3, stars=12, followers=8, days=days,
                release=dict(tag="v1.0.1", date=(dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=2)).isoformat(), downloads=37))


def main():
    os.makedirs(OUT, exist_ok=True)
    data = dict(CONFIG)
    token = os.environ.get("GITHUB_TOKEN")
    st = None
    if "--sample" in sys.argv:
        st = sample()
    elif token:
        try:
            st = fetch(token)
        except Exception as e:  # réseau / API : on garde les anciennes cartes de chiffres
            print("Stats indisponibles :", e)
    files = {"hero.svg": None, "about.svg": card_about(data), "stack.svg": card_stack(data)}
    for key, ic, label, primary in data["buttons"]:
        files["btn-%s.svg" % key] = card_button(ic, label, primary)
    if st:
        st["updated"] = dt.date.today().strftime("%d %b %Y")
        data["release"] = st.get("release")
        files["activity.svg"] = card_activity(data, st)
    files["hero.svg"] = card_hero(data)
    if st or not os.path.exists(os.path.join(OUT, "featured.svg")):
        files["featured.svg"] = card_featured(data, st)
    for name, content in files.items():
        if content:
            with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
                f.write(content)
    print("Cartes :", ", ".join(n for n, c in files.items() if c))


if __name__ == "__main__":
    main()
