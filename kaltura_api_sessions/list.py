from KalturaClient import *
from KalturaClient.Plugins.Core import *
import os

config = KalturaConfiguration(3082203)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
ks = client.session.start(
      os.environ.get('KALTURA_SECRET'),
      "Kolodnydan@gmail.com",
      KalturaSessionType.ADMIN,
      "3082203")
client.setKs(ks)


filter = KalturaMediaEntryFilter()
pager = KalturaFilterPager()

result = client.media.list(filter, pager)
print(result.objects)
