import sys
import numpy as np
import matplotlib
import scipy
import control

print("=== Verificación del entorno ===")
print(f"Python: {sys.version}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"SciPy: {scipy.__version__}")
print(f"Control: {control.__version__}")
print("[OK] Entorno listo")