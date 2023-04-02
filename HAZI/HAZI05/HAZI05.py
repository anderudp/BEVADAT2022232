import pandas as pd
from typing import Tuple
from scipy.stats import mode

class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train = self.y_train = self.x_test = self.y_test = None
        self.y_preds = None

    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        dataset = pd.read_csv(csv_path, header=None).sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = dataset.iloc[:, :4], dataset.iloc[:, -1:]
        return x, y

    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        self.x_test, self.y_test = features.iloc[train_size:train_size + test_size, :], labels.iloc[train_size:train_size + test_size]

    def euclidean(self, element_of_x: pd.DataFrame):
        self.y_preds = self.x_train.copy()
        self.y_preds = self.y_preds.reset_index(drop=True).sub(element_of_x.reset_index(drop=True).loc[0], axis=1) ** 2
        self.y_preds = self.y_preds.sum(axis=1).pow(1/2)

    def predict(self) -> pd.DataFrame:
        labels_pred = []
        for index, row in self.x_test.iterrows():
            self.euclidean(row)
            distances = pd.concat([self.y_preds.reset_index(drop=True), self.y_train.reset_index(drop=True)], axis=1).sort_values(0)
            label_pred = mode(distances.iloc[:self.k, 1])
            labels_pred.append(label_pred)
        return labels_pred
