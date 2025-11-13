from .views import IntegrationViewList,IntegrationAddView,IntegrationUpdateView,IntegrationDeleteView , ActivityListView
from django.urls import path


app_name = 'blogs'
urlpatterns =[
    path('integrationList/',IntegrationViewList.as_view(),name = 'integ-list'),
    path('add-integrationList/', IntegrationAddView.as_view(),name = 'integ-add'),
    path('update/<int:pk>', IntegrationUpdateView.as_view(), name = 'integ-update'),
    path('delete_integ/<int:pk>', IntegrationDeleteView.as_view(), name = 'integ-delete'),
    path('postslist/', ActivityListView.as_view(),name='activity-list'),
   
]
