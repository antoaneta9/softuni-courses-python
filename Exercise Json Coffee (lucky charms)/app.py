import json
import random
import tkinter as tk

json_path = 'data/kysmetcheta.json'

###################### USER INTERFACE ########################
###################### Window creation ######################
root = tk.Tk()
root.title("☕ Късметче с кафето")
root.geometry("500x300")
root.configure(bg="#f9f5eb")

###################### Label Name ######################
title_label = tk.Label(root, text="☕ Късметче с кафето", font=("Arial", 18, "bold"), bg="#f9f5eb", fg="#5c4033")
title_label.pack(pady=20)

def load_data():
    """Opens everything from json file"""
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data['kysmetcheta']

###################### Loading data ######################
lucky_charms = load_data()

def random_coffee_lucky():
    """Getting random coffee lucky charm"""
    charm = random.choice(lucky_charms)
    result_label.config(text=charm)


###################### Button ######################
button = tk.Button(root, text="Изтегли късметче ☀️", font=("Arial", 14), bg="#d7bfae", fg="#2b1d0e", relief="raised", command=random_coffee_lucky)
button.pack(pady=20)
button.pack(pady=10)

###################### Result input box ######################
result_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14), bg="#f9f5eb", fg="#3c2a1e", justify="center")
result_label.pack(pady=20)

###################### Starting app ######################
root.mainloop()
