# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcaddon
import os

ADDON = xbmcaddon.Addon()

def play_audio(url, station_name, icon=""):
    """Spustí rádio stream"""
    listitem = xbmcgui.ListItem(station_name)
    listitem.setArt({'icon': icon, 'thumb': icon})
    listitem.setInfo('music', {'title': station_name})
    xbmc.Player().play(url, listitem)

def radio_notify(message):
    """Zobrazí oznámenie pre Rádio"""
    xbmcgui.Dialog().notification("Počúvam Rádiá", message, xbmcgui.NOTIFICATION_INFO, 4000)

def log_radio(msg):
    xbmc.log(f"RADIO_LOG: {msg}", xbmc.LOGINFO)

