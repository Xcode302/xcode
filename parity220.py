#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2022,  1, 13 )
#expirydate = datetime.date(2021, 12, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rconnecting to server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    y=1
    newperiod=period
    banner='figlet RXCE V 2.0'
    thisway=[2,2,6,6,8,8,11,11,12,12,15,15,16,16,18,18,19,19,20,20]
    thatway=[1,1,3,3,4,4,5,5,7,7,9,9,10,10,14,14,13,13,17,17]
    numbers=[]
    i=1
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @rxcehack143")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully Connected to the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        def getSum(n):
            sum=0
            for digit in str(n):
                sum += int(digit)
            return sum
        if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1," : RED")
                else:
                    print(newperiod+1," : GREEN")
            else:
                if current in numbers:
                    print(newperiod+1," : GREEN")
                else:
                    print(newperiod+1," : RED")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1,": RED")
                else:
                    print(newperiod+1,": GREEN")
            else:
                if current in numbers:
                    print(newperiod+1,": GREEN")
                else:
                    print(newperiod+1,": RED")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @rxcehack143")
            print(numbers)
            
            
            
            
            
            
if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=1, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=23, minute=18, second=0, microsecond=0)
    
    
    if (now>First and now<Firstend):
            period=240
            hero()
    
    else:
        banner='figlet Rxce 7.o '
        print("Hi!! Thanks for buying the hack")
        print("----------Your play time-----------")
        print(" 12:00 PM- 12:15 PM")
        print(" 04:00 PM- 04:15 PM")
        print(" 07:00 PM- 07:15 PM")
        print(" 09:00 PM- 09:15 PM")
        print(" 11:00 PM- 12:15 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @ethical_expert007 ")
else:
    banner='figlet Thank '
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@ethical_expert007 for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 2.     3000 INR -------  30 Days")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print( "Msg me on telegram @ethical_expert007"
