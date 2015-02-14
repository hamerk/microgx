sec_list = ['1.01_F', '1.02_F', '1.03_F', '1.04_F', '1.05_F', '1.06_F', '1.07_F', '1.08_F', '1.01_R', '1.02_R', '1.03_R', '1.04_R', '1.05_R', '1.06_R', '1.07_R', '1.08_R', '1.09_F', '1.10_F', 'FUNGNEGW_F', 'FUNGPOS_F', 'HIDI', 'HIDI', 'HIDI', 'HIDI', '1.09_R', '1.10_R', 'FUNGNEGW_R', 'FUNGPOS_R', 'HIDI', 'HIDI', 'HIDI', 'HIDI']
runum = '1952'
op = 'KH'


dad_text = "\t\t100\tResults_Group\tShort50\tPOP6\t"
text = "\t\t100\tResults_Group\tSHORTSEQPOP7\tPOP7\t"


count = 0
print("Container Name\tDescription\tContainerType\tAppType\tOwner\tOperator\t")
print(runum + "\t\t96-Well\tRegular\tMGX\t" + op + "\t")
print("AppServer\tAppInstance\t")
print("SequencingAnalysis\t")
print("Well\tSample Name\tComment\tPriority\tResults Group 1\tInstrument Protocol 1\tAnalysis Protocol 1\t")

for i in range (1, (len(sec_list)/8)+1):
    if i < 10:
        i = '0' + str(i)
    for x in [chr(a) for a in range(65, 73)]:
        print x + str(i) + '\t' + sec_list[count] \
             + text
        count += 1