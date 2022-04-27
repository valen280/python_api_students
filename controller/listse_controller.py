from flask import Response, Blueprint, jsonify,json,request
from service.listse_service import ListSE_Service
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)
list_se_service = ListSE_Service()
@app_list_se.route('/list_se/all')
def get_all_users():

    return Response(status=200, response=json.dumps(list_se_service.get_all_students(), cls=UtilEncoder),
                    mimetype="application/json")

@app_list_se.route('/list_se',methods=['POST'])
def save_student():
    data = request.json
    try:
        list_se_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=200,response=json.dumps({"message":str(e)}),
                    mimetype="application/json")

@app_list_se.route('/list_se/addtostart',methods=['POST'])
def save_student_to_start():
    data = request.json
    try:
        list_se_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=200,response=json.dumps({"message":str(e)}),
                    mimetype="application/json")

@app_list_se.route('/list_se/invert')
def invert():
    return Response (status=200, response = json.dumps(list_se_service.invert(), cls=UtilEncoder),
                    mimetype="application/json")

@app_list_se.route('/list_se/changeXtrems')
def changeXtrems():
    return Response (status=200, response = json.dumps(list_se_service.changeXtremes(), cls=UtilEncoder),
                    mimetype="application/json")

@app_list_se.route('/list_se/deletedata/<identification>')
def deletedata(identification):
    return Response (status=200, response = json.dumps(list_se_service.deletedata(id).deletedata(identification), cls=UtilEncoder),
                    mimetype="application/json")
