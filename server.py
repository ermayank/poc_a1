from flask import Flask,request,json,render_template
import protoformat_pb2

from app import processData

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/jsondata", methods=['GET', 'POST'])
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


@app.route("/jsonform", methods=['GET', 'POST'])
def jsonForm():
    if request.method == "POST":
       formData = request.form
       id = formData.get("RFWID")
       benchmarkType = formData.get("benchmarkType")
       workloadMetric =formData.get('workloadMetric')
       batchUnit = int(formData.get('batchUnit'))
       batchID = int(formData.get('batchID'))
       batchSize = int(formData.get('batchSize'))
       dataType = formData.get('dataType')
       dataAnalytics= formData.get('dataAnalytics')
       data = processData(id,benchmarkType,workloadMetric,batchUnit,batchID,batchSize,dataType,dataAnalytics)
       print(data)
       return data
   
    # return data
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

    #Process data
    result = processData(id,benchmarkType,workloadMetric,batchUnit,batchID,batchSize,dataType,dataAnalytics)

    #Add to Proto
    batch_response.RFW_ID = result['RFWID']
    batch_response.last_batch_ID = result['lastBatchID']
    for x in result['dataRequested']:
        batch_response.batch_data.append(x)
    batch_response.data_analytics = result['dataAnalytics']
    searlized_batch_res = batch_response.SerializeToString()
    return searlized_batch_res

if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)