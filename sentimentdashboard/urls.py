from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^input$', 'dashboard.views.inputInfo', name='inputInfo'),
    url(r'^result$', 'dashboard.views.result', name='result'),
    url(r'^dashboard$', 'dashboard.views.dashboard', name='dashboard'),
    url(r'^home$', 'dashboard.views.home', name='home'),
    url(r'^$', 'dashboard.views.home', name='home'),
    url(r'^createclassifier$', 'dashboard.views.createClassifier', name='createClassifier'),
    url(r'^about$', 'dashboard.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
