from kivymd.toast import toast
import time
import requests


URL1 = 'http://127.0.0.1:5000/masala'
URL2 = 'http://127.0.0.1:5000/aunret'
URL3 = 'http://127.0.0.1:5000/balret'
URL4 = 'http://127.0.0.1:5000/sanret'


class node:
    def __init__(self, sc, amt, stk, mn, astk, bstk, sstk, aestk, bestk, sestk):
        self.stock_code = sc
        self.amount = amt
        self.stock = stk
        self.masala_name = mn
        self.aunstk = astk
        self.balstk = bstk
        self.sanstk = sstk
        self.aunexpstk = aestk
        self.balexpstk = bestk
        self.sanexpstk = sestk
        self.left = self.right = None


class r_node:
    def __init__(self, c, nm, add, cno, bill_amt, amt, ph, ap, pd, md, cash, rsa, esa, qty, rqty, eqty):
        self.code = c
        self.name = nm
        self.address = add
        self.contact_num = cno
        self.bill = bill_amt
        self.amount_paid = ap
        self.balance = amt
        self.previous_history = ph
        self.paid = pd
        self.mode = md
        self.cd = cash
        self.return_stk_amt = rsa
        self.expiry_stk_amt = esa
        self.quantity = qty
        self.return_qty = rqty
        self.expiry_qty = eqty
        self.left = self.right = None


def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = (len(arr)) / 2
    mid = int(mid)
    root = node(arr[mid], 0.00, 0, "", 0, 0, 0, 0, 0, 0)
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root


def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.stock_code == key:
        return root

    # Key is greater than root's key
    if root.stock_code < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


def inorder_insert():
    try:
        r = requests.get(url=URL1)
        data = r.json()
        f = open("masala.txt")
    except FileNotFoundError:
        print('File does not exist')
    except:
        print('Data not found')
        return

    mas_count = len(data)

    global countofmasala
    countofmasala = mas_count

    arrayofmasalacode = []
    for masala_code in range(1, mas_count + 1):
        arrayofmasalacode.append(masala_code)
    root = sortedArrayToBST(arrayofmasalacode)

    if root is None:
        return None
    i = 0

    while i < mas_count:
        t = search(root, arrayofmasalacode[i])
        mas = f.readline()
        setattr(t, 'masala_name', mas.rstrip("\n"))
        setattr(t, 'amount', data[i][0])
        setattr(t, 'stock', data[i][1])
        setattr(t, 'aunstk', data[i][2])
        setattr(t, 'balstk', data[i][3])
        setattr(t, 'sanstk', data[i][4])
        setattr(t, 'aunexpstk', data[i][5])
        setattr(t, 'balexpstk', data[i][6])
        setattr(t, 'sanexpstk', data[i][7])
        i += 1

    f.close()
    return root


def masinorder(root, flag):
    current = root
    stack = []
    mas = ""
    global name

    if flag == 0:
        name = 'stock'
    elif flag == 1:
        name = 'aunstk'
    elif flag == 2:
        name = 'balstk'
    elif flag == 3:
        name = 'sanstk'

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            node = stack.pop()
            if flag != 0 and getattr(node, name) != 0:
                mas = mas + "\n\nName : " + getattr(node, 'masala_name') + "\nStock : " + str(getattr(node, name)) + \
                      "     Total Amount : " + str(round(getattr(node, name) * getattr(node, 'amount'), 2))
            elif flag == 0:
                mas = mas + "\n\nName : " + getattr(node, 'masala_name') + "\nStock : " + str(getattr(node, name)) + "       Unit price : " + str(getattr(node, 'amount'))
            current = node.right
        else:
            break
    return mas


def masalasearch(root, x):
    if root is None:
        return None

    nodeStack = [root]
    searchstack = []

    j = len(x)
    match_flag = i = 0
    while len(nodeStack):
        node = nodeStack[0]

        while j > 0:
            if node.masala_name[i] is x[i] or ord(node.masala_name[i]) == ord(x[i]) - 32:

                match_flag = 1
                j -= 1
                i += 1

            else:
                match_flag = 0
                break

        if match_flag == 1:
            searchstack.append(nodeStack[0])

        nodeStack.pop(0)
        if node.right:
            nodeStack.append(node.right)
        if node.left:
            nodeStack.append(node.left)

        i = 0
        j = len(x)

    return searchstack


