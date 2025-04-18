from customtkinter import*
from PIL import Image
from socket import*
import threading
clients = socket(AF_INET , SOCK_STREAM)
clients.connect(("localhost", 2011))



window = CTk()
window.geometry("400x550")
window.configure(fg_color = "teal")


f1 = CTkFrame(window, width=350, height=400, )
f1.pack_propagate(False)
f1.pack(pady = 10)



text_pole = CTkTextbox(f1, width=300, height=380)
text_pole.configure(state = "disabled")
text_pole.pack()



f2 = CTkFrame(window,width=370, height=70)
f2.pack_propagate(False)
f2.pack(pady = 20)


entr = CTkEntry(f2, width=230, height=60 , placeholder_text="Введіть повідомлення....", 
                font = ("Arial", 13, "italic"))
entr.pack(pady=20, side = "left" , padx=10)


load_image = Image.open("zobrawena2/pixil-frame-0(2).png")
ready_image = CTkImage(light_image= load_image , size=(20,25))





def otoslat():
    msg = entr.get()
    print(f"DENIS "+ str({msg}))
    entr.delete(0, END)
    

    text_pole.configure(state = "normal")
    text_pole.insert(END, msg + "\n")
    text_pole.configure(state = "disable")
    clients.send(f"ДЕНИС {msg.encode()}")



def efg():
    while True:
        try:
            text = clients.recv(1024).decode()
            
            text_pole.configure(state = "normal")
            text_pole.insert(END, text + "\n")
            text_pole.configure(state = "disable")
            
        except:
            pass


threading.Thread(target=efg).start()


b1 = CTkButton(f2 , text="Отправить" , image=ready_image, command= otoslat,width=90, height=38, font = ("Arial", 12, "italic") )
b1.pack(pady = 20)


window.mainloop()
