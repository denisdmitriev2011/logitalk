from socket import*
import threading
server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost", 2011))
server.setblocking(False)
server.listen(5)
clients = []
print("working ... ")
a = 1
def prinim_sms() :
    while 1 :
        for c in clients:
            try:
                print(c.recv(1024).decode())
            except:
                pass
threading.Thread(target=prinim_sms).start()
sms = ""
def otpravlat():
    global sms
    try :
        sms=input("")
        for c in clients:
            c.send(sms.encode())
    except:
        pass

threading.Thread(target=otpravlat).start()
while 1:
    try:
        comun, ip =server.accept()
        comun.setblocking(False)
        print("приєднався клієнт" ,ip)
        clients.append(comun)
    except:
         pass