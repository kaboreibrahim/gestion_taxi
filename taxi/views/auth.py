from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from taxi.forms import PropietaireForm, LoginForm,VerificationForm,AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from taxi.models import VerificationCode
from django.contrib.auth import get_backends
from django.contrib.auth.decorators import login_required
# view de creation de compte 
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
#from taxi.models import P 

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
             
def register(request):
    if request.method == 'POST':
        form = PropietaireForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('verify')  # Rediriger vers la page de vérification
    else:
        form = PropietaireForm()
    return render(request, 'connexion/register.html', {'form': form})

# view de verification de creation de compte 

def verify(request):
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                verification_code = VerificationCode.objects.get(code=code)
                user = verification_code.user
                user.is_active = True
                user.is_verified = True
                user.save()
                verification_code.delete()  # Supprimer le code de vérification après validation
                
                # Obtenir le backend d'authentification utilisé
                backend = get_backends()[0]
                login(request, user, backend='accounts.auth_backends.EmailOrUsernameModelBackend')
                return redirect('login')
            except VerificationCode.DoesNotExist:
                form.add_error('code', 'Code invalide')
    else:
        form = VerificationForm()
    return render(request, 'connexion/verify.html', {'form': form})


# view de connexion """
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()
    return render(request, 'connexion/login.html', {'form': form})


@login_required
def deconnection(request):
    logout(request)
    # Redirige l'utilisateur vers une page après la déconnexion (par exemple la page d'accueil)
    return redirect('login')

#view reste password

"""def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():  # Mettre à jour le nom du modèle ici
                # Ici, vous pouvez ajouter le code pour envoyer l'e-mail de réinitialisation de mot de passe
                return redirect('password_reset_done')
            else:
                form.add_error('email', "Aucun compte n'est associé à cette adresse e-mail.")
    else:
        form = PasswordResetForm()
    return render(request, 'recuperation/password_reset.html', {'form': form})"""
