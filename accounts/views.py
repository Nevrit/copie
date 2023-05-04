# Cette importation permet de récupérer le modèle utilisateur en l'occurence la class Shopper dans le accounts.models
from django.contrib.auth import get_user_model, login, logout, authenticate
# Cette importation permet de récupérer le modèle utilisateur en l'occurence la class Shopper dans le accounts.models
from django.contrib.auth import login
from django.http import HttpResponseRedirect 
from django.shortcuts import redirect, render
from django.urls import reverse
from Home.views import index

# Cette variable permet de récupérer la class Utilisateur Shopper dans accounts.models.Shopper
User = get_user_model()
# Cette variable permet de récupérer la class Utilisateur Shopper dans accounts.models.Shopper


# Create your views here.
def signin(request):
    if request.method == 'POST':
        # Si la request est égal à POST, on récupère les données des éléments (username) qui sont dans le formulaire signup.html
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Si la request est égal à POST, on récupère les données des éléments (username) qui sont dans le formulaire signup.html
        
        # Récupère les données passées à la variable user (nom utilisateur & mot de passe)
        user = authenticate(username = username, password = password)
        # Récupère les données passées à la variable user (nom utilisateur & mot de passe)
        
        # Vérification des données rentrées. Si elle sont correctes, on connecte l'utilisateur
        if user:
            login(request, user) # On conncete l'utilisateur s'il existe dans la base
            return HttpResponseRedirect(reverse(index))
        
    return render(request, 'account/signin.html')
    

def signup(request):
    if request.method == 'POST':
        # Si la request est égal à POST, on récupère les données des éléments (name) qui sont dans le formulaire signup.html
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        
        
        # Si la request est égal à POST, on récupère les données des éléments (name) qui sont dans le formulaire signup.html

        # Creer un utilisateurs
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            last_name = last_name,
            first_name = first_name
        )
        # Creer un utilisateurs
        
        # Connecter l'utilisateur
        connection = login(request, user)
        # Connecter l'utilisateur
        
        return HttpResponseRedirect(reverse(index))
        
    return render(request, 'account/signup.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse(index)) 