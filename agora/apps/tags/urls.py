from django.urls import path

from agora.apps.tags import views

urlpatterns = [
    path('',
         views.TagListView.as_view(),
         name='tag-list'),
    path('<slug:slug>/',
         views.TagDetailView.as_view(),
         name='tag-detail'),
    path('<slug:slug>/delete/',
         views.TagDeleteView.as_view(),
         name='tag-delete'),
]
