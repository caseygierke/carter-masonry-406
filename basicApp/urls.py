
from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ServicesPageView, PortfolioPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
]