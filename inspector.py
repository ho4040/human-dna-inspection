
def check_AGA(df):
    print("AGA Paper https://www.ncbi.nlm.nih.gov/pubmed/18385763 \n")
    print("rs1385699", df[(df["#CHROM"] == 'chrX') & (df['ID'] == 'rs1385699') ])
    print("rs1352015", df[(df["#CHROM"] == 'chrX') & (df['ID'] == 'rs1352015') ])
    
    print("\n\n")
    print("Related gene with EDA2R (https://www.genecards.org/cgi-bin/carddisp.pl?gene=EDA2R)\n")
    # Gene : EDA
    # 68835911..69259322 (https://www.ncbi.nlm.nih.gov/gene/1896)
    snp_on_EDA = df[(df['#CHROM'] == 'chrX') & (df['POS'] >= 68835911) & (df['POS'] <= 69259322)].groupby(by='ANN[*].EFFECT')['ANN[*].EFFECT'].count()
    # Gene : TRAF6 
    # 36505317..36531863 (https://www.ncbi.nlm.nih.gov/gene/?term=NM_001199427)
    snp_on_TRAF6 = df[(df['#CHROM'] == 'chr11') & (df['POS'] >= 36505317) & (df['POS'] <= 36531863)].groupby(by='ANN[*].EFFECT')['ANN[*].EFFECT'].count()
    
    print("EDA\n", snp_on_EDA)
    print("\n")
    print("TRAF6\n", snp_on_TRAF6)

