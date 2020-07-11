#pay me 
#rate is 10.5 
#time and half is 1.5

hours = float(input("Enter Hours"))
rate = float(input ("Enter Rate"))
pay = hours * rate
payover = (((hours-40) * (rate*1.5))+ (rate * (40)))
   
if hours <= 40:
      
        print("Pay: "+ str(pay) )
else:
		print("Pay: "+ str(payover) )
