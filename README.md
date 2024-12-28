# eBay Item Listings with Anthropic Claude and AWS

Welcome to the **eBay Item Listings Project**, an open-source solution that simplifies marketplace listing creation using the power of **Anthropic Claude** and **eBay APIs**, all hosted on **AWS Lambda** and **Bedrock**. This repository demonstrates how AI and cloud services can work together to automate repetitive tasks, saving time and effort for sellers and businesses.

## Problem Statement
Creating eBay marketplace listings is often a time-consuming and manual process. Sellers need to write item descriptions, ensure compliance with eBay's formatting requirements, and manage API integrations for publishing listings. This project addresses these challenges by:

- Automating the generation of optimized item descriptions.
- Streamlining the process of creating, listing, and publishing items.
- Reducing the overall time and effort required for marketplace operations.

## Solution Overview
This project integrates **Anthropic Claude**, an advanced generative AI model, with eBay's API using **AWS Lambda** and **Bedrock**. Key features include:

- **AI-Powered Description Generation**: Generates high-quality, platform-compliant item descriptions using Anthropic Claude.
- **eBay API Integration**: Automates workflows for creating items, listing offers, and publishing listings.
- **Cloud Hosting**: Fully hosted on AWS Lambda and Bedrock for scalability and reliability.

## Features
- **Automated Text Generation**: Quickly generates descriptive content that meets eBay's standards.
- **Seamless API Workflows**: End-to-end integration with eBay API for item creation, offers, and publishing.
- **Scalable Infrastructure**: Leverages AWS Lambda for serverless computing and Bedrock for AI model deployment.

## Key Contributors
- **Sai (Architect and Original Contributor)**: Designed and implemented the overall architecture, combining AI and cloud services.
- **Geethika**: Led eBay API integration, focusing on creating items, listing offers, and publishing workflows.
- **Rakesh**: Developed Bedrock-powered solutions for generating item descriptions and invoking eBay API for item creation.

## Getting Started
### Prerequisites
1. **AWS Account**: Set up AWS Lambda and Bedrock services.
2. **eBay Developer Account**: Obtain eBay API credentials.
3. **Node.js or Python**: Required for running scripts and managing dependencies.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/sai28593/ebay-item-listings-anthropic-claude.git
   cd ebay-item-listings-anthropic-claude
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Configure environment variables:
   Create a `.env` file with the following:
   ```env
   EBAY_APP_ID=<your-ebay-app-id>
   EBAY_CERT_ID=<your-ebay-cert-id>
   EBAY_DEV_ID=<your-ebay-dev-id>
   AWS_REGION=<your-aws-region>
   BEDROCK_ENDPOINT=<your-bedrock-endpoint>
   ```

### Usage
1. **Deploy to AWS Lambda**:
   Use the deployment script or AWS CLI to upload the code to your Lambda function.
   ```bash
   npm run deploy
   ```
2. **Invoke the Function**:
   Use AWS Lambda's console or CLI to invoke the function and generate eBay listings:
   ```bash
   aws lambda invoke --function-name CreateEbayListing output.json
   ```
3. **Test the Integration**:
   Run sample tests to verify eBay API integration and text generation.

### Sample Input
```json
{
  "itemTitle": "Wireless Headphones",
  "itemCategory": "Consumer Electronics",
  "itemPrice": 99.99,
  "itemCondition": "New"
}
```

### Sample Output
```json
{
  "listingId": "1234567890",
  "status": "Published",
  "description": "Brand-new wireless headphones with crystal-clear audio quality and long-lasting battery life. Perfect for everyday use."
}
```

## How It Works
1. **Generate Descriptions**: Bedrock invokes Anthropic Claude to create optimized item descriptions.
2. **Integrate with eBay**: AWS Lambda uses eBay API to create the item, list the offer, and publish it.
3. **End-to-End Automation**: Fully automated pipeline minimizes manual intervention.

## Contributing
We welcome contributions! If you'd like to enhance this project, please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed descriptions of your changes.

## License
This project is licensed under the [MIT License](LICENSE).

## Feedback and Support
For questions, feedback, or issues, please open an issue on GitHub or reach out to me directly.

---

Happy coding! Let’s make marketplace listings smarter and faster. 🎉
