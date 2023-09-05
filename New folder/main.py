import phonenumbers
from phone import number
# for country code ->
from phonenumbers import geocoder
from phonenumbers import carrier
# for location ->
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

pepnum = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnum,'en')
# print(location)
service_pro = phonenumbers.parse(number)
cpro = carrier.name_for_number(service_pro,'en')
# print(cpro)

api_key = '03b0004635b248d6af1339ad64fcb361'
geocoders = OpenCageGeocode(api_key)
query = str(location)
results = geocoders.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(my_map)
my_map.save('das_location.html')

