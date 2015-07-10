from collectionapp.backends import MyRegistrationView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)


urlpatterns = patterns('',
    url(r'^$', 'collectionapp.views.index', name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^posts/(?P<slug>[-\w]+)/$',
        'collectionapp.views.post_detail',
        name='post_detail'),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$',
        'collectionapp.views.edit_post',
        name='edit_post'),

    # create an article
    url(r'^posts/(?P<slug>[-\w]+)/create_article/$',
        'collectionapp.views.create_article',
        name='create_article'),

    # our new browse flow
    url(r'^browse/$', RedirectView.as_view(pattern_name='browse')),
    url(r'^browse/name/$','collectionapp.views.browse_by_name',name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$', 'collectionapp.views.browse_by_name', name='browse_by_name'),

    # the new password reset URLs
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/ (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'}, name="password_reset_complete"),

    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_post/$', 'collectionapp.views.create_post', name='registration_create_post'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
