from django.urls.resolvers import URLPattern
from todos import views
from django.urls import path


urlpatterns = [
    # path('', views.TodosAPIView.as_view(), name='todos'),

    # serach [ todos/?id=2, or todos/?desc="" or todos/?is_complete=true ]

    path('create-todo', views.CreateTodoAPIView.as_view(), name='create-todo'),
    path('list-todo', views.ListTodoAPIView.as_view(), name='list-todo'),
    path('<int:id>', views.TodoDetailAPIView.as_view(), name='todo'),

]