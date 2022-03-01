from api.urls.jwt import jwt_urls
from api.urls.yasg import yasg_urls


urlpatterns = (jwt_urls + yasg_urls)
