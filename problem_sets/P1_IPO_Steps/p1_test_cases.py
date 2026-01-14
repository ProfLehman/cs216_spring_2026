import subprocess
import sys
from pathlib import Path

# p1_test_cases.py
# spring 2026
# prof. lehman
# automated sample test cases

TIMEOUT_SECONDS = 2
STUDENT_FILE = "p1.py"   # require students to name their file this

TESTS = [
    {
        "name": "Sample 1: under 10,000",
        "inp": "3000\n28\n",
        "expected": "\n".join([
            "Enter number of steps",
            "Enter stride distance in inches",
            "You walked 3,000 steps which is 1.33 miles",
            "You need 7,000 more steps to reach 10,000",
        ])
    },
    {
        "name": "Sample 2: over 10,000",
        "inp": "12500\n28\n",
        "expected": "\n".join([
            "Enter number of steps",
            "Enter stride distance in inches",
            "You walked 12,500 steps which is 5.52 miles",
            "You were 2,500 steps over 10,000",
        ])
    },
    {
        "name": "Sample 3: exactly 10,000",
        "inp": "10000\n28\n",
        "expected": "\n".join([
            "Enter number of steps",
            "Enter stride distance in inches",
            "You walked 10,000 steps which is 4.42 miles",
            "You walked exactly 10,000 steps",
        ])
    },
    # Optional edge cases — keep/remove based on what you want to require
    {
        "name": "Sample 4: 9999 steps",
        "inp": "9999\n28\n",
        "expected": "\n".join([
            "Enter number of steps",
            "Enter stride distance in inches",
            "You walked 9,999 steps which is 4.42 miles",
            "You need 1 more steps to reach 10,000",
        ])
    },
    {
        "name": "Sample 5: 10001 steps",
        "inp": "10001\n28\n",
        "expected": "\n".join([
            "Enter number of steps",
            "Enter stride distance in inches",
            "You walked 10,001 steps which is 4.42 miles",
            "You were 1 steps over 10,000",
        ])
    },
    {
        "name": "Sample 6: 0 steps",
        "inp": "0\n28\n",
        "expected": "\n".join([
            "Enter number of steps",
            "Enter stride distance in inches",
            "You walked 0 steps which is 0.00 miles",
            "You need 10,000 more steps to reach 10,000",
        ])
    },
]

def indent(text: str, spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(pad + line for line in text.split("\n"))

def run_student(program_path: Path, input_text: str):
    """Run student's script with given stdin; return (rc, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, str(program_path)],
        input=input_text,
        text=True,
        capture_output=True,
        timeout=TIMEOUT_SECONDS
    )
    out = result.stdout.replace("\r\n", "\n").strip()
    err = result.stderr.replace("\r\n", "\n").strip()
    return result.returncode, out, err

def main():
    here = Path(__file__).resolve().parent
    student_path = here / STUDENT_FILE

    if not student_path.exists():
        print(f"ERROR: Could not find {STUDENT_FILE} in this folder.")
        print("Fix: Rename your program file to p1.py (exactly).")
        return

    print(f"Running {len(TESTS)} tests against: {student_path.name}\n")

    passed = 0
    for t in TESTS:
        name = t["name"]
        try:
            rc, out, err = run_student(student_path, t["inp"])
        except subprocess.TimeoutExpired:
            print(f"[FAIL] {name}: program timed out (possible infinite loop)\n")
            continue

        if rc != 0:
            print(f"[FAIL] {name}: program crashed (exit code {rc})")
            if err:
                print("  STDERR:")
                print(indent(err))
            print()
            continue

        expected = t["expected"]
        if out == expected:
            print(f"[PASS] {name}\n")
            passed += 1
        else:
            print()
            print(f"[FAIL] {name}: output mismatch")
            print("  Expected:")
            print(indent(expected))
            print("  Got:")
            print(indent(out))
            print()

    print(f"Result: {passed}/{len(TESTS)} tests passed.")

if __name__ == "__main__":
    main()
