# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, AuctionItem, Bid
from .forms import ProductForm, AuctionItemForm
from django.utils import timezone
from decimal import Decimal

def index(request):
    products = Product.objects.all()[:3]
    auctions = AuctionItem.objects.all()[:2]
    return render(request, "index.html", {
        "products": products,
        "auctions": auctions,
    })

def wishlist_view(request):
    return render(request, "wishlist.html")

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def auction_view(request):
    auctions = AuctionItem.objects.all()
    now = timezone.now()
    return render(request, "auction.html", {
        "auctions": auctions,
        "now": now,
    })

def create_auction_item(request):
    if request.method == "POST":
        form = AuctionItemForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.start_time = timezone.now()
            auction.save()
            return redirect("auction")
    else:
        form = AuctionItemForm()
    return render(request, "new_auction_item.html", {"form": form})

def auction_item_detail(request, auction_id):
    item = get_object_or_404(AuctionItem, pk=auction_id)

    if request.method == "POST":
        # Only grab the bid_amount; bidder_name will default in the model
        bid_amount = Decimal(request.POST.get("bid_amount", "0"))
        if bid_amount > 0:
            Bid.objects.create(
                auction     = item,
                bid_amount  = bid_amount,
                timestamp   = timezone.now()
            )
        return redirect("auction_detail", auction_id=auction_id)

    bids = item.bids.all()  # uses related_name="bids"
    return render(request, "auction_item_detail.html", {
        "item": item,
        "bids": bids,
    })

def inventory_dashboard(request):
    products = Product.objects.all()
    return render(request, "inventory_dash.html", {"products": products})

def add_inventory_item(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("inventory_dashboard")
    else:
        form = ProductForm()
    return render(request, "add_inventory_item.html", {"form": form})

def edit_inventory_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("inventory_dashboard")
    else:
        form = ProductForm(instance=product)
    return render(request, "add_inventory_item.html", {"form": form})
