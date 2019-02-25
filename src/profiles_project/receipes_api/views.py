from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# Create your views here.


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'aloha Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        print("*"*100)
        print("THE DATA: {0}".format(request.data))
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})


class ReceipeApiView(APIView):
    """Test API View."""

    serializer_class = serializers.ReceipeSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = {"title": "Fruit Salad",
                      "ingredients": [
                          {"name": "apple", "image": "https://azure.com/apple",
                           "portion": {"amount": 1, "type": "Unit"}},
                          {"name": "pineapple", "image": "https://azure.com/pineapple",
                           "portion": {"amount": 0.5, "type": "Cup"}},
                          {"name": "Sour cream", "image": "https://azure.com/sour_cream",
                           "portion": {"amount": 1, "type": "Cup"}},
                          {"name": "Almonds", "image": "https://azure.com/almonds",
                           "portion": {"amount": 0.5, "type": "Cup"}},
                          {"name": "Lechera", "image": "https://azure.com/lechera",
                           "portion": {"amount": 1, "type": "Can"}}
                      ],
                      "instructions": ["add fruit", "mix sour cream",
                                       "mix lechera", "add the almonds"],
                      "image": "https://azure.com/fruit_salad"
                      }

        return Response({'message': 'Hello!', 'an_apiview hi': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        print(models.Portion.objects.all())

        _receipe = {"title": "Fruit Salad",
                    "ingredients": [
                        {"name": "apple", "image": "https://azure.com/apple",
                         "portion": {"amount": 1, "type": "Unit"}},
                        {"name": "pineapple", "image": "https://azure.com/pineapple",
                         "portion": {"amount": 0.5, "type": "Cup"}},
                        {"name": "Sour cream", "image": "https://azure.com/sour_cream",
                         "portion": {"amount": 1, "type": "Cup"}},
                        {"name": "Almonds", "image": "https://azure.com/almonds",
                         "portion": {"amount": 0.5, "type": "Cup"}},
                        {"name": "Lechera", "image": "https://azure.com/lechera",
                         "portion": {"amount": 1, "type": "Can"}}
                    ],
                    "instructions": ["add fruit", "mix sour cream",
                                     "mix lechera", "add the almonds"],
                    "image": "https://azure.com/fruit_salad"
                    }

        receipe = models.Receipe(
            title=_receipe["title"],
            image=_receipe["image"])
        receipe.save()

        portion = models.Portion(amount=1.5, portion_type="cup")
        portion.save()

        ingredient = models.Ingredient(
            name="apple", image="http://azure.com/apple", portion=portion)
        ingredient.save()

        ingredients = models.IngredientList(
            list_id=receipe, ingredient=ingredient)
        ingredients.save()

        instruction = models.Instruction(instruction="Add the apple")
        instruction.save()

        instructions = models.InstructionList(
            list_id=receipe, instruction=instruction)
        instructions.save()

        print(receipe)
        print("*"*100)
        return Response({'message': "aloha"})
        # print("THE DATA: {0}".format(request.data))
        # serializer = serializers.ReceipeSerializer(data=request.data)

        # if serializer.is_valid():
        #     name = serializer.data.get('name')
        #     message = 'Hello {0}'.format(name)
        #     return Response({'message': message})
        # else:
        #     return Response(
        #         serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})


class IngredientApiView(APIView):
    """Test API View."""

    serializer_class = serializers.IngredientSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        if 'id' in request.GET:

            ingredients = models.Ingredient.objects.filter(
                pk=int(request.GET['id']))

            if len(ingredients) > 0:
                ingredient = ingredients[0]
                ingredient = {
                    'ingredient': ingredient.name,
                    'image': ingredient.image,
                    'portion': {
                        'amount': ingredient.portion.amount,
                        'portion_type': ingredient.portion.portion_type}
                }
                return Response(ingredient)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            ingredient = {"name": "apple", "image": "https://azure.com/apple",
                          "portion": 1}

            portion = models.Portion.objects.get(pk=int(ingredient["portion"]))

            return Response({'ingredient': ingredient, 'amount': portion.amount, 'type': portion.portion_type})

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.IngredientSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            image = serializer.data.get('image')
            portion_id = serializer.data.get('portion')

            if models.Portion.objects.filter(pk=int(portion_id)).exists():
                portion = models.Portion.objects.get(pk=int(portion_id))

                ingredient = models.Ingredient(
                    name=name, image=image, portion=portion)
                print(ingredient)
                ingredient.save()

                return Response({"name": ingredient.name, "image": ingredient.image,
                                 "portion": ingredient.portion.pk})

            else:
                return Response('Portion not found', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        print('pk: {0}'.format(pk))
        print('the thing: {0}'.format(request.data))
        return Response({'method': 'delete', 'pk': pk})


class ReceipesViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.ReceipeList

    def list(self, request):
        """Return a hello message."""

        receipes = [
            {"title": "Fruit Salad",
             "ingredients": [
                 {"name": "apple", "image": "https://azure.com/apple",
                  "portion": {"amount": 1, "type": "Unit"}},
                 {"name": "pineapple", "image": "https://azure.com/pineapple",
                  "portion": {"amount": 0.5, "type": "Cup"}},
                 {"name": "Sour cream", "image": "https://azure.com/sour_cream",
                  "portion": {"amount": 1, "type": "Cup"}},
                 {"name": "Almonds", "image": "https://azure.com/almonds",
                  "portion": {"amount": 0.5, "type": "Cup"}},
                 {"name": "Lechera", "image": "https://azure.com/lechera",
                  "portion": {"amount": 1, "type": "Can"}}
             ],
                "instructions": ["add fruit", "mix sour cream",
                                 "mix lechera", "add the almonds"],
                "image": "https://azure.com/fruit_salad"
             }
        ]

        return Response({'receipes': receipes})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.ReceipeList(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        print(request.data)
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
