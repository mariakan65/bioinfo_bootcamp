from pathlib import Path

pval_path = Path("C:/Users/user/bioinfo_bootcamp/week7/data/pvalues.tsv")
pval_path.parent.mkdir(parents=True, exist_ok=True)

content = (
    "GeneID\tpvalue\tlog2FC\n"
    "GENE_1\t0.0001\t2.5\n"
    "GENE_2\t0.0020\t1.8\n"
    "GENE_3\t0.0080\t-2.1\n"
    "GENE_4\t0.0120\t1.2\n"
    "GENE_5\t0.0350\t0.9\n"
    "GENE_6\t0.0410\t-1.1\n"
    "GENE_7\t0.0600\t0.4\n"
    "GENE_8\t0.1200\t-0.3\n"
    "GENE_9\t0.4500\t0.1\n"
    "GENE_10\t0.8900\t0.05\n"
)

with open(pval_path, "w", encoding="utf-8") as f:
    f.write(content)

print("To pvalues.tsv dimiourgithike epitychos me ta swsta p-values!")