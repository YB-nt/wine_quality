from flask import Blueprint, render_template,request
from . import pred

result = Blueprint('result',__name__)

@result.route('/result',methods=['POST','GET'])
def index():
    if(request.method=='POST'):
        req=request.form
        print("req:",req)
    else:
        print("Error")
    
    data=list(req.values())
    print("Data:",data)
    # try:
    result=pred.Predict(data)
    if(int(result)==8 or int(result)==7):
        re='1등급 입니다.'
    elif(int(result)==6 or int(result)==5):
        re='2등급 입니다.'
    elif(int(result)==4 or int(result)==3):
        re='3등급 입니다.'
    else:
        re='결과를 찾을 수 없음'

    # except Exception as e:
    #         print("Error:",e)
    return render_template("result.html",ans=re), 200
