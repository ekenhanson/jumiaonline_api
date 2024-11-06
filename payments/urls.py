from rest_framework.routers import DefaultRouter
from .views import BankDetailViewSet, CryptoWalletDetailViewSet

router = DefaultRouter()
router.register(r'bank-details', BankDetailViewSet)
router.register(r'crypto-wallets', CryptoWalletDetailViewSet)

urlpatterns = router.urls



# The Premium Web Hosting plan does not support ReactJS applications. For hosting ReactJS applications, you would need to use one of our VPS plans.