from django.shortcuts import render, redirect, get_object_or_404
from .models import FirstScreen, Choise, Sites, Contact, Image, Logo, SeoSites
from .forms import FirstScreenForm, ChoiseForm, ContactForm, SitesForm, ImageForm, ChoiseSelectForm, SeoSitesForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from main.models import Building, TypeChoise, Image
import logging

logger = logging.getLogger(__name__)






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


@login_required
def edit(request, pk=None):
    building = None
    contact = None
    site = None
    image_form = None
    building_list = Building.objects.filter(type_choise__user=request.user)
    choise_building_form = None  # Форма для выбора недвижимости
    choise = None
    seo = None 
    

    if pk:
        # Получаем объект FirstScreen по pk
        building = get_object_or_404(FirstScreen, pk=pk)
        choise = building.choise  # Получаем связанный объект Choise
        contact = choise.contact if hasattr(choise, 'contact') else None  # Получаем связанный объект Contact (если он существует)
        site = choise.sites if hasattr(choise, 'sites') else None  # Получаем связанный объект Sites (если он существует)
        seo = getattr(choise, 'seosites', None) 
        
        # Инициализируем формы с существующими данными
        form = FirstScreenForm(instance=building)
        contact_form = ContactForm(instance=contact) if contact else ContactForm()
        site_form = SitesForm(instance=site) if site else SitesForm()
        image = site.image_icons.first() if site and site.image_icons.exists() else None
        image_form = ImageForm(instance=image) if image else ImageForm()
         # Инициализируем форму для выбора недвижимости
        choise_building_form = ChoiseSelectForm(instance=choise, user=request.user)
        seo_form = SeoSitesForm(instance=seo) if seo else SeoSitesForm()
    else:
        # Если pk не передан, создаем пустые формы
        form = FirstScreenForm()
        contact_form = ContactForm()
        site_form = SitesForm()
        image_form = ImageForm()
        choise_building_form = ChoiseSelectForm(user=request.user)
        seo_form= SeoSitesForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'choise_building_form':
            choise_building_form = ChoiseSelectForm(request.POST, instance=choise, user=request.user)
            if choise_building_form.is_valid():
                choise_building_form.save()
                choise_building_form.instance.selected_buildings.set(choise_building_form.cleaned_data['selected_buildings'])
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': choise_building_form.errors}, status=400)

        # Проверяем, является ли запрос удалением изображения для building
        if 'delete_image_general' in request.POST:
            building_id = request.POST.get('building_id')
            return delete_image_general(request, building_id)

        # Проверяем, является ли запрос удалением изображения для contact
        elif 'delete_image_contacts' in request.POST:
            contact_id = request.POST.get('contact_id')
            return delete_image_contacts(request, contact_id)
        
        # Если это не удаление, обрабатываем формы с данными из POST-запроса
        form = FirstScreenForm(request.POST, request.FILES, instance=building)
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        site_form = SitesForm(request.POST, request.FILES, instance=site)
        image_form = ImageForm(request.POST, request.FILES, instance=image) if image else ImageForm(request.POST, request.FILES)
        seo_form = SeoSitesForm(request.POST, instance=seo)


        if form.is_valid() and contact_form.is_valid() and site_form.is_valid() and image_form.is_valid() and seo_form.is_valid():
            first_screen = form.save(commit=False)
            first_screen.save()

            # Обработка формы Contact
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.choise = first_screen.choise
                contact.save()
            elif not contact:
                contact = contact_form.save(commit=False)
                contact.choise = first_screen.choise
                contact.save()

            # Обработка формы Sites
            if site_form.is_valid():
                site = site_form.save(commit=False)
                site.choise = first_screen.choise
                site.save()
            elif not site:
                site = site_form.save(commit=False)
                site.choise = first_screen.choise
                site.save()

            # Обработка формы Image
            if image_form.is_valid():
                image_contact = image_form.save(commit=False)
                image_contact.sites = site
                image_contact.save()

            if seo_form.is_valid():
                seo = seo_form.save(commit=False)
                seo.choise = first_screen.choise
                seo.save()

            return redirect('edit_s', pk=first_screen.pk)

    return render(request, 'sites/edit.html', {
        'form': form,
        'contact_form': contact_form,
        'site_form': site_form,
        'building': building,
        'contact': contact,
        'site': site,
        'choise': choise if building else None,
        'image_form': image_form,
        'buildings': building_list,
        'choise_building_form': choise_building_form,
        'seo': seo,
        'seo_form' : seo_form

    })




