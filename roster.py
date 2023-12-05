# https://goheels.com/sports/mens-basketball/roster
import pandas as pd 


roster = ["Cadeau", "Davis", "Bacot"]
player ={"Last Name": roster,
         "Fist Name":["Elliot", "RJ", "Armando"],
         "height":[73,72,83],
         "weight":[180,180,240]}
data=pd.DataFrame(player)
print(data)