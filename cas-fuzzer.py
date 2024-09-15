import requests
import urllib3
import time
import sys
import argparse

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-u", "--url", type=ascii, help="base URL for CAS application", required=True)
    argParser.add_argument("-m", "--mode", type=ascii, help="mode to use", required=True)
    argParser.add_argument("-f", "--fuzz", type=ascii, help="fuzz string to use for fuzz", required=False)
    argParser.add_argument("-l", "--log", help="log output to a file",  action="store_true")
    argParser.add_argument("-v", "--verbose", help="verbose output",  action="store_true")
    args = argParser.parse_args()

    urllib3.disable_warnings()

    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    ##  Downgrade SSL level - required for some IdPs
    #requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'DEFAULT@SECLEVEL=1'

    target_url = args.url.replace("'", "")
    mode = args.mode.replace("'", "")

    if(mode == "fuzz"):
        if(args.fuzz is None):
            sys.exit('Fuzz string required for fuzz mode')
        else:
            fuzz_str = args.fuzz.replace("'", "")
    else:
        sys.exit('Fuzz string required for fuzz mode')

    base_url = target_url + "/login?service="        

    #print("base_url = " + base_url)

    test_urls = [
        'http://www.google.com',                    # Does the IdP accept a fake HTTP SP?
        'https://www.google.com',                   # Does the IdP accept a fake HTTPS SP?
        'http://www.google.com/' + fuzz_str,        # What if we append the fuzz string? (HTTP)
        'https://www.google.com/' + fuzz_str,       # What if we append the fuzz string? (HTTPS)
        'http://' + fuzz_str,                       # HTTP fuzz string
        'https://' + fuzz_str,                      # HTTPS fuzz string
        'http://www.' + fuzz_str,                   # HTTP www.fuzz string
        'https://www.' + fuzz_str,                  # HTTPS www.fuzz string
        'http://subdomain.' + fuzz_str,             # Test for HTTP subdomains
        'https://subdomain.' + fuzz_str             # Test for HTTPS subdomains
    ]

    valid_urls = []

    print("[*] Testing SP URL list")

    for test_url in test_urls:
        #print("[*] Testing SP URL: " + test_url)
        print('.', end='', flush=True)
        result = requests.get(base_url + test_url, verify=False, headers=req_headers, allow_redirects=True)
        #print('result: ' + str(result.status_code))
        if(("JSESSIONID" in str(result.headers)) or ("TGC" in str(result.headers))):
            valid_urls.append(test_url)
            #print("- Valid URL found: " + test_url)
        time.sleep(3)

    print("")     # Newline for output formatting purposes
    print("[*] URL list exhausted")

    if(len(valid_urls) > 0):
        for valid_url in valid_urls:
            print("[*] Valid URL found: " + valid_url)
    else:
        print("[*] No valid URLs found")
    print("[*] Done.")

if __name__ == '__main__':
    main()