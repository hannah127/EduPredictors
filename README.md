# Data Exploration Projekt

## Goal of this Project

Predict Students' Dropout and Academic Success

- Trainieren unterschiedlicher Klassifikationsmodelle
- Herausfinden, welches Modell am Besten ist

## Course of Action

### 1. Data Cleanup

1. Entfernen der Zeilen, die NaN Werte haben
2. Korrelationsanalyse durchführen
   a. Pearson Korrelation für lineare Zusammenhänge
   b. Spearman Korrelation für nicht lineare Zusammenhänge
3. Spalten, die eine geringe Korrelation zu der Zielspalte haben, werden aus dem
   Datensatz entfernt
4. Zeilen, die bei der Zielspalte „Enrolled“ stehen haben, werden entfernt

### Training of ML-Models

1. k- Nearest-Neighbours
2. Random Forest
3. Decision Tree
4. Naive Bayes

- Aufsplitten des Datensatzes: 70% Trainingsdaten, 30% Testdaten
- Trainieren des Modells mit Hilfe von scikit-learn
- Verbesserung der Performance des Modells durch Hyperparametertuning
- Verwendung von GridSearchCV von scikit-learn

### Evaluation

- Erstellung einer Confusion Matrix und einer ROC-Kurve
- Berechnung von accuracy, precision, recall und f1-score
- Interpretation der Ergebnisse und Wahl des besten Modells

## Group Members of "EduPredictors"

- Elisabeth Barar (2825002)
- Johanna Unruh (5132960)

## Execution of the Notebooks

All the packages that are needed to execute the jupyter notebooks can be installed depending on the pip version with `pip install -r requirements.txt` or `pip3 install -r requirements.txt`.

- to do: Reihenfolge der Notebooks
