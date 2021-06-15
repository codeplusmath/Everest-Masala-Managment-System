import mysql.connector      # database connected
mydb = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='#Sonawane@21', database='masaladb')
mycursor = mydb.cursor()    # use of cursor for execution

# creation of masala BST using masala and stock file
'''
mycursor.execute("CREATE TABLE masala(code SMALLINT, mas_name VARCHAR(50), cost_price DOUBLE, stock INT, aunstk INT, balstk INT, sanstk INT, aunexpired INT, balexpired INT, sanexpired INT)")
f = open("masala.txt")
s = open("stock.txt")
i = 1
for x in range(1, 226, 2):
  y = f.readline()      # masala name
  z = f.readline()      # price
  z = float(z)
  u = s.readline()      # stock
  u = int(u)
  sql = "INSERT INTO masala (code, mas_name, cost_price, stock) VALUES (%s, %s, %s, %s)"
  val = (i, y.rstrip("\n"), z, u, )
  mycursor.execute(sql, val)
  mydb.commit()
  i += 1
f.close()
s.close()
'''
# creation of retailer BST using each individual files
'''
mycursor.execute("CREATE TABLE aundh(code SMALLINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), address VARCHAR(50), contact CHAR(10), bill float, amount_paid float, balance_history float, previous_history float, paid smallint, mode VARCHAR(6), cd float, return_stk_amt float, expiry_stk_amt float, quantity float, return_qty float, expiry_qty float)")
f = open("aundh.txt")
for x in range(1, 11):
    t = f.readline()    # name
    t = t.upper()
    u = f.readline()    # add
    u = u.upper()
    v = f.readline()    # cnumm

    sql = "INSERT INTO aundh(code, name, address, contact, bill, amount_paid, balance_history, previous_history, paid, mode, cd, return_stk_amt, expiry_stk_amt, quantity, return_qty, expiry_qty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (x, t.rstrip("\n"), u.rstrip("\n"), v.rstrip("\n"), 0.00, 0.00, 0.00, 0.00, 1, "NONE", 0.00, 0.00, 0.00, 0, 0.00, 0.00)
    mycursor.execute(sql, val)
    mydb.commit()
f.close()
'''
# creation of validation table
'''
owner = "akashmore"
opass = "am301996"
sale = "vijaywd"
spass = "vw281999"
dboy1 = "omkar"
dpass1 = "os212001"
dboy2 = "rajkumar"
dpass2 = "rs252001"
type1 = "owner"
type2 = "salesman"
type3 = "boy"
mycursor.execute("CREATE TABLE user(name VARCHAR(10), password VARCHAR(10), type VARCHAR(8)")


sql = "INSERT INTO user (name, password, type) VALUES (%s, %s, %s)"
val = [(owner, opass, type1), (sale, spass, type2), (dboy1, dpass1, type3), (dboy2, dpass2, type3)]
mycursor.executemany(sql, val)
mydb.commit()
'''
'''
mycursor.execute("ALTER TABLE masala ADD aunstk SMALLINT")
mycursor.execute("ALTER TABLE masala ADD balstk SMALLINT")
mycursor.execute("ALTER TABLE masala ADD sanstk SMALLINT")
'''

'''
for x in range(1, 114):
  sql = "UPDATE masala SET balstk = %s WHERE code = %s"
  val = (10, x)
  mycursor.execute(sql, val)
mydb.commit()
'''
