from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Home
    path("", views.index, name="index"),

    # Products
    path("products/", views.products_view, name="products"),

    # Wishlist (static)
    path("wishlist/", views.wishlist_view, name="wishlist"),

    # Auctions
    path("auction/", views.auction_view, name="auction"),
    path("auction/new/", views.create_auction_item, name="create_auction_item"),
    path("auction/<int:auction_id>/", views.auction_item_detail, name="auction_detail"),

    # Inventory
    path("inventory/", views.inventory_dashboard, name="inventory_dashboard"),
    path("inventory/add/", views.add_inventory_item, name="add_inventory_item"),
    path("inventory/<int:pk>/edit/", views.edit_inventory_item, name="edit_inventory_item"),
]

# In DEBUG mode, serve media files through Django
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
