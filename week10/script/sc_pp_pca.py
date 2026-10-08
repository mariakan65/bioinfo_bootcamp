import scanpy as sc
file_path = ("C:/Users/user/bioinfo_bootcamp/week9/data/pbmc3k_clean.h5ad")
def run_normalization_pca(file):
    adata = sc.read_h5ad(file)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver='arpack')
    print(adata.var['highly_variable'].sum())

run_normalization_pca(file_path)