# button --- update
def update(root, mas, quantity):        # mas and quantity is received from textbox
    if root is None:
        return None

    nodeStack = [root]      # Create an empty stack for preorder traversal and append root to it
    # nodeStack.append(root)

    j = len(mas)  # length of the masala to be searched
    match_flag = i = 0  # flag and index set to 0
    # Do iterative preorder traversal to search x
    while len(nodeStack):  # loop until stack is not empty
        # See the top item from stack and check if it is same as x
        node = nodeStack[0]

        while j > 0:  # loop until length of masala
            if node.masala_name[i] == mas[i] or ord(node.masala_name[i]) == ord(mas[i]) - 32:
                match_flag = 1
            else:
                match_flag = 0
                break  # goes for further traversal
            j -= 1
            i += 1

        if match_flag == 1:             # mas is the complete name of masala & found then update and break loop
            setattr(nodeStack[0], 'stock', getattr(nodeStack[0], 'stock') + quantity)
            break

        nodeStack.pop(0)
        # append right and left children of the popped node to stack
        if node.right:
            nodeStack.append(node.right)
        if node.left:
            nodeStack.append(node.left)

        i = 0
        j = len(mas)


def sortedArrayToRST(arr):
    if not arr:
        return None
    mid = (len(arr)) / 2
    mid = int(mid)
    root = r_node(arr[mid], "", "", "", 0.00, 0.00, 0.00, 0.00, 1, "", 0.00, 0.00, 0.00, 0, 0, 0)
    root.left = sortedArrayToRST(arr[:mid])
    root.right = sortedArrayToRST(arr[mid + 1:])
    return root


def ret_search(root, key):

    if root is None or root.code == key:
        return root

    if root.code < key:
        return ret_search(root.right, key)

    return ret_search(root.left, key)


def retsearch(root, retname):
    if root is None:
        return None

    nodestack = [root]
    searchstack = []

    j = len(retname)
    match_flag = i = 0

    while len(nodestack):
        node = nodestack[0]

        while j > 0:
            if node.name[i] == retname[i] or ord(node.name[i]) == ord(retname[i]) - 32:
                match_flag = 1
            else:
                match_flag = 0
                break
            j -= 1
            i += 1

        if match_flag == 1:
            searchstack.append(nodestack[0])

        nodestack.pop(0)
        if node.right:
            nodestack.append(node.right)
        if node.left:
            nodestack.append(node.left)

        i = 0
        j = len(retname)
    return searchstack


def retailer_inorder_insert(val, filename):
    try:
        r = requests.get(url=val)
        data = r.json()
        f = open(filename)
    except FileNotFoundError:
        print('File does not exist')
    except:
        print('Data not found')
        return
    ret_count = len(data)

    global countofret
    countofret = ret_count
    array_of_retailercode = []
    for retailer_code in range(1, ret_count + 1):
        array_of_retailercode.append(retailer_code)

    root = sortedArrayToRST(array_of_retailercode)

    if root is None:
        return None

    i = 0
    while i < ret_count:
        t = ret_search(root, array_of_retailercode[i])
        mas = f.readline()  # name
        mas = mas.upper()
        u = f.readline()  # add
        u = u.upper()
        v = f.readline()  # cnumm
        setattr(t, 'name', mas.rstrip("\n"))
        setattr(t, 'address', u.rstrip("\n"))
        setattr(t, 'contact_num', v.rstrip("\n"))
        setattr(t, 'bill', data[i][0])
        setattr(t, 'amount_paid', data[i][1])
        setattr(t, 'balance', data[i][2])
        setattr(t, 'previous_history', data[i][3])
        setattr(t, 'paid', data[i][4])
        setattr(t, 'mode', data[i][5])
        setattr(t, 'cd', data[i][6])
        setattr(t, 'return_stk_amt', data[i][7])
        setattr(t, 'expiry_stk-amt', data[i][8])
        setattr(t, 'quantity', data[i][9])
        setattr(t, 'return_qty', data[i][10])
        setattr(t, 'expiry_qty', data[i][11])
        i += 1

    f.close()
    return root


