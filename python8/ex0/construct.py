import sys, os, site

if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You're still plugged in\n")
    pyv = sys.executable
    print(f"Current Python: {pyv}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")
else:
    print("MATRIX STATUS: Welcome to the construct:\n")
    pyv = sys.executable
    print(f"Current Python: {pyv}")
    vem = os.environ.get("VIRTUAL_ENV")
    venv_name = os.path.basename(vem)
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {vem}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    pack = site.getsitepackages()[0]
    print("Package installation path:")
    print(pack)
    