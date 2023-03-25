import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


def add_grade(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    new_df['grade'] = new_df[["math score", "reading score", "writing score"]].sum(axis=1).div(300)
    new_df['grade'] = new_df['grade'].apply(lambda x:
                                            'A' if x >= 0.9
                                            else 'B' if x >= 0.8
                                            else 'C' if x >= 0.7
                                            else 'D' if x >= 0.6
                                            else 'F')
    return new_df


def math_bar_plot(input_df: pd.DataFrame) -> plt.Figure:
    new_df = input_df.copy()
    new_df = new_df.groupby(['gender']).mean(numeric_only=True)['math score']
    fig, ax = plt.subplots()
    ax = new_df.plot(kind="bar")
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    #plt.show()
    return fig


def writing_hist(input_df: pd.DataFrame) -> plt.Figure:
    new_df = input_df.copy()
    fig, ax = plt.subplots()
    ax.hist(new_df['writing score'])
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    #plt.show()
    return fig


def ethnicity_pie_chart(input_df: pd.DataFrame) -> plt.Figure:
    new_df = input_df.copy()
    new_df = new_df.groupby(['race/ethnicity']).size().reset_index(name="counts")
    fig, ax = plt.subplots()
    ax.pie(new_df["counts"], autopct='%1.1f%%', labels=new_df['race/ethnicity'])
    ax.set_title('Proportion of Students by Race/Ethnicity')
    #plt.show()
    return fig
