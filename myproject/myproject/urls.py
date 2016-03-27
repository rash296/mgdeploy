

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,patterns, url
from django.contrib import admin


urlpatterns = [
	url(r'^$', 'webapp.views.home', name='home'),
	url(r'^contact/$', 'webapp.views.contact', name='contact'),
	url(r'^about/$', 'webapp.views.about', name='about'),
	url(r'^achievement/$', 'webapp.views.achievement', name='achievement'),
    url(r'^admin/', admin.site.urls),
    url(r'^list/$', 'webapp.views.list', name='list'),
    #url(r'^att/$','webapp.views.att',name='att'),
    url(r'^test/$', 'webapp.views.test', name='test'),
    url(r'^attendance/$', 'webapp.views.attendance', name='attendance'),
    url(r'^query/$', 'webapp.views.query', name='query'),
    url(r'^notify/$', 'webapp.views.notify', name='notify'),
     url(r'^profile/$', 'webapp.views.profile', name='profile'),
]
   

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
