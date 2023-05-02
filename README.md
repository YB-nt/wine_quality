# wine_quality

<br>
### 프로젝트 과정
kaggle dataset (csv)-> google Drive(gdown)-> model(RandomForest) -> Flask
                                          -> database(sqlite) 
<br><br>                                          

### 프로젝트 내용

- 케글에서 불러온 데이터를 google Drive 에 업로드 하고 gdown을 사용하여 데이터를 불러오기
<br><br>
- sklearn을 활용하여 불러온 데이터를 통해서 모델(RandomForest)을 만들어 주고 joblib를 이용하여  피클링을 진행하였다.
<br><br>
- 불러온 데이터를 추가적으로 데이터베이스에 적재 시켜주었다. 
<br><br>
- Flask를 사용하여 웹페이지를 구성하고 피클링된 모델을 사용하여서 와인 정보를 입력하면 와인의 등급을 확인할 수 있도록 만들어 주었다.
