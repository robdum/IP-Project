from api.src.constants.enums.rating_enum import RatingEnum
from api.src.models.base_model import BaseModel
from api.src.models.category_model import CategoryModel
from rest_framework import serializers
from django.db import models


class TipAndTrickModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    average_rating = models.FloatField(default=RatingEnum.UNAVAILABLE.value)
    number_of_ratings = models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)


class TipAndTrickSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipAndTrickModel
        fields = ('id', 'title', 'description', 'average_rating', 'number_of_ratings', 'category', 'date_created', 'date_modified')
