from django.urls import path
from DemoForm import views
urlpatterns = [
    path('',views.w1),
    path('success/',views.success_views),
    path('Regform/',views.reg_views),
    path('Final/',views.final_views),
    path('Login/',views.login_views),
    path('savedata/',views.save_views),
]
