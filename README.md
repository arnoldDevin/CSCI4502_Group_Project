# Yelp Us! 

Team 18 CSCI4502_Group_Project Team 

Video: https://www.screencast.com/t/x9kemBofvg6x

## Team Members

Taylor Gunter

Devin Arnold

Matthew Coker

## Project Description
This project answers the question of if successful businesses have more in common than just good service. Using association rules, clustering, decision trees, confusion matrices, and built in python tools, we were able to determine what successful businesses have in common, what uncommon businesses have in common, and how the two differ. Our primary data set is provided by kaggle and yelp, the files included are as follows:

yelp_business.csv,
yelp_business_attributes.csv, yelp_checkins.csv, and
yelp_business_hours.csv

Our secondary data set which is integrated with the primary data set is titled MedianZip-3.xlsx which has been integrated with yelp_business.csv to make yelp_money_merge.csv. This file was used to create a map of the Phoenix area mean income distribution, Business open of closed map, and a map clustering represented businesses.

We performed data cleaning on the entire data set. Getting rid of nan values, discarding attributes deemed unimportant, cleaned empty attributes, simplified attributes (2 unique values instead of 3 or more), discarding sparse tuples and non-business tuples, and changing string values to integers. For example, the clean version of yelp_business_attributes.csv which is called clean_test.csv contain attributes that only have values of 0's and 1's representing 'yes' and 'no'. But some attributes have multiple unique values of up to 5. For example, in yelp_business_attributes.csv, we changed the values under the 'Smoking' which were 0, "Outdoor", and "Yes" to integers where "Outdoor" is represented by the number 1 and "Yes" is represented by the number 2. We also did this for the "RestaurantsPriceRange2", where the values are translated and range from 0-4 representing how expensive a business is.

This project uses several different tools, we mainly coded in python in jupyter notebook using different libraries. The librarires and tools we used are Pandas, Numpy, Scikit-learn, Mlxtend, Matplotlib, and Bokeh. Mlxtend is a toolkit downloaded from anaconda used for doing association rules on the clean_data.csv. Using these tools as well as a now clean data set. We are able to perform data mining to answer the question what what makes businesses successful and unsuccessful.

## Summary of Questions Sought and Answered

What makes a business successful?

Are these attributes specific?

In order to answer the ultimate question of what successful and unsuccessful businesses have in common, we must use the knowledge gained from the data:

Data sets are very sparsely populated.

Support and confidence are very low for many item sets and item pairs.

The Application:

This knowledge can be applied to where to locate a future business. This information can be used to show the factors for what makes a business successful as well as finding correlations between successful businesses.

The Answers:

Checkins and stars are the largest determining factors in whether a business succeeds or fails. This is as expected, the more ratings a business has with a high average star count will lead to a business most likely succeeding. The surrounding population size and median income of an area make a difference if a business succeeds. More specifically, a surrounding population over 33,000 and income over 29,000. 