# flag = 1 => all retailers & 0 => pending retailers
def retinorder(root, flag):

    ret = ""
    if root is None:
        return ret
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            node = stack.pop()
            if getattr(node, 'paid') == 0 or flag:
                ret = ret + "\n\nName : " + getattr(node, 'name') + "\nContact : " + getattr(node,
                                                                                             'contact_num') + "\nAddress : " + getattr(
                    node, 'address') + "\nBill : " + str(round(getattr(node, 'bill'),2)) + "        Amount Paid :" + str(round(getattr(node,
                                                                                                               'amount_paid'),2)) + "\nBalance History : " + str(round(getattr(
                    node, 'balance'),2)) + "      Previous history : " + str(round(getattr(node, 'previous_history'),2))
            current = node.right
        else:
            break
    return ret


def transactions(root):
    Total = [0, 0, 0, 0, 0, 0, 0]
    if root is None:
        return Total
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            node = stack.pop()
            Total[0] += getattr(node, 'bill')
            Total[1] += getattr(node, 'amount_paid')
            Total[2] += getattr(node, 'balance')
            Total[3] += getattr(node, 'previous_history')
            Total[4] += getattr(node, 'cd')
            Total[5] += getattr(node, 'return_stk_amt')
            Total[6] += getattr(node, 'expiry_stk_amt')
            current = node.right
        else:
            break
    return Total


def stocktojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            # code
            l[i].append(getattr(current, 'stock'))
            i += 1
            current = current.right
        else:
            break

    return l


def aunstktojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            l[i].append(getattr(current, 'aunstk'))
            i += 1
            current = current.right
        else:
            break
    return l


def balstktojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            l[i].append(getattr(current, 'balstk'))
            i += 1
            current = current.right
        else:
            break
    return l


def sanstktojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            l[i].append(getattr(current, 'sanstk'))
            i += 1
            current = current.right
        else:
            break

    return l


def aunexptojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            l[i].append(getattr(current, 'aunexpstk'))
            i += 1
            current = current.right
        else:
            break
    return l


def balexptojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            l[i].append(getattr(current, 'balexpstk'))
            i += 1
            current = current.right
        else:
            break
    return l


def sanexptojson(root):
    l = []
    for i in range(countofmasala):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            l[i].append(getattr(current, 'sanexpstk'))
            i += 1
            current = current.right
        else:
            break

    return l


def createbilltojson(root):
    l = []
    for i in range(countofret):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            # code
            l[i].append(getattr(current, 'paid'))
            l[i].append(getattr(current, 'bill'))
            l[i].append(getattr(current, 'balance'))
            l[i].append(getattr(current, 'quantity'))
            i += 1
            current = current.right
        else:
            break
    return l


def updatebilltojson(root):
    l = []
    for i in range(countofret):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            # code
            l[i].append(getattr(current, 'balance'))
            l[i].append(getattr(current, 'return_stk_amt'))
            l[i].append(getattr(current, 'expiry_stk_amt'))
            l[i].append(getattr(current, 'return_qty'))
            l[i].append(getattr(current, 'expiry_qty'))
            i += 1
            current = current.right
        else:
            break
    return l


def deliverbilltojson(root):
    l = []
    for i in range(countofret):
        l.append([])

    i = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            # code
            l[i].append(getattr(current, 'amount_paid'))
            l[i].append(getattr(current, 'balance'))
            l[i].append(getattr(current, 'previous_history'))
            l[i].append(getattr(current, 'paid'))
            l[i].append(getattr(current, 'mode'))
            l[i].append(getattr(current, 'cd'))
            i += 1
            current = current.right
        else:
            break
    return l


try:
    mas_tree = inorder_insert()
    aun_tree = retailer_inorder_insert(URL2, "aundh.txt")
    bal_tree = retailer_inorder_insert(URL3, "balewadi.txt")
    san_tree = retailer_inorder_insert(URL4, 'sangvi.txt')
except ConnectionError:
    pass
