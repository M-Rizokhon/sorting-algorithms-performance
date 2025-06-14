# sorting-algorithms-performance
# 🧪 Sorting Algorithm Benchmarking

This project benchmarks the performance of six popular sorting algorithms on datasets of varying sizes and types. It compares run times for:
- **Bubble Sort**
- **Selection Sort**
- **Insertion Sort**
- **Merge Sort**
- **Tim Sort**
- **Quick Sort**

The results are visualized using `matplotlib`, and the datasets are tested in three different orderings:
- Random (unsorted)
- Sorted (ascending)
- Reversely sorted (descending)

## 📋 Features
- Custom implementation of six sorting algorithms
- Automatically generates datasets of various sizes
- Benchmarks sorting performance on:
  - 9 different sizes (from 10 to 2000)
  - 3 data orderings (unsorted, sorted, reversed)
- Visual comparison of run time per algorithm
- Clean plotting with legends and axis labeling

## 📊 Dataset Sizes
List lengths tested:  
`[10, 50, 100, 500, 1000, 1500, 1700, 1800, 2000]`

Each list is tested in all 3 ordering cases, so 27 total test cases per algorithm.

## 🧠 Sorting Implementations
Sorting algorithms are implemented manually inside a Python class, with:
- Efficient recursive handling for merge and quick sort
- In-place sorting where possible
- A working version of Tim Sort mimicking the real one with insertion sort + merge

## 📈 Visualization
Results are plotted for:
- Sorting of unsorted lists
- Sorting of already sorted lists
- Sorting of reversely sorted lists

Each graph shows how each algorithm scales with increasing input size.

### Example Plot
> Plots are generated using `matplotlib`, displaying time (in seconds) vs. list size.

## 🧪 How to Run

1. Make sure Python 3 is installed.
2. Install the required library:

```bash
pip install matplotlib

