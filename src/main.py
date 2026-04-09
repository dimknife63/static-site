import sys
import os
import shutil
sys.path.append(os.path.dirname(__file__))

from generate_page import generate_pages_recursive


def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isfile(s):
            print(f"Copying {s} -> {d}")
            shutil.copy(s, d)
        else:
            copy_static(s, d)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()