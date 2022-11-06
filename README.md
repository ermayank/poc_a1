
# Programming on Cloud - Assignment 1

# Problem Statement

This assignment aims to practice the concepts, and techniques for data models and the communications for resources represented by data models. 

The data set is from a Github project, under the directory of Workload Data.  

[Workload Data Link](https://github.com/haniehalipour/Online-Machine-Learning-for-Cloud-Resource-Provisioning-of-Microservice-Backend-Systems)

The workload data contains the workload generated from two industrial benchmarks NDBench from Netflix andDell DVD store from Dell. Both benchmarks are deployed on a cluster of cloud VMs on AWS and Azure clouds.  The workload has been split to training sets and testing sets for machine learning purpose. 

In each of the workload file, the first 4 columns containthe following attributes.

CPUUtilization_Average,NetworkIn_Average,NetworkOut_Average,MemoryUtilization_Average

In this assignment, please developa client/server program to servea“workload query”scenario. In this scenario,  a client sends a ‘Request For Workload (RFW)’,  and the server replies an ‘Response for Data (RFD)’for each conversation.  

The client’s RFW includes:

    1. RFWID
    2. Benchmark Type (such as DVD store or NDBench)
    3. Workload Metric (such as CPU or NetworkIn or NetworkOut or Memory)
    4. Batch Unit (the number of samples contained in each batch, such as 100)
    5. Batch ID (such as the 1stor 2ndor... 5thBatch)
    6. Batch Size (such as the how many batches to return, 5 means 5 batches to return) 
    7. Data Type (training data or testing data)
    8. Data analytics ( 10p, 50p, 95p, 99p, avg, std, max, min), for example 50p means 50th percentile

The server’s RFD reply includes: 

    1. RFWID
    2. The last Batch ID
    3. The data samples requested
    4. The data analytics

This assignment is responsible for the design of the data model, and implementation of the data communication. There is no need to develop a full-fledged database system. Data can be stored in files or any kinds of storage, such as relational databases or nosql databases. 

## Technical Requirement
### 1. Data Communication
The data should be communicated between the client and server through data serialization/deserialization in two methods, namely text based (de)-serialization and binary (de)-serialization.For example,(1) XML orJSON can be used fortext based (de)-serialization.(2) Protocol Buf or Thrift can be used for binary (de)-serialization.For each method, your program should be able to retrieve the samples requested for each RFW. 

### 2. Programming Language
You can program this application in any language.

### 3. Application 
Your client/server can be a standalone program or you build on any software framework that supports client/server. You can choose the protocol your prefer TCP, or HTTP. 

# Solution
The client-server application’s functionality is shown in the produced result. The client can send a workload query byproviding  the  necessary  input  parameters.  JSON  and  Protobufare the two forms of serialisation and de-serialization used by the program.  We  have  utilised  various  data  models  to  describe  the client request and the server answer in accordance with each typeof serialisation.Additionally, it describes the technological setup,software  programs,  and  libraries  required  to  create  the  client-server  application.  

In  addition,  we  have  set  up  our  applicationon  an  Amazon  Web  Services  (AWS)  EC2  machine,  using Docker.

### JSON Data Model

For  JSON  based  serialization  and  de-serialization  we have used JSON data model. At the client side the query is modelled as  python  dictionary  which  is  similar  to  JSON  Object.  It has  the  parameters  entered  by  the  client  such  as  RFW  ID,Benchmark  Type,  Workload  Metric,  Batch  Unit,  Batch  ID,Batch  Size,  Data  Type,  Data  analytics.  The  JSON  object having the query parameters at the client side is shown below:

    {
    "id": "1112",
    "benchmarkType": "DVD",
    "workloadMetric": "NetworkIn_Average",
    "batchUnit": 3,
    "batchID": 2,
    "batchSize": 3,
    "dataType": "training",
    "dataAnalytics": "avg"
    }

### ProtoBuf Data Model

    syntax = "proto3";
    
    message dataRequest{
        string RFW_ID =1;
        string benchmark_type = 2;
        string work_metric =3;
        int32 batch_unit =4;
        int32 batch_ID= 5;
        int32 batch_size =6;
        string data_type =7;
        string data_analytics =8;
        }
    message dataResponse{
        string RFW_ID = 1;
        int32 last_batch_ID = 2;
        repeated double batch_data =3[packed=true];
        double data_analytics =4;
        }

## Run the Code

To this this project
- Pull Docker Image from docker hub using
```bash
  docker  pull  mguptaca/asn:flask-container
```
- Run docker Image using the following command. 
You can map any of the port at your host machine in this case 80 to port exposed by the container i.e. 5000.
```bash
  docker run -p 80:5000 mguptaca/asn:flask-container
```


## Authors

- [@ermayank](https://www.github.com/ermayank)
- [@attarkousar](https://www.github.com/attarkousar)

