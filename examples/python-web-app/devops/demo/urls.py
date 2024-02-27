from django.urls import path, include

urlpatterns = [
    path('', include('demo.urls')),  # Add this line for the root path
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),
]
