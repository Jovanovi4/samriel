from django.shortcuts import render, redirect, get_object_or_404
from .models import FirstScreen, Choise
from .forms import FirstScreenForm, ChoiseForm

def sites(request, pk=None):
    building = None
    choise = Noneß

    if pk:
        building = get_object_or_404(FirstScreen, pk=pk)
        choise = building.choise
        form = FirstScreenForm(instance=building)
        form2 = ChoiseForm(instance=choise) if choise else ChoiseForm()
    else:
        form = FirstScreenForm()
        form2 = ChoiseForm()

    if request.method == 'POST':
        form = FirstScreenForm(request.POST, request.FILES, instance=building)
        form2 = ChoiseForm(request.POST, instance=choise)
        if form.is_valid() and form2.is_valid():
            choise = form2.save(commit=False)
            choise.user = request.user
            choise.save()
            first_screen = form.save(commit=False)
            first_screen.choise = choise
            first_screen.save()
            return redirect('index')

    return render(request, 'sites/sites.html', {'form': form, 'form2': form2, 'building': building})

def landing(request, page_id):
    landing_page = get_object_or_404( id=page_id)