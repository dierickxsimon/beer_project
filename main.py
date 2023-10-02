import requests
from utils import URL
from tempratureReading import tempratureHandler
from relaisHandlers import relaisHandler, fridgeHandler, warmHandler


def getActiveBatch():
    try:
        url = URL + 'active_batch/'
        response = requests.get(url)
        response.raise_for_status()
        responseData = response.json()
        id = responseData['id']
        setting = responseData['setting']
        return id, setting, response
    except requests.exceptions.RequestException as e:
        response = f'something went wrong with getting the active batch {str(e)} '
        return None, None, response

def getBatchLastData(id):
    try:
        url = URL + 'streams/'
        body = {'id': id}
        response = requests.post(url, json=body)
        response.raise_for_status()
        data = response.json()
        if data:
            data = data[0]
        return data, response
    except requests.exceptions.RequestException as e:
        response = f'something went wrong with getting the data of the active batch {str(e)} '
        return None, response

def sendData(temprature, set_temprature, fridge, warm_element, batch):
    try:
        url = URL + 'update_streams/'
        body = {
            'temprature': temprature,
            'set_temprature': set_temprature,
            'fridge': fridge,
            'warm_element': warm_element,
            'batch': batch
        }
        print(body)
        response = requests.post(url, json=body)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        response = f'something went wrong with sending the data {str(e)} '
        return response

def logResponse(response):
    print('response:', response)



while True:
    batch, setting, response = getActiveBatch()
    logResponse(response)
    data, response = getBatchLastData(batch)
    logResponse(response)

    set_T = setting['set_T']
    min_T = setting['min_T']
    max_T = setting['max_T']
    callibrated_T = setting['callibrated_T']

    if not data:
        temprature = None
        fridge = False
        warm_element = False
        temprature = tempratureHandler(temprature,fridge, warm_element, callibrated_T)

        if temprature > set_T:
            fridge = fridgeHandler(fridge)
        elif set_T > temprature:
            warm_element = warmHandler(warm_element)
        elif set_T == temprature:
            pass

    else:
        temprature = data['temprature']
        fridge = data['fridge']
        warm_element = data['warm_element']

        temprature = tempratureHandler(temprature, fridge, warm_element, callibrated_T)

        if fridge:
            if temprature < set_T:
                fridge, warm_element = relaisHandler(fridge, warm_element)
        elif warm_element:
            if temprature > set_T:
                fridge, warm_element = relaisHandler(fridge, warm_element)
        else:
            if temprature < min_T:
                warm_element = warmHandler(warm_element)
            elif temprature > max_T:
                fridge = fridgeHandler(fridge)

    response = sendData(temprature, set_T, fridge, warm_element, batch)
    print(response)