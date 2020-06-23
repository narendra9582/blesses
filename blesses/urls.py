from django.contrib import admin  
from django.urls import path  
import homepage
import employee
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', homepage.views.emp),  
    path('emp', employee.views.emp),  
    path('show',employee.views.show),  
    path('edit/<int:id>', employee.views.edit),  
    path('update/<int:id>', employee.views.update),  
    path('delete/<int:id>', employee.views.destroy),  
] 