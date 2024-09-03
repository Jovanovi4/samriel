from django.shortcuts import render, redirect, get_object_or_404
from .models import FirstScreen, Choise, Sites, Contact, Image, Logo
from .forms import FirstScreenForm, ChoiseForm, ContactForm, SitesForm, ImageForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def sites(request):
    sort_by = request.GET.get('sort', '-id')
    sites_list = Choise.objects.filter(user=request.user).order_by(sort_by)
    return render(request, 'sites/sites.html', {'sites_list': sites_list, 'sort_by': sort_by})

def add(request, pk=None):
    choise = None

    if pk:
        choise = get_object_or_404(Choise, pk=pk)
        form = ChoiseForm(instance=choise)
    else:
        form = ChoiseForm()

    if request.method == 'POST':
        form = ChoiseForm(request.POST, instance=choise)

        if form.is_valid():
            choise = form.save(commit=False)
            choise.user = request.user
            choise.save()

            if not hasattr(choise, 'firstscreen'):
                first_screen = FirstScreen.objects.create(choise=choise)

            # Редирект на страницу редактирования, используя pk нового объекта FirstScreen
            return redirect('edit_s', pk=first_screen.pk)

    return render(request, 'sites/add.html', {'form': form, 'choise': choise})


def edit(request, pk=None):
    building = None
    contact = None
    site = None
    image_form = None

    if pk:
        # Получаем объект FirstScreen по pk
        building = get_object_or_404(FirstScreen, pk=pk)
        choise = building.choise  # Получаем связанный объект Choise
        contact = choise.contact if hasattr(choise, 'contact') else None  # Получаем связанный объект Contact (если он существует)
        site = choise.sites if hasattr(choise, 'sites') else None  # Получаем связанный объект Sites (если он существует)
        
        # Инициализируем формы с существующими данными
        form = FirstScreenForm(instance=building)
        contact_form = ContactForm(instance=contact) if contact else ContactForm()
        site_form = SitesForm(instance=site) if site else SitesForm()
         # Получаем объект Image, если он существует
        image = site.image_icons.first() if site and site.image_icons.exists() else None
        image_form = ImageForm(instance=image) if image else ImageForm()
    else:
        # Если pk не передан, создаем пустые формы
        form = FirstScreenForm()
        contact_form = ContactForm()
        site_form = SitesForm()
        image_form = ImageForm()

    if request.method == 'POST':
        # Обрабатываем формы с данными из POST-запроса
        form = FirstScreenForm(request.POST, request.FILES, instance=building)
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        site_form = SitesForm(request.POST, request.FILES, instance=site)
        image_form = ImageForm(request.POST, request.FILES, instance=image) if image else ImageForm(request.POST, request.FILES)

        if form.is_valid() and contact_form.is_valid() and site_form.is_valid() and image_form.is_valid():
            first_screen = form.save(commit=False)
            first_screen.save()

            # Обработка формы Contact
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.choise = first_screen.choise
                contact.save()
            else:
                # Если Contact форма невалидна, создаем новый объект Contact
                if not contact:
                    contact = contact_form.save(commit=False)
                    contact.choise = first_screen.choise
                    contact.save()

            # Обработка формы Sites
            if site_form.is_valid():
                site = site_form.save(commit=False)
                site.choise = first_screen.choise
                site.save()

                                # Обработка формы Image
                if image_form.is_valid():
                    image_contact = image_form.save(commit=False)
                    image_contact.sites = site
                    image_contact.save()
            else:
                # Если Sites форма невалидна, создаем новый объект Sites
                if not site:
                    site = site_form.save(commit=False)
                    site.choise = first_screen.choise
                    site.save()
            

            return redirect('edit_s', pk=first_screen.pk)

    return render(request, 'sites/edit.html', {
        'form': form,
        'contact_form': contact_form,
        'site_form': site_form,
        'building': building,
        'contact': contact,
        'site': site,
        'choise': choise,
        'image_form': image_form,
    })



def landing(request, page_id):
    landing_page = get_object_or_404(FirstScreen, pk=page_id)
        # Форматирование цены с точками как разделителями тысяч
    if landing_page.price is not None:
        landing_page.price = '{:,}'.format(landing_page.price).replace(',', '.')

    variants_list1 = landing_page.variants1.split('\n') if landing_page.variants1 else []
    variants_list2 = landing_page.variants2.split('\n') if landing_page.variants2 else []
    variants_list3 = landing_page.variants3.split('\n') if landing_page.variants3 else []

    return render(request, 'sites/landing_page.html', {
        'landing_page': landing_page ,
        'variants_list1': variants_list1,
        'variants_list2': variants_list2,
        'variants_list3': variants_list3
        })


def delete_image_contacts(request, contacts_id):
    if request.method == 'POST':
        try:
            # Получаем объект Contact по ID
            contact = get_object_or_404(Contact, pk=contacts_id)
            
            # Проверяем, есть ли изображение у объекта
            if contact.image_contacts:
                # Удаляем файл изображения с файловой системы
                contact.image_contacts.delete(save=False)
                
                # Устанавливаем поле image_contacts в None, чтобы удалить ссылку на файл
                contact.image_contacts = None
                
                # Сохраняем изменения
                contact.save()
            
            # Возвращаем пользователя на страницу редактирования
            return redirect('edit_s', pk=contacts_id)
        
        except Contact.DoesNotExist:
            # Возвращаем JSON ответ с ошибкой, если объект не найден
            return JsonResponse({'status': 'error', 'message': 'Contact not found'}, status=404)
    
    # Перенаправляем на страницу редактирования, если запрос не POST
    return redirect('edit_s', pk=contacts_id)


def delete_image_general(request, building_id):
    if request.method == 'POST':
        try:
            # Получаем объект Contact по ID
            building = get_object_or_404(FirstScreen, pk=building_id)
            
            # Проверяем, есть ли изображение у объекта
            if building.image:
                # Удаляем файл изображения с файловой системы
                building.image.delete(save=False)
                
                # Устанавливаем поле image_contacts в None, чтобы удалить ссылку на файл
                building.image = None
                
                # Сохраняем изменения
                building.save()
            
            # Возвращаем пользователя на страницу редактирования
            return redirect('edit_s', pk=building_id)
        
        except Contact.DoesNotExist:
            # Возвращаем JSON ответ с ошибкой, если объект не найден
            return JsonResponse({'status': 'error', 'message': 'Contact not found'}, status=404)
    
    # Перенаправляем на страницу редактирования, если запрос не POST
    return redirect('edit_s', pk=building_id)
