#!/usr/bin/env python3
"""Bangun index.html dari src/template.html + data/dc_data.json.

Jalankan dari folder repo:  python3 src/build.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
data = (ROOT / "data" / "dc_data.json").read_text(encoding="utf-8")
json.loads(data)                                   # pastikan JSON valid
assert "</script" not in data.lower()
assert tpl.count("__DATA__") == 1

page = tpl.replace("__DATA__", data)
cut = page.index("</style>") + len("</style>")
head, body = page[:cut], page[cut:]

ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Ccircle cx='16' cy='16' r='14' fill='%2313845A'/%3E%3Ccircle cx='16' cy='16' r='6' fill='%23FAFCFB'/%3E%3C/svg%3E")
DESC = ("Peta interaktif data center di Asia Tenggara: fasilitas yang beroperasi, dibangun, dan direncanakan, "
        "lengkap dengan kapasitas MW per tahap dan wilayah.")

html = f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{DESC}">
<meta property="og:title" content="Peta Data Center Asia Tenggara">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#EBF0EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0C1315" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{ICON}">
{head}
</head>
<body>
{body}
</body>
</html>
"""
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html ditulis:", round(len(html) / 1024), "KB")
