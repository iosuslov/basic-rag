#!/usr/bin/env python3
"""Script to run linting and formatting checks."""

import argparse
import os
import subprocess
import sys
from typing import List, Tuple

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def run_command(command: List[str]) -> Tuple[int, str, str]:
    """Run a command and return its exit code, stdout and stderr."""
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr


def print_step(message: str) -> None:
    """Print a step message."""
    print(f"\n{'-' * 80}\n{message}\n{'-' * 80}")


def run_linting() -> int:
    """Run linting checks."""
    print_step("Running linting checks...")
    commands = [
        ["ruff", "format", "--check", "."],
        ["ruff", "check", "."],
        ["mypy", ".", "--ignore-missing-imports"],
    ]

    exit_code = 0
    for cmd in commands:
        print(f"\nRunning: {' '.join(cmd)}")
        ret_code, stdout, stderr = run_command(cmd)

        if ret_code == 0:
            print(f"{GREEN}✓ Passed{RESET}")
        else:
            print(f"{RED}✗ Failed{RESET}")
            print("Output:")
            if stdout:
                print(stdout)
            if stderr:
                print(stderr)
            exit_code = 1

    return exit_code


def run_tests() -> int:
    """Run pytest with coverage."""
    print_step("Running tests...")
    command = [
        "pytest",
        "-v",  # verbose output
        "--cov=app",  # measure coverage for app directory
        "--cov-report=term-missing",  # show lines that need test coverage
    ]

    # Add project root to PYTHONPATH
    env = dict(os.environ)
    env["PYTHONPATH"] = os.getcwd()

    print(f"\nRunning: {' '.join(command)}")
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
    )
    stdout, stderr = process.communicate()
    ret_code = process.returncode

    if ret_code == 0:
        print(f"{GREEN}✓ All tests passed{RESET}")
    else:
        print(f"{RED}✗ Some tests failed{RESET}")
        print("Output:")
        if stdout:
            print(stdout)
        if stderr:
            print(stderr)

    return ret_code


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run code quality checks and tests.")
    parser.add_argument(
        "--lint-only",
        action="store_true",
        help="Run only linting checks",
    )
    parser.add_argument(
        "--test-only",
        action="store_true",
        help="Run only tests",
    )
    return parser.parse_args()


def main() -> int:
    """Run all checks."""
    args = parse_args()
    exit_code = 0

    # Run selected checks based on arguments
    if args.lint_only:
        exit_code = run_linting()
    elif args.test_only:
        exit_code = run_tests()
    else:
        # Run all checks
        lint_code = run_linting()
        test_code = run_tests()
        exit_code = lint_code or test_code

    if exit_code == 0:
        print(f"\n{GREEN}All checks passed!{RESET}")
    else:
        print(f"\n{RED}Some checks failed!{RESET}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
