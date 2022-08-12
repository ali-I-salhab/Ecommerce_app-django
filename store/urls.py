



from rest_framework_nested import routers
from rest_framework import renderers

from . import views


router =routers.DefaultRouter()

router.register(prefix='products',viewset= views.ProductListWithClass)

router.register(prefix='collections',viewset= views.collection_list)

products_router=routers.NestedDefaultRouter(router,'products',lookup='products')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews')




urlpatterns = router.urls+products_router.urls
