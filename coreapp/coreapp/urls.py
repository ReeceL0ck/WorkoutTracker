from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

admin.site.site_header = "WorkoutTracker Admin"
admin.site.site_title = "WorkoutTracker Admin Portal"
admin.site.index_title = "Welcome to WorkoutTracker Portal"


urlpatterns = [
    path('U2FsdGVkX1ctHhTkRbj69RCkG9F7vA9Mbl5qOvnm2Y/', admin.site.urls),
    path("tracker/", include("tracker.urls"), name="home"),
    path('', include("user_login.urls")),
    # path('', RedirectView.as_view(url='tracker/')),

]