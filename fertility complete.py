'''
A data set of 100 participates in a seminal fertility analysis taking into consideration some of the participants life styles and determining the contributing factor which affects the validity of the seminal fluid
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fert=pd.read_csv('fertility_Diagnosis.txt')
cols = ['Season','Age','Childish disease','Accident or trauma','Surgical int','High fevers in last years','freq of alcohol cons.','Smoking_habit','No of hours spent sitting per day','Output']
fert.columns = cols
#percentage of normal to altered
normal=fert[(fert['Output']=='N')]
pri=len(normal)
d=fert['Output']
dd=len(d)
per=(pri/dd)*100
print('Percentage of Normal seminal fluid to altered seminal fluid\n',per,'%')

#Age distribution of participants
rati=fert.groupby('Age').Output.size()
plt.plot(rati)
plt.title('Age distribution of participant')
plt.xlabel('Age')
plt.ylabel('Population')
plt.savefig('age dist.png',format='png')
plt.show()

#smoking chart
agee=fert.groupby('Smoking_habit').size()
plt.pie(agee)
plt.title('Ration of those that has a smoking habit')
plt.legend(['never','occasional','daily'])
plt.show()

#Hours spent sitting down
hours=fert.groupby('No of hours spent sitting per day').size()
plt.plot(hours)
plt.title('No of hours which the participant sit per day')
plt.xlabel('Hours')
plt.ylabel('Population')
plt.savefig('hours.png',format='png')
plt.show()

#Seasons
sea=fert.groupby('Season').size()
plt.pie(sea)
plt.title('Seasons in which analysis is taken ')
plt.legend(['winter','spring','summer','fall'])
plt.savefig('season.png',format='png')
plt.show()

#Deciding which of the factors affect the output of the seminal fertility the most
'Season','Age','Childish disease','Accident or trauma','Surgical int','High fevers in last years','freq of alcohol cons.','Smoking_habit','No of hours spent sitting per day','Output''''
'''

season=fert.groupby(['Season','Output']).size()
print('Season factor\n',season)

age=fert.groupby(['Age','Output']).size()
print('\nAge factor\n',age)
children=fert.groupby(['Childish disease','Output']).size()
print('\nInformation of those with childish diseases\n',children)
accident=fert.groupby(['Accident or trauma','Output']).size()
print('\nThose that have had a traumatic experience or are involved in an accident\n',accident)
surgical=fert.groupby(['Surgical int','Output']).size()
print('\nThose that have been subject to a surgical operation \n',surgical)
fever=fert.groupby(['High fevers in last years','Output']).size()
print('\nDistribution of those with fevers in last years\n',fever)
freq_alcohol=fert.groupby(['freq of alcohol cons.','Output']).size()
print('\nThe alcohol consumers\n',freq_alcohol)
habit=fert.groupby(['Smoking_habit','Output']).size()
print('\nSmokers\n',habit)
sitting=fert.groupby(['No of hours spent sitting per day','Output']).size()
print('\nHigh hours of sitting in a day',sitting)

#The affecting factors of output

h=fert.groupby('Output')
g=h.get_group('O')
print('Altered seminal fluids\n',g)
j=g['Season']
print('Season\n',j)
k=g['No of hours spent sitting per day']
print('\nHours spent sittin\n',k)
l=g['Childish disease']
print('\nDisease\n',l)
m=g['High fevers in last years']
print('\nFevers\n',m)
n=g['Surgical int']
print('\nSurgery\n',n)
o=g['Accident or trauma']
print('\nAccident\n',o)
p=g['Age']
print('\nAge\n',p)
q=g['freq of alcohol cons.']
print('\nAlcohol\n',q)
r=g['Smoking_habit']
print('\nSmoking\n',r)
