# 🧬 SARS-CoV-2 Genome Mutation Tracker

A Python-based bioinformatics tool for comparing the Wuhan reference genome with SARS-CoV-2 variant genomes using **position-by-position alignment**.

---

## 📊 Key Results

| Metric | Value |
|---------|-------|
| Wuhan Genome Length | **29,903 bp** |
| Variant Genome Length | **29,740 bp** |
| Total SNPs Identified | **21,338** |
| Transitions | **6,896** |
| Transversions | **14,442** |
| Ts/Tv Ratio | **0.48** |
| Deletions in Variant | **163 bp** |

---

## 📈 Mutation Density Graph

![Mutation Density Graph](mutation_graph.png)

---

## 🧪 Methodology

1. Load Wuhan and variant genomes from FASTA files.
2. Perform position-by-position sequence comparison.
3. Detect SNPs between the genomes.
4. Classify mutations into **Transitions** and **Transversions**.
5. Identify insertions/deletions based on sequence length.
6. Generate text and CSV reports.
7. Visualize mutation density using a lollipop graph.

### First 20 Mutations

```
Position 2 : T → G
Position 3 : T → A
Position 4 : A → T
Position 5 : A → C
Position 6 : A → T
Position 8 : G → T
Position 10: T → C
Position 12: A → C
Position 15: C → A
Position 16: C → A
Position 17: T → C
Position 18: T → G
Position 19: C → A
Position 20: C → A
Position 22: A → T
Position 23: G → T
Position 24: G → T
Position 25: T → A
Position 28: C → A
Position 29: A → T
```

---

## 📂 Project Structure

```text
viral_genome_mutation_tracker/
│
├── main.py
├── mutation_graph.png
├── README.md
│
├── data/
│   ├── Wuhan.fasta
│   └── datavariant.fasta
│
└── results/
    ├── mutation_report.txt
    └── mutation_report.csv
```

---

## 🚀 How to Run

```bash
# Install dependencies
pip install biopython matplotlib

# Run the analysis
python main.py
```

---

## 📤 Output Files

| File | Description |
|------|-------------|
| mutation_report.txt | Summary statistics and first 20 mutations |
| mutation_report.csv | Complete SNP mutation list |
| mutation_graph.png | Mutation density visualization |

---

## 🛠️ Technologies Used

- Python 3.13
- Biopython
- Matplotlib

---

## 👨‍🔬 Author

**Jegan Udhaya**  
1st Year B.Tech Biotechnology Student

**GitHub:**  
https://github.com/jeganudhaya2007-ops

---

## 📝 License

This project is intended for educational and learning purposes only.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

Thank you for visiting this repository.