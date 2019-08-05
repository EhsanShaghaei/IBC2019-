#Innopolis University Bootcamp 2019
#@author : Ehsan Shaghaei     github : https://github.com/Ehsan2754/IBC2019/
#Sesstion1
#Task 3
#Labratory 104
#Terms Of Task:
#                                   Strings
#   Create app which reads two strings - Name and Surname from standard input and:
#    • Determines if which part of name is longer and outputs it.
#    • Outputs the full name and its length.
#
#
##################################################
#      #InnoBootCamp2019                         #   
#      #PythonLab                                #
#      #EhsanSghaghaei   http://t.me/EhsanSH2754 #   
##################################################
firstName = input ('Enter your first name!\n')
lastName  = input ('Enter your last name!\n')
#    Task >>>> Determines if which part of name is longer and outputs it.
if   len(firstName)  > len(lastName) : print ('Your first name is a longer string!\n')
elif len(firstName)  < len(lastName) : print ('Your last  name is a longer string!\n')
elif len(firstName) == len(lastName) : print ('Your first name has the same length as your last name!\n')
#    Task >>>> Outputs the full name and its length.
fullName = firstName + ' ' + lastName
print ('Your full name is '+fullName+ " and it's lenght is "+ str(int(len(firstName))+int(len(lastName)))+'\n')
#Task is Done!!!!
