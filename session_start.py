from KalturaClient import *
from KalturaClient.Plugins.Core import *

config = KalturaConfiguration(3082203)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)

secret = "KALTURA_SECRET"
user_id = "Kolodnydan@gmail.com"
k_type = KalturaSessionType.USER
partner_id = 3082203
expiry = 86400
privileges = ""

result = client.session.start(secret, user_id, k_type, partner_id, expiry, privileges)
print(result.objects)

# file_data = open('application/static/video/Countdown Timer.mov', 'rb')
#
# result = client.media.upload(file_data)
# one = sorted(result.objects, key=lambda k: k.createdAt, reverse=True)
# for i in one:
#     print(i)
# print(one[1])
