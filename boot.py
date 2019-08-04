import networkx as nx
import osmnx as ox
from dataFormat import *
#import numpy as np
import requests
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

#df = pd.DataFrame(index=range(0,4),columns=['A'], dtype='float')

#AVG SPEED IN BANGALORE
AVG_SPEED = 50;
VELO_THRESH = 5;

Data = Analitics()
refer = referenceData()

def haversine(lat1, lng1, lat2, lng2):
    dist = ox.great_circle_vec(lat1, lng1, lat2, lng2, earth_radius=6371009)
    return dist

def clearGPS(raw):
    # THREASHOLD DISTANCE
    FILTER_THRESHOLD = 100.0;

    # get the nearest network node to each point
    good_orig_node = ox.get_nearest_node(G2, (raw["Lat"], raw["Lng"]), method='haversine', return_dist=True)
    if(good_orig_node[1] > FILTER_THRESHOLD) :
        ret = -1
    else:
        ret = good_orig_node[0]
    return ret



def velocityVeh(lat1,lng1,lat2, lng2, timeStamp1,timeStamp2):
    dist = haversine(lat1,lng1,lat2, lng2)
    if timeStamp2 != timeStamp1:
        velocity = dist/(timeStamp2-timeStamp1)
    else: velocity = 0
    return velocity

def avgVelocity(avgVel, currVelo, count):
    avgVel = avgVel + ((currVelo-avgVel)/(count+1))
    return avgVel

def findDay(timeStamp):
    day = (timeStamp//86400)%7
    return(day)

#get the nearest network node to each point
# print("rohit")
# good_orig_node = ox.get_nearest_node(G2, (12.9100389, 77.6876632), method='haversine',return_dist=True)
# #good_orig_node = list(good_orig_node)
# print(good_orig_node)
# #bad_orig_node = ox.get_nearest_node(G2, (25.071764, 55.138978), method='euclidean')
# dest_node = ox.get_nearest_node(G2, (12.906579, 77.6906155), method='haversine',return_dist=True)
# #dest_node = list(dest_node)
# print(dest_node)
#
#
# # find the route between these nodes then plot it
# route = nx.shortest_path(G2, good_orig_node[0], dest_node[0], weight='length')
# # fig, ax = ox.plot_graph_route(G2, route, fig_height=10, fig_width=10)
# print(route)
#
# # find the route between these nodes then plot it
# print(route)


bN,bS,bE,bW = map(float,Data.getCordinates())
print(bN,bS,bE,bW)

ox.config(use_cache=True, log_console=True)
ox.__version__
# get a graph for some city
SMALL_MARINA = [ bN, bS, bE, bW]
G2 = ox.graph_from_bbox(
    *SMALL_MARINA,
    simplify=False,
    retain_all=True,
    network_type='drive',
)
print("R_SQUAD::: loaded map data and all nodes")
# fig2, ax2 = ox.plot_graph(G2, fig_height=10, fig_width=10)
Data.changeTimeformat()
minTime, maxTime = map(int,Data.getTimeLimit())
Data.groupingVehicle()
print(Data.data.head())
print(Data.data.describe())


Data.data['node'] = Data.data.apply(clearGPS, axis = 1)

print(Data.data.head())
print(Data.data)


#Data.data = Data.data[~Data.data['node'].isin([-1])]

Data.iteratingThroughGroups()
lastPath = Data.usrIdClmn[0]

prevLat = 0
prevLon = 0
prevNode =0
prevTimestamp =0
prevVelo =0
prevDay =0
prevTime =0

zeroFlag =0
zeroPrevLat =0
zeroPrevLon =0
zeroPrevNod =0
zeroPrevVelo =0
zeroTimestamp =0

velocity =0
dir =0

for index, row in Data.data.iterrows():
    print(index, row['node'])
    presentPath = row['User Id']
    day = (row['Time']// 86400) - (minTime // 86400)
    dayRem = (row['Time']) % 86400
    timeStamp = row['Time']%1800
    if(row['node']!= -1):
        if(index == 0 or lastPath != presentPath):

            refer.updateFile(day, row['node'], timeStamp, 1, 0,1,)

        else:

            if row['node'] >= prevNode :
                dir = 1
            else:
                dir =0

            avgVel,vn = refer.getDAta(day, row['node'], timeStamp, dir)
            velocity = velocityVeh(prevLat,  prevLon,row['Lat'], row['Lng'],prevTimestamp, row['Time'])


            if (vn !=0).all:
                AvgVEL = avgVelocity(avgVel, velocity, vn)
            else:
                AvgVEL = velocity

            refer.updateFile(day, row['node'], timeStamp, dir, AvgVEL, vn+1)

        prevLat = row['Lat']
        prevTimestamp = row['Time']
        prevLon = row['Lng']
        prevNode = row["node"]
        prevVelo = velocity
        lastPath = presentPath

print(refer.refData.head())