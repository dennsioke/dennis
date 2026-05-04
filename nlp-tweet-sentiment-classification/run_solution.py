"""
run_solution.py

Runs the full pipeline: generate dataset, prepare splits, train model, grade results.
"""

import subprocess
import sys


def run(cmd):
    print(f"\n>> {cmd}")
    result = subprocess.run(cmd, shell=True, check=True)
    return result


if __name__ == "__main__":
    run("python generate_dataset.py")
    run("python prepare.py")
    run("python solution.py")
    run("python grade.py --predictions predictions.csv")
