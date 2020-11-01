from KalturaClient import *
from KalturaClient.Plugins.Core import *

config = KalturaConfiguration(3082203)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)

secret = "c379e618a42f4722e5c0a11c3084c9e7"
user_id = "Kolodnydan@gmail.com"
k_type = KalturaSessionType.USER
partner_id = "3082203"
expiry = 86400
privileges = ""

result = client.session.start(secret, user_id, k_type, partner_id, expiry, privileges)
print(result)
