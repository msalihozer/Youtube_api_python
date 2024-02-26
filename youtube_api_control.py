import os
import cv2
from googleapiclient.discovery import build
from google.oauth2 import service_account
from time import strftime, sleep
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import time
import datetime

api_key_file = "xxx.json"  # Servis hesabı anahtar JSON dosyanızla değiştirin
api_service_name = "xxx"
api_version = "v3"

credentials = service_account.Credentials.from_service_account_file(api_key_file, scopes=[
    "xxxx.force-ssl"])
youtube = build(api_service_name, api_version, credentials=credentials)

def get_url(youtube, kanal_id):
    istek = youtube.search().list(
        part="id",
        channelId=kanal_id,
        eventType="live",
        type="video"
    )
    yanıt = istek.execute()

    if 'items' in yanıt and len(yanıt['items']) > 0:
        canli_akis_id = yanıt['items'][0]['id']['videoId']
        canli_akis_urlsi = f"https://www.youtube.com/xxxxx"
        return canli_akis_urlsi
    else:
        return None


def main():
    sure = 420
    sayac = 0  
    while True:
        kanal_id = "xxxx"  # Yakalamak istediğiniz YouTube kanalının kimlik bilgisiyle değiştirin
        current_time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")

        with open('youtube_log.txt', 'a') as log_file, open('way_youtube_log.txt', 'a') as log_file2, open('radyo_youtube_log.txt', 'a') as log_file3:
            canli_akis_urlsi = get_xxxx_url(youtube, kanal_id)

            if canli_akis_urlsi:
                print("Canlı Yayın Var: ", canli_akis_urlsi)
                log_file.write(f'{canli_akis_urlsi}:{current_time}\n')
                sayac = 0
            else:
                print("Canlı Yayın Yok ")
                sayac += 1
                if sayac == 3:                    
                    sayac = 0
                    log_file.write(f'{canli_akis_urlsi}:{current_time}\n')            

        time.sleep(sure)

if __name__ == "__main__":
    main()
