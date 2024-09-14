# cas-fuzzer
A tool for pen testers to audit the security of a CAS SSO server.
> [!CAUTION]
> Disclaimer: Intended only for use on systems that you are legally authorized to access. 
# installation
* Requires Python
* Download and run script
# usage
1. Identify target
2. Review and update test URL list<br />
```
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
```

4. Run the cas-fuzzer.py script<br />
```
┌──(toneill㉿kali)-[~/tools/cas-fuzzer]
└─$ python cas-fuzzer.py
[*] Enter CAS server hostname: example.school.edu
[*] Enter CAS port: 9443
[*] Enter CAS context path: cas
[*] Enter fuzz string: fake-school.com
[*] Testing SP URL list
..........
[*] URL list exhausted
[*] Valid URL found: https://www.google.com
[*] Valid URL found: https://www.google.com/fake-school.com
[*] Done.
┌──(toneill㉿kali)-[~/tools/cas-fuzzer]
└─$ 
```

# fuzz strings
## default strings
Combinations that test common misconfigurations.
## portswigger URL validation bypass list
https://portswigger.net/web-security/ssrf/url-validation-bypass-cheat-sheet
# todo list
* update default test url list to include additional tests
* read test urls from a file
