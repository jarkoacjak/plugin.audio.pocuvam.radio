import sys
import urllib.parse
import xbmcgui
import xbmcplugin

def build_url(query):
    # Funkcia na správne generovanie odkazov v menu
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def main():
    handle = int(sys.argv[1])
    arg_string = sys.argv[2][1:]
    params = dict(urllib.parse.parse_qsl(arg_string))

    # Zmena na 'files' prinúti Kodi skryť predvolené štvorčeky a načítať reálne logá
    xbmcplugin.setContent(handle, 'files')

    # --- KOMPLETNÁ DATABÁZA RÁDIÍ S FUNKČNÝMI LOGAMI ---
    radia_sk = [
        {"nazov": "Moveit Rádio", "url": "https://play.radiosebastian.eu/listen/moveitradiosk/radio.mp3", "logo": "https://static.mytuner.mobi/media/tvos_radios/play_250_250.webp"},
        {"nazov": "Fun Rádio Leto", "url": "https://stream.funradio.sk:8000/summer128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_leto.png"},
        {"nazov": "Fun Rádio Mileniálky", "url": "https://stream.funradio.sk:8000/milenialky128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_milenialky.png"},
        {"nazov": "Fun Rádio Dance", "url": "http://stream.funradio.sk:8000/dance128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_dance.png"},
        {"nazov": "Fun Rádio Chill", "url": "https://stream.funradio.sk/chill128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_chill.png"},
        {"nazov": "Fun Rádio 80's - 90's", "url": "http://stream.funradio.sk:8000/80-90-128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_80_90.png"},
        {"nazov": "Fun Rádio CZ - SK", "url": "http://stream.funradio.sk:8000/cs128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_czsk.png"},
        {"nazov": "V2Beat Radio", "url": "https://de1se01.v2beat.live/icecast.audio", "logo": "https://app.v2beat.com/images/viib-v2beat-logo-neon.jpg"},
        {"nazov": "Záhorácke Rádio", "url": "http://live.zahorackeradio.sk:8080/zr128.mp3", "logo": "https://www.zahorackeradio.sk/wp-content/uploads/2020/01/logo.png"},
        {"nazov": "Top Rádio", "url": "https://solid1.streamupsolutions.com/proxy/vhhggmih/stream", "logo": "https://topradio.sk/_next/image?url=%2Fimages%2Ftopradio.jpg&w=256&q=75"},
        {"nazov": "Trnavské Rádio", "url": "https://solid33.streamupsolutions.com/proxy/mujdmamw/trnavske", "logo": "https://trnavskeradio.sk/assets/images/logo.png"},
        {"nazov": "Rádio SUB FM", "url": "https://stream.subfm.sk/subfm", "logo": "https://subfm.sk/wp-content/uploads/2021/05/subfm-logo.png"},
        {"nazov": "Rádio Ticho", "url": "https://solid1.streamupsolutions.com/proxy/rpiipoer/tiche", "logo": "https://radioticho.sk/wp-content/uploads/2022/02/logo.png"},
        {"nazov": "Sky Rádio", "url": "http://stream.skyradio.sk:8000/sky128", "logo": "https://skyradio.sk/images/logo.png"},
        {"nazov": "Rádio Slobodný Vysielač", "url": "https://vysielanie.online/radio/8020/SV128.mp3", "logo": "https://slobodnyvysielac.sk/wp-content/uploads/2018/10/logo.png"},
        {"nazov": "Rádio Zábava", "url": "https://stream.zeno.fm/eyac00cx1nhvv", "logo": "https://radiozabava.sk/wp-content/uploads/2023/logo.png"},
        {"nazov": "Rádio Rusyn FM", "url": "https://stream.rusyn.fm/rusyny.mp3", "logo": "https://rusyn.fm/templates/rusyn/images/logo.png"},
        {"nazov": "Rádio X - Metal X", "url": "https://stream.radiox.sk:8443/metal.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X - Oldies X", "url": "https://stream.radiox.sk:8443/oldies.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X - Folklore X", "url": "https://stream.radiox.sk:8443/ludovky.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X - Chillout X", "url": "https://stream.radiox.sk:8443/chillout.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X - Dance X", "url": "https://stream.radiox.sk:8443/dance.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X - DNB X", "url": "https://stream.radiox.sk:8443/dnb.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X", "url": "https://stream.radiox.sk:8443/radiox_256.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio X - Alternative X", "url": "https://stream.radiox.sk:8443/alternative.mp3", "logo": "https://radiox.sk/wp-content/uploads/2021/05/radiox-logo.png"},
        {"nazov": "Rádio Vlna - Classic Rock", "url": "https://stream.radiovlna.sk/rock-hi.mp3", "logo": "https://www.radiovlna.sk/assets/images/logo_classic_rock.png"},
        {"nazov": "Rádio Vlna - Oldies Párty", "url": "https://stream.radiovlna.sk:8000/party-hi.mp3", "logo": "https://www.radiovlna.sk/assets/images/logo_oldies_party.png"},
        {"nazov": "Rádio Vlna - 60's & 70s", "url": "https://stream.radiovlna.sk/gold-hi.mp3", "logo": "https://www.radiovlna.sk/assets/images/logo_gold.png"},
        {"nazov": "Rádio Vlna - Balady", "url": "https://stream.radiovlna.sk/balady-hi.mp3", "logo": "https://www.radiovlna.sk/assets/images/logo_balady.png"},
        {"nazov": "Rádio v Nitre", "url": "http://195.210.28.150:8932/radiovnitre_live.mp3", "logo": "https://radiovnitre.sk/wp-content/uploads/2022/10/logo.png"},
        {"nazov": "Rádio Vega", "url": "https://stream.sepia.sk:8000/vega128.mp3", "logo": "https://radiovega.sk/wp-content/uploads/2020/09/logo.png"},
        {"nazov": "Rádio Tlis", "url": "https://stream.tlis.sk/tlis.mp3", "logo": "https://tlis.sk/wp-content/uploads/2019/11/tlis-logo.png"},
        {"nazov": "Rádio Topoľčany", "url": "http://80.242.44.249:8000/;", "logo": "https://radiotopolcany.sk/wp-content/uploads/2021/logo.png"},
        {"nazov": "Radio Slovakia International", "url": "https://icecast.stv.livebox.sk/rsi_128.mp3", "logo": "https://rtvs.sk/assets/images/rsi-logo.png"},
        {"nazov": "Rádio Šírava", "url": "http://stream.sepia.sk:8000/radiosirava.mp3", "logo": "https://radiosirava.sk/wp-content/uploads/2021/04/logo.png"},
        {"nazov": "Rádio Rock SV", "url": "https://s2.myradiostream.com/:4870/listen.mp3", "logo": "https://radiorock.sv/logo.png"},
        {"nazov": "Rádio Sity", "url": "https://radiosity.online:8000/aac", "logo": "https://radiosity.sk/wp-content/uploads/2022/logo.png"},
        {"nazov": "Rádio Pyramída", "url": "https://icecast.stv.livebox.sk/pyramida_128.mp3", "logo": "https://rtvs.sk/assets/images/pyramida-logo.png"},
        {"nazov": "Rádio Rebeca", "url": "https://mpc2.mediacp.eu:8200/rebecaweb", "logo": "https://rebeca.sk/wp-content/uploads/2020/logo.png"},
        {"nazov": "Rádio Pohoda 2", "url": "http://mpc1.mediacp.eu:18111/stream", "logo": "https://radiopohoda.sk/logo2.png"},
        {"nazov": "Rádio Pokoj", "url": "http://radioserver.online:8822/;", "logo": "https://radiopokoj.sk/logo.png"},
        {"nazov": "Rádio Piešťany", "url": "https://solid33.streamupsolutions.com/proxy/gktiemqb/stream", "logo": "https://radiopiestany.sk/wp-content/uploads/2019/logo.png"},
        {"nazov": "Rádio Pohoda", "url": "https://audio.radiopohoda.com:8000/stream", "logo": "https://radiopohoda.sk/wp-content/uploads/2021/logo.png"},
        {"nazov": "Rádio Paráda", "url": "https://extra.mediacp.eu/stream/RadioParada,o.z.", "logo": "https://www.radioparada.sk/wp-content/uploads/2021/12/LOGO-PARADA-NEW-1024x1024.png"},
        {"nazov": "Rádio Patria", "url": "https://icecast.stv.livebox.sk/patria_128.mp3", "logo": "https://rtvs.sk/assets/images/patria-logo.png"},
        {"nazov": "Rádio Modra", "url": "http://185.98.208.12:8000/;", "logo": "https://radiomodra.sk/wp-content/uploads/2021/logo.png"},
        {"nazov": "Rádio PaF", "url": "https://node-23.zeno.fm/92cv04cggfhvv", "logo": "https://radiopaf.sk/logo.png"},
        {"nazov": "Rádio Logos", "url": "http://radioserver.online:8824/;", "logo": "https://radiologos.sk/logo.png"},
        {"nazov": "Rádio Metropolitan", "url": "https://mpc2.mediacp.eu:8214/stream", "logo": "https://radiometropolitan.sk/logo.png"},
        {"nazov": "Rádio Klub", "url": "https://listen.radioking.com/radio/860681/stream/930496", "logo": "https://radioklub.sk/logo.png"},
        {"nazov": "Rádio Litera", "url": "https://icecast.stv.livebox.sk/litera_128.mp3", "logo": "https://rtvs.sk/assets/images/litera-logo.png"},
        {"nazov": "Rádio KIKS - Big 90s", "url": "https://online.radiokiks.sk:8000/kiks_big90s.mp3", "logo": "https://radiokiks.net/wp-content/uploads/2024/08/Logo_BIG_90.png"},
        {"nazov": "Rádio KIKS - Rock Music", "url": "https://online.radiokiks.sk:8000/kiks_rock.mp3", "logo": "https://radiokiks.net/wp-content/uploads/2024/08/Logo_ROCK.png"},
        {"nazov": "Rádio KIKS", "url": "https://online.radiokiks.sk:8000/kiks_hq.mp3", "logo": "https://radiokiks.net/wp-content/uploads/2024/08/Logo_KIKS.png"},
        {"nazov": "Rádio KIKS - Big 80s", "url": "https://online.radiokiks.sk:8000/kiks_big80s.mp3", "logo": "https://radiokiks.net/wp-content/uploads/2024/08/Logo_BIG_80.png"},
        {"nazov": "Rádio Jemné Chillout", "url": "https://stream.bauermedia.sk/chillout-hi.mp3", "logo": "https://www.jemne.sk/assets/images/logo_chillout.png"},
        {"nazov": "Rádio Junior", "url": "https://icecast.stv.livebox.sk/junior_128.mp3", "logo": "https://rtvs.sk/assets/images/junior-logo.png"},
        {"nazov": "Rádio Janko Hraško", "url": "http://78.24.9.110:31088/;", "logo": "https://www.jankohrasko.sk/templates/jh/images/logo.png"},
        {"nazov": "Rádio Jazz", "url": "http://stream.sepia.sk:8000/jazz192.mp3", "logo": "http://radiojazz.sk/image/logo.png"},
        {"nazov": "Rádio FanWaves", "url": "https://stream.zeno.fm/gtkbdehhekftv", "logo": "https://fanwaves.de/logo.png"},
        {"nazov": "Rádio Folk", "url": "https://mpc1.mediacp.eu/stream/demo2", "logo": "https://www.radiofolk.sk/wp-content/uploads/2021/08/cropped-cropped-cropped-Logo-pre-web.png"},
        {"nazov": "Rádio Biblia", "url": "http://radiobiblia.online:8000/stream.ogg", "logo": "https://radiobiblia.sk/logo.png"},
        {"nazov": "Rádio Extra", "url": "http://live.topradio.cz:8000/extra192", "logo": "https://radioextra.sk/logo.png"},
        {"nazov": "Rádio Beta Česko a Slovenské Hity", "url": "http://109.71.67.102:8000/beta_cspop.mp3", "logo": "https://www.radiobeta.sk/images/logo.png"},
        {"nazov": "Rádio Beta 80'S a 90'S", "url": "http://109.71.67.102:8000/beta_80a90.mp3", "logo": "https://www.radiobeta.sk/images/logo.png"},
        {"nazov": "Rádio Beta Hráme jubilantom", "url": "http://109.71.67.102:8000/beta_jubilanti.mp3", "logo": "https://www.radiobeta.sk/images/logo.png"},
        {"nazov": "Rádio Bela", "url": "http://65.109.81.84:8855/live", "logo": "https://radiobela.sk/logo.png"},
        {"nazov": "Rádio Best FM", "url": "https://stream3.bestfm.sk:8000/160.aac", "logo": "https://bestfm.sk/wp-content/uploads/2021/09/logo_transparent.png"},
        {"nazov": "Rádio Basavel", "url": "https://stream.zeno.fm/6gd9c6yn4nhvv", "logo": "https://radiobasavel.sk/logo.png"},
        {"nazov": "Rádio Aetter", "url": "http://stream.aetter.sk:8000/aetter", "logo": "https://aetter.sk/wp-content/uploads/2020/09/logo.png"},
        {"nazov": "Rádio 7", "url": "https://play.radio7.sk/128", "logo": "https://radio7.sk/wp-content/uploads/2021/05/logo_r7.png"},
        {"nazov": "Rádio 9", "url": "http://147.232.191.167:8000/high.mp3", "logo": "https://r9.sk/logo.png"},
        {"nazov": "PARTY RADIO", "url": "https://mpc1.mediacp.eu/stream/partyradio", "logo": "https://partyradio.sk/logo.png"},
        {"nazov": "Rádio Viva", "url": "http://stream.sepia.sk:8000/viva320.mp3", "logo": "https://radioviva.sk/wp-content/uploads/2022/logo.png"},
        {"nazov": "Fresh Rádio", "url": "https://icecast2.radionet.sk/freshradio.sk", "logo": "https://freshradio.sk/logo.png"},
        {"nazov": "Rádio Rock", "url": "https://stream.bauermedia.sk/rock-hi.mp3", "logo": "https://radiorock.sk/intro-v2.png"},
        {"nazov": "Rádio Maria Slovakia", "url": "https://dreamsiteradiocp5.com/proxy/radiomariaslomp3?mp=/stream.mp3", "logo": "https://www.radiomaria.sk/wp-content/uploads/2020/logo.png"},
        {"nazov": "Rádio Lumen", "url": "https://audio.lumen.sk/live128.mp3", "logo": "https://www.lumen.sk/images/lumen_logo.png"},
        {"nazov": "Na vlne Novohradu", "url": "https://radioserver.online/proxy/navlnenovohradu/novohradHQ.mp3", "logo": "https://navlnenovohradu.sk/logo.png"},
        {"nazov": "Na vlne Liptova", "url": "http://radioserver.online:8009/hq.mp3", "logo": "https://navlneliptova.sk/logo.png"},
        {"nazov": "Mirjam Radio", "url": "https://dreamsiteradiocp5.com/proxy/rmslo?mp=/stream", "logo": "https://mirjamradio.sk/logo.png"},
        {"nazov": "METALSCENA netRADIO", "url": "https://listen.radioking.com/radio/263218/stream/308365", "logo": "https://metalscena.sk/logo.png"},
        {"nazov": "Mars Dance Rádio", "url": "https://stream.zenolive.com/683gf5xrxfeuv?1686916511841", "logo": "https://marsdance.sk/logo.png"},
        {"nazov": "HITRÁDIO SLOVAKIA", "url": "https://hitradioslovakia.stream.laut.fm/hitradioslovakia", "logo": "https://hitradioslovakia.sk/logo.png"},
        {"nazov": "BB FM", "url": "http://stream.bbfm.sk:8000/bbfm128.mp3", "logo": "https://www.bbfm.sk/bbfm_logo.png"},
        {"nazov": "Rádio Regina - Západ", "url": "https://icecast.stv.livebox.sk/regina-ba_128.mp3", "logo": "https://rtvs.sk/assets/images/regina-ba-logo.png"},
        {"nazov": "Rádio Regina - Stred", "url": "https://icecast.stv.livebox.sk/regina-bb_128.mp3", "logo": "https://rtvs.sk/assets/images/regina-bb-logo.png"},
        {"nazov": "Rádio Regina - Východ", "url": "https://icecast.stv.livebox.sk/regina-ke_128.mp3", "logo": "https://rtvs.sk/assets/images/regina-ke-logo.png"},
        {"nazov": "Rádio Devín", "url": "https://icecast.stv.livebox.sk/devin_128.mp3", "logo": "https://rtvs.sk/assets/images/devin-logo.png"},
        {"nazov": "Europa 2", "url": "https://stream.bauermedia.sk/europa2-hi.mp3", "logo": "https://www.europa2.sk/assets/images/logo.png"},
        {"nazov": "Dobré Rádio", "url": "https://stream.dobreradio.sk/dobreradio.mp3", "logo": "https://www.dobreradio.sk/assets/images/logo.png"},
        {"nazov": "Rádio InfoVojna", "url": "https://stream1.infovojna.com:8000/live", "logo": "https://www.infovojna.bz/public/img/logo.png"},
        {"nazov": "Rádio_FM", "url": "https://icecast.stv.livebox.sk/fm_128.mp3", "logo": "https://rtvs.sk/assets/images/fm-logo.png"},
        {"nazov": "Rádio Dychovka", "url": "https://epanel.mediacp.eu:7661/stream", "logo": "https://radiodychovka.sk/logo.png"},
        {"nazov": "Rádio Košice", "url": "http://stream.ecce.sk:8000/radiokosice-128.mp3", "logo": "https://www.radiokosice.sk/img/logo.png"},
        {"nazov": "FIT Family RADIO", "url": "http://solid67.streamupsolutions.com:8052/;", "logo": "https://fitfamilyradio.sk/logo.png"},
        {"nazov": "Rádio WOW", "url": "https://radioserver.online:9816/radiowow.mp3", "logo": "https://radiowow.sk/wp-content/uploads/2020/logo.png"},
        {"nazov": "Rádio Slovensko", "url": "https://icecast.stv.livebox.sk/slovensko_128.mp3", "logo": "https://rtvs.sk/assets/images/slovensko-logo.png"},
        {"nazov": "Detské Rádio", "url": "https://stream.21.sk/detskeradio-192.mp3", "logo": "https://www.detskeradio.sk/img/logo.png"},
        {"nazov": "Rádio Frontinus", "url": "http://stream.frontinus.sk:8000/frontinus128.mp3", "logo": "https://www.frontinus.sk/images/logo.png"},
        {"nazov": "Rádio Expres", "url": "https://stream.expres.sk/128.mp3", "logo": "https://www.expres.sk/assets/images/logo.png"},
        {"nazov": "Rádio Melody", "url": "https://stream.bauermedia.sk/melody-hi.mp3", "logo": "https://www.radiomelody.sk/cover.png?f=raw"},
        {"nazov": "Rádio Beta", "url": "http://109.71.67.102:8000/beta_live_high.mp3", "logo": "https://www.radiobeta.sk/images/logo.png"},
        {"nazov": "Fun Rádio", "url": "https://stream.funradio.sk:8000/fun128.mp3", "logo": "https://pub.funradio.sk/media/logo/funradio_logo_main.png"},
        {"nazov": "Rádio Vlna", "url": "http://stream.radiovlna.sk/vlna-hi.mp3", "logo": "https://www.radiovlna.sk/assets/images/logo.png"}
    ]

    radia_cz = [
        {"nazov": "Český Blaník", "url": "https://playerservices.streamtheworld.com/api/livestream-redirect/RADIO_BLANIKCZ_128.mp3", "logo": "https://prazsky.blanik.cz/assets/images/logo.png"},
        {"nazov": "Rádio Impuls", "url": "http://icecast5.play.cz/impuls128.mp3", "logo": "https://www.impuls.cz/images/logo.png"},
        {"nazov": "Crazy Rádio", "url": "http://live.topradio.cz:8000/crazy128", "logo": "http://hit-radio.cz/media/logo_6a043bd4bd019.jpg"},
        {"nazov": "Československé rádio", "url": "http://live.topradio.cz:8000/csradio128", "logo": "https://www.radioexpert.net/radio-logo/czech/%C4%9Beskoslovensk%C3%A9-r%C3%A1dio-232-most-czech-320.jpg"},
        {"nazov": "Coop tip", "url": "http://ice4.abradio.cz/coop128.mp3", "logo": "https://www.cooptipradio.cz/logo.png"},
        {"nazov": "Country Radio", "url": "https://stream.rcs.revma.com/h7rwanvb938uv", "logo": "https://www.countryradio.cz/assets/images/logo.png"},
        {"nazov": "ClubRadio", "url": "http://icecast2.play.cz/Clubradio.mp3", "logo": "http://api.play.cz/static/radio_logo/t200/clubradio.png"},
        {"nazov": "Color Music Radio", "url": "http://icecast6.play.cz/color192.mp3", "logo": "https://www.colormusicradio.cz/logo.png"},
        {"nazov": "Classic Praha", "url": "https://icecast8.play.cz/classic128.mp3", "logo": "https://www.classicpraha.cz/assets/images/logo.png"},
        {"nazov": "Calimeroclub", "url": "http://live.topradio.cz:8000/calimero192", "logo": "https://www.calimeroclub.eu/img/picture/231/logo-cali.jpg"},
        {"nazov": "Audio Kostel", "url": "https://evcast.mediacp.eu:1585/stream", "logo": "https://www.kostel.cz/logo.png"},
        {"nazov": "Bikers Radio Doupě", "url": "http://icecast7.play.cz/bikersradiodoupe128.mp3", "logo": "https://www.bikersradio.cz/images/logo.png"},
        {"nazov": "Alternative Times Radio", "url": "http://ice3.abradio.cz/alternative128.mp3", "logo": "https://alternativetimes.cz/logo.png"},
        {"nazov": "Astra Rádio", "url": "https://astra.icecast.cz/", "logo": "https://radioastra.cz/logo.png"},
        {"nazov": "Rádio Kiss", "url": "https://n25a-eu.rcs.revma.com/asn0cmvb938uv", "logo": "https://www.kiss.cz/files/design/logo.png"},
        {"nazov": "Evropa 2", "url": "https://ice.actve.net/fm-evropa2-128", "logo": "https://www.evropa2.cz/wp-content/themes/evropa2/assets/img/logo.png"},
        {"nazov": "BlackFM Radio", "url": "http://icecast2.play.cz/blackfm-radio-192.mp3", "logo": "https://blackfm.cz/image/freestyle/blackfm_logo_www.jpg"},
        {"nazov": "Blue Radio", "url": "https://stream.blueradio.cz/live", "logo": "https://stream.blueradio.cz/img/logo.png"},
        {"nazov": "Bojler Room", "url": "https://ice4.abradio.cz/bojler_room_128.aac", "logo": "https://bojlerroom.cz/logo.png"},
        {"nazov": "Bus Radio", "url": "http://mpc1.mediacp.eu:8064/;", "logo": "https://busradio.cz/logo.png"}
    ]

    action = params.get('action')

     if action is None:
        # HLAVNÉ MENU
        url_sk = build_url({'action': 'list', 'country': 'sk'})
        li_sk = xbmcgui.ListItem(label='[B][COLOR yellow]Hudba:[/COLOR] 🇸🇰 Slovenské rádiá[/B]')
        li_sk.setArt({
            'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/250px-Flag_of_Slovakia.svg.png',
            'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/250px-Flag_of_Slovakia.svg.png'
        })
        xbmcplugin.addDirectoryItem(handle, url_sk, li_sk, isFolder=True)

        url_cz = build_url({'action': 'list', 'country': 'cz'})
        li_cz = xbmcgui.ListItem(label='[B][COLOR yellow]Hudba:[/COLOR] 🇨🇿 České rádiá[/B]')
        li_cz.setArt({
            'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/250px-Flag_of_the_Czech_Republic.svg.png',
            'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/250px-Flag_of_the_Czech_Republic.svg.png'
        })
        xbmcplugin.addDirectoryItem(handle, url_cz, li_cz, isFolder=True)

    elif action == 'list':
        # ZOZNAM STANÍC
        country = params.get('country')
        vybrane_radia = radia_sk if country == 'sk' else radia_cz

        for radio in vybrane_radia:
            li = xbmcgui.ListItem(label=radio['nazov'])
            
            # Nastavenie priamych grafických adries pre zobrazenie loga namiesto štvorčeka
            li.setArt({
                'icon': radio['logo'],
                'thumb': radio['logo'],
                'poster': radio['logo']
            })
            
            li.setInfo('video', {'title': radio['nazov']})
            li.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle, radio['url'], li, isFolder=False)

    xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main()
