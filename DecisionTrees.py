import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=Nonte, threshold=None, left=None, right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value=None

    def is_lead_none(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split=min_samples_split
        self.max_depth=max_depth
        self.n_features=n_features
        self.root=None

    def fit(self, X, y):
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(X,y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_feats = X.shape
        n_labels = len(np.unique(y))

        # checa o critério de parada
        if (depth>=self.max_depth or n_labels==1 or n_samples<self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=)

        feat_idx = np.random.choice(n_feats)
        # encontra o melhor split
        best_thresh, best_feature = self._best_split(X, y, feat_idx):

        
        # criar child nodes
    
    def _most_common_label(self):
        coutner = Counter(y)
        value = counter.most_common(1)[0][0]
        return value

    def predict():