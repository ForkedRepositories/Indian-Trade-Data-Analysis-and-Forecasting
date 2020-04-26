import pandas as pd
# Creating the first Dataframe using dictionary 
df1 = pd.DataFrame() 
  
# Creating the Second Dataframe using dictionary 
df2 = pd.DataFrame({"a":[1, 2, 3], 
                    "b":[5, 6, 7],  
                    "c":[1, 5, 4]}) 
df3 = pd.DataFrame({"a":[1, 2, 3], 
                    "b":[5, 6, 7],  
                    "c":[1, 5, 4]}) 
  
# for appending df2 at the end of df1 
df1 = df1.append(df2, ignore_index = True) 
df1 = df1.append(df3, ignore_index = True) 
df1.to_csv('test.csv', header = True, index = False)