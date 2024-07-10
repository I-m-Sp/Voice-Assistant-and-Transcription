import Audio_Processing as aud
import Speech_Recognition as sr
import Voice_Assistant as va

aud.start()
audio_url=sr.upload(sr.filename)
transcript_id=sr.transcribe(audio_url)
polling_response=sr.poll(transcript_id)
# sr.save_txt(polling_response)
va.request(polling_response['text'])