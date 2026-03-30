# Geometry LLM Evaluation: Representation Invariance Benchmark

This project benchmarks whether Large Language Models (LLMs) can solve the same geometry problem when it is presented in three different mathematical representations:

- **Coordinate (coord):** Problems stated using (x,y) coordinates and algebraic equations.
- **Euclidean (euclid):** Problems stated using classical geometry (lengths, angles, properties).
- **Vector (vector):** Problems stated using vector notation and operations (dot products, magnitudes, etc.).

The dataset contains 160 hand-crafted geometry problems across four categories (length, area, angle, ratio), each written in all three representations. Every model is evaluated on all 480 prompts (160 problems x 3 representations). The core research question: if a model truly understands geometry, it should produce the same correct answer regardless of how the problem is phrased.

---

## Table of Contents

1. [Setup](#1-setup)
2. [Prepare the Dataset](#2-prepare-the-dataset)
3. [Run Model Inference](#3-run-model-inference)
4. [Parse and Score Outputs](#4-parse-and-score-outputs)
5. [Run Analysis Scripts](#5-run-analysis-scripts)
6. [Project Structure](#6-project-structure)

---

## 1. Setup

**Prerequisites:** Python 3.9+ and pip.

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate          # Windows

pip install -r requirements.txt
```

Set your OpenRouter API key as an environment variable (required for model inference):

```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

---

## 2. Prepare the Dataset

### 2a. Create the problem definitions file

Create a Python file at `dataset_specs/dataset.py` containing a list called `PROBLEMS`. Each entry is a dictionary with the following keys:

```python
PROBLEMS = [
    {
        "id": "length_hard_01",
        "category": "length",
        "coord": "Triangle ABC has vertices A(0,0), B(5,0), and C(3,4). Find the length of the internal angle bisector of angle A, terminating at side BC.",
        "euclid": "In Triangle ABC, the side lengths are AB = 5, AC = 5, and BC = 2*sqrt(5). Find the length of the internal angle bisector drawn from vertex A to side BC.",
        "vector": "Let vectors u = (5,0) and v = (3,4). Find the length of the segment along the angle bisector of u and v, extending from the origin to the line segment connecting the endpoints of u and v.",
        "answer": "3.162"
    },
    # ... add more problems following the same format
]
```

Required fields for every problem:
- `id`: Unique identifier (e.g., `"area_hard_05"`).
- `category`: One of `length`, `area`, `angle`, or `ratio`.
- `coord`: The coordinate-geometry version of the problem.
- `euclid`: The Euclidean-geometry version of the same problem.
- `vector`: The vector-geometry version of the same problem.
- `answer`: The gold-standard numeric answer as a string (e.g., `"3.162"`).

The repository includes `dataset_specs/dataset.py` with 160 problems already defined.

### 2b. Generate the dataset files

Run the generation script from the project root:

```bash
python -m scripts.generate_dataset
```

This reads `dataset_specs/dataset.py` and writes individual `.txt` files into `problems/exp1/<category>/`, producing four files per problem:
- `<id>_coord.txt`
- `<id>_euclid.txt`
- `<id>_vector.txt`
- `<id>_answer.txt`

---

## 3. Run Model Inference

All models are queried through the [OpenRouter API](https://openrouter.ai/). Before running either script, open it and set the `MODEL` variable to a valid OpenRouter model identifier (e.g., `"google/gemini-2.5-flash"`). The variable is located near the top of each file and is set to a placeholder by default.

There are two prompt strategies:

### Prompt 1: Direct numeric answer

The model is asked to output only a final numeric answer with no reasoning. This tests raw problem-solving ability.

1. Open `scripts/run_models_prompt1.py` and set `MODEL = "<your_model_name>"` (e.g., `"google/gemini-2.5-flash"`).
2. Run:

```bash
python -m scripts.run_models_prompt1
```

### Prompt 2: Euclidean conversion + reasoning

The model is asked to (1) convert the problem into a pure Euclidean format, (2) show its reasoning, and (3) output a structured JSON with `euclidean_conversion`, `reasoning`, and `numeric_answer`. This tests whether explicit representation translation improves invariance.

1. Open `scripts/run_model_prompt2.py` and set `MODEL = "<your_model_name>"`.
2. Run:

```bash
python -m scripts.run_model_prompt2
```

Both scripts iterate over all problems and representations, saving raw model outputs to `runs/raw_outputs/<model_name>/`.

To evaluate multiple models, update the `MODEL` variable and re-run the script for each model.

---

## 4. Parse and Score Outputs

After inference is complete, extract numeric predictions from the raw outputs and then score them against the gold answers.

### 4a. Parse outputs

```bash
python -m scripts.parse_outputs --model <model_name>
```

This reads raw text files from `runs/raw_outputs/<model_name>/`, extracts the numeric answer (via JSON parsing with regex fallback), and writes parsed results to `runs/parsed_answers/<model_name>/`.

### 4b. Score predictions

```bash
python -m scripts.score_exp1 --model <model_name>
```

This matches each parsed prediction against the gold answer from `problems/exp1/<category>/<id>_answer.txt` and produces a CSV at `runs/scores/exp1_<model_name>.csv` with columns: `problem`, `category`, `representation`, `predicted`, `gold`, `correct`.

**Important:** The `correct` column is left empty by default and must be filled in (manually or programmatically) with `1` or `0` before running the analysis scripts. The analysis scripts read scored CSVs from `runs/scores_rep_to_euclid/`. Copy or move your finalized score files into that directory before proceeding.

---

## 5. Run Analysis Scripts

Once all models have been scored and the CSVs are in `runs/scores_rep_to_euclid/`, run the following analysis scripts in order. All scripts are run from the project root directory.

### Step 1: Tabulation (summary tables)

```bash
python -m scripts.tabulation
python -m scripts.tabulation1
python -m scripts.tabulation2
```

- `tabulation.py` computes per-model accuracy by representation, accuracy gap, Invariance@3, and Consistency@3. Outputs `runs/analysis/geometry_invariance_summary.csv`.
- `tabulation1.py` adds bootstrap 95% confidence intervals and McNemar exact tests. Outputs `runs/analysis/geometry_invariance_summary_with_CIs.csv`.
- `tabulation2.py` adds statsmodels McNemar variant. Outputs `runs/analysis/geometry_invariance_summary_with_CIs_and_mcnemar.csv`.

### Step 2: Invariance and consistency breakdown

```bash
python -m scripts.invariance_analysis
```

Computes Invariance@3 and Consistency@3 per model and per category. Outputs `runs/analysis/invariance_consistency_summary.csv` and `runs/analysis/invariance_by_category.csv`.

### Step 3: Inconsistency audit

```bash
python -m scripts.analyze_inconsistency
```

Prints a per-model summary of how many problems are correct on all representations, wrong on all, or inconsistent across representations.

### Step 4: Representation flip analysis

```bash
python -m scripts.representation_flip_analysis
```

Analyzes item-level correctness patterns (CCC, CCW, CWC, WCC, CWW, WCW, WWC, WWW) across the three representations. Computes pairwise coherence and transfer rates. Outputs CSVs and figures to `runs/analysis/`.

### Step 5: Surface complexity regression

```bash
python -m scripts.surface_complexity_regression
```

Extracts surface-level features from problem text (token count, symbol count, number of coordinates, etc.) and runs logistic regression to test whether surface complexity predicts model failures. Outputs regression tables, marginal effects, and diagnostic plots to `runs/analysis/`.

### Step 6: Visualization

```bash
python -m scripts.plot_results
```

Generates line plots and bar charts comparing accuracy across representations for all models. Outputs figures to `runs/analysis/figures/`.

---

## 6. Project Structure

```
geometry_llm_eval/
|
|-- dataset_specs/              # Problem definitions
|   |-- dataset.py              # PROBLEMS list (160 problems)
|
|-- problems/exp1/              # Generated .txt files (one per problem x representation)
|   |-- length/
|   |-- area/
|   |-- angle/
|   |-- ratio/
|
|-- scripts/                    # All runnable scripts
|   |-- generate_dataset.py     # Step 2: write problem .txt files
|   |-- run_models_prompt1.py   # Step 3: inference (direct answer prompt)
|   |-- run_model_prompt2.py    # Step 3: inference (Euclidean conversion prompt)
|   |-- parse_outputs.py        # Step 4a: extract numeric predictions
|   |-- score_exp1.py           # Step 4b: score against gold answers
|   |-- tabulation.py           # Step 5.1: summary table
|   |-- tabulation1.py          # Step 5.1: summary + bootstrap CIs + McNemar
|   |-- tabulation2.py          # Step 5.1: summary + statsmodels McNemar
|   |-- invariance_analysis.py  # Step 5.2: invariance/consistency metrics
|   |-- analyze_inconsistency.py# Step 5.3: inconsistency audit
|   |-- representation_flip_analysis.py  # Step 5.4: flip patterns
|   |-- surface_complexity_regression.py # Step 5.5: logistic regression
|   |-- plot_results.py         # Step 5.6: figures
|
|-- runs/                       # All outputs
|   |-- raw_outputs/            # Raw LLM responses
|   |-- parsed_answers/         # Extracted numeric predictions
|   |-- scores_rep_to_euclid/   # Scored CSVs (input for analysis)
|   |-- analysis/               # Analysis outputs (CSVs, plots, regression tables)
|       |-- figures/
|
|-- requirements.txt
|-- README.md
```

---

## Key Metrics

- **Invariance@3:** Fraction of problems where the model is correct on all three representations.
- **Consistency@3:** Fraction of problems where the model gives the same predicted answer on all three representations (regardless of correctness).
- **Accuracy Gap:** Difference between the highest and lowest accuracy across the three representations for a given model.
- **Flip Patterns:** 8 correctness patterns (CCC through WWW) in Euclid-Coord-Vector order, where C = correct and W = wrong.
