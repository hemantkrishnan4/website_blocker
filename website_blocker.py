from time import *  
from datetime import *  
  
host_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com"]  

def intro():
    print('------------------------------- ')
    print("Welcome to the Website blocker")
    print('------------------------------- ')
    print('''Press 1.Add websites
      2.Remove websites
      3.Show list
      4.Reset
      5.To start blocker''')

def blocker():
    while True:      
            if datetime(datetime.now().year,datetime.now().month,datetime.now().day,8)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,20):  
                with open(host_path,"r+") as fileptr:  
                    content = fileptr.read()  
                    for website in websites:  
                        if website in content:  
                            pass  
                        else:  
                            fileptr.write(redirect+"    "+website+"\n")  
            else:  
                with open(host_path,'r+') as file:  
                    content = file.readlines();  
                    file.seek(0)  
                    for line in content:  
                        if not any(website in line for website in websites):  
                            file.write(line)  
                    file.truncate()  
            sleep(5)
    
def safety():
    _sfcy_='''# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost'''
    with open(host_path,'r+') as file:
        file.write(_sfcy_)
while True:
    intro()
    x=int(input("Enter the number: "))
    
    if x==1:
        web=input("Enter the website: ")
        websites.append(web)
        print("Added Successfully")
        
    if x==2:
        web=("Enter the name of the website to be removed")
        websites.remove(web)
        with open(host_path,'r+') as file:
            content = file.readlines();  
            file.seek(0)  
            for line in content: 
                if not any(website in line for website in websites):  
                    file.write(line)  
                    file.truncate()
        print("Removed Successfully")

    if x==3:
        print("Blocked websites are: ")
        for name in websites:
            print(name)

    if x==4:
        safety()
        print("Default settings Restored")
        
    if x==5:
        print("Started Blocking Websites :)")
        print("The websites will be blocked during working hrs")
        blocker()
        
        
