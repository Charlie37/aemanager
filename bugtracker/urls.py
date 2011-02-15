from django.conf.urls.defaults import *

urlpatterns = patterns('bugtracker.views',

    # issue
    url(regex=r'^$',
        view='issue_list',
        name='issue_list'),
    url(regex=r'^closed/$',
        view='closed_issue_list',
        name='closed_issue_list'),
    url(regex=r'^add/$',
        view='issue_create_or_edit',
        name='issue_add'),
    url(regex=r'^edit/(?P<id>\d+)/$',
        view='issue_create_or_edit',
        name='issue_edit'),
    url(regex=r'^delete/(?P<id>\d+)/$',
        view='issue_delete',
        name='issue_delete'),
    url(regex=r'^(?P<id>\d+)/$',
        view='issue_detail',
        name='issue_detail'),
    url(regex=r'^close/(?P<id>\d+)/$',
        view='issue_close',
        name='issue_close'),
    url(regex=r'^reopen/(?P<id>\d+)/$',
        view='issue_reopen',
        name='issue_reopen'),

    # comment
    url(regex=r'^comment/edit/(?P<id>\d+)/$',
        view='comment_create_or_edit',
        name='comment_edit'),
    url(regex=r'^comment/add/(?P<issue_id>\d+)/$',
        view='comment_create_or_edit',
        name='comment_add'),
    url(regex=r'^comment/delete/(?P<id>\d+)/$',
        view='comment_delete',
        name='comment_delete'),

    # vote
    url(regex=r'^vote/(?P<issue_id>\d+)/$',
        view='vote',
        name='vote'),
    url(regex=r'^unvote/(?P<issue_id>\d+)/$',
        view='unvote',
        name='unvote'),
)