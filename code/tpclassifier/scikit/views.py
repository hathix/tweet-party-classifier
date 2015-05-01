from django.shortcuts import render
from django.http import HttpResponseRedirect

import sklearn.main as main


def index(request):
	nwords, num_tweets, accuracy_train, accuracy_test = main.run_accuracy_reports()
	context = {"accuracy_train": accuracy_train, "accuracy_test": accuracy_test, "nwords": nwords, "num_tweets": num_tweets}
	return render(request, "scikit/index.html", context)
