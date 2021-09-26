from django.db.models import fields
import first_app
from rest_framework import serializers
from first_app.models import Student, College, Album, Track

"""
## validators
def name_startwith_R(data):
        if data[0].lower() == 'r':
                return data
        else:
                raise serializers.ValidationError(" Name  not starting with R/r")

class StudentSerializer(serializers.Serializer):
        # id = serializers.IntegerField()
        name = serializers.CharField(max_length=100, validators= [name_startwith_R])
        age = serializers.IntegerField()
        city = serializers.CharField(max_length=100)
        marks = serializers.IntegerField()

        def create(self, validated_data):
                stud = Student.objects.create(**validated_data)
                return stud

        def update(self, instance, validated_data):
                instance.name = validated_data.get("name", instance.name)              ## if name is not sent,  
                instance.age = validated_data.get("age", instance.age)                        ## old instance name is maintened
                instance.city = validated_data.get("city")
                instance.marks = validated_data.get("marks")
                instance.save()
                return instance

        ###  field validations---------

        def validate_age(self, value):
                if value > 21:
                        return value
                else:
                        raise serializers.ValidationError(" Age should be more than 21 years")

        ## object level validations

        def validate(self, data):
                print("in validate method")
                if (data.get("city") == "Mumbai") and (data.get("age") > 21):
                        return data
                        
"""

##  model Serializer------------------

class StudentSerializer(serializers.ModelSerializer):                ## models from models 
        class Meta:
                model = Student
                # fields = ('name' , 'age' , 'city', 'marks' )               # marks not req so not written
                fields = '__all__'                                              # all
                # exclude = ["id", "marks"]
                # read_only_fields = ["name"]

                def validate_age(self, value):
                        if value > 21:
                                return value
                        else:
                                raise serializers.ValidationError(" Age should be more than 21 years")

class CollegeSerializer(serializers.ModelSerializer):
        class Meta:
                model = College
                fields = '__all__'
                

### Serializer relations

class TrackSerializer(serializers.ModelSerializer):
        class Meta:
                model = Track
                fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
        # tracks = serializers.StringRelatedField(many = True)
        # tracks= serializers.PrimaryKeyRelatedField(many =True, read_only= True)
        # tracks= serializers.HyperlinkedRelatedField(many=True,read_only= True, view_name='track-detail')
        # tracks= serializers.SlugRelatedField(many =True, read_only= True, slug_field='title')

        ## nested serializer by other serializer
        tracks= TrackSerializer(many= True, read_only= True)
        class Meta:
                model = Album
                fields = '__all__'

# class TrackSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = Track
#                 fields = '__all__'