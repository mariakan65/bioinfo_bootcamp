import scanpy as sc
from pathlib import Path
file_path = Path("C:/Users/user/bioinfo_bootcamp/week9/data/pbmc3k_clean.h5ad")

def run_cell_annotation(file):
    adata = sc.read_h5ad(file)
    print("Preprocessing (Normalization, Log1p, HVGs, Scale, PCA)")
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver='arpack')
    print("Calculating k-NN Graph & UMAP Embedding")
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)
    sc.tl.umap(adata)
    print("Leiden Clustering")
    sc.tl.leiden(adata, resolution=0.5)
    num_clusters = len(adata.obs['leiden'].unique())
    print(f"{num_clusters} clusters found.")


    sc.pl.umap(
        adata,
        color=['leiden'],
        title='PBMC 3k: UMAP Clustering (Leiden resolution = 0.5)',
        save='pbmc3k_clustering_umap.png',
        show=False
    )
    print("Analysis complete. Saved graph.")
    
if __name__ == "__main__":
    run_cell_annotation(file_path)
