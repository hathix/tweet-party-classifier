# README #

Implementation of a Naive Bayes classifier for political tweets using scikit-learn.

* test_classifier implements an ad-hoc NB from scratch
* sklearn_classifier makes use of the BernoulliNB classifier bundled in scikit-learn

The main difference between the two is speed. This is due to the fact that scikit-learn uses contiguous in-memory C-arrays (numpy arrays) instead of Python lists. This data structure is able to handle heavy math manipulations much more efficiently.


### Why scikit-learn?

Scikit-learn provides efficient and optimized out-of-the-box classification algorithms.

It also provides lots of useful functionalities for evaluating and improving the quality of classification.

Using scikit-learn helps to cut down on development time by sparing us the trouble of having to implement the internal details of every algorithm, it also provides us with a simple and flexible framework to test future approaches.

We hope to assess differences in accuracy between the scikit-learn implementation and our custom implementation.


### Accuracy and time reports.

Tweets in DB: ~2000
——————————————————————
Vocabulary size: 500
Accuracy of classifier in train set: 0.783
Accuracy of classifier in test set: 0.639
Total running time: 3.87 secs

Vocabulary size: 1000
Accuracy of classifier in train set: 0.843
Accuracy of classifier in test set: 0.663
Total running time: 4.19 secs

Vocabulary size: 2000
Accuracy of classifier in train set: 0.904
Accuracy of classifier in test set: 0.712
Total running time: 5.12 secs

Vocabulary size: 2500
Accuracy of classifier in train set: 0.920
Accuracy of classifier in test set: 0.724
Total running time: 5.44 secs

Vocabulary size: 3000
Accuracy of classifier in train set: 0.926
Accuracy of classifier in test set: 0.717
Total running time: 5.76 secs

Vocabulary size: 4000
Accuracy of classifier in train set: 0.940
Accuracy of classifier in test set: 0.705
Total running time: 6.34 secs

We found that a vocab size of 2500 was ideal, past this the accuracy of the classifier in the test set begins to deteriorate.


Tweets in DB: ~120K
————————————————————
Vocabulary size: 2500
Accuracy of classifier in train set: 0.768
Accuracy of classifier in test set: 0.759
Total running time: 353.05 secs


We like the fact that the accuracy gap between train/test data has reduced drastically.
This means the model generalizes better to unseen data and is not overfitting as it was before.


### How to setup.

The classification and feature extraction pipeline has been tested with the
following library versions:

- Python 2.7.6

- nltk==3.0.2

- scikit-learn==0.15.1

- numpy==1.9.1


#### Running classifiers and/or comparing:

After installing requirements, run

```python main.py```

This will

- fetch a list of sample tweets ( fetched from included SQLite DB)
- create a vocabulary of frequent words
- turn the tweets into boolean vectors
- create training and test sets
- convert datasets to matrix form
- train a Bernoulli Naive Bayes classifier (best suited for boolean features)
- print out predicted results for a sample of the test data
- print out accuracy score over entire test data for classifier(s)


### Improvements.

At the moment we are running the classifiers with a vocabulary containing common words, but we could improve the algorithm by selecting those words that maximize dispersion upon Republican/Democrat classes, something like “factor analysis” - http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html.

Note: the reported times are for the entire training + evaluation process. Once we are confident with our model, there would be no need to perform the training overtime, it can be done offline once in a while and saved to a disk.

We could also try other approaches such as SVM or RandomForests. Tuning these methods for improved results would require extra work of cross-validation and parameter tuning.
