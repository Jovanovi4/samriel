# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Building
from .forms import BuildingForm

def index(request):
    buildings = Building.objects.all()
    return render(request, 'main/index.html', {'buildings': buildings})

def add(request):
    add_form = BuildingForm()

    form = None

    if request.method == 'POST':
        form_type = request.POST.get('type')
        if form_type == '1':
            form = BuildingForm(request.POST, request.FILES)
        elif form_type == '2':
            form = BuildingForm(request.POST, request.FILES)

        if form and form.is_valid():
            form.save()
            return redirect('index')
    else:
        form_type = request.GET.get('type')
        if form_type == '1':
            form = BuildingForm()
        elif form_type == '2':
            form = BuildingForm()

    return render(request, 'main/add.html', {
        'add_form': add_form,
        'form': form,
    })

def edit(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES, instance=building)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BuildingForm(instance=building)
    return render(request, 'main/edit.html', {'form': form, 'building': building})

def delete(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        building.delete()
        return redirect('index')
    return render(request, 'main/confirm_delete.html', {'building': building})
