# timetable-reminder-chatbot
import json
k=int(input("Hi friend how can i help you in following ways \n 1) making  time table \n 2)to know details of today timetable\n please enter 1 or 2" ))
if (k<0) or (k>2) :                           #if input is other than 1 or 2 it will rise exception
    raise Exception("Sorry you have given unknown input")
if k==1 :                               
 f=open('s2','w')        #it will create file and store in a computer 
 c={}
 m=int(input("Hi! friend i will help in you timetable making ,please enter how many subjects you need to study  "))
 for i in range(1,m+1) :
    a=input("please enter the subject name")
    b= input("please set  the time  you neeed to study, in the enterd way - hours : minutes AM/PM for ex:-2:23 PM")
    c[a]=b
 f.write(str(c))
else :
   m=open('s2','r')      #it will open the stored file
   g=m.read()
   c = json.loads(g)     #it will change string to dictonary
   if c.items() :
     print("Today you timetable is :-\nsubjects  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttime")
     print(c.keys(),"\t\t\t\t\t\t\t\t\t\t\t  ",c.values())       #it will print the subjects and time
   else :
      print("there is no present timetable")
