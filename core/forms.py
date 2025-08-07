from django import forms
from .models import Product,AuctionItem
# core/forms.py


class ProductForm(forms.ModelForm):
    # define exactly the options in your HTML
    CATEGORY_CHOICES = [
        ('Action Figures', 'Action Figures'),
        ('Lightsabers',     'Lightsabers'),
        ('Apparel',         'Apparel'),
        ('Memorabilia',     'Memorabilia'),
        ('Posters',         'Posters'),
        ('Models',          'Models'),
        ('Collectibles',    'Collectibles'),
    ]
    CONDITION_CHOICES = [
        ('new',       'New'),
        ('like-new',  'Like New'),
        ('used',      'Used'),
    ]
    AVAILABILITY_CHOICES = [
        ('available',     'Available'),
        ('out-of-stock',  'Out of Stock'),
        ('discontinued',  'Discontinued'),
    ]

    # override those fields as choice/radio
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
            'name': 'category',
        })
    )
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'space-y-2',
            'name': 'condition',
        })
    )
    availability_status = forms.ChoiceField(
        choices=AVAILABILITY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
            'name': 'availability_status',
        })
    )
    image_url = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'block w-full text-sm text-gray-300 bg-gray-800 rounded-lg border border-gray-600 cursor-pointer focus:outline-none',
            'name': 'image_url',
        }),
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'sku',
            'description',
            'category',
            'price',
            'quantity',
            'condition',
            'availability_status',
            'image_url',
            'tags',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
                'name': 'name',
                'placeholder': 'Enter item name',
            }),
            'sku': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
                'name': 'sku',
                'placeholder': 'Auto-generated or enter SKU',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none h-32',
                'name': 'description',
                'placeholder': 'Detailed description of the item',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
                'name': 'price',
                'step': '0.01',
                'placeholder': '0.00',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
                'name': 'quantity',
                'placeholder': '0',
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg text-white bg-gray-800 focus:outline-none',
                'name': 'tags',
                'placeholder': 'Enter tags separated by commas',
            }),
        }


class AuctionItemForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Action Figures', 'Action Figures'),
        ('Lightsabers',     'Lightsabers'),
        ('Apparel',         'Apparel'),
        ('Memorabilia',     'Memorabilia'),
        ('Posters',         'Posters'),
        ('Models',          'Models'),
        ('Props',           'Props'),
        ('Collectibles',    'Collectibles'),
    ]
    CONDITION_CHOICES = [
        ('mint',      'Mint'),
        ('near-mint', 'Near Mint'),
        ('good',      'Good'),
        ('fair',      'Fair'),
    ]
    DURATION_CHOICES = [
        (3, '3 Days'),
        (5, '5 Days'),
        (7, '7 Days'),
        (10,'10 Days'),
    ]
    # Overrides for dropdowns/radios/file
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md focus:ring-yellow-500 focus:border-yellow-500 text-gray-200',
            'name': 'category',
        })
    )
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md focus:ring-yellow-500 focus:border-yellow-500 text-gray-200',
            'name': 'condition',
        })
    )
    duration = forms.ChoiceField(
        choices=DURATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md focus:ring-yellow-500 focus:border-yellow-500 text-gray-200',
            'name': 'duration',
        })
    )
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md focus:ring-yellow-500 focus:border-yellow-500 text-gray-200',
            'name': 'start_time',
        })
    )
    image_url = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'block w-full text-sm text-gray-300 bg-gray-900 rounded-lg border border-gray-600 cursor-pointer focus:outline-none',
            'name': 'image_url',
        })
    )

    class Meta:
        model = AuctionItem
        fields = [
            'image_url',
            'product_name',
            'category',
            'condition',
            'description',
            'year_of_production',
            'dimensions',
            'authentication',
            'starting_bid',
            'reserve_price',
            'buy_now_price',
            'duration',
            'start_time',
            'shipping_options',
        ]
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'product_name',
                'placeholder': 'Enter item name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'description',
                'rows': 6,
            }),
            'year_of_production': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'year_of_production',
            }),
            'dimensions': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'dimensions',
            }),
            'authentication': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'authentication',
            }),
            'starting_bid': forms.NumberInput(attrs={
                'class': 'w-full pl-8 pr-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'starting_bid',
                'step': '0.01',
                'placeholder': '0.00',
            }),
            'reserve_price': forms.NumberInput(attrs={
                'class': 'w-full pl-8 pr-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'reserve_price',
                'step': '0.01',
            }),
            'buy_now_price': forms.NumberInput(attrs={
                'class': 'w-full pl-8 pr-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'buy_now_price',
                'step': '0.01',
            }),
            'shipping_options': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded-md text-gray-200 focus:outline-none',
                'name': 'shipping_options',
                'placeholder': 'e.g. Standard, Express',
            }),
        }
