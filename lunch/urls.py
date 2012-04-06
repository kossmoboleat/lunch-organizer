from django.conf.urls.defaults import patterns, include, url
from views import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
    ('^hello/$', hello),
    #(r'^admin/', admin.site.urls),
    (r'^time/$', current_datetime),
    (r'^lunch/$', lunch_template),
    (r'^lunch/new_lunch/(\d{4}-\d{2}-\d{2})/$', new_lunch_template),
    (r'^lunch/edit_lunch/(\d*)/$', edit_lunch_template)
)
