import csv
import os

import pandas as pd

# Clearing screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Variables
file = "finalData.csv"
sp = "-" * os.get_terminal_size().columns

# Reading the csv.
rows = []

with open(file,'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
headers = rows[0]
star_data = rows[1:]
df = pd.read_csv(file)
solar_mass_list = df["solar_mass"].tolist()
solar_radius_list = df["solar_radius"].tolist()
solar_mass_list.pop(0)
solar_radius_list.pop(0)

# Convert star solar mass into si unit or kilogram.
star_solar_mass_si_unit = []
for data in solar_mass_list:
    si_unit = float(data)*1.989e+30
    star_solar_mass_si_unit.append(si_unit)
print("\nStar Solar Mass SI unit ->",star_solar_mass_si_unit[5],"<- See full data at ' gravity.csv ' .")

# Convert star solar radius into SI unit or meters.
star_solar_radius_si_unit = []
for data in solar_radius_list:
    si_unit = float(data)* 6.957e+8
    star_solar_radius_si_unit.append(si_unit)
print("\nStar Solar Radius SI unit ->",star_solar_radius_si_unit[8],"<- See full data at ' gravity.csv ' .")

# Calculate the gravity of each planet.
total_masses = []
total_radiuses  = []

star_masses = star_solar_mass_si_unit
star_radiuses = star_solar_radius_si_unit
star_names = df["star_names"].tolist()
star_names.pop(0)
star_gravities = []
for index,data in enumerate(star_names):  
    a = float(star_masses[index])*5.972e+24
    b = float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000*6.674e-11    
    total_masses.append(a)
    total_radiuses.append(b)
    gravity =  0 
    if int(b):
        gravity =  a/b     
    star_gravities.append(gravity)
print("\nStar Gravities ->",star_gravities[2],"<- See full data at ' gravity.csv ' .\n")
print("\nTotal Masses of all stars in data ->",total_masses[5],"<- See full data at ' gravity.csv ' .")
print("\nTotal Radiuses of all stars in data ->",total_masses[3],"<- See full data at ' gravity.csv ' .")

# Create a new csv with gravity data.
star_gravities.append("extra")
df["star_gravity"] = star_gravities


# Printing divider and Data.
print("\nGravity Data", sp)
print(df.head())
print(sp, "\n")

# Storing all data into gravity.csv file .
df.to_csv("gravity.csv",index=False)
