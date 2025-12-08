from django.urls import path
from . import views
urlpatterns = [
    path('', views.task_list, name='home'),
    path('note/<int:pk>', views.task_note, name='note'),
    path('add/', views.task_add,name='add-note'),
    path('edit/<int:pk>', views.NoteUpdateView.as_view() ,name='edit-note'),
    path('delete/<int:pk>', views.task_delete, name='delete-note'),
    path('logorsign/', views.logorsign, name='logorsign'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')

]