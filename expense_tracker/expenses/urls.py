from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    # User authentication based urls
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),

    # Expensee management based urls 
    path('expenses/', views.expense_list, name = 'expense_list'),
    path('expense/create/',views.expense_create,name= 'expense_create'),
    path('expense/<int:pk>/edit/', views.expense_edit, name = 'expense_edit'),
    path('expenses/<int:pk>/delete/',views.expense_delete, name = 'expense_delete'),

    #Category Management based Urls
    path('categories/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    #Reports Based URls 
    path('summary_report/', views.summary_report, name='summary_report'),
    path('expenses_by_date_range/', views.expenses_by_date_range, name='expenses_by_date_range'),
    path('expenses_by_category/', views.expenses_by_category, name='expenses_by_category'),


]
    