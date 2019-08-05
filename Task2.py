#Innopolis University Bootcamp 2019
#@author : Ehsan Shaghaei     github : https://github.com/Ehsan2754/IBC2019/
#Sesstion1
#Task 2
#Labratory 104
#Terms Of Task:
#                       Conditions
#• Create app, which reads point coordinates (x, y) from console
# input and outputs coordinate quarter of a point. if point is  
# located on one of the axes, it reports the axes name.
#
#
##################################################
#      #InnoBootCamp2019                         #   
#      #PythonLab                                #
#      #EhsanSghaghaei   http://t.me/EhsanSH2754 #   
##################################################

x = int(input("Enter X \n"))
y = int(input ("Enter Y \n"))
# Task >>>> Checking if the point is on Orgin 
if   x == y == 0 : print ("the point is on Orgin!\n")
# Task >>>> Checking if the point is on Y-axis 
elif x == 0 : print ("the point is on Y-axis!\n")
# Task >>>> Checking if the point is on X-axis 
elif y == 0 : print ("the point is on X-axis!\n")
#Task is Done!!!!