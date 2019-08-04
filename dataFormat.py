import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


class Analitics():
	def __init__(self):
		self.data=pd.read_csv('Locus-trail-data-Jan-to-May.csv')
		self.data.drop_duplicates(keep="first",inplace=True)
	def dataInfo(self):
		self.data.head()
		self.data.describe()

	def getCordinates(self):
		return self.data['Lat'].max(),self.data['Lat'].min(),self.data['Lng'].max(),self.data['Lng'].min()

	def getTimeLimit(self):
		return self.data['Time'].max(),self.data['Time'].min()
	def getCordinateX(self):
		gometry=self.getCordinates()
		#self.data.drop_duplicates(keep="first",inplace=True)
		#data1=self.data.loc[self.data['Lat']==gometry[0]]
		print(self.data.loc[self.data['Lat']==gometry[0]])
		print(self.data.loc[self.data['Lat']==gometry[1]])
		print(self.data.loc[self.data['Lng']==gometry[2]])
		print(self.data.loc[self.data['Lng']==gometry[3]])
	def changeTimeformat(self):
		self.t =pd.to_datetime(self.data['Time'])
		self.data['Time']=((self.t- dt.datetime(1970,1,1)).dt.total_seconds()).astype(int)
		#self.data['Time']= self.data['Time'].dt.total_seconds()
		print(self.data['Time'])
	def groupingVehicle(self):
		self.data = self.data.sort_values('Time')
		self.data.groupby('User Id')
		print(self.data.head())

	def iteratingThroughGroups(self):
		self.usrIdClmn = (self.data['User Id'])
		self.usrIdClmn = self.Remove(self.usrIdClmn)
		print(self.usrIdClmn)

	def Remove(self, duplicate):
		final_list = []
		for num in duplicate:
			if num not in final_list:
				final_list.append(num)
		return final_list

	def deleteRow(self, indx):
		self.data.drop(self.data.index[indx],inplace = True)
class referenceData():
	"""docstring for NewTable"""
	def __init__(self):
		self.createFile()
	def createFile(self):
		self.refData=pd.DataFrame(columns=['Day','Node','timeStamp','direction','Velocity', 'numbrVehicle' ])
		self.refData.to_csv('referenceData.csv')
	def updateFile(self,day,node,timestmp, direction,velocty,numbrVehicle):
		self.refData.loc[len(self.refData)]= [day,node,timestmp, direction,velocty,numbrVehicle]
		self.refData.to_csv('referenceData.csv')

	def getDAta(self,day,node,timestmp,direction):
		if ((self.refData['Day']==day) & (self.refData['Node']==node) & (self.refData['timeStamp']==timestmp) & (self.refData[timeDat['direction']==direction])).any() :

		    return direc['Velocity'],direc['numbrVehicle']
		updateFile(self, day, node, timestmp, direction, 0, 0)
		return (0, 0)