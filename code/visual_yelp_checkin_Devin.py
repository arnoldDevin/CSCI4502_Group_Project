import numpy as np
import csv
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

o = open('yelp_checkin.csv')
business_id = []
weekday = []
hour = []
checkins = []

csv_o = csv.reader(o)
for row in csv_o:
	business_id.append(str(row[0]))
	weekday.append(str(row[1]))
	hour.append(str(row[2]))
	checkins.append(str(row[3]))
o.close()

mon = 0; tue = 0; wed = 0; thu = 0; fri = 0; sat = 0; sun = 0

for value in range(len(business_id)):
	if weekday[value] == "Mon":
		mon = mon + int(checkins[value])
	if weekday[value] == "Tue":
		tue = tue + int(checkins[value])
	if weekday[value] == "Wed":
		wed = wed + int(checkins[value])
	if weekday[value] == "Thu":
		thu = thu + int(checkins[value])
	if weekday[value] == "Fri":
		fri = fri + int(checkins[value])
	if weekday[value] == "Sat":
		sat = sat + int(checkins[value])
	if weekday[value] == "Sun":
		sun = sun + int(checkins[value])

print(mon)
print(tue)
print(wed)
print(thu)
print(fri)
print(sat)
print(sun)

axis = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

hist = figure(x_range=axis, plot_height=350, title="Frequency of checkins versus days",
          toolbar_location=None, tools="")
hist.vbar(x=axis, top=[sun, mon, tue, wed, thu, fri, sat], width=0.9)
hist.left[0].formatter.use_scientific = False
hist.xgrid.grid_line_color = None
hist.y_range.start = 0

show(hist)



