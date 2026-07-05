from Bio import SeqIO
import os
import matplotlib.pyplot as plt
from collections import Counter

# ==============================
# 1. FILE PATHS
# ==============================
wuhan_path = "data/Wuhan.fasta"
variant_path = "data/datavariant.fasta"

# ==============================
# 2. CHECK FILES EXIST
# ==============================
if not os.path.exists(wuhan_path):
    print("Wuhan file not found:", wuhan_path)
    exit()

if not os.path.exists(variant_path):
    print("Variant file not found:", variant_path)
    exit()

# ==============================
# 3. LOAD SEQUENCES
# ==============================
wuhan = str(SeqIO.read(wuhan_path, "fasta").seq)
variant = str(SeqIO.read(variant_path, "fasta").seq)

# ==============================
# 4. BASIC INFO
# ==============================
print("\n=== GENOME LENGTH INFO ===")
print("Wuhan length   :", len(wuhan))
print("Variant length :", len(variant))

# ==============================
# 5. MUTATION DETECTION
# ==============================
limit = min(len(wuhan), len(variant))

mutations = []
snp_count = 0
transitions = 0
transversions = 0

for i in range(limit):
    # Skip if either base is 'N' (unknown)
    if wuhan[i] == 'N' or variant[i] == 'N':
        continue
        
    if wuhan[i] != variant[i]:
        mutations.append((i + 1, wuhan[i], variant[i]))
        snp_count += 1
        
        # Check for Transition (A<->G or C<->T) vs Transversion
        if (wuhan[i] == 'A' and variant[i] == 'G') or (wuhan[i] == 'G' and variant[i] == 'A') or \
           (wuhan[i] == 'C' and variant[i] == 'T') or (wuhan[i] == 'T' and variant[i] == 'C'):
            transitions += 1
        else:
            transversions += 1

# ==============================
# 5b. INDEL DETECTION (Insertions/Deletions)
# ==============================
insertions = 0
deletions = 0

if len(variant) > len(wuhan):
    insertions = len(variant) - len(wuhan)
elif len(wuhan) > len(variant):
    deletions = len(wuhan) - len(variant)

# ==============================
# 6. OUTPUT SUMMARY
# ==============================
print("\n=== MUTATION SUMMARY ===")
print(f"Total SNP mutations: {snp_count}")
print(f"Transitions (A↔G, C↔T): {transitions}")
print(f"Transversions (A↔C, A↔T, G↔C, G↔T): {transversions}")
if transitions + transversions > 0:
    print(f"Ts/Tv Ratio: {transitions / (transversions or 1):.2f}")

# Handle length differences
if deletions > 0:
    print(f"Note: Wuhan has {deletions} extra bases (Deletions in Variant).")
elif insertions > 0:
    print(f"Note: Variant has {insertions} extra bases (Insertions in Variant).")

print("\nFirst 20 mutations:")
for m in mutations[:20]:
    print(f"Position {m[0]}: {m[1]} → {m[2]}")

# ==============================
# 7. SAVE RESULTS (TEXT & CSV)
# ==============================
os.makedirs("results", exist_ok=True)

# 7a. Save Text Report
output_file = "results/mutation_report.txt"
with open(output_file, "w") as f:
    f.write("=== MUTATION REPORT ===\n\n")
    f.write(f"Wuhan length   : {len(wuhan)}\n")
    f.write(f"Variant length : {len(variant)}\n")
    f.write(f"Total SNPs     : {snp_count}\n")
    f.write(f"Transitions    : {transitions}\n")
    f.write(f"Transversions  : {transversions}\n")
    f.write(f"Insertions     : {insertions}\n")
    f.write(f"Deletions      : {deletions}\n\n")

    f.write("First 20 Mutations (Full list too large for text file):\n")
    f.write("----------------------\n")
    for m in mutations[:20]:
        f.write(f"Position {m[0]}: {m[1]} -> {m[2]}\n")

print(f"\n Text report saved to: {output_file}")

# 7b. Save CSV Report (Excel-friendly)
csv_file = "results/mutation_report.csv"
with open(csv_file, "w") as f:
    f.write("Position,Reference,Variant\n")
    for m in mutations:
        f.write(f"{m[0]},{m[1]},{m[2]}\n")

print(f" CSV report saved to: {csv_file}")

# ==============================
# 8. VISUALIZATION (LOLLIPOP GRAPH)
# ==============================
if snp_count > 0:
    # Get mutation positions
    x = [m[0] for m in mutations]
    
    # Use Counter to efficiently group into bins of 1000
    bin_size = 1000
    binned_counts = Counter((pos - 1) // bin_size for pos in x)
    
    # Sort the bins for the x-axis
    sorted_bins = sorted(binned_counts.keys())
    counts = [binned_counts[b] for b in sorted_bins]

    plt.figure(figsize=(12, 5))
    plt.stem(sorted_bins, counts, basefmt=" ")  # Lollipop style
    
    plt.title(f"Mutation Density Across Genome (Total: {snp_count} SNPs)")
    plt.xlabel(f"Genome Region ({bin_size} bp bins)")
    plt.ylabel("Number of Mutations")
    plt.grid(True, alpha=0.3)  # Light grid for readability
    
    print("\n Displaying graph... (Close the graph window to end program)")
    plt.savefig("mutation_graph.png", dpi=300, bbox_inches='tight')
    plt.show()
else:
    print("\n No mutations found, so no graph was generated.")

print(" Mutation analysis completed successfully!")



"""
Genome Mutation Tracker
Author: Jegan Udhaya
Language: Python
Libraries: Biopython, Matplotlib

Description:
Compares the Wuhan SARS-CoV-2 genome with a variant genome,
detects nucleotide differences, and generates a mutation report.
"""