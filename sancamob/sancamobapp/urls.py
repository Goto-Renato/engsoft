from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'sancamobapp.views.reps'),
    url(r'^get/(?P<rep_id>\d+)/$', 'sancamobapp.views.rep')
)
