# retirement-rate-project

```bash
cd /path/to/retirement-rate-project

git add .
git commit -m "プログラムを保存します"
git push origin main
```

```bash
# 起動方法
python userinterface/retirement_controller.py
    
# 社員の退職率を予測する
curl -XPOST "http://localhost:8080/predict" -H "Content-type:application/json" -d '
{
    satisfaction_level = 9.2,
    last_evaluation = 2.2,
    number_project = 6.8 
}
'

退職率の高い社員一覧を表示する
curl -XGET "http://localhost:8080/all" -H "Content-type:application/json" -d '
{
   
}
'
```