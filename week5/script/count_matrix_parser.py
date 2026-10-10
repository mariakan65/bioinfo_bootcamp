import pandas as pd
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / 'data'
file_path = DATA_DIR / 'counts.tsv'

def count_matrix(data):
    data_path = Path(data)
    if not data_path.exists():
        print(f"{data_path} does not exist")
        return

    df = pd.read_csv(data_path, sep="\t", index_col=0)

    df["average_control"] = (df["Control_1"] + df["Control_2"])/2
    df["average_treated"] = (df["Treated_1"] + df["Treated_2"])/2

    df["Fold_Change"] = df["average_treated"] / df["average_control"]
    df["log2FC"] = np.log2(df["Fold_Change"])

    df["Status"] = "Unchanged"
    df.loc[df["log2FC"] >= 1.0, "Status"] = "Upregulated"
    df.loc[df["log2FC"] <= -1.0, "Status"] = "Downregulated"
    print("Gene Expression Count Matrix completed!")
    print(df[["average_control", "average_treated", "Fold_Change", "log2FC", "Status"]])

    output_path = data_path.parent / "expression_results.tsv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, sep="\t")
    print(f"Results saved in {output_path}")

if __name__ == "__main__":
    count_matrix(file_path)
