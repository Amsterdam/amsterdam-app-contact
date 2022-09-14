from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from amsterdam_app_api.views import views_city


schema_view = get_schema_view(
    openapi.Info(
        title="Amsterdam APP Module: CityOffices",
        default_version='v1',
        description="API backend server for: CityOffices"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

""" Base path: /api/v1
"""

urlpatterns = [
   # Swagger (drf-yasg framework)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^apidocs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # City information (contact, counters)
    path('city-offices', csrf_exempt(views_city.city_offices)),
    path('waiting-times', csrf_exempt(views_city.waiting_times)),

]
