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
with open ("transaction_data.csv") as csvfile:
	reader= csv.reader(csvfile)
	for row in reader:
		data.append(row)



db_length = len(data)



def pvcalculator (x):

	discRate=0.0025
	numberofBusinesDay=262
	paymentAmount=100

	s = x
	ii, dd = divmod(s, 1)


	iii=int(ii)

	sum1=0
	for i in range (iii):
	    
	    sum1=sum1+paymentAmount/(1+(discRate/numberofBusinesDay))**(i+1)
	    

	sum1=sum1+ (dd*paymentAmount)/(1+(discRate/numberofBusinesDay))**(iii+2)

	return (sum1)






columns = ['ID', 'Username', 'FundDate', 'factorPnt' , 'fundedAmount' ,'paybackAmount','dailyPmtCnt','collDailyAmt','PVsum']

df = pd.DataFrame(columns=columns)

for i in range (db_length-1):

	ID=data[i+1][1]
	Username=data[i+1][2]
	FundDate=data[i+1][3]
	factorPnt=data[i+1][4]
	fundedAmount=data[i+1][5]
	paybackAmount=data[i+1][6]
	dailyPmtCnt=data[i+1][7]
	collDailyAmt=data[i+1][8]
	x=float(collDailyAmt)
	PVsum=pvcalculator(x)

	df.loc[i] = [ID, Username, FundDate, 1.35, fundedAmount, paybackAmount,100,collDailyAmt,PVsum]



df.to_csv('dcf.csv')