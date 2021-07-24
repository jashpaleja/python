# import re
#
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
# import re


# # validation of Mobile No.
# def ValidateMob(no):
#     if len(no) != 13:
#         print("Invalid mobile no.")
#         return False
#     m = re.search("[+91][7-9]", no)
#     if m.start() == 0:
#         print("No. succesfully validated")
#     else:
#         print("Invalid no. for India")
#
#
# ValidateMob("+917977911127")
# #validation of Email Id
# import re
#
# def ValidateEmail(email):
#     regex= '[a-z]+[0-9]*@[a-z]+[\.][a-z]'
#     if re.search(regex,email):
#         print("Valid email")
#     else :
#         print("Invalid")
#
# email="abc.xyz@gmail.com"
# ValidateEmail(email)
# import re
#
# txt = "my name is jash paleja"
# x = re.split("\s", txt)
# print(x)

import re

txt = "my name is jasz"
x = re.sub("z", "h", txt)
print(x)
