#!/usr/bin/env python
# coding: utf-8

# In[86]:


#!pip3 install pymysql


# In[72]:


get_ipython().system('pip3 install mysql-connector')


# In[73]:


# Import libraries

import pandas as pd
import pymysql
from sqlalchemy import create_engine
import mysql.connector as mysql


# create dataframe from excel file

df = pd.read_excel (r'C:\Users\User\Downloads\data_records.xlsx')

print (df)


# In[74]:


# Listing Column names

list(df.columns)


# In[75]:


# Output  of the rows

print("Total rows: {0}".format(len(df)))


# In[76]:


# Returning a tuple representing the dimensionality of the DataFrame

df.shape


# In[81]:


# printing info in DataFrame

df.info()


# In[89]:


# Creating an MySQL database using Python

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="nancywachira"
    
)

print(mydb)
#   connecting to the object

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS data_records2")

print("\n data_records-2 Database successfully created")


# In[90]:


mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = "nancywachira",
    database = "data_records2"

)

#connecting to the database by creating an engine that connects to the MySQL database.

engine = create_engine("mysql+pymysql://root:nancywachira@localhost/data_records2")
        



df.to_sql('data_records2', engine, index=False)


# In[92]:


df = pd.read_sql_query("SELECT * FROM data_records", engine)
#df.head()


# In[93]:


authentication = pd.DataFrame(df, columns= ['User Name', 'Password'])

authentication.head()


# In[57]:


employee_records = pd.DataFrame(df, columns= ['Emp ID', 'Name Prefix', 'First Name', 'Middle Initial', 'Last Name', 'Gender', 'E Mail', "Father's Name", "Mother's Name", "Mother's Maiden Name", 'Date of Birth', 'Time of Birth', 'Age in Yrs.', 'Weight in Kgs.', 'Date of Joining', 'Quarter of Joining', 'Half of Joining', 'Year of Joining', 'Month of Joining', 'Month Name of Joining', 'Short Month', 'Day of Joining', 'DOW of Joining', 'Short DOW', 'Age in Company (Years)', 'Salary', 'SSN', 'Phone No.', 'Place Name', 'County', 'City', 'State', 'Zip', 'Region'])

employee_records.head()


# In[58]:


list(employee_records.columns)


# In[85]:


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(r'C:\Users\User\Downloads\data_records2.xlsx', engine='xlsxwriter')



df.to_excel(writer, sheet_name='data_records')
authentication.to_excel(writer, sheet_name='authentication')
employee_records.to_excel(writer, sheet_name='employee_records')


writer.save()

print('data_records written successfully to Excel File.')


# In[ ]:




