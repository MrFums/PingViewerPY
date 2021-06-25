


try:
    from tcp_latency import measure_latency
    from statistics import mode
    from colorama import Fore, Style
    import os

    os.system('mode con: cols=50 lines=10')

    
    hostsite = 'google.com'
    print (Fore.YELLOW + " Sending packets to", Style.BRIGHT + str(hostsite))
    print (Style.RESET_ALL + Fore.YELLOW + "\n Please wait...")
    
    pinglist = measure_latency(host=hostsite, runs=8, timeout=1.5)
    addition = 0
    for i in range (len(pinglist)-1):
        addition += pinglist[i]
    median = addition / (len(pinglist)-1)
    try:
        os.system('cls' if os.name=='nt' else 'clear')
    except Exception as e:
        print (e)


    def assigncolour(pingnum,category):
        if pingnum <= 45: #green
            print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.GREEN + str(pingnum), "ms")
        elif pingnum > 45 and pingnum <= 80: #bright yellow
            print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + str(pingnum), "ms")

        elif pingnum > 80 and pingnum <= 130: #yellow
            print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.YELLOW + str(pingnum), "ms")

        else: #red
            print (Style.RESET_ALL, category, Style.RESET_ALL + Fore.RED + str(pingnum), "ms")

        return

    print (Fore.RED + Style.BRIGHT + " Ping Report from", Style.RESET_ALL + Fore.RED + hostsite,"\n")
    pingnum = int(median)
    category = "Median:     "
    assigncolour(pingnum,category)
    
    pingnum = int(mode(pinglist))
    category = "Average:    "
    assigncolour(pingnum,category)

    pingnum = int(max(pinglist))
    category = "Max:        "
    assigncolour(pingnum,category)
    
    pingnum = int(min(pinglist))
    category = "Min:        "
    assigncolour(pingnum,category)
    
    pingnum = int(max(pinglist)-min(pinglist))
    category = "Range:      "
    assigncolour(pingnum,category)

    allformat = []
    for i in range (len(pinglist)-1):
        ping = str(int(pinglist[i])) + "ms"
        allformat.append(ping)

    allformat = (', '.join(allformat))
    
    print (Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT, allformat)

    


    
except Exception as e:
    print (" ERROR:",e)

input()
