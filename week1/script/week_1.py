from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


file_path = DATA_DIR / "reads_1.fastq"


fastq_content = """@SRR001.1 HWI-ST286:4:1:1:1146 length=35
NNCCTAAACCCTAAACCCTAAACCCTAAACCCTAA
+
#11DFFFFFGHHHJJIJJIJJJJJIJJJJJJJJJJ
@SRR001.2 HWI-ST286:4:1:1:1189 length=35
ANANCCTAAACCCTAAACCCTAAACCCTAAACCCT
+
#1BDFFFFFFGHHHJJJJJJJJJJJJJJJJJJJJJ
@SRR001.3 HWI-ST286:4:1:1:1143 length=35
NNANCCTAAACCCTAAACCCTAAACCCTAAACCCT
+
#1BDFFFFFFFHHHJJJJJJJJJJJJJJJJJJJJJ
@SRR001.4 HWI-ST286:4:1:1:1195 length=35
TNCCTAAACCCTAAACCCTAAACCCTAAACCCTAA
+
#11DFFFFFFGHHHJJJJJJJJJJJJJJJJJJJJJ
@SRR001.5 HWI-ST286:4:1:1:1122 length=35
ANCCTAAACCCTAAACCCTAAACCCTAAACCCTAA
+
#11DFFFFFFGHHHJJJJJJJJJJJJJJJJJJJJJ
"""

with open(file_path, "w") as f:
    f.write(fastq_content.strip())

print(f"Local file {file_path.name} successfully created at {DATA_DIR}!")
def parse_fastq(filepath):
    filepath = Path(filepath)
    reads = 0
    bases = 0
    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            if i % 4 == 1:
                reads += 1
                bases += len(line.strip())
    average_bases = bases / reads if reads > 0 else 0
    print(f"Total reads: {reads}")
    print(f"Total bases: {bases}")
    print(f"Average bases: {average_bases}")


parse_fastq(file_path)
