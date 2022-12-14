import os, glob

folders = {}
for f in glob.glob("**", recursive=True):
    if os.path.isdir(f):
        t = folders
        for s in f.split("\\"):
            if s in t:
                t = t[s]
            else:
                t[s] = {}

    if os.path.isfile(f):
        if os.path.split(f)[1].startswith("index."):
            continue
        t = folders
        ext = os.path.splitext(f)
        if ext[1] in [".htm", ".html"]:
            for s in f.split("\\"):
                if s in t:
                    t = t[s]
                else:
                    t[s] = f

def listup(file, folder, cnt):
    for k, v in folder.items():
        if isinstance(v, dict):
            file.write(f"<h{cnt}>{k}</h{cnt}>\n")
            file.write("<ul>\n")
            listup(file, v, cnt+1)
            file.write("</ul>\n")
        else:
            file.write(f"<li><a href='{v}'>{k}</a></li>\n")

with open("index.htm", mode="w", encoding="utf-8") as file:
    file.write("""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>""")
    listup(file, folders, 1)
    file.write("</body></html>")