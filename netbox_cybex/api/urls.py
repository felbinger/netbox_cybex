from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_cybex'

router = NetBoxRouter()
router.register('credential', views.CredentialViewSet)

urlpatterns = router.urls
