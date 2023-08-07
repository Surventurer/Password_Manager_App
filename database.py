import datetime
import mysql.connector
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class DataBase:
    def __init__(self,host,user,passwd,database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database=database

    def add_password(self,em,namee,username, password):
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        s=DataBase.secure()
        q1='''insert into `%s`(Name_of_Application,Username_in_Application,Password_in_Application) values(%s,%s,%s)'''
        for u,v in s:
            namee=namee.replace(u,v)
            username=username.replace(u,v)
            password=password.replace(u,v)
        q2=(em,namee,username, password)
        cur.execute(q1,q2)
        connect.commit()
        connect.close()
    def secure():
        s=(('a','一种16'),("b","乙100"),("c","सी17"),("d","डी211"),("e","电子19"),("f","एफ333"),("g","जी366"),("h","एच636"),('i',"一世367"),("j","जे789"),("k","克123"),("l","升719"),
("m","米911"),("n","एन46"),("o","Ø55"),("p","磷51"),("q","क्यू101"),("r","आर742"),('s',"秒943"),("t","吨102"),("u","你317"),("v","वी109"),("w","瓦444"),("x","एक्स577"),
("y","是210"),("z","जेड420"),('A','一种6'),("B","乙8"),("C","सी2"),("D","डी1"),("E","电子7"),("F","एफ0"),("G","जी21"),("H","एच63"),
('I',"一世33"),("J","जे122"),("K","克41"),("L","升32"),("M","米69"),("N","एन82"),("O","Ø99"),("P","磷00"),("Q","क्यू11"),("R","आर3"),('S',"秒77"),("T","吨20"),
("U","你352"),("V","वी87"),("W","瓦38"),("X","एक्स29"),("Y","是90"),("Z","जेड60"),(" ","!00!"))
        return s
    def delete_password(self,em,namee,username):
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        q3="""DELETE FROM `%s` WHERE Name_of_Application=%s and Username_in_Application=%s"""
        s=DataBase.secure()
        for s,t in s:
            namee=namee.replace(s,t)
            username=username.replace(s,t)
        q2=(em,namee,username)
        cur.execute(q3,q2)
        connect.commit()
        connect.close()
    def show_records(self,em):
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        q1="select * from `%s`"
        q2=(em,)
        cur.execute(q1,q2)
        sr=cur.fetchall()
        s=DataBase.secure()
        t=[]
        for so in sr:
            b1,b2,b3=so
            while True:
                o=[]
                l=(b1,b2,b3)
                if l==None:
                    break
                for p in l:
                    k=str(p)
                    for a,b in s:
                        k=k.replace(b,a)
                    o.append(k)
                break
            t.append(tuple(o))
        connect.close()
        return t

    def get_user(self, email):
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        cur.execute("select * from user")
        s=DataBase.secure()
        r=cur.fetchall()
        for a in range(len(r)):
            a1,a2,a3=r[a][0],r[a][1],r[a][3]
            while True:
                o=[]
                l=(a1,a2,a3)
        
                if l==None:
                    break
                for p in l:
                    k=str(p)
                    for a,b in s:
                        k=k.replace(b,a)
                    o.append(k)
                break
            for j in range(len(o)):
                if o[1]==email:
                    return (o[0],o[2])
        connect.close()

    def add_user(self, name, email, password):
        try:
            connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
            cur=connect.cursor()
            cur.execute("select * from user")
            r=cur.fetchall()
            if r == []:
                query1 ="""create table `%s`(Name_of_Application varchar(1000),Username_in_Application varchar(1000),Password_in_Application varchar(5000))"""
                qu1=(email,)
                cur.execute(query1,qu1)
                accountcreation=DataBase.get_date()
                l=DataBase.secure()
                for m,n in l:
                    name=name.replace(m,n)
                    email=email.replace(m,n)
                    password=password.replace(m,n)
                q1='''insert into user(name,email,password,accountcreation) values(%s,%s,%s,%s)'''
                q2=(name, email, password,accountcreation)
                cur.execute(q1,q2)
                connect.commit()
                connect.close()
            else:
                l=DataBase.secure()
                for j,k in l:
                    email=email.replace(j,k)
                for a in r:
                    if a[1]==email:
                        pop = Popup(title='Account exist',content=Label(text='Account already exist. !!'),size_hint=(None, None), size=(400, 400))
                        pop.open()
                    else:
                        ll=DataBase.secure()
                        for s,t in ll:
                            email=email.replace(t,s)
                        query2 ="""create table `%s`(Name_of_Application varchar(1000),Username_in_Application varchar(1000),Password_in_Application varchar(5000))"""
                        qu2=(email,)
                        cur.execute(query2,qu2)
                        connect.commit()
                        accountcreation=DataBase.get_date()
                        l=DataBase.secure()
                        for m,n in l:
                            name=name.replace(m,n)
                            email=email.replace(m,n)
                            password=password.replace(m,n)
                        q1='''insert into user(name,email,password,accountcreation) values(%s,%s,%s,%s)'''
                        q2=(name, email, password,accountcreation)
                        cur.execute(q1,q2)
                        connect.commit()
        except Exception as error:
            print(error)
        connect.close()
    def delpassval(self,em,name,usernameapp):
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        q1="select * from `%s`"
        q2=(em,)
        cur.execute(q1,q2)
        r=cur.fetchall()
        ss=DataBase.secure()
        for s,t in ss:
            name=name.replace(s,t)
            usernameapp=usernameapp.replace(s,t)
        for i in r:
            if i[0]== name and i[1]==usernameapp:
                return True
        else:
            return False
        connect.close()

    def validate(self, email, password):
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        cur.execute("select * from user")
        s=DataBase.secure()
        r=cur.fetchall()
        if r != []:
            for u in range(len(r)):
                a1,a2=r[u][1],r[u][2]
                while True:
                    o=[]
                    l=(a1,a2)
                    if l==None:
                        break
                    for p in l:
                        k=str(p)
                        for a,b in s:
                            k=k.replace(b,a)
                        o.append(k)
                    break
                if o[0]==email and o[1]==password:
                    return True
        else:
            return False
        connect.close()
    def userspersonal(self,email):
        pass
    def uspaac(self,email):
        emaill=email
        connect=mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        cur=connect.cursor()
        ll=DataBase.secure()
        for s,t in ll:
            email=email.replace(s,t)
        q3="""DELETE FROM user WHERE email=%s"""
        q4=(email,)
        cur.execute(q3,q4)
        connect.commit()
        q1="""Drop table if exists `%s`"""
        q2=(emaill,)
        cur.execute(q1,q2)
        connect.commit()
        connect.close()
        
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


