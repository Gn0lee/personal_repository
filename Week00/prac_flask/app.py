from flask import Flask, render_template
app = Flask(__name__)

@app.route('/mother')
def mother():
   return render_template('mother.html')

@app.route('/child')
def mypage():  
   return render_template('child.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)