#from django.conf import settings
#from django.conf.urls.static import static
import statistics
from django.urls import path 
from . import views
from shopmart import settings

urlpatterns = [
    path('index',views.index,name='index'),
    path('fixed',views.fixed,name='fixed'),
    path('Nonfixed',views.Nonfixed,name='Nonfixed'),
    path('Statement',views.Statement,name='Statement'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about'),
    path('insertfixed',views.insertfixed,name='insertfixed'),
    path('insertnonfixed',views.insertnonfixed,name='insertnonfixed'),
    
]

