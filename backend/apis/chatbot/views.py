# chatbot/views.py
# Import necessary modules and libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests
from django.conf import settings
from difflib import get_close_matches

@api_view(['POST'])
def chatbot_response(request):
    # Check if the 'message' key exists in the request data
    if 'message' not in request.data:
        return Response({'error': 'No message provided'}, status=400)

    try:
        # Extract the user message from the request data
        user_message = request.data['message']
        print(f"Received user message: {user_message}")

        # Load FAQs from the faqs.json file
        with open('d:/New folder/backend/apis/chatbot/faqs.json', 'r') as f:
            faqs = json.load(f)['faqs']
        print("Checking FAQs...")

        # Check if the user message matches any FAQ exactly
        for faq in faqs:
            print(f"Checking FAQ: {faq['question']}")
            if user_message.lower() == faq['question'].lower():
                print("Match found in FAQs.")
                return Response({'reply': faq['answer']}, status=200)

        # Use fuzzy matching to find approximate matches in FAQs
        faq_questions = [faq['question'] for faq in faqs]
        close_matches = get_close_matches(user_message.lower(), [q.lower() for q in faq_questions], n=1, cutoff=0.8)

        if close_matches:
            matched_question = close_matches[0]
            matched_faq = next(faq for faq in faqs if faq['question'].lower() == matched_question)
            print("Fuzzy match found in FAQs.")
            return Response({'reply': matched_faq['answer']}, status=200)

        print("No match found in FAQs. Querying OpenRouter API...")

        # Prepare the payload for querying the OpenRouter API
        openrouter_url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            'Authorization': '',
            'Content-Type': 'application/json',
            'HTTP-Referer': 'https://flumers.com',
            'X-Title': 'Flumers Assistant'
        }
        payload = {
            'model': 'deepseek/deepseek-r1-0528:free',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant for Flumers platform. Always refer to the brand as "Flumers.AI" and avoid any variations like "Flume".'},
                {'role': 'user', 'content': user_message}
            ]
        }

        # Debugging: Print the payload being sent to the API
        print(f"Payload: {payload}")

        # Send the request to the OpenRouter API
        response = requests.post(openrouter_url, headers=headers, json=payload)
        print(f"OpenRouter API response status: {response.status_code}")
        print(f"OpenRouter API response data: {response.text}")

        # Check if the API response is in JSON format
        if response.headers.get('Content-Type') == 'application/json':
            response_data = response.json()

            # Extract the chatbot reply if the response is valid
            if response.status_code == 200 and 'choices' in response_data:
                bot_reply = response_data['choices'][0]['message']['content']
                print("OpenRouter API returned a valid response.")
                return Response({'reply': bot_reply}, status=200)
            else:
                print("Failed to get a valid response from OpenRouter API.")
                return Response({'error': 'Failed to get a response from OpenRouter', 'details': response_data}, status=500)
        else:
            print("OpenRouter API did not return JSON.")
            print(f"Response headers: {response.headers}")
            print(f"Response text: {response.text}")

            # Provide a detailed error message for non-JSON responses
            return Response({
                'error': 'OpenRouter API did not return JSON',
                'details': response.text,
                'suggestion': 'The API might be down or the request might be incorrect. Please check the API status or your request payload.'
            }, status=500)

    except Exception as e:
        # Handle any exceptions that occur during processing
        print(f"Error during chatbot response: {str(e)}")
        return Response({'error': 'Failed to process message', 'details': str(e)}, status=500)
