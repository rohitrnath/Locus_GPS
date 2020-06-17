# **LOCUS MAPS!**

**Objective of the idea**** :**

**Locus Maps is an approach on creating an onground movement for logistics companies. It is also optimized to provide the time taken to cover the distance from the starting point to the end point.**

**Problem addressed**** :**

Below are the listed potential benefits of the **GoTo** System:

1. Uses LOTR GPS data to build an equivalent of google maps.
2. It also provides the most appropriate time taken to cover the distance from the starting point to the end point.

**Current Challenges:**

1. Use of OSRM to create a path same as that of google maps.
2. Fitting GPS data to the OSRM data.
3. Predict time taken navigating between two locations.

**LocusMaps – Integration of OSRM and GPS**** :**

![](RackMultipart20200617-4-j5mdt4_html_f68c38c14c32eee4.jpg)

![](RackMultipart20200617-4-j5mdt4_html_b30984bdcfc45cbb.jpg)

**Proposed Idea Description**** :**

The training consist of two kinds of classification:

Classification based on vehicle ID for clean GPS train data

After classify, find the distance to nodes using euclidian distance or will find the direction of moving using bayes theorem

Clear all co-ordinates in out of threshold.

Classification based on timestamp(in day and time).

find the average velocity of node with number of vehicle passing

in defenite time.

Updating the classification table.

3. Doing logical regression based on velocity and timestamp.

In testing we will take both starting and ending co-ordinaes

1. Find all route nodes array
2. Find all nodes time stamp
3. Finding the route with least estimated time stamp plot in the map with all heatmap data.

**Picture of Surjapur plotted in python with node points**** :**

![](RackMultipart20200617-4-j5mdt4_html_763222e2b8d5bfa8.png)
