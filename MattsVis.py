import numpy as np
import csv
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

o = open('yelp_business_attributes.csv')
dogsAllowed = [] #column 33
alcohol = []
smoking = []
hasTV = []
happyHour = []
goodForKids = []

csv_o = csv.reader(o)
for row in csv_o:
	dogsAllowed.append(str(row[67]))
	alcohol.append(str(row[21]))
	smoking.append(str(row[65]))
	hasTV.append(str(row[27]))
	happyHour.append(str(row[46]))
o.close()

alc = 0
smoke = 0
TV = 0
happy = 0
kids = 0

for value in range(len(dogsAllowed)):
	if (dogsAllowed[value] == "TRUE" and alcohol[value] == "TRUE"):
		alc += 1
	if (dogsAllowed[value] == "TRUE" and smoking[value] == "TRUE"):
		smoke += 1
	if (dogsAllowed[value] == "TRUE" and hasTV[value] != "Na"):
		TV += 1
	if (dogsAllowed[value] == "TRUE" and happyHour[value] == "TRUE"):
		happy += 1
	if (dogsAllowed[value] == "TRUE" and goodForKids[value] != "Na"):
		kids += 1


dogsAlloweds = ["Alcohol", "Smoking", "Has a TV", "Happy Hour", "Good for Kids"]

p = figure(x_range=dogsAlloweds, plot_height=350, title="Ammount of Places That Allow Dogs as well as Other Things",
          toolbar_location=None, tools="")

p.vbar(x=dogsAlloweds, top=[alc, smoke, TV, happy, kids], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
output_file("dogsAllowed_Vs_Fear.html", title="Ammount of Places That Allow Dogs as well as Other Things")
