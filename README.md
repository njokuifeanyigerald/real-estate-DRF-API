# real-estate-DRF-API
built a real estate api that contains listing, users and realtor with search properties
![Screenshot (117)](https://user-images.githubusercontent.com/46121207/166107985-692bb119-e915-4635-ac48-c6ac8f654672.png)

## What is it all about
Realtors have to register and login to create a house or land for  either sell  or rent, then consumers or unthenticated users will go to the API and view each listing and can still be able to search for listings in the API.

Used djangorestframework-simplejwt to do the authentication

### This links are for authenticated users(Realtors)
![Screenshot (120)](https://user-images.githubusercontent.com/46121207/172001030-75d80747-0683-40d5-8c0e-f89be1515776.png)

### This links are for unauthenticated userss
![Screenshot (121)](https://user-images.githubusercontent.com/46121207/172001036-a9c87576-57d5-4361-af33-e43a9c4f54a1.png)

**Installation**

```xml
pipenv shell
pipenv install django djangorestframework pillow psycopg2 djangorestframework-simplejwt python-environ django-cors-headers 
```

# real-estate-DRF-API
built a real estate api that contains listing, users and realtor with search properties
![Screenshot (117)](https://user-images.githubusercontent.com/46121207/166107985-692bb119-e915-4635-ac48-c6ac8f654672.png)


remember to collectstatic

```bash
python manage.py collectstatic
```