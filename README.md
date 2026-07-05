# 🧬 Genome Mutation Tracker

## 📖 Overview

Genome Mutation Tracker is a beginner bioinformatics project developed using Python. It compares the genome sequence of the original Wuhan SARS-CoV-2 virus with a variant genome, identifies nucleotide differences (mutations), counts them, generates a mutation report, and visualizes mutation distribution using a graph.

This project was created as a learning project to understand genome comparison and mutation analysis using real FASTA files.

---

## ✨ Features

- Read genome sequences from FASTA files
- Compare two genome sequences nucleotide by nucleotide
- Detect mutation positions
- Count total mutations
- Generate a mutation report (`mutation_report.txt`)
- Visualize mutation distribution using Matplotlib

---

## 🛠 Technologies Used

- Python 3
- Biopython
- Matplotlib

---

## 📂 Project Structure

```
Genome_Mutation_Tracker/
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
└── README.md
```

---

## ▶️ How to Run

1. Install the required libraries:

```bash
pip install biopython matplotlib
```

2. Place the genome files inside the `data` folder:

- Wuhan.fasta
- datavariant.fasta

3. Run the program:

```bash
python src/main.py
```

---

## 📊 Output

The program will:

- Display genome lengths
- Detect mutation positions
- Count total mutations
- Save the mutation report
- Display a mutation distribution graph

---

## ⚠️ Current Limitation

This project performs a direct position-by-position comparison of genome sequences. It does not perform sequence alignment, so genomes of different lengths may require alignment for biologically accurate comparison.

---

## 🚀 Future Improvements

- Add sequence alignment
- Compare multiple genome variants
- Export mutation data as CSV
- Improve mutation visualizations
- Build a simple graphical user interface (GUI)

---

## 👨‍💻 Author

**Jegan Udhaya**

B.Tech Biotechnology Student

Learning Bioinformatics, Python, and Computational Biology