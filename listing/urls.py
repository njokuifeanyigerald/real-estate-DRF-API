from django.urls import path
from .views import ManageListingView,ListingDetailView,ListingsView,SearchView


urlpatterns = [
    path('',ManageListingView.as_view(), name='ManageListingView' ),
    path('details/',ListingDetailView.as_view(), name='details' ),
    path('listings/', ListingsView.as_view(), name='listings'),
    path('search/', SearchView.as_view(), name='search')
   
]