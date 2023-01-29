from flask import Flask, jsonify, request
import requests
import math

response = ''
app = Flask(__name__)

part_index=["코","목","오른쪽 어깨","오른쪽 팔꿈치","오른쪽 손목","왼쪽 어깨",
           "왼쪽 팔꿈치","왼쪽 손목","오른쪽 엉덩이","오른쪽 무릎","오른쪽 발목",
           "왼쪽 엉덩이","왼쪽 무릎","왼쪽 발목","오른쪽 눈","왼쪽 눈","오른쪽 귀",
           "왼쪽 귀"]

#based on the image, send_pose_est returns array of size 3
#First element is shoulder/height ratio
#second one is lower body / height ratio
#thrid one is upper bofdy / height ratio
@app.route('/', methods = ['GET', 'POST'])
def send_pose_est(path):
    global response
    if (request.method == 'GET'):
        return jsonify({'img' : response})
    
    url = "https://naveropenapi.apigw.ntruss.com/vision-pose/v1/estimate"
    client_id = "b41bfdqmg1"
    client_secret = "AHCHw93NO8yHc6vcIOmBrhdbhzKN87NVP4akyVEF"
    files = {'image':open(path,'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,files=files,headers=headers)
    rescode = response.status_code

    if(rescode==200):
        print("Successed")
        response_json = response.json()
        response_dict=dict(response_json['predictions'][0])
        print(response_dict)
        return [shoulder_height_ratio(response_dict),lower_height_ratio(response_dict),upper_height_ratio(response_dict)]

    else:
        print("Failed")
        return -1

#calculate shoulder/height and return, except error happens
def shoulder_height_ratio(response_dict):
    try:
        shoulder_width = response_dict["5"]["x"] - response_dict["2"]["x"]
        height =  response_dict["10"]["y"]-response_dict["0"]["y"]
        print(shoulder_width/height)
        if(shoulder_width/height<0) :
            return -1
        return shoulder_width / height
    except:
        return shoulder_height_sub(response_dict)
        

def shoulder_height_sub(response_dict):
    try:
        shoulder_width = response_dict["5"]["x"] - response_dict["2"]["x"]
        height =  response_dict["13"]["y"]-response_dict["0"]["y"]
        print(shoulder_width/height)
        if(shoulder_width/height<0) :
            return -1
        return shoulder_width / height
    except:
        return -1

def lower_height_ratio(response_dict):
    try:
        lower =  response_dict["10"]["y"] - response_dict["8"]["y"]
        height = response_dict["10"]["y"]-response_dict["0"]["y"]
        print(lower/height)
        if(lower/height<0) :
            return -1
        return lower/height
    except:
        return lower_height_sub(response_dict)

def lower_height_sub(response_dict):
    try:
        lower =  response_dict["13"]["y"] - response_dict["11"]["y"]
        height = response_dict["13"]["y"]-response_dict["0"]["y"]
        print(lower/height)
        if(lower/height<0) :
            return -1
        return lower/height
    except:
        return -1

def upper_height_ratio(response_dict):
    try:
        upper =  response_dict["8"]["y"] - response_dict["1"]["y"]
        height = response_dict["10"]["y"]-response_dict["0"]["y"]
        print(upper/height)
        if(upper/height<0) :
            return -1
        return upper/height
    except:
        return upper_height_sub(response_dict)

def upper_height_sub(response_dict):
    try:
        upper =  response_dict["11"]["y"] - response_dict["1"]["y"]
        height = response_dict["13"]["y"]-response_dict["0"]["y"]
        print(upper/height)
        if(upper/height<0) :
            return -1
        return upper/height
    except:
        return -1

#어깨가 넓음 0.35

def type_check(path):
    score = send_pose_est(path)
    type_score = 0
    if(score[0]>0.35):
         type_score+=1
    else :
        type_score-=1

    if(abs(score[2]-0.4)<0.4):
        type_score=0
    return type_score+1



if __name__ == "__main__":
    app.run(debug=True)
    result  = type_check("24.jpg")
    type_string = ["Wave","Straight","Natural"]
    print(type_string[result])