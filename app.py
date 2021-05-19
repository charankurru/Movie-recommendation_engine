from flask import *


app  = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def recommendation():
    print(request.form['movie'])
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
