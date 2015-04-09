# Rough work

## Mathematical modeling

### Building model

Each lawmaker *i* has an ideal point X[i] that represents where they stand on the left/right spectrum (not sure what correlates to what.)

Each bill *d* has a popularity (difficulty) B[d], which reflects how overall attractive the bill is, and a polarity (discrimination) A[d], which reflects where the bill is on the left/right axis. When popularity B[d] is high (very positive), most lawmakers will vote yes. When popularity B[d] is low (very negative), most lawmakers will vote no. When popularity B[d] is near zero, the polarity A[d] and the individual lawmaker's ideal point X[i] determine how the lawmaker will vote.

This can be modeled by:

```
P(yes)[i,d] = S(X[i]A[d] + B[d])
```

where S(x) = the inverse logistic function `(e^x)/(1 + e^x)`. S(x) tends toward 0 as x approaches -Infinity and tends toward 1 as x approaches +Infinity. This distribution is useful because it allows for outliers.

### Testing model

For each pairing of lawmaker and bill, we can determine the error score E[i,d], which simply measures if the prediction was right or wrong.

```
E[i,d] =
	1 if P(yes)[i,d] < 0.5 and vote = yes
	1 if P(yes)[i,d] > 0.5 and vote = no
	0 otherwise
```

Essentially, we say the model erred if it predicted a better-than-average chance that the lawmaker would vote differently than they actually did.

The expected error rate R[i,d], meanwhile, is defined as

```
R[i,d] = min(P[i,d], 1 - P[i,d])
```

Note that E[i,d] is either 0 or 1, while R[i,d] is any real number between 0 and 1 inclusive.

Now, since E[i,d] is simply whether the prediction was right or wrong, a P[i,d] close to 0.5 is more likely to be wrong than a more extreme P[i,d].

To control for this difference, we can assign an excess error EE[i,d]:

```
EE[i,d]
```