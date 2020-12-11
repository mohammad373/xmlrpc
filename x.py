# xmlrpc

import os
import sys
import time
import requests
from colorama import Fore

def __xmlrpc__():
    os.system("clear")
    time.sleep(1)

        print(Fore.YELLOW + "[" + Fore.BLUE + "*" + Fore,YELLOW + "]" + Fore.BLUE + " ~ " + Fore.GREEN + "Hello . Welcome Back ;)")
        time.sleep(1)
        target = input(Fore.YELLOW + "\n[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED + " ~ " + Fore.BLUE + "Pleass Enter The Address Target " + Fore.GREEN + "==>  ")
        time.sleep(1)
        if target == "" or None:
            try:
                print(Fore.RED  + "Error : Your Target Is None ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        if "http" not in target or "https" not in target:
            target = "http://" + target
        else:
            pass
        my_list = ["xmlrpc.php" , "xmlrpc"]
        #ahoo1010.ir    |    http://ahoo1010.ir/xmlrpc

        for i in my_list:
            q = target + "/" + i
            r = requests.get(q)
            if r.status_code == 200:
                print(Fore.GREEN +"\n[+] " + Fore.GREEN + q)
            else:
                print(Fore.RED + "\n[-] " + Fore.RED + q)

__xmlrpc__()
