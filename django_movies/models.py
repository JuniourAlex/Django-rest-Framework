from django.db import models
from datetime import datetime
from django.urls import reverse

class Category(models.Model):
    """ Категории """
    name = models.CharField('Категория', max_length=200)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    """ Актёры и Режиссёры """
    name = models.CharField( 'Имя', max_length=250)
    age = models.PositiveSmallIntegerField('Возраст', default = 0)
    image = models.ImageField('Фото', upload_to='actors/')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёры и Режиссеры'
        verbose_name_plural = 'Актёры и Режиссеры'

class Genre(models.Model):
    """ Жанры """
    name = models.CharField( 'Имя', max_length=250)
    descriription = models.TextField('Описание')




    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movies(models.Model):
    """ Фильмы """
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    posts = models.ImageField(upload_to= 'posters/')
    year = models.PositiveIntegerField('Выход Фильма', default=2020)
    country = models.CharField('Страна' , max_length=30)
    actors = models.ManyToManyField(Actor, max_length=200, verbose_name='Актёры')
    genres = models.ManyToManyField(Genre, verbose_name="жанр")
    budget = models.PositiveIntegerField('Бюджет', help_text='Введите значение в долларах',default=0)
    fees_in_world = models.PositiveIntegerField('Сборы в Мире',help_text='Введите значение в долларах')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null = True, verbose_name= 'Категория')
    url = models.SlugField(max_length=150, unique = True)


    def get_absolute_url(self,**kwargs):
        return reverse('movie_detail', {'slug': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class RatingStar(models.Model):
        value = models.PositiveIntegerField('Значение', default=0)

        def __str__(self):
            return self.value


        class Meta:
            verbose_name = 'Рейтинг'
            verbose_name_plural = 'Рейтинги'



class Rating(models.Model):

    ip = models.CharField('ip клиента', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name = 'Звезда')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name = 'Фильм')


    def __str__(self):
        return f'{self.star} - {self.movie}'


    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'



class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField('Имя' , max_length=150)
    title = models.TextField('Сообщение')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,verbose_name = 'Фильм',related_name='reviews')


    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

