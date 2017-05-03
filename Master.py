#TO DO:
#find HTML table of sizes
#STEPS:
#User is asked if they are male or female
#User is asked what their country of residence is (string value)
#User is asked where the brand they are shopping for is based (string value)
#Calculate result (using shoe sizes)
#Return conversion value
#Print results

'''
Notes
-write more functions up front to shorten input statements
-for each task there should be simple solution
-filter dataframe (look in pandas doc towards the bottom)
-filter by column = us and size = 7 then grab that index key and return the whole row from the dataframe
-can use OR in loops as long as there are | pipes | around them
-ln 42 in Pandas doc for filtering except we want 'US' == '7'
-tables are in order of [0], [1], [2], [3] instead of mens, womens, girls, boys
'''

import lxml.html as LH
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

shoes = pd.read_html('http://www.shoemetro.com/t-shoe-size-chart.aspx')
#print(shoes)

w_shoes = shoes[2]
m_shoes = shoes[3]

w_columns = {
    "size_column1": [ w_shoes[0] ], #US
    "size_column2": [ w_shoes[1] ], #Euro
    "size_column3": [ w_shoes[2] ], #UK
    "size_column_in": [ w_shoes[3] ], #Inches
    "size_column_cm": [ w_shoes[4] ] #CM
}

conts = {
    "euro": ['germany', 'italy', 'france', 'switzerland', 'poland', 'netherlands', 'the netherlands', 'ukraine', 'greece', 'austria', 'sweden', 'norway', 'malta', 'czech republic', 'belgium', 'iceland', 'finland', 'croatia', 'cyprus', 'romania', 'hungary', 'denmark', 'bulgaria', 'luxembourg', 'monaco', 'slovenia', 'serbia', 'vatican city', 'albania', 'lithuania', 'belarus', 'montenegro', 'estonia', 'moldova', 'slovakia', 'bosnia', 'herzegovina', 'kosovo', 'latvia', 'san marino', 'macedonia', 'liechtenstein', 'andorra', 'gibraltar', 'faroe islands', 'isle of man', 'jersey', 'svalbard', 'jan mayen', 'aland islands'],
    "uk": ['great britain', 'ireland', 'scotland', 'wales'],
    "usa": ['usa', 'us', 'u.s.', 'u.s.a.', 'america', 'north america']
}

gender = input("Are you a male or female? ")
gender = gender.lower()

#Male
if gender == 'male' or gender =='m':
    home = input("What is your country of residence? ")
    home = home.lower()
    size = input("What size are you? ")       
#Female
elif gender == 'female' or gender =='f':
    home = input("What is your country of residence? ")
    home = home.lower()
    size = input("What size are you? ")  
else:
    print("Program has quit.")

def get_continent_list(home, dict_of_conts):
    for key in dict_of_conts:
        if home in dict_of_conts[key]:
            return dict_of_conts[key]

result = get_continent_list(home, conts)
print(result)

<<<<<<< HEAD
#^^^^^ DONT TOUCH ^^^
'''
def get_size_df(get_continent_list, size):
     return w_shoes[w_shoes[result] == size]

result_2 = get_size_df(get_continent_list, conts)
print(result_2)
'''
=======
# ^^^ DON'T TOUCH ^^^


w_shoes.columns = ['US', 'Euro', 'UK', 'Inches', 'CM']

#US
if result == usa:
    chart = w_shoes[ w_shoes['US'] == size]
    print(chart)

#Euro
elif result == euro:
    chart = w_shoes[ w_shoes['Euro'] == size]
    print(chart)

#UK
elif result == uk:
    chart = w_shoes[ w_shoes['UK'] == size]
    print(chart)

else:
    print("Invalid")

>>>>>>> upstream/master



<<<<<<< HEAD
for cont in dict_of_conts():
    if cont['USA'] == size:
        print("%s with a size of %.3f is on the Dean's list." % (student['Name'], student['GPA']) )
=======
'''
def get_size_column(size, dict_of_columns):
    for result in w_shoes:
        for key in dict_of_columns:
            if size in dict_of_columns[key]:
                print("hello")
                return dict_of_columns[key]
            else:
                print("hi")
    #        index_series = pd.Series( columns = ['US', 'Euro', 'UK', 'Inches', 'CM'] )
    #        print(index_series)

answer = get_size_column(result, w_columns)
'''

'''
shoes = pd.read_html('http://www.shoemetro.com/t-shoe-size-chart.aspx')
#print(shoes)

w_shoes = shoes[2]
m_shoes = shoes[3]


#THEORY1
us_data = pd.Series( data = 
euro_data = pd.Series( data =
uk_data = pd.Series( data =
inches_data = pd.Series( data =
cm_data = pd.Series( data = 
>>>>>>> upstream/master


series_dict = { 'US': us_data, 'Euro': euro_data,  'UK': uk_data,  'Inches': inches_data, 'CM': cm_data } #fill in with appropriate variables
table = pd.DataFrame( series_dict )
print(table)
#THEORY1






#THEORY2
for size in result():
    if conts['US'] == size:
        print(pd.DataFrame( series_dict, columns = ['US', 'Euro', 'UK', 'Inches', 'CM'] ))

#THEORY2






#THEORY3
def get_size_df(get_continent_list, size):     #Don't know about this yet?
     return w_shoes[w_shoes[result] == size]

result_2 = get_size_df(get_continent_list, conts)
print(result_2)
#THEORY3



#THEORY4
deans_list = students[ ['Name', 'GPA'] ][ students.GPA >= 3.4 ]
#THEORY4



'''



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
