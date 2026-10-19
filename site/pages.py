# The Mavic 3 Flight Trainer website. build.py calls build(docs_dir).
# Every page shares one layout; each one has its own title, description, canonical URL and structured data.
import json, datetime, pathlib, html

SITE = 'https://razee4315.github.io/mavic3-flight-trainer/'
BASE = '/mavic3-flight-trainer/'
NAME = 'Mavic 3 Flight Trainer'
REPO = 'https://github.com/Razee4315/mavic3-flight-trainer'
APP = BASE + 'app/'
TODAY = datetime.date.today().isoformat()
NAV = [('features/', 'Features'), ('lessons/', 'Lessons'), ('controls/', 'Controls'), ('faq/', 'FAQ'), ('about/', 'About')]

ICON = {
    'play': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg>',
    'gps': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/><circle cx="12" cy="12" r="7"/></svg>',
    'modes': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 18l5-6 4 3 7-9"/><path d="M15 6h5v5"/></svg>',
    'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
    'camera': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h3l2-2h6l2 2h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    'remote': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="9" width="18" height="10" rx="4"/><circle cx="8" cy="14" r="1.6"/><circle cx="16" cy="14" r="1.6"/><path d="M12 9V4"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
}

LESSONS = [
    ('Basics', [
        ('Know your remote', 'Every stick, switch and button on the RC-N1, with the motors locked.'),
        ('Motors, takeoff and hover', 'Start the motors with the stick command, lift off, hover and land.'),
        ('Altitude and yaw', 'Climb to 10 m, spin a full circle each way and land on the pad.'),
        ('Forward, back and sideways', 'Fly through five rings using only pitch and roll.'),
    ]),
    ('Orientation', [
        ('Square pattern, tail-in', 'Visit four corners of a 25 m square without turning the nose.'),
        ('Nose-forward circuit', 'Fly the square again, turning so the camera faces where you go.'),
        ('Nose-in orientation', 'The drone faces you and left and right feel reversed.'),
        ('Orbit the water tower', 'Circle a point of interest while keeping the camera on it.'),
    ]),
    ('Advanced', [
        ('Figure eight', 'Seven rings on a figure-eight track with smooth, blended turns.'),
        ('Precision landing on a roof', 'Land on a rooftop pad, then fly home.'),
        ('Wind and ATTI mode', 'No GPS and a 7 m/s wind. You hold the drone in place.'),
        ('Return to Home', 'Trigger RTH, cancel it, then let the drone bring itself home.'),
        ('Cinematic shot', 'Cine mode, a gimbal tilt and a well framed photo.'),
    ]),
]

FAQ = [
    ('Is the Mavic 3 Flight Trainer free?', 'Yes. It is free and open source. It runs in your browser with nothing to install.'),
    ('Do I need a controller?', 'No. A keyboard works. Xbox and PlayStation gamepads work too, and so does an RC transmitter in USB joystick mode. Phones and tablets get on-screen sticks.'),
    ('Which stick mode should I pick?', 'Mode 2. It is the DJI default: the left stick controls throttle and yaw, the right stick controls pitch and roll. Pick Mode 1 or 3 only if your real remote is set that way.'),
    ('How realistic is it?', 'It uses the Mavic 3 published speeds for Cine, Normal and Sport mode, and copies GPS braking, ATTI drift, obstacle sensing and Return to Home. It is a training aid, not an exact flight model.'),
    ('Can it replace real flight training?', 'No. Use it to learn the controls and build habits, then practise with the real aircraft in an open area and follow your local aviation rules.'),
    ('Does it work on a phone?', 'Yes. It runs in any modern browser, including mobile Chrome and Safari, with touch sticks on screen.'),
    ('Is this an official DJI product?', 'No. It is an unofficial Final Year Project and is not affiliated with or endorsed by DJI.'),
]


def esc(s): return html.escape(s, quote=True)


