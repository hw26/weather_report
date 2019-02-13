import urllib, json, sys


def main():
	user_input = raw_input("Enter the city: ")  




	API_KEY = "3642eae414529c2d868690848fa0fd81"
	url = "https://api.openweathermap.org/data/2.5/weather?q="

	url = url + user_input + "&appid=" + API_KEY

	try:
	    response = urllib.urlopen(url)
	except urllib.error.HTTPError as e:
	    sys.stdout.write('The server couldn\'t fulfill the request.')
	    sys.stdout.write('Error code: ', e.code)
	except urllib.error.URLError as e:
	    sys.stdout.write('We failed to reach a server.')
	    sys.stdout.write('Reason: ', e.reason)
	else:
		data = json.loads(response.read())
		if data['cod'] != 200:
			sys.stdout.write(data['message'])
			return
		degree = round((data['main']['temp'] -273.15)* 5 /9) + 32
		sys.stdout.write(user_input + " temprature is " + str(degree) + " fahrenheit")

if __name__ == '__main__':
	main()
