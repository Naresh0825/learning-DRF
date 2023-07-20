# from rest_framework import serializers
# from book_api.models import Book

# class BookSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField(max_length=100)
#     number_of_pages=serializers.IntegerField()
#     published_date=serializers.DateTimeField()
#     quantity=serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)
    
#     def update(self, instance, data):
#         instance.title=data.get("title",instance.title)
#         instance.number_of_pages=data.get("number_of_pages",instance.number_of_pages)
#         instance.published_date=data.get("published_date",instance.published_date)
#         instance.quantity=data.get("quantity",instance.quantity)

#         instance.save()
#         return instance

from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

    def validate_title(self, value):
        if value=="Diet Coke":
            raise ValidationError("No Diet Coke please")
        return value
    
    def validate(self, data):
        if data["number_of_pages"]>500 and data["quantity"]>200:
            raise ValidationError("Too heay for inventory")
        return data
