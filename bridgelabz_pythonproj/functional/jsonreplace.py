'''
/**********************************************************************************
* Purpose: Read in the following message: Hello <<name>>, We have your full
* name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx.
* Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
* Use Regex to replace name, full name, Mobile#, and Date with proper value.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 7-1-2019
*
***********************************************************************************/
'''
import re
import datetime

s = datetime.date.today()  # current date
given_string = """                    

Hello <<name>>, 
We have your full name as <<full name>> in our system. 
your contact number is 91­xxxxxxxxxx.
Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
"""
# format of output

# user input
name = input("enter name ")
full_name = input("enter full name ")
phone = input("enter number ")

n = re.sub(r"<<name>>", name, given_string)  # replace function
f = re.sub(r"<<full name>>", full_name, n)

p = re.sub(r"xxxxxxxxxx", phone, f)

regex_val = "\w{3} \w{3} \w{4}"  # number validation

if re.search(regex_val, p):
    print("Valid phone number")

    d = re.sub(r"01/01/2016", str(s), p)

    print(d)
else:
    print("invalid number")
