import sys
import getopt
from flask import Flask, request, jsonify
from models import User, Account
from database import db_session
import simplejson as json

makejson = json.dumps
app = Flask(__name__)

DEFAULT_PORT_NO = 8888

def usageguide():
    print("InsecureBankv2 Backend-Server")
    print("Options:")
    print("  --port p    serve on port p (default 8888)")
    print("  --help      print this message")

@app.errorhandler(500)
def internal_server_error(error):
    print(" [!] Internal Server Error:", error)
    return "Internal Server Error", 500

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    Responsemsg = "fail"
    u = User.query.filter(User.username == user).first()
    print("u =", u)
    if u and u.password == request.form['password']:
        Responsemsg = "Correct Credentials"
    elif u and u.password != request.form['password']:
        Responsemsg = "Wrong Password"
    elif not u:
        Responsemsg = "User Does not Exist"
    else:
        Responsemsg = "Some Error"

    data = {"message": Responsemsg, "user": user}
    print(makejson(data))
    return makejson(data)

@app.route('/getaccounts', methods=['POST'])
def getaccounts():
    Responsemsg = "fail"
    from_acc = to_acc = None
    user = request.form['username']

    u = User.query.filter(User.username == user).first()
    if not u or u.password != request.form['password']:
        Responsemsg = "Wrong Credentials so trx fail"
    else:
        Responsemsg = "Correct Credentials so get accounts will continue"
        accounts = Account.query.filter(Account.user == user)
        for acc in accounts:
            if acc.type == 'from':
                from_acc = acc.account_number
            if acc.type == 'to':
                to_acc = acc.account_number

    data = {"message": Responsemsg, "from": from_acc, "to": to_acc}
    print(makejson(data))
    return makejson(data)

@app.route('/changepassword', methods=['POST'])
def changepassword():
    Responsemsg = "fail"
    newpassword = request.form['newpassword']
    user = request.form['username']

    u = User.query.filter(User.username == user).first()
    if not u:
        Responsemsg = "Error"
    else:
        u.password = newpassword
        db_session.commit()
        Responsemsg = "Change Password Successful"

    data = {"message": Responsemsg}
    print(makejson(data))
    return makejson(data)

@app.route('/dotransfer', methods=['POST'])
def dotransfer():
    Responsemsg = "fail"
    from_acc = to_acc = amount = None
    user = request.form['username']

    u = User.query.filter(User.username == user).first()
    if not u or u.password != request.form['password']:
        Responsemsg = "Wrong Credentials so trx fail"
    else:
        from_acc = request.form['from_acc']
        to_acc = request.form['to_acc']
        amount = int(request.form['amount'])

        from_account = Account.query.filter(Account.account_number == from_acc).first()
        to_account = Account.query.filter(Account.account_number == to_acc).first()

        if from_account and to_account:
            from_account.balance -= amount
            to_account.balance += amount
            db_session.commit()
            Responsemsg = "Success"

    data = {"message": Responsemsg, "from": from_acc, "to": to_acc, "amount": amount}
    print(makejson(data))
    return makejson(data)

@app.route('/devlogin', methods=['POST'])
def devlogin():
    user = request.form['username']
    Responsemsg = "Correct Credentials"
    data = {"message": Responsemsg, "user": user}
    print(makejson(data))
    return makejson(data)

if __name__ == '__main__':
    port = DEFAULT_PORT_NO

    try:
        options, args = getopt.getopt(sys.argv[1:], "", ["help", "port="])
        for op, arg1 in options:
            if op == "--help":
                usageguide()
                sys.exit(2)
            elif op == "--port":
                port = int(arg1)
    except getopt.GetoptError:
        usageguide()
        sys.exit(2)

    print(f"Starting InsecureBankv2 Server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)
