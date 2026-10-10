from Bio import SeqIO
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
input_file = REPO_ROOT / "week1" / "data" / "reads_1.fastq"
output_file = REPO_ROOT / "week2" / "data" / "filtered_reads.fastq"


def clean_fastq(input_fastq, output_fastq, threshold):
    input_path = Path(input_fastq)
    output_path = Path(output_fastq)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"Error: Input file not found at {input_path}")
        return []

    passed_records = []
    total_reads = 0

    for record in SeqIO.parse(input_path, "fastq"):
        total_reads += 1
        score = record.letter_annotations["phred_quality"]
        avg_score = sum(score) / len(score)
        if avg_score >= threshold:
            passed_records.append(record)
        else:
            pass
    with open(output_path, "w") as output_handle:
        SeqIO.write(passed_records, output_handle, "fastq")

    print("--- QC Filtering Results ---")
    print(f"Total reads processed: {total_reads}")
    print(f"Reads passed (Q >= {threshold}): {len(passed_records)}")
    print(f"Filtered file saved at: {output_path}.")

if __name__ == "__main__":
    clean_fastq(input_file, output_file, threshold=20)









