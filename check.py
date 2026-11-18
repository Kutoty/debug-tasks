"""Show that each buggy module fails and each fixed module passes."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent / "tasks"
CASES = {
    "off-by-one": ("total", lambda fn: fn([1, 2, 3]) == 6),
    "missing-key": ("lookup", lambda fn: fn("missing") is None),
    "wrong-mean": ("mean", lambda fn: fn([2, 4]) == 3),
}

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    failures = 0
    for name, (fn_name, expect) in CASES.items():
        buggy = load(ROOT / name / "buggy.py", f"{name}_buggy")
        fixed = load(ROOT / name / "fixed.py", f"{name}_fixed")
        buggy_ok = safe(expect, getattr(buggy, fn_name))
        fixed_ok = safe(expect, getattr(fixed, fn_name))
        if buggy_ok or not fixed_ok:
            failures += 1
            print(f"FAIL {name}: buggy_passed={buggy_ok} fixed_passed={fixed_ok}")
        else:
            print(f"OK   {name}: buggy fails, fix passes")
    if failures:
        raise SystemExit(1)
    print(f"{len(CASES)} tasks checked")

def safe(expect, fn):
    try:
        return bool(expect(fn))
    except Exception:
        return False

if __name__ == "__main__":
    main()
