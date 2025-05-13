import requests

def download_audio(report):
    response = requests.get(report['audio'], stream=True)
    with open('calls/' + report['name'] + '.mp3', 'wb') as f:
        f.write(response.content)