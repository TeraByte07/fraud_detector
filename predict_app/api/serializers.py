from rest_framework import serializers

class FraudInputSerializer(serializers.Serializer):
    type = serializers.CharField()  # Ensure this field matches your input
    amount = serializers.FloatField()
    oldbalanceOrg = serializers.FloatField()
    newbalanceOrig = serializers.FloatField()
