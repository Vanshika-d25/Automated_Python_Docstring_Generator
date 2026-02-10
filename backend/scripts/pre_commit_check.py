import sys
import os
import subprocess
from pathlib import Path

# -------------------------------
# Fix Python import path
# -------------------------------
# Add backend/ to PYTHONPATH so "analyzer" can be imported
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# -------------------------------
# TOML compatibility
# -------------------------------
try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # Python < 3.11

# -------------------------------
# Internal imports
# -------------------------------
from analyzer.ast_parser import analyze_code
from analyzer.pep257_checker import check_pep257


def load_config():
    config_path = Path("pyproject.toml")
    if not config_path.exists():
        print("❌ pyproject.toml not found")
        sys.exit(1)

    with open(config_path, "rb") as f:
        data = tomllib.load(f)

    return data["tool"]["docstring_enforcer"]


def get_staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True
    )
    return [f for f in result.stdout.splitlines() if f.endswith(".py")]


def main():
    config = load_config()
    style = config["style"]
    min_coverage = config["min_coverage"]
    fail_on_pep257 = config["fail_on_pep257"]

    files = get_staged_files()
    if not files:
        sys.exit(0)

    combined_code = ""
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            combined_code += f.read() + "\n"

    result = analyze_code(combined_code, style)
    coverage = result["stats"]["coverage_percent"]

    if coverage < min_coverage:
        print(f"❌ Docstring coverage {coverage}% < required {min_coverage}%")
        sys.exit(1)

    if fail_on_pep257:
        pep_report = check_pep257(combined_code)
        if pep_report != "PEP-257 Compliant":
            print("❌ PEP-257 violations found:")
            print(pep_report)
            sys.exit(1)

    print("✅ Docstring checks passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
