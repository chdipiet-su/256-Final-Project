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

#COURTNEY
"""
gender = input("Are you a male or female? ")
shoes = input("Are you shopping for shoes? [y/n] ")

#Male/Yes
if gender == 'male' or gender =='m' and shoes == 'y' or shoes == 'yes':
    home = input("What is your country of residence? ")
    location = input("What country is the brand you're shopping for from? ")
#Male/No
elif gender == 'male' or gender =='m' and shoes == 'n' or shoes == 'no':
    clothes = input("Are you shopping for clothes? [y/n]")
    if clothes == 'y' or clothes == 'yes':
        home = input("What is your country of residence? ")
        location = input("What country is the brand you're shopping for from? ")
    else:
        print("Program has quit.")
#Female/Yes
elif gender == 'female' or gender =='f' and shoes == 'y' or shoes == 'yes':
    home = input("What is your country of residence? ")
    location = input("What country is the brand you're shopping for from? ")
#Female/No
elif gender == 'female' or gender =='f' and shoes == 'n' or shoes == 'no':
    clothes = input("Are you shopping for clothes? [y/n]")
    if clothes == 'y' or clothes == 'yes':
        home = input("What is your country of residence? ")
        location = input("What country is the brand you're shopping for from? ")
    else:
        print("Program has quit.")   
else:
    print("Program has quit.")

"""
#CHRISTINA
#
#
