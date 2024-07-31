from flask import Flask,request,url_for,render_template,redirect
app2=Flask(__name__)
#ATM Application
accounts={'12345':{'pin':'111','balance':3000},
           '45678':{'pin':'222','balance':6000}}
#account creation
@app2.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        accno=request.form['accno']
        pinno=request.form['pinno']
        initial_balance=request.form.get('balance',0)
        if accno in accounts:
            return "<center><h1>Account Already existed</h1></center>",400
        accounts[accno]={'pin':pinno,'balance':initial_balance}
        return "<center><h1>Account created successfully...!</h1></center>"
    return render_template('atm.html')
@app2.route('/data')
def data():
    accounts_list=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
    return accounts_list
@app2.route('/alreadyacc',methods=['GET','POST'])
def alreadyacc():
    if request.method=='POST':
        accno=request.form["accno"]
        pinno=request.form["pinno"]
        if accno in accounts:
            details=accounts[accno]
            print(details)
            accounts_list=[{'account_id':accno,'pinno':details['pin']}]
            #accounts_list=[{'account_id':accno,'pinno':details['pin']} for accno,details in accounts.items()]
            if pinno==accounts_list[0]['pinno']:
                return redirect(url_for('panel',accno=accno,pinno=pinno))
            else:
                return "<center><h1>Invalid Pin Number</h1></center>"
        else:
            return "<center><h1>Invalid Account Number</h1></center>",400
    return render_template('login.html')
@app2.route('/panel/<accno>/<pinno>')
def panel(accno,pinno):
    return render_template('options.html',accno=accno,pinno=pinno)
@app2.route('/deposit/<accno>/<pinno>',methods=['GET','POST'])
def deposit(accno,pinno):
    if request.method=='POST':
        amount=int(request.form['deposit'])
        print(amount)
        details=accounts[accno]
        accounts_list=[{'account_id':accno,'pinno':details['pin']}]
        #accounts_list=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
        if accounts_list[0]['account_id']==accno:
            accounts[accno]['balance']+=amount
        return redirect(url_for('panel',accno=accno,pinno=pinno))
        print(accounts)
    return render_template('deposit.html')

@app2.route('/withdraw/<accno>/<pinno>',methods=['GET','POST'])
def withdraw(accno,pinno):
    if request.method=='POST':
        amount=int(request.form['withdraw'])
        print(amount)
        details=accounts[accno]
        accounts_list=[{'account_id':accno,'balance':details['balance']}]
        #accounts_list=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
        if accounts_list[0]['account_id']==accno:
            oramount=accounts_list[0]['balance']
        if amount>oramount:
            return "</center><h1>Given amount is out of balance</h1></center>"
        else:
            accounts[accno]['balance']-=amount
            return redirect(url_for('panel',accno=accno,pinno=pinno))
            print(accounts)
    return render_template('withdraw.html')

@app2.route('/balance/<accno>/<pinno>',methods=['GET','POST'])
def balance(accno,pinno):
    details=accounts[accno]
    accounts_list=[{'account_id':accno,'balance':details['balance']}]
    return render_template('balance.html',accounts_list=accounts_list)
app2.run(debug=True,use_reloader=True)


# @app2.route('/deposit',methods=['GET','POST'])
# def deposit():
#     return render_template('deposit.html')

# @app2.route('/options')
# def options():
#     return redirect(url_for('deo'))
# @app2.route('/deo',methods=['GET','POST'])
# def deposit():
#     if request.method=='POST':
#         deposit=request.form["deposit"]
#         accounts=accounts+deposit
#         return "Succesfully deposit your Money"
#     return render_template('/deposit')
