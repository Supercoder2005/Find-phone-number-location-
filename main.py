import phonenumbers 
import opencage 
import folium 
from myphoneno import number 
from phonenumbers import geocoder 

pepnumber = phonenumbers.parse(number) 
location = geocoder.description_for_number(pepnumber,"en") 
print("The phone number is from the country :",location) 

from phonenumbers import carrier 
service_pro = phonenumbers.parse(number) 
print("The service provider for this phone number is :",carrier.name_for_number(service_pro,"en")) 

from opencage.geocoder import OpenCageGeocode 
key = "7227db11613042a29c3bb63b4d658acd" 
geocoder = OpenCageGeocode(key) 
query = str(location) 
results = geocoder.geocode(query) 
lat = results[0]['geometry']['lat'] 
lng = results[0]['geometry']['lng'] 
print("Latitude :",lat,", Longitude :",lng) 

myMap = folium.Map(location = [lat,lng],zoom_start = 13) 
folium.Marker([lat,lng],popup=location).add_to(myMap) 

myMap.save("mylocation.html") 