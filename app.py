import pandas as pd
import numpy as np

#Function to calculate Average of the Data
def calculateAvg(data):
    return sum(data)/len(data)

#Function to calculate Maximum value of the Data
def calculateMin(data):
    return min(data)

#Function to calculate Minimum value of the Data
def calculateMax(data):
    return max(data)

#Function to calculate Standard Deviation of the Data
def calculateStd(data):
    avg = calculateAvg(data)
    var = sum((x-avg)**2 for x in data) / len(data)
    std = var**0.5
    return std

#Function to calculate percentile
def calculatePercentile(data, value):
    np.percentile(data, value)


def processData(id,benchmarkType,workloadMetric,batchUnit,batchID ,batchSize,dataType ,dataAnalytics):
    # Data sheet to process string
    str = f'{benchmarkType}-{dataType}.csv'  
    url = f'https://raw.githubusercontent.com/haniehalipour/Online-Machine-Learning-for-Cloud-Resource-Provisioning-of-Microservice-Backend-Systems/master/Workload%20Data/{str}'
    df = pd.read_csv(url)
    #Length of data
    dataLength = len(df)  
    #Total Number of Batches = Last batch ID
    lastBatchId = batchID + batchSize - 1
    #Col to Process
    df = df[workloadMetric]
    startingPoint = ((batchID - 1) * batchUnit)
    endingPoint = startingPoint + (batchSize * batchUnit)
    finalData = df.iloc[startingPoint:endingPoint].tolist()

    match dataAnalytics:
        case "avg":
            dataAnalysis = calculateAvg(finalData)
        case "min":
            dataAnalysis = calculateMin(finalData)
        case "max":
            dataAnalysis = calculateMax(finalData)
        case "std":
            dataAnalysis = calculateStd(finalData)
        case _:
            dataAnalysis = calculatePercentile(finalData, int(dataAnalytics))


    finalRes = {
        "RFWID":id,
        "lastBatchID": lastBatchId,
        "dataRequested": finalData,
        "dataAnalytics":dataAnalysis
    }
    return finalRes