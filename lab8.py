import pandas as pd
import numpy as np
data={"name":["asha","ravi","imran","sneha","meena"],
      "marks":[78,np.nan,62,np.nan,85],
      "age":[18,19,np.nan,20,np.nan],
      }
df=pd.DataFrame(data)
print("original dataframe:\n",df)
mean_marks=df["marks"].mean()
df["marks"]=df["marks"].fillna(mean_marks)
median_age=df["age"].median()
df["age"]=df["age"].fillna(median_age)
print("\ndataframe after filling missing values:\n",df)
