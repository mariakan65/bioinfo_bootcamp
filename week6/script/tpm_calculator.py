from pathlib import Path
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / 'data'
data_path = DATA_DIR / 'counts_with_length.tsv'

def calculate_tpm(file):
    file_path = Path(file)
    if not file_path.exists():
        print(f'File not found in {file_path}')
        return
    df = pd.read_csv(file_path, sep='\t', index_col=0)
    df["Length_kb"] = df["Length_bp"] / 1000
    df["RPK"] = df["Sample_1"] /df["Length_kb"]
    scaling_factor = df["RPK"].sum()/1000000
    df["TPM"] = df["RPK"] / scaling_factor
    total_tpm = df["TPM"].sum()
    print("TPM Calculator Result")
    print(df)
    print(f"Total TPM: {total_tpm:.2f}")

    output_path = file_path.parent / "tpm_results.tsv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, sep="\t")
    print(f"Results saved in {output_path}")

if __name__ == "__main__":
    calculate_tpm(data_path)

