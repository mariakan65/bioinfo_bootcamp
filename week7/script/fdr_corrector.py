import numpy as np
import pandas as pd
from pathlib import Path
from statsmodels.stats.multitest import multipletests


data_file = Path("C:/Users/user/bioinfo_bootcamp/week7/data/pvalues.tsv")
data_file.parent.mkdir(parents=True, exist_ok=True)

def adjust_p(file):
    df = pd.read_csv(file, sep="\t", index_col=0)
    df["p_adjusted"] = multipletests(df["pvalue"], method="fdr_bh")[1]
    condition = (df["p_adjusted"] < 0.05) & (df["log2FC"].abs() >= 1.0)
    df["Significant"] = "NO"
    df.loc[condition, "Significant"] = "YES"
    countp = (df["pvalue"] < 0.05).sum()
    counta = (df["Significant"] == "YES").sum()
    print("FDR correction results((Benjamini-Hochberg)")
    print(df[["pvalue", "p_adjusted", "log2FC", "Significant"]])
    print(f"Before adjustin p-values {countp} genes were significant.")
    print(f"After adjustin p-values {counta} genes remained significant.")
    output_path = file.parent / "fdr_results.tsv"
    df.to_csv(output_path, sep="\t")
    print(f"\nResults saved in {output_path}")


adjust_p(data_file)

