# Weather Dash

Weather dash is a flask app that adds weather cards to your dashboard based on the name of a city. You can add multiple cities or remove them. The app fetches live weather data from [OpenWeatherMap](https://openweathermap.org/)


<p>
	<img width="700" height="700" src="https://github.com/anish03/weather-widget/blob/master/Images/Screenshot.png">
</p>

## How to use

### Clone Repository
```
git clone https://github.com/anish03/weather-widget.git
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run on localhost
```
cd src/
flask run
```

## API endpoints

### Register

* URL:
	```/register```

* Method:
	```GET``` | ```POST```

* URL Params:
	None

### Account

* URL:
	```/account```

* Method:
	```GET``` | ```POST```

* URL Params:
	None

### New Post

* URL:
	```/post/new```

* Method:
	```POST```

* URL Params:
	None

### Post
	
* URL:
	```/post/:id```

* Method:
	```GET```

* URL Params:
	#### Required
	```id=[integer]```

