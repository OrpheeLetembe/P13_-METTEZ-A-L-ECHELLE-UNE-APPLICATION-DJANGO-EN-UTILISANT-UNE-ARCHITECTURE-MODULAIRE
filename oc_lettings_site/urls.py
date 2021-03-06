from django.contrib import admin
from django.urls import path, include

from .views import index


# test sentry function
def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    # test sentry url app
    path('sentry-debug/', trigger_error),

]
