import random

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def csv_to_df(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def capitalize_columns(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    new_df.columns = [name.capitalize() if 'e' not in name else name for name in new_df.columns]
    return new_df


def math_passed_count(input_df: pd.DataFrame) -> int:
    new_df = input_df.copy()
    return new_df[new_df['math score'] >= 50].shape[0]


def did_pre_course(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    return new_df[new_df["test preparation course"] == "completed"]


def average_scores(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    return new_df.groupby('parental level of education')[["math score", "reading score", "writing score"]].mean()


def add_age(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    random.seed(42)
    age = [random.randint(18, 66) for i in range(new_df.shape[0])]
    new_df['age'] = age
    return new_df


def female_top_score(input_df: pd.DataFrame) -> tuple:
    new_df = input_df.copy()
    new_df = new_df[new_df['gender'] == "female"]
    new_df['score total'] = new_df[["math score", "reading score", "writing score"]].sum(axis=1)
    new_df = new_df[new_df['score total'] == new_df['score total'].max()]
    return new_df['math score'].iloc[0], new_df['reading score'].iloc[0], new_df['writing score'].iloc[0]

print(female_top_score(csv_to_df("StudentsPerformance.csv")))
