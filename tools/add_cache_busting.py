with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('const esc = s =>')
if idx != -1:
    line_end = c.find('\n', idx)
    newline = '\r\n' if '\r\n' in c else '\n'
    insert = 'const imgSrc = u => u ? (esc(u) + (u.includes("?") ? "&" : "?") + "v=20261122b") : "";' + newline
    c = c[:line_end+1] + insert + c[line_end+1:]

    replacements = [
        ('<img src="${esc(f)}" alt="${esc(figLabel(f))}">', '<img src="${imgSrc(f)}" alt="${esc(figLabel(f))}">'),
        ('<img src="${esc(q.markscheme)}"', '<img src="${imgSrc(q.markscheme)}"'),
        ('<img src="${esc(q.image)}"', '<img src="${imgSrc(q.image)}"'),
        ('<img loading="lazy" src="${esc(x.image)}"', '<img loading="lazy" src="${imgSrc(x.image)}"'),
        ('<img loading="lazy" src="${esc(f)}"', '<img loading="lazy" src="${imgSrc(f)}"'),
        ('<img loading="lazy" src="${esc(x.markscheme)}"', '<img loading="lazy" src="${imgSrc(x.markscheme)}"'),
        ('q.image ? `<img src="${esc(q.image)}"', 'q.image ? `<img src="${imgSrc(q.image)}"'),
        ('q.markscheme ? `<img src="${esc(q.markscheme)}"', 'q.markscheme ? `<img src="${imgSrc(q.markscheme)}"'),
        ('`<img src="${esc(f)}" alt="${figLabel(f)}">`', '`<img src="${imgSrc(f)}" alt="${figLabel(f)}">`'),
    ]
    for old, new in replacements:
        c = c.replace(old, new)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated index.html successfully with cache-busting!")
else:
    print("Could not find esc!")
