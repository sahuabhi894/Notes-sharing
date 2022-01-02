"""sharefiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about, name="about"),
    path('', index, name="index"),
    path('login',handleLogin, name="handleLogin"),
    path('signup', handleSignUp, name="handleSignUp"),
    path('contact',contact, name="contact"),
    path('contact_me',contact_me, name="contact_me"),

    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('/verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),

    path('admin_home',admin_home,name = 'admin_home'),
    path('profile',profile,name = 'profile'),
    path('logout/', handelLogout, name="handleLogout"),
    path('changepassword',changepassword, name='changepassword'),
    path('edit_profile',edit_profile, name='edit_profile'),
    path('upload_notes',upload_notes, name='upload_notes'),
    path('view_mynotes',view_mynotes, name='view_mynotes'),
    path('delete_mynotes/<int:pid>',delete_mynotes, name='delete_mynotes'),
    path('view_users',view_users, name='view_users'),
    path('delete_users/<int:pid>',delete_users, name='delete_users'),
     path('pending_notes',pending_notes, name='pending_notes'),
      path('assign_status/<int:pid>',assign_status, name='assign_status'),
      path('accepted_notes',accepted_notes, name='accepted_notes'),
       path('rejected_notes',rejected_notes, name='rejected_notes'),
 path('all_notes',all_notes, name='all_notes'),
  path('delete_notes/<int:pid>',delete_notes, name='delete_notes'),
  path('viewallnotes',viewallnotes, name='viewallnotes'),
  path('first_year',first_year,name='first_year'),
  path('second_year',second_year,name='second_year'),
  path('third_year',third_year,name='third_year'),
  path('forth_year',forth_year,name='forth_year'),
  path('other',other,name='other'),
  path('cse1',cse1,name='cse1'),
  path('ece1',ece1,name='ece1'),
  path('cse2',cse2,name='cse2'),
  path('ece2',ece2,name='ece2'),
  path('cse3',cse3,name='cse3'),
  path('ece3',ece3,name='ece3'),
  path('cse4',cse4,name='cse4'),
  path('ece4',ece4,name='ece4'),
  path('assignment_cse_1',assignment_cse_1,name='assignment_cse_1'),
  path('assignment_ece_1',assignment_ece_1,name='assignment_ece_1'),
  path('book_cse_1',book_cse_1,name='book_cse_1'),
  path('book_ece_1',book_ece_1,name='book_ece_1'),
  path('cl_cse_1',cl_cse_1,name='cl_cse_1'),
  path('cl_ece_1',cl_ece_1,name='cl_ece_1'),
  path('others_cse_1',others_cse_1,name='others_cse_1'),
  path('others_ece_1',others_ece_1,name='others_ece_1'),
  path('qp_cse_1',qp_cse_1,name='qp_cse_1'),
  path('qp_ece_1',qp_ece_1,name='qp_ece_1'),
  path('assignment_cse_2',assignment_cse_2,name='assignment_cse_2'),
  path('assignment_ece_2',assignment_ece_2,name='assignment_ece_2'),
  path('book_cse_2',book_cse_2,name='book_cse_2'),
  path('book_ece_2',book_ece_2,name='book_ece_2'),
  path('cl_cse_2',cl_cse_2,name='cl_cse_2'),
  path('cl_ece_2',cl_ece_2,name='cl_ece_2'),
  path('others_cse_2',others_cse_2,name='others_cse_2'),
  path('others_ece_2',others_ece_2,name='others_ece_2'),
  path('qp_cse_2',qp_cse_2,name='qp_cse_2'),
  path('qp_ece_2',qp_ece_2,name='qp_ece_2'),
  path('assignment_cse_3',assignment_cse_3,name='assignment_cse_3'),
  path('assignment_ece_3',assignment_ece_3,name='assignment_ece_3'),
  path('book_cse_3',book_cse_3,name='book_cse_3'),
  path('book_ece_3',book_ece_3,name='book_ece_3'),
  path('cl_cse_3',cl_cse_3,name='cl_cse_3'),
  path('cl_ece_3',cl_ece_3,name='cl_ece_3'),
  path('others_cse_3',others_cse_3,name='others_cse_3'),
  path('others_ece_3',others_ece_3,name='others_ece_3'),
  path('qp_cse_3',qp_cse_3,name='qp_cse_3'),
  path('qp_ece_3',qp_ece_3,name='qp_ece_3'),
  path('assignment_cse_4',assignment_cse_4,name='assignment_cse_4'),
  path('assignment_ece_4',assignment_ece_4,name='assignment_ece_4'),
  path('book_cse_4',book_cse_4,name='book_cse_4'),
  path('book_ece_4',book_ece_4,name='book_ece_4'),
  path('cl_cse_4',cl_cse_4,name='cl_cse_4'),
  path('cl_ece_4',cl_ece_4,name='cl_ece_4'),
  path('others_cse_4',others_cse_4,name='others_cse_4'),
  path('others_ece_4',others_ece_4,name='others_ece_4'),
  path('qp_cse_4',qp_cse_4,name='qp_cse_4'),
  path('qp_ece_4',qp_ece_4,name='qp_ece_4'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
