from django.shortcuts import render, redirect, get_object_or_404
from .models import Building, Seo, TypeChoise
from .forms import BuildingForm, SeoForm, OldBuildingForm, TypeForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    sort_by = request.GET.get('sort', '-id')
    building_list = Building.objects.filter(type_choise__user=request.user).order_by(sort_by)
    paginator = Paginator(building_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj, 'sort_by': sort_by})



@login_required
def add(request, pk=None):
    types = None

    if pk:
        types = get_object_or_404(TypeChoise, pk=pk)
        form = TypeForm(instance=types)
    else:
        form = TypeForm()

    if request.method == 'POST':
        form = TypeForm(request.POST, instance=types)

        if form.is_valid():
            types = form.save(commit=False)
            types.user = request.user
            types.save()

            if types.type_choise == '1':
                building_form = BuildingForm(request.POST, request.FILES)
            elif types.type_choise == '2':
                building_form = OldBuildingForm(request.POST, request.FILES)
            else:
                building_form = None

            if building_form:

                if building_form.is_valid():
                    building = building_form.save(commit=False)
                    building.type_choise = types
                    building.save()
                    return redirect('edit', pk=building.pk)

    return render(request, 'main/add.html', {'form': form, 'types': types})


@login_required
def edit(request, pk=None):
    building = None
    form_class = None

    if pk:
        building = get_object_or_404(Building, pk=pk)
        if building.type_choise.type_choise == '1':
            form_class = BuildingForm
            template_name = 'main/edit.html'  # Шаблон для Building
        elif building.type_choise.type_choise == '2':
            form_class = OldBuildingForm
            template_name = 'main/old_edit.html'  # Шаблон для OldBuilding
        else:
            form_class = None

    if request.method == 'POST' and form_class:
        form = form_class(request.POST, request.FILES, instance=building)
        if form.is_valid():
            building = form.save(commit=False)
            building.save()
            return redirect('edit', pk=building.pk)
    else:
        form = form_class(instance=building) if form_class else None

    return render(request, template_name, {'form': form, 'building': building})



@login_required
def delete(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        building.delete()
        return redirect('index')
    return render(request, 'main/delete_confirm.html', {'building': building})


