# CO1 Assignment – Design, Analysis and Validation of an Efficient Search Strategy for a Large-Scale Student Record System

**Course:** CSA06 Design and Analysis of Algorithms (Dept. of CSE) | **Faculty:** Dr. F. Mary Harin Fernandez | **Student:** Raksha
**Course Outcome:** CO1 – determine algorithm efficiency using asymptotic notations and mathematical techniques (Master Theorem, substitution).

## Project summary
A university database holds 10³ – 10⁶+ student records identified by unique registration numbers. Three algorithms from different design paradigms are designed, analysed mathematically (operation counts, best/average/worst case, asymptotics, recurrences), implemented and benchmarked at n = 1,000 / 10,000 / 100,000 / 1,000,000, and a design is recommended. The Day-4 Design Challenge (50,000 searches/hour, 10⁶ records, daily updates) re-evaluates and modifies the design.

| # | Algorithm | Paradigm | Preprocessing | Avg. search | Measured avg. search at n = 10⁶ |
|---|---|---|---|---|---|
| 1 | Linear search (iterative) | Brute force | none | Θ(n) | 25,864 µs (483,964 comparisons) |
| 2 | Binary search (recursive) | Decrease-and-conquer | sort, Θ(n log n) | Θ(log n) | 4.76 µs (18.9 comparisons) |
| 3 | Hash table, chaining | Transform-and-conquer | build, Θ(n) | Θ(1) expected | 0.91 µs (1.4 comparisons) |

**Task 11 recommendation:** sorted array + binary search (general case). **Task 12 decision:** MODIFY – sorted master + nightly-rebuilt hash index (details in `Task_12_Design_Challenge/`).

## How to run
Requirements: Python 3.9+; `matplotlib` and `pygments`/`Pillow` only for graphs/screenshots (`pip install matplotlib pillow pygments`).
```bash
cd Task_8_Implementation_Testing/Source_Code
python3 test_correctness.py        # correctness tests  -> must print ALL TESTS PASSED
python3 benchmark.py               # experiments        -> ../results.csv (about 1 minute)
python3 ../../Task_9_Experimental_Performance/make_graphs.py   # tables + graphs -> Report/Tables_and_Graphs/
```
Timings depend on the machine; operation counts are machine-independent and reproducible (fixed random seeds).

## Repository structure
```
CO1_Assignment
├── Task_1_Algorithm_Design/            README.md  – three approaches, pseudocode, preprocessing, justification
├── Task_2_Basic_Operation/             README.md
├── Task_3_Mathematical_Complexity/     README.md  – derivations incl. preprocessing and combined cost
├── Task_4_Case_Analysis/               README.md  – best / average / worst case
├── Task_5_Asymptotic_Analysis/         README.md
├── Task_6_Recurrence_Formulation/      README.md
├── Task_7_Recurrence_Solution/         README.md  – substitution, Master Theorem, induction
├── Task_8_Implementation_Testing/      README.md, results.csv, test/benchmark logs
│   └── Source_Code/                    algorithms.py, test_correctness.py, benchmark.py
├── Task_9_Experimental_Performance/    README.md, results.csv, results_tables.md, make_graphs.py
├── Task_10_Theory_vs_Experiment/       README.md
├── Task_11_Final_Recommendation/       README.md
├── Task_12_Design_Challenge/           README.md  – impact, evaluation, adaptation, defence
├── Report/
│   ├── Source_Code_Screenshots/        rendered images of the source files
│   ├── Output_Screenshots/             rendered images of test / benchmark output
│   ├── Analysis/                       combined analysis (Tasks 2–7, 10–12)
│   ├── Tables_and_Graphs/              PNG graphs + results_tables.md
│   └── Documentation/                  Full_Report.md (all tasks in one document)
└── README.md
```

## Marks map
| Task | Marks | Location |
|---|---|---|
| 1 Algorithm design | 5 | Task_1_Algorithm_Design |
| 2 Basic operation | 2 | Task_2_Basic_Operation |
| 3 Mathematical complexity | 6 | Task_3_Mathematical_Complexity |
| 4 Best/avg/worst | 4 | Task_4_Case_Analysis |
| 5 Asymptotic analysis | 3 | Task_5_Asymptotic_Analysis |
| 6 Recurrence formulation | 3 | Task_6_Recurrence_Formulation |
| 7 Recurrence solution | 4 | Task_7_Recurrence_Solution |
| 8 Implementation & testing | 4 | Task_8_Implementation_Testing |
| 9 Experimental performance | 3 | Task_9_Experimental_Performance |
| 10 Theory vs experiment | 4 | Task_10_Theory_vs_Experiment |
| 11 Final recommendation | 4 | Task_11_Final_Recommendation |
| 12 Design challenge | 8 | Task_12_Design_Challenge |
