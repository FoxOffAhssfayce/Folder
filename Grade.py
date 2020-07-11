#score check If the score is out of range, print error 
#score must between 0.0 and 1.0
score= float(input("Enter score bewteen 0.0 and 1.0"))
if score < .6 and score >= .0:
    print("F")
elif score >=.6 and score <=.69:
    print ("D")
elif score >=.7 and score <=.79:
    print ("C")
elif score >=.8 and score <=.89:
    print ("B")
elif score >=.9 and score <= 1.0:
    print ("A")
else:
    print ("Error")
