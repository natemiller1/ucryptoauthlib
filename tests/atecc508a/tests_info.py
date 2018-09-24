# -*- coding: utf-8 -*-
import logging

from cryptoauthlib.constant import INFO_MODE_REVISION, INFO_MODE_STATE
from cryptoauthlib.device import ATECC508A

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("atecc508a.tests_info")


def run(atecc508a=None):
    if not atecc508a:
        atecc508a = ATECC508A()

    packet = atecc508a.atcab_info()
    log.info("atcab_info: %s", packet)

    packet = atecc508a.atcab_info_base(INFO_MODE_REVISION)
    log.info("atcab_info_base - revision: %s", packet)

    packet = atecc508a.atcab_info_base(INFO_MODE_STATE)
    log.info("atcab_info_base - state: %s", packet)