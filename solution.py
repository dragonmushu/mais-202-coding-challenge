import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def openCSVasDF(file):
    return pd.read_csv(file)

def getAverageInterestRates(df):
    differentPurposes = {row['purpose'] for index, row in df.iterrows()}
    averageInterestRates = {key:round(np.mean(df.loc[df['purpose'] == key]['int_rate']), 3)  for key in differentPurposes}
    xLabels = sorted(averageInterestRates.keys())
    yValues = [averageInterestRates[key] for key in xLabels]
    interestRatesDF = pd.DataFrame({'purpose': xLabels, 'avg_rate': yValues})
    interestRatesDF = interestRatesDF[['purpose', 'avg_rate']]
    return interestRatesDF

def tabulate(df):
    fig, ax = plt.subplots()
    ax.axis('off')
    plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

def plotBar(df):
    ax = df.plot(x='purpose', y='avg_rate', kind='bar', title='Average Interest Rates for Different Purposes')
    ax.set_xlabel("Purpose")
    ax.set_ylabel("Average Interest Rate")
    plt.tight_layout()

data = openCSVasDF('data.csv')
averages = getAverageInterestRates(data)
print(averages)
tabulate(averages)
plotBar(averages)
plt.show()
