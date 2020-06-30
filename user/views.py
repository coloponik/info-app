from django.shortcuts import render
from account.decorators import login_required
import user.forms
import account.forms
import account.views

class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):
    form_class = user.forms.SignupForm

    def generate_username(self, form):
        username = form.cleaned_data['email']
        return username
    
    # def after_signup(self, form):
    #     super(SignupView, self).after_signup(form)

@login_required
def profile(request):
    return render(request, 'account/info_profile.html')

@login_required
def logout(request):
    return render(request, 'account/logout.html')

@login_required
def notes(request):
    return render(request, 'account/notes.html')

@login_required
def settings(request):
    return render(request, 'account/settings.html')