"""

from django.core.management.base import BaseCommand
from core.models import Product, AuctionItem
from django.utils import timezone

class Command(BaseCommand):
    help = "Load initial products and auctions"

    def handle(self, *args, **kwargs):

        # --- Products (9 total) ---
        sample_products = [
            {"name": "Darth Vader Helmet",               "price": 299,   "img": "/static/images/darthvaderhelmet.png"},
            {"name": "Limited Edition Lightsaber",       "price": 149,   "img": "/static/images/lightsaber.png"},
            {"name": "Star Wars: A New Hope Movie Poster","price": 39,    "img": "/static/images/poster.png"},
            {"name": "Millennium Falcon Model",          "price": 89,    "img": "/static/images/milleniumfalcon2.png"},
            {"name": "Stormtrooper Armor Set",            "price": 499,   "img": "/static/images/stormtrooperarmor.png"},
            {"name": "Master Yoda Figurine",              "price": 49,    "img": "/static/images/yoda.png"},
            {"name": "Death Star Blueprints",             "price": 29,    "img": "/static/images/deathstar.png"},
            {"name": "R2-D2 Interactive Replica",         "price": 199,   "img": "/static/images/r2d2.png"},
            {"name": "Jedi Master Robe",                  "price": 79,    "img": "/static/images/jedirobe.png"},
        ]
        for p in sample_products:
            Product.objects.create(
                name=p["name"],
                sku=p["name"][:3].upper(),
                description=f"Authentic merchandise: {p['name']}",
                category="Collectibles",
                price=p["price"],
                quantity=5,
                condition="new",
                availability_status="available",
                image_url=p["img"],
                tags="star wars"
            )

        # --- Auctions (7 total: 4 active + 3 upcoming) ---
        sample_auctions = [
            # Active auctions
            {"name": "Vintage Luke Skywalker Lightsaber", "starting": 2450,  "img": "/static/images/lightsaber.png"},
            {"name": "Darth Vader Helmet Replica",       "starting": 8750,  "img": "/static/images/darthvaderhelmet.png"},
            {"name": "Millennium Falcon Model",          "starting": 5200,  "img": "/static/images/milleniumfalcon.png"},
            {"name": "Princess Leia Figure (Mint)",      "starting": 1890,  "img": "/static/images/leiafigurine.png"},
            # Upcoming auctions
            {"name": "Death Star Ultimate Collector",     "starting": 15000, "img": "/static/images/deathstarmodel.png"},
            {"name": "Boba Fett Helmet (Screen Used)",    "starting": 25000, "img": "/static/images/bobafetthelmet.png"},
            {"name": "Interactive R2-D2 Droid",           "starting": 8500,  "img": "/static/images/r2d2.png"},
        ]
        for a in sample_auctions:
            AuctionItem.objects.create(
                product_name=a["name"],
                category="Props",
                condition="mint",
                description=f"Limited auction for {a['name']}",
                year_of_production="2023",
                dimensions="10×10×10",
                authentication="Certified",
                starting_bid=a["starting"],
                reserve_price=None,
                buy_now_price=None,
                duration=7,
                start_time=timezone.now(),
                shipping_options="Standard",
                image_url=a["img"],
            )

        self.stdout.write(self.style.SUCCESS("Sample data loaded."))
"""
from django.core.management.base import BaseCommand
from core.models import Product, AuctionItem
from django.utils import timezone

class Command(BaseCommand):
    help = "Load initial products and auctions"

    def handle(self, *args, **kwargs):
        # Only load once
        if Product.objects.exists() or AuctionItem.objects.exists():
            self.stdout.write(self.style.NOTICE("Sample data already present; skipping."))
            return

        # --- Products (9 total) ---
        sample_products = [
            {"name": "Darth Vader Helmet",               "price": 299,   "img": "/static/images/darthvaderhelmet.png"},
            {"name": "Limited Edition Lightsaber",       "price": 149,   "img": "/static/images/lightsaber.png"},
            {"name": "Star Wars: A New Hope Movie Poster","price": 39,    "img": "/static/images/poster.png"},
            {"name": "Millennium Falcon Model",          "price": 89,    "img": "/static/images/milleniumfalcon2.png"},
            {"name": "Stormtrooper Armor Set",           "price": 499,   "img": "/static/images/stormtrooperarmor.png"},
            {"name": "Master Yoda Figurine",             "price": 49,    "img": "/static/images/yoda.png"},
            {"name": "Death Star Blueprints",            "price": 29,    "img": "/static/images/deathstar.png"},
            {"name": "R2-D2 Interactive Replica",        "price": 199,   "img": "/static/images/r2d2.png"},
            {"name": "Jedi Master Robe",                 "price": 79,    "img": "/static/images/jedirobe.png"},
        ]
        for p in sample_products:
            Product.objects.create(
                name=p["name"],
                sku=p["name"][:3].upper(),
                description=f"Authentic merchandise: {p['name']}",
                category="Collectibles",
                price=p["price"],
                quantity=5,
                condition="new",
                availability_status="available",
                image_url=p["img"],
                tags="star wars"
            )

        # --- Auctions (7 total: 4 active + 3 upcoming) ---
        sample_auctions = [
            # Active auctions
            {"name": "Vintage Luke Skywalker Lightsaber", "starting": 2450,  "img": "/static/images/lightsaber.png"},
            {"name": "Darth Vader Helmet Replica",       "starting": 8750,  "img": "/static/images/darthvaderhelmet.png"},
            {"name": "Millennium Falcon Model",          "starting": 5200,  "img": "/static/images/milleniumfalcon.png"},
            {"name": "Princess Leia Figure (Mint)",      "starting": 1890,  "img": "/static/images/leiafigurine.png"},
            # Upcoming auctions
            {"name": "Death Star Ultimate Collector",     "starting": 15000, "img": "/static/images/deathstarmodel.png"},
            {"name": "Boba Fett Helmet (Screen Used)",    "starting": 25000, "img": "/static/images/bobafetthelmet.png"},
            {"name": "Interactive R2-D2 Droid",           "starting": 8500,  "img": "/static/images/r2d2.png"},
        ]
        for a in sample_auctions:
            AuctionItem.objects.create(
                product_name=a["name"],
                category="Props",
                condition="mint",
                description=f"Limited auction for {a['name']}",
                year_of_production="2023",
                dimensions="10×10×10",
                authentication="Certified",
                starting_bid=a["starting"],
                reserve_price=None,
                buy_now_price=None,
                duration=7,
                start_time=timezone.now(),
                shipping_options="Standard",
                image_url=a["img"],
            )

        self.stdout.write(self.style.SUCCESS("Sample data loaded."))
