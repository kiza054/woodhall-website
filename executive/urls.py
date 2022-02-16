from django.urls import path
from executive.views import (ExecutiveIndexView, 
                            QuartermastersDatabaseView, 
                            QuartermastersDatabaseAddView, 
                            QuartermastersDatabaseEditView, 
                            QuartermastersDatabaseDeleteView)

urlpatterns = [
    path('home/', ExecutiveIndexView.as_view(), name='executive_home'),
    path('quartermaster/database/', QuartermastersDatabaseView.as_view(), name='executive_quartermaster_database'),
    path('quartermaster/database/add/', QuartermastersDatabaseAddView.as_view(), name='executive_quartermaster_database_add'),
    path('quartermaster/database/edit/<slug:slug>', QuartermastersDatabaseEditView.as_view(), name='executive_quartermaster_database_edit'),
    path('quartermaster/database/delete/<slug:slug>', QuartermastersDatabaseDeleteView.as_view(), name='executive_quartermaster_database_delete')
]