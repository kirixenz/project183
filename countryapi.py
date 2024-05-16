from tkinter import *
import requests
import json

root = Tk()
root.geometry("600x600")
root.configure(background="#89CFF0")

city_name_label = Label(root, text="Capital City Name", font=("Arial", 20, "bold"), fg="white", bg="#89CFF0")
city_name_label.place(relx=0.3, rely=0.1, anchor=CENTER)

city_entry = Entry(root)
city_entry.place(relx=0.1, rely=0.18)

country_name = Label(root, text="Country:", font=("Arial", 18, "bold"), fg="white", bg="#89CFF0")
country_name.place(relx=0.1, rely=0.35)

region_name = Label(root, text="Region:", font=("Arial", 18, "bold"), fg="white", bg="#89CFF0")
region_name.place(relx=0.1, rely=0.45)

language_name = Label(root, text="Language:", font=("Arial", 18, "bold"), fg="white", bg="#89CFF0")
language_name.place(relx=0.1, rely=0.55)

population_name = Label(root, text="Populaion:", font=("Arial", 18, "bold"), fg="white", bg="#89CFF0")
population_name.place(relx=0.1, rely=0.65)

area_name = Label(root, text="Area:", font=("Arial", 18, "bold"), fg="white", bg="#89CFF0")
area_name.place(relx=0.1, rely=0.75)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)

    country = api_output_json[0]["name"]
    reg = api_output_json[0]["region"]
    lang = api_output_json[0]["languages"][0]["name"]
    popn = api_output_json[0]["population"]
    country_area = api_output_json[0]["area"]

    country_name.config(text="Country: " + country)
    region_name.config(text="Region: " + reg)
    language_name.config(text="Language: " + lang)
    population_name.config(text="Population: " + str(popn))
    area_name.config(text="Area: " + str(country_area))

city_details_button = Button(root, text="City Details", relief=FLAT, bg="#4682B4", command=city_details)
city_details_button.place(relx=0.1, rely=0.25)

root.mainloop()