from django.urls import path,include
from .views import ContactList,ContactDetail,SearchResultsView,HomePageView

urlpatterns = [
    path('list',ContactList.as_view()),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('',HomePageView.as_view()),
    path('<int:pk>',ContactDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]