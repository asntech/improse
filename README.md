# Improse
Improse - Integrated Methods for Prediction of Super-Enhancers

## Introduction
This is an easy to install and run python package for Improse (Integrated Methods for Prediction of Super-Enhancers)

## Prerequisites
Improse required:
			
	 Python (>= 2.6 or >= 3.3),
	 NumPy (>= 1.6.1), http://www.numpy.org/
	 SciPy (>= 0.9), http://www.scipy.org/
	 Scikit-learn (>= 0.17), http://scikit-learn.org/
	 Pandas (>= 0.16.2). http://pandas.pydata.org/

If you already have a working installation of numpy and scipy, the easiest way to install scikit-learn and pandas is using pip

	 pip install -U scikit-learn

	 hpip install -U pandas

or using conda:

	 conda install scikit-learn

	 conda install pandas


If you don’t already have a python installation with numpy, scipy and pandas, we recommend to install either via your package manager or via a python bundles (Canopy, Anaconda). These come with numpy, scipy, scikit-learn, pandas and many other helpful scientific and data processing libraries and available for platforms including Windows, Mac OSX and Linux.


## Install Improse
You can install Improse either from PyPi using pip and install it from the source. Please make sure you have already installed the above mentioned python libraries required to run Improse.

Install from PyPi

	 pip install improse

Install from the source

	 python setup.py install

## Use Improse
Once you have installed Improse, you can type:
	improse --help
to find the avaiable commands and required parameters to run Improse. 

### Improse demo

To run a demo using Random Forest model and validate it using 10-fold cross-validation, you can type

	improse --demo

This will save the results in the current working directory with a folder named 'Improse_results'. If you wish to save the results in a specific folder, you can type

	improse --demo --output ~/path/to/your/folder

### Select model 
Improse comes with six state-of-the-art machine learning models including Random Forest (RF), Support Vector Machines (SVM), K-Nearest Neighbor (kNN), AdaBoost (AB), Decision Tree (DT) and Naive Bayes (NB). Random Forest is the default model.

To select model you need to type:
	 
	 improse --model MODEL_NAME

MODEL_NAME can be 'rf', 'svm', 'knn', 'ab', 'dt', 'nb' or use 'all' if you want use all models one by one.

### Define features and feature subsets
To select model you need to type:
	 
	 improse --model svm --feature H3K27ac,Brd4,p300,pGC

Make sure the features names are coma separated. 

If you want to compare the indidual predictive power or combinatorial predive power of different features, you need to pass the argument '--compare' with '--features'

	 improse --model svm --feature H3K27ac,Brd4,p300,pGC --compare

To check the combinatorial predive power of features, you need to combine features with '+' symbole

	 improse --model svm --feature H3K27ac+Brd4,p300, pGC+pAT --compare


### Run model with cross-validation

### Run model with test data

### Make predictions


## Support
If you have questions, or found any bug in the program, please write to us at khana10[at]mails.tsinghua.edu.cn

## Cite Us
If you use Improse please cite us: 
