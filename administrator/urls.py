from django.urls import path, re_path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', dash_view, name='dashboard'),
    path('accounts/login/', qwqw, name='qwqw'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),



    path('question/', select_direction_view, name = 'question'),
    path('single-question-edit/<int:pk>/', single_question_edit, name='single_question_edit'),
    path('create-question/<int:pk>/', create_question_view, name = 'create_question'),
    path('delete-question/<int:pk>/', delete_question_view, name = 'delete_question'),

    path('single-logic-question-edit/<int:pk>/', single_logic_question_edit, name='single_logic_question_edit'),
    path('delete-logic-question/<int:pk>/', delete_logic_question_view, name = 'delete_logic_question'),
    path('create-logic-question/<int:pk>/', create_lg_question_view, name = 'create_lg_question'),
    path('logic-question/', logic_question_view, name = 'logic_question'),
    
    
    
    path('welcome/', create_welcome_view, name = 'create_welcome'),
    


    path('create-direction/', create_direction_view, name = 'create_direction'),
    path('selected-dir/<int:pk>/', selected_direction_view, name = 'selected_direction'),
    path('selected-dir-logic/<int:pk>/', selected_direction_logic_view, name = 'selected_direction_logic'),
    path('continue-dir/<int:pk>/', continue_dir_view, name = 'continue_dir'),
    path('directions/', direction_view, name = 'directions'),
    path('single-direction/<int:pk>/', direction_edit_view, name = 'direction_edit'),
    path('delete-direction/<int:pk>/', delete_direction_view, name = 'delete_dir'),
    

    path('results/', get_result_view, name='results'),
    path('logic-answers/<int:pk>/', logic_answers_view, name='view_answers'),


    path('reset-passwd/', reset_passwd_view, name='reset'),


    path('return-previous-is-logic/<int:pk>/', return_previous_is_logic_view, name='return_previous_is_logic_view'),


    path('create-error/<int:pk>/', backend_error, name='backend_error'),

    
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)