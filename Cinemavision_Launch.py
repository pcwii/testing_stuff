import requests
import json

kodi_ip = "192.168.0.32"
kodi_port = "8080"
kodi_user = ""
kodi_pass = ""
json_header = {'content-type': 'application/json'}
kodi_path = "http://"+kodi_user+":"+kodi_pass+"@"+kodi_ip+":"+kodi_port+"/jsonrpc"
addon_name = "script.cinemavision"
#  addon_name = "pmc"


def cv_play():
    method = "Addons.ExecuteAddon"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1,
        "params": {
            "addonid": "script.cinemavision",
            "params": [
                "experience",
                "nodialog"
            ]
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        print(kodi_response.text)
    except Exception as e:
        print(e)


def play_movie_by_id(movieid):
    method = "Player.Open"
    kodi_payload = {
        'jsonrpc': '2.0',
        'method': method,
        'id': 1,
        'params': {
            'item': {
                'movieid': movieid
            }
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        print(kodi_response.text)
    except Exception as e:
        print(e)


def kodi_play():
    method = "Player.Open"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1,
        "params": {
            "item": {
                "playlistid": 1
            }
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        print(kodi_response.text)
    except Exception as e:
        print(e)


def list_addons():
    method = "Addons.GetAddons"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": "1",
        "params": {
            "type": "xbmc.addon.executable"
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        print(e)
        return "NONE"


def list_all_movies():
    method = "VideoLibrary.GetMovies"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1,
        "params": {
            "properties": [
            ],
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        movie_list = json.loads(kodi_response.text)["result"]["movies"]
        return movie_list
    except Exception as e:
        print(e)
        return "NONE"


def find_movie_match(movie_name, movie_list):
    content = []
    for movie in movie_list:
        movie_title = str(movie['label'])
        if movie_name.lower() in movie_title.lower():
            print(movie['label'])
            info = {
                "label": movie['label'],
                "movieid": movie['movieid']
            }
            content.append(info)
    return content


def get_movie_id(movie_name, movie_list):
    movie_id = 'NONE'
    for movie in movie_list:
        if movie_name == movie['label']:
            movie_id = movie['movieid']
    return movie_id


def clear_playlist():
    method = "Playlist.Clear"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1,
        "params": {
            "playlistid": 1
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def add_playlist(movieid):
    method = "Playlist.Add"
    kodi_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": {
            "playlistid": 1,
            "item": {
                "movieid": movieid
            }
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        # print(e)
        return e


def mute_kodi():
    method = "Application.SetMute"
    kodi_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": {
            "mute": "toggle"
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def update_library():
    method = "VideoLibrary.Scan"
    kodi_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": {
            "showdialogs": True
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def clean_library():
    method = "VideoLibrary.Clean"
    kodi_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": {
            "showdialogs": True
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def reboot_kodi():
    method = "System.Reboot"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def shutdown_kodi():
    method = "System.Shutdown"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def skip_fwd():
    method = "Player.Seek"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1,
            "value": "smallforward"
        },
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def skip_rev():
    method = "Player.Seek"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1,
            "value": "smallbackward"
        },
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def pause_movie():
    method = "Player.PlayPause"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1,
            "play": False},
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def resume_movie():
    method = "Player.PlayPause"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1,
            "play": True},
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def stop_movie():
    method = "Player.Stop"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1
        },
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def subtitles_on():
    method = "Player.SetSubtitle"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1,
            "subtitle": {
                "enable": True
            },
        },
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        return kodi_response.text
    except Exception as e:
        return e


def subtitles_off():
    method = "Player.SetSubtitle"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": 1,
            "subtitle": False},
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        print(kodi_response.text)
        return kodi_response.text

    except Exception as e:
        return e
# print(list_all_movies())
# print(find_movie_match('spider', list_all_movies()))
# print(list_addons())
# print(clear_playlist())
# print(add_playlist(1))
# print(mute_kodi())
# play_movie_by_id(50)
# print(get_movie_id('Arrival', list_all_movies()))
# update_library()
# clean_library()
# reboot_kodi()
print(subtitles_on())


