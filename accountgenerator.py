import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid
import string
import names






def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for i in range(size))




def generate_random_time(month):
  day = generate_random_day(month)
  if random.random() < 0.5:
    date = datetime.datetime(2021, month, day,10,00)
  else:
    date = datetime.datetime(2021, month, day,16,00)
  time_offset = numpy.random.normal(loc=0.0, scale=180)
  final_date = date + datetime.timedelta(minutes=time_offset)
  return final_date

def generate_random_day(month):
  day_range = calendar.monthrange(2021,month)[1]
  return random.randint(1,day_range)







columns = ['ID', 'RecDate', 'SysDate', 'firstName' , 'lastName' ,'userName']

df = pd.DataFrame(columns=columns)

for i in range (10):

	a= generate_random_time(6)
	SysDate=a.strftime("%m/%d/%y %H:%M") 
	RecDate = a.strftime("%m/%d/%y")
	
	ID=id_generator()
	firstName= names.get_first_name()
	lastName= names.get_last_name()
	userName = firstName + lastName
	df.loc[i] = [ID, RecDate, SysDate, firstName, lastName, userName]

df.to_csv('test_data.csv')