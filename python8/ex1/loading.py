import importlib.util
import importlib.metadata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pack = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready"
}

ok = True

for ve, msg in pack.items():
    spec = importlib.util.find_spec(ve)
    if spec is None:
        print(f"[ERROR] {ve} - not intalled")
        ok = False
    else:
        ver = importlib.metadata.version(ve)
        print(f"[OK] ({ver}) - {msg}")

if not ok:
    print("\nInstall with pip:")
    print("pip install -r requirements.txt")
    print("\nInstall with Poetry:")
    print("poetry install")
else:
    print("Analyzing Matrix data...")
    ints = np.random.randn(1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame(ints)
    plt.plot(df)
    print("Generating visualization...")
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")