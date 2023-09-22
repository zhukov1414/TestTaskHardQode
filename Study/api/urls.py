from django.urls import path


from api.views import (ProductAPIView,
                       LessonListView,
                       ProductLessonsAPIView,
                       LessonDetailView)

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(),
         name='lesson-detail'),
    path('product/<int:product_id>/', ProductLessonsAPIView.as_view(),
         name='product-lessons'),
    path('product/<int:product_id>/lessons/<int:pk>/',
         LessonDetailView.as_view(),
         name='lesson-detail')
]
