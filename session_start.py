from KalturaClient import *
from KalturaClient.Plugins.Core import *

config = KalturaConfiguration(3082203)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)

secret = "KALTURA_SECRET"
user_id = "Kolodnydan@gmail.com"
k_type = KalturaSessionType.USER
partner_id = "PARTNE_ID"
expiry = 86400
privileges = ""

result = client.session.start(secret, user_id, k_type, partner_id, expiry, privileges)
print(result.objects[0])
