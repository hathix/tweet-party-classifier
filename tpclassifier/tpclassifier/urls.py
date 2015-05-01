from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'tpclassifier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^tweets/', include('tweets.urls')),
    url(r'^scikit/', include('scikit.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
