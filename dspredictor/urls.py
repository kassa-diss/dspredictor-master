from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#connecting seperated apps urls into main path
urlpatterns = [

    path('', include('webfront.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('predictions/', include('predictions.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
