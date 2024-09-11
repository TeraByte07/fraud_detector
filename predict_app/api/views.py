from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
from .serializers import FraudInputSerializer
import os

# Load the model and label encoder
model_path = os.path.join('ml_models', 'mlp.pkl')
model = joblib.load(model_path)

label_encoder_path = os.path.join('ml_models', 'label_encoder.pkl')
label_encoder = joblib.load(label_encoder_path)

class FraudPredictionView(APIView):
    def post(self, request):
        # Deserialize the input data
        serializer = FraudInputSerializer(data=request.data)
        
        # Check if the input data is valid
        if serializer.is_valid():
            # Extract validated data
            validated_data = serializer.validated_data
            
            # Debugging: Print valid values for the 'type' field
            print("Valid type values:", label_encoder.classes_)
            
            # Handle encoding for the 'type' field
            try:
                payment_type_encoded = label_encoder.transform([validated_data['type']])[0]
            except ValueError:
                return Response({'error': 'Invalid type value'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Prepare the data for the model
            input_data = [
                payment_type_encoded,
                validated_data['amount'],
                validated_data['oldbalanceOrg'],
                validated_data['newbalanceOrig']
            ]
            input_data = np.array(input_data).reshape(1, -1)  # Reshape for model input
            
            # Make prediction
            prediction = model.predict(input_data)
            
            # Return the prediction result
            return Response({'prediction': prediction[0]})
        
        # Return validation errors if input data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
