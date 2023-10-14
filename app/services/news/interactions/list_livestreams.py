import json
import requests
from bs4 import BeautifulSoup

def get_youtube_response(channel):

    headers = {
        'authority': 'www.youtube.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://www.youtube.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-arch': '"arm"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"117.0.5938.149"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="117.0.5938.149", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.149"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"13.2.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'service-worker-navigation-preload': 'true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }
    
    url = 'https://www.youtube.com/@{channel}/streams'.format(channel=channel)

    response = requests.get(url, headers=headers)

    return response

def get_all_videos(response):

    soup = BeautifulSoup(response.text)
    data  = soup.find_all("script")

    string_script = str(data[35])
    json_starting_index = string_script .find('{')
    json_payload_string = string_script[json_starting_index:-10]
    payload = json.loads(json_payload_string)
    
    for main_payload in payload['contents']['twoColumnBrowseResultsRenderer']['tabs']:
        try:
            if (main_payload['tabRenderer']['title']) == 'Live':
                final_payload = main_payload
        except:
            pass

    all_videos = final_payload['tabRenderer']['content']['richGridRenderer']['contents']
    
    return all_videos

def is_video_live(video):
    try:
        status = video['richItemRenderer']['content']['videoRenderer']['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['text']['accessibility']['accessibilityData']['label']
        if status == 'LIVE':
            return True
        else:
            return False
    except:
        return False

def get_video_details(video):

    video_thumbnail = video['richItemRenderer']['content']['videoRenderer']['thumbnail']['thumbnails'].pop().get('url')
    video_title = video['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
    video_link = 'https://www.youtube.com' + video['richItemRenderer']['content']['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    
    response = {
        'thumbnail' : video_thumbnail,
        'title' : video_title,
        'link' : video_link
    }
    
    return response

def get_livestreams(all_videos):
    livestreams = []

    for video in all_videos:

        if is_video_live(video):

            livestreams.append(get_video_details(video))
    
    return livestreams

def get_channel_livestreams(channel_name):
    response = get_youtube_response(channel_name)
    all_videos = get_all_videos(response)
    livestreams = get_livestreams(all_videos)
    return livestreams

def list_livestreams(data):
    try:
        response = get_channel_livestreams(data.station_handle)
    except:
        response = []
    return response