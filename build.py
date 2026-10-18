# Wraps src/app.html (artifact body) into a standalone page you can double-click.
import pathlib
src = pathlib.Path(__file__).with_name('src') / 'app.html'
body = src.read_text(encoding='utf-8')
head_end = body.index('</style>') + len('</style>')
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + body[:head_end] + '\n</head>\n<body>\n' + body[head_end:] + '\n</body>\n</html>\n')
out = pathlib.Path(__file__).with_name('Mavic 3 Flight Trainer.html')
out.write_text(page, encoding='utf-8')
(out.parent / 'index.html').write_text(page, encoding='utf-8')  # GitHub Pages entry point
print('wrote', out, 'and index.html', len(page), 'bytes')
