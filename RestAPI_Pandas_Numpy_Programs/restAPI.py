import requests


class RestAPI(object):
    '''
    Class fo REST API execution.
    '''
    def __init__(self,
                 server,
                 port,
                 userName,
                 password,
                 protocol="http",
                 sslVerify=False,
                 headers={'Content-type': 'application/json'}):
        '''
        Contructor of class.
        '''
        self.server = server
        self.port = port
        self.userName = userName
        self.password = password
        self.protocol = protocol
        self.sslVerify = sslVerify
        self.headers = headers
        self.auth = (self.userName, self.password)

    def _buildUrl(self, routeUrl):
        '''
        Building the REST url.
        '''
        #myurl = "https://10.234.139.26:8443/univmax/restapi/82/replication/symmetrix/000197900143/storagegroup/test_1/"
        myurl = "{}://{}:{}/{}".format(self.protocol, self.server, self.port, routeUrl)
        return myurl

    def executeGET(self, routeUrl, queryStringDict=None):
        '''
        Execute GET on given url.
        '''
        responseData = {'msg': "No response from executeGET.", 'status_code': 500}
        try:
            myUrl = self._buildUrl(routeUrl)
            if not self.sslVerify:
                requests.packages.urllib3.disable_warnings()

            if queryStringDict:
                index = 0
                for k, v in queryStringDict:
                    if (index == 0):
                        myUrl = "{}?{}={}".format(myUrl, k, v)
                    else:
                        myUrl = "&{}={}".format(myUrl, k, v)
                    index += 1

            responseData = requests.get(url=myUrl, verify=self.sslVerify, auth=self.auth, headers=self.headers)
            responseData = {'msg': "GET operation successful.", 'output': responseData.json(), 'status_code': responseData.status_code}
        except Exception as e:
            responseData = {'msg': e, 'status_code': responseData.status_code}
        finally:
            return responseData

    def executePOST(self, routeUrl, inputData):
        '''
        Execute POST on given url.
        '''
        responseData = {'msg': "No response from executePOST.", 'status_code': 500}
        try:
            myUrl = self._buildUrl(routeUrl)
            if not self.sslVerify:
                requests.packages.urllib3.disable_warnings()
            responseData = requests.post(url=myUrl, data=inputData, verify=self.sslVerify, auth=self.auth, headers=self.headers)
            responseData = {'msg': "POST operation successful.", 'output': responseData.json(), 'status_code': responseData.status_code}
        except Exception as e:
            responseData = {'msg': e, 'status_code': responseData.status_code}
        finally:
            return responseData

    def executePUT(self, routeUrl, inputData):
        '''
        Execute PUT on given url.
        '''
        responseData = {'msg': "No response from executePUT.", 'status_code': 500}
        try:
            myUrl = self._buildUrl(routeUrl)
            if not self.sslVerify:
                requests.packages.urllib3.disable_warnings()
            responseData = requests.put(url=myUrl, data=inputData, verify=self.sslVerify, auth=self.auth, headers=self.headers)
            responseData = {'msg': "PUT operation successful.", 'output': responseData.json(), 'status_code': responseData.status_code}
        except Exception as e:
            responseData = {'msg': e, 'status_code': responseData.status_code}
        finally:
            return responseData

    def executeDELETE(self, routeUrl):
        '''
        Execute DELETE on given url.
        '''
        responseData = {'msg': "No response from executeDELETE.", 'status_code': 500}
        try:
            myUrl = self._buildUrl(routeUrl)
            if not self.sslVerify:
                requests.packages.urllib3.disable_warnings()
            responseData = requests.delete(url=myUrl, verify=self.sslVerify, auth=self.auth, headers=self.headers)
            responseData = {'msg': "DELETE operation successful.", 'output': responseData.json(), 'status_code': responseData.status_code}
        except Exception as e:
            responseData = {'msg': e, 'status_code': responseData.status_code}
        finally:
            return responseData


if __name__ == "__main__":
    server = "10.234.139.26"
    port = "8443"
    userName = "smc"
    password = "smc"
    routeUrl = "univmax/restapi/82/replication/symmetrix/000197900143/storagegroup/test_1/"
    protocol = "https"
    r = RestAPI(server, port, userName, password, protocol)
    d = r.executeGET(routeUrl)
    print(d)
