import os

for fpath in ['file/navbar.css', 'happybday/file/navbar.css']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make responsive
    content = content.replace('min-width: 68px;', 'min-width: 0;')
    content = content.replace('padding: 6px 12px;', 'padding: 6px 5px; flex: 1; text-align: center;')
    content = content.replace('font-size: 11px;', 'font-size: 9px;')
    content = content.replace('font-size: 18px;', 'font-size: 16px;')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed navbar CSS")
