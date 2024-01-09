from flask import Flask,render_template,request
import pickle
import numpy as np


app = Flask(__name__)

def prediction(list):
    file_name = "Model\predictor.pickle"
    with open (file_name,'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([list])
    return pred_value


@app.route('/',methods= ['POST','GET'])
def index():
    pred = 0
    if request.method =='POST':
        ram = request.form['ram']
        weight = request.form['weight']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')
        company = request.form['company']
        typeName= request.form['typeName']
        os= request.form['os']
        cpuType= request.form['cpuType']
        gpuType= request.form['gpuType']

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(float(weight))
        feature_list.append(len(touchscreen))
        feature_list.append(len(ips))

        def appendList(list,feature):
            for item in list:
                if item == feature:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

            
        company_list = ['acer', 'apple', 'asus', 'dell', 'hp', 'lenovo', 'msi', 'company_toshiba', 'other']
        typename_list = ['2 in 1 convertible', 'gaming', 'netbook', 'typename_notebook', 'ultrabook', 'workstation']
        opsys_list = ['linux', 'mac', 'windows', 'other']
        cpu_list = ['amd', 'intel core i3', 'intel core i5', 'intel core i7', 'other']
        gpu_list = ['amd', 'intel', 'nvidia']

        
        appendList(company_list,company)
        appendList(typename_list,typeName)
        appendList(opsys_list,os)
        appendList(cpu_list,cpuType)
        appendList(gpu_list,gpuType)

        pred = prediction(feature_list)*219
        pred =  np.round(pred[0])
     
        
        

    return render_template("index.html",pred = pred)

if __name__ == '__main__':
    app.run(debug=True)
