from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
    path('liked/<int:pk>/<slug:slug>', views.like_post, name='like_post'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
