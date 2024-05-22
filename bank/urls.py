from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.BankListView.as_view(), name='bank-list'),
    path('branches/<str:name>/', views.BranchDetailView.as_view(), name='branch-detail'),
]