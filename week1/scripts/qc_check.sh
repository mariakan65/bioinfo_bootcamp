#!/bin/bash

FASTA_FILE="$1"

if [ -z "$FASTA_FILE" ]; then
    echo "Error: No FASTA file provided!"
    echo "Usage: ./qc_check.sh <path_to_fasta>"
    exit 1
fi

echo "========================================"
echo " Processing File: $FASTA_FILE"
echo "========================================"

SEQS=$(grep -c "^>" "$FASTA_FILE")
GC=$(grep -v "^>" "$FASTA_FILE" | awk '{total+=length($0); gc+=gsub(/[GCgc]/,"")} END {printf "%.2f", (gc/total)*100}')

echo "Total Sequences : $SEQS"
echo "GC Content (%)  : $GC%"
echo "========================================"
