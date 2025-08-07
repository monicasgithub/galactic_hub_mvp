from django.db import models

class Product(models.Model):
    name                = models.CharField(max_length=100)
    sku                 = models.CharField(max_length=100)
    description         = models.TextField()
    category            = models.CharField(max_length=100)
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    quantity            = models.IntegerField()
    condition           = models.CharField(max_length=50)
    availability_status = models.CharField(max_length=50)
    image_url           = models.ImageField(
                              upload_to="images/",
                              blank=True,
                              help_text="Upload product image"
                          )
    tags                = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class AuctionItem(models.Model):
    product_name       = models.CharField(max_length=100)
    category           = models.CharField(max_length=100)
    condition          = models.CharField(max_length=100)
    description        = models.TextField()
    year_of_production = models.CharField(max_length=4)
    dimensions         = models.CharField(max_length=100)
    authentication     = models.CharField(max_length=100)
    starting_bid       = models.DecimalField(max_digits=10, decimal_places=2)
    reserve_price      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    buy_now_price      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration           = models.IntegerField(help_text="Duration in days")
    start_time         = models.DateTimeField()
    shipping_options   = models.CharField(max_length=255)
    image_url          = models.ImageField(
                             upload_to="images/",
                             blank=True,
                             help_text="Upload auction item image"
                         )

    def __str__(self):
        return self.product_name


class Bid(models.Model):
    auction      = models.ForeignKey(
                       AuctionItem,
                       related_name="bids",
                       on_delete=models.CASCADE
                   )
    bidder_name  = models.CharField(
                       max_length=100,
                       default="Default User",
                       help_text="Name of the bidder (defaults for MVP)"
                   )
    bid_amount   = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.bidder_name} – ${self.bid_amount}"
