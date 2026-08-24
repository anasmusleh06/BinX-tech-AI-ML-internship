# Cardiac Patient Monitoring System

## AI & Machine Learning Individual Final Project

This project is an end-to-end machine-learning analysis of the Kaggle **Cardiovascular Disease** dataset. It is designed to demonstrate the skills covered in the AI & Machine Learning training track: Python, NumPy, Pandas, statistics, exploratory data analysis, supervised learning, model evaluation, feature engineering, Scikit-learn Pipelines, clustering, and PCA.

> **Educational scope:** This project is an ML analysis exercise. It is not a clinical diagnostic system and does not provide treatment, emergency, or medical recommendations.

## Project Objectives

- Prepare and validate a public cardiovascular dataset.
- Perform descriptive statistics and exploratory data analysis.
- Define a binary supervised-learning classification problem.
- Establish a Logistic Regression baseline.
- Compare the baseline with a Random Forest classifier.
- Evaluate models using train/test splitting, cross-validation, accuracy, precision, recall, F1-score, ROC-AUC, and a confusion matrix.
- Engineer additional features and build a reusable Scikit-learn Pipeline.
- Explore the dataset using PCA and K-Means clustering.
- Produce reproducible outputs and documentation.

## Project Structure

```text
Final_Project/
├── data/
│   ├── cardio_train.csv
│   ├── cardio_clean.csv
│   └── data_dictionary.md
├── models/
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_eda_and_statistics.ipynb
│   ├── 03_supervised_learning.ipynb
│   ├── 04_model_evaluation.ipynb
│   ├── 05_feature_engineering_pipeline.ipynb
│   └── 06_clustering_and_pca.ipynb
├── outputs/
├── src/
├── README.md
└── requirements_ml.txt
```

## Dataset Setup

Download the Cardiovascular Disease dataset from Kaggle and place the CSV in:

```text
data/cardio_train.csv
```

The notebooks expect the original semicolon-separated CSV format.

The cleaned dataset will be generated automatically by `01_data_preparation.ipynb`.

## Notebook Execution Order

Run the notebooks from top to bottom in this order:

1. `01_data_preparation.ipynb`
2. `02_eda_and_statistics.ipynb`
3. `03_supervised_learning.ipynb`
4. `04_model_evaluation.ipynb`
5. `05_feature_engineering_pipeline.ipynb`
6. `06_clustering_and_pca.ipynb`

Each notebook builds on artifacts created by the previous notebooks.

## Main Machine-Learning Design

### Target

`cardio` is the binary target.

### Supervised Models

- Logistic Regression — baseline
- Random Forest — comparison model

### Evaluation

- Train/test split
- Stratified 5-fold cross-validation
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix
- ROC curves

### Feature Engineering

The pipeline creates:

- `bmi` from height and weight
- `pulse_pressure` from systolic and diastolic blood-pressure fields

These are machine-learning features for this educational project and should not be interpreted as clinical recommendations.

### Unsupervised Learning

- Standardization
- PCA
- K-Means clustering
- Silhouette score
- PCA visualization of clusters

## Reproducibility

The project uses fixed random seeds where appropriate and keeps preprocessing inside Scikit-learn Pipelines for the supervised workflow.

Install dependencies:

```bash
pip install -r requirements_ml.txt
```

Then open Jupyter Notebook or JupyterLab and execute the notebooks in the specified order.

## Limitations

- The analysis is based on a public dataset and is not a validated clinical system.
- Dataset quality, measurement conventions, and class labels may contain limitations.
- Correlation does not imply causation.
- Clustering results are mathematical groupings rather than clinically validated patient categories.
- Model performance on this dataset should not be interpreted as real-world medical performance.
- No identifiable patient information is intentionally used.

## Final Demo

The final individual demonstration should explain:

1. The problem and target.
2. Data preparation decisions.
3. Main EDA findings.
4. Baseline and comparison models.
5. Cross-validation and final metrics.
6. Confusion matrix and error types.
7. Feature engineering and Pipeline.
8. PCA and clustering findings.
9. Limitations and reproducibility.

## Alignment With Project Requirements

The project structure and notebooks are designed to cover the required areas: environment and dataset setup, data preparation, EDA/statistics, supervised classification, evaluation, feature engineering and Pipeline, unsupervised analysis, documentation, and reproducible execution.
