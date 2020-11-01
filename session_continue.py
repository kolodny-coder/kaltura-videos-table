from KalturaClient import *
from KalturaClient.Plugins.Core import *

config = KalturaConfiguration(3082203)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
ks = client.session.start(
      "943b0eb1a9fd8b8da4f78cb37930f3ac",
      "Kolodnydan@gmail.com",
      KalturaSessionType.ADMIN,
      "3082203")
client.setKs(ks)

session = "djJ8MzA4MjIwM3xjW0c3wg7rklqv0FAr3p55hrpTDJy-7PphwcL7OoJ1q4vZ7mNK09bO9ABn3t63m5BPAeuM0BW1IIYeppCVXUOdqLHvPaiWnHCXuqxVObuKww=="

result = client.session.get(session)
print(result)
