"""Lab Assignment"""
import pandas as pd
from collections import  Counter
import numpy as np
import random
import scipy.stats as stat
from wordcloud import WordCloud
import matplotlib.pyplot as plt

"""Question 1 : Takes Close to 180 Seconds"""

print("Solution for Question 1 (ETA 185 Seconds): \n")
x = []
y = []
areaForCount = 0
N = 10000000
for _ in range(1, N):
    x = (random.uniform(0, 1))
    y = (random.uniform(0, 1))
    func = np.round(np.e**(-(x**2)/2), 5)
    if func > y:
        areaForCount = areaForCount+1

print("From Points", areaForCount/N)


print("From Standard Normal", stat.norm(0, 1).cdf(1))



"""
from scipy.integrate import quad

def integrand(x):
    return np.e**(-(x**2)/2)

ans, err = quad(integrand, 0, 1)

print(ans)
"""

"""Question 2 : Prime numbers less than 1000"""

print("Solution for question 3:\n")

n = 1
while n < 1000:
    isComposite = 0
    for i in range(2, (n-1)):
        if n % i == 0:
            isComposite = 1

    if isComposite != 1:
        print(n)
    n = n + 1



"""Question 3 : The Purpose of this code is to import dataset and analyse"""
print("Solution for Q 3: \n")

"""a."""
titanicWeight = pd.read_csv("/Users/arunprakash/Downloads/titanic_wt.csv")


titanicData = pd.read_csv("/Users/arunprakash/Downloads/titanic_data.csv")

titanicData["Weight"] = titanicWeight["Weight"]

MissingSeries = titanicData.isnull().sum()

"""b."""
print("Columns with missing values", list(titanicData.columns[titanicData.isnull().any()]))

"""Replacing Missing Values for Weight and age"""
titanicData["Weight"].fillna(titanicData["Weight"].mean(), inplace=True)
titanicData["Age"].fillna(titanicData["Age"].mean(), inplace=True)

""" c. """
#number of survived and npnsurvived by class
FirstSurvived = len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 1)])
FirstNot = len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 0)])

secondSurvived = len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 1)])
secNot = len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 0)])

ThirdSurvived = len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 1)])
ThirdNot = len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 0)])


df = pd.DataFrame([['Survived','First',FirstSurvived],['Survived','Second',secondSurvived],['Survived','Third',ThirdSurvived],['Not Survived','First',FirstNot],
                   ['Not Survived','Second', secNot],['Not Survived','Third', ThirdNot]],columns=['group','column','val'])

df.pivot("column", "group", "val").plot(kind='bar')
plt.title('Number Survived and Not Survived by class')
plt.show()

## Survival probability by class
FirstClass = 100 * len(titanicData[(titanicData.Pclass == 1) & (titanicData["Survived"] == 1)])/len(titanicData)
SecondClass = 100 * len(titanicData[(titanicData.Pclass == 2) & (titanicData["Survived"] == 1)])/len(titanicData)
ThirdClass = 100 * len(titanicData[(titanicData.Pclass == 3) & (titanicData["Survived"] == 1)])/len(titanicData)

data = {
    'First': FirstClass,
    'Second': SecondClass,
    'Third' : ThirdClass
}
plt.bar(data.keys(), data.values())
plt.title("Survival Probability By Class")
plt.show()




"""d."""
FirstMale = 100 * len(titanicData[(titanicData.Pclass == 1) & (titanicData.Sex == "male") & (titanicData["Survived"] == 1)])/len(titanicData[(titanicData.Pclass == 1) & (titanicData.Sex == "male")])
FirstFemale = 100 * len(titanicData[(titanicData.Pclass == 1) & (titanicData.Sex == "female") & (titanicData["Survived"] == 1)])/len(titanicData[(titanicData.Pclass == 1) & (titanicData.Sex == "female")])

SecondMale = 100 * len(titanicData[(titanicData.Pclass == 2) & (titanicData.Sex == "male") & (titanicData["Survived"] == 1)])/len(titanicData[(titanicData.Pclass == 2) & (titanicData.Sex == "male")])
SecondFemale = 100 * len(titanicData[(titanicData.Pclass == 2) & (titanicData.Sex == "female") & (titanicData["Survived"] == 1)])/len(titanicData[(titanicData.Pclass == 2) & (titanicData.Sex == "female")])

