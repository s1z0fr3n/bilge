# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAB-p2jwZUY4QmjJEAHGQ8AAEvAsx3Qe98k6Oevc9EDRe-FOI2XG3LjQM5Z5Ly98m0nOgbAqcmYvDAT3LRvk0kN5OOh7hVMB-NR53QvFLcDR1FCd6YdUqDIWTFKiEKD-2zhtr1kMis1IgL94JgTHcu9iUi9-ZBliWSnkurKSpHKdSTxkcrC2ggjuCjmEJhfayzGUzf8-LW1XNf01ZRor_YmmI_8tXLPUcC8-O__7UFwkC_IDIMginomwazfDPwWtF6BlZ3wcN8GSTYJ7MDj2mSXF_g8HVFCv7BY4G1E49dVFJ0rmFrdEEFqNtl_W_Z0cmekqoVT2xgGOPTBTyd-OVlpAAAAAVSzMXEA")
SESSION_NAME1 = getenv("SESSION_NAME", "AgBQsUSiJebEIRzGqXLd5QE9PZPAUJDepX5jax9vdo-NfzjXReMFGd4xFJ5vLc00ZY39Qw-4FrXq0EEXGCRzeooM0pU-iTYxYBAu4sGecGJTfyLjEFD_0dcuBGiEkz3Dsijg_Zjr4aNdukIzWiFdn9e2I6ida1TXLJAELXydydRZ2Ap5fxJXp9cdoR9dh9rMOCJ_n154l8DKM7_4SyOnFYruj5FY7adq837QT_F-t2K9s4ttZebxfex-CNJd1ssMXaKYlviitjb3nSKvlpxUo9Sq0ajCAMKQPxiI1CB-qOzSfFjoHrlLF4_HqAFkZHs3cGf0AQxCZTQiMICbP3uMpSA9AAAAAVDdGEQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5899172788:AAFL5tMcEfFuxWXqSJcQInMtCT6M_jTyBOA")
BOT_NAME = getenv("BOT_NAME", "𝄞ɪ̇ʟɢᴇ ᴍᴜsɪᴄ TR🇹🇷")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Bilge_Duyuru")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/03f1c9ec4513c3a52bc22.jpg")
admins = {6021808752}
API_ID = int(getenv("API_ID", "26621160"))
API_HASH = getenv("API_HASH", "5803c132487b7cd8d2e86532f9fe0296")
BOT_USERNAME = getenv("BOT_USERNAME", "Bilge_MusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Bilge_Asistan1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Bilge_Destekk")
PROJECT_NAME = getenv("PROJECT_NAME", "BilgeMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/s1z0fr3n/bilge")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1923"))
ARQ_API_KEY = getenv("ARQ_API_KEY", " ELYSFW-QKNWXK-FMOMPB-PTIRGP-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001785850313")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", '/!').split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6021808752").split()))
