from django.contrib import admin


from courses.models import (Product,
                            SaveAccessProduct,
                            Lesson,
                            LessonView)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'owner',
                    'lesson_views_count',
                    'total_viewing_time',
                    'student_count',
                    'purchase_percentage']
    verbose_name = "Продукт"
    verbose_name_plural = "Продукты"


@admin.register(SaveAccessProduct)
class SaveAccessProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    verbose_name = "Доступ к продуктам"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'subject',
                    'video_url',
                    'duration_seconds',
                    'created',
                    'last_viewed']
    verbose_name = 'Урок'
    verbose_name_plural = 'Уроки'


@admin.register(LessonView)
class LessonViewAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'lesson',
                    'viewing_time',
                    'is_completed']
