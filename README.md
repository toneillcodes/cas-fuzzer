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
 test_urls = [<br />
    'http://www.google.com',                    # Does the IdP accept a fake HTTP SP?<br />
    'https://www.google.com',                   # Does the IdP accept a fake HTTPS SP?<br />
    'http://www.google.com/' + fuzz_str,        # What if we append the fuzz string? (HTTP)<br />
    'https://www.google.com/' + fuzz_str,       # What if we append the fuzz string? (HTTPS)<br />
    'http://' + fuzz_str,                       # HTTP fuzz string<br />
    'https://' + fuzz_str,                      # HTTPS fuzz string<br />
    'http://www.' + fuzz_str,                   # HTTP www.fuzz string<br />
    'https://www.' + fuzz_str,                  # HTTPS www.fuzz string<br />
    'http://subdomain.' + fuzz_str,             # Test for HTTP subdomains<br />
    'https://subdomain.' + fuzz_str             # Test for HTTPS subdomains<br />
  ]<br />

4. Run the cas-fuzzer.py script<br />
`┌──(toneill㉿kali)-[~/tools/cas-fuzzer]`<br />
`└─$ python cas-fuzzer.py`<br />
`[*] Enter CAS server hostname: example.school.edu`<br />
`[*] Enter CAS port: 9443`<br />
`[*] Enter CAS context path: cas`<br />
`[*] Enter fuzz string: fake-school.com`<br />
`[*] Testing SP URL list`<br />
`..........`<br />
`[*] URL list exhausted`<br />
`[*] Valid URL found: https://www.google.com`<br />
`[*] Valid URL found: https://www.google.com/fake-school.com`<br />
`[*] Done.`<br />
`┌──(toneill㉿kali)-[~/tools/cas-fuzzer]`<br />
`└─$`<br />

# fuzz strings
## default strings
Combinations that test common misconfigurations.
## portswigger URL validation bypass list
https://portswigger.net/web-security/ssrf/url-validation-bypass-cheat-sheet
# todo list
* update default test url list to include additional tests
* read test urls from a file
