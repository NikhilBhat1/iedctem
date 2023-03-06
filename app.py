
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return render_template('new.html')
@app.route('/events', methods=['GET'])
def eventsp():
    return render_template('pg2.html')
@app.route('/returns', methods=['GET'])
def returnsp():
    return render_template('new.html')



if __name__ == "__main__":
    app.run()
