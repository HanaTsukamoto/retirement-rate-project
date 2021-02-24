
from flask import Flask, request, jsonify
import pandas as pd 
import pickle 
import os.path

app = Flask(__name__)
hr_df = pd.read_csv("./社員データ.csv")
社員データ = hr_df[['satisfaction_level', 'last_evaluation', 'number_project']]
社員ID = hr_df['社員ID']
parent_directory = os.path.dirname(os.path.abspath(__file__))

@app.route('/predict', methods=["POST"])
def predict():
    """
    社員の退職率を予測します。
    社員のデータを受け取って、退職率予測モデルに入力して、退職率を0~100の間で返します。
    """
    url = "http://localhost:8080/predict"
    satisfaction_level =  request.json(url, "satisfaction_level")
    last_evaluation =  request.json(url, "last_evaluation")
    number_project =  request.json(url, "number_project")
    # loaded_model = pickle.load(open("/Users/hana/ml/retirement-rate-project/退職率計算モデル.sav", "rb"))
    loaded_model = pickle.load(open(parent_directory + "/../退職率計算モデル", 'rb'))
    x = [satisfaction_level, last_evaluation, number_project]

    return jsonify({
        "retirement rate": str(loaded_model.predict([x])[0])
        # "retirement rate": str(loaded_model.predict(社員データ)[0])
        #  辞書型に格納されているうち0番目の値をstringとして返す
    })


@app.route('/all', methods=["GET"])
def all():
    """
    退職率の高い社員一覧を表示する
    社員の退職率データを受け取って退職率が75%以上の社員を表示
    """ 
    # loaded_model = pickle.load(open("/Users/hana/ml/retirement-rate-project/退職率計算モデル.sav", "rb"))
    loaded_model = pickle.load(open(parent_directory + "/../退職率計算モデル", 'rb'))
    退職率 = loaded_model.predict_proba(社員データ)[:, 1]
    # print(退職率)
    # loadedmodel print　method の戻り値
    # print(loaded_model.predict_proba(社員データ)[:, 1])
    
    退職率一覧 = {}
    for i in range(len(社員データ)):
       if 退職率[i] >= 0.75:
           退職率一覧[社員ID[i]] = 退職率[i]
                   
    return jsonify({
        "退職率が高い社員一覧": 退職率一覧
    })



if __name__ == "__main__":
    app.run(port=8080, debug=True)