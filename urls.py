from django.conf.urls.defaults import *
from lunch.views import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
	('^hello/$', hello),
    #(r'^admin/', admin.site.urls),
    (r'^time/$', current_datetime),
    (r'^lunch/$', lunch_template),
    (r'^lunch/new_lunch/(\d{4}-\d{2}-\d{2})/$', new_lunch_template),
    (r'^lunch/edit_lunch/(\d*)/$', edit_lunch_template)
)
