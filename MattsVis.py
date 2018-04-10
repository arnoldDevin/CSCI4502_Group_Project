import numpy as np
import csv
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

o = open('yelp_business_attributes.csv')
dogsAllowed = []
alcohol = []
smoking = []
hasTV = []
happyHour = []
goodForKids = []

#Open CSV, read in certain columns and append each
#of their values to a list named after thei attribute
csv_o = csv.reader(o)
for row in csv_o:
	dogsAllowed.append(str(row[67]))
	alcohol.append(str(row[21]))
	smoking.append(str(row[65]))
	hasTV.append(str(row[27]))
	happyHour.append(str(row[46]))
	goodForKids.append(str(row[18]))
o.close()

#These variables are used to find the amount of 'Trues' or non-'Na'
alc = 0
smoke = 0
TV = 0
happy = 0
kids = 0
count = 0

for value in range(len(dogsAllowed)):
	#There are NO places where these attributes are both true, this is ignored pretty much
	#A lot of the attributes just have and entire column of Na's
	if (dogsAllowed[value] == 'True' and alcohol[value] == 'True'):
		alc = alc + 1
	if (dogsAllowed[value] == 'True' and smoking[value] == 'True'):
		smoke = smoke +  1
	if (dogsAllowed[value] == 'True' and hasTV[value] != 'Na'):
		TV = TV + 1
	if (dogsAllowed[value] == 'True' and happyHour[value] == 'True'):
		happy = happy + 1
	if alcohol[value] == 'True' and goodForKids[value] != 'Na':
		kids = kids + 1

	#Counted up the amount of places that serves alcohol, allows smoking, has
	#a TV, and is good for kids. Compared them all on a bar chart
	if (alcohol[value] == 'True'):
		alc = alc + 1
	if (smoking[value] == 'True'):
		smoke = smoke +  1
	if (hasTV[value] != 'Na'):
		TV = TV + 1
	if (happyHour[value] == 'True'):
		happy = happy + 1
	if goodForKids[value] != 'Na':
		kids = kids + 1


#Bar Chart
dogsAlloweds = ["Alcohol", "Smoking", "Has a TV", "Happy Hour", "Good for Kids"]

p = figure(x_range=dogsAlloweds, plot_height=350, title="Ammount of Places That Allow Dogs as well as Other Things",
          toolbar_location=None, tools="")

p.vbar(x=dogsAlloweds, top=[alc, smoke, TV, happy, kids], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
output_file("dogsAllowed_Vs_Fear.html", title="Ammount of Places That Allow Dogs as well as Other Things")
