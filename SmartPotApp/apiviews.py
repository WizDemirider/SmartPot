from django.http import HttpResponse
from rest_framework import generics, status
from .models import AppUser, History
import os

class PostData(generics.GenericAPIView):
    # permission_classes = (AllowAny,)

    def post(self, request, uid):
        try:
            user = AppUser.objects.get(id=uid)
        except AppUser.DoesNotExist:
            return HttpResponse("User not found. Check the token sent.", status=status.HTTP_400_BAD_REQUEST)

        new_data = History(user=user)

        recv_data = request.body.decode()
        try:
            # moisture, temperature, humidity = [float(val) for val in recv_data.split('&')]
            moisture, temperature = [float(val) for val in recv_data.split('&')]
            new_data.moisture = moisture
            new_data.temperature = temperature
            # new_data.humidity = humidity
            new_data.save()
        except Exception:
            return HttpResponse("Data format is wrong, expected moisture, temperature, humidity separated by &.", status=status.HTTP_400_BAD_REQUEST)

        timestamp = new_data.timestamp
        data_resp = timestamp.strftime('%d/%m/%y')+'&'+timestamp.strftime('%I:%M %p')+'&'+str(user.moisture_preference)
        
        if 'DEBUG' in os.environ and os.environ['DEBUG']:
            print(data_resp)

        return HttpResponse(data_resp)