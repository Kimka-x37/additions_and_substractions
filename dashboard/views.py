from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from .models import *
from .forms import *

@login_required(login_url='home')
def dashboard(request):
    username = request.user.username
    transactions = Transaction.objects.filter(autor = username)
    transactions_sum = sum(transactions.values_list('sum', flat=True))

    return render(request, 'dashboard/dashboard.html', {
        'username': username, 
        'transactions':transactions, 
        'sum':transactions_sum})

@login_required(login_url='home')
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='home')
def add_addition(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid:
            addition = form.save(commit=False)
            addition.substraction = False
            addition.autor = request.user.username
            addition.save()
            return redirect('dashboard')
        else:
            return render(request, 'dashboard/add_addition.html', {'form':form, 'error':"Вы ввели чтото не правильно!"})
    else:
        form = TransactionForm()
        return render(request, 'dashboard/add_addition.html', {'form':form})

@login_required(login_url='home')
def add_substraction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid:
            addition = form.save(commit=False)
            addition.sum = form.cleaned_data['sum'] * -1
            addition.substraction = True
            addition.autor = request.user.username
            addition.save()
            return redirect('dashboard')
        else:
            return render(request, 'dashboard/add_substraction.html', {'form':form, 'error':"Вы ввели чтото не правильно!"})
    else:
        form = TransactionForm()
        return render(request, 'dashboard/add_substraction.html', {'form':form})

@login_required(login_url='home')
def additions(request):
    username = request.user.username
    transactions = Transaction.objects.filter(autor = username, substraction = False)

    return render(request, 'dashboard/additions.html', {'transactions':transactions})

@login_required(login_url='home')
def substractions(request):
    username = request.user.username
    transactions = Transaction.objects.filter(autor = username, substraction = True)

    return render(request, 'dashboard/substractions.html', {'transactions':transactions})

@login_required(login_url='home')
def delete_page(request):
    username  = request.user.username
    transactions = Transaction.objects.filter(autor = username)
    transactions_sum = sum(transactions.values_list('sum', flat=True))

    return render(request, 'dashboard/delete.html', {
        'transactions':transactions, 
        'sum':transactions_sum})

@login_required(login_url='home')
def delete(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.user.username == transaction.autor:
        transaction.delete()
        return redirect('delete_page')
    else:
        return redirect('delete_page')