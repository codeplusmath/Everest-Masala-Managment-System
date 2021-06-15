from flask import Flask, request, flash, jsonify
import mysql.connector

mydb = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Your Password',
                               database='masaladb')
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/user')
def user_send():
    try:
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/masala')
def masala_send():
    try:
        mycursor.execute("SELECT cost_price, stock, aunstk , balstk, sanstk, aunexpired, balexpired, sanexpired FROM masala")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/aunret')
def aunret_send():
    try:
        mycursor.execute("SELECT bill, amount_paid, balance_history , previous_history, paid, mode, cd, return_stk_amt, expiry_stk_amt, quantity, return_qty, expiry_qty FROM aundh")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/balret')
def balret_send():
    try:
        mycursor.execute("SELECT bill, amount_paid, balance_history , previous_history, paid, mode, cd, return_stk_amt, expiry_stk_amt, quantity, return_qty, expiry_qty FROM balewadi")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/sanret')
def sanret_send():
    try:
        mycursor.execute("SELECT bill, amount_paid, balance_history , previous_history, paid, mode, cd, return_stk_amt, expiry_stk_amt, quantity, return_qty, expiry_qty FROM sangvi")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.errorhandler(404)
def not_found(error=None):
    msg = {
        'status': 404,
        'message': 'Not Found ' + request.url,
    }
    resp = jsonify(msg)
    resp.status_code = 404

    return resp


@app.route('/aunstk_reset')
def aunstk_reset():
    try:
        request.get_json()
        mycursor.execute("update masala set aunstk=0")
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/balstk_reset')
def balstk_reset():
    try:
        request.get_json()
        mycursor.execute("update masala set balstk=0")
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/sanstk_reset')
def sanstk_reset():
    try:
        request.get_json()
        mycursor.execute("update masala set sanstk=0")
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/stock_update')
def stock_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update masala set stock=%s where code=%s"
            val = (x[i][0], i + 1, )
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/aunstk_update')
def aunstk_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            mycursor.execute("update masala set aunstk=%s where code=%s", x[i][0], i+1)
            print(x[i][0])
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/balstk_update')
def balstk_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            mycursor.execute("update masala set balstk=%s where code=%s", x[i][0], i+1)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/sanstk_update')
def sanstk_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            mycursor.execute("update masala set sanstk=%s where code=%s", x[i][0], i+1)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/aunexpstk_update')
def aunexpstk_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update masala set aunexpired=%s where code=%s"
            val = (x[i][0], i + 1, )
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/balexpstk_update')
def balexpstk_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update masala set balexpired=%s where code=%s"
            val = (x[i][0], i + 1, )
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)\


@app.route('/sanexpstk_update')
def sanexpstk_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update masala set sanexpired=%s where code=%s"
            val = (x[i][0], i + 1, )
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/aun_reset')
def aun_reset():
    try:
        mycursor.execute("update aundh set bill=0, amount_paid=0, paid=1, mode='NONE', cd=0, return_stk_amt=0, expiry_stk_amt=0, quantity=0, return_qty=0, expiry_qty=0")
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/bal_reset')
def bal_reset():
    try:
        mycursor.execute("update balewadi set bill=0, amount_paid=0, paid=1, mode='NONE', cd=0, return_stk_amt=0, expiry_stk_amt=0, quantity=0, return_qty=0, expiry_qty=0")
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/san_reset')
def san_reset():
    try:
        mycursor.execute("update sangvi set bill=0, amount_paid=0, paid=1, mode='NONE', cd=0, return_stk_amt=0, expiry_stk_amt=0, quantity=0, return_qty=0, expiry_qty=0")
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


# change data in the server as send by create bill function
@app.route('/aundh_create')
def aundh_create():
    try:
        x = request.get_json()

        for i in range(len(x)):
            sql = "update aundh set paid=%s, bill=%s, balance_history=%s, quantity=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/balewadi_create')
def balewadi_create():
    try:
        x = request.get_json()

        for i in range(len(x)):
            sql = "update balewadi set paid=%s, bill=%s, balance_history=%s, quantity=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], i + 1,)
            print(val)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/sangvi_create')
def sangvi_create():
    try:
        x = request.get_json()

        for i in range(len(x)):
            sql = "update sangvi set paid=%s, bill=%s, balance_history=%s, quantity=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


# change data in the server as send by update bill function
@app.route('/aundh_update')
def aundh_update():
    try:
        x = request.get_json()

        for i in range(len(x)):
            sql = "update aundh set balance_history=%s, return_stk_amt=%s, expiry_stk_amt=%s, return_qty=%s, expiry_qty=%s where code = %s"

            val = (x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp

    except Exception as e:
        print(e)


@app.route('/balewadi_update')
def balewadi_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update balewadi set balance_history=%s, return_stk_amt=%s, expiry_stk_amt=%s, return_qty=%s, expiry_qty=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/sangvi_update')
def sangvi_update():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update sangvi set balance_history=%s, return_stk_amt=%s, expiry_stk_amt=%s, return_qty=%s, expiry_qty=%s where code = %s"

            val = (x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


# change data in the server as send by delivery function
@app.route('/aundh_delivery')
def aundh_delivery():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update aundh set amount_paid=%s, balance_history=%s, previous_history=%s, paid=%s, mode=%s, cd=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], x[i][5], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/balewadi_delivery')
def balewadi_delivery():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update balewadi set amount_paid=%s, balance_history=%s, previous_history=%s, paid=%s, mode=%s, cd=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], x[i][5], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


@app.route('/sangvi_delivery')
def sangvi_delivery():
    try:
        x = request.get_json()
        for i in range(len(x)):
            sql = "update sangvi set amount_paid=%s, balance_history=%s, previous_history=%s, paid=%s, mode=%s, cd=%s where code = %s"
            val = (x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], x[i][5], i + 1,)
            mycursor.execute(sql, val)
        mydb.commit()
        resp = 'success'
        return resp
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # app.run()
    app.run(host="127.0.0.1", port=5000)