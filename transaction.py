import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid
import string
import names
import csv


data=[]
with open ("test_data.csv") as csvfile:
	reader= csv.reader(csvfile)
	for row in reader:
		data.append(row)


def ranID():
	
	db_length = len(data)
	
	rand_name= random.randint(1,db_length-1)
	chosen_name=data[rand_name][1]
	return rand_name

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




columns = ['ID', 'Username', 'FundDate', 'factorPnt' , 'fundedAmount' ,'paybackAmount','dailyPmtCnt','collDailyAmt']

df = pd.DataFrame(columns=columns)


for i in range (20):
	a=ranID()
	ID=data[a][1]
	Username=data[a][6]
	b= generate_random_time(6)
	FundDate=b.strftime("%m/%d/%y %H:%M") 
	fundedAmount=random.uniform(0,10000)
	paybackAmount=fundedAmount*1.35
	collDailyAmt=paybackAmount/100


	df.loc[i] = [ID, Username, FundDate, 1.35, fundedAmount, paybackAmount,100,collDailyAmt]



df.to_csv('transaction_data.csv')