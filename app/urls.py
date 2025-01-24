from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('matching/', views.matching_view, name='matching_view'),
    path('success/', views.success, name='success'),  # 成功時のリダイレクト先
]