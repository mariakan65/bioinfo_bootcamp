from pathlib import Path
import pandas as pd
file_path = Path("C:/Users/user/bioinfo_bootcamp/week6/data/counts_with_length.tsv")
file_path.parent.mkdir(parents=True, exist_ok=True)


def calculate_tpm(file):
    df = pd.read_csv(file, sep='\t', index_col=0)
    df["Length_kb"] = df["Length_bp"] / 1000
    df["RPK"] = df["Sample_1"] /df["Length_kb"]
    scaling_factor = df["RPK"].sum()/1000000
    df["TPM"] = df["RPK"] / scaling_factor
    total_tpm = df["TPM"].sum()
    print("TPM Calculator Result")
    print(df)
    print(f"Total TPM: {total_tpm:.2f}")

    output_path = file.parent / "tpm_results.tsv"
    df.to_csv(output_path, sep="\t")
    print(f"Results saved in {output_path}")

calculate_tpm(file_path)

