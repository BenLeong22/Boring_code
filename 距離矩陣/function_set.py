# coding=utf8
import requests
import json
import urllib
import urllib.request
import googlemaps

def osmr(origin_longitude,origin_latitude,destination_longitude,destination_latitude):
    r = requests.get(f"http://localhost:5000/route/v1/foot/"+str(origin_longitude)+","+str(origin_latitude)+";"+str(destination_longitude)+","+str(destination_latitude)+"?overview=false")
    results = json.loads(r.content)
    distance=100000000
    duration=100000000
    if(results.get("code") == "Ok"):
        legs = results.get("routes").pop(0).get("legs")
        distance = legs[0].get("distance")
        duration = legs[0].get("duration")
    return {"distance":distance,"duration":duration}

def google(origin_longitude,origin_latitude,destination_longitude,destination_latitude):
    gmaps = googlemaps.Client(key='AIzaSyCvJTbnzdh7y_Fy9iPuwSa3HagvcfBbSpw')
    my_dist = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)],
                                    [str(destination_latitude) + " " + str(destination_longitude)], mode='transit')
    check = my_dist.get("rows")[0].get("elements")[0].get("status")
    distance=100000000
    duration=100000000
    if check == 'OK':
        distance = my_dist.get("rows")[0].get("elements")[0].get("distance").get("value")
        duration = my_dist.get("rows")[0].get("elements")[0].get("duration").get("value")
    return {"distance":distance,"duration":duration}