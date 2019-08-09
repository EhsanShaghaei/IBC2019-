#Innopolis University Bootcamp 2019
#@author : Ehsan Shaghaei     github : https://github.com/Ehsan2754/IBC2019/
#Session1
#Task 1
#Labratory 104
#Terms Of Task:
#                           Expressions
#   • Read two integers N1 and N2 from standard input.
#   • Determine if N1 a denominator of N2 or vice versa.
#   • If there is residue of division N1/N2 or N2/N1 - output it.
#   • Determine amount of digits in N1.
#   • Determine if the square root of N2.
#
#
##################################################
#      #InnoBootCamp2019                         #   
#      #PythonLab                                #
#      #EhsanSghaghaei   http://t.me/EhsanSH2754 #   
##################################################

#   TASK >>>> Read two integers N1 and N2 from standard input.
N1 = int (input ('Enter N1 number!\n'))
N2 = int (input ('Enter N2 number!\n'))

#   TASK >>>> Determine if N1 a denominator of N2 or vice versa.
if  N2 % N1 == 0 : print ( str(N1) + " is a denominator of "+ str(N2) + "\n")
else: 
    print (str(N1) + "is a not a denominator of "+str(N2)+ " \n")

#   TASK >>>> If there is residue of division N1/N2 or N2/N1 - output it.
    if (N2 % N1) == N1 : print ("The remainder of N1 to N2 is : " + str(N1 % N2)+'\n')
    else:
        print ("The remainder of N2 to N1 is : " + str(N2 % N1)+'\n')
#   TASK >>>> Determine amount of digits in N1.

#  /*************************SOLUTION 1*************************/
# stringN1 = str (N1)
# digitCounter = 0
# for digit in stringN1 :
#     digitCounter +=1 
# print ('N1 has '+str(digitCounter)+' digits!\n')
# /*************************SOLUTION 2*************************/
print ('N1 has '+str(len(str(N1)))+' digits!\n')
#   TASK >>>> Determine if the square root of N2.
import math
print ('Square root of N1 is : '+ str(math.sqrt(N1))+'\n')
print ('Square root of N2 is : '+ str(math.sqrt(N2))+'\n')
if N1 == math.sqrt(N2) : print ('N1 is the square root of N2.\n')
#Task is Done!!!!
