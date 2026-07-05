from Bio import SeqIO
import os
import matplotlib.pyplot as plt
# ==============================
# 1. FILE PATHS (CORRECTED)
# ==============================
wuhan_path = "data/Wuhan.fasta"
variant_path = "data/datavariant.fasta"  # FIXED SPELLING

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

for i in range(limit):
    if wuhan[i] != variant[i]:
        mutations.append((i + 1, wuhan[i], variant[i]))
        snp_count += 1

# ==============================
# 6. OUTPUT SUMMARY
# ==============================
print("\n=== MUTATION SUMMARY ===")
print("Total SNP mutations:", snp_count)

print("\nFirst 20 mutations:")
for m in mutations[:20]:
    print(f"Position {m[0]}: {m[1]} → {m[2]}")

# ==============================
# 7. SAVE RESULTS
# ==============================
os.makedirs("results", exist_ok=True)

output_file = "results/mutation_report.txt"

with open(output_file, "w") as f:
    f.write("=== MUTATION REPORT ===\n\n")
    f.write(f"Wuhan length   : {len(wuhan)}\n")
    f.write(f"Variant length : {len(variant)}\n")
    f.write(f"Total SNPs     : {snp_count}\n\n")

    f.write("Mutations:\n")
    f.write("----------------------\n")

    for m in mutations:
        f.write(f"Position {m[0]}: {m[1]} -> {m[2]}\n")

print("\n Report saved to:", output_file)
print(" Mutation analysis completed successfully!")



import matplotlib.pyplot as plt

# Get mutation positions
x = [m[0] for m in mutations]

# Create bins of 1000 bases
bins = range(0, max(x) + 1000, 1000)
counts = [0] * (len(bins) - 1)

# Count mutations in each bin
for pos in x:
    for i in range(len(bins) - 1):
        if bins[i] <= pos < bins[i + 1]:
            counts[i] += 1
            break

plt.figure(figsize=(12, 4))
plt.bar(range(len(counts)), counts)

plt.title("Mutation Density Across Genome")
plt.xlabel("Genome Region (1000 bp bins)")
plt.ylabel("Number of Mutations")


plt.show()



"""
Genome Mutation Tracker
Author: Jegan Udhaya
Language: Python
Libraries: Biopython, Matplotlib

Description:
Compares the Wuhan SARS-CoV-2 genome with a variant genome,
detects nucleotide differences, and generates a mutation report.
"""