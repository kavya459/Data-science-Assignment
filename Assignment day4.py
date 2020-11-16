Question 1: 
import pandas as pd
print(pd__version__)

Question 2::
import pandas as pd
import numpy as np
Arr=np.array([1,2,3,4,5,6,7])
Ser=pd.Series(Arr)
print(Ser)
Question 3::
import pandas as pd
Data=pd.DataFrame({'Eid':['2b1','3c1','4g1','6h1'],
                                         'Name':["kushal","koushika","Aruna","ranju"],
                                         "dept":["finance","sales","production",'HR'],
                                          "Salary":[10000,15000,9000,50000]})
Data.columns=[Data.index]
print(Data)                
Question 4::
import pandas as pd
data=pd.read_csv("/storage/emulated/0/pubg - Dr. Darshan Ingle.csv")
print(data.columns)
Question 5::




Question 6::
import pandas as pd 
data=pd.read_csv("/storage/emulated/0/pubg Dr. Darshan Ingle.csv")
Data=get_value(car="usa")

