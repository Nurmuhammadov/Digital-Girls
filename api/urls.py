from django.urls import path, include
from .views import *


urlpatterns = [
    # gets
    path('get-welcome/', get_welcome, name='get_welcome'),
    path('get-direction/', get_direction, name='get_direction'),
    path('get-test/', get_test, name='get_test'),

    #posts
    path('post-pupil/', create_pupil, name='past_pupil'),
    path('post-result/', create_result, name='post_result'),
    path('post-logic-result/', create_logic_reault, name='post_logic_reault'),
]
