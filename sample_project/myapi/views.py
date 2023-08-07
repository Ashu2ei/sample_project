from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback

class SimplePostAPIView(APIView):

    def post(self, request):
        try:
            # Process input data (for demonstration, just echoing back the data)
            data = request.data  # Access the POST data
            x = data['value_of_x']
            y = data['value_of_y']
            output = x+y
            output = {
                "message": "Data received successfully.",
                "input_data": data,
                "output_is":output
            }

            return Response(output, status=status.HTTP_200_OK)

        except:
            traceback.print_exc()
            return Response({"error": "An error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
