from django.conf.urls  import url , include
from .views import Register
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'register', Register)

urlpatterns = [
    url('', include(router.urls)),
]