import customtkinter
from tkinter import *
from tkinter import messagebox

#window
app=customtkinter.CTk()
app.title('BMI CALCULATOR')
app.geometry('400x450')
app.config(bg='#000')

font1=('Arial',20,'bold')
font2=('Arial',20,'bold')
font3=('Arial',20,'bold')

#function
def calc():
    try:
        height=float(height_entry.get())
        weight=float(weight_entry.get())
        if variable2.get()=="ft":
            height*=30.48
        if variable1.get()=="lb":
            weight*=0.453592
        bmi=weight/((height/100)**2)
        result_label.configure(text="Your BMI is:{:.1f}".format(bmi))
    except ValueError:
        messagebox.showerror('Error','Enter a valid number!')
    except ZeroDivisionError:
        messagebox.showerror('Error','Height cannot be 0!')


#label_entrybox
title_label=customtkinter.CTkLabel(app,font=font1,text='BMI Calculator',text_color='#fff',bg_color='#000')
title_label.place(x=30,y=30)

height_label=customtkinter.CTkLabel(app,font=font1,text='Height',text_color='#fff',bg_color='#000')
height_label.place(x=30,y=100)

height_entry=customtkinter.CTkEntry(app,font=font1,text_color='#fff',bg_color='#000')
height_entry.place(x=30,y=130)

weight_label=customtkinter.CTkLabel(app,font=font1,text='Weight',text_color='#fff',bg_color='#000')
weight_label.place(x=30,y=160)

weight_entry=customtkinter.CTkEntry(app,font=font1,text_color='#fff',bg_color='#000')
weight_entry.place(x=30,y=190)

#dropdown
weight_options=['kg','lb']
height_options=['cm','ft']
variable1=StringVar()
variable2=StringVar()

weight_option=customtkinter.CTkComboBox(app,font=font2,text_color='#000',fg_color='#fff',dropdown_hover_color='#000',values=weight_options,variable=variable1,width=80)
weight_option.place(x=180,y=190)
weight_option.set=('kg')

height_option=customtkinter.CTkComboBox(app,font=font2,text_color='#000',fg_color='#fff',dropdown_hover_color='#000',values=height_options,variable=variable2,width=80)
height_option.place(x=180,y=130)
height_option.set=('cm')

#calculate
calculate_button=customtkinter.CTkButton(app,font=font2,command=calc,text_color='#fff',text='Calculate',fg_color='#06911f',hover_color='#06911f',bg_color='#000',cursor='hand2',corner_radius=5,width=200)
calculate_button.place(x=50,y=250)

#result
result_label=customtkinter.CTkLabel(app,text='',font=font3,text_color='#fff',bg_color='#000')
result_label.place(x=50,y=280)

app.mainloop()