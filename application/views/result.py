from flask import Blueprint, render_template,request
from . import pred

result = Blueprint('result',__name__)

@result.route('/result',methods=['POST','GET'])
def index():
    req=request.form
    data=list(req.values())
    try:
        ans=pred.Predict(data)
        if(int(ans)==6):
            re='1등급 입니다.'
        elif(int(ans)==5):
            re='2등급 입니다.'
        elif(int(ans)==4):
            re='3등급 입니다.'
        elif(int(ans)==3):
            re='4등급 입니다.'
        else:
            re='5등급 입니다.'

    except ValueError:
            re='값을 다시 입력 해주세요.'
    return render_template("result.html",ans=re), 200
