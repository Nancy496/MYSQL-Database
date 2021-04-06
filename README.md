# MYSQL-Database
## pip3 install pymysql
## pip3 install mysql-connector
# Import libraries

   import pandas as pd
   import pymysql
   from sqlalchemy import create_engine
   import mysql.connector as mysql
## create dataframe from excel file
    df = pd.read_excel (r'C:\Users\User\Downloads\data_records.xlsx')
    print (df)
    ![Import libraries](https://user-images.githubusercontent.com/75600702/113766517-e51c7980-96f3-11eb-9539-80c8a1bca24e.PNG)
# printing info in DataFrame
   df.info()
    ![Info](https://user-images.githubusercontent.com/75600702/113766812-42182f80-96f4-11eb-96d4-ddb24d5efb70.PNG)
# Creating an MySQL database using Python
     mydb = mysql.connect(
     host="localhost",
     user="root",
     password="nancywachira"
    )
print(mydb)
##   indentifying  the object
    mycursor = mydb.cursor()
     mycursor.execute("CREATE DATABASE IF NOT EXISTS data_records2")
     print("\n data_records-2 Database successfully created")
     ![Database](https://user-images.githubusercontent.com/75600702/113767146-b0f58880-96f4-11eb-96fc-ec010cf2246d.PNG)
  ##  Creating an engine that connects to the MySQL database
       mydb = mysql.connect(
       host = "localhost",
       user = "root",
       password = "nancywachira",
       database = "data_records2")
       engine = create_engine("mysql+pymysql://root:nancywachira@localhost/data_records2")
       df.to_sql('data_records2', engine, index=False)
       authentication = pd.DataFrame(df, columns= ['User Name', 'Password'])
## Authentication Sheet with records for username $ password
      authentication = pd.DataFrame(df, columns= ['User Name', 'Password'])
      authentication.head()
      ![Authentication](https://user-images.githubusercontent.com/75600702/113767836-86f09600-96f5-11eb-9bd5-c3dd59028482.PNG)
## Employee Records
       employee_records = pd.DataFrame(df, columns= ['Emp ID', 'Name Prefix', 'First Name', 'Middle Initial', 'Last Name',   
'Gender', 'E Mail', "Father's Name", "Mother's Name", "Mother's Maiden Name", 'Date of Birth', 'Time of Birth', 'Age in Yrs.', 'Weight in Kgs.', 'Date of Joining', 'Quarter of Joining', 'Half of Joining', 'Year of Joining', 'Month of Joining', 'Month Name of Joining', 'Short Month', 'Day of Joining', 'DOW of Joining', 'Short DOW', 'Age in Company (Years)', 'Salary',  'SSN', 'Phone No.', 'Place Name', 'County', 'City', 'State', 'Zip', 'Region'])
       employee_records.head()
   ![Employee](https://user-images.githubusercontent.com/75600702/113768205-f6668580-96f5-11eb-9a36-422f3ee1f4be.PNG)
   
# Creating  Pandas Excel writer using XlsxWriter 
      writer = pd.ExcelWriter(r'C:\Users\User\Downloads\data_records2.xlsx', engine='xlsxwriter')
      df.to_excel(writer, sheet_name='data_records')
      authentication.to_excel(writer, sheet_name='authentication')
      employee_records.to_excel(writer, sheet_name='employee_records')
     writer.save()
     print('data_records written successfully to Excel File.')

