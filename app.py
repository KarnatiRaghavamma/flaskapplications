from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome to the first class Raghavamma"
@app.route('/second')
def second():
    return render_template('welcome.html')
@app.route('/age',methods=['GET','POST'])
def age():
    if request.method=='POST':
        age=request.form['age']
        print(age)
    return render_template('age.html')
# hw
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        mobilenumber=request.form['mobilenumber']
        email=request.form['email']
        dob=request.form['dob']
        return f"<ul><li>{name}</li><li>{username}</li><li>{mobilenumber}</li><li>{email}</li><li>{dob}</li></ul>"
    return render_template('regis.html')
# passing data through url args
@app.route('/info')
def info():
    print(request.args)
    print(request.args.get('username'))
    return "Pass Data"
app.run(debug=True)
