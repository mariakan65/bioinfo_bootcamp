from Bio import SeqIO
from pathlib import Path

reference = "AGCTTAGCTAGCTAGCGATCGATCGATCGATCCGATCGATCGAT"

def find_sequence(ref_sequence, input_fastq):
    input_path = Path(input_fastq)
    matches = []
    for record in SeqIO.parse(input_path, "fastq"):
        seq = str(record.seq)
        match_position = ref_sequence.find(seq)
        if match_position != -1:
            matches.append({
                "read_id": record.id,
                "position": match_position,
                "sequence": seq
            })
    return matches
input_file = Path("C:/Users/user/bioinfo_bootcamp/week2/data/filtered_reads.fastq")

results = find_sequence(reference, input_file)
print(f"Found {len(results)} sequences in {input_file}")
for result in results:
    print(f"Read ID: {result['read_id']} | Position: {result['position']}")