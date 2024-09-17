from django.urls import path
from . import views
from .views import homepage,detail,registration,sign_in,log_out,detail

urlpatterns = [
    path('',views.homepage,name='home'),
    path('product<int:id>',detail,name='detail'),
    path('reg/',registration,name='reg'),
    path('login/',sign_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('category/<slug:category_slug>/', homepage, name='category'),
 
]