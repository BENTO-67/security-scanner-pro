import requests # pyright: ignore[reportMissingModuleSource]

def check_security(url):
    if not url.startswith("http"):
        url = "https://" + url
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        h = response.headers
        
        results = {
            "ssl_enabled": url.startswith("https"),
            "x_frame_options": "X-Frame-Options" in h,
            "content_security_policy": "Content-Security-Policy" in h,
            "recommendations": []
        }
        
        if not results["x_frame_options"]:
            results["recommendations"].append("ثغرة XFO: يُنصح بضبط الهيدر لمنع الـ Clickjacking.")
        if not results["content_security_policy"]:
            results["recommendations"].append("ثغرة CSP: يفضل تفعيل سياسة أمان المحتوى.")
        if not results["recommendations"]:
            results["recommendations"].append("الموقع يبدو جيداً من حيث الهيدرات الأساسية.")
            
        return results
    except Exception as e:
        return {"error": "تعذر الاتصال، الموقع محمي أو الرابط خاطئ."}