from django.shortcuts import render, redirect, get_object_or_404
from .models import Building, Seo
from .forms import BuildingForm, SeoForm, OldBuildingForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    sort_by = request.GET.get('sort', '-id')
    building_list = Building.objects.filter(user=request.user).order_by(sort_by)
    paginator = Paginator(building_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj, 'sort_by': sort_by})

@login_required
def edit(request, pk=None):
    if pk:
        building = get_object_or_404(Building, pk=pk, user=request.user)
        seo_instance = Seo.objects.filter(building=building).first()
    else:
        building = None
        seo_instance = None

    form_type = request.GET.get('type') if not pk else building.type

    form_class = BuildingForm if form_type == '1' else OldBuildingForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=building)
        seo_form = SeoForm(request.POST, instance=seo_instance)
        
        if form.is_valid() and seo_form.is_valid():
            building = form.save(commit=False)
            building.user = request.user  # Связываем с текущим пользователем
            building.save()
            seo = seo_form.save(commit=False)
            seo.building = building
            seo.save()
            return redirect('index')
    else:
        form = form_class(instance=building)
        seo_form = SeoForm(instance=seo_instance)

    return render(request, 'main/edit.html', {
        'form': form,
        'seo_form': seo_form,
        'building': building,
        'type': form_type
    })


@login_required
def delete(request, pk):
    building = get_object_or_404(Building, pk=pk, user=request.user)
    if request.method == 'POST':
        building.delete()
        return redirect('index')
    return render(request, 'main/delete_confirm.html', {'building': building})

