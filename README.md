# CS51 Final Project

<!--
**Predicting how politicians will vote.**

Uses data from [Quorum](https://quorum.us) and with machine learning to generate a left/right score for each lawmaker and each bill; then uses the Ideal Points algorithm to determine the probability that a given lawmaker will vote yes on a given bill.

Check out our full [writeup](writeup.md).
-->

Neel Mehta, Ajay Nathan, Saranya Vijayakumar, Sam Lam.

## Getting started

This project uses [Python 2](https://python.org).

```
$ pip install -r requirements.txt
$ python
> import nltk
> nltk.download() # follow graphical installer
$ python tpclassifier/manage.py runserver
$ open http://127.0.0.1:8000/
```