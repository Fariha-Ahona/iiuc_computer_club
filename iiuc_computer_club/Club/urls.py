from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view

urlpatterns = [
    path('', views.main, name='main'),  # Welcome Page
    # path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard Page
    path('dashboard/notice/', views.notice, name='notice'),
    #path('signout/', views.signout, name='signout'),  # Logout Functionality
    path('about/', views.about, name='about'),
    path('notice/', views.notice, name='notice'),
    path('announcement/', views.announcement, name='announcement'),
    path('events/', views.event_list, name='event_list'),
    path('saveenquiry/', views.save_enquiry,name='saveenquiry'),
    path('contact/', contact_view, name='contact'),
    path('Blog/', views.blog_page, name='blog_page'),
    path('logout/', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

