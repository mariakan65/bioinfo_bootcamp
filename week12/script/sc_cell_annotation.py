import scanpy as sc
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent.parent / 'week9' / 'data'
data_path = DATA_DIR / 'pbmc3k_clean.h5ad'

def run_cell_annotation(file):
    file_path = Path(file)
    if not file_path.exists():
        print(f"File {file_path} does not exist")
        return
    adata = sc.read_h5ad(file_path)

    print("Normalization, Log1p, HVGs, Scale, PCA")
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver='arpack')
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=0.5, flavor='igraph', n_iterations=2, directed=False)

    print("Calcuating Marker Genes (Wilcoxon Rank-Sum)")
    sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon')
    result = adata.uns['rank_genes_groups']
    groups = result['names'].dtype.names
    print("Top 5 Marker Genes per Cluster:")
    for group in groups:
        top_genes = [result['names'][i][group] for i in range(5)]
        print(f"Cluster {group}: {', '.join(top_genes)}")

    marker_genes = ['CD79A', 'CD3D', 'CD14', 'LYZ', 'GNLY', 'PPBP']
    sc.pl.umap(
        adata,
        color=['leiden'] + marker_genes,
        ncols=3,
        save='_pbmc3k_feature_plots.png',
        show=False
    )
    sc.pl.dotplot(
        adata,
        marker_genes,
        groupby='leiden',
        save='_pbmc3k_marker_dotplot.png',
        show=False
    )

    print("Analysis Complete")


if __name__ == "__main__":
    run_cell_annotation(data_path)