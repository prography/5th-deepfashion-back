from rest_framework import serializers
from .models import PostImage, Clothing, PostImage, CodiList


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class CodiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodiList
        fields = "__all__"



class ClothingSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)

    class Meta:
        model = Clothing
        fields = "__all__"

    def create(self, validated_data):
        clothing_image = self.context.get("view").request.FILES
        instance = self.Meta.model.objects.create(**validated_data)
        try:
            instance.img = clothing_image['img']
        except:
            pass
        return instance

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret["images"] = ImageSerializer(instance.images.all(), many=True).data
    #     ret["clothing"] = instance.pk
    #     return ret
