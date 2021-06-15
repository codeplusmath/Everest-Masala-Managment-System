from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivymd.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivymd.toast import toast
import requests
from connected import *
#from kivymd.toast import toast
import os

LabelBase.register(name='DelaGothic', fn_regular='.\Assest\DelaGothicOne-Regular.ttf')
LabelBase.register(name='Mukta-Medium', fn_regular='.\Assest\Mukta-Medium.ttf')
LabelBase.register(name='Mukta-SemiBold', fn_regular='.\Assest\Mukta-SemiBold.ttf')
LabelBase.register(name='VarelaRound', fn_regular='.\Assest\VarelaRound-Regular.ttf')
Window.clearcolor = (1,1,1,1)


class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = MDApp.get_running_app()

        app.username = loginText
        app.password = passwordText

        try:
            URL = 'http://127.0.0.1:5000/user'
            r = requests.get(url=URL)
            data = r.json()
        except:
            toast('Network Error')
            return

        for x in data:
            if app.username == x[0]:
                if app.password == x[1]:
                    if x[2] == "owner":
                        self.ids.loginerror.text = ""
                        self.manager.transition = SlideTransition(direction="left")
                        self.manager.current = 'ownerconnected'
                        break
                    elif x[2] == "salesman":
                        self.ids.loginerror.text = ""
                        self.manager.transition = SlideTransition(direction="left")
                        self.manager.current = 'salesmanconnected'
                        break
                    elif x[2] == "boy":
                        self.ids.loginerror.text = ""
                        self.manager.transition = SlideTransition(direction="left")
                        self.manager.current = 'boyconnected'
                        break
            else:
                self.ids.loginerror.text = "incorrect username or password"

    def resetForm(self):
        self.ids['password'].text = ""


class EverestApp(MDApp):
    username = StringProperty(None)
    password = StringProperty(None)
    dialog = None

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))

        manager.add_widget(OwnerConnected(name='ownerconnected'))
        manager.add_widget(OwnerViewAunBills(name='ownerviewaundhbills'))
        manager.add_widget(OwnerViewBalBills(name='ownerviewbalewadibills'))
        manager.add_widget(OwnerViewSanBills(name='ownerviewsangvibills'))
        manager.add_widget(OwnerViewAunUpdates(name='ownerviewaundhupdates'))
        manager.add_widget(OwnerViewBalUpdates(name='ownerviewbalewadiupdates'))
        manager.add_widget(OwnerViewSanUpdates(name='ownerviewsangviupdates'))
        manager.add_widget(AunViewStock(name='viewaunstock'))
        manager.add_widget(BalViewStock(name='viewbalstock'))
        manager.add_widget(SanViewStock(name='viewsanstock'))

        manager.add_widget(OwnerNextConnected(name='ownernextconnected'))
        manager.add_widget(ViewStock(name='viewstock'))
        manager.add_widget(SearchMasala(name='searchmasala'))
        manager.add_widget(UpdateStock(name='updatestock'))
        manager.add_widget(AunSearchRetailer(name='aunsearchretailer'))
        manager.add_widget(BalSearchRetailer(name='balsearchretailer'))
        manager.add_widget(SanSearchRetailer(name='sansearchretailer'))
        manager.add_widget(AunViewRetailer(name='aunviewretailer'))
        manager.add_widget(BalViewRetailer(name='balviewretailer'))
        manager.add_widget(SanViewRetailer(name='sanviewretailer'))
        manager.add_widget(AunPendingRetailer(name='aunpending'))
        manager.add_widget(BalPendingRetailer(name='balpending'))
        manager.add_widget(SanPendingRetailer(name='sanpending'))

        manager.add_widget(OwnerNextNextConnected(name='ownernextnextconnected'))
        manager.add_widget(OwnerViewAundhTransaction(name='ownerviewaundhtransaction'))
        manager.add_widget(OwnerViewBalewadiTransaction(name='ownerviewbalewaditransaction'))
        manager.add_widget(OwnerViewSangviTransaction(name='ownerviewsangvitransaction'))

        manager.add_widget(SalesManConnected(name='salesmanconnected'))
        manager.add_widget(AunCreateBill(name='auncreatebill'))
        manager.add_widget(BalCreateBill(name='balcreatebill'))
        manager.add_widget(SanCreateBill(name='sancreatebill'))
        manager.add_widget(ViewAunBills(name='viewaundhbills'))
        manager.add_widget(ViewBalBills(name='viewbalewadibills'))
        manager.add_widget(ViewSanBills(name='viewsangvibills'))
        manager.add_widget(SalesViewStock(name='salesviewstock'))
        manager.add_widget(SalesViewAunStock(name='salesviewaunstock'))
        manager.add_widget(SalesViewBalStock(name='salesviewbalstock'))
        manager.add_widget(SalesViewSanStock(name='salesviewsanstock'))
        manager.add_widget(SalesAunViewRetailer(name='salesaunviewretailer'))
        manager.add_widget(SalesBalViewRetailer(name='salesbalviewretailer'))
        manager.add_widget(SalesSanViewRetailer(name='salessanviewretailer'))

        manager.add_widget(BoyConnected(name='boyconnected'))
        manager.add_widget(BoyViewAunBills(name='boyviewaundhbills'))
        manager.add_widget(BoyViewBalBills(name='boyviewbalewadibills'))
        manager.add_widget(BoyViewSanBills(name='boyviewsangvibills'))
        manager.add_widget(UpdateAundhBill(name='boyupdateaun'))
        manager.add_widget(UpdateBalewadiBill(name='boyupdatebal'))
        manager.add_widget(UpdateSangviBill(name='boyupdatesan'))
        manager.add_widget(DeliveryAundh(name='deliveraun'))
        manager.add_widget(DeliveryBalewadi(name='deliverbal'))
        manager.add_widget(DeliverySangvi(name='deliversan'))

        manager.add_widget(BoyNextConnected(name='boynextconnected'))
        manager.add_widget(BoyAunViewStock(name='boyviewaunstock'))
        manager.add_widget(BoyBalViewStock(name='boyviewbalstock'))
        manager.add_widget(BoySanViewStock(name='boyviewsanstock'))
        manager.add_widget(BoyAunPendingRetailer(name='boyaunpending'))
        manager.add_widget(BoyBalPendingRetailer(name='boybalpending'))
        manager.add_widget(BoySanPendingRetailer(name='boysanpending'))

        self.theme_cls.primary_palette = 'Indigo'
        return manager

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    EverestApp().run()
