from django.urls import re_path as url
from django.contrib import admin
from msystem import views 






urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    url('admin/', admin.site.urls),       
    url(r'^msystem/cash/(\d+)/$', views.ca_sh, name='ca_sh'), 
    url(r'^msystem/cash/(\d+)/cas_h$', views.cas_h, name='cas_h'), 
    url(r'^msystem/branch/(\d+)/$', views.branch_br, name='branch_br'), 
    url(r'^msystem/branch/(\d+)/br_add$', views.br_add, name='br_add'), 
    url('cashl/', views.ass_list, name='ass_list'), 
    url(r'^msystem/n_member/$', views.n_member, name='n_member'),
    
    url('memlist/', views.mem_list, name='mem_list'),
    url(r'^msystem/meminfo/(\d+)/$', views.mem_per, name='mem_per'),
    url(r'^msystem/memdel/(\d+)/$', views.delMem, name='delMem'),
    url(r'^msystem/memupdate/(\d+)/$', views.updMem, name='updMem'),
    url(r'^msystem/memupdate/(\d+)/update_mem$', views.MemEdit, name='MemEdit'),
    url('membere/', views.member_p, name='member_p'),
    url('memlist/membere/', views.member_p, name='member_p'),
    url('report/', views.bara_re, name='bara_re'),
    url('memrep/', views.bara_indv, name='bara_indv'),
    url(r'^msystem/brrep/(\d+)/$', views.bara_indv, name='bara_indv'), 
    url(r'^msystem/brrep/(\d+)/memr_ad$', views.report_add, name='report_add'), 
    url('membrep/', views.mem_port, name='mem_port'),
    url(r'^msystem/memor/(\d+)/$', views.mem_repor, name='mem_repor'),
    url(r'^msystem/memor/(\d+)/memp_add$', views.member_report, name='member_report'),

    url(r'^about$', views.about, name='about'),
    url(r'^contacts$', views.contacts, name=' contacts'),
   ]
    

