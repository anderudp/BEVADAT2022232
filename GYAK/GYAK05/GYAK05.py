import numpy as np
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix as sk_confusion_matrix

class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train = self.y_train = self.x_test = self.y_test = None
        self.y_preds = None

    @staticmethod
    def load_csv(self, csv_path: str) -> Tuple[np.ndarray, np.ndarray]:
        np.random.seed(42)
        dataset = np.genfromtxt(csv_path, delimiter=',')
        np.random.seed(42)
        np.random.shuffle(dataset, )
        x, y = dataset[:, :4], dataset[:, -1]
        return x, y

    def train_test_split(self, features: np.ndarray, labels: np.ndarray):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        self.x_train, self.y_train = features[:train_size, :], labels[:train_size]
        self.x_test, self.y_test = features[train_size:train_size + test_size, :], labels[train_size:train_size + test_size]

    def euclidean(self, element_of_x: np.ndarray):
        self.y_preds = np.sqrt(np.sum((self.x_train - element_of_x) ** 2, axis=1))

    def predict(self, x_test: np.ndarray) -> np.ndarray:
        labels_pred = []
        for x_test_element in x_test:
            self.y_preds = np.array(sorted(zip(self.y_preds, self.y_train)))
            label_pred = mode(self.y_preds[:self.k, 1], keepdims=False).mode
            labels_pred.append(label_pred)
        return np.array(labels_pred, dtype=np.int32)

    def accuracy(self):
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self) -> np.ndarray:
        return sk_confusion_matrix(self.y_test, self.y_preds)

    @property
    def k_neighbors(self):
        return self.k