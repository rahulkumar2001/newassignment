from django.urls import path
#now import the views.py file into this code
from myapp import views
urlpatterns=[
  path('donardata/',views.Donordata.as_view(), name="donordata"),
  # path('mydownline',views.myDownline,name="mydownline")

]