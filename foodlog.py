
import os
import csv

startnum = int(input("enter starnum: "))
stop =0
foods = []
foods.append(['Date', 'Food'])
drive = 'C:/Users/Rebecca/Google Drive/Junior Semester 1/Ethics/FoodLogDays csvs/DailySummary'
drive2 = 'C:/Users/Rebecca/Google Drive/Junior Semester 1/Ethics/FoodLogDays csvs/'
while startnum < 4800:
	if os.path.exists( drive + str(startnum) +'.csv'): 
		openfile = open (drive+ str(startnum) +'.csv', 'r')
		reader = csv.reader(openfile)
		
		i =0
		for row in reader:
			if i>0:
				date = row[0]
				food = row[1]
				foods.append([date,food])
			i +=1
		startnum+=1
		foods.append(['', ''])
	else:		
		startnum+=1
		stop+=1
		if stop == 5:
			break

with open(drive2 + 'foodlog.csv', 'w') as foodfile:
        foodwriter = csv.writer(foodfile)
        for item in foods:
                foodwriter.writerow(item)
openfile.close()
