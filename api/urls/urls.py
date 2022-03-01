from api.urls.jwt import jwt_urls
from api.urls.people import people_urls
from api.urls.products import products_urls
from api.urls.quotes import quotes_urls
from api.urls.yasg import yasg_urls


urlpatterns = (jwt_urls + yasg_urls + products_urls
               + people_urls + quotes_urls)
