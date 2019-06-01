'''from datetime import datetime
dt_now = datetime.now()
print( dt_now.strftime("%Y-%m-%d-%H.%M.%S") )


from datetime import datetime, timedelta
dt_yesterday = datetime.now() - timedelta(days=1)
print( dt_yesterday.strftime("%Y-%m-%d-%H.%M.%S") )


import datetime 
import dateutil.relativedelta
now = datetime.datetime.now()
print now + dateutil.relativedelta.relativedelta(months=-1)'''


from datetime import datetime
datetime_object = datetime.strptime("01/01/17 12:10:03.234567", '%d/%m/%y %H:%M:%S.%f')
print(datetime_object)