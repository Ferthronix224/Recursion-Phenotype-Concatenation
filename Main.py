phenotype = [['MP2'], '(', [['Log'], '(', [['Sqr'], '(', ['lg'], ')'], ')'], ')']

def phenotype_str_concatenation(phenotype):
    phenotype_str = ''
    for i in range(len(phenotype)):
        if len(phenotype[i]) == 1:
            if type(phenotype[i][0]) is str:
                phenotype_str += phenotype[i][0]
        elif len(phenotype[i]) > 1:
            for ii in range(len(phenotype[i])):
                if type(phenotype[i][ii]) is list:
                    phenotype_str += phenotype_str_concatenation([phenotype[i][ii]])
                if type(phenotype[i][ii]) is str:
                    phenotype_str += phenotype[i][ii]
    return phenotype_str

print(phenotype_str_concatenation(phenotype))
