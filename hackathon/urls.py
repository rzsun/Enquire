from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^input$', 'sentclassify.views.inputInfo', name='inputInfo'),
    url(r'^result$', 'sentclassify.views.result', name='result'),
    url(r'^createclassifier$', 'sentclassify.views.createClassifier', name='createClassifier'),
    url(r'^admin/', include(admin.site.urls)),
)
