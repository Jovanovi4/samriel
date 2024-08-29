from django.shortcuts import render, redirect, get_object_or_404
from .models import Building, Seo, TypeChoise, Image, Plans
from .forms import BuildingForm, SeoForm, OldBuildingForm, TypeForm, ImageForm, PlansForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse




@login_required
def index(request):
    sort_by = request.GET.get('sort', '-id')
    query = request.GET.get('q', '')
    
    if query:
        building_list = Building.objects.filter(
            type_choise__user=request.user,
            title__icontains=query  # Фильтрация по полю title, игнорируя регистр
        ).order_by(sort_by)
    else:
        building_list = Building.objects.filter(type_choise__user=request.user).order_by(sort_by)
    
    # Пагинация
    paginator = Paginator(building_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'main/index.html', {
        'page_obj': page_obj,
        'sort_by': sort_by,
        'query': query
    })



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




# @login_required
# def edit(request, pk=None):
#     building = None
#     form_class = None
#     image_form_class = None
#     plans_form_class = None
#     template_name = None

#     if pk:
#         building = get_object_or_404(Building, pk=pk)
#         if building.type_choise.type_choise == '1':
#             form_class = BuildingForm
#             image_form_class = ImageForm
#             template_name = 'main/edit.html'
#         elif building.type_choise.type_choise == '2':
#             form_class = OldBuildingForm
#             image_form_class = ImageForm
#             template_name = 'main/old_edit.html'
#         else:
#             form_class = None
#             image_form_class = None

#     if request.method == 'POST' and form_class:
#         form = form_class(request.POST,request.FILES, instance=building)
#         image_form = image_form_class(request.POST, request.FILES)

#         if form.is_valid() and image_form.is_valid():
#             building = form.save(commit=False)
#             building.save()

#             # Обработка изображений для слайдера
#             images = request.FILES.getlist('image_s')
#             for img in images:
#                 Image.objects.create(building=building, image_s=img)

#             return redirect('edit', pk=building.pk)
#     else:
#         form = form_class(instance=building) if form_class else None
#         image_form = image_form_class() if image_form_class else None

#  # Получение всех изображений для конкретного объекта
#     image_list = Image.objects.filter(building=building)


#     return render(request, template_name, {'form': form, 'image_form': image_form, 'building': building, 'image_list': image_list})




@login_required
def edit(request, pk=None):
    building = None
    form_class = None
    image_form_class = None
    plans_form_class = PlansForm  # Инициализация формы для планов
    template_name = None

    if pk:
        building = get_object_or_404(Building, pk=pk)
        if building.type_choise.type_choise == '1':
            form_class = BuildingForm
            image_form_class = ImageForm
            template_name = 'main/edit.html'
        elif building.type_choise.type_choise == '2':
            form_class = OldBuildingForm
            image_form_class = ImageForm
            template_name = 'main/old_edit.html'
        else:
            form_class = None
            image_form_class = None

    if request.method == 'POST' and form_class:
        form = form_class(request.POST, request.FILES, instance=building)
        image_form = image_form_class(request.POST, request.FILES)
        plans_form = plans_form_class(request.POST)

        if form.is_valid() and image_form.is_valid() and plans_form.is_valid():
            building = form.save(commit=False)
            building.save()

            # Обработка изображений для слайдера
            images = request.FILES.getlist('image_s')
            for img in images:
                Image.objects.create(building=building, image_s=img)

            # Обработка планов
            plans = plans_form.save(commit=False)
            plans.building = building
            plans.save()

            return redirect('edit', pk=building.pk)
    else:
        form = form_class(instance=building) if form_class else None
        image_form = image_form_class() if image_form_class else None
        plans_form = plans_form_class(instance=building.plans.first()) if building and building.plans.exists() else plans_form_class()

    # Получение всех изображений для конкретного объекта
    image_list = Image.objects.filter(building=building)

    return render(request, template_name, {
        'form': form,
        'image_form': image_form,
        'building': building,
        'image_list': image_list,
        'plans_form': plans_form,
    })


@login_required
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('edit', pk=image.building.pk)
    return render(request, 'main/delete_confirm.html', {'image': image})


@login_required
def delete(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        building.delete()
        return redirect('index')
    return render(request, 'main/delete_confirm.html', {'building': building})

# @login_required
# def delete_image_building(request, building_id):
#     building = get_object_or_404(Building, pk=building_id)
#     if request.method == 'POST':
#         if building.image:
#             building.image.delete(save=False)
#             building.image = None
#             building.save()
#         else:
#             return redirect('edit', pk=building_id)

#     return redirect('edit', pk=building_id)

def delete_image_building(request, building_id):
    if request.method == 'POST':
        # В зависимости от модели, возможно, нужно будет изменить код
        try:
            building = get_object_or_404(Building, pk=building_id)
            if building.image:
                building.image.delete(save=False)
                building.image = None
                building.save()
            return redirect('edit', pk=building_id)
        except Building.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return redirect('edit', pk=building_id)