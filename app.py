from crypt import methods
from flask import Flask,request,json,render_template

from src.serveJson import processData

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('json_data.html')

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
    # batch_object = RFW_response(id, bench_type, metric, batch_unit, batch_id, batch_size)
    # result = batch_object.send_json_data_results()
    return data

@app.route("/protodata")
def protoData():
    return "<p>This will give ProtoBuff data</p>"

if __name__ =="__main__":
    app.run(debug=True)