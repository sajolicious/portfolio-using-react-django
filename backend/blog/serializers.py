from .models import blog,contact
from rest_framework import serializers
class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields=('id','title','description')

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields=['name','email','subject','subject']