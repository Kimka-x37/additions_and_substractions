from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_addition', views.add_addition, name='add_addition'),
    path('add_substraction', views.add_substraction, name='add_substraction'),
    path('additions', views.additions, name='additions'),
    path('substractions', views.substractions, name='substractions'),
    path('delete_page', views.delete_page, name='delete_page'),
    path('delete_page/<int:id>', views.delete, name='delete'),
    path('logout', views.logout_view, name='logout')
]