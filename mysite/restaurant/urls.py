from django.urls import path

from .views import ListUsercreate, UserRetrieveUpdateDestroy
# app_name = "profiles"
app_name = 'restaurant'
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('ListUsercreate/', ListUsercreate.as_view(), name="createListUser"),
    path('UserRetrieveUpdateDestroy/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name="UserRetrieveUpdateDestroy"),

]
