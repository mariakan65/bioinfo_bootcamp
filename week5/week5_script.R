library(pheatmap)
set.seed(456)
counts_matrix <-matrix(rpois(400, lambda = 120), nrow = 50, ncol = 8)
rownames(counts_matrix) <- paste0("Gene_", 1:50)
colnames(counts_matrix) <- c("Ctrl_1", "Ctrl_2", "Ctrl_3", "Ctrl_4", "Treat_1", "Treat_2", "Treat_3", "Treat_4")

counts_matrix[1:15, 5:8] <- counts_matrix[1:15, 5:8] + 180
counts_matrix[16:30, 5:8] <- pmax(10, counts_matrix[16:30, 5:8] - 80)


annotation_col <- data.frame(
  Condition = factor(c("Control", "Control", "Control", "Control",
                       "Treated", "Treated", "Treated", "Treated"))
)
rownames(annotation_col) <- colnames(counts_matrix)

pheatmap(
  counts_matrix,
  filename = "week5/heatmap_plot.png",
  scale = "row",
  annotation_col = annotation_col,
  cluster_rows = TRUE,
  cluster_cols = TRUE,
  show_colnames = TRUE,
  show_rownames = FALSE,
  main = "RNA-Seq Heatmap with Sample Annotation"
)

