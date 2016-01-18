How to use Improse
==================

Once you have installed Improse, you can type::

	improse --help

to find the available commands and required parameters to run Improse. 

Improse demo
-------------

To run a demo using Random Forest model and validate it using 10-fold cross-validation, you can type::

	improse --demo

This will save the results in the current working directory with a folder named ``Improse_results``. If you wish to save the results in a specific folder, you can type::

	improse --demo --output ~/path/to/your/folder

Select model
------------
Improse comes with six state-of-the-art machine learning models including Random Forest (RF), Support Vector Machines (SVM), K-Nearest Neighbor (kNN), AdaBoost (AB), Decision Tree (DT) and Naive Bayes (NB). Random Forest is the default model.

To select model you need to type::

	improse --model MODEL_NAME

MODEL_NAME can be ``rf``, ``svm``, ``knn``, ``ab``, ``dt``, ``nb`` or use ``all`` if you want use all models one by one.

Define features and feature subsets
-----------------------------------
To tell the model to use specific features you need to type::

	improse --model svm --feature H3K27ac,Brd4,p300,pGC

Make sure the features names are coma separated. 

If you want to compare the individual predictive power or combinatorial predictive power of different features, you need to pass the argument ``--compare`` with ``--features``::

	mprose --model svm --feature H3K27ac,Brd4,p300,pGC --compare

To check the combinatorial predictive power of features, you need to combine features with ``+`` symbol::

	improse --model svm --feature H3K27ac+Brd4,p300,pGC+pAT --compare

Here model will test the combinatorial predictive power [H3K27ac,Brd4] and [pGC,pAT] along with p300.

Run model with cross-validation
-------------------------------
By default all models use 10-fold cross-validation. If you want to set different fold lets say 5, set ``--cv`` parameter as::

	improse --model rf --feature H3K27ac,Brd4,p300,pGC,pAT,phastCons --cv 5

Run model with test data
------------------------
To run the model with a test data you need the feature data saved a CSV file. Next, you need to tell the model, features you have to make prediction with using ``--feature`` and also provide the CSV file to '--input' and next type ``--test`` to tell model it is test datasets::

	improse --model rf --feature H3K27ac,Brd4,p300,pGC,pAT,phastCons --input ~/path/to/CSV/file.csv --test

This will generate an ROC plot and save the performance evaluations [precision, recall, f1-score, AUC, PRC] to ``Improse_tesults.txt``.

Make predictions
------------------
To make predictions should have computed available features and saved a CSV file. Next, you need to tell the model the features you have to make prediction with using ``--feature`` and also provide the CSV file to ``--input`` and next type ``--pred`` to make predictions::

	improse --model rf --feature H3K27ac,Brd4,p300,pGC,pAT,phastCons --input ~/path/to/CSV/file.csv --pred

This will save the predictions results as CSV file ``Improse_[MODEL_NAME]_predictions.csv``. In the CSV file the field Class is 1=SE and 0=TE. We also report  probability score for each prediction to tell the user how good and bad a prediction is. This will help to decide which candidates to select for further analysis.
