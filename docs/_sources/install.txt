Installation
============

Prerequisites
-------------
Improse requires:

	* Python (>= 2.6 or >= 3.3)
	* NumPy (>= 1.6.1): http://www.numpy.org/
	* SciPy (>= 0.9): http://www.scipy.org/
	* Scikit-learn (>= 0.17): http://scikit-learn.org/
	* Pandas (>= 0.16.2): http://pandas.pydata.org/

If you already have a working installation of numpy and scipy, the easiest way to install scikit-learn and pandas is using pip::

	pip install -U scikit-learn

	pip install -U pandas

or using conda::

	conda install scikit-learn

	conda install pandas


If you don’t already have a python installation with numpy, scipy and pandas, we recommend to install either via your package manager or via a python bundles (Canopy, Anaconda). These come with numpy, scipy, scikit-learn, pandas and many other helpful scientific and data processing libraries and available for platforms including Windows, Mac OSX and Linux.


Install Improse
---------------
You can install Improse either from PyPi using pip and install it from the source. Please make sure you have already installed the above mentioned python libraries required to run Improse.

Install from PyPi::

	pip install improse

Install from the source::
	
	tar -zxvf improse-1.0.tar.gz
	cd improse-1.0
	python setup.py install

