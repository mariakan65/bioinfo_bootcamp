from Bio import Align
from pathlib import Path

def analyze_sam(sam_path):
    unmapped_reads = 0
    mapped_reads = 0
    total_reads = 0
    hq_mappings = 0
    with Align.parse(sam_path, "sam") as alignments:
        for alignment in alignments:
            if (alignment.flag & 256) != 0 and (alignment.flag & 2048) != 0:
                continue
            total_reads += 1

            if (alignment.flag & 4) ==  0:
                mapped_reads += 1
            else:
                unmapped_reads += 1
            if alignment.mapq is not None  and alignment.mapq >= 30:
                hq_mappings += 1
    print(f"SAM file analysis completed! Total reads: {total_reads}\nMapped reads: {mapped_reads}\nUnmapped reads: "
              f"{unmapped_reads}\nHigh Quality mappings(QR Score >=30): {hq_mappings}")



sam_file = Path("C://Users/user/bioinfo_bootcamp/week4/data/sample.sam")
analyze_sam(sam_file)

