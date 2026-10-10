import scanpy as sc
from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent.parent/ "week9" / "data"
data_path = DATA_DIR  / "pbmc3k_clean.h5ad"

def run_normalization_pca(file):
    file_path = Path(file)
    if not file_path.exists():
        print(f"File {file_path} does not exist")
        return
    adata = sc.read_h5ad(file_path)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver='arpack')
    print(adata.var['highly_variable'].sum())

if __name__ == "__main__":
    run_normalization_pca(data_path)
