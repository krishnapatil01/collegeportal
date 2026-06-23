from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),


    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_request/<int:request_id>/<str:action>/', views.manage_request, name='manage_request'),
    path('view_student_profiles', views.view_student_profiles, name='view_student_profiles'),
    path('view_alumni_profiles', views.view_alumni_profiles, name='view_alumni_profiles'),
    path('add_funding_info', views.add_funding_info, name='add_funding_info'),
    

    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('create_student_profile/', views.create_student_profile, name='create_student_profile'),
    path('view_student_profile/', views.view_student_profile, name='view_student_profile'),
    path('update_student_profile/', views.update_student_profile, name='update_student_profile'),
    path('student_job_port/', views.student_job_port, name='student_job_port'),  
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),# View a specific post with comments
    path('search_alumni/', views.search_alumni, name='search_alumni'),  
    path('alumni/<int:alumni_id>/', views.alumni_profile, name='alumni_profile'),
    path('view_resources/', views.view_resources, name='view_resources'),
   



    path('alumni_dashboard/', views.alumni_dashboard, name='alumni_dashboard'),
    path('view_alumni_profile/', views.view_alumni_profile, name='view_alumni_profile'),
    path('update_alumni_profile/', views.update_alumni_profile, name='update_alumni_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_board/', views.post_board, name='post_board'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('view_post_alumini/<int:post_id>/', views.view_post_alumini, name='view_post_alumini'),# View a specific post with comments
    path('upload_resource/', views.upload_resource, name='upload_resource'),
    path('view_uploaded_notes', views.view_uploaded_notes, name='view_uploaded_notes'),
    path('edit_resource/edit/<int:pk>/', views.edit_resource, name='edit_resource'),
    path('delete_resource/delete/<int:pk>/', views.delete_resource, name='delete_resource'),
    path('view_funding_info', views.view_funding_info, name='view_funding_info'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
