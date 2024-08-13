import requests

def check_url_virus_free(api_key, url):
    # Endpoint for the URL scanning API
    scan_url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    report_url = 'https://www.virustotal.com/vtapi/v2/url/report'
    
    # Scan the URL
    params = {'apikey': api_key, 'url': url}
    response = requests.post(scan_url, data=params)
    if response.status_code != 200:
        return f"Error: {response.status_code}"
    
    scan_data = response.json()
    if 'scan_id' not in scan_data:
        return "Error: Scan failed"
    
    scan_id = scan_data['scan_id']
    
    # Retrieve the report for the scanned URL
    params = {'apikey': api_key, 'resource': scan_id}
    response = requests.get(report_url, params=params)
    if response.status_code != 200:
        return f"Error: {response.status_code}"
    
    report_data = response.json()
    
    # Check the scan results
    if 'positives' in report_data:
        positives = report_data['positives']
        total = report_data['total']
        if positives == 0:
            return f"The URL is virus-free (scanned by {total} engines)."
        else:
            return f"The URL is potentially dangerous! Detected by {positives}/{total} engines."
    else:
        return "Error: Report retrieval failed"

def main():
    api_key = input("virustotal api key")
    url = input("Link to be verify:")
    result = check_url_virus_free(api_key, url)
    print(result)