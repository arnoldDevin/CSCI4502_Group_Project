import pandas as pd

dfYelp = pd.read_csv('yelp-dataset/yelp_business_attributes.csv')
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

dfYelp.head(100)
dfYelp = dfYelp.rename(index = str, columns={"HasTV":"Alcohol_true"})
dfYelp = dfYelp.rename(index = str, columns={"Alcohol":"HasTV"})
dfYelp = dfYelp.rename(index = str, columns={"Alcohol_true":"Alcohol"})

dfYelp = dfYelp.rename(index = str, columns={"RestaurantsAttire":"NoiseLevel_true"})
dfYelp = dfYelp.rename(index = str, columns={"NoiseLevel":"RestaurantsAttire"})
dfYelp = dfYelp.rename(index = str, columns={"NoiseLevel_true":"NoiseLevel"})
      
dfYelp = dfYelp.rename(index = str, columns={"RestaurantsReservations":"WiFi_true"})
dfYelp = dfYelp.rename(index = str, columns={"WiFi":"RestaurantsReservations"})
dfYelp = dfYelp.rename(index = str, columns={"WiFi_true":"WiFi"})

dfYelp = dfYelp.rename(index = str, columns={"DriveThru":"Smoking_true"})
dfYelp = dfYelp.rename(index = str, columns={"Smoking":"DriveThru"})
dfYelp = dfYelp.rename(index = str, columns={"Smoking_true":"Smoking"})

dfYelp = dfYelp.rename(index = str, columns={"RestaurantsCounterService":"AgesAllowed_true"})
dfYelp = dfYelp.rename(index = str, columns={"AgesAllowed":"RestaurantsCounterService"})
dfYelp = dfYelp.rename(index = str, columns={"AgesAllowed_true":"AgesAllowed"})


dfYelp.apply(lambda x: len(x.unique()))

