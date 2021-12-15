# Author: MOG 12/15/21

distance = input("What is the driving distance in miles? ")
mpg = input("What is the fuel efficiency of your landspeeder miles/gallon? ")
price = input("What is the price of fuel/gallon in credits? ")

trip_cost = (float(distance) / float(mpg)) * float(price)


print("The total cost of your {} mile trip will be {} credits.".format(distance, trip_cost))
