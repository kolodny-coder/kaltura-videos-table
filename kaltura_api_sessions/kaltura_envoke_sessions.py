from KalturaClient import *
from KalturaClient.Plugins.Core import *
import os




def get_entry(entry_id):
    config = KalturaConfiguration(3082203)
    config.serviceUrl = "https://www.kaltura.com/"
    client = KalturaClient(config)
    ks = client.session.start(
        os.environ.get('KALTURA_SECRET'),
        "Kolodnydan@gmail.com",
        KalturaSessionType.ADMIN,
        "3082203")
    client.setKs(ks)

    version = -1

    result = client.media.get(entry_id, version)
    return result.json()





def add_media():
      config = KalturaConfiguration(3082203)
      config.serviceUrl = "https://www.kaltura.com/"
      client = KalturaClient(config)
      ks = client.session.start(
          os.environ.get('KALTURA_SECRET'),
          "Kolodnydan@gmail.com",
          KalturaSessionType.ADMIN,
          "3082203")
      client.setKs(ks)

      entry = KalturaMediaEntry()
      entry.sourceType = KalturaSourceType.URL
      entry.searchProviderType = KalturaSearchProviderType.YOUTUBE
      entry.mediaType = KalturaMediaType.VIDEO

      result = client.media.add(entry)
      print(result)


from KalturaClient import *
from KalturaClient.Plugins.Core import *

def delete(idx):

    config = KalturaConfiguration(3082203)
    config.serviceUrl = "https://www.kaltura.com/"
    client = KalturaClient(config)
    ks = client.session.start(
          os.environ.get('KALTURA_SECRET'),
          "Kolodnydan@gmail.com",
          KalturaSessionType.ADMIN,
          "3082203")
    client.setKs(ks)

    entry_id = idx

    result = client.media.delete(entry_id)
    print(result)
