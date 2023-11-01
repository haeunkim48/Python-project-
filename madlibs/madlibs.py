# string concatenation (how to put strings together)
youtuber = "" # some string variable 

# a few ways to do this 
#print ("subscribe to" + youtuber)
#print ("subscribe to {} ".format(youtuber)) 
#print (f"subscribe to {youtuber}") # we can define the string by adding f in front of the string 

adj = input ("Adjective : ")
verb1 = input ("Verb: ")
verb2 = input ("Verb: ")
famous_person = input ("Famous person: ")

madlib = f"Computer programming is so {adj}ama! It makes me so excited all the time because I love to {verb1}. Stay healthy and {verb2} like you are {famous_person}!"


print (madlib)
