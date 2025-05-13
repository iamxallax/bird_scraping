import moviepy

from get_info import get_info
from whisper import tts
from download_audio import download_audio

def make_audio():
    reports = get_info()
    for report in reports:
        tts(report['name'], 'tts/' + report['name'])
        download_audio(report)

def make_playlist():
    reports = get_info()
    silence = moviepy.AudioFileClip('silence.mp3')
    for report in reports:
        try:
            tts = moviepy.AudioFileClip('tts/' + report['name'] + '.mp3')
            call = moviepy.AudioFileClip('calls/' + report['name'] + '.mp3')
        except KeyError:
            print(f"Error processing {report['name']}")
            continue
        moviepy.concatenate_audioclips([tts, silence, call]).write_audiofile('playlist/' + report['name'] + '.mp3')
        tts.close()
        call.close()
    silence.close()

if __name__ == '__main__':
    # make_audio() 
    make_playlist()