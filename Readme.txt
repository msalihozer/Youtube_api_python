YouTube Live Stream Monitoring with Python YouTube API
This Python script is prepared as an example of using the YouTube API. It queries a specific URL for live stream status and keeps a log of the activity.

Usage
Ensure you have a valid API key file for the YouTube API v3.
You can find the official documentation and quickstart guide here.
Customize the script according to your requirements.
Be mindful of the query and operations within your quota limits. You can learn about query quotas here.
Place the .json file in your Python directory or provide the full path.
Configuration
api_key_file: Replace this with the path to your service account key JSON file.
api_service_name: Enter the name of the service you've created.
api_version: If you're using an older version, update the version information.
Replace "xxxx.force-ssl" with the credentials you've generated.
Setup
Refer to the Google Developer Console for instructions on using the YouTube API v3.
Place the JSON file generated for your service account in the same directory as the Python script, or provide the full path.
Enter the service name you've created in api_service_name.
Update the version information in api_version if you're using an older version.
Provide the credentials "xxxx.force-ssl" in the script.
License
This project is licensed under the MIT License.

Acknowledgements
Special thanks to Google's YouTube API documentation.
Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


Açıklama Türkçe:
Python Youtube Api kullanımına örnek olarak hazırlanmıştır.(https://developers.google.com/youtube/v3/quickstart/python)
Bu betik verilen adrese gidip canlı yayın sorgusu atmakda ve log tutmakda. 
Kullanımlarınıza göre değişiklik yapabiliriz. 
Dikkat etmeniz gereken sorgu ve işlemlerin belirli bir kotaya dahil olması. 
Kotanızı dikkate alarak işlem yapınız. Sorgu kotalarını öğrenebilirsiniz.(https://developers.google.com/youtube/v3/determine_quota_cost)
.Json dosyasını python dizinine koyunuz veya tam yol olarak giriniz.
api_key_file = "xxx.json"  # Servis hesabı anahtar JSON dosyanızla değiştirin
api_service_name = "xxx"
api_version = "v3"

Google developer console'dan youtube api v3 kullanımına bakınız.
Sizin için oluşturulan .json dosyasını python betiğinin dosyasına koyunuz veya tam yol veriniz. ==> api_key_file = "xxx.json"
Oluşturduğunuz servisin adınız giriniz.==> api_service_name = "xxx"
Daha eski bir versiyon kullanıyorsanız versiyon bilgisini güncelleyiniz.==>api_version = "v3"
Sizin oluşturulan xxxx.forca-sssl bilgisini giriniz. ==> credentials = service_account.Credentials.from_service_account_file(api_key_file, scopes=[
    "xxxx.force-ssl"])
youtube = build(api_service_name, api_version, credentials=credentials)

