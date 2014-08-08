from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^input$', 'dashboard.views.inputInfo', name='inputInfo'),
    url(r'^result$', 'dashboard.views.result', name='result'),
    url(r'^createclassifier$', 'dashboard.views.createClassifier', name='createClassifier'),
    url(r'^admin/', include(admin.site.urls)),
)
