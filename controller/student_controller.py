from flask import Response, Blueprint, jsonify,json
from service.student_service import StudentService
from util.util_encoder import UtilEncoder

app_student = Blueprint("app_student",__name__)

@app_student.route('/student/all')
def get_all_students():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_all_students(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )
    #return jsonify(student_service.get_all_students_dict())


@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_students_by_gender(gender):
    student_service = StudentService()
    return str(student_service.get_percentage_students_by_gender(int(gender)))

@app_student.route('/student/per_students_job_avgsalario/<gender>')
def get_percentage_students_job_avg_salary(gender):
    student_service = StudentService()
    return jsonify(student_service.get_percentage_students_job_avg_salary(int(gender)))

@app_student.route('/student/get_salary_students/<gender>/<salary>')
def get_salary_students(gender, salary):
    student_service = StudentService()
    return jsonify(student_service.get_salary_students(int(gender),int(salary)))

@app_student.route('/student/salario_mayor/<gender>')
def get_most_payed(gender):
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_most_payed(int(gender)), cls=UtilEncoder)
                    , mimetype="application/json")

@app_student.route("/student/determinar_salario/<rangoMin>/<rangoMax>")
def determinar_salario(rangoMin,rangoMax):
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.determinar_salario(int(rangoMin),int(rangoMax)), cls=UtilEncoder)
                    , mimetype="application/json")

@app_student.route('/student/promSalarial/<gender>')
def prom_salarial(gender):
    student_service = StudentService()
    return str(student_service.prom_salarial(int(gender)))

@app_student.route('/student/edad_promedio')
def edad_promedio():
    student_service = StudentService()
    return str(student_service.edad_promedio())

@app_student.route('/student/get_zona_rural_encima_prom')
def get_zona_rural_encima_prom():
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_zona_rural_encima_prom(),cls=UtilEncoder)
                    , mimetype="application/json")

@app_student.route('/student/get_students_by_city')
def get_students_by_city():
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_students_by_city(),cls=UtilEncoder)
                    , mimetype="application/json")

