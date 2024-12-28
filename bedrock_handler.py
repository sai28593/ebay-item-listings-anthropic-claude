import json
import boto3

def create_product(event, context):
    # Initialize Bedrock client for model invocation
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )
    lambda_client = boto3.client('lambda')
    
    # Parse the payload from the incoming event
    request_payload = event
    
    # Extract the product title from the payload
    product_title = request_payload["body"]["itemDetails"]["product"]["title"]
    
    # Generate a prompt for the Bedrock model
    prompt = f"Write a product description for {product_title}. Do not include any extra text or backticks. Do not use inverted commas. Full description, can include eBay-supported HTML tags."
    
    # Bedrock model invocation parameters
    model_parameters = {
        "modelId": "<BEDROCK_ARN>",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 750,
            "top_k": 250,
            "stop_sequences": [],
            "temperature": 1,
            "top_p": 0.999,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    }
    
    # Invoke the Bedrock model to generate the description
    model_response = bedrock_client.invoke_model(**model_parameters)
    model_response_body = json.loads(model_response.get('body').read())
    generated_description = model_response_body.get('content')[0].get('text')
    
    # Clean up the generated description (remove newlines)
    cleaned_description = generated_description.replace("\n", " ")
    
    # Update the payload with the generated product description
    request_payload["body"]["itemDetails"]["product"]["description"] = cleaned_description
    
    # Invoke another Lambda function with the updated payload
    lambda_response = lambda_client.invoke(
        FunctionName='<ARN>',
        InvocationType="RequestResponse",
        Payload=json.dumps(request_payload)
    )
    lambda_function_response = json.load(lambda_response["Payload"])
    
    # Return the updated payload from the invoked Lambda function
    return {
        'statusCode': 200,
        'response': lambda_function_response
    }
