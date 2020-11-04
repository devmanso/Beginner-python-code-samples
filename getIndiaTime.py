from datetime import *
import pytz 
  
  
tz_INDIA = pytz.timezone('Asia/Kolkata')  
datetime_INDIA = datetime.now(tz_INDIA) 
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))

#output:
# INDIA time: 19:29:53
