import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ANALYSIS_DIR = Path("runs/analysis")
FIG_DIR = ANALYSIS_DIR / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ===============================
# Load geometry robustness summary
# ===============================
geo = pd.read_csv(ANALYSIS_DIR / "geometry_invariance_summary.csv")

# ===============================
# Plot 1: Geometry Sensitivity Line Plot
# ===============================
plt.figure(figsize=(12, 6))
x = range(len(geo))

plt.plot(x, geo["coord"], marker="o", label="Coord")
plt.plot(x, geo["euclid"], marker="o", label="Euclid")
plt.plot(x, geo["vector"], marker="o", label="Vector")

plt.xticks(x, geo["model"], rotation=30, ha="right")
plt.ylabel("Accuracy")
plt.title("Geometry Sensitivity Across Models")
plt.legend()
plt.tight_layout()

plt.savefig(FIG_DIR / "geometry_sensitivity.png", dpi=300)
plt.close()

# ===============================
# Plot 2: Bar Plot (Coord vs Euclid vs Vector)
# ===============================
geo_plot = geo.set_index("model")[["coord", "euclid", "vector"]]

geo_plot.plot(kind="bar", figsize=(12, 6))
plt.ylabel("Accuracy")
plt.title("Accuracy by Geometry Representation per Model")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Representation")
plt.tight_layout()

plt.savefig(FIG_DIR / "accuracy_by_representation.png", dpi=300)
plt.close()

print(f"[DONE] Figures saved to {FIG_DIR}")
