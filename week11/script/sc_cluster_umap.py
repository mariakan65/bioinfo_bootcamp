import scanpy as sc
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent.parent/'week9'/'data'
data_path = DATA_DIR/"pbmc3k_clean.h5ad"


def run_clustering_umap(file):
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

    print("k-NN Graph & UMAP Embedding")
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)
    sc.tl.umap(adata)

    print("Leiden Clustering")
    sc.tl.leiden(adata, resolution=0.5)

    num_clusters = len(adata.obs['leiden'].unique())
    print(f"{num_clusters} cell clusters found.")



    sc.pl.umap(
        adata,
        color=['leiden'],
        title="PBMC 3k: UMAP Clustering (Leiden res=0.5)",
        save="_pbmc3k_clusters.png",
        show=False
    )

    print("Analysis Complete")


if __name__ == "__main__":
    run_clustering_umap(data_path)