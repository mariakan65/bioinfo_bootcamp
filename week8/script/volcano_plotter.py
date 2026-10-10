import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
DATA_DIR = REPO_ROOT / 'week7'/'data'
data_file = DATA_DIR / 'fdr_results.tsv'



def plot_volcano(file):
    file_path = Path(file)
    if not file_path.exists():
        print(f'File {file_path} does not exist!')
        return
    df = pd.read_csv(file_path, sep="\t", index_col=0)
    df["neg_log10_padj"] = -np.log10(df["p_adjusted"])
    plt.figure(figsize = (12,8))
    up = df[(df["p_adjusted"] < 0.05) & (df["log2FC"] >= 1.0)]
    down = df[(df["p_adjusted"] < 0.05) & (df["log2FC"] <= -1.0)]
    not_sig = df[(df["p_adjusted"] >= 0.05) | (df["log2FC"].abs() < 1.0)]
    plt.scatter(not_sig["log2FC"], not_sig["neg_log10_padj"], color="grey", alpha=0.6, label="Not Significant", s=40)
    plt.scatter(up["log2FC"], up["neg_log10_padj"], color="#E10600FF", alpha=0.9, label="Upregulated", s=60)
    plt.scatter(down["log2FC"], down["neg_log10_padj"], color="#00239CFF", alpha=0.9, label="Downregulated", s=60)


    for gene_id, row in pd.concat([up, down]).iterrows():
        plt.text(row["log2FC"] + 0.05, row["neg_log10_padj"] + 0.05, str(gene_id), fontsize=9, fontweight='bold')


    plt.axhline(y=-np.log10(0.05), color="black", linestyle="--", linewidth=1, label="padj = 0.05")
    plt.axvline(x=1.0, color="blue", linestyle="--", linewidth=1, label="|log2FC| = 1.0")
    plt.axvline(x=-1.0, color="blue", linestyle="--", linewidth=1)

    plt.title("RNA-Seq Differential Expression: Volcano Plot", fontsize=12, fontweight='bold')
    plt.xlabel("log2(Fold Change)", fontsize=11)
    plt.ylabel("-log10(Adjusted p-value)", fontsize=11)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True)
    plt.grid(True, linestyle=":", alpha=0.5)

    output_img = file_path.parent.parent.parent / "week8" / "data" / "volcano_plot.png"
    output_img.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_img, dpi=300, bbox_inches='tight')
    print("Volcano plotting complete")
    plt.close()

if __name__ == "__main__":
    plot_volcano(data_file)