# https://goheels.com/sports/mens-basketball/roster
import pandas as pd 

player ={"Last Name": ["Cadeau", "Davis", "Bacot","High","Ryan","Trimble","Wojcik", "Washington","Lebo","Landry","Okonkwo"],
         "Fist Name":["Elliot", "RJ", "Armando","Zayden","Cormac","Seth","Paxson","Jalen","Creighton","Rob","James"],
         "height":[73,72,83,83,78, 76, 76, 73, 73, 77, 82],
         "weight":[180,180,240,225,195, 195, 195, 230, 180, 190,240]}
data=pd.DataFrame(player)

#bmi = weight in kg / height in meters squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")