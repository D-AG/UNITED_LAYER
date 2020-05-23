# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:03:00 2020

@author: Daksh
"""


rooms1=[["The Inn",1,"No Air Conditioning","No Free Breakfast","TV Available","No Wifi",3],["Royal Palace",101,"Air Conditioning","Free Breakfast","TV Available","Wifi Available",8]]
rooms = []
coh=1
n=0
while(coh!=0):
    print( """
    
    * WELCOME TO HOTEL APPLICATION *  
   _________________________________    
    1.Press 1 to Add Hotel
    2.Press 2 to View All hotel
    3.Press 3 to search rooms
    4.Press 4 to exit program
   _________________________________
     """ )
    ch=int(input())
    number=0

    if (ch==1):
        
        name = str(input("name of your hotel?\n"))
        n = int(input("Number of rooms?\n" ))
        
        if not (n > 0):
            # sys.exit("Number of rooms must be positive integer")
            n = int(input("Number of rooms must be positive integer, try again:" ))
        
       
        
        for i in range(n):
            room_tmp = [name, i]
        
            ac = str(input(f"Air conditioning available in room?(Y/N) In room number:{i}\n"))
            room_tmp.append("Air Conditioning") if (ac.upper() == "Y") else room_tmp.append("No Air Conditioning")
        
            fb = str(input(f"Free Breakfast Available in room number:{i}?(Y/N) \n"))
            room_tmp.append("Free Breakfast") if (fb.upper() == "Y") else room_tmp.append("No Free Breakfast")
        
            tv = str(input(f"Televison Availabe in room number:{i}? (Y/N)\n"))
            room_tmp.append("TV Available") if (tv.upper() == "Y") else room_tmp.append("No TV")
        
            wifi = str(input(f"Free WiFi Available in room number:{i} (Y/N)\n"))
            room_tmp.append("Wifi") if (wifi.upper() == "Y") else room_tmp.append("No Wifi")
        
            room_tmp.append(int(input(f"Enter the cost/night($) for room number: {i}?(0-10)\n")))
        
            rooms1.append(room_tmp)
            del room_tmp
        
        con=input("DATA SAVED....press any key to continue")
    if(ch==2):
            
        

        
        
        
        print(": HOTEL NAME : ROOM NUMBER :  AIR CONDITIONING  : BREAKFAST  :  TELEVISION   : WIFI  : Cost/night($):")
        for item in rooms1:
            print(":",item[0],""*(13-len(item[0])),":",item[1],""*(13-len(str(item[1]))),":",item[2],""*(20-len(item[2])),":",item[3],""*(12-len(item[3])),":",item[4],""*(15-len(item[4])),":",item[5],""*(7-len(item[5])),":",item[6],""*(12-len(str(item[6]))),":")
        conto=input("Press any key to continue")
    if(ch==3):
           print("Searching hotels near your area...")
           cost=int(input("Please enter your budget/night in $?(0-10)\n"))
           if not (cost > 0):
            # sys.exit("Number of rooms must be positive integer")
                cost = int(input("Budget/night must be positive integer, try again:" ))
           counter=0
           print(": HOTEL NAME : ROOM NUMBER :  AIR CONDITIONING  : BREAKFAST  :  TELEVISION   : WIFI  : Cost/night($):")
           for b in range(0,(n+2)):
               if(cost >= rooms1[b][6]):
                   
                   print(":",rooms1[b][0],""*(13-len(str(rooms1[b][0]))),":",rooms1[b][1],""*(13-len(str(rooms1[b][1]))),":",rooms1[b][2],""*(20-len(str(rooms1[b][2]))),":",rooms1[b][3],""*(12-len(str(rooms1[b][3]))),":",rooms1[b][4],""*(15-len(str(rooms1[b][4]))),":",rooms1[b][5],""*(7-len(str(rooms1[b][5]))),":",rooms1[b][6],""*(12-len(str(rooms1[b][6]))),":")
                   # print(rooms1[b])
                   counter=1
           ex=input("Press any key to continue..")
           if(counter==0):
                   print("No Hotels found accoeding to your budget")
                   ex=input("Press any key to continue\n")
                    
    if(ch==4):
        coh=0
          
else:
      print("Terminating Hotel Application...")
          
          

    
            
        
