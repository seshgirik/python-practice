import requests

url = 'http://10.10.226.39:32781/li'
# myobj = {'somekey': 'somevalue'}
headers = {"Content-type": "text/xml;charset=UTF-8", "SOAPAction": "\"http://mavenir.net/li/addTarget\"",
           "User-Agent": "Jakarta Commons-HttpClient/3.1"}

body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:li="http://mavenir.net/li/">
   <soapenv:Header/>
   <soapenv:Body>
        <li:addTarget>
         <litid>222229900</litid>
         <target>18898710124</target>
         <deliveryfunction2>192.168.60.57:50008</deliveryfunction2>
         <deliveryfunction3>192.168.60.57:31600</deliveryfunction3>
         <targettype>MSISDN</targettype>
      </li:addTarget>
   </soapenv:Body>
</soapenv:Envelope>"""

x = requests.post(url, headers=headers, data = body)
print(body)
print(x.text)
