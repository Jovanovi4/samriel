from django.db import models
from django.conf import settings 


class Choise(models.Model):
    TYPE_CHOICES = [
        ('1', 'Комплексы (ЖК, Коттеджные поселки)'),
        ('2', 'Отдельные объекты (Вторичка, частные объявления)'),
        ('3', 'Сайт отдельного ЖК'),
    ]

    CATEGORY_CHOICES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Наименование объекта', max_length=255) 
    type = models.CharField('Тип недвижимости', max_length=100, choices=TYPE_CHOICES, default='1')
    category = models.CharField('Категория недвижимости', max_length=100, choices=CATEGORY_CHOICES, default='house', blank=True)


class FirstScreen(models.Model):
    CATEGORY_CHOICES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
    ]
    PREFIX_CHOICES = [
        ('1', ''),
        ('2', 'от'),
        ('3', 'до'),
    ]

    choise = models.OneToOneField(Choise, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    name = models.CharField('Имя сайта', max_length=255)
    title = models.CharField('Заголовок сайта', max_length=255, blank=True) 
    category = models.CharField('Категория недвижимости', max_length=100, choices=CATEGORY_CHOICES, default='house', blank=True)
    prefix = models.CharField('Префикс цены', max_length=100, choices=PREFIX_CHOICES, default='2', blank=True)
    price = models.IntegerField('Цена объекта', blank=True, null=True)
    question1 = models.CharField('Вопрос №1', max_length=255, blank=True)
    variants1 = models.TextField('Варианты №1', blank=True, null=True)
    question2 = models.CharField('Вопрос №2', max_length=255, blank=True)
    variants2 = models.TextField('Варианты №2', blank=True, null=True)
    question3 = models.CharField('Вопрос №3', max_length=255, blank=True)
    variants3 = models.TextField('Варианты №3', blank=True, null=True)
    question4 = models.CharField('Вопрос №4', max_length=255, blank=True)
    variants4 = models.TextField('Варианты №4', blank=True, null=True)


class Contact(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    tg_link = models.CharField('Ссылка Telegram', max_length=255, blank=True) 
    whatsapp = models.CharField('WhatsApp', max_length=255, blank=True) 
    description = models.TextField('', blank=True, null=True)
    number = models.CharField('Номеp', max_length=255, blank=True) 
    vk_link = models.TextField('', blank=True, null=True)
    instagram_link = models.TextField('', blank=True, null=True)
    youtube_link = models.TextField('', blank=True, null=True)


class Sites(models.Model):
    name = models.CharField('Название компании', max_length=255)
    number = models.CharField('Номеp', max_length=255, blank=True) 
    decoding = models.CharField('Расшифровка', max_length=255, blank=True)
    text_under_number = models.CharField('Подпись под номером', max_length=255, blank=True)
    link = models.CharField('Ccskrf', max_length=255, blank=True)