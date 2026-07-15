#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to Data Analytics Lab")


# In[2]:


a = 20
b = 10

print("Addition =",a+b) 
print("Subtraction =",a-b) 
print("Multiplication =",a*b) 
print("Division =",a/b)


# In[4]:


name = "John" 
dept = "AI&DS" 
cgpa = 8.9
print("Name:",name) 
print("Department:",dept) 
print("CGPA:",cgpa)


# In[5]:


import numpy as np
a = np.array([10,20,30,40,50])
print(a)
print("Mean =",np.mean(a))
print("Sum =",np.sum(a))


# In[6]:


import pandas as pd
data = {'Name':['John','David','Alex'], 'Marks':[85,90,95]}
df = pd.DataFrame(data) 
print(df)


# In[8]:


import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[10,20,15,25,30]
plt.plot(x,y)
plt.title("Sample Line Graph")
plt.xlabel("X Axis") 
plt.ylabel("Y Axis") 
plt.show()


# In[13]:


import pandas as pd
df = pd.read_csv(r"C:\Users\HDC0422048\Downloads\archive (4)\malnutrition_data (1).csv")
print(df)


# In[15]:


df.drop_duplicates(inplace=True)
df.dropna(inplace=True)


# In[16]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv(r"C:\Users\HDC0422048\Downloads\archive (4)\malnutrition_data (1).csv")
le = LabelEncoder()
df["nutrition_status"] = le.fit_transform(df["nutrition_status"])
X = df.drop("nutrition_status", axis=1)
y = df["nutrition_status"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100)
print(classification_report(y_test, y_pred))


# In[ ]:




