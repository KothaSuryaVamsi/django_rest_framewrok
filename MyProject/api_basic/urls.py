from django.urls import path
from .views import article_list, article_details, ArticleAPIView, ArticleDetails
urlpatterns = [
    # path('article/', article_list),
    path('article/',ArticleAPIView.as_view()),
    # path('detail/<int:pk>', article_details)
    path('details/<int:id>/',ArticleDetails.as_view())
]
