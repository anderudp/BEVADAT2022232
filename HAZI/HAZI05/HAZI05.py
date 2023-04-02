import pandas as pd
from typing import Tuple

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

    def predict(self, x_test: pd.DataFrame) -> pd.DataFrame:
        labels_pred = []
        for x_test_element in x_test:
            self.euclidean(x_test_element)
            self.y_preds = np.array(sorted(zip(self.y_preds, self.y_train)))
            label_pred = mode(self.y_preds[:self.k, 1], keepdims=False).mode
            labels_pred.append(label_pred)
        return np.array(labels_pred, dtype=np.int32)
