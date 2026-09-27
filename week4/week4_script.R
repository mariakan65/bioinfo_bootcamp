library(ggplot2)

set.seed(123)
n_genes <- 2000
data <- data.frame(
  gene_id = paste0("Gene_",1:n_genes), 
  log2FoldChange = rnorm(n_genes, mean = 0, sd = 1.5),
  pvalue = runif(n_genes, min = 0, max = 1)
)
data$pvalue[1:100] <- data$pvalue[1:100]/100
head(data)

data$neg_log10_value <- -log10(data$pvalue)
data$status <- "Not Significant"
data$status[data$log2FoldChange > 1 & data$pvalue <0.05] <- "Upregulated"
data$status[data$log2FoldChange < -1 & data$pvalue < 0.05] <- "Downregulated"

data$status <- factor(data$status, levels = c("Upregulated", "Downregulated", "Not Significant"))
table(data$status)
volcano_plot <- ggplot(data, aes(x = log2FoldChange, y = neg_log10_value, colour = status))+
  geom_point(size = 1.5, alpha = 0.6)+
  scale_color_manual(values = c("Upregulated" = "#91003f", "Downregulated" = "#3690c0", "Not Significant" = "#969696"))+
  geom_hline(yintercept = -log10(0.05), linetype = "dashed", color = "black")+
  geom_vline(xintercept = c(-1, 1), linetype = "dashed", color = "black")+
  xlim(-4,4) +
  ylim(0,5) +
  theme_minimal() +
  labs(
  title = "Volcano Plot of Differential Gene Expression",
  x = expression(log[2] ~ "Fold Change"),
  y = expression(-log[10] ~ "(p-value"),
  color = "Status")

print(volcano_plot)

ggsave(filename = "volcano_plot.png",
  plot = volcano_plot,
  width = 8,
  height = 6,
  dpi = 300 )


