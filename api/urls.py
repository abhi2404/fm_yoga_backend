from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Registration.as_view()),
    path('login/',views.Login.as_view()),
    path('UserDetails/',views.user_details.as_view()),
    path('payment/',views.payment_month_wise.as_view()),
    path('plan_activity/',views.plan_activity.as_view()),
    path('all_shift/',views.get_all_shift.as_view()),
    path('logout/',views.Logout.as_view())
]