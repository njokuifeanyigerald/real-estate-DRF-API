import email
from itsdangerous import Serializer
from rest_framework.views import APIView
from .models import ListingModel
from rest_framework import status, response, generics, permissions
from .serializer import  ListingsSerializer
from rest_framework.generics import ListCreateAPIView


from django.contrib.postgres.search import SearchQuery, SearchVector


# a view for only realtors
class ManageListingView(APIView):
    def get(self, request):
        try:
            user = request.user
            if not user.is_realtor:
                return response.Response({'error': 'user is not a realtor'}, 
                        status=status.HTTP_403_FORBIDDEN)
            slug = request.query_params.get('slug')
            # if slug was not passed
            if not slug:
                listing=  ListingModel.objects.order_by('-date_created').filter(realtor=user.email)
                serializer = ListingsSerializer(listing, many=True)
                return response.Response({'listing':serializer.data}, status=status.HTTP_200_OK)
            if not ListingModel.objects.filter(realtor = user.email, slug=slug).exists():
                return response.Response({'error': 'Lisiting not found'}, status=status.HTTP_404_NOT_FOUND)
            
            listing  = ListingModel.objects.get(realtor=user.email, slug=slug)
            serializer = ListingsSerializer(listing)
            return response.Response({'success': serializer.data}, status=status.HTTP_200_OK)

                
        except:
            return response.Response({'error': 'something went wrong while retrieveing the list'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, format=None):
        # try:
        user = request.user

        if not user.is_realtor:
            return response.Response({'error': 'user is not a realtor'}, 
                    status=status.HTTP_403_FORBIDDEN)


        data = request.data
        title = data['title']
        slug = data['slug']
        if ListingModel.objects.filter(slug=slug):
            return response.Response({
                'error':' Listing with slug already exists'}, status=status.HTTP_400_BAD_REQUEST
            )

        address = data['address']
        city = data['city']
        state = data['state']
        zipcode = data['zipcode']
        description = data['description']

        price = data['price']
        try:
            price = int(price)
        except:
            return response.Response({'error', 'price must be an integer'},
                status=status.HTTP_400_BAD_REQUEST)

        bedrooms = data['bedrooms']
        try:
            bedrooms = int(bedrooms)
        except:
            return response.Response({'error', 'bedrooms must be a integer value'},
                status=status.HTTP_400_BAD_REQUEST)



        bathrooms = data['bathrooms']
        try:
            bathrooms = float(bathrooms)
        except:
            return response.Response({'error', 'bathrooms must be a floating value'},
                status=status.HTTP_400_BAD_REQUEST)
        if bedrooms <= 0  or bathrooms >= 10:
            bathrooms = 1.0
        
        bathrooms = round(bathrooms, 1)

        sale_type = data['sale_type']

        if sale_type == 'FOR_RENT':
            sale_type = 'For Rent'
        else:
            sale_type = 'For Sale'

        home_type = data['home_type']
        if (home_type == 'CONDO' or home_type == 
                'condo' or home_type == 'Condo'):
            home_type = 'Condo'
        elif (home_type =='TOWNHOUSE' or 
                home_type== 'townhouse' or home_type=='Townhouse'):
            home_type = 'Townhouse'
        else:
            home_type = 'House'
        
        main_photo = data['main_photo']
        photo1 = data['photo1']
        photo2 = data['photo2']
        photo3 = data['photo3']

        is_published = data['is_published']
        # tried is using isupper(), it didn't work then
        # I went old school
        if  is_published == 'true' or is_published == 'True':
            is_published = True
        else:
            is_published = False
            

        ListingModel.objects.create(

            realtor = user.email,
            title = title,
            slug=slug,
            address=address,
            city=city,
            state=state,
            zipcode = zipcode,
            description = description,
            price = price,
            bedrooms = bedrooms,
            bathrooms=bathrooms,
            sale_type = sale_type,
            home_type=home_type,
            main_photo =main_photo,
            photo1 = photo1,
            photo2 = photo2,
            photo3=photo3,
            is_published=is_published

        )
        return response.Response({'success':' Listing created successfully'}, status=status.HTTP_201_CREATED)
        
        # except:
        #     return response.Response({'error', 'something went wrong when creating listing'},
        #             status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

    
    def put(self, request, format=None):
        # try:
        user = request.user
        if not user.is_realtor:
            return response.Response({'error': 'user is not a realtor'}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data

        title = data['title']
        slugdata = data['slug']
        slug = request.query_params.get('slug')
        address = data['address']
        city = data['city']
        state = data['state']
        zipcode = data['zipcode']
        description = data['description']

        price = data['price']
        try:
            price = int(price)
        except:
            return response.Response({'error', 'price must be an integer'},
                status=status.HTTP_400_BAD_REQUEST)


        bedrooms = data['bedrooms']
        try:
            bedrooms = int(bedrooms)
        except:
            return response.Response({'error', 'bedrooms must be a integer value'},
                status=status.HTTP_400_BAD_REQUEST)

        bathrooms = data['bathrooms']
        try:
            bathrooms = float(bathrooms)
        except:
            return response.Response({'error', 'bathrooms must be a floating value'},
                status=status.HTTP_400_BAD_REQUEST)
        if bedrooms <= 0  or bathrooms >= 10:
            bathrooms = 1.0
        
        bathrooms = round(bathrooms, 1)

        sale_type = data['sale_type']

        if (sale_type == 'FOR_RENT' or sale_type=='For Rent' or sale_type == 'For_rent' or 
                sale_type == 'for rent'.isupper() or sale_type == 'for_rent'.isupper()):
            sale_type = 'For Rent'
        else:
            sale_type = 'For Sale'

        home_type = data['home_type']
        if (home_type == 'CONDO' or home_type == 
                'condo'.isupper() or home_type == 'Condo'.isupper()):
            home_type = 'Condo'
        elif (home_type =='TOWNHOUSE' or 
                home_type== 'townhouse' or home_type=='Townhouse'):
            home_type = 'Townhouse'
        else:
            home_type = 'House'
        
        main_photo = data['main_photo']
        photo1 = data['photo1']
        photo2 = data['photo2']
        photo3 = data['photo3']

        is_published = data['is_published']
        # tried is using isupper(), it didn't work then
        # I went old school
        if  is_published == 'true' or is_published == 'True':
            is_published = True
        else:
            is_published = False

        if not ListingModel.objects.filter(realtor=user.email, slug=slug).exists():
            return response.Response({'error': 'listing does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        ListingModel.objects.filter(realtor=user.email, slug=slug).update(
            title = title,
            slug=slugdata,
            address=address,
            city=city,
            state=state,
            zipcode = zipcode,
            description = description,
            price = price,
            bedrooms = bedrooms,
            bathrooms=bathrooms,
            sale_type = sale_type,
            home_type=home_type,
            main_photo =main_photo,
            photo1 = photo1,
            photo2 = photo2,
            photo3=photo3,
            is_published=is_published

        )
        return response.Response({'success':' Listing successfully updated'}, status=status.HTTP_200_OK)
        # except:
        #     return response.Response({'error', 'something went wrong when creating listing'},
        #             status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

    def patch(self, request, format=None):
        try:
            user = request.user
            if not user.is_realtor:
                return response.Response({'error', 'user is not a realtor'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            # slug = data['slug']
            slug = request.query_params.get('slug')

            is_published = data['is_published']
            if  is_published == 'true' or is_published == 'True':
                is_published = True
            else:
                is_published = False
            if not ListingModel.objects.filter(realtor=user.email, slug=slug).exists():
                return response.Response({'error': 'listing does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
            ListingModel.objects.filter(realtor=user.email, slug=slug).update(
                is_published=is_published
            )
            return response.Response({'success':' Listing publish status successfully updated'},
                        status=status.HTTP_200_OK)
        except:
            return response.Response({'error', 'something went wrong when retriveing listing'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

    def delete(self, request):
        try: 
            user = request.user
            if not user.is_realtor:
                return response.Response({'error', 'user is not a realtor'}, status=status.HTTP_403_FORBIDDEN)
            
    
            slug = request.query_params.get('slug')
            if not ListingModel.objects.filter(realtor=user.email, slug=slug).exists():
                return response.Response({'error': 'listing does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
            listing= ListingModel.objects.filter(realtor=user.email, slug=slug)
            if listing.exists():
                listing.delete()
                return response.Response({'success':' Listing  successfully deleted'},
                        status=status.HTTP_204_NO_CONTENT)
            else:
                return response.Response({'error':' failed to delete listing'},
                        status=status.HTTP_400_BAD_REQUEST)

        except:
            return response.Response({'error', 'something went wrong when retriveing listing'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

# detail view for everyone
class ListingDetailView(APIView):
    def get(self, request, format=None):
        try:
            slug = request.query_params.get('slug')

            if not slug:
                return response.Response({'error': 'Must provide slug'},status=status.HTTP_400_BAD_REQUEST)
            if not ListingModel.objects.filter(slug=slug, is_published=True).exists():
                return response.Response({'error': 'listing with this slug does not exist or not published'},
                status=status.HTTP_404_NOT_FOUND)
            listing = ListingModel.objects.get(slug=slug, is_published=True)
            serializer = ListingsSerializer(listing)

            return response.Response({'listing': serializer.data}, status=status.HTTP_200_OK)

        except:
            return response.Response({'error', 'something went wrong when retriveing listing'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


# view for everyone
class ListingsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        try:
            if not ListingModel.objects.filter(is_published=True).exists():
                return response.Response({'error': 'listing is does not exist or yet to be published'})
            listing  = ListingModel.objects.filter(is_published= True).order_by('-date_created')
            serializer = ListingsSerializer(listing, many=True)

            return response.Response({'listings': serializer.data}, status=status.HTTP_200_OK)

        except:
            return response.Response({'error', 'something went wrong when retriveing listing'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


class SearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        try:
            search = request.query_params.get('search')


            vector = SearchVector('title', 'description', 'state', 'city', 'bedrooms','bathrooms')
            query = SearchQuery(search)
            if not (ListingModel.objects.annotate(search = vector)
                        .filter(search = query,is_published = True)):
                return response.Response({'error': 'search for listings not found'}, status=status.HTTP_404_NOT_FOUND)
            listing = ListingModel.objects.annotate(
               search = vector).filter(
                search = query,
                is_published = True
            )
            serializer = ListingsSerializer(listing, many=True)
            return response.Response({'success': serializer.data}, status=status.HTTP_200_OK)
        except:
            return response.Response({'error', 'something went wrong when retriveing listing'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)  