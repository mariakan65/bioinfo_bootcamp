from Bio import SeqIO
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
input_file = DATA_DIR / "filtered_reads.fastq"


reference = "AGCTTAGCTAGCTAGCGATCGATCGATCGATCCGATCGATCGAT"

def find_sequence(ref_sequence, input_fastq):
    input_path = Path(input_fastq)
    matches = []
    if not input_path.exists():
        print(f"Error:File not found at {input_path}.")
        return matches
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

if __name__ == "__main__":
    results = find_sequence(reference, input_file)
    print(f"Found {len(results)} matching sequences in {input_file.name}")
    for result in results:
        print(f"Read ID: {result['read_id']} | Position: {result['position']}")
