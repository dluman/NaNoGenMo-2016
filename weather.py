import yaml

class Forecast:
	def __init__(self,data):
		self.high = data['data'][0]['Max TemperatureF']
		self.low = data['data'][2]['Min TemperatureF']
		self.humidity = data['data'][7]['Mean Humidity']
		self.visibility = data['data'][13]['Mean VisibilityMiles']
		self.windspeed = data['data'][16]['Mean Wind SpeedMPH']
		self.gustspeed = data['data'][17]['Max Gust SpeedMPH']
		self.precipitation = data['data'][18]['PrecipitationIn']
		self.cloudcover = data['data'][19]['PCloudCover']
		self.event = data['data'][20]['Events']

def getForecast(date):
	with open('yaml/sphreak-weather.yaml','r') as climate:
		weather = yaml.load(climate)
	for data in weather:
		if str(data['EST'])==str(date):
			report = Forecast(data)
	return report	

#DATA FORMAT
#
#EST: 1985-11-1
#  data:
#0   - Max TemperatureF: 61
#1  - Mean TemperatureF: 52
#2   - Min TemperatureF: 42
#3   - Max Dew PointF: 42
#4   - MeanDew PointF: 35
#5   - Min DewpointF: 24
#6   - Max Humidity: 79
#7   - Mean Humidity: 55
#8   - Min Humidity: 24
#9   - Max Sea Level PressureIn: 30.15
#10   - Mean Sea Level PressureIn: 30.07
#11   - Min Sea Level PressureIn: 29.99
#12   - Max VisibilityMiles: 20
#13   - Mean VisibilityMiles: 14
#14   - Min VisibilityMiles: 10
#15   - Max Wind SpeedMPH: 17
#16   - Mean Wind SpeedMPH: 13
#17   - Max Gust SpeedMPH: 
#18   - PrecipitationIn: 0.00
#19   - PCloudCover: 4
#20   - Events: 
#21   - WindDirDegrees: 51
