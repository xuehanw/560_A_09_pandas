# https://goheels.com/sports/mens-basketball/roster
import pandas as pd 

player ={"Last Name": ["Cadeau", "Davis", "Bacot"],
         "Fist Name":["Elliot", "RJ", "Armando"],
         "height":[73,72,83],
         "weight":[180,180,240]}
data=pd.DataFrame(player)

data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")