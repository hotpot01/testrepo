from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        message='hello admin'
        return render_template('form.html',message=message,username=username)
    message='Bad username or password'
    return render_template('form.html', message=message,username=username)

if __name__ == '__main__':
    app.run(debug=True)