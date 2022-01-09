import json
import requests 



class Student:
    
    def __init__(self,url='',name='',roll='',city=''):
        self.url=url
        self.name=name
        self.roll=roll
        self.city=city

    def list_stu(self):
        res=requests.get(url=self.url)
        return res.json()

    def  create_stu(self,dic):
        header={'content-type':'application/json'}
        res=requests.post(url=self.url,headers=header,data=dic)        
        return res.json()

    def update_stu(self,id,dic):
        header={'content-type':'application/json'}
        res=requests.put(url=self.url.join(id),headers=header,data=json.dumps(dic))
        return res.json()

    def partially_update(self,id,dic):
        header={'content-type':'application/json'}
        res=requests.patch(url=self.url+f'{id}',headers=header,data=dic)
        return res.json()


    def delete_stu(self,id):
        res=requests.delete(url=self.url+f'{id}')
        return res.json()
    
    def json_stu_info(self):
        stu={'name':self.name,'roll':self.roll,'city':self.city}
        return json.dumps(stu)

    def update_name(self):
        stu={"name":self.name}
        return json.dumps(stu)

    def update_roll(self):
        stu={"roll":self.roll}
        return json.dumps(stu)

    def update_city(self):
        stu={"city":self.city}
        return json.dumps(stu)
    


menu=['1. Student Information','2. Create Student','3. Update Student','4. Delete Student']
while True:
    for id in menu:
        print(id)

    choice=int(input('Enter Your Choice :'))



    if choice==1:
        student=Student(url='http://127.0.0.1:8000/student/')
        print(student.list_stu())


    if choice==2:
        name=input('Enter Your Name :')
        roll=int(input('Enter Your Roll :'))
        city=input('Enter Your City :')
        student=Student(url='http://127.0.0.1:8000/student/',name=name,roll=roll,city=city)
        
        res=student.create_stu(student.json_stu_info())
        print(res)

    if choice==3:
        while True:
            new_menu=['1. Complete Update :','2. Update Name :','3. Update Roll :','4. Update City']
            for item in new_menu:
                print(item)
            update_choice=input('Enter Your Choice :')

            if update_choice=='1':
                id=input('Enter your id you want to update :')
                name=input('Enter Your Name :')
                roll=int(input('Enter Your Roll :'))
                city=input('Enter Your City :')
                student=Student(url='http://127.0.0.1:8000/student/',name=name,roll=roll,city=city)
                res=student.update_stu(id=id,dic=student.json_stu_info())
                update_choice=input('Enter c for continue and e for exit :')
                

            if update_choice=='2':
                id=input('Enter your id you want to update :')
                name=input('Enter Your Name :')
                student=Student(url='http://127.0.0.1:8000/student/',name=name)
                res=student.partially_update(id=id,dic=student.update_name())
                print(res)
                update_choice=input('Enter c for continue and e for exit :')
                

            if update_choice=='3':
                id=input('Enter your id you want to update :')
                roll=int(input('Enter Your Roll :'))
                student=Student(url='http://127.0.0.1:8000/student/',roll=roll)
                res=student.partially_update(id=id,dic=student.update_roll())
                print(res)
                update_choice=input('Enter c for continue and e for exit :')

            if update_choice=='4':
                id=input('Enter your id you want to update :')
                city=input('Enter Your city :')
                student=Student(url='http://127.0.0.1:8000/student/',city=city)
                res=student.partially_update(id=id,dic=student.update_city())
                print(res)
                update_choice=input('Enter c for continue and e for exit :')
            if update_choice=='c':
                continue
            if update_choice=='e':
                break
            else:
                exit(0)

    if choice==4:
        id=int(input('Enter Id which you want to delete :'))
        student=Student(url='http://127.0.0.1:8000/student/')
        res=student.delete_stu(id=id)
        print(res)


    if choice==0:
        exit(0)
