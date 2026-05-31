import os
import pandas
from sklearn import linear_model

original_data = pandas.read_csv("Original_data.csv")
df = pandas.read_csv("Finance_data.csv")

questions = original_data.columns

def genderToNum(x):
    if type(x)!=str:
        if x ==1:
            return "female"
        else:
            return"male"
    else:
        if x == "female":
            return 1
        else:
            return 0

def YesNotoNum(x):
    if type(x)!=str: 
        if x ==1:
            return "yes"
        else:
            return"no"
    if x == "yes":
        return 1
    else:
        return 0
    
def FactorToNum(x):
    if type(x)!=str:
        if x ==1:
            return "Returns"
        elif x ==2:
            return "Locking Period"
        elif x ==3:
            return "Risk"
    if x == "Returns":
        return 1
    elif x == "Locking Period":
        return 2
    elif x == "Risk":
        return 3

def ObjectiveToNum(x):
    if type(x)!=str:
        if x ==1:
            return "Capital Appreciation"
        elif x ==2:
            return "Income"
        elif x ==3:
            return "Growth"
    if x == "Capital Appreciation":
        return 1
    elif x == "Income":
        return 2
    elif x == "Growth":
        return 3
    
def PurposeToNum(x):
    if type(x)!=str:
        if x ==1:
            return "Wealth Creation"
        elif x ==2:
            return "Savings for Future"
        elif x ==3:
            return "Returns"
    if x == "Wealth Creation":
        return 1
    elif x == "Savings for Future":
        return 2
    elif x == "Returns":
        return 3
    
def DurationToNum(x):
    if type(x)!=str:
        if x ==1:
            return "1-3 years"
        elif x ==2:
            return "More than 5 years"
        elif x ==3:
            return "3-5 years"
        elif x ==4:
            return "Less than 1 year"
    if x == "1-3 years":
        return 1
    elif x == "More than 5 years":
        return 2
    elif x == "3-5 years":
        return 3
    elif x == "Less than 1 year":
        return 4
    
def Invest_MonitorToNum(x):
    if type(x)!=str:
        if x ==1:
            return "Monthly"
        elif x ==2:
            return"Weekly"
        else:
            return "Daily"
    if x == "Monthly":
        return 1
    elif x == "Weekly":
        return 2
    else:
        return 3
    
def ExpectToNum(x):
    if type(x)!=str:
        if x ==1:
            return "20%-30%"
        elif x ==2:
            return "10%-20%"
        elif x ==3:
            return "30%-40%"
    if x == "20%-30%":
        return 1
    elif x == "10%-20%":
        return 2
    elif x == "30%-40%":
        return 3

df["gender"] = df["gender"].apply(genderToNum)
df["Investment_Avenues"] = df["Investment_Avenues"].apply(YesNotoNum)
df["Factor"] = df["Factor"].apply(FactorToNum) #change the next three
df["Objective"] = df["Objective"].apply(ObjectiveToNum)
df["Purpose"] = df["Purpose"].apply(PurposeToNum)
df["Duration"] = df["Duration"].apply(DurationToNum)
df ["Invest_Monitor"] = df["Invest_Monitor"].apply(Invest_MonitorToNum)
df["Expect"] = df["Expect"].apply(ExpectToNum)


print(df["Avenue"].unique())
