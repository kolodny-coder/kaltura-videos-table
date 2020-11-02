from KalturaClient import *
from KalturaClient.Plugins.Core import *


def get_entry(entry_id):
    config = KalturaConfiguration(3082203)
    config.serviceUrl = "https://www.kaltura.com/"
    client = KalturaClient(config)
    ks = client.session.start(
          "943b0eb1a9fd8b8da4f78cb37930f3ac",
          "Kolodnydan@gmail.com",
          KalturaSessionType.ADMIN,
          "3082203")
    client.setKs(ks)

    version = -1

    result = client.media.get(entry_id, version)
    return result.json()
