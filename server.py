from flask import Flask,request,json,render_template
import protoformat_pb2

from src.app import processData

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/jsondata", methods=['GET'])
def jsonData():
    reqData = request.json
    id = reqData['id'],
    benchmarkType = reqData['benchmarkType']
    workloadMetric =reqData['workloadMetric']
    batchUnit = reqData['batchUnit']
    batchID = reqData['batchID']
    batchSize = reqData['batchSize']
    dataType = reqData['dataType']
    dataAnalytics= reqData['dataAnalytics']
    data = processData(id,benchmarkType,workloadMetric,batchUnit,batchID,batchSize,dataType,dataAnalytics)
    return data
    return render_template('json_data.html')

@app.route("/protodata")
def protoData():
    reqData = protoformat_pb2.dataRequest.FromString(request.data)
    batch_response = protoformat_pb2.dataResponse()

    #Parse Request
    id = reqData.RFW_ID,
    id = ''.join(id[0])
    benchmarkType = reqData.benchmark_type
    workloadMetric =reqData.work_metric
    batchUnit = reqData.batch_unit
    batchID = reqData.batch_ID
    batchSize = reqData.batch_size
    dataType = reqData.data_type
    dataAnalytics= reqData.data_analytics
    # print(id,benchmarkType,workloadMetric,batchUnit,batchID,batchSize,dataType,dataAnalytics)

    #Process data
    result = processData(id,benchmarkType,workloadMetric,batchUnit,batchID,batchSize,dataType,dataAnalytics)

    #Add to Proto
    batch_response.RFW_ID = result['RFWID']
    batch_response.last_batch_ID = result['lastBatchID']
    for x in result['dataRequested']:
        batch_response.batch_data.append(x)
    batch_response.data_analytics = result['dataAnalytics']
    searlized_batch_res = batch_response.SerializeToString()
    print(searlized_batch_res)

    mayank = protoformat_pb2.dataResponse.FromString(searlized_batch_res)
    print(mayank)
    return "Data is sent"

if __name__ =="__main__":
    app.run(debug=True)