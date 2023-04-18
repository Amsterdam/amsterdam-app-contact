""" Swagger definitions """
from drf_yasg import openapi

city = openapi.Schema(type=openapi.TYPE_STRING, description='city')
directions_url = openapi.Schema(type=openapi.TYPE_STRING, description='url')
html = openapi.Schema(type=openapi.TYPE_STRING, description='html')
identifier = openapi.Schema(type=openapi.TYPE_STRING, description='identifier')
image = openapi.Schema(type=openapi.TYPE_OBJECT, description='images')
lat = openapi.Schema(type=openapi.TYPE_INTEGER, description='latitude')
lon = openapi.Schema(type=openapi.TYPE_INTEGER, description='longitude')
postal_code = openapi.Schema(type=openapi.TYPE_STRING, description='postal code (1234ab)')
queued = openapi.Schema(type=openapi.TYPE_INTEGER, description='queue length')
street_name = openapi.Schema(type=openapi.TYPE_STRING, description='street name')
street_number = openapi.Schema(type=openapi.TYPE_STRING, description='house number')
text = openapi.Schema(type=openapi.TYPE_STRING, description='text')
title = openapi.Schema(type=openapi.TYPE_STRING, description='title')
url = openapi.Schema(type=openapi.TYPE_STRING, description='url')
visiting_hours_content = openapi.Schema(type=openapi.TYPE_STRING, description='html')
waiting_time = openapi.Schema(type=openapi.TYPE_INTEGER, description='waiting time')


address = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    description='address',
    properties={
        'streetName': street_name,
        'streetNumber': street_number,
        'postalCode': postal_code,
        'city': city
    }
)

opening_hours_regular = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'city_office_id': openapi.Schema(type=openapi.TYPE_STRING, description='city office id (foreign key)'),
            'day_of_week': openapi.Schema(type=openapi.TYPE_STRING, description='day of the week (sun = 0)'),
            'opens_hours': openapi.Schema(type=openapi.TYPE_STRING, description='hours (0-23)'),
            'opens_minutes': openapi.Schema(type=openapi.TYPE_STRING, description='minutes (0-59)'),
            'closes_hours': openapi.Schema(type=openapi.TYPE_STRING, description='hours (0-23)'),
            'closes_minutes': openapi.Schema(type=openapi.TYPE_STRING, description='minutes (0-59)')
        }
    )
)


opening_hours_exceptions = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'city_office_id': openapi.Schema(type=openapi.TYPE_STRING, description='city office id (foreign key)'),
            'date': openapi.Schema(type=openapi.TYPE_STRING, description='date field (2022-12-31)'),
            'opens_hours': openapi.Schema(type=openapi.TYPE_STRING, description='hours (0-23)'),
            'opens_minutes': openapi.Schema(type=openapi.TYPE_STRING, description='minutes (0-59)'),
            'closes_hours': openapi.Schema(type=openapi.TYPE_STRING, description='hours (0-23)'),
            'closes_minutes': openapi.Schema(type=openapi.TYPE_STRING, description='minutes (0-59)')
        }
    )
)


as_city_offices = {
    'methods': ['get'],
    'responses': {
        200: openapi.Response(
            'application/json',
            openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'identifier': identifier,
                        'title': title,
                        'image': image,
                        'address': address,
                        'addressContent': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description='address info',
                            properties={
                                'html': html,
                                'title': title
                            }
                        ),
                        'coordinates': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description='address',
                            properties={
                                'lat': lat,
                                'lon': lon
                            }
                        ),
                        'directionsUrl': directions_url,
                        'appointment': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description='appointment details',
                            properties={
                                'url': url,
                                'text': text
                            }
                        ),
                        'visitingHoursContent': visiting_hours_content,
                        'visitingHours': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'regular': opening_hours_regular,
                                    'exceptions': opening_hours_exceptions
                                }
                            )
                        ),
                        'order': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='order of city offices'
                        )
                    }
                )
            ),
            examples={'application/json': {'status': True, 'result': {}}}
        )
    },
    'tags': ['City']
}


as_waiting_times = {
    'methods': ['get'],
    'responses': {
        200: openapi.Response(
            'application/json',
            openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'identifier': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='identifier'
                        ),
                        'queued': queued,
                        'waitingTime': waiting_time
                    }
                )
            ),
            examples={'application/json': {'status': True, 'result': {}}}
        )
    },
    'tags': ['City']
}
