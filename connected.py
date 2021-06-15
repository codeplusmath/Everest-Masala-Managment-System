from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from datetime import date  # Import date class from datetime module
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from mains import *
from kivymd.toast import toast

today = date.today()


# Owner Connected Screen
class OwnerConnected(Screen):
    # logout
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def next(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def viewaunmasala(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'viewaunstock'
        self.manager.get_screen('viewaunstock')

    def viewbalmasala(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'viewbalstock'
        self.manager.get_screen('viewbalstock')

    def viewsanmasala(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'viewsanstock'
        self.manager.get_screen('viewsanstock')

    # View Bills
    def viewAunBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewaundhbills'
        self.manager.get_screen('ownerviewaundhbills')

    def viewBalBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewbalewadibills'
        self.manager.get_screen('ownerviewbalewadibills')

    def viewSanBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewsangvibills'
        self.manager.get_screen('ownerviewsangvibills')

    def viewAunUpdates(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewaundhupdates'
        self.manager.get_screen('ownerviewaundhupdates')

    def viewBalUpdates(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewbalewadiupdates'
        self.manager.get_screen('ownerviewbalewadiupdates')

    def viewSanUpdates(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewsangviupdates'
        self.manager.get_screen('ownerviewsangviupdates')


class OwnerViewAunBills(Screen):
    def on_enter(self):
        file = open("aundhbill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class OwnerViewBalBills(Screen):
    def on_enter(self):
        file = open("balewadibill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class OwnerViewSanBills(Screen):
    def on_enter(self):
        file = open("sangvibill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class OwnerViewAunUpdates(Screen):
    def on_enter(self):
        file = open("aundhupdates.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class OwnerViewBalUpdates(Screen):
    def on_enter(self):
        file = open("balupdates.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    # back screen
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class OwnerViewSanUpdates(Screen):
    def on_enter(self):
        file = open("sanupdates.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    # back screen
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class AunViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')

    def on_enter(self):
        text = ""
        text += masinorder(mas_tree, 1)
        self.ids.view_aun_masala.text = text


class BalViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')

    def on_enter(self):
        text = ""
        text += masinorder(mas_tree, 2)
        self.ids.view_bal_masala.text = text


class SanViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')

    def on_enter(self):
        text = ""
        text += masinorder(mas_tree, 3)
        self.ids.view_san_masala.text = text


# Owner Next Connected Screen
class OwnerNextConnected(Screen):
    # logout
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    # back screen
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')

    def next(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownernextnextconnected'
        self.manager.get_screen('ownernextnextconnected')

    def viewmasala(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'viewstock'
        self.manager.get_screen('viewstock')

    def searchsc(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'searchmasala'
        self.manager.get_screen('searchmasala')

    def updatestk(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'updatestock'
        self.manager.get_screen('updatestock')

    def aunsearchret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'aunsearchretailer'
        self.manager.get_screen('aunsearchretailer')

    def balsearchret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'balsearchretailer'
        self.manager.get_screen('balsearchretailer')

    def sansearchret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'sansearchretailer'
        self.manager.get_screen('sansearchretailer')

    def aunviewret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'aunviewretailer'
        self.manager.get_screen('aunviewretailer')

    def balviewret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'balviewretailer'
        self.manager.get_screen('balviewretailer')

    def sanviewret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'sanviewretailer'
        self.manager.get_screen('sanviewretailer')


class ViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def on_enter(self):
        text = ""
        text += masinorder(mas_tree, 0)
        self.ids.view_masala.text = text


class SearchMasala(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def search(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        load_masala = ""
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!"
        else:
            for x in range(len(node)):
                load_masala = load_masala + "\nName : " + getattr(node[x], 'masala_name') + "\n" + "Stock : " + str(
                    getattr(node[x], 'stock')) + "        Unit Price : " + str(getattr(node[x], 'amount')) + "\n\n"
            self.ids.search_masala.text = load_masala
        self.ids.masalaname.text = ""


class UpdateStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def search(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!"
        else:
            self.ids.search_masala.text = ""
            maslist = []
            for x in range(len(node)):
                maslist.append(getattr(node[x], 'masala_name'))
            self.ids.masspinner.values = maslist

    def updatestk(self, masalaname, quantity):  # button -- Update
        update(mas_tree, masalaname, int(quantity))
        self.ids['stockname'].text = ""
        self.ids['stockquantity'].text = ""

    def save(self):  # button -- Save Changes
        try:
            URL = 'http://127.0.0.1:5000/stock_update'
            requests.get(url=URL, json=stocktojson(mas_tree))
        except ConnectionError:
            toast("Network Error")


class AunSearchRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def search_aun_ret(self, retailername):
        node = retsearch(aun_tree, retailername)
        load_retailer = ""

        if len(node) == 0:
            self.ids.search_aun_retailer.text = "\nRetailer does not exist!"
        else:
            for x in range(len(node)):
                if getattr(node[x], 'paid') == 1:
                    pd = "PAID"
                else:
                    pd = "NOT PAID"
                load_retailer = load_retailer + "\n\nName : " + getattr(node[x], 'name') + "\nContact : " + str(
                    getattr(node[x], 'contact_num')) + "\nAddress : " + getattr(node[x], 'address') + "\nBill : " + str(
                    getattr(node[x], 'bill')) + "        Amount Paid :" + str(
                    getattr(node[x], 'amount_paid')) + "\nBalance History : " + str(
                    getattr(node[x], 'balance')) + "      Paid : " + pd + "\n"
            self.ids.search_aun_retailer.text = load_retailer
        self.ids['aunretailername'].text = ""


class BalSearchRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def search_bal_ret(self, retailername):
        node = retsearch(bal_tree, retailername)
        load_retailer = ""

        if len(node) == 0:
            self.ids.search_bal_retailer.text = "\nRetailer does not exist!"
        else:
            for x in range(len(node)):
                if getattr(node[x], 'paid') == 1:
                    pd = "PAID"
                else:
                    pd = "NOT PAID"
                load_retailer = load_retailer + "\n\nName : " + getattr(node[x], 'name') + "\nContact : " + str(
                    getattr(node[x], 'contact_num')) + "\nAddress : " + getattr(node[x], 'address') + "\nBill : " + str(
                    getattr(node[x], 'bill')) + "        Amount Paid :" + str(
                    getattr(node[x], 'amount_paid')) + "\nBalance History : " + str(
                    getattr(node[x], 'balance')) + "      Paid : " + pd + "\n"
            self.ids.search_bal_retailer.text = load_retailer
        self.ids['balretailername'].text = ""


class SanSearchRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def search_san_ret(self, retailername):
        node = retsearch(san_tree, retailername)
        load_retailer = ""

        if len(node) == 0:
            self.ids.search_san_retailer.text = "\nRetailer does not exist!"
        else:
            for x in range(len(node)):
                if getattr(node[x], 'paid') == 1:
                    pd = "PAID"
                else:
                    pd = "NOT PAID"
                load_retailer = load_retailer + "\n\nName : " + getattr(node[x], 'name') + "\nContact : " + str(
                    getattr(node[x], 'contact_num')) + "\nAddress : " + getattr(node[x], 'address') + "\nBill : " + str(
                    getattr(node[x], 'bill')) + "        Amount Paid :" + str(
                    getattr(node[x], 'amount_paid')) + "\nBalance History : " + str(
                    getattr(node[x], 'balance')) + "      Paid : " + pd + "\n"
            self.ids.search_san_retailer.text = load_retailer
        self.ids['sanretailername'].text = ""


class AunViewRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def on_enter(self):
        text = ""
        text += retinorder(aun_tree, 1)
        self.ids.view_aun_retailer.text = text

    def pending_aun_ret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'aunpending'
        self.manager.get_screen('aunpending')


class BalViewRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def on_enter(self):
        text = ""
        text += retinorder(bal_tree, 1)
        self.ids.view_bal_retailer.text = text

    def pending_bal_ret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'balpending'
        self.manager.get_screen('balpending')


class SanViewRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def on_enter(self):
        text = ""
        text += retinorder(san_tree, 1)
        self.ids.view_san_retailer.text = text

    def pending_san_ret(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'sanpending'
        self.manager.get_screen('sanpending')


class AunPendingRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'aunviewretailer'
        self.manager.get_screen('aunviewretailer')

    def on_enter(self):
        text = ""
        text += retinorder(aun_tree, 0)
        self.ids.pending_aun.text = text


class BalPendingRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'balviewretailer'
        self.manager.get_screen('balviewretailer')

    def on_enter(self):
        text = ""
        text += retinorder(bal_tree, 0)
        self.ids.pending_bal.text = text


class SanPendingRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'sanviewretailer'
        self.manager.get_screen('sanviewretailer')

    def on_enter(self):
        text = ""
        text += retinorder(san_tree, 0)
        self.ids.pending_san.text = text


# Owner Next Next Connected Screen
class OwnerNextNextConnected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextconnected'
        self.manager.get_screen('ownernextconnected')

    def ResetAunBill(self):
        f = open("aundhbill.txt", "wt")
        f.write("Name: Vijay Waidande (WMH-01)\nCompany Name: Everest Spices\n")
        f.close()

    def ResetBalBill(self):
        f = open("balewadibill.txt", "wt")
        f.write("Name: Vijay Waidande (WMH-01)\nCompany Name: Everest Spices\n")
        f.close()

    def ResetSanBill(self):
        f = open("sangvibill.txt", "wt")
        f.write("Name: Vijay Waidande (WMH-01)\nCompany Name: Everest Spices\n")
        f.close()

    def ResetAunUpdate(self):
        f = open("aundhupdates.txt", "wt")
        f.write("Name: Vijay Waidande (WMH-01)\nCompany Name: Everest Spices\n")
        f.close()

    def ResetBalUpdate(self):
        f = open("balupdates.txt", "wt")
        f.write("Name: Vijay Waidande (WMH-01)\nCompany Name: Everest Spices\n")
        f.close()

    def ResetSanUpdate(self):
        f = open("sanupdates.txt", "wt")
        f.write("Name: Vijay Waidande (WMH-01)\nCompany Name: Everest Spices\n")
        f.close()

    def ResetAunStock(self):
        try:
            URL = 'http://127.0.0.1:5000/aunstk_reset'
            requests.get(url=URL)
        except ConnectionError:
            toast('Network error')

    def ResetBalStock(self):
        try:
            URL = 'http://127.0.0.1:5000/balstk_reset'
            requests.get(url=URL)
        except ConnectionError:
            toast('Network error')

    def ResetSanStock(self):
        try:
            URL = 'http://127.0.0.1:5000/sanstk_reset'
            requests.get(url=URL)
        except ConnectionError:
            toast('Network error')

    def AunRetReset(self):
        try:
            URL = 'http://127.0.0.1:5000/aun_reset'
            requests.get(url=URL)
        except ConnectionError:
            toast('Network error')

    def BalRetReset(self):
        try:
            URL = 'http://127.0.0.1:5000/bal_reset'
            requests.get(url=URL)
        except ConnectionError:
            toast('Network error')

    def SanRetReset(self):
        try:
            URL = 'http://127.0.0.1:5000/san_reset'
            requests.get(url=URL)
        except ConnectionError:
            toast('Network error')

    def viewAunTransaction(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewaundhtransaction'
        self.manager.get_screen('ownerviewaundhtransaction')

    def viewBalTransaction(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewbalewaditransaction'
        self.manager.get_screen('ownerviewbalewaditransaction')

    def viewSanTransaction(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ownerviewsangvitransaction'
        self.manager.get_screen('ownerviewsangvitransaction')


class OwnerViewAundhTransaction(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextnextconnected'
        self.manager.get_screen('ownernextnextconnected')

    def on_enter(self):
        Total = transactions(aun_tree)
        load_text = "Total bill : " + str(round(Total[0], 2)) + "\n\nTotal amount paid : " + str(
            round(Total[1], 2)) + "\n\nTotal balance history : " + str(
            round(Total[2], 2)) + "\n\nTotal previous amount pending : " + str(
            round(Total[3], 2)) + "\n\nTotal cash discount given(received from company) : " + str(
            round(Total[4], 2)) + "\n\nTotal returned stock amount : " + str(
            round(Total[5], 2)) + "\n\nTotal expired stock amount : " + str(round(Total[6], 2))

        if Total[0] == Total[1] + Total[4] + Total[5] and Total[2] == 0:
            # bill is completely paid with 0 balance history
            self.ids.mylabel.text = load_text + "\n\nComplete amount is received! No pending amount for this time."

        elif Total[0] < Total[1] + Total[4] + Total[5] and Total[2] == 0.00:
            # bill must be paid completely and also previous amount
            self.ids.mylabel.text = load_text + "\n\nComplete amount is received for the current delivery!"

        elif Total[0] < Total[1] + Total[4] + Total[5] and Total[2] != 0:
            # bill must be paid completely and also previous amount
            self.ids.mylabel.text = load_text + "\n\nComplete amount is not received for the current delivery!"

        else:
            self.ids.mylabel.text = load_text + "\n\nComplete amount is not received! Still Pending amount left."


class OwnerViewBalewadiTransaction(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextnextconnected'
        self.manager.get_screen('ownernextnextconnected')

    def on_enter(self):
        Total = transactions(bal_tree)
        load_text = "Total bill : " + str(round(Total[0], 2)) + "\n\nTotal amount paid : " + str(
            round(Total[1], 2)) + "\n\nTotal balance history : " + str(
            round(Total[2], 2)) + "\n\nTotal previous amount pending : " + str(
            round(Total[3], 2)) + "\n\nTotal cash discount given(received from company) : " + str(
            round(Total[4], 2)) + "\n\nTotal returned stock amount : " + str(
            round(Total[5], 2)) + "\n\nTotal expired stock amount : " + str(round(Total[6], 2))

        if Total[0] == Total[1] + Total[4] + Total[5] and Total[2] == 0:
            # bill is completely paid with 0 balance history
            self.ids.mylabel.text = load_text + "\n\nComplete amount is received! No pending amount for this time."

        elif Total[0] < Total[1] + Total[4] + Total[5] and Total[2] == 0.00:
            # bill must be paid completely and also previous amount
            self.ids.mylabel.text = load_text + "\n\nComplete amount is received for the current delivery!"

        elif Total[0] < Total[1] + Total[4] + Total[5] and Total[2] != 0:
            # bill must be paid completely and also previous amount
            self.ids.mylabel.text = load_text + "\n\nComplete amount is not received for the current delivery!"

        else:
            self.ids.mylabel.text = load_text + "\n\nComplete amount is not received! Still Pending amount left."


class OwnerViewSangviTransaction(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownernextnextconnected'
        self.manager.get_screen('ownernextnextconnected')

    def on_enter(self):
        Total = transactions(san_tree)
        load_text = "Total bill : " + str(round(Total[0], 2)) + "\n\nTotal amount paid : " + str(
            round(Total[1], 2)) + "\n\nTotal balance history : " + str(
            round(Total[2], 2)) + "\n\nTotal previous amount pending : " + str(
            round(Total[3], 2)) + "\n\nTotal cash discount given(received from company) : " + str(
            round(Total[4], 2)) + "\n\nTotal returned stock amount : " + str(
            round(Total[5], 2)) + "\n\nTotal expired stock amount : " + str(round(Total[6], 2))

        if Total[0] == Total[1] + Total[4] + Total[5] and Total[2] == 0:
            # bill is completely paid with 0 balance history
            self.ids.mylabel.text = load_text + "\n\nComplete amount is received! No pending amount for this time."

        elif Total[0] < Total[1] + Total[4] + Total[5] and Total[2] == 0.00:
            # bill must be paid completely and also previous amount
            self.ids.mylabel.text = load_text + "\n\nComplete amount is received for the current delivery!"

        elif Total[0] < Total[1] + Total[4] + Total[5] and Total[2] != 0:
            # bill must be paid completely and also previous amount
            self.ids.mylabel.text = load_text + "\n\nComplete amount is not received for the current delivery!"

        else:
            self.ids.mylabel.text = load_text + "\n\nComplete amount is not received! Still Pending amount left."


# Salesman Connected Screen
class SalesManConnected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    # create bills
    def aundhbills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'auncreatebill'
        self.manager.get_screen('auncreatebill')

    def balewadibills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'balcreatebill'
        self.manager.get_screen('balcreatebill')

    def sangvibills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'sancreatebill'
        self.manager.get_screen('sancreatebill')

    # View Bills
    def viewAunBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewaundhbills'
        self.manager.get_screen('viewaundhbills')

    def viewBalBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewbalewadibills'
        self.manager.get_screen('viewbalewadibills')

    def viewSanBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'viewsangvibills'
        self.manager.get_screen('viewsangvibills')

    def viewStock(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salesviewstock'
        self.manager.get_screen('salesviewstock')

    def viewaunstock(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salesviewaunstock'
        self.manager.get_screen('salesviewaunstock')

    def viewbalstock(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salesviewbalstock'
        self.manager.get_screen('salesviewbalstock')

    def viewsanstock(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salesviewsanstock'
        self.manager.get_screen('salesviewsanstock')

    def aunviewret(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salesaunviewretailer'
        self.manager.get_screen('salesaunviewretailer')

    def balviewret(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salesbalviewretailer'
        self.manager.get_screen('salesbalviewretailer')

    def sanviewret(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'salessanviewretailer'
        self.manager.get_screen('salessanviewretailer')


class AunCreateBill(Screen):
    def disconnect(self):
        t = "Save file if bill creation completed."
        self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
        [MDRaisedButton(valign='center', text='Save', font_size='16sp', font_name='VarelaRound',
                        on_release=lambda _: self.save_aun_bill()),
         MDRaisedButton(valign='center', text='Cancel', font_size='16sp', font_name='VarelaRound',
                        on_release=lambda _: self.dialog.dismiss())], )
        self.dialog.open()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    # reset it in retailer submit
    tempbill = 0  # for maintaining bill, quantity for a retailer
    tempqty = 0
    ctr = 1

    node = []     # final retailer searched object

    # this function takes retailer name as input and searches for it in the tree and prints it in the bill
    # button -- Search Retailer
    def search_aun_ret(self, retailername):
        node = retsearch(aun_tree, retailername)
        if len(node):  # this happens only when retailer is found
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['aunspinner'].values = retlist
            self.ids['aunspinner'].text = 'Retailer List'
        else:
            self.ids.search_aun_retailer.text = "\nRetailer does not exist!"

    def printret(self, retailername):
        self.node = retsearch(aun_tree, retailername)
        try:
            if len(self.node) > 1:
                raise IndexError()
            nm = getattr(self.node[0], 'name')
            f = open("aundhbill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["\nBeat - Aundh, Pune (Samarth Enterprises)\nDate - ", str(today), "\nShop Name: ",
                      nm, "\nAddress: ", getattr(self.node[0], 'address'), "\nContact No: ",
                      getattr(self.node[0], 'contact_num'), "\n\n"])

        f.close()

    def searchmasala(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            maslist = []
            for i in range(len(node)):
                maslist.append(getattr(node[i], 'masala_name'))
            self.ids['masspinner'].values = maslist
            self.ids['masspinner'].text = 'Masala List'

    # function takes masala name and quantity as parameter and reduce it in the tree & add it in aundh outgoing stock
    # button -- Submit
    def searchmasforaundh(self, masalaname, quantity, ret_name):
        node = masalasearch(mas_tree, masalaname)
        try:
            if len(node) > 1 or len(node) == 0:  # for masala
                raise IndexError()
            if ret_name is None or len(ret_name) < 5:  # for retailer name
                raise IndexError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("aundhbill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        text = ""
        present_stock = getattr(node[0], 'stock')
        amt = getattr(node[0], 'amount')
        f.writelines(
            [str(self.ctr), "] ", getattr(node[0], 'masala_name'), "\nUnit Price:     ", str(amt), "\nQty.:     "])
        if present_stock < quantity:  # available stock is less
            text = text + "\nYou will get " + str(quantity - present_stock) + "pieces less.\n"
            self.ids.search_masala.text = text
            setattr(node[0], 'stock', 0)  # stock is over
            setattr(node[0], 'aunstk', getattr(node[0], 'aunstk') + present_stock)
            f.writelines([str(present_stock), "(Pcs), Value:     ", str(round(present_stock * amt, 2)), "\n",
                          str(quantity - present_stock), " pieces less.\n\n"])
            quantity = present_stock  # we need this for addition in bill
        else:  # stock is available
            f.writelines([str(quantity), "(Pcs), Value:     ", str(round(quantity * amt, 2)), "\n\n"])
            setattr(node[0], 'stock', present_stock - quantity)  # stock is reduced
            setattr(node[0], 'aunstk', getattr(node[0], 'aunstk') + quantity)  # increment going stock
        f.close()

        self.tempqty += quantity
        self.tempbill += round(quantity * amt, 2)
        self.ctr += 1
        self.ids['aunmasalaname'].text = ""
        self.ids['aunquantity'].text = ""

    # button -- Submit retailer
    def aun_ret_submit(self, ret_name):
        try:
            if len(ret_name) < 5 or ret_name is None:
                raise IndexError()
            f = open("aundhbill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["Shop's Quantity    ", str(self.tempqty), "(Pcs)\nShop's Order Value    ",
                      str(round(self.tempbill, 2)),
                      "\nShop's Net Order Value    ", str(round(self.tempbill, 2)),
                      "\n\n---------------------------------------------------\n"])
        f.close()

        setattr(self.node[0], 'paid', 0)
        setattr(self.node[0], 'bill', self.tempbill)
        setattr(self.node[0], 'balance', self.tempbill)
        setattr(self.node[0], 'quantity', self.tempqty)

        try:
            URL = 'http://127.0.0.1:5000/aundh_create'
            requests.get(url=URL, json=createbilltojson(aun_tree))

            URL = 'http://127.0.0.1:5000/stock_update'
            requests.get(url=URL, json=stocktojson(mas_tree))

            URL = 'http://127.0.0.1:5000/aunstk_update'
            requests.get(url=URL, json=aunstktojson(mas_tree))
        except ConnectionError:
            toast("Network Error")

        self.ids['aunretailername'].text = ""
        self.tempbill = self.tempqty = 0  # reset for new retailer
        self.ctr = 1

    # button -- Save bill
    def save_aun_bill(self):
        tq = 0
        tv = 0
        stack = []
        current = aun_tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                tq += getattr(current, 'quantity')
                tv += getattr(current, 'bill')
                current = current.right
            else:
                break

        try:
            f = open("aundhbill.txt", "at")
        except FileNotFoundError:
            t = "File is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(
            ["Total Quantity   ", str(tq), "(Pcs)\nTotal Value    ", str(round(tv, 2)), "\nTotal Net Value    ",
             str(round(tv, 2))])
        f.close()


class BalCreateBill(Screen):
    def disconnect(self):
        t = "Save file if bill creation completed."
        self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
        [MDRaisedButton(valign='center', text='Save', font_size='16sp', font_name='VarelaRound',
                        on_release=lambda _: self.save_aun_bill()),
         MDRaisedButton(valign='center', text='Cancel', font_size='16sp', font_name='VarelaRound',
                        on_release=lambda _: self.dialog.dismiss())], )
        self.dialog.open()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    # reset it in retailer submit
    tempbill = 0  # for maintaining bill, quantity & balance history for a retailer
    tempqty = 0
    ctr = 1
    node = []

    def search_bal_ret(self, retailername):
        node = retsearch(bal_tree, retailername)
        if len(node):  # this happens only when retailer is found
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['balspinner'].values = retlist
            self.ids['balspinner'].text = 'Retailer List'
        else:
            self.ids.search_bal_retailer.text = "\nRetailer does not exist!"

    def printret(self, retailername):
        self.node = retsearch(bal_tree, retailername)
        try:
            if len(self.node) > 1:
                raise IndexError()
            nm = getattr(self.node[0], 'name')
            f = open("balewadibill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["\nBeat - Balewadi, Pune (Samarth Enterprises)\nDate - ", str(today), "\nShop Name: ",
                      nm, "\nAddress: ", getattr(self.node[0], 'address'), "\nContact No: ",
                      getattr(self.node[0], 'contact_num'), "\n\n"])
        f.close()

    def searchmasala(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            maslist = []
            for i in range(len(node)):
                maslist.append(getattr(node[i], 'masala_name'))
            self.ids['masspinner'].values = maslist
            self.ids['masspinner'].text = 'Masala List'

    def searchmasforbalewadi(self, masalaname, quantity, ret_name):
        node = masalasearch(mas_tree, masalaname)
        try:
            if len(node) > 1 or len(node) == 0:  # for masala
                raise IndexError()
            if ret_name is None or len(ret_name) < 5:  # for retailer name
                raise IndexError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("balewadibill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        text = ""
        present_stock = getattr(node[0], 'stock')
        amt = getattr(node[0], 'amount')
        f.writelines(
            [str(self.ctr), "] ", getattr(node[0], 'masala_name'), "\nUnit Price:     ", str(amt), "\nQty.:     "])
        if present_stock < quantity:  # available stock is less
            text = text + "\nYou will get " + str(quantity - present_stock) + "pieces less.\n"
            self.ids.search_masala.text = text
            setattr(node[0], 'stock', 0)  # stock is over
            setattr(node[0], 'balstk', getattr(node[0], 'balstk') + present_stock)
            f.writelines([str(present_stock), "(Pcs), Value:     ", str(round(present_stock * amt, 2)), "\n",
                          str(quantity - present_stock), " pieces less.\n\n"])
            quantity = present_stock  # we need this for addition in bill
        else:  # stock is available
            f.writelines([str(quantity), "(Pcs), Value:     ", str(round(quantity * amt, 2)), "\n\n"])
            setattr(node[0], 'stock', present_stock - quantity)  # stock is reduced
            setattr(node[0], 'balstk', getattr(node[0], 'balstk') + quantity)  # increment going stock
        f.close()
        self.tempqty += quantity
        self.tempbill += round(quantity * amt, 2)
        self.ctr += 1
        self.ids['balmasalaname'].text = ""
        self.ids['balquantity'].text = ""

    # button -- Submit retailer
    def bal_ret_submit(self, ret_name):
        try:
            if len(ret_name) < 5 or ret_name is None:
                raise IndexError()
            f = open("balewadibill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["Shop's Quantity    ", str(self.tempqty), "(Pcs)\nShop's Order Value    ",
                      str(round(self.tempbill, 2)),
                      "\nShop's Net Order Value    ", str(round(self.tempbill, 2)),
                      "\n\n---------------------------------------------------\n"])
        f.close()

        setattr(self.node[0], 'paid', 0)
        setattr(self.node[0], 'bill', self.tempbill)
        setattr(self.node[0], 'balance', self.tempbill)
        setattr(self.node[0], 'quantity', self.tempqty)

        try:
            URL = 'http://127.0.0.1:5000/balewadi_create'
            requests.get(url=URL, json=createbilltojson(bal_tree))

            URL = 'http://127.0.0.1:5000/stock_update'
            requests.get(url=URL, json=stocktojson(mas_tree))

            URL = 'http://127.0.0.1:5000/balstk_update'
            requests.get(url=URL, json=balstktojson(mas_tree))

        except ConnectionError:
            toast("Network Error")

        self.ids['balretailername'].text = ""
        self.tempbill = self.tempqty = 0  # reset for new retailer
        self.ctr = 1

    # button -- Save bill
    def save_bal_bill(self):
        tq = 0
        tv = 0
        stack = []
        current = bal_tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                tq += getattr(current, 'quantity')
                tv += getattr(current, 'bill')
                current = current.right
            else:
                break

        try:
            f = open("balewadibill.txt", "at")
        except FileNotFoundError:
            t = "File is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(
            ["Total Quantity   ", str(tq), "(Pcs)\nTotal Value    ", str(round(tv, 2)), "\nTotal Net Value    ",
             str(round(tv, 2))])
        f.close()


class SanCreateBill(Screen):
    def disconnect(self):
        t = "Save file if bill creation completed."
        self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
        [MDRaisedButton(valign='center', text='Save', font_size='16sp', font_name='VarelaRound',
                        on_release=lambda _: self.save_aun_bill()),
         MDRaisedButton(valign='center', text='Cancel', font_size='16sp', font_name='VarelaRound',
                        on_release=lambda _: self.dialog.dismiss())], )
        self.dialog.open()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    tempbill = 0  # for maintaining bill, quantity & balance history for a retailer
    tempqty = 0
    ctr = 1
    node = []

    def search_san_ret(self, retailername):
        node = retsearch(san_tree, retailername)
        if len(node):  # this happens only when retailer is found
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['sanspinner'].values = retlist
            self.ids['sanspinner'].text = 'Retailer List'
        else:
            self.ids.search_san_retailer.text = "\nRetailer does not exist!"

    def printret(self, retailername):
        self.node = retsearch(san_tree, retailername)
        try:
            if len(self.node) > 1:
                raise IndexError()
            nm = getattr(self.node[0], 'name')
            f = open("sangvibill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["\nBeat - Sangvi, Pune (Samarth Enterprises)\nDate - ", str(today), "\nShop Name: ",
                      nm, "\nAddress: ", getattr(self.node[0], 'address'), "\nContact No: ",
                      getattr(self.node[0], 'contact_num'), "\n\n"])
        f.close()

    def searchmasala(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            maslist = []
            for i in range(len(node)):
                maslist.append(getattr(node[i], 'masala_name'))
            self.ids['masspinner'].values = maslist
            self.ids['masspinner'].text = 'Masala List'

    def searchmasforsangvi(self, masalaname, quantity, ret_name):
        node = masalasearch(mas_tree, masalaname)
        try:
            if len(node) > 1 or len(node) == 0:  # for masala
                raise IndexError()
            if ret_name is None or len(ret_name) < 5:  # for retailer name
                raise IndexError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("sangvibill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        text = ""
        present_stock = getattr(node[0], 'stock')
        amt = getattr(node[0], 'amount')
        f.writelines(
            [str(self.ctr), "] ", getattr(node[0], 'masala_name'), "\nUnit Price:     ", str(amt), "\nQty.:     "])
        if present_stock < quantity:  # available stock is less
            text = text + "\nYou will get " + str(quantity - present_stock) + "pieces less.\n"
            self.ids.search_masala.text = text
            setattr(node[0], 'stock', 0)  # stock is over
            setattr(node[0], 'sanstk', getattr(node[0], 'sanstk') + present_stock)
            f.writelines([str(present_stock), "(Pcs), Value:     ", str(round(present_stock * amt, 2)), "\n",
                          str(quantity - present_stock), " pieces less.\n\n"])
            quantity = present_stock  # we need this for addition in bill
        else:  # stock is available
            f.writelines([str(quantity), "(Pcs), Value:     ", str(round(quantity * amt, 2)), "\n\n"])
            setattr(node[0], 'stock', present_stock - quantity)  # stock is reduced
            setattr(node[0], 'sanstk', getattr(node[0], 'sanstk') + quantity)  # increment going stock
        f.close()
        self.tempqty += quantity
        self.tempbill += round(quantity * amt, 2)
        self.ctr += 1
        self.ids['sanmasalaname'].text = ""
        self.ids['sanquantity'].text = ""

    def san_ret_submit(self, ret_name):
        try:
            if len(ret_name) < 5 or ret_name is None:
                raise IndexError()
            f = open("sangvibill.txt", "at")
        except:
            t = "Incomplete details filled!\nFile is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["Shop's Quantity    ", str(self.tempqty), "(Pcs)\nShop's Order Value    ",
                      str(round(self.tempbill, 2)),
                      "\nShop's Net Order Value    ", str(round(self.tempbill, 2)),
                      "\n\n---------------------------------------------------\n"])
        f.close()

        setattr(self.node[0], 'paid', 0)
        setattr(self.node[0], 'bill', self.tempbill)
        setattr(self.node[0], 'balance', self.tempbill)
        setattr(self.node[0], 'quantity', self.tempqty)

        try:
            URL = 'http://127.0.0.1:5000/sangvi_create'
            requests.get(url=URL, json=createbilltojson(san_tree))

            URL = 'http://127.0.0.1:5000/stock_update'
            requests.get(url=URL, json=stocktojson(mas_tree))

            URL = 'http://127.0.0.1:5000/sanstk_update'
            requests.get(url=URL, json=sanstktojson(mas_tree))
        except ConnectionError:
            toast("Network Error")

        self.ids['sanretailername'].text = ""
        self.tempbill = self.tempqty = 0  # reset for new retailer
        self.ctr = 1

    def save_san_bill(self):
        try:
            f = open("sangvibill.txt", "at")
        except FileNotFoundError:
            t = "File is not accessible."
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=
            [MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                            on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        tq = 0
        tv = 0
        stack = []
        current = san_tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                tq += getattr(current, 'quantity')
                tv += getattr(current, 'bill')
                current = current.right
            else:
                break

        f.writelines(
            ["Total Quantity   ", str(tq), "(Pcs)\nTotal Value    ", str(round(tv, 2)), "\nTotal Net Value    ",
             str(round(tv, 2))])
        f.close()


class ViewAunBills(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def on_enter(self):
        file = open("aundhbill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def ownerback(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'ownerconnected'
        self.manager.get_screen('ownerconnected')


class ViewBalBills(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def on_enter(self):
        file = open("balewadibill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')


class ViewSanBills(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        file = open("sangvibill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file


class SalesViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 0)
        self.ids.view_masala.text = t


class SalesViewAunStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 1)
        self.ids.view_aun_masala.text = t


class SalesViewBalStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 2)
        self.ids.view_bal_masala.text = t


class SalesViewSanStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 3)
        self.ids.view_san_masala.text = t


class SalesAunViewRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += retinorder(aun_tree, 1)
        self.ids.view_aun_retailer.text = t


class SalesBalViewRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += retinorder(bal_tree, 1)
        self.ids.view_bal_retailer.text = t


class SalesSanViewRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'salesmanconnected'
        self.manager.get_screen('salesmanconnected')

    def on_enter(self):
        t = ""
        t += retinorder(san_tree, 1)
        self.ids.view_san_retailer.text = t


# Delivery Boy Connected Screen
class BoyConnected(Screen):

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def next(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def viewAunBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyviewaundhbills'
        self.manager.get_screen('boyviewaundhbills')

    def viewBalBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyviewbalewadibills'
        self.manager.get_screen('boyviewbalewadibills')

    def viewSanBills(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyviewsangvibills'
        self.manager.get_screen('boyviewsangvibills')

    def updateaunbill(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyupdateaun'
        self.manager.get_screen('boyupdateaun')

    def updatebalbill(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyupdatebal'
        self.manager.get_screen('boyupdatebal')

    def updatesanbill(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyupdatesan'
        self.manager.get_screen('boyupdatesan')

    def aundelivery(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'deliveraun'
        self.manager.get_screen('deliveraun')

    def baldelivery(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'deliverbal'
        self.manager.get_screen('deliverbal')

    def sandelivery(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'deliversan'
        self.manager.get_screen('deliversan')


class BoyViewAunBills(Screen):
    def on_enter(self):
        file = open("aundhbill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')


class BoyViewBalBills(Screen):
    def on_enter(self):
        file = open("balewadibill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')


class BoyViewSanBills(Screen):
    def on_enter(self):
        file = open("sangvibill.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')


class UpdateAundhBill(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    tempretval = 0
    tempqty = 0
    tempexpval = 0
    tempexpqty = 0

    ctr = 1
    searchedret = []
    searchedmas = []

    # retailer name as input and searches for it in the tree and prints it in the bill
    # button -- Search Retailer
    def search_aun_ret(self, retailername):
        node = retsearch(aun_tree, retailername)
        if len(node):  # this happens only when retailer is found
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['aunspinner'].values = retlist
            self.ids['aunspinner'].text = 'Retailer List'
        else:
            self.ids.search_aun_retailer.text = "\nRetailer does not exist!"

    def printret(self, retailername):
        self.searchedret = retsearch(aun_tree, retailername)
        try:
            if not retailername:  # only problem is that name can be empty
                raise ValueError()
            if len(self.searchedret) > 1:
                raise ValueError()
            f = open("aundhupdates.txt", "at")
            f.writelines(["\nBeat - Aundh, Pune (Samarth Enterprises)\nDate - ", str(today), "\nShop Name: ",
                          getattr(self.searchedret[0], 'name'), "\nAddress: ", getattr(self.searchedret[0], 'address'), "\nContact No: ",
                          getattr(self.searchedret[0], 'contact_num'), "\n\n"])
            f.close()

        except:
            t = "Incomplete details filled\nFile is not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

    def searchmasala(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            self.ids.search_masala.text = ""
            maslist = []
            for i in range(len(node)):
                maslist.append(getattr(node[i], 'masala_name'))
            self.ids['masspinner'].values = maslist
            self.ids['masspinner'].text = 'Masala List'

    # function takes masala name and quantity as parameter and reduce it in the tree & add it in aundh outgoing stock
    # button -- Submit
    def searchmasforaundh(self, masalaname, quantity, ret_name):
        self.searchedmas = masalasearch(mas_tree, masalaname)
        try:
            if not ret_name:  # only problem is that name can be empty
                raise ValueError()
            if len(self.searchedmas) > 1:
                raise IndexError()
            if not masalaname:  # only problem is that mode can be empty
                raise ValueError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("aundhupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        amt = getattr(self.searchedmas[0], 'amount')
        value = round(quantity * amt, 2)
        f.writelines([str(self.ctr), "] ", getattr(self.searchedmas[0], 'masala_name'), "\nUnit Price:     ", str(amt), "\nQty.:     ", str(quantity),
                      "(Pcs), Value:     ", str(value), "\n"])
        f.close()

        setattr(self.searchedmas[0], 'stock', getattr(self.searchedmas[0], 'stock') + quantity)

        setattr(self.searchedret[0], 'balance', getattr(self.searchedret[0], 'balance') - value)
        setattr(self.searchedret[0], 'return_stk_amt', getattr(self.searchedret[0], 'return_stk_amt') + value)
        setattr(self.searchedret[0], 'return_qty', getattr(self.searchedret[0], 'return_qty') + quantity)


        self.tempqty += quantity
        self.tempretval += value
        self.ctr += 1
        # reduce the quantity going to retailer and increment the return stock amount

        self.ids['aunmasalaname'].text = ""
        self.ids['aunquantity'].text = ""

    # button -- Submit expired masala
    def aun_expiry(self, masalaname, quantity, ret_code):
        try:
            if not ret_code:
                raise IndexError()
            if len(self.searchedmas) > 1:
                raise IndexError()
            if not masalaname:  # only problem is that mode can be empty
                raise ValueError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("aundhupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        if len(self.searchedmas) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            self.ids.search_masala.text = ""
            amt = getattr(self.searchedmas[0], 'amount')
            f.writelines(
                [str(self.ctr), "] ", getattr(self.searchedmas[0], 'masala_name'), "     (expired)\nUnit Price:     ", str(amt), "\nQty.:     ",
                 str(quantity),
                 "(Pcs), Value:     ", str(round(quantity * amt, 2)), "\n"])
            f.close()

            setattr(self.searchedmas[0], 'aunexpstk', getattr(self.searchedmas[0], 'aunexpstk') + quantity)  # add expired quantity in data
            setattr(self.searchedret[0], 'expiry_stk_amt', getattr(self.searchedret[0], 'expiry_stk_amt') + round(quantity*amt, 2))
            setattr(self.searchedret[0], 'expiry_qty', getattr(self.searchedret[0], 'expiry_qty') + quantity)
            self.tempexpqty += quantity
            self.tempexpval += round(quantity * amt, 2)
            self.ctr += 1

        self.ids['aunmasalaname'].text = ""
        self.ids['aunquantity'].text = ""

    # button -- Submit retailer
    def aun_ret_submit(self, ret_name):
        try:
            if not ret_name or len(ret_name) < 5:  # only problem is that mode can be empty
                raise ValueError()

            f = open("aundhupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        f.writelines(["\n\nShop's Return Quantity    ", str(self.tempqty), "(Pcs)\nShop's Return Value    ",
                      str(round(self.tempretval, 2)), "\nExpired Quantity     ", str(self.tempexpqty),
                      "(Pcs.)\nExpried stock value       ", str(round(self.tempexpval, 2)),
                      "\n\n---------------------------------------------------\n"])
        f.close()
        self.ids['aunretailername'].text = ""
        self.tempqty = self.tempretval = self.tempexpqty = self.tempexpval = 0
        self.ctr = 1
        try:
            URL = 'http://127.0.0.1:5000/aundh_update'
            requests.get(url=URL, json=updatebilltojson(aun_tree))


            URL = 'http://127.0.0.1:5000/stock_update'
            requests.get(url=URL, json=stocktojson(mas_tree))


            URL = 'http://127.0.0.1:5000/aunexpstk_update'
            requests.get(url=URL, json=aunexptojson(mas_tree))
        except ConnectionError:
            toast("Network Error")

    # button -- Save bill
    def save_aun_bill(self):
        try:
            f = open("aundhupdates.txt", "at")
        except:
            t = "File not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        tq = 0
        tv = 0
        teq = 0
        tev = 0

        stack = []
        current = aun_tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                tq += getattr(current, 'return_qty')
                tv += getattr(current, 'return_stk_amt')
                teq += getattr(current, 'expiry_qty')
                tev += getattr(current, 'expiry_stk_amt')
                current = current.right
            else:
                break

        f.writelines(["Total Return Quantity   ", str(tq), "(Pcs)\nTotal Return Value    ", str(round(tv, 2)),
                      "\nTotal Expired Quantity    ", str(teq), "(Pcs)\nTotal Expired Stock Value    ",
                      str(round(tev, 2))])
        f.close()


class UpdateBalewadiBill(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    tempretval = 0
    tempqty = 0
    tempexpval = 0
    tempexpqty = 0
    ctr = 1
    searchedret = []
    searchedmas = []

    # retailer name as input and searches for it in the tree and prints it in the bill
    # button -- Search Retailer
    def search_bal_ret(self, retailername):
        node = retsearch(bal_tree, retailername)
        if len(node):  # this happens only when retailer is found
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['balspinner'].values = retlist
            self.ids['balspinner'].text = 'Retailer List'
        else:
            self.ids.search_bal_retailer.text = "\nRetailer does not exist!"

    def printret(self, retailername):
        self.searchedret = retsearch(bal_tree, retailername)
        try:
            if not retailername:  # only problem is that name can be empty
                raise ValueError()
            if len(self.searchedret) > 1:
                raise ValueError()
            f = open("balupdates.txt", "at")
            f.writelines(["\nBeat - Balewadi, Pune (Samarth Enterprises)\nDate - ", str(today), "\nShop Name: ",
                          getattr(self.searchedret[0], 'name'), "\nAddress: ", getattr(self.searchedret[0], 'address'),
                          "\nContact No: ",
                          getattr(self.searchedret[0], 'contact_num'), "\n\n"])
            f.close()
        except:
            t = "Incomplete details filled\nFile is not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

    def searchmasala(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            self.ids.search_masala.text = ""
            maslist = []
            for i in range(len(node)):
                maslist.append(getattr(node[i], 'masala_name'))
            self.ids['masspinner'].values = maslist
            self.ids['masspinner'].text = 'Masala List'

    def searchmasforbalewadi(self, masalaname, quantity, ret_name):
        self.searchedmas = masalasearch(mas_tree, masalaname)
        try:
            if not ret_name:  # only problem is that name can be empty
                raise ValueError()
            if len(self.searchedmas) > 1:
                raise IndexError()
            if not masalaname:  # only problem is that mode can be empty
                raise ValueError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("balupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        amt = getattr(self.searchedmas[0], 'amount')
        value = round(quantity * amt, 2)
        f.writelines(
            [str(self.ctr), "] ", getattr(self.searchedmas[0], 'masala_name'), "\nUnit Price:     ", str(amt), "\nQty.:     ", str(quantity),
             "(Pcs), Value:     ", str(value), "\n"])
        f.close()
        setattr(self.searchedmas[0], 'stock',
                getattr(self.searchedmas[0], 'stock') + quantity)  # add returned quantity in the stock

        setattr(self.searchedret[0], 'balance', getattr(self.searchedret[0], 'balance') - value)
        setattr(self.searchedret[0], 'return_stk_amt', getattr(self.searchedret[0], 'return_stk_amt') + value)
        self.tempqty += quantity
        self.tempbh -= value
        self.tempretval += value
        self.ctr += 1
        # reduce the quantity going to retailer and increment the return stock amount
        self.ids['balmasalaname'].text = ""
        self.ids['balquantity'].text = ""

    def bal_expiry(self, masalaname, quantity, ret_code):
        try:
            if not ret_code:
                raise IndexError()
            if len(self.searchedmas) > 1:
                raise IndexError()
            if not masalaname:  # only problem is that mode can be empty
                raise ValueError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("balupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        if len(self.searchedmas) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            self.ids.search_masala.text = ""
            amt = getattr(self.searchedmas[0], 'amount')
            f.writelines(
                [str(self.ctr), "] ", getattr(self.searchedmas[0], 'masala_name'), "     (expired)\nUnit Price:     ", str(amt),
                 "\nQty.:     ",
                 str(quantity),
                 "(Pcs), Value:     ", str(round(quantity * amt, 2)), "\n"])
            f.close()
            setattr(self.searchedmas[0], 'balexpstk',
                    getattr(self.searchedmas[0], 'balexpstk') + quantity)  # add expired quantity in data

            setattr(self.searchedret[0], 'expiry_stk_amt',
                    getattr(self.searchedret[0], 'expiry_stk_amt') + round(quantity * amt, 2))
            self.tempexpqty += quantity
            self.tempexpval += round(quantity * amt, 2)
            self.ctr += 1

        self.ids['balmasalaname'].text = ""
        self.ids['balquantity'].text = ""

    def bal_ret_submit(self, ret_name):
        try:
            if not ret_name or len(ret_name) < 5:  # only problem is that mode can be empty
                raise ValueError()
            f = open("balupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["\n\nShop's Return Quantity    ", str(self.tempqty), "(Pcs)\nShop's Return Value    ",
                      str(round(self.tempretval, 2)), "\nExpired Quantity     ", str(self.tempexpqty),
                      "(Pcs.)\nExpried stock value       ", str(round(self.tempexpval, 2)),
                      "\n\n---------------------------------------------------\n"])
        f.close()
        self.ids['balretailername'].text = ""
        self.tempqty = self.tempretval = self.tempexpqty = self.tempexpval = 0
        self.ctr = 1

        try:
            URL = 'http://127.0.0.1:5000/balewadi_update'
            r = requests.get(url=URL, json=updatebilltojson(bal_tree))

            URL = 'http://127.0.0.1:5000/stock_update'
            requests.get(url=URL, json=stocktojson(mas_tree))

            URL = 'http://127.0.0.1:5000/balexpstk_update'
            requests.get(url=URL, json=balexptojson(mas_tree))
        except ConnectionError:
            toast("Network Error")

    def save_bal_bill(self):
        try:
            f = open("balupdates.txt", "at")
        except:
            t = "File not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        tq = 0
        tv = 0
        teq = 0
        tev = 0
        stack = []
        current = bal_tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                tq += getattr(current, 'return_qty')
                tv += getattr(current, 'return_stk_amt')
                teq += getattr(current, 'expiry_qty')
                tev += getattr(current, 'expiry_stk_amt')
                current = current.right
            else:
                break
        f.writelines(["Total Return Quantity   ", str(tq), "(Pcs)\nTotal Return Value    ", str(round(tv, 2)),
                      "\nTotal Expired Quantity    ", str(teq), "(Pcs)\nTotal Expired Stock Value    ",
                      str(round(tev, 2))])
        f.close()


class UpdateSangviBill(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    tempretval = 0
    tempqty = 0
    tempexpval = 0
    tempexpqty = 0
    ctr = 1
    searchedret = []
    searchedmas = []

    # retailer name as input and searches for it in the tree and prints it in the bill
    # button -- Search Retailer
    def search_san_ret(self, retailername):
        node = retsearch(san_tree, retailername)
        if len(node):  # this happens only when retailer is found
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['sanspinner'].values = retlist
            self.ids['sanspinner'].text = 'Retailer List'
        else:
            self.ids.search_aun_retailer.text = "\nRetailer does not exist!"

    def printret(self, retailername):
        self.searchedret = retsearch(san_tree, retailername)
        try:
            if not retailername:  # only problem is that name can be empty
                raise ValueError()
            if len(self.searchedret) > 1:
                raise ValueError()
            f = open("sanupdates.txt", "at")
            f.writelines(["\nBeat - Sangvi, Pune (Samarth Enterprises)\nDate - ", str(today), "\nShop Name: ",
                          getattr(self.searchedret[0], 'name'), "\nAddress: ", getattr(self.searchedret[0], 'address'),
                          "\nContact No: ",
                          getattr(self.searchedret[0], 'contact_num'), "\n\n"])
            f.close()
        except:
            t = "Incomplete details filled\nFile is not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

    def searchmasala(self, masalaname):
        node = masalasearch(mas_tree, masalaname)
        if len(node) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            self.ids.search_masala.text = ""
            maslist = []
            for i in range(len(node)):
                maslist.append(getattr(node[i], 'masala_name'))
            self.ids['masspinner'].values = maslist
            self.ids['masspinner'].text = 'Masala List'

    def searchmasforsangvi(self, masalaname, quantity, ret_name):
        self.searchedmas = masalasearch(mas_tree, masalaname)
        try:
            if not ret_name:  # only problem is that name can be empty
                raise ValueError()
            if len(self.searchedmas) > 1:
                raise IndexError()
            if not masalaname:  # only problem is that mode can be empty
                raise ValueError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("sanupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        amt = getattr(self.searchedmas[0], 'amount')
        value = round(quantity * amt, 2)
        f.writelines(
            [str(self.ctr), "] ", getattr(self.searchedmas[0], 'masala_name'), "\nUnit Price:     ", str(amt), "\nQty.:     ", str(quantity),
             "(Pcs), Value:     ", str(value), "\n"])
        f.close()
        setattr(self.searchedmas[0], 'stock',
                getattr(self.searchedmas[0], 'stock') + quantity)  # add returned quantity in the stock

        setattr(self.searchedret[0], 'balance', getattr(self.searchedret[0], 'balance') - value)
        setattr(self.searchedret[0], 'return_stk_amt', getattr(self.searchedret[0], 'return_stk_amt') + value)
        self.tempqty += quantity
        self.tempbh -= value
        self.tempretval += value
        self.ctr += 1
        # reduce the quantity going to retailer and increment the return stock amount
        self.ids['sanmasalaname'].text = ""
        self.ids['sanquantity'].text = ""

    def san_expiry(self, masalaname, quantity, ret_code):
        try:
            if not ret_code:
                raise IndexError()
            if len(self.searchedmas) > 1:
                raise IndexError()
            if not masalaname:  # only problem is that mode can be empty
                raise ValueError()
            quantity = int(quantity)
            if quantity < 0:
                abs(quantity)
            if quantity == 0:
                raise ValueError()
            f = open("sanupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        if len(self.searchedmas) == 0:
            self.ids.search_masala.text = "\nMasala does not exist!\n"
        else:
            self.ids.search_masala.text = ""
            amt = getattr(self.searchedmas[0], 'amount')
            f.writelines(
                [str(self.ctr), "] ", getattr(self.searchedmas[0], 'masala_name'), "     (expired)\nUnit Price:     ", str(amt),
                 "\nQty.:     ",
                 str(quantity),
                 "(Pcs), Value:     ", str(round(quantity * amt, 2)), "\n"])
            f.close()
            setattr(self.searchedmas[0], 'sanexpstk',
                    getattr(self.searchedmas[0], 'sanexpstk') + quantity)  # add expired quantity in data
            setattr(self.searchedret[0], 'expiry_stk_amt',
                    getattr(self.searchedret[0], 'expiry_stk_amt') + round(quantity * amt, 2))
            self.tempexpqty += quantity
            self.tempexpval += round(quantity * amt, 2)
            self.ctr += 1

        self.ids['sanmasalaname'].text = ""
        self.ids['sanquantity'].text = ""

    def san_ret_submit(self, ret_name):
        try:
            if not ret_name or len(ret_name) < 5:  # only problem is that mode can be empty
                raise ValueError()
            f = open("sanupdates.txt", "at")
        except:
            t = "Incomplete details filled\nFile not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        f.writelines(["\n\nShop's Return Quantity    ", str(self.tempqty), "(Pcs)\nShop's Return Value    ",
                      str(round(self.tempretval, 2)), "\nExpired Quantity     ", str(self.tempexpqty),
                      "(Pcs.)\nExpried stock value       ", str(round(self.tempexpval, 2)),
                      "\n\n---------------------------------------------------\n"])
        f.close()
        self.ids['sanretailername'].text = ""
        self.tempqty = self.tempretval = self.tempexpqty = self.tempexpval = 0
        self.ctr = 1
        try:
            URL = 'http://127.0.0.1:5000/san_update'
            requests.get(url=URL, json=updatebilltojson(san_tree))

            URL = 'http://127.0.0.1:5000/stock_update'
            r = requests.get(url=URL, json=stocktojson(mas_tree))

            URL = 'http://127.0.0.1:5000/sanexpstk_update'
            requests.get(url=URL, json=sanexptojson(mas_tree))
        except:
            toast("Network Error")

    def save_san_bill(self):
        try:
            f = open("sanupdates.txt", "at")
        except:
            t = "File not accessible"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        tq = 0
        tv = 0
        teq = 0
        tev = 0
        stack = []
        current = san_tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                tq += getattr(current, 'return_qty')
                tv += getattr(current, 'return_stk_amt')
                teq += getattr(current, 'expiry_qty')
                tev += getattr(current, 'expiry_stk_amt')
                current = current.right
            else:
                break
        f.writelines(["Total Return Quantity   ", str(tq), "(Pcs)\nTotal Return Value    ", str(round(tv, 2)),
                      "\nTotal Expired Quantity    ", str(teq), "(Pcs)\nTotal Expired Stock Value    ",
                      str(round(tev, 2))])
        f.close()


class AunContent(BoxLayout):
    pass


class BalContent(BoxLayout):
    pass


class SanContent(BoxLayout):
    pass


class DeliveryAundh(Screen):
    def disconnect(self):
        self.aunsavechange()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.aunsavechange()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    def search_aun_ret(self, retailername):
        node = retsearch(aun_tree, retailername)
        if len(node):
            self.ids.search_aun_retailer.text = ""
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['aunspinner'].values = retlist
            self.ids['aunspinner'].text = 'Retailer List'
        else:
            self.ids.search_aun_retailer.text = "\nRetailer does not exist!"

    def previous_history(self, retailername):
        node = retsearch(aun_tree, retailername)
        try:
            if len(node) > 1:
                raise IndexError()
            ap = float(getattr(node[0], 'amount_paid'))
            ph = getattr(node[0], 'previous_history')
        except:
            t = "Incomplete details filled"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        t = "Previous Balance Rs." + str(ph)
        self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', content_cls=AunContent(),
                               buttons=[
                                   MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                                                  on_release=lambda _: self.dialog.dismiss()),
                                   MDRaisedButton(valign='center', text='Pay', font_size='16sp',
                                                  font_name='VarelaRound',
                                                  on_release=lambda _: self.setdata(retailername,
                                                                                    self.dialog.content_cls.ids.aunqty.text,
                                                                                    ap, ph))], )
        self.dialog.open()

    def setdata(self, retailername, amount, ap, ph):
        try:
            amt = round(float(amount), 2)
        except:
            return
        node = retsearch(aun_tree, retailername)
        setattr(node[0], 'amount_paid', float(ap) + amt)
        setattr(node[0], 'previous_history', float(ph) - amt)
        self.dialog.content_cls.ids.aunqty.text = ""

    def aundelivery(self, retailername, amount, md):

        node = retsearch(aun_tree, retailername)  # searching by fullname
        try:
            ap = float(getattr(node[0], 'amount_paid'))
            bh = float(getattr(node[0], 'balance'))
            amt = round(float(amount), 2)
            if not md:  # only problem is that mode can be empty
                raise ValueError()
            if len(node) > 1:
                raise IndexError()
        except:
            t = "Incomplete details filled"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        if amt > bh or amt < 0:     # wrong user input
            if bh == 0:
                t = "\nNo pending amount for current bill!"
            else:
                t = "\nPay amount less than or equal to " + str(bh)
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        if bh >= 10000:  # first check bill > 10000 then amount > 10000
            if amt >= 10000 and amt == bh:  # total amount is paid by cash then only cd
                if md == "CASH" or md == "cash" or md == "Cash":
                    cd = round(amt / 50, 2)
                    text = "Cash discount = " + str(cd) + "\nPay only " + str(round(amt - cd, 2))
                    self.ids.aundelivery.text = text
                    setattr(node[0], 'amount_paid', ap + amt - cd)
                    setattr(node[0], 'balance', bh - amt)
                    setattr(node[0], 'mode', "CASH")
                    setattr(node[0], 'cd', float(getattr(node[0], 'cd')) + cd)
                    setattr(node[0], 'paid', 1)
                    setattr(node[0], 'previous_history', 0)

                elif md == "CHEQUE" or md == "cheque" or md == "Cheque":    # total amount is paid
                    text = "NO Cash discount!\nYou have opted for 7 day cheque."
                    self.ids.aundelivery.text = text
                    setattr(node[0], 'amount_paid', ap + amt)
                    setattr(node[0], 'balance', bh - amt)
                    setattr(node[0], 'mode', "CHEQUE")
                    setattr(node[0], 'paid', 1)
                    setattr(node[0], 'previous_history', 0)

            elif amt != bh:
                self.ids.aundelivery.text = ""
                setattr(node[0], 'amount_paid', ap + amt)
                setattr(node[0], 'mode', md)
                setattr(node[0], 'balance', 0)
                setattr(node[0], 'previous_history', bh - amt)

        elif bh < 10000:
            self.ids.aundelivery.text = ""
            setattr(node[0], 'amount_paid', ap + amt)
            setattr(node[0], 'balance', 0)
            setattr(node[0], 'mode', md)
            setattr(node[0], 'previous_history', bh - amt)
            if amt == bh:
                setattr(node[0], 'paid', 1)

        self.ids['aunamount'].text = ""
        self.ids['aunmode'].text = ""

    def aunsavechange(self):
        try:
            URL = 'http://127.0.0.1:5000/aundh_delivery'
            requests.get(url=URL, json=deliverbilltojson(aun_tree))
        except ConnectionError:
            toast("Network Error")


class DeliveryBalewadi(Screen):
    def disconnect(self):
        self.balsavechange()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.balsavechange()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    def search_bal_ret(self, retailername):
        node = retsearch(bal_tree, retailername)
        if len(node):  # this happens only when retailer is found
            self.ids.search_bal_retailer.text = ""
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['balspinner'].values = retlist
            self.ids['balspinner'].text = 'Retailer List'
        else:
            self.ids.search_bal_retailer.text = "\nRetailer does not exist!"

    def previous_history(self, retailername):
        node = retsearch(bal_tree, retailername)
        try:
            if len(node) > 1:
                raise IndexError()
            ap = float(getattr(node[0], 'amount_paid'))
            ph = getattr(node[0], 'previous_history')
        except:
            t = "Incomplete details filled"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        t = "Previous Balance Rs." + str(ph)
        self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', content_cls=BalContent(),
                               buttons=[
                                   MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                                                  on_release=lambda _: self.dialog.dismiss()),
                                   MDRaisedButton(valign='center', text='Pay', font_size='16sp',
                                                  font_name='VarelaRound',
                                                  on_release=lambda _: self.setdata(retailername,
                                                                                    self.dialog.content_cls.ids.balqty.text,
                                                                                    ap, ph))], )
        self.dialog.open()

    def setdata(self, retailername, amount, ap, ph):
        try:
            amt = round(float(amount), 2)
        except:
            return
        node = retsearch(bal_tree, retailername)
        setattr(node[0], 'amount_paid', float(ap) + amt)
        setattr(node[0], 'previous_history', float(ph) - amt)
        self.dialog.content_cls.ids.balqty.text = ""

    def baldelivery(self, retailername, amount, md):
        node = retsearch(bal_tree, retailername)
        try:
            ap = float(getattr(node[0], 'amount_paid'))
            bh = float(getattr(node[0], 'balance'))
            amt = round(float(amount), 2)
            if not md:  # only problem is that mode can be empty
                raise ValueError()
            if len(node) > 1:
                raise IndexError()
        except:
            t = "Incomplete details filled"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        if amt > bh or amt < 0:
            if bh == 0:
                t = "There is no balance left. Don't pay anything!"
            else:
                t = "Pay amount less than or equal to " + str(bh)
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom',
                                   buttons=[
                                       MDRaisedButton(valign='center', text='OK', font_size='16sp',
                                                      font_name='VarelaRound',
                                                      on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        if bh >= 10000:  # first check bill > 10000 then amount > 10000
            if amt >= 10000 and amt == bh:  # total amount is paid then only cd
                if md == "CASH" or md == "cash" or md == "Cash":
                    cd = round(amt / 50, 2)
                    text = "Cash discount = " + str(cd) + "\nPay only " + str(round(amt - cd, 2))
                    self.ids.baldelivery.text = text
                    setattr(node[0], 'amount_paid', ap + amt - cd)
                    setattr(node[0], 'balance', bh - amt)
                    setattr(node[0], 'mode', "CASH")
                    setattr(node[0], 'cd', float(getattr(node[0], 'cd')) + cd)
                    setattr(node[0], 'paid', 1)
                    setattr(node[0], 'previous_history', 0)

                elif md == "CHEQUE" or md == "cheque" or md == "Cheque":
                    text = "NO Cash discount!\nYou have opted for 7 day cheque."
                    self.ids.baldelivery.text = text
                    setattr(node[0], 'amount_paid', ap + amt)
                    setattr(node[0], 'balance', bh - amt)
                    setattr(node[0], 'mode', "CHEQUE")
                    setattr(node[0], 'paid', 1)
                    setattr(node[0], 'previous_history', 0)

            elif amt != bh:
                self.ids.baldelivery.text = ""
                setattr(node[0], 'amount_paid', ap + amt)
                setattr(node[0], 'balance', 0)
                setattr(node[0], 'mode', md)
                setattr(node[0], 'previous_history', bh - amt)

        elif bh < 10000:
            self.ids.baldelivery.text = ""
            setattr(node[0], 'amount_paid', ap + amt)
            setattr(node[0], 'balance', 0)
            setattr(node[0], 'mode', md)
            setattr(node[0], 'previous_history', bh - amt)
            if amt == bh:
                setattr(node[0], 'paid', 1)

        self.ids['balamount'].text = ""
        self.ids['balmode'].text = ""

    def balsavechange(self):
        try:
            URL = 'http://127.0.0.1:5000/balewadi_delivery'
            requests.get(url=URL, json=deliverbilltojson(bal_tree))
        except ConnectionError:
            toast("Network Error")


class DeliverySangvi(Screen):
    def disconnect(self):
        self.sansavechange()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.sansavechange()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    def search_san_ret(self, retailername):
        node = retsearch(san_tree, retailername)
        if len(node):
            self.ids.search_san_retailer.text = ""
            retlist = []
            for i in range(len(node)):
                retlist.append(getattr(node[i], 'name'))
            self.ids['sanspinner'].values = retlist
            self.ids['sanspinner'].text = 'Retailer List'
        else:
            self.ids.search_san_retailer.text = "\nRetailer does not exist!"

    def previous_history(self, retailername):
        node = retsearch(san_tree, retailername)
        try:
            if len(node) > 1:
                raise IndexError()
            ap = getattr(node[0], 'amount_paid')
            ph = getattr(node[0], 'previous_history')
        except:
            t = "Incomplete details filled"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        t = "Previous Balance Rs." + str(ph)
        self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', content_cls=SanContent(),
                               buttons=[
                                   MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                                                  on_release=lambda _: self.dialog.dismiss()),
                                   MDRaisedButton(valign='center', text='Pay', font_size='16sp',
                                                  font_name='VarelaRound',
                                                  on_release=lambda _: self.setdata(retailername,
                                                                                    self.dialog.content_cls.ids.sanqty.text,
                                                                                    ap, ph))], )
        self.dialog.open()

    def setdata(self, retailername, amount, ap, ph):
        try:
            amt = round(float(amount), 2)
        except:
            return
        node = retsearch(san_tree, retailername)
        setattr(node[0], 'amount_paid', float(ap) + amt)
        setattr(node[0], 'previous_history', float(ph) - amt)
        self.dialog.content_cls.ids.sanqty.text = ""

    def sandelivery(self, retailername, amount, md):
        node = retsearch(san_tree, retailername)
        try:
            ap = getattr(node[0], 'amount_paid')
            bh = getattr(node[0], 'balance')
            amt = round(float(amount), 2)
            if not md:  # only problem is that mode can be empty
                raise ValueError()
            if len(node) > 1:
                raise IndexError()
        except:
            t = "Incomplete details filled"
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', buttons=[
                MDRaisedButton(valign='center', text='OK', font_size='16sp', font_name='VarelaRound',
                               on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return

        if amt > bh or amt < 0:
            if bh == 0:
                t = "There is no balance left. Don't pay anything!"
            else:
                t = "Pay amount less than or equal to " + str(bh)
            self.dialog = MDDialog(title=t, size_hint=(0.8, 1), type='custom', content_cls=SanContent(),
                                   buttons=[
                                       MDRaisedButton(valign='center', text='OK', font_size='16sp',
                                                      font_name='VarelaRound',
                                                      on_release=lambda _: self.dialog.dismiss())], )
            self.dialog.open()
            return
        if bh >= 10000:  # first check bill > 10000 then amount > 10000
            if amt >= 10000 and amt == bh:  # total amount is paid then only cd
                if md == "CASH" or md == "cash" or md == "Cash":
                    cd = round(amt / 50, 2)
                    text = "Cash discount = " + str(cd) + "\nPay only " + str(round(amt - cd, 2))
                    self.ids.sandelivery.text = text
                    setattr(node[0], 'amount_paid', ap + amt - cd)
                    setattr(node[0], 'balance', float(getattr(node[0], 'balance')) - amt)
                    setattr(node[0], 'mode', "CASH")
                    setattr(node[0], 'cd', float(getattr(node[0], 'cd')) + cd)
                    setattr(node[0], 'paid', 1)
                    setattr(node[0], 'previous_history', 0)

                elif md == "CHEQUE" or md == "cheque" or md == "Cheque":
                    text = "NO Cash discount!\nYou have opted for 7 day cheque."
                    self.ids.sandelivery.text = text
                    setattr(node[0], 'amount_paid', ap + amt)
                    setattr(node[0], 'balance', float(getattr(node[0], 'balance')) - amt)
                    setattr(node[0], 'mode', "CHEQUE")
                    setattr(node[0], 'paid', 1)
                    setattr(node[0], 'previous_history', 0)

            elif amt != bh:
                self.ids.sandelivery.text = ""
                setattr(node[0], 'amount_paid', ap + amt)
                setattr(node[0], 'balance', 0)
                setattr(node[0], 'mode', md)
                setattr(node[0], 'previous_history', bh - amt)

        elif bh < 10000:
            self.ids.sandelivery.text = ""
            setattr(node[0], 'amount_paid', ap + amt)
            setattr(node[0], 'balance', 0)
            setattr(node[0], 'mode', md)
            setattr(node[0], 'previous_history', bh - amt)
            if amt == bh:
                setattr(node[0], 'paid', 1)

        self.ids['sanamount'].text = ""
        self.ids['sanmode'].text = ""

    def sansavechange(self):
            try:
                URL = 'http://127.0.0.1:5000/sangvi_delivery'
                requests.get(url=URL, json=deliverbilltojson(san_tree))
            except ConnectionError:
                    toast("Network Error")


# Delivery Boy Next Connected Screen
class BoyNextConnected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boyconnected'
        self.manager.get_screen('boyconnected')

    def viewaunmasala(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyviewaunstock'
        self.manager.get_screen('boyviewaunstock')

    def viewbalmasala(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyviewbalstock'
        self.manager.get_screen('boyviewbalstock')

    def viewsanmasala(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyviewsanstock'
        self.manager.get_screen('boyviewsanstock')

    def viewpendaun(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boyaunpending'
        self.manager.get_screen('boyaunpending')

    def viewpendbal(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boybalpending'
        self.manager.get_screen('boybalpending')

    def viewpendsan(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'boysanpending'
        self.manager.get_screen('boysanpending')


class BoyAunViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 1)
        self.ids.view_aun_masala.text = t


class BoyBalViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 2)
        self.ids.view_bal_masala.text = t


class BoySanViewStock(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def on_enter(self):
        t = ""
        t += masinorder(mas_tree, 3)
        self.ids.view_san_masala.text = t


class BoyAunPendingRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def on_enter(self):
        t = ""
        t += retinorder(aun_tree, 0)
        self.ids.pending_aun.text = t


class BoyBalPendingRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def on_enter(self):
        t = ""
        t += retinorder(bal_tree, 0)
        self.ids.pending_bal.text = t


class BoySanPendingRetailer(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'boynextconnected'
        self.manager.get_screen('boynextconnected')

    def on_enter(self):
        t = ""
        t += retinorder(san_tree, 0)
        self.ids.pending_san.text = t
