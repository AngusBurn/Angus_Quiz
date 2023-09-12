import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

sql_command = """
SELECT Year, CO2, Temperature FROM ClimateData
"""

cursor.execute(sql_command)
rows = cursor.fetchall()

for row in rows:
    year, co2_record, temp_record = row
    years.append(year)
    co2.append(co2_record)
    temp.append(temp_record)

connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
