
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('menu',views.menuView, name='menu'),
    path('about',views.aboutView, name='about'),
    path('book',views.bookTableView, name='book'),
    path('feedback',views.feedback, name='feedback'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
