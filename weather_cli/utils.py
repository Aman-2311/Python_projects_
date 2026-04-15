import requests # Import requests to make HTTP calls
from config import API_KEY,BASE_URL  #acessing api using config

#creating function

def get_weatherz(city):
    params ={
        "q":city,
        "appid":API_KEY,
        "units":'metric'
    }
#error handling
    try:
        response =requests.get(BASE_URL,params=params)
        #if not 200
        response.raise_for_status()
        #convert data to json
        data =response.json()
        result= {
            'city':data['city'],
            'temp':data['main']['temp'],
            'humidity':data['main']['humidity'],
            'condition':data['weather'][0]['description']
        }
        return result

    #handle https error
    except requests.exceptions.HTTPError:
        return {"error":"City not found or API error"}

    #network error handle

    except requests.exceptions.RequestException:
        return{"error":"Network error"}


