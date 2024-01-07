from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from database import DataBase
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.namee.text, self.email.text, self.password.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
                self.reset()
        else:
            invalidForm()
            self.reset()
            
    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            db.userspersonal(self.email.text)
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
            self.reset()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class Introduction(Screen):
    def login(self):
        sm.current = "login"

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        global e
        name, created = db.get_user(self.current)
        e=self.current
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
    def btn(self):
        show_popup.show(self)
    def deleteaccount(self):
        db.uspaac()
    
class AddPassword(Screen):
    namee = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def submit(self):
        if self.namee.text != "" and self.username.text != "" and self.password.text != "" :
            if self.password != "":
                db.add_password(e,self.namee.text,self.username.text, self.password.text)
                self.reset()
                addsucess()
                sm.current = "main"
            else:
                invalidForm()
                self.reset()
        else:
            invalidForm()
            self.reset()
    def Back(self):
        self.reset()
        sm.current = "main"
        
    def reset(self):
        self.username.text = ""
        self.password.text = ""
        self.namee.text = ""
    
class LookPassword(Screen):
        def on_enter(self):
            d=db.show_records(e)
            word=''
            self.ids.word_label.text=""
            for r in d:
                word=f'{word}\n{r}'
                self.ids.word_label.text=f'{word}'
        def Back(self):
            sm.current = "main"
        
class DeletePassword(Screen):
    namee = ObjectProperty(None)
    username = ObjectProperty(None)
    def submit(self):
        if self.namee.text != "" and self.username.text != "":
            if db.delpassval(e,self.namee.text,self.username.text)==True:
                db.delete_password(e,self.namee.text,self.username.text)
                self.reset()
                deletesucess()
                sm.current = "main"
            else:
                invalidDetails()
                self.reset()
        else:
            invalidForm()
            self.reset()
    def delbtn(self):
        if db.dvalidate(self.namee.text,self.username.text):
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
            self.reset()
    def Back(self):
        self.reset()
        sm.current = "main"
    def reset(self):
        self.username.text = ""
        self.namee.text = ""
        
class DeleteAccount:
    def deleteaccount(self):
        db.uspaac(e)

class P(FloatLayout):
    def deleteaccount(self):
        db.uspaac(e)
        show_popup.unshow(self)
        
class WindowManager(ScreenManager):
    pass

class show_popup(P):
    def __init__(self):
        self.show=P()
    def show(self):
        global pop
        self.show=P()
        pop = Popup(title='Account Delete',
                      content=self.show,
                      size_hint=(None, None), size=(400, 400))
        pop.open()
    
    def unshow(self):
        pop.dismiss()
    
def addsucess():
    pop = Popup(title='Sucessfull Added',
                  content=Label(text='Password added sucessfully..'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def deletesucess():
    pop = Popup(title='Sucessfull Deleted',
                  content=Label(text='Password delete sucessfully..'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()
    
def invalidDetails():
    pop = Popup(title='Invalid Details',
                  content=Label(text='Invalid Name of Application or Username in Application.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("bgkvnagtcfqxlblygymx-mysql.services.clever-cloud.com","uurvikppbsf3wlm4","frqPn7GgoOlMQ9lA9ik4","bgkvnagtcfqxlblygymx")

screens = [Introduction(name="Introduction"),LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"), AddPassword(name="Add"),LookPassword(name="look"),DeletePassword(name="delete")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "Introduction"

class MyMainApp(App):
    def build(self):
        self.title="LOCKWORD"
        return sm

if __name__ == "__main__":
    MyMainApp().run()
