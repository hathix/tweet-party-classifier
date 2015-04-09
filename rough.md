# Rough work

## Mathematical modeling

### Building model

Each lawmaker *i* has an ideal point X[i] that represents where they stand on the left/right spectrum (not sure what correlates to what.)

Each bill *d* has a popularity (difficulty) B[d], which reflects how overall attractive the bill is, and a polarity (discrimination) A[d], which reflects where the bill is on the left/right axis. When popularity B[d] is high (very positive), most lawmakers will vote yes. When popularity B[d] is low (very negative), most lawmakers will vote no. When popularity B[d] is near zero, the polarity A[d] and the individual lawmaker's ideal point X[i] determine how the lawmaker will vote.

We can use this information to predict if the lawmaker will vote yes:

```
P(yes)[i,d] = S(X[i]A[d] + B[d])
```

where S(x) = the inverse logistic function `(e^x)/(1 + e^x)`. S(x) tends toward 0 as x approaches -Infinity and tends toward 1 as x approaches +Infinity. This distribution is useful because it allows for outliers.

We also know C[i,d], where

```
C[i,d] =
	1 if lawmaker i actually voted yes on bill d
	0 if they voted no
```

We can now compare the predicted outcomes P(yes)[i,d] to the actual outcomes C[i,d] to determine the accuracy of the model.

### Testing model

For each pairing of lawmaker and bill, we can determine the error score E[i,d], which simply measures if the prediction was right or wrong.

```
E[i,d] =
	1 if P(yes)[i,d] < 0.5 and C[i,d] = 1 (yes)
	1 if P(yes)[i,d] > 0.5 and C[i,d] = 0 (no)
	0 otherwise
```

Essentially, we say the model erred if it predicted a better-than-average chance that the lawmaker would vote yes when they actually voted no, or the reverse.

Now, since E[i,d] is simply whether the prediction was right or wrong, a P[i,d] close to 0.5 is more likely to be wrong than a more extreme P[i,d].

But we can control for this by introducing the expected error rate R[i,d], which is defined as

```
R[i,d] = min(P(yes)[i,d], 1 - P(yes)[i,d])
```

Note that E[i,d] is either 0 or 1, while R[i,d] is any real number between 0 and 1 inclusive.

To control for this difference, we can assign an excess error EE[i,d]:

```
EE[i,d] = E[i,d] - R[i,d]
```

The expected/average value of EE[i,d] is 0, so finding the average EE[i,d] for all lawmakers *i* and bills *d* is an informative measure of the error in the model.