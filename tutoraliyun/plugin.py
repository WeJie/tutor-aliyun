from glob import glob
import os

HERE = os.path.abspath(os.path.dirname(__file__))


templates = os.path.join(HERE, "templates")


config = {
    "add": {
        "USE_NAS_STORAGE": False,
    },
}




def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
