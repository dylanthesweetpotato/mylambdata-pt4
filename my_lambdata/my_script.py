import pandas as pd

from my_lambdata.my_mod import enlarge


print("Happy Wednesday")

df = pd.DataFrame ({"x": [1,2,3], "y":[4,5,6]})
print (df)

x = 5
print(x, "Enlarge", enlarge(x))