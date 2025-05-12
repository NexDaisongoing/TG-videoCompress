#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

import logging
from decouple import config


LOGS = logging.getLogger(__name__)

try:
    APP_ID = config("APP_ID", default=24810254, cast=int)
    API_HASH = config("API_HASH", default="aadb42caec01695fa0a77c09b3e0ef47")
    BOT_TOKEN = config("BOT_TOKEN", default="7766680940:AAFRLQDTwpbreK-dZ-kk8fupB6tHkMBwk2g")
    DEV = config("DEV", default="1772989999")
    OWNER = config("OWNER", default="7543269959")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMB = config("THUMB", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
