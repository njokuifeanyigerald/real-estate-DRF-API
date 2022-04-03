from django.db import models


class ListingModel(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Townhouse'

    realtor = models.EmailField(max_length=300)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sale_type = models.CharField(max_length=20, choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=20, choices=HomeType.choices, default=HomeType.HOUSE)
    main_photo = models.ImageField(upload_to='listing/')
    photo1 = models.ImageField(upload_to='listing/')
    photo2 = models.ImageField(upload_to='listing/')
    photo3 = models.ImageField(upload_to='listing/')
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


    # so we can delete the actual data like the images
    # in the database
    def delete(self):
        self.main_photo.storge.delete(self.main_photo.name)
        self.photo1.storge.delete(self.photo1.name)
        self.photo2.storge.delete(self.photo2.name)
        self.photo3.storge.delete(self.photo3.name)

        super().delete()


    def __str__(self):
        return self.title

