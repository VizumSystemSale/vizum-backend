from fastapi import APIRouter, HTTPException
import requests
import os

router = APIRouter()

@router.post("/create_shopify_product")
async def create_shopify_product(name: str, description: str):
    try:
        shopify_access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")
        shopify_shop_name = os.getenv("SHOPIFY_SHOP_NAME")

        if not shopify_access_token or not shopify_shop_name:
            raise HTTPException(status_code=400, detail="Shopify access token or shop name not set.")

        url = f"https://{shopify_shop_name}.myshopify.com/admin/api/2023-04/products.json"

        payload = {
            "product": {
                "title": name,
                "body_html": description,
                "vendor": "Default Vendor",
                "product_type": "Generic Product",
                "tags": ["example", "shopify"]
            }
        }

        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": shopify_access_token
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=f"Shopify API error: {response.text}")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Shopify connection error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
