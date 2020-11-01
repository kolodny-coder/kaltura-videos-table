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


filter = KalturaMediaEntryFilter()
pager = KalturaFilterPager()

result = client.media.list(filter, pager)

print(result)