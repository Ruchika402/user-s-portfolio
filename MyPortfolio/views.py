from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from urllib3 import request

from .models import portfolios, Project
from .forms import RegisterForm, PortfolioForm




# ================= HOME =================
def home(request):
    portfolio = None

    if request.user.is_authenticated:
        try:
            portfolio = portfolios.objects.get(user=request.user)
        except portfolios.DoesNotExist:
            portfolio = None

    return render(request, 'MyPortfolio/home.html', {'portfolio': portfolio})


# ================= ABOUT =================
def about(request):
    portfolio = None

    if request.user.is_authenticated:
        try:
            portfolio = portfolios.objects.get(user=request.user)
        except portfolios.DoesNotExist:
            portfolio = None

    return render(request, 'MyPortfolio/about.html', {'portfolio': portfolio})


# ================= SERVICES =================
def services(request):
    portfolio = None

    if request.user.is_authenticated:
        try:
            portfolio = portfolios.objects.get(user=request.user)
        except portfolios.DoesNotExist:
            portfolio = None

    return render(request, 'MyPortfolio/services.html', {'portfolio': portfolio})


# ================= PROJECTS =================
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def projects(request):
    portfolio = None
    user_projects = None

    if request.user.is_authenticated:
        try:
            portfolio = portfolios.objects.get(user=request.user)
        except portfolios.DoesNotExist:
            portfolio = None

        # Fetch projects for the logged-in user
        user_projects = Project.objects.filter(user=request.user)

    return render(request, 'MyPortfolio/projects.html', {
        'portfolio': portfolio,
        'projects': user_projects
    })
# 2️⃣ Add a New Project
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = request.user  # assign logged-in user
            new_project.save()
            return redirect('projects')  # redirect to projects page
    else:
        form = ProjectForm()
    
    return render(request, 'MyPortfolio/add_project.html', {'form': form})

# ================= CONTACT =================
def contact(request):
    portfolio = None

    if request.user.is_authenticated:
        try:
            portfolio = portfolios.objects.get(user=request.user)
        except portfolios.DoesNotExist:
            portfolio = None

    return render(request, 'MyPortfolio/contact.html', {'portfolio': portfolio})


# ================= REGISTER =================
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'MyPortfolio/register.html', {'form': form})



# ================= LOGIN =================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'MyPortfolio/login.html')


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('home')


# ================= DASHBOARD =================
@login_required
def dashboard(request):
    portfolio, created = portfolios.objects.get_or_create(user=request.user)

    if request.method == 'POST' and 'update_portfolio' in request.POST:
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PortfolioForm(instance=portfolio)

    if request.method == 'POST' and 'add_project' in request.POST:
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('dashboard')
    else:
        project_form = ProjectForm()

    user_projects = Project.objects.filter(user=request.user)
    return render(request, 'MyPortfolio/dashboard.html', {
        'form': form,
        'projects': user_projects,
        'project_form': project_form
    })
