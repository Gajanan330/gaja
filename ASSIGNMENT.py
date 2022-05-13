class DataSet:
    output=[]

class userinput:
    def get(self):
        i=1
        while i!=11:
            distance=float(input('enter distance:'))
            time=float(input('enter time:'))
            DataSet.output+=[[distance,time]]
            i+=1
class Measure:
    def measure(self):
        a=DataSet.output
        for i in a:
            res=i[0]/i[1]
            i.append(res)
class Display:
    def display(self):
        for i in DataSet.output:
            print(i)
object1=userinput()
object1.get()
object2=Measure()
object2.measure()
object3=Display()
object3.display()

import csv
a=['Distance','Time','Speed']
r=DataSet.output
f='data.csv'

fileOpen=open(f,'w')
f1=csv.writer(fileOpen)
f1.writerow(a)
f1.writerows(r)
fileOpen.close()
