# 🧬 Viral Genome Mutation Tracker

## 📖 Overview
**Viral Genome Mutation Tracker** is a beginner-friendly bioinformatics project developed using **Python** and **Biopython**. It compares the genome sequence of the original Wuhan SARS-CoV-2 reference genome with a variant genome, identifies nucleotide differences (mutations), counts them, classifies mutation types, generates a mutation report, and visualizes mutation distribution using a bar chart.

This project was created as a learning project to understand genome comparison, mutation analysis, and basic computational biology using real FASTA genome sequences.

---

## ✨ Features

- ✅ Read genome sequences from FASTA files
- ✅ Compare two genome sequences nucleotide by nucleotide
- ✅ Detect SNP (Single Nucleotide Polymorphism) positions
- ✅ Count total mutations
- ✅ Classify mutations as **Transitions** and **Transversions**
- ✅ Calculate the **Ts/Tv (Transition/Transversion) Ratio**
- ✅ Detect genome length differences (deletions)
- ✅ Generate a mutation report
- ✅ Visualize mutation distribution using a **bar chart**

---

## 📊 Results

### Genome Length Comparison

| Genome | Length (bp) |
|---------|------------:|
| Wuhan Reference | 29,903 |
| Variant Genome | 29,740 |

### Mutation Summary

| Metric | Value |
|---------|------:|
| **Total SNP Mutations** | 21,338 |
| **Transitions (A↔G, C↔T)** | 6,896 |
| **Transversions (A↔C, A↔T, G↔C, G↔T)** | 14,442 |
| **Ts/Tv Ratio** | 0.48 |
| **Deletions in Variant** | 163 bp |

---

## 📈 Mutation Density Graph

![Mutation Density Graph](mutation_graph.png)

*Figure: Distribution of SNP mutations across the SARS-CoV-2 genome using 1000 bp bins.*

---

## 🔬 Sample Mutations (First 20)

```text
Position 2 : T → G
Position 3 : T → A
Position 4 : A → T
Position 5 : A → C
Position 6 : A → T
Position 8 : G → T
Position 10: T → C
...
```

---

## 🛠 Technologies Used

- Python 3.13
- Biopython
- Matplotlib
- Git
- GitHub

---

## 📂 Project Structure

```text
viral_genome_mutation_tracker/
│
├── data/
│   ├── Wuhan.fasta
│   └── datavariant.fasta
│
├── src/
│   └── main.py
│
├── results/
│   └── mutation_report.txt
│
├── mutation_graph.png
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/viral_genome_mutation_tracker.git
```

### 2️⃣ Install Dependencies

```bash
pip install biopython matplotlib
```

### 3️⃣ Add Genome Files

Place the following files inside the **data/** folder:

- Wuhan.fasta
- datavariant.fasta

### 4️⃣ Run the Program

```bash
python src/main.py
```

---

## 📊 Sample Output

```text
=== GENOME LENGTH INFO ===
Wuhan length : 29903
Variant length: 29740

=== MUTATION SUMMARY ===

Total SNP mutations: 21338

Transitions (A↔G, C↔T): 6896
Transversions (A↔C, A↔T, G↔C, G↔T): 14442

Ts/Tv Ratio: 0.48

Note:
Wuhan genome contains 163 additional bases
(compared with the variant genome).

First 20 mutations:

Position 2 : T → G
Position 3 : T → A
Position 4 : A → T
...
```

---

## ⚠️ Current Limitation

This project performs a **direct position-by-position genome comparison** without sequence alignment.

When genomes have different lengths, the mutation counts may be biologically inaccurate because insertions and deletions are not aligned before comparison.

---

## 🚀 Future Improvements

- Add pairwise sequence alignment
- Compare multiple genome variants
- Export mutation results as CSV or Excel
- Improve mutation visualization with interactive plots
- Build a graphical user interface (GUI)
- Annotate mutations by gene and genomic region
- Support protein-level mutation analysis

---

## 👨‍💻 Author

**Jegan Udhaya**

B.Tech Biotechnology Student

Learning Bioinformatics • Python • Computational Biology

GitHub: https://github.com/your-username

---

## 📜 License

This project is intended for **educational and learning purposes**.

---

## 🙏 Acknowledgments

- NCBI for providing SARS-CoV-2 reference genome data
- Biopython Community
- Python Community
- My Professors and Mentors

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!