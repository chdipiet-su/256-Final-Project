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

m_columns = {
    "size_column1": [ m_shoes[0] ], #US
    "size_column2": [ m_shoes[1] ], #Euro
    "size_column3": [ m_shoes[2] ], #UK
    "size_column_in": [ m_shoes[3] ], #Inches
    "size_column_cm": [ m_shoes[4] ] #CM
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
#print(result)


#WOMEMN
w_shoes.columns = ['US', 'Euro', 'UK', 'Inches', 'CM']

#US
if result == conts["usa"]:
    chart = w_shoes[ w_shoes['US'] == size]
    print(chart)   
#Euro
elif result == conts["euro"]:
    chart = w_shoes[ w_shoes['Euro'] == size]
    print(chart)
#UK
elif result == conts["uk"]:
    chart = w_shoes[ w_shoes['UK'] == size]
    print(chart)
else:
    print("Invalid")


#MEN
m_shoes.columns = ['US', 'Euro', 'UK', 'Inches', 'CM']

#US
if result == conts["usa"]:
    chart = m_shoes[ m_shoes['US'] == size]
    print(chart)   
#Euro
elif result == conts["euro"]:
    chart = m_shoes[ m_shoes['Euro'] == size]
    print(chart)
#UK
elif result == conts["uk"]:
    chart = m_shoes[ m_shoes['UK'] == size]
    print(chart)
else:
    print("Invalid")

