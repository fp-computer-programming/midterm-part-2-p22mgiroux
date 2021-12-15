# Author: MOG 12/15/21

vi = input("What is the initial velocity? ")
vf = input("What is the final velocity? ")
t = input("What is the time? ")

a = (float(vf) - float(vi)) / float(t)

print("The average velocity is {} m/s^2.".format(a))