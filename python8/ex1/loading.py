import sys
import os
import importlib.util
import importlib.metadata

def main() -> None:
    PACKAGES = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        }

    missing = []
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for package, description in PACKAGES.items():
        if importlib.util.find_spec(package) is None:
            print(f"[MISSING] {package}")
            missing.append(package)
        else:
            version = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {description}")

    if missing:
        print("\nMissing dependencies detected.\n")

        print("Install with pip:")
        print("pip install -r requirements.txt")

        print("\nInstall with Poetry:")
        print("poetry install")
        sys.exit(1)

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...\n")
    data = np.random.randn(1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame(data, columns=["matrix_signal"])
    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(df["matrix_signal"])
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    if os.path.exists("poetry.lock") and os.path.exists("pyproject"):
        print("Install with poetry!")
    else:
        print("Install with pip!")

if __name__ == '__main__':
    main()