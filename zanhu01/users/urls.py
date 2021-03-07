from django.urls import path
from zanhu01.users import views

app_name = "users"
urlpatterns = [
    path('update/', views.UserUpdateView.as_view(), name='update'),
    path('<username>/', views.UserDetailView.as_view(), name='detail'),
]
