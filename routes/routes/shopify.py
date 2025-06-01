from fastapi import APIRouter, HTTPException
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter()

@router.post("/create_shopify_product")
async def create_shopify_product(name: str, description: str):
    try:
        shopify_api_key = os.getenv("SHOPIFY_API_KEY")
        shopify_password = os.getenv("SHOPIFY_PASSWORD")
        shopify_shop_name = os.getenv("SHOPIFY_SHOP_NAME")

        if not all([shopify_api_key, shopify_password, shopify_shop_name]):
            raise HTTPException(status_code=400, detail="Shopify credentials are not properly set.")

        # Ensure the API version is up-to-date
        url = f"https://{shopify_shop_name}.myshopify.com/admin/api/2023-04/products.json"

        payload = {
            "product": {
                "title": name,
                "body_html": description,
                "vendor": "Default Vendor",  # Update as needed
                "product_type": "Generic Product",  # Update as needed
                "tags": ["example", "shopify"]
            }
        }

        headers = {"Content-Type": "application/json"}
        auth = (shopify_api_key, shopify_password)
        response = requests.post(url, json=payload, headers=headers, auth=auth)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=f"Shopify API error: {response.text}")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Shopify connection error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
