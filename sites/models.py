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
    DEFAULT_IMAGE = 'images/default_image.jpg'

    choise = models.OneToOneField(Choise, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images/', default=DEFAULT_IMAGE)
    name = models.CharField('Имя сайта', max_length=255, blank=True, default='Город в Самаре')
    title = models.CharField('Заголовок сайта', max_length=255, blank=True, default='Купить квартиру в новостройках Самары') 
    category = models.CharField('Категория недвижимости', max_length=100, choices=CATEGORY_CHOICES, default='apartment', blank=True)
    prefix = models.CharField('Префикс цены', max_length=100, choices=PREFIX_CHOICES, default='2', blank=True)
    price = models.IntegerField('Цена объекта', blank=True, null=True, default=6800000)
    question1 = models.CharField('Вопрос №1', max_length=255, blank=True, default='какое количество комнат необходимо?')
    variants1 = models.TextField('Варианты №1', blank=True, null=True, default='Студия\n1 комнатная\n2 комнатная\n3 комнатная\n4 и более')
    question2 = models.CharField('Вопрос №2', max_length=255, blank=True, default='какой район вы рассматриваете?')
    variants2 = models.TextField('Варианты №2', blank=True, null=True, default='Любой район\nКуйбышевский район\nЛенинский район\nЖелезнодорожный район\nОктябрьский район\nСоветский район\nПромышленный район')
    question3 = models.CharField('Вопрос №3', max_length=255, blank=True, default='какой бюджет планируете на покупку?')
    variants3 = models.TextField('Варианты №3', blank=True, null=True, default='около 4 млн.\nдо 4,5 млн.\nдо 5 млн.\nдо 5,5 млн.\nдо 6 млн.\nдо 6,5 млн.\nболее 7 млн.')
    question4 = models.CharField('Вопрос №4', max_length=255, blank=True)
    variants4 = models.TextField('Варианты №4', blank=True, null=True)

    def __str__(self):
        return self.prefix


class Contact(models.Model):
    DEFAULT_IMAGE = 'profile_images_contact/default_image.jpg'


    choise = models.OneToOneField(Choise, on_delete=models.CASCADE)
    image_contacts = models.ImageField(blank=True, null=True, upload_to='profile_images_contact/', default=DEFAULT_IMAGE)
    tg_link = models.CharField('Ссылка Telegram', max_length=255, blank=True, default='t.me/') 
    whatsapp = models.CharField('WhatsApp', max_length=255, blank=True, default='+79229988776') 
    description = models.TextField('', blank=True, null=True, default='Здравствуйте. Интересует покупка квартиры!')
    number = models.CharField('Номеp', max_length=255, blank=True, default='+79229988776') 
    vk_link = models.CharField('Ссылка на VK', max_length=255, blank=True, null=True)
    instagram_link = models.CharField('Ссылка на YouTube Канал', max_length=255, blank=True, null=True)
    youtube_link = models.CharField('Ссылка на Instagram', max_length=255, blank=True, null=True)



class Logo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image_icons = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name or "Logo {}".format(self.id)

class Sites(models.Model):
    choise = models.OneToOneField(Choise, on_delete=models.CASCADE)
    name = models.CharField('Название компании', max_length=255, default='Без названия')
    number = models.CharField('Номеp', max_length=255, blank=True, default='+79229988776') 
    decoding = models.CharField('Расшифровка', max_length=255, blank=True, default='агентство недвижимости')
    text_under_number = models.CharField('Подпись под номером', max_length=255, blank=True, default='с 9.00 до 20.00')
    link = models.CharField('Ссылка', max_length=255, blank=True)
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True, blank=True)



class Image(models.Model):
    DEFAULT_IMAGE = 'profile_images_contact/free-icon-user-219983.png'
    sites = models.ForeignKey(Sites, on_delete=models.CASCADE, related_name='image_icons')
    image_icons = models.ImageField(blank=True, null=True, upload_to='icon_images/', default=DEFAULT_IMAGE)

