from django.urls import path
from project_01.views import HomeView, UserCreateView, UserListView, UserUpdateView, user_search_by_id, \
    user_delete_by_id

app_name = 'project_01'

urlpatterns = [

    # Home
    path('', HomeView.as_view(), name='home'),

    # User
    path('user/list', UserListView.as_view(), name='list_user'),
    path('user/new', UserCreateView.as_view(), name='create_user'),
    path('user/update/<pk>', UserUpdateView.as_view(), name='update_user'),
    path('user/detail/<pk>', user_search_by_id, name='detail_user'),
    path('user/delete/<pk>', user_delete_by_id, name='delete_user')
]
