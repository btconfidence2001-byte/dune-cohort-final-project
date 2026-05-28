from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import UserRegistrationForm
from django.contrib.auth import logout as django_logout

# Create your views here.


def register(request):
    """Handles new shopper or merchant registration and initiates their session."""
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Wavespace, {user.username}! Your account is ready.')
            return redirect('accounts:dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """Authenticates users and securely redirects them to their intended destination."""
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        next_url = request.POST.get('next', '')
        if form.is_valid():
            login(request, form.get_user())
            
            # Security validation checking to prevent malicious off-site redirects
            if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('accounts:dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form, 'next': next_url})


@login_required
def logout_view(request):
    """Logs out the user via POST request, with an explicit fallback for safety."""
    if request.method == 'POST':
        django_logout(request) # Call the renamed function safely here
        messages.info(request, 'You have safely logged out of your session.')
        return redirect('accounts:login')
    
    # Fallback to prevent confusing silent failures if accessed via GET link
    messages.warning(request, 'Invalid logout attempt. Please use the interface buttons.')
    return redirect('accounts:dashboard')


@login_required
def dashboard(request):
    """
    The main traffic router. Instead of a middleman screen, it instantly
    serves the correct workflow experience based on the user's role profile.
    """
    if request.user.is_staff or request.user.is_superuser:
        return redirect('accounts:staff_panel')
    elif request.user.role == 'SELLER':
        return redirect('accounts:seller_start')
    return redirect('accounts:buyer_start')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def buyer_start(request):
    return render(request, 'accounts/buyer_start.html')

@login_required
def seller_start(request):
    return render(request, 'accounts/seller_start.html')


@user_passes_test(lambda u: u.is_staff, login_url='accounts:dashboard')
def staff_panel(request):
    return render(request, 'accounts/staff_panel.html')