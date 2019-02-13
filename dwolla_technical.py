import urllib, json


def main():
	user_input = raw_input("Enter the city: ")  




	API_KEY = "3642eae414529c2d868690848fa0fd81"
	url = "https://api.openweathermap.org/data/2.5/weather?q="

	url = url + user_input + "&appid=" + API_KEY

	try:
	    response = urllib.urlopen(url)
	except urllib.error.HTTPError as e:
	    print('The server couldn\'t fulfill the request.')
	    print('Error code: ', e.code)
	except urllib.error.URLError as e:
	    print('We failed to reach a server.')
	    print('Reason: ', e.reason)
	else:
		data = json.loads(response.read())
		if data['cod'] != 200:
			# print data
			print(data['message'])
			return data['message']
		degree = ((data['main']['temp'] -273.15)* 5 /9) + 32
		print(user_input + " temprature is " + str(degree) + " fahrenheit")
		return user_input + " temprature is " + str(degree) + " fahrenheit"

if __name__ == '__main__':
	main()
