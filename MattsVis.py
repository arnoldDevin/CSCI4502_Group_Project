import numpy as np
import csv
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

o = open('yelp_business_attribtues.csv')
dogsAllowed = [] #column 33
alcohol = []
smoking = []
hasTV = []
happyHour = []
goodForKids = []

csv_o = csv.reader(o)
for row in csv_o:
	dogsAllowed.append(str(row[68]))
	alcohol.append(str(row[22]))
	smoking.append(str(row[66])
	hasTV.append(str(row[23]) #full_bar and beer_and_wine
	happyHour.append(str(row[47])
o.close()

dogs = 0
alc = 0
smoke = 0
TV = 0
happy = 0
kids = 0

for value in range(len(dogsAllowed)):
	if (dogsAllowed[value] == "TRUE" && alcohol[value] == "TRUE"):
		alc += 1
	if (dogsAllowed[value] == "TRUE" && smoking[value] == "TRUE"):
		smoke += 1
	if (dogsAllowed[value] == "TRUE" && hasTV[value] == "TRUE"):
		TV += 1
	if (dogsAllowed[value] == "TRUE" && happyHour[value] == "TRUE"):
		happy += 1
	if (dogsAllowed[value] == "TRUE" && goodForKids[value] == "TRUE"):
		kids += 1
dogsAlloweds = ["Tech Savy/No Privacy", "Tech Savvy/Lose Touch", "Tech Savvy/Less Safe", "Tech Savvy/None Fear", "Tech Savvy/Other"]

p = figure(x_range=dogsAlloweds, plot_height=350, title="Tech Savvy People's Biggest Technological Fear",
           toolbar_location=None, tools="")

p.vbar(x=dogsAlloweds, top=[dogsAllowed, alcohol, smoking, hasTv, happyHour], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
output_file("dogsAllowed_Vs_Fear.html", title="dogsAllowed Level Vs Biggest Fear")
