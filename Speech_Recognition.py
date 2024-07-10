
# Upload
import api
import requests
headers={'authorization':api.AssemblyAI}
filename="audio.mp3"
upload_endpoint='https://api.assemblyai.com/v2/upload'
transcript_endpoint='https://api.assemblyai.com/v2/transcript'
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data=_file.read(chunk_size)
                if not data:
                    break
                yield data
    upload_response=requests.post(upload_endpoint,
                           headers=headers,
                           data=read_file(filename))
    print(upload_response.json())
    audio_url=upload_response.json()['upload_url']
    return audio_url

# Transcribe

def transcribe(audio_url):
    transcript_request={"audio_url":audio_url}
    transcript_response=requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    print(transcript_response.json())
    job_id=transcript_response.json()['id']
    return job_id

# Poll
def poll(transcript_id):
    polling_endpoint=transcript_endpoint + '/' + transcript_id
    while True:
        polling_response=requests.get(polling_endpoint, json=transcript_id, headers=headers)
        if polling_response.json()['status']=='completed':
            print(polling_response.json())
            return polling_response.json()
        elif polling_response.json()['status']=='error':
            return polling_response.json()['error']

# Saving in a file

def save_txt(polling_response):
    txt_filename="audio.txt"
    try:
        with open(txt_filename, 'w') as f:
            f.write(polling_response['text'])
        print("transcription saved!!")
    except:
        print(polling_response)

# Sample of how to implement it:

# audio_url=upload(filename)
# transcript_id=transcribe(audio_url)
# polling_response=poll(transcript_id)
# save_txt(polling_response)



