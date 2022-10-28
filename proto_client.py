import protoformat_pb2, requests

batch_request_data = protoformat_pb2.dataRequest()


# id= input('Enter Request For Workload (RFW) ID:')
# benchmarkType=input('type one of the following:\n 1. DVD\n 2. NDBench\n')
# workloadMetric=input('type one of the metrics from the following:\n'
#                '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
#                ' 4. MemoryUtilization_Average\n')
# batchUnit=int(input('Enter the number of samples you want in one batch in integer: \n'))
# batchID=int(input('Enter the Batch Id (from which batch you want the data to start from in integer): \n'))
# batchSize=int(input('Enter the number of batches to be returned in integer: \n'))
# dataType=(input('Enter the type of batch: \n 1. testing\n 2. training\n'))
# dataAnalytics=input('Enter the Type of Analysis you want: \n')


# batch_request_data.RFW_ID =id
# batch_request_data.benchmark_type = benchmarkType
# batch_request_data.work_metric =workloadMetric
# batch_request_data.batch_unit =batchUnit
# batch_request_data.batch_ID= batchID
# batch_request_data.batch_size =batchSize
# batch_request_data.data_type =dataType
# batch_request_data.data_analytics =dataAnalytics

batch_request_data.RFW_ID ='123'
batch_request_data.benchmark_type = 'DVD'
batch_request_data.work_metric ='CPUUtilization_Average'
batch_request_data.batch_unit = 2
batch_request_data.batch_ID= 2
batch_request_data.batch_size =2
batch_request_data.data_type ='testing'
batch_request_data.data_analytics ='avg'


print(f"binary: {batch_request_data.SerializeToString()}")
res = requests.get("http://127.0.0.1:5000/protodata", headers={'Content-Type': 'application/protobuf'},data=batch_request_data.SerializeToString())
print("request sent")

# batch_response = protoformat_pb2.Data_Response.FromString(res.content)
# file = open('Proto_DataLog', "wb")
# file.write(res.content)
# file.close()

# print(batch_response)
