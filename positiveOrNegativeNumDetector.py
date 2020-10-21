# this code detects if a number is negative, positive, or zero

import time

num = float(input("Enter a number: ")) #get input
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

print("Job finished, Console will close in three seconds")
time.sleep(3)#make sure to import time before callling this
exit()
# wait three seconds then close the console 
