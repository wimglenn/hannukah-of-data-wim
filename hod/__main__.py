import runpy
from pathlib import Path


print("passwd: 5777")
scripts = sorted(Path(__file__).parent.glob("q*.py"))
for script in scripts:
    print(f" {script.name} ".center(40, "-"))
    runpy.run_path(script, run_name="__main__")
