import requests

def my_function():
  val = input("Enter your value: ")

  response = requests.get("http://ip-api.com/json/" + val).json() ##49.145.77.165

  print("Country: " + response['country'])
  print("Country Code: " + response['countryCode'])
  print("Region: " + response['region'])
  print("Region Name: " + response['regionName'])
  print("City: " + response['city'])
  print("Zip Code: " + response['zip'])
  print("Timezone: " + response['timezone'])
  print("ISP: " + response['isp'])
  print("Company: " + response['org'])
  print("ASP: " + response['as'])
  print("Latitude: " + str(response['lat']))
  print("Longitude: " + str(response['lon']))

user_input = ''
my_function()

while True:
    user_input = input('Do you want to continue? yes/no: ')

    if user_input.lower() == 'yes':
        my_function()
        continue
    elif user_input.lower() == 'no':
        print('Thank you for using our app!')
        break
    else:
        print('Type yes/no')
        