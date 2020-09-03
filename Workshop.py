def Printmainmenu():
    print("Welcome to the Workshop system"+'\n'+"Choose Menu:"+'\n'+'1. Client'+'\n'+'2. Mechanic'+'\n'+"3. Exit")
    
def Printclientmenu():
    print("Welcome to the Client menu."+'\n'+"Choose Option:"+'\n'+"1. Enter Client data"+'\n'+"2. Services"+'\n'+"3. Print invoice"+'\n'+"4. Go back to previous menu")

def Printmechmenu():
    print("Welcome to the Mechanic menu."+'\n'+"Choose Option:"+'\n'+"1. Enter new mechanic"+'\n'+"2. List of mechanics"+'\n'+"3. Go back to previous menu")

def Printservices():
    print("")

def Printservicemenu():
    print("Welcome to the Services menu."+'\n'+"Choose Option:"+'\n'+"1. Car service"+'\n'+"2. Paint Job"+'\n'+"3. Air Pressure"+'\n'+"4. Oil change"+'\n'+"5. Tuning"+'\n'+"6. Return")






Mechanic_list= {"1" : "Ahmed", "2" : "Ali"}
Client_list= {}


def Workshop():
    Endrun = False
    while not Endrun:
        
        Printmainmenu()
    
        x=int(input())
        new=Payment()
        new2=Mechanic()
        JL= new.Jobs_avail
        
        
        if x==1:
            clientmenudone = False
            while not clientmenudone:
                    Printclientmenu()
                    y=int(input())
                    if y==1:
                        
                        candatadone = False
                        while not candatadone:
                            new.regc()
                            new.regcar()
                            candatadone = True

                    if y==2:
                        jobdone= False
                        while not jobdone:
                            Printservicemenu()
                            o= int(input())

                            if o==1:
                                new.jobs.append("Car service")
                                new.total+= JL["Service"]
                                
                            if o==2:
                                new.jobs.append("Paint Job")
                                new.total+= JL["Paint Job"]
                            if o==3:
                                new.jobs.append("Air Pressure")
                                new.total+= JL["Air Pressure"]
                            if o==4:
                                new.jobs.append("Oil Change")
                                new.total+= JL["Oil Change"]
                            if o==5:
                                new.jobs.append("Tuning")
                                new.total+= JL["Tuning"]
                            if o==6:
                                jobdone = True

                    if y==3:
                        invodone= False
                        while not invodone:
                            new.Invoice()
                            invodone = True

                            


                            
                    if y==4:
                        clientmenudone = True
                        
        if x==2:
            mechmenudone= False
            while not mechmenudone:
                Printmechmenu()
                v=int(input())
                if v==1:
                    mechdatadone = False
                    while not mechdatadone:
                        new.Regmech()
                        mechdatadone = True
                if v==2:
                    print(Mechanic_list)
                if v==3:
                    mechmenudone = True
            
        if x==3:
            Endrun = True
        

        
class Client:
    def __init__(self):
        self.Uid=0
        self.name=''
        self.total = 0
        self.jobs=[]
        
        
        
    def regc(self):
        self.Uid+=1
        print(self.Uid)
        print("Enter name :")
        self.name=input()
        


class Mechanic(Client):
    def __init__(self):
        Client.__init__(self)
        self.Name=''
        self.ID=2
        
        
    def Regmech(self):
        self.ID+=1
        print(self.ID)
        print("Enter name :")
        self.Name=input()
        Mechanic_list[self.ID]=self.Name
        print(Mechanic_list)


          
class Vehicle(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.car_company= ''
        self.car_model=''
        self.car_plate=''
        self.car_colour=''
        

    def regcar(self):
        print("Enter Car Company :")
        self.car_company=input()
        print("Enter Car model :")
        self.car_model=input()
        print("Enter Car No.plate :")
        self.car_plate=input()
        print("Enter Car colour :")
        self.car_colour= input()
        Client_list[self.Uid]=self.name,self.car_company,self.car_model,self.car_plate,self.car_colour,self.total
        print(Client_list)

class Repair(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.Jobs_avail= {"Service" : 1000, "Paint Job": 1500, "Air Pressure": 30, "Oil Change": 700, "Tuning": 500}
        self.Service= 1000
        self.Paint_job=1500
        self.Air_pressure= 30
        self.Oil_change= 700
        self.Tuning= 500

class Payment(Repair):
    def __init__(self):
        Repair.__init__(self)
        self.Payed= 0

    def Cash(self):
        change= 0
        Payed= 0
        total= self.total
        print("Amount Payed =")
        x=int(input())
        if x > total:
            change= x-total
            print("Your change = ",change,'\n',"Thank You.")
        if x== total:
            print("No change."+'\n'+"Thank You.")
        
        

    def Invoice(self):
        print("INVOICE",'\n',"Client name:",'',self.name,'\n',"Jobs Done:",'\n',self.jobs,'\n','\n',"Total = ", self.total)
        print("Please select mode of payment:"+'\n'+"Choose Option:"+'\n'+"1. Cash"+'\n'+"2. EasyPaisa"+'\n'+"3. Debit")
        y=int((input()))
        if y==1:
            self.Cash()
        elif y==2:
            print("Thank You.")

        elif y==3:
            print("Thank You.")
            

          





            

Workshop()
