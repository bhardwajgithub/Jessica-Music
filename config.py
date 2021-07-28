from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQBRW8cCEVPsPWIxmKodXNWmtSLVn9fapauZOYTGvnsDFeJHOQgYfmwcPbDyaj5A4HWMAJXbm6IFslOlJlrfoG5P6SE-BKcfFCGAnpVhbmkegbyYeSjVZoFy9vwd3jad9FBlGOoxikwbXzlGnwNGzToo_-yD03AB37P-1cE0Ewg4TllX-UP1zClhkaQbtp-GXMQE3BU4uasiPohgO-nMN3jV2Jcu4btS38uP0WI4fnoEPKaO3BpEgoiLtz58yi9P9GHBeH68p4ribvgWfDVADl7SK2H6HAH4-rAzCftgs4CJs6ZBewDWJyT5Mep3G-Pn-35ppnK_XGAgFrafLL4hiXVNaNU6dAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1607821276:AAG4SguYGRG7v8yZ8IFqRiZoCyure4XTT9I")
BOT_NAME = getenv("BOT_NAME", "musicbots")

API_ID = int(getenv("API_ID", "2635566" ))
API_HASH = getenv("API_HASH", "93d0d287297f17610a0692cfb046dcda")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "170"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1947924017").split()))
