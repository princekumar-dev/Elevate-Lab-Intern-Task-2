import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    data_path = "Titanic-Dataset.csv"
    df = pd.read_csv(data_path)

    print('\n=== DataFrame info ===')
    df.info()

    print('\n=== Summary statistics (describe) ===')
    print(df.describe(include='all'))

    print('\n=== Missing values per column ===')
    print(df.isnull().sum())

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if c.lower() != 'passengerid']

    for col in numeric_cols:
        print(f"\n-- Plotting {col}: histogram and boxplot --")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        sns.histplot(df[col].dropna(), kde=True, ax=axes[0])
        axes[0].set_title(f"Histogram of {col}")
        sns.boxplot(x=df[col].dropna(), ax=axes[1])
        axes[1].set_title(f"Boxplot of {col}")
        plt.tight_layout()
        plt.show()

    print('\n-- Creating pairplot (may take a moment) --')
    pair_cols = numeric_cols.copy()
    if 'Survived' in df.columns and 'Survived' not in pair_cols:
        pair_cols.append('Survived')
    sample = df[pair_cols].dropna()
    if len(sample) > 500:
        sample = sample.sample(500, random_state=1)
    sns.pairplot(sample, hue='Survived' if 'Survived' in sample.columns else None, diag_kind='kde', plot_kws={'alpha':0.6})
    plt.suptitle('Pairplot of numeric features', y=1.02)
    plt.show()

    print('\n-- Correlation matrix --')
    corr = df.select_dtypes(include=[np.number]).corr()
    print(corr)
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title('Correlation matrix')
    plt.tight_layout()
    plt.show()

    print('\n=== Simple inferences ===')
    if 'Survived' in df.columns:
        surv_rate = df['Survived'].mean()
        print(f"Overall survival rate: {surv_rate:.3f}")
        if 'Sex' in df.columns:
            print('\nSurvival rate by Sex:')
            print(df.groupby('Sex')['Survived'].mean())
        if 'Pclass' in df.columns:
            print('\nSurvival rate by Pclass:')
            print(df.groupby('Pclass')['Survived'].mean().sort_index())
        if 'Age' in df.columns:
            bins = [0, 12, 18, 35, 60, 120]
            labels = ['child', 'teen', 'young_adult', 'adult', 'senior']
            age_grp = pd.cut(df['Age'], bins=bins, labels=labels)
            print('\nSurvival rate by Age group:')
            print(df.groupby(age_grp)['Survived'].mean())

    print('\nAnalysis complete (no files written).')


if __name__ == '__main__':
    main()
