""" Django views file for city offices api """
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from amsterdam_app_api.api_messages import Messages
from amsterdam_app_api.models import CityOffices
from amsterdam_app_api.models import CityOfficesOpeningHoursRegular, CityOfficesOpeningHoursExceptions
from amsterdam_app_api.swagger.swagger_views_city_offices import as_city_offices, as_waiting_times
from amsterdam_app_api.GenericFunctions.StaticData import StaticData
from amsterdam_app_api.GenericFunctions.Sort import Sort


messages = Messages()


def get_opening_hours(identifier):
    """ Get opening hours """
    regular = [
        {
            'dayOfWeek': x.day_of_week,
            'opening': {'hours': x.opens_hours, 'minutes': x.opens_minutes},
            'closing': {'hours': x.closes_hours, 'minutes': x.closes_minutes}
        }
        for x in list(CityOfficesOpeningHoursRegular.objects.filter(city_office_id=identifier).all())
    ]
    exceptions = [
        {
            'date': x.date,
            'opening': {'hours': x.opens_hours, 'minutes': x.opens_minutes},
            'closing': {'hours': x.closes_hours, 'minutes': x.closes_minutes}
        }
        if x.opens_hours is not None else {'date': x.date}
        for x in list(CityOfficesOpeningHoursExceptions.objects.filter(city_office_id=identifier).all())
    ]
    return {'regular': regular, 'exceptions': exceptions}


@swagger_auto_schema(**as_city_offices)
@api_view(['GET'])
def city_offices(request):
    """ City offices api """
    offices = list(CityOffices.objects.all())
    data = []
    for office in offices:
        opening_hours = get_opening_hours(office.identifier)
        city_office = {
            'identifier': office.identifier,
            'title': office.title,
            'image': office.images,
            'address': {
                'streetName': office.street_name,
                'streetNumber': office.street_number,
                'postalCode': office.postal_code,
                'city': office.city
            },
            'addressContent': office.address_content,
            'coordinates': {
                'lat': office.lat,
                'lon': office.lon
            },
            'directionsUrl': office.directions_url,
            'appointment': office.appointment,
            'visitingHoursContent': office.visiting_hours_content,
            'visitingHours': opening_hours,
            'order': office.order
        }
        data.append(city_office)

    sort = Sort()
    result = sort.list_of_dicts(data, key='order', sort_order='asc')
    return Response({'status': True, 'result': result})


@swagger_auto_schema(**as_waiting_times)
@api_view(['GET'])
def waiting_times(request):
    """ waiting time api """
    lookup_table = StaticData.city_office_waiting_times_lookup_table()
    urls = StaticData.urls()
    url = urls['waiting_times']
    city_offices_waiting_times = requests.get(url, timeout=3).json()
    result = []
    try:
        for i in range(0, len(city_offices_waiting_times)):
            identifier = lookup_table[str(city_offices_waiting_times[i]['id'])]
            data = CityOffices.objects.filter(identifier=identifier).values('identifier').first()
            waiting_time_str = city_offices_waiting_times[i]['waittime']

            try:
                if waiting_time_str.lower() == 'meer dan een uur':
                    waiting_time = 60
                elif waiting_time_str.lower() == 'geen':
                    waiting_time = 0
                else:
                    waiting_time = int(waiting_time_str.split(' ')[0])
            except Exception:
                waiting_time = None

            result.append({
                'identifier': data['identifier'],
                'queued': city_offices_waiting_times[i]['waiting'],
                'waitingTime': waiting_time
            })
    except Exception:
        pass
    return Response({'status': True, 'result': result})
