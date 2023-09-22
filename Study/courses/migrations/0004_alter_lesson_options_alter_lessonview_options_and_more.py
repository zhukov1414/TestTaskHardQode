# Generated by Django 4.2 on 2023-09-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_product_lesson_views_count_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Добавление урока'},
        ),
        migrations.AlterModelOptions(
            name='lessonview',
            options={'verbose_name_plural': 'Стасус просмотров'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='lesson_views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотренных уроков'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Процент приобретения продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='student_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество студентов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_viewing_time',
            field=models.PositiveIntegerField(default=0, verbose_name='Сумма просмотров'),
        ),
    ]
