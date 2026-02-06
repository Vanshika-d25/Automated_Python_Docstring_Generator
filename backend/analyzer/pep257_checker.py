import subprocess
import tempfile
import os

def check_pep257(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        temp_path = f.name

    result = subprocess.run(
        ["pydocstyle", temp_path],
        capture_output=True,
        text=True
    )

    os.remove(temp_path)

    return result.stdout if result.stdout else "PEP-257 Compliant"
