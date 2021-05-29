

Hours = int(input("Please enter the number of hours:"))
RPH = int(input("Please enter the rate per hour:"))
GrossPay = computepay(Hours,RPH)
print('Hours: 'Hours, ' GrossPay: 'GrossPay)

def computepay(Hours, RPH)
if Hours > 40:
       GrossPay = (40*RPH) + (Hours-40)*RPH*1.5
     else:
       GrossPay = Hours*RPH
       
       return Hours, Grosspay    