dfYelp['Alcohol'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['Alcohol'].replace(to_replace = 'none', value =0 , inplace = True )

dfYelp['DietaryRestrictions_vegetarian'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DietaryRestrictions_vegetarian'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DietaryRestrictions_vegetarian'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DietaryRestrictions_soy-free'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DietaryRestrictions_soy-free'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DietaryRestrictions_soy-free'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DietaryRestrictions_halal'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DietaryRestrictions_halal'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DietaryRestrictions_halal'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DietaryRestrictions_kosher'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DietaryRestrictions_kosher'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DietaryRestrictions_kosher'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DietaryRestrictions_vegan'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DietaryRestrictions_vegan'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DietaryRestrictions_vegan'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DietaryRestrictions_gluten-free'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DietaryRestrictions_gluten-free'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DietaryRestrictions_gluten-free'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['AgesAllowed'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['AgesAllowed'].replace(to_replace = 'True', value =1 , inplace = True )
dfYelp['AgesAllowed'].replace(to_replace = '18plus', value =18 , inplace = True )
dfYelp['AgesAllowed'].replace(to_replace = '21plus', value =21 , inplace = True )

dfYelp['RestaurantsCounterService'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsCounterService'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['RestaurantsCounterService'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BYOB'].replace(to_replace = 'Na', value =0 , inplace = True )

dfYelp['Open24Hours'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['Open24Hours'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['Open24Hours'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessAcceptsBitcoin'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessAcceptsBitcoin'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessAcceptsBitcoin'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DogsAllowed'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DogsAllowed'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DogsAllowed'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['DriveThru'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['DriveThru'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['DriveThru'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['Smoking'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['Smoking'].replace(to_replace = 'no', value =0 , inplace = True )
dfYelp['Smoking'].replace(to_replace = 'outdoor', value =1 , inplace = True )
dfYelp['Smoking'].replace(to_replace = 'yes', value =2 , inplace = True )

dfYelp['CoatCheck'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['CoatCheck'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['CoatCheck'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForMeal_brunch'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForMeal_brunch'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForMeal_brunch'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForMeal_breakfast'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForMeal_breakfast'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForMeal_breakfast'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForMeal_dinner'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForMeal_dinner'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForMeal_dinner'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForMeal_lunch'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForMeal_lunch'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForMeal_lunch'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForMeal_latenight'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForMeal_latenight'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForMeal_latenight'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForMeal_dessert'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForMeal_dessert'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForMeal_dessert'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_sunday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_sunday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_sunday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_saturday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_saturday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_saturday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_friday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_friday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_friday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_thursday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_thursday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_thursday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_wednesday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_wednesday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_wednesday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_tuesday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_tuesday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_tuesday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BestNights_monday'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BestNights_monday'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BestNights_monday'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['RestaurantsDelivery'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsDelivery'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['RestaurantsDelivery'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['OutdoorSeating'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['OutdoorSeating'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['OutdoorSeating'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['RestaurantsTableService'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsTableService'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['RestaurantsTableService'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForDancing'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['GoodForDancing'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['GoodForDancing'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['HappyHour'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['HappyHour'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['HappyHour'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['RestaurantsTakeOut'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsTakeOut'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['RestaurantsTakeOut'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['WiFi'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['WiFi'].replace(to_replace = 'no', value =0 , inplace = True )
dfYelp['WiFi'].replace(to_replace = 'free', value =1 , inplace = True )
dfYelp['WiFi'].replace(to_replace = 'paid', value =2 , inplace = True )

dfYelp['RestaurantsReservations'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsReservations'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['RestaurantsReservations'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['Caters'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['Caters'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['Caters'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['Music_live'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['Music_live'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['Music_live'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['RestaurantsAttire'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsAttire'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['RestaurantsAttire'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['NoiseLevel'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['NoiseLevel'].replace(to_replace = 'average', value =2 , inplace = True )
dfYelp['NoiseLevel'].replace(to_replace = 'very_loud', value =4 , inplace = True )
dfYelp['NoiseLevel'].replace(to_replace = 'quiet', value =1 , inplace = True )
dfYelp['NoiseLevel'].replace(to_replace = 'loud', value =3 , inplace = True )

dfYelp['HasTV'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['HasTV'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['HasTV'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BikeParking'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BikeParking'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BikeParking'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['WheelchairAccessible'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['WheelchairAccessible'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['WheelchairAccessible'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['GoodForKids'].replace(to_replace = 'Na', value =0 , inplace = True )

dfYelp['RestaurantsPriceRange2'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['RestaurantsPriceRange2'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['HairSpecializesIn_africanamerican'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['HairSpecializesIn_africanamerican'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['HairSpecializesIn_coloring'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['HairSpecializesIn_coloring'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['HairSpecializesIn_coloring'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessParking_valet'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessParking_valet'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessParking_valet'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessParking_lot'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessParking_lot'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessParking_lot'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessParking_street'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessParking_street'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessParking_street'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessParking_garage'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessParking_garage'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessParking_garage'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessParking_validated'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessParking_validated'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessParking_validated'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['BusinessAcceptsCreditCards'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['BusinessAcceptsCreditCards'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['BusinessAcceptsCreditCards'].replace(to_replace = 'True', value =1 , inplace = True )

dfYelp['ByAppointmentOnly'].replace(to_replace = 'Na', value =0 , inplace = True )
dfYelp['ByAppointmentOnly'].replace(to_replace = 'False', value =0 , inplace = True )
dfYelp['ByAppointmentOnly'].replace(to_replace = 'True', value =1 , inplace = True )



#Deletes columns with only one value
columns = ['AcceptsInsurance',
           'Corkage',
           'DietaryRestrictions_dairy-free',
           'HairSpecializesIn_curly',
           'HairSpecializesIn_perms',
           'HairSpecializesIn_kids',
           'HairSpecializesIn_extensions',
           'HairSpecializesIn_asian',
           'HairSpecializesIn_asian',
           'Music_dj',
           'Music_background_music',
           'Music_no_music',
           'Music_karaoke',
           'Music_jukebox',
           'Music_video',
           'Ambience_intimate',
           'Ambience_classy',
           'Ambience_hipster',
           'Ambience_divey',
           'Ambience_touristy',
           'Ambience_upscale',
           'Ambience_casual',
           'Ambience_romantic',
           'RestaurantsGoodForGroups',
           'BYOBCorkage',
           'Ambience_trendy',
           'HairSpecializesIn_straightperms',
           ]
dfYelp.drop(columns, inplace = True, axis =1)

#dfYelp.to_csv('clean_yelp_business_attributes.csv')