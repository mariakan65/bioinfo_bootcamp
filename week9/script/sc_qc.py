import scanpy as sc

def run_sc_qc():
    adata = sc.datasets.pbmc3k()
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    num_mt = adata.var['mt'].sum()
    print(f"Number of mitochondrial genes found: {num_mt}")
    data = sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
    initial_cells = adata.n_obs

    cell_mask = (
            (adata.obs['n_genes_by_counts'] >= 200) &
            (adata.obs['n_genes_by_counts'] <= 2500) &
            (adata.obs['pct_counts_mt'] < 5.0)
    )
    adata_filtered = adata[cell_mask, :].copy()

    removed_cells = initial_cells - adata_filtered.n_obs
    print(f"Initial number of cells: {initial_cells}")
    print(f"Rejected cells (Low Quality / Dead / Doublets): {removed_cells}")
    print(f"Clean cells filtered for analysis: {adata_filtered.n_obs}")


    output_path = "C:/Users/user/bioinfo_bootcamp/week9/data/pbmc3k_clean.h5ad"
    adata_filtered.write(output_path)
    print(f"\nDataset saved to: {output_path}")


run_sc_qc()

