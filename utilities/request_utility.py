import requests
from utilities.logger_utility import LogUtility


class RequestUtility:
    @staticmethod
    def getJsonContentByRequesting(url):
        try:
            response = requests.get(url)
            json_content = response.json()
            response.close()
            return json_content
        except Exception as ex:
            LogUtility.write_error("Exception occurred (on ->RequestUtility=>getJsonContentByRequesting()), due to : {}".format(ex))
            raise Exception('getting json content from request the URL {} is failed'. format(url))
