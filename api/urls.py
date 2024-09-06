from django.urls import path
from .views import MyUserDetailView
from .views import MyUserListView
from .views import HomeownerDetailView
from .views import HomeownerListView
from .views import SupplierDetailView
from .views import SupplierListView
from .views import MaterialDetailView
from .views import MaterialListView
from .views import BrandDetailView
from .views import BrandListView

urlpatterns = [
    path("myusers/", MyUserListView.as_view(), name = "myuser_list_view"),
    path("myuser/<int:id>/", MyUserDetailView.as_view(), name = "myuser_detail_view"),
    path("homeowners/", HomeownerListView.as_view(), name = "homeowner_list_view"),
    path("homeowner/<int:id>/", HomeownerDetailView.as_view(), name = "homeowner_detail_view"),
    path("suppliers/", SupplierListView.as_view(), name = "supplier_list_view"),
    path("supplier/<int:id>/", SupplierDetailView.as_view(), name = "supplier_detail_view"),
    path("materials/", MaterialListView.as_view(), name = "material_list_view"),
    path("material/<int:id>/", MaterialDetailView.as_view(), name = "material_detail_view"),
    path("brands/", BrandListView.as_view(), name = "brand_list_view"),
    path("brand/<int:id>/", BrandDetailView.as_view(), name = "brand_detail_view"),
]