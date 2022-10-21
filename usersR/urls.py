from django.urls import path
from .views import homePageview, SignUpView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homePageview.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup')

]
