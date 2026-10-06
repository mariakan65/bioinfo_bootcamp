from Bio import SeqIO
from pathlib import Path


def clean_fastq(input_fastq, output_fastq, threshold):
    input_fastq = Path(input_fastq)
    output_fastq = Path(output_fastq)

    output_fastq.parent.mkdir(parents=True, exist_ok=True)

    passed_records = []
    total_reads = 0

    for record in SeqIO.parse(input_fastq, "fastq"):
        total_reads += 1
        score = record.letter_annotations["phred_quality"]
        avg_score = sum(score) / len(score)
        if avg_score >= threshold:
            passed_records.append(record)
        else:
            pass
    with open(output_fastq, "w") as output_handle:
        SeqIO.write(passed_records, output_fastq, "fastq")

    print("--- QC Filtering Results ---")
    print(f"Total reads processed: {total_reads}")
    print(f"Reads passed (Q >= {threshold}): {len(passed_records)}")
    print(f"Filtered file saved at: {output_fastq}")
input_file = Path("C:/Users/user/bioinfo_bootcamp/week1/data/reads_1.fastq")
output_file = Path("C:/Users/user/bioinfo_bootcamp/week2/data/filtered_reads.fastq")
clean_fastq(input_file, output_file, threshold=20)








