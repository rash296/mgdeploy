

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,patterns, url
from django.contrib import admin


urlpatterns = [
	url(r'^$', 'webapp.views.home', name='home'),

    url(r'^home/$', 'webapp.views.home', name='home'),
    #url(r'^login/$','webapp.views.login_user'),
	url(r'^contact/$', 'webapp.views.contact', name='contact'),
    url(r'^base/$', 'webapp.views.base', name='base'),
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

    url(r'^log/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'webapp.views.logout_page',name="logout"),
    #url(r'^login/$', 'webapp.contrib.auth.views.login''webapp.views.user',name="login"), # If user is not login it will redirect to login page  
    url(r'^register/$', 'webapp.views.register',name="register"),
    url(r'^register/success/$', 'webapp.views.register_success',name="success"),
    url(r'^logged_in/$', 'webapp.views.user',name="is_in_multiple_groups"),
    url(r'^loginhome/$', 'webapp.views.loginhome',name="loginhome"),
    url(r'^student_data/$', 'webapp.views.student_data'),
    url(r'^parent_data/$', 'webapp.views.parent_data'),
    url(r'^chart/$', 'webapp.views.chart', name='chart'),
    url(r'^announcements/$', 'webapp.views.announcements', name='announcements'),
    

    
    #url(r'^chart/$', 'webapp.views.chart', name='chart'),
]
   

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
