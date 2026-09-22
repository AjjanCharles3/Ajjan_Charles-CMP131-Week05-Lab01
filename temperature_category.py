#Charles Ajjan
#CMP131
#Week5
#Lab4
#Temperature Category
# Date started 09/18/2026
temp=(bool(input("WELCOME PLEASE ENTER THE CURRENT TEMERATURE"   ,   )))
temp_reading= (temp)  
Cold = ("=<49")
Warm=  ("=>50-79")
Hot= ("=>80+")
print("temp", temp_reading)
if("temp_reading <49"): 
   print("Cold, Remember your Jacket")
elif ("temp_reading =>50-79"):   
   print("Warm outside")
else:
   print("Hot! Maybe stay inside")