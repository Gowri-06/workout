from django.urls import path
from myapp import views
from django.contrib import admin


urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.index, name='index'), 
    path("",views.index, name='index'), 
    # path("add/",views.add, name='add'), 
    # path("add/addrecord/",views.addrecord, name='addrecord'),
    # path('delete/<int:id>/',views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('update/updaterecord/<int:id>/', views.updaterecord, name='updaterecord'),

 
]