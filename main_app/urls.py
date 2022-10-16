from django.urls import path

import main_app.views as views

# Client
urlpatterns = [
    # path('test', views.TestView.as_view(), name='test'),
    path('stream', views.Home, name='test'),
]
