#TO DO:
#find HTML table of sizes
#STEPS:

#User is asked if they are male or female
#User is asked if they're shopping for shoes? (Bool=true) 
#User is asked what their country of residence is (string value)
#User is asked where the brand they are shopping for is based (string value)
#Calculate result (using shoe sizes)
#Return conversion value
#Print results

#User is asked if they are male or female
#User is asked if they're shopping for shoes? (Bool=false) 
#User is asked what their country of residence is (string value)
#User is asked where the brand they are shopping for is based (string value)
#Calculate result (using clothing sizes)
#Return conversion value
#Print results

#import HTML charts and Pandas stuff
#4 input statements
#2 functions to claculate results (shoes or clothing)
#2 print statements

#SOPHIA
import lxml.html as LH
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

shoes = pd.read_html('http://www.shoemetro.com/t-shoe-size-chart.aspx')
print(shoes)

'''
Notes
-write more functions up front to shorten input statements
-for each task there should be simple solution
-filter dataframe (look in pandas doc towards the bottom
-filter by column = us and size = 7 then grab that index key and return the whole row from the dataframe
-can use OR in loops as long as there are | pipes | around them
-ln 42 in Pandas doc for filtering except we want 'US' == '7'
-tables are in order of [0], [1], [2], [3] instead of mens, womens, girls, boys

'''








#COURTNEY

gender = input("Are you a male or female? ")
gender = gender.lower()
shoes = input("Are you shopping for shoes? [y/n] ")
shoes = shoes.lower()

#Male/Yes
if gender == 'male' or gender =='m' and shoes == 'y' or shoes == 'yes':
    home = input("What is your country of residence? ")
    home = home.lower()
    size = input(flaot("What size are you?")) 
#Male/No
elif gender == 'male' or gender =='m' and shoes == 'n' or shoes == 'no':
    clothes = input("Are you shopping for clothes? [y/n]")
    clothes = clothes.lower()
    if clothes == 'y' or clothes == 'yes':
        home = input("What is your country of residence? ")
        home = home.lower()
        size = input(flaot("What size are you?"))       
    else:
        print("Program has quit.")
#Female/Yes
elif gender == 'female' or gender =='f' and shoes == 'y' or shoes == 'yes':
    home = input("What is your country of residence? ")
    home = home.lower()
    size = input(flaot("What size are you?")) 
#Female/No
elif gender == 'female' or gender =='f' and shoes == 'n' or shoes == 'no':
    clothes = input("Are you shopping for clothes? [y/n]")
    clothes = clothes.lower()
    if clothes == 'y' or clothes == 'yes':
        home = input("What is your country of residence? ")
        home = home.lower()
        size = input(flaot("What size are you?")) 
    else:
        print("Program has quit.")   
else:
    print("Program has quit.")


#CHRISTINA
#
#
euro = ['germany', 'italy', 'france', 'switzerland', 'poland', 'netherlands', 'the netherlands', 'ukraine', 'greece', 'austria', 'sweden', 'norway', 'malta', 'czech republic', 'belgium', 'iceland', 'finland', 'croatia', 'cyprus', 'romania', 'hungary', 'denmark', 'bulgaria', 'luxembourg', 'monaco', 'slovenia', 'serbia', 'vatican city', 'albania', 'lithuania', 'belarus', 'montenegro', 'estonia', 'moldova', 'slovakia', 'bosnia', 'herzegovina', 'kosovo', 'latvia', 'san marino', 'macedonia', 'liechtenstein', 'andorra', 'gibraltar', 'faroe islands', 'isle of man', 'jersey', 'svalbard', 'jan mayen', 'aland islands']
uk = ['great britain', 'ireland', 'scotland', 'wales']
usa = ['usa', 'u.s.a.', 'america', 'north america']


"""
give new_location which is whatever continent their home country is in (eure, uk, or usa)
match up new_location with size

new_size = shoes[[home,

TO DO:

For loops that iterate through 3 country lists to find continent of origin (return value, 'home_continent' - just a new name for the list that already exisit)
Be able to match that varable with the name of the column on the HTML table
Iterate through that specific column looking for 'size'
Find where size exists in column under continent of origin on HTML table and return the entire corresponding row in the form of a dataframe
Create a string sntence to print out that is populated with new variables






"""





