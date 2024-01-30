from django.db import models


class Info(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    subtitle_ru = models.CharField(max_length=255)
    subtitle_uz = models.CharField(max_length=255)
    subtitle_en = models.CharField(max_length=255)

    about_ru = models.TextField()
    about_uz = models.TextField()
    about_en = models.TextField()

    address_ru = models.TextField()
    address_uz = models.TextField()
    address_en = models.TextField()

    telegram = models.CharField('telegram | ssilka qo\'yish kerak', max_length=255)
    instagram = models.CharField('instagram | ssilka qo\'yish kerak', max_length=255)
    youtube = models.CharField('youtube | ssilka qo\'yish kerak', max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    pdf = models.FileField(upload_to='catalog/')

    def __str__(self):
        return '{} - info model'.format(self.pk)

    class Meta:
        verbose_name = 'Главная информация'
        verbose_name_plural = 'Главные информации'


class Project(models.Model):
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    description_ru = models.TextField()
    description_uz = models.TextField()
    description_en = models.TextField()

    image = models.ImageField(upload_to='projects/', blank=True)

    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class FeedBack(models.Model):
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=13)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='certificates/', blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Branch(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Objects(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='objects/', blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Trust(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='trusts/', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нам доверяют'
        verbose_name_plural = 'Нам доверяют'
