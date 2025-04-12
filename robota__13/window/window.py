from customtkinter import*
window = CTk()

window.geometry("400x400")
window.title("Clicer")
window.configure
label = (CTkButton(window))
label_2 = (CTkSlider(window))
label_3 = (CTkCheckBox(window, text= "Ви не робот?"))
label_4 = (CTkCheckBox(window, text= "Ви бобр?"))
text = CTkLabel(window, text="ДРАСТЕ")
text.pack()

label_2.place(x=0,y=0)



label.place(x=90,y=90)

label_3.place(x=300,y=300)
label_4.pack()

window.mainloop()