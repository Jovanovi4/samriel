from django.db import models
from django.conf import settings 



class TypeChoise(models.Model):
    TYPE_CHOICES = [
        ('1', 'Комплексы (ЖК, Коттеджные поселки)'),
        ('2', 'Отдельные объекты (Вторичка, частные объявления)'),
    ]

    CATEGORY_CHOICES = [
        ('1', 'Квартира'),
        ('2', 'Дом'),
    ]

    type_choise = models.CharField('Тип недвижимости', max_length=100, choices=TYPE_CHOICES, default='1')
    category = models.CharField('Категория недвижимости', max_length=100, choices=CATEGORY_CHOICES, default='1')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)



class Building(models.Model):
    CATEGORY_CHOISE = [
        ('1', 'Квартира'),
        ('2', 'Дом'),   
        ('3', 'Дача'),
        ('4', 'Земельный участок'),
    ]
    
    type_choise = models.ForeignKey(TypeChoise, on_delete=models.CASCADE)
    title = models.CharField('Наименование объекта', max_length=255, blank=True, null=True, default="Без названия") 
    top_description = models.CharField('Текст над названием', max_length=255, blank=True, null=True) 
    down_description = models.CharField('Текст под названием', max_length=255, blank=True, null=True) 
    deadline = models.CharField('Срок сдачи', max_length=255, blank=True, null=True)
    description1 = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Главное фото объекта', blank=True, upload_to='images/')
    jarlyk = models.CharField('Ярлык', max_length=255, blank=True, null=True)
    about_before_slide = models.TextField('Описание до слайдера', blank=True, null=True)
    about_after_slide = models.TextField('Описание после слайдера', blank=True, null=True)
    category = models.CharField('Категория недвижимости', max_length=100, choices=CATEGORY_CHOISE, default='1', blank=True)
    video_name = models.CharField('Заголовок видео', max_length=255, blank=True, null=True) 
    video = models.CharField('Видео с YouTube', max_length=255, blank=True, null=True)
    location = models.CharField('Координаты на карте', max_length=255, blank=True, null=True)
    adres = models.CharField('Адрес с текстом', max_length=255, blank=True, null=True)
    characteristic = models.CharField('Характеристика', max_length=255, blank=True, null=True)
    description2 = models.TextField('Описание', blank=True, null=True)
    advantages = models.CharField('Преимущество', max_length=255, blank=True, null=True)
    deteil_description = models.TextField('Детальное описание', blank=True, null=True)
    square = models.IntegerField('Площадь', blank=True, null=True)
    floor = models.IntegerField('Этаж', blank=True, null=True) 
    all_floor = models.IntegerField('Всего этажей', blank=True, null=True)
    price = models.IntegerField('Цена объекта', blank=True, null=True)

    def __str__(self):
        return self.title


class Seo(models.Model):
    building = models.OneToOneField(Building, on_delete=models.CASCADE)
    name = models.CharField('Назване страницы', max_length=255, blank=True, null=True)
    url_link = models.CharField('URL', max_length=255, blank=True, null=True)
    deskription_seo = models.TextField('Описание', blank=True, null=True)
    key_word = models.TextField('Ключевые слова', blank=True, null=True)

    def __str__(self):
        return self.name or "Без названия"


class Image(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='images')
    image_s = models.ImageField(blank=True, upload_to='slyder_images/')