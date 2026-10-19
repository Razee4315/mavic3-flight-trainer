# Builds everything GitHub Pages serves from docs/:
#   - the simulator: src/app.html wrapped into a standalone page (docs/app/ and a double-clickable copy at the root)
#   - the website: the pages defined in site/pages.py
import pathlib, sys
ROOT = pathlib.Path(__file__).parent
body = (ROOT / 'src' / 'app.html').read_text(encoding='utf-8')
head_end = body.index('</style>') + len('</style>')
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + body[:head_end] + '\n</head>\n<body>\n' + body[head_end:] + '\n</body>\n</html>\n')
(ROOT / 'Mavic 3 Flight Trainer.html').write_text(page, encoding='utf-8')
app = ROOT / 'docs' / 'app' / 'index.html'
app.parent.mkdir(parents=True, exist_ok=True)
app.write_text(page, encoding='utf-8')
print('wrote simulator', len(page), 'bytes')

sys.path.insert(0, str(ROOT / 'site'))
import pages
pages.build(ROOT / 'docs')
