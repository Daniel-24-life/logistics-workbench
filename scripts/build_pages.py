from pathlib import Path
from shutil import copyfile
import sys

repository = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1])
files = {
    "index.html": "dist/index.html",
    "styles.css": "dist/styles.css",
    "app.js": "dist/app.js",
    "policy.js": "dist/policy.js"
}

for output_path, input_path in files.items():
    target = out / output_path
    target.parent.mkdir(parents=True, exist_ok=True)
    copyfile(repository / input_path, target)
