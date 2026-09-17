#!/bin/bash
FASTA_FILE=$1

if [ -z "$FASTA_FILE" ]; then
	echo "Error: No Fasta file provided!"
	echo "Usage ./genome_summary <path_to_fasta>"
	exit 1
fi
echo "========================================"
echo " Processing File: $FASTA_FILE"
echo "========================================"


OUTPUT_FILE="../results/summary_report.tsv"

if [ ! -f "$OUTPUT_FILE" ]; then
    echo -e "Sample_Name\tSequences\tTotal_Bases\tGC_Percent" > "$OUTPUT_FILE"
fi

SAMPLE_NAME=$(basename "$FASTA_FILE")
SEQS=$(grep -c "^>" "$FASTA_FILE")
TOTAL=$(grep -v "^>" "$FASTA_FILE" | awk '{total+=length($0)} END {print total}')
GC=$(grep -v "^>" "$FASTA_FILE" | awk '{total+=length($0); gc+=gsub(/[GCgc]/,"")} END {if (total > 0) printf "%.2f", (gc/total)*100; else print "0.00"}')

echo -e "${SAMPLE_NAME}\t${SEQS}\t${TOTAL}\t${GC}" >> "$OUTPUT_FILE"

echo "Processed: $SAMPLE_NAME -> Appended to $OUTPUT_FILE"
