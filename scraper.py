import requests
from supabase import create_client, Client

# مفاتيح التشغيل الخاصة بك
SCRAPERAPI_KEY = "57da298d183935eb8b6ff3b9d9677739"
SUPABASE_URL = "https://hlgatfhjhzzykwkpift.supabase.co"
SUPABASE_KEY = "sb_secret_PtSZbIw8pMo-Lh-dZEKHOg_RIKf9iZ6"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def test_supabase_connection():
    print("جاري اختبار الاتصال بقاعدة البيانات وحفظ منتج تجريبي...")
    
    sample_product = {
        "asin": "B08N5WRWNW",
        "title": "منتج تجريبي من أمازون ريسيل",
        "price": "1500 EGP",
        "condition": "Like New",
        "image_url": "https://m.media-amazon.com/images/I/example.jpg",
        "product_url": "https://www.amazon.eg/-/en/s?k=warehouse"
    }
    
    try:
        res = supabase.table("products").upsert(sample_product).execute()
        print("✅ تم ربط وحفظ البيانات في Supabase بنجاح!", res)
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاتصال بـ Supabase: {e}")

if __name__ == "__main__":
    test_supabase_connection()
