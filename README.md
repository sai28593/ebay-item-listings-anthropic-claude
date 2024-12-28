# Serverless Framework: eBay Item Listings with Anthropic Claude  

This project demonstrates the use of the Serverless Framework to create eBay item listings by integrating Anthropic Claude for AI-powered content generation.  

---

## **Development Setup**  

Follow the steps below to set up your development environment:  

### Prerequisites  

1. **Install Python**  
   - Ensure Python 3.8.5 or above is installed.  
   - [Download Python](https://www.python.org/downloads/).  

2. **Install AWS CLI**  
   - Follow the [official AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).  
   - Configure AWS CLI credentials:  
     - Use [Option #2 from AWS Well-Architected Labs](https://wellarchitectedlabs.com/common/documentation/aws_credentials/#cli).  
     - Example:  
       ```
       Access Key: <AWS Access Key>  
       Secret Key: <AWS Secret Key>
       Default Region: us-east-1  
       Output Format: json  
       ```  

3. **Install NVM**  
   - Use the [NVM installation guide](https://www.freecodecamp.org/news/node-version-manager-nvm-install-guide/) to install Node Version Manager.  

4. **Install Serverless Framework**  
   - Run the following command to install Serverless globally:  
     ```bash
     npm install -g serverless@3.39.0  
     ```  

---

## **Deployment Steps**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo-name/ebay-item-listings  
   cd ebay-item-listings  

2. Install dependencies:

      ```
      bash
      npm install
      ```
  
3. Deploy the application:
    ```
    bash
    serverless deploy  
    ```

4. Upon successful deployment, you’ll see output similar to:
    ```
    bash
    Deploying ebay-item-listings to stage dev (us-east-1)  
    ✔ Service deployed to stack ebay-item-listings-dev (112s)  
    functions:  
      createListing: ebay-item-listings-dev-createListing (2 kB)
    ```
  
### Usage

Create eBay Item Listings
Invoke the function locally for testing:
bash
serverless invoke local --function createListing --data '{"itemDetails": {"title": "Sample Product", "description": "A great item!"}}'  
Invoke the deployed function:
bash
serverless invoke --function createListing --data '{"itemDetails": {"title": "Sample Product", "description": "A great item!"}}'  
Expected output:
json
{
    "statusCode": 200,
    "body": "{\"message\": \"Item listing created successfully!\", \"listingId\": \"123456789\"}"
}
Dependencies and Plugins
To include third-party Python dependencies for this project, install the serverless-python-requirements plugin:

Install the plugin:

bash
Copy code
serverless plugin install -n serverless-python-requirements  
Add dependencies to a requirements.txt file. For example:

txt
Copy code
anthropic  
boto3  
The dependencies will be bundled with the Lambda package during the deployment process.

