import customtkinter
import random

#def
def gacha_pull():
    # List of items in the gacha pool
    gacha_pool = [
        "Sword",
        "Chicken",
        "Sho",
        "Phu",
        "OFF"
    ]

    # Assigning probabilities to each item in the gacha pool
    item_probabilities = {
        "Item 1": 0.4,
        "Item 2": 0.3,
        "Item 3": 0.2,
        "Item 4": 0.08,
        "Item 5": 0.02
    }

    # Randomly selecting an item based on the assigned probabilities
    item = random.choices(gacha_pool, weights=item_probabilities.values(), k=1)[0]
    Changevar.set(item)






#Variables / app information
app = customtkinter.CTk()
app.title('Gacha Noob')
app.geometry('1000x500')
Changevar = customtkinter.StringVar()
Changevar.set('None')

Name_item = customtkinter.CTkLabel(app,text = "Name : ", textvariable = Changevar, fg_color="transparent")
Name_item.pack()
#Rolls = customtkinter.CTkEntry(app, placeholder_text="Rolls")
#Rolls.pack(pady = (20,0))

#Buttons
button_Clicktorools = customtkinter.CTkButton(app,text = 'Click to roll',command = gacha_pull)
button_Clicktorools.pack(pady = (20,20))
#change var





app.mainloop()