ThirdMale = 100 * len(titanicData[(titanicData.Pclass == 3) & (titanicData.Sex == "male") & (titanicData["Survived"] == 1)])/len(titanicData[(titanicData.Pclass == 3) & (titanicData.Sex == "male")])
ThirdFemale = 100 * len(titanicData[(titanicData.Pclass == 3) & (titanicData.Sex == "female") & (titanicData["Survived"] == 1)])/len(titanicData[(titanicData.Pclass == 3) & (titanicData.Sex == "female")])



df = pd.DataFrame([['male','First',FirstMale],['male','Second',SecondMale],['male','Third',ThirdMale],['female','First',FirstFemale],
                   ['female','Second', SecondFemale],['female','Third', ThirdFemale]],columns=['group','column','val'])

df.pivot("column", "group", "val").plot(kind='bar')
plt.title('Probability of Survival by class and gender')
plt.show()


"""e. """
out = pd.cut(titanicData["Age"], bins=[0, 18, 25, 40, 60, 100], include_lowest=False)
print(out)
titanicData["AgeBin"] = out

tit = titanicData[titanicData["Survived"]==1].groupby('AgeBin')['AgeBin'].count()
print(tit)

tit.plot(kind="bar")
plt.title("Number Survived by Age Group")
plt.show()


"""f."""

print("the number of survivors and the probability of survival is subject to Age, Class and Gender")

"""Question 4."""
"""a."""
print("Solution for Question 4: \n")
collegesDataset = pd.read_csv("/Users/arunprakash/Downloads/College.csv")
collegesDataset = collegesDataset.rename(columns={'Unnamed: 0':'University Name'})

collegesDataset = collegesDataset.set_index('University Name', drop=True)
print(collegesDataset.head(6))

"""b."""


privateUniversities = collegesDataset[collegesDataset.Private == 'Yes']

publicUniversities = collegesDataset[collegesDataset.Private == 'No']

privateUniversitiesWitAtleast50Criteria = privateUniversities[privateUniversities.Top25perc > 50]
publicUniversitiesWithAtleast50Criteria = publicUniversities[publicUniversities.Top25perc > 50]

print(publicUniversitiesWithAtleast50Criteria.head(6))

"""c. """

data = {
    'Private': len(privateUniversitiesWitAtleast50Criteria),
    'Public': len(publicUniversitiesWithAtleast50Criteria)
}

plt.bar(data.keys(), data.values())
plt.title("Comparisan between public and privates Criterias - Bar Plot")
plt.show()


plotData = [privateUniversitiesWitAtleast50Criteria["Top25perc"],publicUniversitiesWithAtleast50Criteria["Top25perc"]]
plt.boxplot(x=plotData)
plt.title("Comparisan in terms of BoxPlot")
plt.xticks([1, 2], ['private', 'public'])
plt.show()

"""d. """

print("There Exists very little differences between the top25% student ratio in Private and Public Colleges, which is observed from box plotss!")

"""Question 5: Word Counter """
"""The contents are stored in a txt file"""

print("Question 5:")

file = open(r"/Users/arunprakash/Downloads/text.txt", "r", encoding="utf-8-sig")
textFile = file.read().replace(".", "").replace(",", "")
wordcount = Counter(textFile.split())
words = wordcount.items()

wordsToRemove = ['a', 'an', 'the', 'in', 'on', 'and', 'or', 'with', 'he', 'she', 'his', 'her', 'their', 'where', 'to', 'will', 'would', 'at', 'have', 'is', 'was', 'be', 'were', 'of', 'which', 'there', 'for']

for i in range(0, len(wordsToRemove)):
    if wordcount[wordsToRemove[i]]:
        wordcount.pop(wordsToRemove[i])


print("the File :", wordcount.items())

print("Formatted Display")
for item in wordcount.items():
    print("{}\t{}".format(*item))

"""For the Sake of Visualization"""


wordcloud = WordCloud(width=1800, height=800, colormap="Oranges_r").generate(textFile)

# plot the WordCloud image
plt.figure()
plt.title("WordCount Visualization")
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

