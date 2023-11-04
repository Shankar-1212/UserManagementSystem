from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from firebase_admin import auth, firestore,credentials
import firebase_admin
from datetime import datetime
import requests
import json
from django.http import JsonResponse
#crfm exempt
from django.views.decorators.csrf import csrf_exempt
# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/shankar/Downloads/backend-12-7d89a-firebase-adminsdk-ij7va-b6b7482766.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    full_name = request.data.get('full_name')
    username = request.data.get('username')

    try:
        # Create a user in Firebase Authentication
        user = auth.create_user(email=email, password=password)

        # Store user information in Firestore
        user_ref = db.collection('users').document(user.uid)
        user_ref.set({
            'email': email,
            'full_name': full_name,
            'username': username,
            'created_at': datetime.now()
        })

        return Response({'message': 'User registered successfully'})
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        api_key = ""  # Replace with your actual Firebase API key
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            print("Received email:", email)
            print("Received password:", password)
        if not email or not password:
            return JsonResponse({"error": "Email and password are required."}, status=400)

        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        response = requests.post(rest_api_url, params={"key": api_key}, json=payload)
    
        if response.status_code == 200:
            return Response(response.json().get('idToken'))

        else:
            error_message = response.json().get('error', {}).get('message', 'Authentication failed.')
            return JsonResponse({"error": error_message}, status=response.status_code)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

@api_view(['POST'])
def retrieve_user_profile(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_email = data.get('email')  # Get the user email from the request body

            if user_email:
                users_ref = db.collection('users')
                query = users_ref.where('email', '==', user_email).limit(1)
                user_data = [doc.to_dict() for doc in query.stream()]

                if user_data:
                    profile_data = {
                        'email': user_data[0].get('email'),
                        'full_name': user_data[0].get('full_name'),
                        'username': user_data[0].get('username')
                        # Include other profile information from the Firestore document
                    }
                    return JsonResponse(profile_data)
                else:
                    return JsonResponse({'error': 'User profile not found'}, status=404)
            else:
                return JsonResponse({'error': 'Email not provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in the request body'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
