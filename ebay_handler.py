import requests
import os
import json

# Environment variables (set in Lambda console)
EBAY_OAUTH_TOKEN = os.getenv('EBAY_OAUTH_TOKEN')
BASE_URL = 'https://api.sandbox.ebay.com/sell/inventory/v1'


def create_inventory_location(oauth_token, location_details):
    """Creates an inventory location on eBay."""
    if not oauth_token:
        raise ValueError("OAuth token is missing.")

    location_key = location_details["locationKey"]
    url = f"{BASE_URL}/location/{location_key}"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Language": "en-US"
    }

    # Check if location exists first
    check_url = f"{BASE_URL}/location/{location_key}"
    try:
        check_response = requests.get(check_url, headers=headers)
        if check_response.status_code == 200:
            # Location exists, return the existing location ID
            return location_key
        elif check_response.status_code == 404:
            # Location doesn't exist, create new location
            response = requests.post(url, headers=headers, json=location_details)
            if response.status_code == 204:
                return location_key
            else:
                raise Exception(f"Error creating inventory location: {response.status_code} - {response.text}")
        else:
            raise Exception(f"Error checking location: {check_response.status_code} - {check_response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def create_inventory_item(oauth_token, item_details):
    """Creates an inventory item on eBay."""
    if not oauth_token:
        raise ValueError("OAuth token is missing.")

    sku = item_details["sku"]
    url = f"{BASE_URL}/inventory_item/{sku}"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Language": "en-US"
    }

    try:
        response = requests.put(url, headers=headers, json=item_details)
        if response.status_code in [201, 204]:
            return sku
        else:
            raise Exception(f"Error creating inventory item: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def create_offer(oauth_token, offer_details):
    """Creates an offer for an existing inventory item."""
    if not oauth_token:
        raise ValueError("OAuth token is missing.")

    url = f"{BASE_URL}/offer"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Language": "en-US"
    }

    try:
        response = requests.post(url, headers=headers, json=offer_details)
        if response.status_code == 201:
            offer_data = response.json()
            return offer_data.get('offerId', None)
        else:
            raise Exception(f"Error creating offer: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def publish_offer(oauth_token, offer_id):
    """Publishes an offer on eBay and returns the listing ID."""
    if not oauth_token:
        raise ValueError("OAuth token is missing.")

    if not offer_id:
        raise ValueError("Offer ID is missing.")

    url = f"{BASE_URL}/offer/{offer_id}/publish/"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Language": "en-US"
    }

    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            publish_data = response.json()
            return publish_data.get('listingId', None)  # Return listing ID
        else:
            raise Exception(f"Error publishing offer: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def ebay_request_processor(event, context):
    """AWS Lambda handler function."""
    if not EBAY_OAUTH_TOKEN:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: OAuth token not found.')
        }

    try:
        # Ensure event['body'] is parsed as a JSON string first if it's coming as a JSON string
        data = event['body']  # Expecting the body to be a JSON string

        location_details = data.get('locationDetails', {})
        item_details = data.get('itemDetails', {})
        offer_details = data.get('offerDetails', {})

        if not location_details or not item_details or not offer_details:
            return {
                'statusCode': 400,
                'body': json.dumps(
                    'Error: Missing location details, item details, or offer details in the event payload.')
            }

        # Create inventory location
        location_key = create_inventory_location(EBAY_OAUTH_TOKEN, location_details)

        if location_key:
            # Create inventory item
            sku = create_inventory_item(EBAY_OAUTH_TOKEN, item_details)

            if sku:
                # Add SKU to the offer details
                offer_details["sku"] = sku

                # Create the offer
                offer_id = create_offer(EBAY_OAUTH_TOKEN, offer_details)

                if offer_id:
                    listing_id = publish_offer(EBAY_OAUTH_TOKEN, offer_id)

                    if listing_id:
                        return {
                            'statusCode': 200,
                            'body': json.dumps({
                                "message": "Offer published successfully!",
                                "offerId": offer_id,
                                "listingId": listing_id
                            })
                        }
                    else:
                        return {
                            'statusCode': 400,
                            'body': json.dumps('Failed to retrieve listing ID after publishing the offer.')
                        }
                else:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Failed to create offer.')
                    }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Failed to create inventory item.')
                }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Failed to create inventory location.')
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal Server Error: {str(e)}")
        }
