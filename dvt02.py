#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv(r"C:\Users\HDC0422048\Downloads\archive (4)\malnutrition_data (1).csv")
print(df.head())


# In[5]:


print(df.info())


# In[6]:


print(df.describe())


# In[9]:


import pandas as pd
df = pd.read_excel(r"C:\Users\HDC0422048\Downloads\dvt.xlsx") 
print(df)


# In[10]:


import sqlite3
conn = sqlite3.connect("student.db")
print("Database created successfully!")
cursor = conn.cursor()


# In[11]:


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")
conn.commit()
print("Table created successfully!")


# In[12]:


cursor.execute("""
INSERT INTO students (id, name, age, department)
VALUES (1, 'Lekha', 21, 'CSBS')
""")
conn.commit()
print("One record inserted.")


# In[13]:


records = [
    (2, 'Arun', 20, 'CSE'),
    (3, 'Priya', 22, 'ECE'),
    (4, 'Rahul', 21, 'IT')
]
cursor.executemany("""
INSERT INTO students VALUES (?, ?, ?, ?)
""", records)
conn.commit()

print("Multiple records inserted.")


# In[14]:


cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)


# In[15]:


url = r"C:\Users\HDC0422048\Downloads\archive (4)\malnutrition_data (1).csv" 
df = pd.read_csv(url) 
print(df.head())


# In[16]:


df.to_csv( r"C:\Users\HDC0422048\Downloads\archive (4)\malnutrition_data (1).csv" , index=False) 
print("CSV File Exported")


# In[17]:


df.to_excel(r"C:\Users\HDC0422048\Downloads\dvt.xlsx", index=False) 
print("Excel File Exported")


# In[18]:


import pandas as pd
df = pd.read_excel(r"C:\Users\HDC0422048\Downloads\dvt.xlsx")
df.to_json("malnutrition.json", orient="records", indent=4)
print("JSON file created successfully!")


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\HDC0422048\Downloads\archive (4)\malnutrition_data (1).csv")
status_count = df["nutrition_status"].value_counts()
plt.figure(figsize=(6,5))
plt.bar(status_count.index, status_count.values)
plt.title("Distribution of Nutrition Status")
plt.xlabel("Nutrition Status")
plt.ylabel("Number of Children")
for i, value in enumerate(status_count.values):
    plt.text(i, value + 1, str(value), ha='center')
plt.show()


# In[ ]:




