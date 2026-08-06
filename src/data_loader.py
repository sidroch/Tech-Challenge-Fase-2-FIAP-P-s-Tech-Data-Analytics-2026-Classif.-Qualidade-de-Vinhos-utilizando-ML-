import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Carrega o dataset a partir do caminho informado."""
    df = pd.read_csv(path)
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica pré-processamentos necessários."""
    df = df.dropna()
    return df

