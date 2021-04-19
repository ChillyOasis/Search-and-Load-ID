# Name: Brian Ong Boon Choon
# UOW: 6355018
# CSIT110

import csv
filePath = "data.csv"
with open(filePath) as csvfile:
    reader = csv.DictReader(csvfile)
    
    row_num = 0
    row_end = 2
    
    inputID = input("Enter Avatar ID: ")
    
    while (inputID == ""):
        print("Empty input, please enter again\n")
        inputID = input("Enter Avatar ID: ")
    
    for row in reader:
        
        if (inputID == row['id']):
            
            print("===============================================")
            print("{0:<10} | {1:>12} | {2:<12}" .format("Avatar ID", "Avatar Name", "Avatar Tribe"))
            print("{0:<10} | {1:>12} | {2:<12}" .format(row['id'], row['name'], row['tribe']))
            print("===============================================")
            
            air = int(row['Air'])
            water = int(row['Water'])
            earth = int(row['Earth'])
            fire = int(row['Fire'])
            
            average = (air + water + earth + fire)/4
            
            print("Four elements power")
            print("===============================================")
            print("{0:>5} | {1:>5} | {2:>5} | {3:>5} | {4:^12}" .format("Air", "Water", "Earth", "Fire", "Average power"))        
            print("{0:>5} | {1:>5} | {2:>5} | {3:>5} | {4:^12}" .format(row['Air'], row['Water'], row['Earth'], row['Fire'], average))
            print("===============================================")
            
        else:
            row_num += 1
        
        if ((inputID != row['id']) and (row_num == row_end)):
            print("No Avatar record found")
        

        
