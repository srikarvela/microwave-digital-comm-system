import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
import os

plt.style.use("dark_background")
plt.rcParams["font.family"] = "SF Pro Display"
plt.rcParams["font.weight"] = "bold"

# Eb/N0 range in dB
eb_n0_db = np.linspace(-2, 12, 100)

# Convert Eb/N0 from dB to linear scale
eb_n0_linear = 10 ** (eb_n0_db / 10)

# Analytical BER expression for BPSK over AWGN
# BER = Q(sqrt(2 * Eb/N0)) = 0.5 * erfc(sqrt(Eb/N0))
ber = 0.5 * erfc(np.sqrt(eb_n0_linear))

# Plot BER vs Eb/N0
plt.figure(figsize=(7, 5))
plt.semilogy(
    eb_n0_db,
    ber,
    linewidth=2.8,
    color="#ff7a18",
    label="Analytical BPSK (AWGN)"
)
plt.grid(True, which="both", linestyle="--", linewidth=0.4, alpha=0.4)
plt.xlabel("Eb/N0 (dB)", fontsize=12, fontweight="bold")
plt.ylabel("Bit Error Rate (BER)", fontsize=12, fontweight="bold")
plt.title(
    "BPSK BER Performance over AWGN Channel",
    fontsize=14,
    fontweight="bold"
)
plt.legend()

# Ensure plots directory exists and build absolute save path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plots_dir = os.path.join(base_dir, "plots")
os.makedirs(plots_dir, exist_ok=True)

save_path = os.path.join(plots_dir, "snr_vs_ber.png")
plt.savefig(save_path, dpi=300)
plt.show()