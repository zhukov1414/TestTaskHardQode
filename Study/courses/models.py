from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    owner = models.ForeignKey(User, verbose_name='Владелец продукта',
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    lesson_views_count = models.PositiveIntegerField(default=0,
                                                     verbose_name='Количество'
                                                     ' просмотренных уроков')
    total_viewing_time = models.PositiveIntegerField(default=0,
                                                     verbose_name='Сумма '
                                                     'просмотров')
    student_count = models.PositiveIntegerField(default=0,
                                                verbose_name='Количество '
                                                'студентов')
    purchase_percentage = models.DecimalField(max_digits=5,
                                              decimal_places=2,
                                              default=0,
                                              verbose_name='Процент '
                                              'приобретения продукта')

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class SaveAccessProduct(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Имя пользователя')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Название продукта')
    start_date = models.DateField(verbose_name='Дата открытия доступа')
    end_date = models.DateField(blank=True,
                                null=True,
                                verbose_name='Дата закрытия доступа')

    class Meta:
        verbose_name_plural = 'Сохраненный доступ к продукту'

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class Lesson(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Имя урока')
    subject = models.ForeignKey(Product,
                                related_name='courses',
                                on_delete=models.CASCADE,
                                verbose_name='Название продукта')
    video_url = models.URLField(verbose_name='Ссылка на видеоурок')
    duration_seconds = models.PositiveIntegerField(
        verbose_name='Продолжительность урока')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    last_viewed = models.DateTimeField(null=True,
                                       blank=True,
                                       verbose_name='Дата '
                                       'последнего просмотра')

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Добавление урока'

    def __str__(self):
        return self.name


class LessonView(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Имя пользователя')
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               verbose_name='Назваине урока')
    viewing_time = models.PositiveIntegerField(default=0,
                                               verbose_name='Длительность '
                                               'просмотра')
    is_completed = models.BooleanField(default=False,
                                       verbose_name='Статус "Просмотрено"/'
                                       '"Не просмотрено"')

    class Meta:
        verbose_name_plural = 'Стасус просмотров'

    def save(self, *args, **kwargs):
        if (self.viewing_time / self.lesson.duration_seconds) >= 0.8:
            self.is_completed = True
            self.lesson.last_viewed = timezone.now()
        else:
            self.is_completed = False
        super().save(*args, **kwargs)
