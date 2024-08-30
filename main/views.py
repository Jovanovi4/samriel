from django.shortcuts import render, redirect, get_object_or_404
from .models import Building, Seo, TypeChoise, Image, Plans
from .forms import BuildingForm, SeoForm, OldBuildingForm, TypeForm, ImageForm, PlansForm, ImagePlansForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




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

@login_required
def edit(request, pk=None):
    building = None
    form_class = None
    image_form_class = None
    image_p_form_class = ImagePlansForm
    plans_form_class = PlansForm
    template_name = None

    # Определение формы и шаблона на основе типа объекта
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
            template_name = 'main/edit.html'  # Можно указать дефолтный шаблон

    if request.method == 'POST' and form_class:
        # Обработка POST-запроса
        return handle_post_request(request, building, form_class, image_form_class, plans_form_class, image_p_form_class)
    
    # Обработка GET-запроса
    return handle_get_request(request, building, form_class, image_form_class, plans_form_class, image_p_form_class, template_name)


def handle_post_request(request, building, form_class, image_form_class, plans_form_class, image_p_form_class):
    # Основная форма
    form = form_class(request.POST, request.FILES, instance=building)
    image_form = image_form_class(request.POST, request.FILES)
    image_plans_form = image_p_form_class(request.POST, request.FILES)

    # Обработка планов
    plan_id = request.POST.get('plan_id')
    if plan_id:
        plan_instance = get_object_or_404(Plans, pk=plan_id, building=building)
        plans_form = plans_form_class(request.POST, instance=plan_instance)
    else:
        plans_form = plans_form_class(request.POST)

    # Флаг для проверки, заполнена ли вкладка планов
    plans_filled = False

    if plans_form.is_valid():
        # Проверка заполненности полей в plans_form
        type_building = plans_form.cleaned_data.get('type_building')
        quanty_room = plans_form.cleaned_data.get('quanty_room')
        total_area_from = plans_form.cleaned_data.get('total_area_from')
        total_area_upto = plans_form.cleaned_data.get('total_area_upto')
        price_from = plans_form.cleaned_data.get('price_from')
        price_upto = plans_form.cleaned_data.get('price_upto')
        description = plans_form.cleaned_data.get('description')

        if any([type_building, quanty_room, total_area_from, total_area_upto, price_from, price_upto, description]):
            plans_filled = True

    if form.is_valid():
        # Сохранение данных основной формы
        building = form.save(commit=False)
        building.save()

        # Обработка изображений для слайдера
        if image_form.is_valid():
            process_images(request.FILES.getlist('image_s'), building, 'image_s')

        # Обработка изображений планов
        if image_plans_form.is_valid():
            process_images(request.FILES.getlist('image_plans'), building, 'image_plans')

        # Обработка планов, если вкладка планов заполнена
        if plans_filled:
            plans = plans_form.save(commit=False)
            plans.building = building
            plans.save()

    # Перенаправление или рендеринг страницы
    return redirect('edit', pk=building.pk) if form.is_valid() else render(request, 'main/edit.html', {
        'form': form,
        'image_form': image_form,
        'plans_form': plans_form,
        'image_plans_form': image_plans_form,
        'building': building,
        'image_list': Image.objects.filter(building=building),
        'plans_list': Plans.objects.filter(building=building),
    })



def handle_get_request(request, building, form_class, image_form_class, plans_form_class, image_p_form_class, template_name):
    form = form_class(instance=building) if form_class else None
    image_form = image_form_class() if image_form_class else None
    plans_form = plans_form_class(instance=building.plans.first()) if building and building.plans.exists() else plans_form_class()
    image_plans_form = image_p_form_class() if image_p_form_class else None

    return render(request, template_name, {
        'form': form,
        'image_form': image_form,
        'plans_form': plans_form,
        'image_plans_form': image_plans_form,
        'building': building,
        'image_list': Image.objects.filter(building=building),
        'plans_list': Plans.objects.filter(building=building), 
    })

def process_images(files, building, field_name):
    for img in files:
        Image.objects.create(building=building, **{field_name: img})

# @login_required
# def edit(request, pk=None):
#     building = None
#     form_class = None
#     image_form_class = None
#     image_p_form_class = ImagePlansForm
#     plans_form_class = PlansForm  # Инициализация формы для планов
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
#         form = form_class(request.POST, request.FILES, instance=building)
#         image_form = image_form_class(request.POST, request.FILES)
#         plans_form = plans_form_class(request.POST)
#         image_plans_form = image_p_form_class(request.POST, request.FILES)

#         if form.is_valid() and image_form.is_valid() and plans_form.is_valid() and image_plans_form.is_valid():
#             building = form.save(commit=False)
#             building.save()

#             # Обработка изображений для слайдера
#             images = request.FILES.getlist('image_s')
#             for img in images:
#                 Image.objects.create(building=building, image_s=img)

#             images_plan = request.FILES.getlist('image_plans')
#             for img in images_plan:
#                 Image.objects.create(building=building, image_plans=img)


#             # Обработка планов
#             plans = plans_form.save(commit=False)
#             plans.building = building
#             plans.save()

#             return redirect('edit', pk=building.pk)
#     else:
#         form = form_class(instance=building) if form_class else None
#         image_form = image_form_class() if image_form_class else None
#         plans_form = plans_form_class(instance=building.plans.first()) if building and building.plans.exists() else plans_form_class()
#         image_plans_form = image_p_form_class() if image_p_form_class else None

#     # Получение всех изображений для конкретного объекта
#     image_list = Image.objects.filter(building=building)

#     return render(request, template_name, {
#         'form': form,
#         'image_form': image_form,
#         'building': building,
#         'image_list': image_list,
#         'plans_form': plans_form,
#         'image_plans_form' : image_plans_form
#     })


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


@login_required
def delete_plans(request, pk):
    plans = get_object_or_404(Plans, pk=pk)
    if request.method == 'POST':
        plans.delete()
        return redirect('edit', pk=plans.building.pk)
    return render(request, 'main/delete_confirm.html', {'plans': plans})

# @csrf_exempt
# @login_required
# def delete_plans(request, pk):
#     plans = get_object_or_404(Plans, pk=pk)
#     if request.method == 'POST':
#         plans.delete()
#         return redirect('edit', pk=plans.building.pk)
    
#     # В случае запроса не POST
#     return render(request, 'main/delete_confirm.html', {'plans': plans})