def layout(path, title, desc, body, schema=(), noindex=False, crumbs=None):
    url = SITE + path
    nav = ''.join(f'<li><a href="{BASE}{p}"{" aria-current=page" if p == path else ""}>{n}</a></li>' for p, n in NAV)
    ld = list(schema)
    if crumbs:
        ld.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE},
            {'@type': 'ListItem', 'position': 2, 'name': crumbs, 'item': url}]})
    ld_html = ''.join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{BASE}">Home</a> / {esc(crumbs)}</nav>' if crumbs else ''
    year = datetime.date.today().year
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{'<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'}
<meta name="theme-color" content="#0a0e12" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f7f8fa" media="(prefers-color-scheme: light)">
<link rel="icon" type="image/svg+xml" href="{BASE}assets/logo.svg">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}assets/img/og.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@600&display=swap">
<link rel="stylesheet" href="{BASE}assets/site.css">{ld_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="{BASE}"><img src="{BASE}assets/logo.svg" alt="" width="32" height="32">{NAME}</a>
    <ul class="links">{nav}<li class="m-cta"><a class="btn primary" href="{APP}">Launch simulator</a></li></ul>
    <a class="btn primary sm cta" href="{APP}">Launch simulator</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav">{ICON['menu']}</button>
  </div>
</header>
<main id="main">
{crumb_html and f'<div class="wrap page-head">{crumb_html}</div>'}
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="brand" href="{BASE}"><img src="{BASE}assets/logo.svg" alt="" width="32" height="32">{NAME}</a>
        <p>A free 3D simulator for learning the DJI Mavic 3 and RC-N1 controls. Built as a Final Year Project.</p>
      </div>
      <div><h3>Learn</h3><ul><li><a href="{BASE}lessons/">Lessons</a></li><li><a href="{BASE}controls/">Controls</a></li><li><a href="{BASE}features/">Features</a></li></ul></div>
      <div><h3>Project</h3><ul><li><a href="{BASE}about/">About</a></li><li><a href="{BASE}faq/">FAQ</a></li><li><a href="{REPO}" rel="noopener">GitHub</a></li></ul></div>
    </div>
    <div class="legal"><span>© {year} {NAME}</span><span>Unofficial. Not affiliated with or endorsed by DJI.</span></div>
  </div>
</footer>
<script>
const nav=document.getElementById('nav'),b=nav.querySelector('.menu-btn');
b.addEventListener('click',()=>{{const o=nav.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>
'''


def card(icon, title, text): return f'<div class="card"><div class="ic">{ICON[icon]}</div><h3>{title}</h3><p>{text}</p></div>'


def home():
    body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow"><i></i>Free · Runs in your browser</span>
    <h1>Learn to fly the DJI Mavic 3<br>before you fly the real one.</h1>
    <p class="lede">A 3D flight simulator with the real RC-N1 remote, Mavic 3 flight modes and 13 guided lessons.</p>
    <div class="cta-row">
      <a class="btn primary" href="{APP}">{ICON['play']}Launch simulator</a>
      <a class="btn" href="{BASE}lessons/">See the lessons</a>
    </div>
    <div class="shot"><img src="{BASE}assets/img/start.webp" alt="Mavic 3 Flight Trainer start screen with the drone on its landing pad and the 13-lesson training course" width="1440" height="900" fetchpriority="high"></div>
    <div class="stats">
      <div class="stat"><b>13</b><span>guided lessons</span></div>
      <div class="stat"><b>3</b><span>stick modes</span></div>
      <div class="stat"><b>0</b><span>installs</span></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><h2>Flies like the real thing</h2><p>Built around the Mavic 3's published specs and behaviour.</p></div>
    <div class="grid">
      {card('modes', 'Cine, Normal, Sport', '5, 15 and 21 m/s top speeds, just like the real flight mode switch.')}
      {card('gps', 'GPS hold and braking', 'Let go of the sticks and it stops and hovers. Lose GPS and it drifts.')}
      {card('shield', 'Obstacle sensing', 'Braking in Normal and Cine. Off in Sport, just like the aircraft.')}
      {card('home', 'Return to Home', 'Climbs, flies home and lands. Smart low-battery RTH included.')}
      {card('camera', 'Gimbal and zoom', 'Tilt from −90° to +35°, zoom up to 28x, take photos and video.')}
      {card('remote', 'A 3D RC-N1 remote', 'Sticks, switches and buttons move as you fly, with a live camera feed.')}
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><h2>See it in action</h2></div>
    <div class="gallery">
      <figure><img src="{BASE}assets/img/lesson-960.webp" alt="Lesson panel guiding the pilot through the throttle on the 3D RC-N1 remote" width="960" height="600" loading="lazy"><figcaption>Step-by-step lessons</figcaption></figure>
      <figure><img src="{BASE}assets/img/flight-960.webp" alt="Mavic 3 in flight over the training field in chase view" width="960" height="600" loading="lazy"><figcaption>Chase view in flight</figcaption></figure>
      <figure><img src="{BASE}assets/img/camera-960.webp" alt="Camera view from the Mavic 3 gimbal, like DJI Fly" width="960" height="600" loading="lazy"><figcaption>Camera view, like DJI Fly</figcaption></figure>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><h2>How it works</h2></div>
    <ol class="steps">
      <li><h3>Pick your stick mode</h3><p>Match your real remote. Mode 2 is the DJI default.</p></li>
      <li><h3>Follow the lessons</h3><p>From the first takeoff to Return to Home, one skill at a time.</p></li>
      <li><h3>Fly free</h3><p>Practise in wind, on a low battery, or in Sport mode.</p></li>
    </ol>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="band">
      <div><h2>Ready for your first flight?</h2><p>No download, no account. Open it and fly.</p></div>
      <a class="btn primary" href="{APP}">{ICON['play']}Launch simulator</a>
    </div>
  </div>
</section>'''
    schema = [
        {'@context': 'https://schema.org', '@type': 'WebSite', 'name': NAME, 'url': SITE},
        {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': NAME, 'url': SITE + 'app/',
         'applicationCategory': 'SimulationApplication', 'operatingSystem': 'Any (web browser)',
         'description': 'Free browser-based 3D flight simulator for learning the DJI Mavic 3 and RC-N1 remote controls.',
         'image': SITE + 'assets/img/og.jpg', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}},
    ]
    return layout('', 'Mavic 3 Flight Trainer: Free DJI Drone Simulator in Your Browser',
                  'Learn to fly the DJI Mavic 3 before your first real flight. Free 3D drone simulator with the RC-N1 remote, real flight modes and 13 guided lessons.',
                  body, schema)


def features():
    body = f'''
<div class="wrap page-body">
  <div class="prose">
    <h1>Features</h1>
    <p class="lede">Everything the trainer simulates, and how it matches the real Mavic 3.</p>
    <h2>Flight modes</h2>
    <p>The C / N / S switch changes speed and sensing, using the Mavic 3's published figures.</p>
    <div class="table"><table><thead><tr><th>Mode</th><th>Max speed</th><th>Climb</th><th>Obstacle sensing</th></tr></thead><tbody>
      <tr><td>Cine</td><td>5 m/s</td><td>1 m/s</td><td>On</td></tr>
      <tr><td>Normal</td><td>15 m/s</td><td>6 m/s</td><td>On</td></tr>
      <tr><td>Sport</td><td>21 m/s</td><td>8 m/s</td><td>Off</td></tr>
    </tbody></table></div>
    <h2>GPS position hold and ATTI mode</h2>
    <p>With GPS, the drone brakes and holds its spot when you let go, leaning into the wind. Without GPS it switches to ATTI mode and drifts, so you hold it in place yourself.</p>
    <h2>Combination Stick Command</h2>
    <p>Start and stop the motors with both sticks down and inward, as on the real aircraft. Hold the throttle down after landing to stop them.</p>
    <h2>Obstacle sensing</h2>
    <p>Braking and radar arcs in Normal and Cine. Sensing is off in Sport mode, and thin power lines can't be detected.</p>
    <h2>Return to Home</h2>
    <p>RTH climbs to the RTH altitude, flies home and lands. Smart low-battery RTH and a forced landing at critical battery are included.</p>
    <h2>Gimbal and camera</h2>
    <p>Tilt from −90° to +35°, recentre with Fn, and zoom 1x, 3x, 7x or 28x. Take photos and record video.</p>
    <h2>The RC-N1 remote, in 3D</h2>
    <p>The sticks tilt, the mode switch slides, the gimbal dial rolls and the buttons press as you fly. The phone in the clamp shows the live camera feed.</p>
    <h2>Three views</h2>
    <ul><li><strong>Chase:</strong> behind the drone, pulling back as you speed up.</li><li><strong>Camera:</strong> what DJI Fly shows.</li><li><strong>Pilot:</strong> line of sight from where you stand.</li></ul>
    <div class="cta-row"><a class="btn primary" href="{APP}">{ICON['play']}Try it now</a></div>
  </div>
</div>'''
    return layout('features/', 'Features: Realistic Mavic 3 Flight Modes, GPS and RTH | Mavic 3 Flight Trainer',
                  'Cine, Normal and Sport modes with real Mavic 3 speeds, GPS braking, ATTI drift, obstacle sensing, Return to Home and a 3D RC-N1 remote.',
                  body, crumbs='Features')


def lessons():
    groups, n, items = '', 0, []
    for g, ls in LESSONS:
        rows = ''
        for t, s in ls:
            n += 1; items.append({'@type': 'ListItem', 'position': n, 'name': t, 'description': s})
            rows += f'<div class="lesson"><span class="n">{n:02d}</span><div><h3>{t}</h3><p>{s}</p></div></div>'
        groups += f'<div class="lesson-group"><h2>{g}</h2>{rows}</div>'
    body = f'''
<div class="wrap page-body">
  <div class="prose">
    <h1>Drone training lessons</h1>
    <p class="lede">13 short lessons that take you from your first takeoff to flying in wind without GPS. Do them in order.</p>
    {groups}
    <div class="cta-row"><a class="btn primary" href="{APP}">{ICON['play']}Start lesson 1</a></div>
  </div>
</div>'''
    schema = [{'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Mavic 3 training lessons', 'itemListElement': items}]
    return layout('lessons/', '13 Beginner Drone Training Lessons for the DJI Mavic 3 | Mavic 3 Flight Trainer',
                  'Learn takeoff, hover, yaw, orientation, orbits, precision landing, ATTI mode and Return to Home in 13 guided drone lessons.',
                  body, schema, crumbs='Lessons')


def controls():
    body = f'''
<div class="wrap page-body">
  <div class="prose">
    <h1>RC-N1 controls and stick modes</h1>
    <p class="lede">How the DJI RC-N1 sticks work, and how they map to your keyboard or gamepad.</p>
    <h2>Stick modes</h2>
    <p>Pick the same mode your real remote uses (DJI Fly → Control → Stick Mode). Mode 2 is the default.</p>
    <div class="table"><table><thead><tr><th>Mode</th><th>Left stick</th><th>Right stick</th></tr></thead><tbody>
      <tr><td>Mode 2</td><td>Throttle ↕ · Yaw ↔</td><td>Pitch ↕ · Roll ↔</td></tr>
      <tr><td>Mode 1</td><td>Pitch ↕ · Yaw ↔</td><td>Throttle ↕ · Roll ↔</td></tr>
      <tr><td>Mode 3</td><td>Pitch ↕ · Roll ↔</td><td>Throttle ↕ · Yaw ↔</td></tr>
    </tbody></table></div>
    <h2>Keyboard and gamepad</h2>
    <div class="table"><table><thead><tr><th>Real remote</th><th>Keyboard</th><th>Gamepad</th></tr></thead><tbody>
      <tr><td>Left stick</td><td><kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd></td><td>Left stick</td></tr>
      <tr><td>Right stick</td><td>Arrow keys</td><td>Right stick</td></tr>
      <tr><td>Start / stop motors</td><td><kbd>S</kbd>+<kbd>D</kbd> with <kbd>↓</kbd>+<kbd>←</kbd></td><td>Both sticks down and in</td></tr>
      <tr><td>Flight mode C / N / S</td><td><kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd></td><td>D-pad</td></tr>
      <tr><td>Pause / Return to Home</td><td><kbd>Space</kbd> tap / <kbd>H</kbd> hold</td><td>B</td></tr>
      <tr><td>Auto takeoff / land</td><td>Hold <kbd>T</kbd></td><td>Start</td></tr>
      <tr><td>Gimbal dial</td><td><kbd>Q</kbd> / <kbd>E</kbd></td><td>LT / RT</td></tr>
      <tr><td>Shutter</td><td><kbd>P</kbd></td><td>A</td></tr>
      <tr><td>Change view</td><td><kbd>C</kbd></td><td>Y</td></tr>
      <tr><td>Menu</td><td><kbd>Esc</kbd></td><td>Back</td></tr>
    </tbody></table></div>
    <p>Hold <kbd>Shift</kbd> for gentle stick input. You can also drag the sticks on the 3D remote with the mouse.</p>
    <h2>Starting the motors</h2>
    <p>DJI drones use the <strong>Combination Stick Command</strong>: pull both sticks down and inward until the motors spin, then push the throttle up gently. After landing, hold the throttle down until the motors stop.</p>
    <div class="cta-row"><a class="btn primary" href="{APP}">{ICON['play']}Practise the controls</a></div>
  </div>
</div>'''
    return layout('controls/', 'DJI RC-N1 Controls and Stick Modes Explained | Mavic 3 Flight Trainer',
                  'Mode 1, Mode 2 and Mode 3 stick layouts for the DJI RC-N1, the combination stick command, and keyboard and gamepad controls.',
                  body, crumbs='Controls')


def faq():
    qs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    body = f'''
<div class="wrap page-body">
  <div class="prose">
    <h1>Frequently asked questions</h1>
    <p class="lede">Short answers about the trainer.</p>
    <div style="margin-top:32px">{qs}</div>
  </div>
</div>'''
    schema = [{'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}]
    return layout('faq/', 'FAQ: Free DJI Mavic 3 Drone Simulator | Mavic 3 Flight Trainer',
                  'Is it free, do you need a controller, which stick mode to use and how realistic it is. Answers about the Mavic 3 Flight Trainer.',
                  body, schema, crumbs='FAQ')


def about():
    body = f'''
<div class="wrap page-body">
  <div class="prose">
    <h1>About the project</h1>
    <p class="lede">Why we built a Mavic 3 simulator.</p>
    <h2>A Final Year Project</h2>
    <p>This trainer is our Final Year Project. Our project needed us to learn the basic controls of a drone, and practising on a real aircraft is expensive and risky for a beginner. So we built a safe place to learn the Mavic 3 and its RC-N1 remote first.</p>
    <h2>How it's built</h2>
    <p>It's a single web page using <strong>Three.js</strong> for the 3D world, the drone and the remote. Flight behaviour follows the Mavic 3's published specs. The source is on <a href="{REPO}" rel="noopener">GitHub</a>.</p>
    <div class="note">Unofficial training tool. Not affiliated with or endorsed by DJI. For real flights, follow the official manual and your local aviation rules.</div>
  </div>
</div>'''
    return layout('about/', 'About: A Final Year Project Drone Simulator | Mavic 3 Flight Trainer',
                  'Why we built the Mavic 3 Flight Trainer: a Final Year Project to learn basic drone controls safely before flying the real aircraft.',
                  body, crumbs='About')


def not_found():
    body = f'''
<section class="hero"><div class="wrap">
  <h1>Page not found</h1>
  <p class="lede">That page doesn't exist. Try the simulator or the home page.</p>
  <div class="cta-row"><a class="btn primary" href="{APP}">Launch simulator</a><a class="btn" href="{BASE}">Home</a></div>
</div></section>'''
    return layout('404.html', 'Page not found | Mavic 3 Flight Trainer', 'This page does not exist.', body, noindex=True)


PAGES = {'': home, 'features/': features, 'lessons/': lessons, 'controls/': controls, 'faq/': faq, 'about/': about}


def build(out: pathlib.Path):
    for path, fn in PAGES.items():
        f = out / path / 'index.html'; f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(fn(), encoding='utf-8')
    (out / '404.html').write_text(not_found(), encoding='utf-8')
    urls = list(PAGES) + ['app/']
    pri = {'': '1.0', 'app/': '0.9'}
    sm = ''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pri.get(p, "0.7")}</priority></url>\n' for p in urls)
    (out / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n', encoding='utf-8')
    (out / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n', encoding='utf-8')
    (out / '.nojekyll').write_text('', encoding='utf-8')
    print('wrote website:', len(PAGES), 'pages, 404, sitemap.xml, robots.txt')
