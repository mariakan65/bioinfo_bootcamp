# ==============================================================================
# Week 3 Project: ChIP-Seq Peak Annotation & Spatial Genomic Analysis
# Bootcamp: Bioinfo Bootcamp
# ==============================================================================

# 1. Load required libraries

library(GenomicRanges)

library(tidyverse)

# 2. Simulate Genomic Features (Genes & Transcripts)
# Defining target genes on chromosome 1 with strand awareness
genes <- GRanges(
  seqnames = "chr1",
  ranges = IRanges(
    start = c(10000, 25000, 45000, 70000, 95000),
    end   = c(15000, 32000, 52000, 78000, 102000)
  ),
  strand = c("+", "-", "+", "+", "-"),
  gene_id = c("BRCA1", "TP53", "EGFR", "MYC", "PTEN")
)

# 3. Derive Promoter Regions (-2000 bp to +500 bp from TSS)
# Using promoters() function which accounts for strand orientation automatically
promoters_gr <- promoters(genes, upstream = 2000, downstream = 500)

# 4. Simulate ChIP-Seq Peaks Data
set.seed(42)
peaks <- GRanges(
  seqnames = "chr1",
  ranges = IRanges(
    start = c(8500, 23500, 40000, 71000, 90000, 110000),
    width = c(300, 450, 500, 250, 600, 400)
  ),
  peak_id = paste0("Peak_", 1:6),
  score = c(85, 120, 45, 210, 95, 30)
)

# 5. Spatial Overlap Analysis (Find peaks overlapping promoters)
overlaps <- findOverlaps(query = peaks, subject = promoters_gr)

# Extract matching annotated data
annotated_peaks <- data.frame(
  peak_id = mcols(peaks)$peak_id[queryHits(overlaps)],
  peak_score = mcols(peaks)$score[queryHits(overlaps)],
  target_gene = mcols(genes)$gene_id[subjectHits(overlaps)],
  gene_strand = as.character(strand(genes)[subjectHits(overlaps)])
)

print("Annotated Peaks in Promoter Regions:")
print(annotated_peaks)

# 6. Visualization: Peak Scores vs Target Gene Promoters
# Convert GRanges to data frame for ggplot2 integration
peaks_df <- as.data.frame(peaks)
peaks_df$is_promoter_peak <- 1:nrow(peaks_df) %in% queryHits(overlaps)

plot_obj <- ggplot(peaks_df, aes(x = peak_id, y = score, fill = is_promoter_peak)) +
  geom_col(width = 0.6) +
  scale_fill_manual(
    values = c("TRUE" = "#2b8cbe", "FALSE" = "#bdbdbd"),
    labels = c("TRUE" = "Promoter Peak", "FALSE" = "Intergenic/Other")
  ) +
  theme_minimal() +
  labs(
    title = "ChIP-Seq Peak Binding Scores & Promoter Localization",
    subtitle = "Annotation of TF binding sites relative to gene promoter regions",
    x = "ChIP-Seq Peak ID",
    y = "Signal Enrichment Score",
    fill = "Genomic Location"
  )

# Display plot
print(plot_obj)

# 7. Save High-Resolution Plot
ggsave(
  filename = "Week3/chip_seq_promoter_annotation.png", 
  plot = plot_obj, 
  width = 8, 
  height = 5, 
  dpi = 300
)