import math
# This program is a calculator for interest on investment and home loan
#  User needs to select the operation they want to execute

s_investment = "investment - to calculate the amount of interest you'll earn from your investment"
s_bond = "bond - to calculate the interest you'll have to pay on a home loan"
print(s_investment)
print(s_bond)

menu = input("Enter either 'investment' or 'bond' from the menu above to proceed : ")

# Statement for investment selection

if menu == "investment" or menu == "INVESTMENT" or menu == "Investment":
 
 P = int(input("How much you want to deposit? "))
 r = int(input("What percentage of interest rate you want to apply to your investment? "))
 t = int(input("For how many years do you plan to invest? "))
 interest = input("Please enter 'simple' or 'compound' interest : ")
 
 if interest == "simple":
  s_investment = P * (1 + ((r/100) * t))
  print(s_investment)
 if interest == "compound":
  n = int(input("Please enter numbers of compound per year : "))
  s_investment = P * (pow((1 + ((r/100)/n)), n*t))
  print(s_investment)
 
# Statement for bond selection
   

elif menu == "bond" or menu == "BOND" or menu == "Bond":

 P =int(input("Enter your house present value : "))
 i = (int(input("Enter the interest rate : "))/100)/12
 n = int(input("For how many months do you plan to repay? "))
 s_bond = (i * P) / (1 - (1 + i) ** (-n))
 print(s_bond)

else : 
  print("Error : Invalid input")
  



 