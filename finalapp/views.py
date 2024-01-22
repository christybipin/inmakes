from django.contrib import auth, messages
from django.http import JsonResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm, PersonCreationForm
from django.shortcuts import redirect, render, get_object_or_404

from .models import Person, City


# Create your views here.
def store(request):
    context = { }
    return render(request, 'Main.html', context)


def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                return redirect('login')
            except:
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                return redirect('loginView')
            except:
                pass
    else:
        form = RegisterForm()
    return render(request, 'register.html', { 'form': form })


def login(request):
    return render(request, 'button.html')


def personcreateview(request):
    submitted=False
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_form?submitted=True')
        else:
            form = PersonCreationForm
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'form.html', { 'form': form, 'submitted': submitted})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/', pk=pk)
    return render(request, 'form.html', { 'form': form })


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', { 'cities': cities })
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def logout(request):
    auth.logout(request)
    return redirect('/')
