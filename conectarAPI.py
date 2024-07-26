import requests

#Datos de prueba
cveID = ['CVE-2021-27104', 'CVE-2021-27102', 'CVE-2021-27103', 'CVE-2021-27101', 'CVE-2021-27017', 'CVE-2021-28550', 'CVE-2021-4939']

request = []
for i in cveID:
    url= f'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={i}'
    answer = requests.get(url)
    if answer.status_code == 200:
        data = answer.json()
        request.append(data)
    else:
        print("Error:", answer.status_code)