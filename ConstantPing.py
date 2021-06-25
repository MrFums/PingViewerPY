from tcp_latency import measure_latency
import os
from colorama import Fore, Style
from time import sleep
hostsite = 'google.com'
def assigncolour(pingnum,category):
    os.system('mode con: cols=20 lines=2')

        
    if pingnum <= 45: #green
        print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.GREEN + str(pingnum), "ms")
    elif pingnum > 45 and pingnum <= 80: #bright green
        print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + str(pingnum), "ms")

    elif pingnum > 80 and pingnum <= 170: #yellow
        print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.YELLOW + str(pingnum), "ms")

    else: #red
        print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.RED + str(pingnum), "ms")
    
    return

while True:
    try:
        currentping = measure_latency(host=hostsite, runs=1, timeout=1.5)
        print (int(currentping[0]))
        
        pingnum = (int(currentping[0]))
        category = "Ping:  "
        assigncolour(pingnum,category)
        sleep(.1)
    except:
        pass
