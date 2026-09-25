library(tidyverse)
cancer_data <- data.frame(
  gene = c("BRCA1", "TP53", "EGFR", "MYC", "PTEN", "KRAS",
           "BRCA1", "TP53", "EGFR", "MYC", "PTEN", "KRAS",
           "BRCA1", "TP53", "EGFR", "MYC", "PTEN", "KRAS"),
  cancer_type = c(rep("Breast", 6), rep("Lung", 6), rep("Colon", 6)),
  expression = c(12.5, 4.2, 8.1, 15.0, 2.1, 9.4,
                 3.1, 14.2, 18.5, 6.2, 8.0, 12.1,
                 5.4, 9.8, 4.2, 11.3, 1.5, 16.8),
  is_mutated = c(TRUE, FALSE, TRUE, FALSE, TRUE, FALSE,
                 FALSE, TRUE, TRUE, FALSE, FALSE, TRUE,
                 FALSE, TRUE, FALSE, TRUE, TRUE, TRUE)
)

cancer_data

filtered_data <- cancer_data %>% 
  filter(is_mutated == TRUE) %>% 
  mutate(log_expr = log2(expression)) %>% 
  select(gene, cancer_type, log_expr) %>% 
  arrange(desc(log_expr))

filtered_data

ggplot(filtered_data, aes(x = gene, y = log_expr, fill = cancer_type)) +
  geom_col(position = "dodge") +
  scale_fill_manual(values = c("Breast" = "#c994c7", "Lung" = "#c51b8a", "Colon" = "#756bb1")) +
  theme_minimal() +
  labs(
    title = "Log2 Expression of Mutated Genes Across Cancers",
    x = "Gene Symbol",
    y = "Log2 Expression",
    fill = "Cancer Type"
  )

ggsave("mutated_genes_expression.png", width = 7, height = 5, dpi = 300)
