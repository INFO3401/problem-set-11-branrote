import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 1. What statistical test would you use for the following scenarios?

# (a) Does a student's current year (e.g., freshman, sophomore, etc.) effect their GPA?
    # Turkey's HSD
# (b) Has the amount of snowfall in the mountains changed over time?
    # T Test
# (c) Over the last 10 years, have there been more hikers on average in Estes Park in the spring or summer?
    # T Test
# (d) Does a student's home state predict their highest degree level?
    # Anova

# Extract the data. Return both the raw data and dataframe
def generateDataset(filename):
    data = pd.read_csv(filename)
    df = data[0:]
    df = df.dropna()
    return data, df

# Run a T test
def runTTest(ivA, ivB, dv):
    ttest = scipy.stats.ttest_ind(ivA[dv], ivB[dv])
    print(ttest)

def runAnova(data, formula):
    model = ols(formula, data).fit()
    aov_table = sm.stats.anova_lm(model, typ=2)
    print(aov_table)

# Run the Analysis
rawData, df = generateDataset('simpsons_paradox.csv')

print("Does gender correlate with adissions?")
men = df[(df['Gender']=='Male')]
women = df[(df['Gender']=='Female')]
runTTest(men, women, 'Admitted')

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData, simpleFormula)

print("Do gender and department correlate with admissions?")
moreComplex = 'Admitted ~ C(Department) + C(Gender)'
runAnova(rawData, moreComplex)

print(df.'simpsons_paradox'())
