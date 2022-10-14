import pandas as pd
import math
import json

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
    finalRes = {
        "RFWID":id,
        "lastBatchID": lastBatchId,
        "dataRequested": finalData,
        "dataAnalytics":"abhi baki che"
    }

    return finalRes