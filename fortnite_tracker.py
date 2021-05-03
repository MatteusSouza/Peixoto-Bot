import requests
from config import TRN_KEY


def validateRegion(region: str):
    regions = ["NAE", "NAW", "EU", "OCE", "BR", "ASIA", "ME"]
    return region.upper() in regions


def validatePlatform(platform):
    platforms = ["PC", "CONSOLE", "MOBILE"]
    return platform.upper() in platforms


def requisition(username, platform, region):
    url = 'https://api.fortnitetracker.com/v1/powerrankings/' + platform + '/' + region + '/' + username
    headers = {
        'TRN-Api-Key': TRN_KEY
    }

    status_code = None
    info = None

    try:
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        info = response.json()

    except:
        # message404 = "\nCould not find the Power ranking for that user. Most likely the user has no Power Ranking."
        # if status_code == 404:
        #     print(f"\33[0:31m{message404}\33[m")
        pass

    finally:
        return {'status_code': status_code, 'response_info': info}


def getPower_ranking(username, platform, region):
    none_status_code = None
    none_response_info = None

    validation = {'platform': validatePlatform(platform), 'region': validateRegion(region)}

    if (validation['platform'] and validation['region']) is True:
        response = requisition(username, platform, region)
        return {'validation': validation,
                'status_code': response['status_code'],
                'response_info': response['response_info']}
    else:
        return {'validation': validation,
                'status_code': none_status_code,
                'response_info': none_response_info}