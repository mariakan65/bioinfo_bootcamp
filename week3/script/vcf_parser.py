import vcfpy

reader = vcfpy.Reader.from_path("C://Users/user/bioinfo_bootcamp/week3/data/sample.vcf")
total_variants = 0
snps = 0
indels = 0
high_quality_variants = 0
for record in reader:
    if not record.ALT:
        continue
    total_variants += 1
    if len(record.ALT[0].value)== 1 and  len(record.REF)==1:
        snps += 1
    elif len(record.ALT[0].value) != len(record.REF):
        indels += 1

    if record.QUAL is not None and  record.QUAL >= 30.0:
        high_quality_variants += 1
print(f"Results of VCF Analysis \nTotal variants: {total_variants}\nSNPs : {snps}\nIndels: {indels}\n"
      f"High Quality Variants(Q >= 30): {high_quality_variants}")