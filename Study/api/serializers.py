from rest_framework import serializers


from courses.models import Product, LessonView, Lesson


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ('viewing_time', 'is_completed')


class LessonSerializer(serializers.ModelSerializer):
    lessonview_set = LessonViewSerializer(many=True, required=False)

    class Meta:
        model = Lesson
        fields = '__all__'
