from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
def home(request):
    return HttpResponse("Welcome to School CRM Backend!")

urlpatterns = [
    path('', home, name='home'),   # ✅ root path
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('students.urls')),
    path('api/', include('classrooms.urls')),
    path('api/', include('attendance.urls')),
    path('api/', include('teachers.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
