"""
Patches 'untitled - Kareem.epub':
- Embeds ZenDots-Regular.ttf
- Adds @font-face to stylesheet.css
- Replaces titlepage.xhtml with styled cover (ZenDots for cover only)
- Updates content.opf manifest
Outputs: 'untitled - Kareem - patched.epub'
"""

import zipfile
import shutil
import os
import re

INPUT_EPUB = "untitled - Kareem.epub"
OUTPUT_EPUB = "untitled - Kareem - patched.epub"
FONT_FILE = "ZenDots-Regular.ttf"
FONT_DEST = "fonts/ZenDots-Regular.ttf"

COVER_XHTML = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <meta charset="UTF-8"/>
  <title>Cover</title>
  <style type="text/css">
    @font-face {
      font-family: "ZenDots";
      src: url("fonts/ZenDots-Regular.ttf") format("truetype");
      font-weight: normal;
      font-style: normal;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    html, body { width: 100%; height: 100%; }

    .cover {
      background-color: #E8820C;
      width: 100%;
      height: 100%;
      min-height: 100vh;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-orient: vertical;
      -webkit-box-direction: normal;
      -ms-flex-direction: column;
      flex-direction: column;
      -webkit-box-pack: center;
      -ms-flex-pack: center;
      justify-content: center;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      padding: 8% 10%;
    }

    .title-block {
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-orient: vertical;
      -webkit-box-direction: normal;
      -ms-flex-direction: column;
      flex-direction: column;
      -webkit-box-pack: center;
      -ms-flex-pack: center;
      justify-content: center;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      text-align: center;
    }

    .title {
      font-family: "ZenDots", Georgia, serif;
      font-size: 2.8em;
      font-weight: normal;
      color: #F5F2EC;
      letter-spacing: 0.05em;
      line-height: 1.2;
      margin-bottom: 0.5em;
    }

    .volume {
      font-family: "ZenDots", Georgia, serif;
      font-size: 1.0em;
      font-weight: normal;
      color: #F5F2EC;
      letter-spacing: 0.2em;
      opacity: 0.85;
    }

    .author-block {
      text-align: center;
      padding-bottom: 2%;
    }

    .author {
      font-family: "ZenDots", Georgia, serif;
      font-size: 0.85em;
      font-weight: normal;
      color: #F5F2EC;
      letter-spacing: 0.2em;
      opacity: 0.75;
    }
  </style>
</head>
<body>
  <div class="cover">
    <div class="title-block">
      <div class="title">Untitled</div>
      <div class="volume">Volume I</div>
    </div>
    <div class="author-block">
      <div class="author">Kareem</div>
    </div>
  </div>
</body>
</html>
"""

FONT_FACE = """\

@font-face {
  font-family: "ZenDots";
  src: url("fonts/ZenDots-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
"""

def patch_opf(opf_content, font_dest):
    """Add font to manifest if not already present."""
    font_item = '<item id="font-zendots" href="{}" media-type="application/x-font-ttf"/>'.format(font_dest)
    if "font-zendots" not in opf_content:
        # Insert before closing </manifest>
        opf_content = opf_content.replace("</manifest>", "  {}\n  </manifest>".format(font_item))
    return opf_content

def main():
    if not os.path.exists(INPUT_EPUB):
        print("ERROR: {} not found".format(INPUT_EPUB))
        return
    if not os.path.exists(FONT_FILE):
        print("ERROR: {} not found".format(FONT_FILE))
        return

    with open(FONT_FILE, "rb") as f:
        font_data = f.read()

    # Read all files from input epub
    files = {}
    with zipfile.ZipFile(INPUT_EPUB, "r") as z:
        for name in z.namelist():
            files[name] = z.read(name)

    # Replace titlepage.xhtml
    if "titlepage.xhtml" in files:
        files["titlepage.xhtml"] = COVER_XHTML.encode("utf-8")
        print("Replaced titlepage.xhtml")
    else:
        files["titlepage.xhtml"] = COVER_XHTML.encode("utf-8")
        print("Added titlepage.xhtml (was not present)")

    # Embed font
    files[FONT_DEST] = font_data
    print("Embedded {}".format(FONT_DEST))

    # Patch stylesheet.css — add @font-face if not present
    css_key = None
    for name in files:
        if name.endswith("stylesheet.css"):
            css_key = name
            break
    if css_key:
        css = files[css_key].decode("utf-8")
        if "ZenDots" not in css:
            css = FONT_FACE + css
            files[css_key] = css.encode("utf-8")
            print("Patched {}".format(css_key))
    else:
        print("WARNING: stylesheet.css not found — font-face not added to stylesheet")

    # Patch content.opf — add font to manifest
    opf_key = None
    for name in files:
        if name.endswith("content.opf"):
            opf_key = name
            break
    if opf_key:
        opf = files[opf_key].decode("utf-8")
        opf = patch_opf(opf, FONT_DEST)
        files[opf_key] = opf.encode("utf-8")
        print("Patched {}".format(opf_key))
    else:
        print("WARNING: content.opf not found")

    # Write output epub
    if os.path.exists(OUTPUT_EPUB):
        os.remove(OUTPUT_EPUB)

    with zipfile.ZipFile(OUTPUT_EPUB, "w", zipfile.ZIP_DEFLATED) as z:
        # mimetype must be first and uncompressed
        if "mimetype" in files:
            z.writestr(
                zipfile.ZipInfo("mimetype"),
                files["mimetype"],
                compress_type=zipfile.ZIP_STORED
            )
        for name, data in files.items():
            if name == "mimetype":
                continue
            z.writestr(name, data)

    print("\nDone. Output: {}".format(OUTPUT_EPUB))


if __name__ == "__main__":
    main()
