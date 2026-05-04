import subprocess
for cmd in ["python generate_dataset.py","python prepare.py","python solution.py","python grade.py --predictions predictions.csv"]:
    print(f"\n>> {cmd}"); subprocess.run(cmd, shell=True, check=True)
