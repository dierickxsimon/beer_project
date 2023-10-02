from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET' : '/api/projects'},
        {'GET' : '/api/projects/id'},
        {'POST' : '/api/projects/id/vote'},

        {'POST' : '/api/users/token'},
        {'POST' : '/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['get'])
def getAllBatches(request):
    batches = Batch.objects.all()
    serializer = BatchSerializer(batches, many=True)

    return Response(serializer.data)

@api_view(['get'])
def getAllTags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)

    return Response(serializer.data)



@api_view(['POST'])
def getSelectedBatch(request):
    if 'id' not in request.data:
        return Response({'error': 'Please provide an "id" in the request body.'}, status=status.HTTP_400_BAD_REQUEST)
    id = request.data['id']

    try:
        batch = Batch.objects.get(id=id)
        serializer = BatchSerializer(batch)
        return Response(serializer.data)
    except Batch.DoesNotExist:
        return Response({'error': 'Batch not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['get'])   
def getActiveBatch(request):
    batch = Batch.objects.filter(is_selected=True).first()
    serializer = BatchSerializer(batch, many=False)
    return Response(serializer.data)
    

@api_view(['POST'])
def getBatchStreams(request):
    if 'id' not in request.data :
        return Response({'error': 'Please provide an "id" in the request body.'}, status=status.HTTP_400_BAD_REQUEST)
    
    id = request.data['id']

    try:
        data = Data.objects.filter(batch=id).order_by('-created')
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)
    except Data.DoesNotExist:
        return Response({'error': 'Data not found.'}, status=status.HTTP_404_NOT_FOUND)
   

@api_view(['POST'])
def uploadData(request):
    try:

        batch_id = request.data['batch']
        batch = Batch.objects.get(id=batch_id)

        set_temprature = request.data['set_temprature']
        temprature = request.data['temprature']
        fridge = request.data['fridge']
        warm_element = request.data['warm_element']

        data = Data.objects.create(
            set_temprature=set_temprature,
            temprature=temprature,
            fridge=fridge,
            warm_element=warm_element,
            batch=batch
        )


        serializer = DataSerializer(data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Batch.DoesNotExist:
        return Response({'error': 'Batch not found.'}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        return Response({'error': f'Missing field: {e}'}, status=status.HTTP_400_BAD_REQUEST)