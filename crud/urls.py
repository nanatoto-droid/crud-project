from django.urls import path
from .import views
urlpatterns = [
path('',views.user_list),
    path('Add/',views.add_user),
    # path('Edit/<id>',views.edit_user),
    path('Edit/<id>',views.edit_user),
    path('Delete/<id>',views.delete_user),
    path('View/<id>',views.view_user),

]