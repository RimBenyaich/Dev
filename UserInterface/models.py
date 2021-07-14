from djongo import models

# Create your models here

class DFModel(models.Model):
    ids = models.BigIntegerField() # min: 1000102, max: 9900000190, mean: 4580533745.265966
    date = models.CharField(max_length=20) # max length was 15
    price = models.IntegerField() # min: 75000, max: 7700000, mean: 540112.8428359866
    bedrooms = models.PositiveSmallIntegerField() # min: 0, max: 33, mean: 3.3710199925953352
    bathrooms = models.FloatField() # min: 0.0, max: 8.0, mean: 2.114934283598667
    sqft_living = models.PositiveSmallIntegerField() # min: 290, max: 13540, mean: 2080.053822658275
    sqft_lot = models.IntegerField() # min: 520, max: 1651359, mean: 15107.306368011847
    floors = models.FloatField() # min: 1.0, max: 3.5, mean: 1.4944002221399482
    waterfront = models.PositiveSmallIntegerField() # min: 0, max: 1, mean: 0.007543502406516105
    view = models.FloatField() # min: 0.0, max: 4.0, mean: 0.23421880784894483
    condition = models.PositiveSmallIntegerField() # min: 1, max: 5, mean: 3.409339133654202
    grade = models.PositiveSmallIntegerField() # min: 1, max: 13, mean: 7.656978896704924
    sqft_above = models.FloatField() # min: 290.0, max: 9410.0, mean: 1788.5032395409107
    sqft_basement = models.PositiveSmallIntegerField() # min: 0, max: 4820, mean: 291.55058311736394
    yr_built = models.PositiveSmallIntegerField() # min: 1900, max: 2015, mean: 1971.010181414291
    yr_renovated = models.FloatField() # min: 0.0, max: 2015.0, mean: 84.42178822658275
    zipcode = models.FloatField() # min: 98001.0, max: 98199.0, mean: 98077.94719548315
    lat = models.FloatField() # min: 47.1559, max: 47.7776, mean: 47.560068220103666
    longi = models.FloatField() # min: -122.519, max: -121.315, mean: -122.21389323398739
    sqft_living15 = models.PositiveSmallIntegerField() # min: 399, max: 6210, mean: 1986.641475379489
    sqft_lot15 = models.IntegerField() # min: 651, max: 871200, mean: 12768.911329137356
