from django.contrib import admin
from django.urls import path
from . import views as main_views
from lettings import views as lettings_views
from profiles import views as profiles_views
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

handler404 = main_views.handle_404
handler500 = main_views.handle_500

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', main_views.index, name='index'),
    path('get_500/', main_views.get_500, name='get_500'),
    path('lettings/', lettings_views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings_views.letting, name='letting'),
    path('profiles/', profiles_views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
