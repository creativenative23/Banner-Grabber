import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    print("""\n

                 * * *
  _                                     
 | |__   __ _ _ __  _ __   ___ _ __     
 | '_ \ / _` | '_ \| '_ \ / _ \ '__|    
 | |_) | (_| | | | | | | |  __/ |       
 |_.__/ \__,_|_| |_|_| |_|\___|_|       
   __ _ _ __ __ _| |__ | |__   ___ _ __ 
  / _` | '__/ _` | '_ \| '_ \ / _ \ '__|
 | (_| | | | (_| | |_) | |_) |  __/ |   
  \__, |_|  \__,_|_.__/|_.__/ \___|_|   
  |___/                                 
   
                        by MG
                        
                 * * *

\n""")
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    print("\nGrabbing Banner for " + ip + ":" + port)
    banner(ip, port)


main()
