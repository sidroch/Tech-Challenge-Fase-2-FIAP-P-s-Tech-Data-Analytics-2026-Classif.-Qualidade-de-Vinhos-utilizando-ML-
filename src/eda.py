import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def describe_data(df: pd.DataFrame):
    """Exibe estatísticas descritivas."""
    print(df.describe())

def correlation_matrix(df: pd.DataFrame, save_path="results/correlation_matrix.png"):
    """Gera matriz de correlação."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

