﻿# -*- coding: utf-8 -*-
# constant values
# Copyright (C) 20XX anonimous <anonimous@sample.com>

# アプリケーション基本情報
APP_FULL_NAME = "JAWS リサーチイット用Google検索モジュール"  # アプリケーションの完全な名前
APP_NAME = "JFW_RI_GLE"  # アプリケーションの名前
APP_ICON = None
APP_VERSION = "1.0.0"
APP_LAST_RELEASE_DATE = "20xx-xx-xx"
APP_COPYRIGHT_YEAR = "2022"
APP_LICENSE = ""
APP_DEVELOPERS = "Kazto Kitabatake(Accessible Tools Laboratory)"
APP_DEVELOPERS_URL = "https://actlab.org/"
APP_DETAILS_URL = "https://example.com/template"
APP_COPYRIGHT_MESSAGE = "Copyright (c) %s %s All lights reserved." % (APP_COPYRIGHT_YEAR, APP_DEVELOPERS)

# build関連定数
BASE_PACKAGE_URL = None
PACKAGE_CONTAIN_ITEMS = ()  # パッケージに含めたいファイルやfolderがあれば指定
NEED_HOOKS = ()  # pyinstallerのhookを追加したい場合は指定
STARTUP_FILE = "application.py"  # 起動用ファイルを指定
UPDATER_URL = None

# update情報
UPDATE_URL = "https://actlab.org/api/checkUpdate"
UPDATER_VERSION = "1.0.0"
UPDATER_WAKE_WORD = "hello"
