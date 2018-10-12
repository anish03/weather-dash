# Weather Widget

Weather widget is a flask app that adds weather cards to your dashboard based on the name of a city. You can add multiple cities or remove them. The app fetches live weather data from [OpenWeatherMap](https://openweathermap.org/)

## API endpoints

### Register

* URL
	```/register```

* Method
	```GET``` | ```POST```

* URL Params
	None

### Account

* URL
	```/account```

* Method
	```GET``` | ```POST```

* URL Params
	None

### New Post

* URL
	```/post/new```

* Method
	```POST```

* URL Params
	None

### Post
	
* URL
	```/post/:id

* Method
	```GET```

* URL Params
	#### Required
	```id=[integer]```
