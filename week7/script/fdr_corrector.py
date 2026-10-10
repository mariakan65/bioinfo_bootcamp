import numpy as np
import pandas as pd
from pathlib import Path
from statsmodels.stats.multitest import multipletests

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / 'data'
data_file = DATA_DIR / 'pvalues.tsv'


def adjust_p(file):
    input_path = Path(file)
    if not input_path.exists():
        print(f"Error: {input_path} does not exist!")
        return
    df = pd.read_csv(input_path, sep="\t", index_col=0)
    df["p_adjusted"] = multipletests(df["pvalue"], method="fdr_bh")[1]
    condition = (df["p_adjusted"] < 0.05) & (df["log2FC"].abs() >= 1.0)
    df["Significant"] = "NO"
    df.loc[condition, "Significant"] = "YES"
    countp = (df["pvalue"] < 0.05).sum()
    counta = (df["Significant"] == "YES").sum()
    print("FDR correction results((Benjamini-Hochberg)")
    print(df[["pvalue", "p_adjusted", "log2FC", "Significant"]])
    print(f"Before adjusting p-values {countp} genes were significant.")
    print(f"After adjusting p-values {counta} genes remained significant.")
    output_path = input_path.parent / "fdr_results.tsv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, sep="\t")
    print(f"\nResults saved in {output_path}")

if __name__ == "__main__":
    adjust_p(data_file)

