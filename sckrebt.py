import requests # type: ignore
import ssl
import socket
from urllib.parse import urlparse

def check_security(url):
    results = {}
    
    # التأكد من أن الرابط يبدأ بـ http/https
    if not url.startswith('http'):
        url = 'https://' + url

    try:
        # 1. فحص الـ SSL
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                results['ssl_enabled'] = True
        
        # 2. فحص الـ Security Headers
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        results['x_frame_options'] = 'X-Frame-Options' in headers
        results['content_security_policy'] = 'Content-Security-Policy' in headers
        results['server_info'] = headers.get('Server', 'Not Exposed')
        
    except Exception as e:
        return {"error": str(e)}

    return results

# تجربة السكربت
target = "google.com"
print(check_security(target))
import requests # type: ignore
import ssl
import socket
from urllib.parse import urlparse

# ... (الكود اللي كتبته أنت موجود هنا، اتركه كما هو) ...

# ضيف هذا الجزء تحت في نهاية الملف:
if __name__ == "__main__":
    target_url = "google.com" # هنا تقدر تغير الموقع اللي تريد تفحصه
    results = check_security(target_url)
    print("--- نتيجة الفحص ---")
    print(results)