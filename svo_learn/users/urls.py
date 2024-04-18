from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'md_employes/',
        views.md_employes,
        name='md_employes'
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
