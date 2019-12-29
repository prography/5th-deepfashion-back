from rest_framework import serializers
from .models import PostImage, Clothing, PostImage, CodiList, FileModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class CodiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodiList
        fields = "__all__"


class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = "__all__"


class ClothingSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)

    class Meta:
        model = Clothing
        fields = "__all__"

    def create(self, validated_data):
        print("VALIDATED DATA", validated_data)
        clothing_image = self.context.get("view").request.FILES
        print(clothing_image, 'clothing IMAGAKLGASDLFKKA;SDFLK')
        instance = self.Meta.model.objects.create(**validated_data)
        instance.img = clothing_image['img']
        return instance

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret["images"] = ImageSerializer(instance.images.all(), many=True).data
    #     ret["clothing"] = instance.pk
    #     return ret
