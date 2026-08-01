import seaborn as sns
import matplotlib.pyplot as plt

def boxplot_feature(df, feature, target, save_path):
    """Gera boxplot de uma feature por classe."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[target], y=df[feature])
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def violin_feature(df, feature, target, save_path):
    """Gera gráfico violin."""
    plt.figure(figsize=(8, 5))
    sns.violinplot(x=df[target], y=df[feature])
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def bar_distribution(df, column, save_path):
    """Distribuição de valores em barras."""
    plt.figure(figsize=(8, 5))
    df[column].value_counts().plot(kind="bar")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

