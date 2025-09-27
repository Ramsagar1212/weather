# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .utils import get_weather_data
# from .serializers import WeatherSerializer


# @api_view(['GET'])
# def weatherview(request):
#     city = request.query_params.get('city','London')
#     data = get_weather_data(city)
    
    
#     if data.get('cod') != 200:
#         return Response({'status':400, 'error':data.get('message', 'Invalid City')})
    
    
#     weather_info = {
#         "city" : data["name"],
#         "temperature": data["main"]["temp"],
#         "description": data["weather"][0]["description"],
#         "icon": data["weather"][0]["icon"],
#     }
    
#     serializer = WeatherSerializer(weather_info)
#     return Response(serializer.data)



from django.shortcuts import render
from .utils import get_weather_data

def weather_page(request):
    city = request.GET.get('city')
    weather = None
    error = None

    if city:
        data = get_weather_data(city)
        if data.get("cod") != 200:
            error = data.get("message", "Invalid city")
        else:
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
            }

    return render(request, "weather.html", {"weather": weather, "error": error})
