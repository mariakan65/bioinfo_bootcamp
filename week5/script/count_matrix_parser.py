import pandas as pd
from pathlib import Path

data_path = Path("C:/Users/user/bioinfo_bootcamp/week5/data/counts.tsv")
data_path.parent.mkdir(parents=True, exist_ok=True)

def count_matrix(data):

    df = pd.read_csv(data, sep="\t", index_col=0)


    df["average_control"] = (df["Control_1"] + df["Control_2"])/2
    df["average_treated"] = (df["Treated_1"] + df["Treated_2"])/2
    df["Fold_Change"] = df["average_treated"] / df["average_control"]

    df["Status"] = "Unchanged"
    df.loc[df["Fold_Change"] > 1.0, "Status"] = "Upregulated"
    df.loc[df["Fold_Change"] < 1.0, "Status"] = "Downregulated"
    print("Gene Expression Count Matrix completed!")
    print(df[["average_control", "average_treated", "Fold_Change", "Status"]])
    output_path = data.parent / "expression_results.tsv"
    df.to_csv(output_path, sep="\t")
    print(f"Results saved in {output_path}")


count_matrix(data_path)
