from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_credentials'

router = NetBoxRouter()
router.register('credentials', views.CredentialViewSet)

urlpatterns = router.urls
