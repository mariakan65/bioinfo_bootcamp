library(ggplot2)

set.seed(321)

counts <- matrix(rpois(10000, lambda = 150), nrow = 1000, ncol = 10)
colnames(counts) <- c("Control", "Control", "Control", "Control", "Control", "Treated", "Treated", "Treated","Treated","Treated")
rownames(counts) <- paste0("Gene_", 1:1000)

counts[1:200, 6:10] <- counts[1:200, 6:10] + 100

pca_result <- prcomp(t(counts), scale. = TRUE)
pca_data <- as.data.frame(pca_result$x)
pca_data$Group <- c(rep("Control", 5), rep("Treated", 5))
percentVar <- round(100 * (pca_result$sdev^2 / sum(pca_result$sdev^2)), 1)

pca_plot <- ggplot(pca_data, aes(x = PC1, y = PC2, colour = Group )) +
  geom_point(size = 5) +
  labs(
    title =  "PCA Plot of RNA-Seq Samples",
    x = paste0("PC1: ", percentVar[1], "% variance"),
    y = paste0("PC2: ", percentVar[2], "% variance")
  )


pca_plot
ggsave("Week6/pca_plot.png", pca_plot, width = 7, height = 5)