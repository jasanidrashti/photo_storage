from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.photo_upload_view, name = 'image_upload'),
    path('success', views.success, name = 'success'),
    path('show', views.get_all_photos),
    path('delete', views.delete_photo),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)