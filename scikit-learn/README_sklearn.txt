# README #

Implementation of a Naive Bayes classifier for political tweets using scikit-learn.

* test_classifier implements an ad-hoc NB from scratch
* sklearn_classifier makes use of the BernoulliNB classifier bundled in scikit-learn

The main difference between the two is speed. This is due to the fact that scikit-learn uses contiguous in-memory C-arrays (numpy arrays) instead of Python lists. This data structure that is able to handle heavy math manipulations much more efficiently.


### Why scikit-learn?

Scikit-learn provides efficient and optimized out-of-the-box classification algorithms.

It also provides lots of useful functionalities for evaluating and improving the quality of classification.

Using scikit-learn helps to cut down on development time by sparing us the trouble of having to implement the internal details of every algorithm, it also provides us with a simple and flexible framework to test future approaches.

We hope to assess differences in accuracy between the scikit-learn implementation and our custom implementation.


### How to setup

The classification and feature extraction pipeline has been tested with the
following library versions:

- Python 2.7.6

- nltk==3.0.2

- scikit-learn==0.15.1

- numpy==1.9.1


