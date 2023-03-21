import pandas as pd
import matplotlib.pyplot as plt

#stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#       "population": [200.4, 143.5, 1252, 1357, 52.98] }

def dict_to_dataframe(test_dict: dict) -> pd.DataFrame:
    return pd.DataFrame(test_dict)


#df = dict_to_dataframe(stats)


def get_column(input_df: pd.DataFrame, column: str) -> pd.Series:
    new_df = input_df.copy()
    return new_df[column]


def get_top_two(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    return new_df.sort_values('area', ascending=False)[:2]


def population_density(input_df: pd.DataFrame) -> pd.DataFrame:
    new_df = input_df.copy()
    new_df['density'] = new_df['population'] / new_df['area']
    return new_df


def plot_population(input_df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.bar(input_df['country'], input_df['population'])
    ax.set_title('Population of Countries')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population (millions)')
    #plt.show()
    return fig


def plot_area(input_df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.pie(input_df['area'], labels=input_df['country'])
    ax.set_title('Area of Countries')
    #plt.show()
    return fig
