# Solution of Exercise 5 - Exercise_5.py
#
# Uploaded by Aurimas A. Nausedas on 11/23/20.
# Updated by Aurimas A. Nausedas on 11/06/21.

name = 'Aurimas A. Nausedas' 
age = 31 # age when updated 1st time
height = 74 # inches
weight = 220 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "He weighs %f kgs." % (weight * 0.453592)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print"If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
