from rest_framework import serializers
from batch.models import Batch, Tag, Setting, Yeast
from data_collection.models import Data
from users.models import Profile


class ProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

class YeastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yeast
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    user = ProfileSerialzer(many=False)
    tag = TagSerializer(many=True)
    yeast = YeastSerializer(many=False)
    setting = SettingSerializer(many=False)

    class Meta:
        model = Batch
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'