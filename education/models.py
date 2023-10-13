from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {
    'blank': True,
    'null': True
}

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name='курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_link=models.URLField(verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                               related_name='lessons')

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name='урок'
        verbose_name_plural='уроки'


class Payments(models.Model):
    PAYMENT_METHOD = (
        ('cash', 'наличные'),
        ('card', 'по карте')
    )

    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='курс',**NULLABLE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name='урок',**NULLABLE)

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)

    payment_date=models.DateField(auto_now_add=True,verbose_name='дата оплаты')
    payment_sum=models.IntegerField(verbose_name='сумма оплаты')
    payment_method=models.CharField(max_length=50,choices=PAYMENT_METHOD,verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

