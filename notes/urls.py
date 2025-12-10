from django.urls import path
from . import views
urlpatterns = [
    path('', views.note_list, name='home'),
    path('note/<int:pk>', views.note_detail, name='note'),
    path('add/', views.note_add ,name='add-note'),
    path('edit/<int:pk>', views.NoteUpdateView.as_view() ,name='edit-note'),
    path('delete/<int:pk>', views.NoteDeleteView.as_view(), name='delete-note'),
    path('logorsign/', views.logorsign, name='logorsign'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup')

]