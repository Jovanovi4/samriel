from django.shortcuts import render, redirect, get_object_or_404
from .models import FirstScreen, Choise
from .forms import FirstScreenForm, ChoiseForm
from django.contrib.auth.decorators import login_required


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

    if pk:
        building = get_object_or_404(FirstScreen, pk=pk)
        form = FirstScreenForm(instance=building)
    else:
        form = FirstScreenForm()

    if request.method == 'POST':
        form = FirstScreenForm(request.POST, request.FILES, instance=building)
        if form.is_valid():
            first_screen = form.save(commit=False)
            first_screen.save()
            return redirect('landing', page_id=first_screen.pk)

    return render(request, 'sites/edit.html', {'form': form, 'building': building})




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
