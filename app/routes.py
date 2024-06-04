from flask import render_template,request
from . import create_app
from joblib import load
import numpy as np


app = create_app()

def prediction(data,model='random-forest'):
    
    Model = load(f'./models/{model}')
    
    prediction = Model.predict(data)
    
    return prediction



@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/predict', methods=['POST'])
def predict():
    
    model = request.form['model']
    
    gender = request.form['gender']
    
    age = request.form['age']
    
    hypertension = request.form['hypertension']
    
    heart_disease = request.form['heart_disease']
    
    # Yes = 1 , No = 0
    married = request.form['married']
    
    #Private = 2, Self-employed = 3, Govt_job = 0, children = 4, Never_worked = 1
    
    work_type=request.form['work_type']
    
    # Urban = 1 Rural = 0
    Residence_type = request.form['Residence_type']
    
    avg_glucose_level= request.form['avg_glucose_level']
    
    bmi  = request.form['bmi']
    
    #formerly smoking = 1 , never smoked  = 2 , smokes = 3 ,unknown = 0
    smoking_status = request.form['smoking_status']
    
    if gender=='male': gender = 1
    else: gender  = 0
    
    if hypertension=='Yes': hypertension=1
    else: hypertension = 0
    
    if heart_disease=='Yes': heart_disease = 1
    else: heart_disease = 0
    
    if married=='Yes': married=1
    else: married = 0
    
    if Residence_type=='Urban': Residence_type=1
    else: Residence_type=0
    
    if work_type=='private': work_type=2
    elif work_type=='Govt': work_type=0
    elif work_type=='self': work_type=3
    elif work_type=='child': work_type=4
    else:work_type=1
    
    if smoking_status=='formerly-smoking': smoking_status=1
    elif smoking_status=='Never-Smoked':smoking_status=2
    elif smoking_status=='Smokes':smoking_status=3
    else:smoking_status=0

    data = [gender,age,hypertension,heart_disease,married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]

    data  = np.array([data],dtype=float)
    
    print(model)

    ans = prediction(data,model)
    
    #print(prediction([[1,67.0,0,1,1,2,1,228.69,36,1]]))
    
    #print(predict)
    
    result = ''

    if ans[0] == 1:
        
        result = "🔴 Chances of  Cerebral Stroke is high"
        
    else:
        
        result = "🟢 Chances of Cerebral Stroke is low"
        


    return render_template('result.html',**{'predict':result})


@app.route("/knn")
def knn():return render_template("knn-vid.html")

@app.route("/svm")
def svm():return render_template("svm-vid.html")

@app.route("/lr")
def lr():return render_template("lr-vid.html")

@app.route("/dec-tree")
def dec_tree():return render_template("dec-tree-vid.html")

@app.route("/random-forest")
def random_forest():return render_template("random-forest-vid.html")
  
  


@app.route("/report")
def reports():
    
    return render_template('report.html')

@app.route("/report-three")
def reports_three():
    
    return render_template('data-report-2.html')

@app.route("/report-two")
def reports_two():
    
    return render_template('data-report.html')


app.run(debug=True)


    

