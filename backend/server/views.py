from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from server.models import ParkingFacility
from server.serializers import ParkingFacilitySerializer
from django.db.models import Q
from datetime import datetime

from geopy.distance import geodesic

# Create your views here.
# request -> response

def say_hello(request) :
    return HttpResponse('Hello World')


# List all facilities
@csrf_exempt
def parking_facility_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # Initialize an empty Q object
        filter_conditions = Q()
        # params that might come from request
        time_param = request.GET.get('time', None)
        price_min_param = request.GET.get('price_min', None)
        price_max_param = request.GET.get('price_max', None)
        long_param = request.GET.get('long', None)
        lat_param = request.GET.get('lat', None)
        distance_limit_param = request.GET.get('distance', None)

        # add optional conditions to Q object
        if time_param:
            time_param = datetime.strptime(time_param + ':00', '%H:%M:%S').time()
            filter_conditions &= Q(open_hours__lte=time_param, close_hours__gte=time_param)
        if price_min_param:
            filter_conditions &= Q(price_per_hour__gte=price_min_param)
        if price_max_param:
            filter_conditions &= Q(price_per_hour__lte=price_max_param)

        # facilities = ParkingFacility.objects.all()

        # apply dynamic filter_conditions to queryset
        facilities = ParkingFacility.objects.filter(filter_conditions)
        if long_param and lat_param and distance_limit_param:
            facilities = [facility for facility in facilities
                          if distance(long_param, lat_param, facility.long, facility.lat) <= float(distance_limit_param)]
            # facilities = (ParkingFacility.objects.annotate(distance=Distance('location', user_location))
            #               .filter(distance__lte=distance_limit_param))

        serializer = ParkingFacilitySerializer(facilities, many=True)

        print(f"Get {len(facilities)} data in total")

        return JsonResponse(serializer.data, safe=False)

def distance(long1, lat1, long2, lat2):
    point1 = (lat1, long1)
    point2 = (lat2, long2)
    return geodesic(point1, point2).miles