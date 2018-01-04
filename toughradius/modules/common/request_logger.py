#!/usr/bin/env python
#coding=utf-8
import os
import logging
from toughradius.pyrad.radius import packet
from toughradius.pyrad import message

logger = logging.getLogger(__name__)
trace = logging.getLogger("trace")

def log_auth(req):
    logger.info('RadiusAccessRequest received from the access device %s:%s'%req.source)
    if os.environ.get('TOUGHRADIUS_TRACE_ENABLED',"0")  == "1":
        trace.info(message.format_packet_str(req))


def log_acct(req):
    logger.info('RadiusAccountingRequest received from the access device %s:%s'%req.source)
    if os.environ.get('TOUGHRADIUS_TRACE_ENABLED', "0") == "1":
        trace.info(message.format_packet_str(req))


def handle_radius(req):
    try:
        if req.code == packet.AccessRequest:
            log_auth(req)
        elif req.code == packet.AccountingRequest:
            log_acct(req)
    except:
        logger.error("request log error", exc_info=True)
        
    return req
