"""
Sammenlikning av årlige kostnader for bensinbil og elbil.
Nina N. Egeberg (niege3523@usn.no)
Oppdatert 2025 09 22
"""
Km = 12000  # [Antall km per år]
TF = 8.38*365  # [Sum Trafikk forsikring per år]

DEl = (Km*0.2)*2  # [Sum Kostnad drivstoff elbil per år]
Fel = 5000  # [Sum Forsikring elbil per år]
BEl = Km*0.1  # [Sum Bomavgift elbil per år]
E = TF+DEl+Fel+BEl  # [Kostnad elbil total per år]

DB = Km*1  # [Sum Drivstoff bensin per år]
FB = 7500  # [Sum Forsikring bensin per år]
BB = Km*0.3  # [Sum Bomavgift bensin per år]
B = TF+DB+FB+BB  # [Kostnad bensinbil total per år]

print("Totalkostnad for bensinbil =",B)
print("Totalkostnad for elbil =",E)
print("Sum differanse =",B-E)
