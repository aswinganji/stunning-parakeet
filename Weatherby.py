from tkinter import*
import requests
import json

root = Tk()
root.geometry("1000x1000")
root.title("Hey,This is Useless!")
root.configure(background = 'lightblue')

city_name = Label(root,text= "Country Wontry")
city_name.place(relx = 0.3,rely = 0.15,anchor = CENTER)

city_entry = Entry(root)
city_entry.place(relx = 0.3,rely = 0.20,anchor = CENTER)

country_label = Label(root)
country_label.place(relx = 0.3,rely = 0.30,anchor = CENTER)

country_language = Label(root)
country_language.place(relx = 0.3,rely = 0.35,anchor = CENTER)

country_region = Label(root)
country_region.place(relx = 0.3,rely = 0.40,anchor = CENTER)

country_population = Label(root)
country_population.place(relx = 0.3,rely = 0.45,anchor = CENTER)

country_area = Label(root)
country_area.place(relx = 0.3,rely = 0.50,anchor = CENTER)



def city_name_function():
    api_request = requests.get("https://restcountries.eu/rest/v2/capital/" + city_entry.get())                                                           
    api_output_json = json.loads(api_request.content)
    
    country_name_var = api_output_json[0]['name']
    region = api_output_json[0]['region']
    language = api_output_json[0]['languages'][0]['name']
    population = api_output_json[0]['population']
    area = api_output_json[0]['area']
    
    country_label['text'] = "Country name = " + country_name_var
    country_language['text'] ="Country Language = " + language
    country_region['text'] ="Country Region = " + region
    country_population['text'] = "Country Population = " + str(population)
    country_area['text'] = "Country Area = " + str(area)
    
    
    

btn = Button(root,text = "Hihi",command = city_name_function)
btn.place(relx = 0.3,rely = 0.25,anchor = CENTER)

root.mainloop()






