import numpy as np
import matplotlib.pyplot as plt

# Define the DNA base pairs
base_pairs = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

# Your DNA sequence 
sequence = "GTGCGGAGGACCCGCAGTATAAGACAATCGTATGAGTCGAAGATTCTCCTAGGTATAGGACCGCTTTAGCTGGCGATGCTGTCTGAGTACTATGATAAGGAAGATGTTCCCCCACGCCTAATAGAGTTTCCTGCGGTTGCCTCTTCTGTTATAATGAAGAACACAACATCCGCAGCGTGCACATACGTCGGCACATTCTACTGTATTTTTGTGGATCGTTGCCACTGACAGGCCAACTTGGCAACTCTCTCCTGTC"

# Number of base pairs
n_bp = len(sequence)

# Parameters for the helix
n_turns = 2  # number of turns in the helix
points_per_turn = 50
radius = 1

# Generate helix coordinates
z = np.linspace(0, n_turns * 2 * np.pi , n_turns * 100)
x1 = radius * np.cos(z)
y1 = radius * np.sin(z)
x2 = radius * np.cos(z + np.pi)  # second strand is opposite
y2 = radius * np.sin(z + np.pi)

# Plotting the DNA double helix
fig, ax = plt.subplots()
ax.plot(x1, z, label='Strand 1', color='blue')
ax.plot(x2, z, label='Strand 2', color='red')

# Plot the base pair connections
for i in range(n_bp):
    index = int(i * len(z) / n_bp)
    ax.plot([x1[index], x2[index]], [z[index], z[index]], 'k--')

    # Annotate the base pairs
    ax.text(x1[index], z[index], sequence[i], fontsize=12, ha='right', color='blue')
    ax.text(x2[index], z[index], base_pairs[sequence[i]], fontsize=12, ha='left', color='red')

ax.set_title("Simplified DNA Helix")
ax.set_xlabel("X-axis (length in nm)")
ax.set_ylabel("Z-axis (height in nm)")

plt.legend()
plt.show()