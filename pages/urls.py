from django.urls import path
# from . import views
from pages.views import PagesListView, PagesDetailView, PageCreate, PageUpdate

# urlpatterns = [
#     # Esto es para vistas basadas en funciones
#     # path('', views.pages, name='pages'),
#     # path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
#     # Esto es para vistas basadas en funciones
#     # path('<int:page_id>/<slug:page_slug>/', PagesDetailView.as_view(), name='page'),
#     # Esto es para vistas basadas en clases
#     path('', PagesListView.as_view(), name='pages'),
#     path('<int:pk>/<slug:page_slug>/', PagesDetailView.as_view(), name='page'),
#     path('create/', PageCreate.as_view(), name='create'),
# ]

# Hace esto para la busqueda en reversa sea mas facil( # es un nombre cualquiera y le indicamos
# que no es una lista que es una tupla
page_patterns = ([
                     # Esto es para vistas basadas en funciones
                     # path('', views.pages, name='pages'),
                     # path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
                     # Esto es para vistas basadas en funciones
                     # path('<int:page_id>/<slug:page_slug>/', PagesDetailView.as_view(), name='page'),
                     # Esto es para vistas basadas en clases
                     path('', PagesListView.as_view(), name='pages'),
                     path('<int:pk>/<slug:page_slug>/', PagesDetailView.as_view(), name='page'),
                     path('create/', PageCreate.as_view(), name='create'),
                     path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
                 ], 'pages')
