from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup$', views.signup , name='signup'),
    url(r'^comments/$',views.save_comment, name='comment'),
    url(r'^profile/$',views.profile_index, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
