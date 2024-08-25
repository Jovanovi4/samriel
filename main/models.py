from django.db import models
from django.conf import settings 


class Building(models.Model):
    CATEGORY_CHOICES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('dacha', 'Дача'),
        ('land', 'Земельный участок'),
    ]
    
    TYPE_CHOICES = [
        ('1', 'Новая недвижимость'),
        ('2', 'Вторичное жильё'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    type = models.CharField('Тип недвижимости', max_length=100, choices=TYPE_CHOICES, default='1')
    title = models.CharField('Наименование объекта', max_length=255) 
    top_description = models.TextField('Текст над названием', blank=True, null=True) 
    down_description = models.TextField('Текст под названием', blank=True, null=True) 
    deadline = models.CharField('Срок сдачи', max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    image_slider = models.ImageField(blank=True, null=True, upload_to='images/')
    jarlyk = models.CharField('Ярлык', max_length=255, blank=True, null=True)
    about_before_slide = models.TextField('Описание до слайдера', blank=True, null=True)
    about_after_slide = models.TextField('Описание после слайдера', blank=True, null=True)
    category = models.CharField('Категория недвижимости', max_length=100, choices=CATEGORY_CHOICES, default='house', blank=True)
    video_name = models.CharField('Заголовок видео', max_length=255, blank=True, null=True) 
    video = models.CharField('Видео с YouTube', max_length=255, blank=True, null=True) # Ссылка на видео
    location = models.CharField('Координаты на карте', max_length=255, blank=True, null=True)
    adres = models.CharField('Адрес с текстом', max_length=255, blank=True, null=True)
    characteristic = models.CharField('Характеристика', max_length=255, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
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
