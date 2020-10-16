import numpy as np


class MyLinearRegression:
    def __init__(self):
        self._coef = None
        self._intercept = None

    def fit(self, X, y):
        if y.ndim == 1:
            y_ = np.reshape(y.values, (y.shape[0], 1))
        else:
            y_ = y.values
        if X.ndim == 1:
            X_ = np.reshape(X.values, (X.shape[0], 1))
        else:
            X_ = X.values
        # -- Simple linear regression
        if X_.shape[1] == 1:
            c = np.cov(X_, y_, rowvar=False)
            v = np.var(X_)
            self._coef = (c / v)
            self._intercept = y.mean() - self._coef * X_.mean()
            print(self._coef, self._intercept)
            return self._coef[1][0], self._intercept[0][1]
        # -- Multiple linear regression
        else: # DOES NOT WORK YET
            Xs = np.hstack((X_, y_))
            #Xs = self._scale(Xs)
            return self._coef, self._intercept

    def _scale(self, X):
        nom = (X - X.min(axis=0))*2
        denom = X.max(axis=0) - X.min(axis=0)
        if denom == 0:
            denom = 1
        return  -1 + nom / denom
