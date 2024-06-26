# Data Exploration Projekt

## Group Members of "EduPredictors"

- Elisabeth Barar (2825002)
- Johanna Unruh (5132960)

## Goal of this Project

The goal of this project is to predict academic success and thereby whether a student will dopout or graduate.
Therefore, we will train four different Machine Learning (ML) models for classification. In addition, we will evaluate which model has the best prediction results and visiulize the model through a streamlit app.

## Course of Action

For this we will do a data cleanup first. Secondly, we will train the models and try to improve them using hyperparameter tuning. Thirdly, we will evaluate the different models.

### 1. Data Cleanup

During the data cleanup we will remove all rows which have NaN values. Following, we will analyze the correlation. Since the dataset is for classification we use the Spearman correlation instead of the Pearson correlation which is for linear correlation. Moreover, we remove columns which have a small correlation with the target column. Finally, we remove all rows which have the target value "enrolled" to have a two class problem.

### 2. Training of ML-Models

We decided to train the four following models: k-Nearest-Neigbours, Random Forest, Decision Trees and Naive Bayes. To train to we split the dataset first in 70% training data and 30% testing data first. Secondly, we train those models using the Python library scikit-learn. Thirdly, we improve the performance of every model using hyperparameter tuning using GridSearchCV of scikit-learn.

### 3. Evaluation

Confusion Matrix and the ROC-curve are methods to compare and evaluate the performance of ML models. Moreover, we will calculate the accuracy, precision, recall and f1-score. This is helpful for evaluating and comparing the performance of the differnent values as well. Finally, we will interprete all results to justify which model has the best results.

## Execution of the Notebooks

We decided to use Jupyter Notebooks, because the output (e.g. grafics) of the belonging cells can be seen and analysized below. Therefore, it is a convenient method to analyze data and ML models.

All the packages that are needed to execute the Jupyter Notebooks can be installed depending on the pip version with `pip install -r requirements.txt` or `pip3 install -r requirements.txt`.

The order of the notebooks is the following:

1. Data Cleanup
2. Training ML Models
3. Evaluation

You can also try our model using this [link](https://hannah127-data-exploration-projekt-app-bcdugr.streamlit.app/).
