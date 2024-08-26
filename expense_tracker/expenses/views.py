from django.shortcuts import render, redirect , get_object_or_404
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login , logout as auth_logout
from .models import Expenses, Category
from .forms import Expensesform , Categoryform
from django.db.models import Sum, Avg
from django.contrib.auth.decorators import login_required
from datetime import datetime

def home(request):
    if request.user.is_authenticated:
        user_expenses = Expenses.objects.filter(user=request.user)
        total_expenditure = user_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        average_expenditure = user_expenses.aggregate(Avg('amount'))['amount__avg'] or 0
        expenses_by_category = user_expenses.values('category__name').annotate(total_amount=Sum('amount'))

        context = {
            'total_expenditure': total_expenditure,
            'average_expenditure': average_expenditure,
            'expenses_by_category': expenses_by_category
        }
    else:
        context = {}
    return render(request, 'home.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})


def logout(request):
        auth_logout(request)
        return redirect('home')


@login_required
def expense_list(request):
    expenses = Expenses.objects.filter(user=request.user)
    return render(request, 'expenses/expense_list.html',{'expenses':expenses})

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = Expensesform(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = Expensesform()
    return render(request, 'expenses/expense_form.html', {'form':form})

@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expenses, pk=pk, user=request.user)
    if request.method == 'POST':
        form = Expensesform(request.POST, instance = expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = Expensesform(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form':form})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expenses, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/delete.html', {'expense': expense})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'Category/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = Categoryform()
    return render(request, 'Category/category_form.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = Categoryform(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = Categoryform(instance=category)
    return render(request, 'Category/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'Category/delete.html', {'category': category})

@login_required
def summary_report(request):
    user_expenses = Expenses.objects.filter(user=request.user)
    total_expenditure = user_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    average_expenditure = user_expenses.aggregate(Avg('amount'))['amount__avg'] or 0

    # Group expenses by category
    expenses_by_category = user_expenses.values('category__name').annotate(total_amount=Sum('amount'))

    context = {
        'total_expenditure': total_expenditure,
        'average_expenditure': average_expenditure,
        'expenses_by_category': expenses_by_category
    }
    return render(request, 'report/summary.html', context)

@login_required
def expenses_by_date_range(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except (ValueError, TypeError):
        start_date = end_date = None

    user_expenses = Expenses.objects.filter(user=request.user)
    if start_date and end_date:
        user_expenses = user_expenses.filter(date__range=[start_date, end_date])
    
    context = {
        'expenses': user_expenses
    }
    return render(request, 'report/by_date_range.html', context)

@login_required
def expenses_by_category(request):
    user_expenses = Expenses.objects.filter(user=request.user)

    # Group expenses by category
    expenses_by_category = user_expenses.values('category__name').annotate(total_amount=Sum('amount'))

    context = {
        'expenses_by_category': expenses_by_category
    }
    return render(request, 'report/by_category.html', context)

