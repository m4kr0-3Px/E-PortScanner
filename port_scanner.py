import socket
import colorama


print(colorama.Fore.YELLOW)
print("1-Scan all ports\n2-Scan a spesific port")
print(colorama.Fore.MAGENTA)
try:
    choose_no=int(input("What is your choice---------->"))

    if choose_no==1:

        print(colorama.Fore.LIGHTRED_EX)
        ip_adress=input("Enter the ip adress:")
        print(colorama.Fore.BLUE)
        print("Open ports are waiting...")
        print(colorama.Fore.RED)
        print("If you want to quit,please press 'q' !!!")
        print(colorama.Fore.RESET)
        while not input("")=="q":


            for i in range(1,65536):
                try:
                    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    res=s.connect_ex((ip_adress,i))

                    if res==0:

                        print(colorama.Fore.YELLOW)
                        print("[+] Port is open:"+str(i))
                    else:
                        continue
                    s.close()


                except:
                    continue
            s.close()


    elif choose_no==2:
        ip_adress=input("Enter the ip_adress----------> ")
        for_port=int(input("Enter a specific port----------> "))
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result=s.connect_ex((ip_adress,for_port))
            if result==0:
                print(colorama.Fore.GREEN)
                print("[+] Port is open---------->"+str(for_port))
            else:
                print(" ")
                print("Waiting result...")
                print(colorama.Fore.RED)
                socket.setdefaulttimeout(1)
                print("[-] Port is closed or firewall is blocking----------->" + str(for_port))

        except:
            print(colorama.Fore.RED)
            print("[-] We can not connect to port----------->" + str(for_port))
except:
    print(colorama.Fore.YELLOW)
    print("Please try to run the program correctly :)")