VIDEO_PREFIX = "/video/radiocanadalive"

NAME = L('Title')

ART  = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################

def Start():
    Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)
    
    HTTP.CacheTime = CACHE_1HOUR

def VideoMainMenu():
    dir = MediaContainer(viewGroup="InfoList")

    dir.Append(
            WebVideoItem(
                "http://www.radio-canada.ca/audio-video/index.shtml#urlMedia=http://www.radio-canada.ca/util/endirect/CBFTdirect.asx&pos=0",
                "Radio-Canada Live",
                subtitle="subtitle",
                summary="clicking on me will call CallbackExample",
        )
    )
    
    return dir

  