def landing(request, page_id):
    landing_page = get_object_or_404(FirstScreen, pk=page_id)
        # Форматирование цены с точками как разделителями тысяч
    if landing_page.price is not None:
        landing_page.price = '{:,}'.format(landing_page.price).replace(',', '.')

     # Получаем связанный объект Sites через поле choise
    site_info = getattr(landing_page.choise, 'sites', None)  # Получаем объект или None, если его нет  
    contact_info = getattr(landing_page.choise, 'contact', None)  # Получаем объект или None, если его нет    
     # Получаем выбранные объекты недвижимости из связанных с этим сайтом
    if landing_page.choise:
        building_list = landing_page.choise.selected_buildings.all()
    else:
        building_list = Building.objects.none()  # Пустой QuerySet, если нет связанного choise

    variants_list1 = landing_page.variants1.split('\n') if landing_page.variants1 else []
    variants_list2 = landing_page.variants2.split('\n') if landing_page.variants2 else []
    variants_list3 = landing_page.variants3.split('\n') if landing_page.variants3 else []

    return render(request, 'sites/landing_page.html', {
        'landing_page': landing_page ,
        'variants_list1': variants_list1,
        'variants_list2': variants_list2,
        'variants_list3': variants_list3,
        'site_info': site_info,
        'contact_info': contact_info,
        'building_list': building_list
        })


@login_required
def landing_page_building(request, page_id):
    # Получаем объект Building
    building = get_object_or_404(Building, pk=page_id)
    contacts = Contact.objects.first()
    # Получаем связанные с Building объекты Image
    images = building.images.all()  # 'images' — это related_name, если он был задан

    # Передаем оба объекта в шаблон
    return render(request, 'sites/landing_page_building.html', {
        'landing_page': building,  # Объект Building
        'images': images , # Связанные изображения
        'contacts': contacts  
    })




def delete_site(request, pk):
    choise = get_object_or_404(Choise, pk=pk, user=request.user)  # Получаем объект Choise, который принадлежит текущему пользователю
    
    if request.method == 'POST':  # Если запрос POST, значит, пользователь подтвердил удаление
        choise.delete()  # Удаляем объект
        return redirect('sites')  # Редирект на страницу со списком сайтов

    # Если запрос GET, отображаем страницу с подтверждением удаления
    return render(request, 'sites/delete_confirm.html', {'choise': choise})

@login_required
def delete_image_general(request, building_id):
    if request.method == 'POST':
        building = get_object_or_404(FirstScreen, pk=building_id)
        if building.image:
            building.image.delete(save=False)
            building.image = None
            building.save()
        return redirect('edit_s', pk=building_id)  # Замените 'edit_s' на нужное имя URL
    return redirect('edit_s', pk=building_id)  #


@login_required
def delete_image_contacts(request, contact_id):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, pk=contact_id)
        if contact.image_contacts:
            contact.image_contacts.delete(save=False)
            contact.image_contacts = None
            contact.save()
        return redirect('edit_s', pk=contact_id)  # Замените 'edit_s' на нужное имя URL
    return redirect('edit_s', pk=contact_id)  # Замените 'edit_s' на нужное имя URL


@login_required
def building_list(request):
    # Извлекаем объекты Building, связанные с пользователем
    type_choises = TypeChoise.objects.filter(user=request.user)
    buildings = Building.objects.filter(type_choise__in=type_choises)

    # Возвращаем данные в шаблон
    return render(request, 'sites/edit.html', {'buildings': buildings})