from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'controller.views.home', name='home'),
    url(r'.*[.]html$', 'controller.views.page', name='page'),
    url(r'^test','controller.views.test', name='test'),
    url(r'^member_create','member.views.member_create',name='member_create'),
    url(r'^member_random','member.views.member',name='member_random')
    # url(r'^httpdocs/', include('httpdocs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
