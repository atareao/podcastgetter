
---
layout: podcasts
title: Podcasts
desc: "Podcasts"
permalink: /podcasts/
---
<article class="page">
    <div class="entry">
        <div id="inputbox" style="display: none;"><select id="select-podcast">
	<option value="Todos">Todos</option>
	<option value="Compilando Podcast">Compilando Podcast</option>
	<option value="Mosqueteroweb tecnologia, Linux, Chromebooks">Mosqueteroweb tecnologia, Linux, Chromebooks</option>
	<option value="Podcast de Eduardo Collado">Podcast de Eduardo Collado</option>
	<option value="Salmorejo Geek">Salmorejo Geek</option>
	<option value="uGeek - Tecnología, Android, Linux, Servidores y mucho más...">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</option>
	<option value="Podcast Linux">Podcast Linux</option>
	<option value="Ubuntu y otras hierbas">Ubuntu y otras hierbas</option>
</select>
</div>
        <div id="for-speed" style="display: none;">
            <select id="select-speed">
                <option value="0.8">0.8x</option>
                <option value="1.0">1.0x</option>
                <option value="1.2">1.2x</option>
                <option value="1.4">1.4x</option>
                <option value="1.6">1.6x</option>
                <option value="1.8">1.8x</option>
                <option value="2.0">2.0x</option>
            </select>
        </div>
        <div class="panel" id="panelplayer" style="height: 70px;">
            <div id="player">
                <a href="#" id="left" onclick="return false" title="Anterior">
                    <span class="control-icon previous-icon" aria-hidden="true"></span>
                </a>
                <a href="#"id="play-pause" onclick="return false" title="Reproducir">
                    <span class="control-icon play-icon" aria-hidden="true"></span>
                </a>
                <a href="#" id="right" onclick="return false" title="Siguiente">
                    <span class="control-icon next-icon" aria-hidden="true"></span>
                </a>


                <audio id="audio" preload="auto" tabindex="0" src="http://www.ivoox.com/radiogeek-el-gobierno-argentina-aprobo-la_mf_22791929_feed_1.mp3">
                    <source src="">
                </audio>
            </div>
            <div id="playing">
                <span id="media-info">
                    <span id="podcast"></span>
                    <span id="duration"></span>
                </span>
                <span id="track"></span>
                <progress id="progressbar" max="100" value=""></progress>
            </div>
            <div id="controls" style="float: left;">
                <!--
                <a href="#" id="volume" onclick="return false" title="Volumen">
                    <span class="control-icon volume-icon" aria-hidden="true"></span>
                </a>
                <a href="#" id="random" onclick="return false" title="Volumen">
                    <span class="control-icon norandom-icon" aria-hidden="true"></span>
                </a>
                -->
                <a href="#" id="search" onclick="return false" title="Filtrar">
                    <span class="control-icon search-icon" aria-hidden="true"></span>
                </a>
                <a href='#' id="speed" onclick="return false" title="Velocidad">
                    <span id="speed-value" aria-hidden="true">1.0x</span>
                </a>
                <!--
                <a href="#" id="download" onclick="return false" title="Descargar">
                    <span class="control-icon download-icon" aria-hidden="true"></span>
                </a>
                -->
            </div>
        </div>

        <div class="panel">
            <ul id="playlist">
                <li class="active">
	<span id="item-0">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/12/podcast19.mp3" title="Podcast 19 – Ciberseguridad con Yaiza Rubio y Ubucon 2018 en Gijón">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 19 – Ciberseguridad con Yaiza Rubio y Ubucon 2018 en Gijón</span>
		</a>
	</span>
</li>
<li>
	<span id="item-1">
		<a href="#" data-media="http://www.ivoox.com/linux-mint-18-3-como-actualizar_mf_22801021_feed_1.mp3" title="Linux Mint 18.3 ¿cómo actualizar?">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Linux Mint 18.3 ¿cómo actualizar?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-2">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-87-private-vlans.mp3" title="Podcast #87: Private Vlans">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #87: Private Vlans</span>
		</a>
	</span>
</li>
<li>
	<span id="item-3">
		<a href="#" data-media="http://www.ivoox.com/167-flasheando-android-one-xiaomi-mi_mf_22788031_feed_1.mp3" title="#167 Flasheando Android ONE en un Xiaomi Mi 5X vía TWRP">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#167 Flasheando Android ONE en un Xiaomi Mi 5X vía TWRP</span>
		</a>
	</span>
</li>
<li>
	<span id="item-4">
		<a href="#" data-media="http://www.ivoox.com/fire-tv-apps-amazon-prime-video_mf_22782774_feed_1.mp3" title="Fire TV, apps y Amazon Prime Vídeo">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Fire TV, apps y Amazon Prime Vídeo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-5">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-86-portainer-remoto.mp3" title="Podcast #86: Portainer y docker remoto">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #86: Portainer y docker remoto</span>
		</a>
	</span>
</li>
<li>
	<span id="item-6">
		<a href="#" data-media="https://ia801507.us.archive.org/12/items/2AplicacionesYReproductorDePodcast/2%20aplicaciones%20y%20reproductor%20de%20podcast.mp3" title="084. Rerproductor de Podcast y 2 App de Oferta">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">084. Rerproductor de Podcast y 2 App de Oferta</span>
		</a>
	</span>
</li>
<li>
	<span id="item-7">
		<a href="#" data-media="http://www.ivoox.com/41-gaming-gnu-linux_mf_22751215_feed_1.mp3" title="#41 Gaming y GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#41 Gaming y GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-8">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-85-cluster-de-proxmox.mp3" title="Podcast #85: Cluster con Proxmox">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #85: Cluster con Proxmox</span>
		</a>
	</span>
</li>
<li>
	<span id="item-9">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-84-paqueteria-snap.mp3" title="Podcast #84: Paquetería snap">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #84: Paquetería snap</span>
		</a>
	</span>
</li>
<li>
	<span id="item-10">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-83-conexion-ipv6-por-tunelbroker.mp3" title="Podcast #83: Conexión IPv6 por túnel broker">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #83: Conexión IPv6 por túnel broker</span>
		</a>
	</span>
</li>
<li>
	<span id="item-11">
		<a href="#" data-media="http://www.ivoox.com/linux-android-otras-noticias_mf_22680412_feed_1.mp3" title="Linux, Android y otras noticias">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Linux, Android y otras noticias</span>
		</a>
	</span>
</li>
<li>
	<span id="item-12">
		<a href="#" data-media="http://www.ivoox.com/166-linux-con-todos-respetos_mf_22668853_feed_1.mp3" title="#166 Linux: Con Todos Respetos">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#166 Linux: Con Todos Respetos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-13">
		<a href="#" data-media="https://ia601500.us.archive.org/0/items/NasVsServidorLinux/Nas%20vs%20Servidor%20Linux.mp3" title="083. Nas vs Servidor Linux">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">083. Nas vs Servidor Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-14">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-82-instalacion-mikrotik.mp3" title="Podcast #82: Instalación mikrotik de cliente">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #82: Instalación mikrotik de cliente</span>
		</a>
	</span>
</li>
<li>
	<span id="item-15">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-81-transitos-y-peering.mp3" title="Podcast #81: Tránsitos y peering">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #81: Tránsitos y peering</span>
		</a>
	</span>
</li>
<li>
	<span id="item-16">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-80-listas-de-spam.mp3" title="Podcast #80: Listas de Spam">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #80: Listas de Spam</span>
		</a>
	</span>
</li>
<li>
	<span id="item-17">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-79-ebtables.mp3" title="Podcast #79: ebtables">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #79: ebtables</span>
		</a>
	</span>
</li>
<li>
	<span id="item-18">
		<a href="#" data-media="https://ia601504.us.archive.org/25/items/SlimbookOneEl3En1/SlimbookOne_El_3_en_1.mp3" title="082. Slimbook One. El 3 en 1">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">082. Slimbook One. El 3 en 1</span>
		</a>
	</span>
</li>
<li>
	<span id="item-19">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-78-policy-routing-en-mikrotik.mp3" title="Podcast #78: Policy Routing en Mikrotik">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #78: Policy Routing en Mikrotik</span>
		</a>
	</span>
</li>
<li>
	<span id="item-20">
		<a href="#" data-media="https://www.ivoox.com/s02e03-distros-derivadas-entrevista-unav-linux-on_mf_22563701_feed_1.mp3" title="S02E03 Distros derivadas, entrevista uNav y Linux on Galaxy">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S02E03 Distros derivadas, entrevista uNav y Linux on Galaxy</span>
		</a>
	</span>
</li>
<li>
	<span id="item-21">
		<a href="#" data-media="http://www.ivoox.com/chromebooks-netbooks-revival_mf_22531698_feed_1.mp3" title="Chromebooks. Netbooks revival">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Chromebooks. Netbooks revival</span>
		</a>
	</span>
</li>
<li>
	<span id="item-22">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-77-opendns.mp3" title="Podcast #77: OpenDNS">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #77: OpenDNS</span>
		</a>
	</span>
</li>
<li>
	<span id="item-23">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-76-analizar-trafico-en-mikrotik.mp3" title="Podcast #76: Analizar tráfico en Mikrotik">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #76: Analizar tráfico en Mikrotik</span>
		</a>
	</span>
</li>
<li>
	<span id="item-24">
		<a href="#" data-media="http://www.ivoox.com/40-linux-connexion-aleix-pol_mf_22492088_feed_1.mp3" title="#40 Linux Connexion con Aleix Pol">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#40 Linux Connexion con Aleix Pol</span>
		</a>
	</span>
</li>
<li>
	<span id="item-25">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/especial-plataformas-de-podcasting-con-ivan-patxi.mp3" title="Especial: Plataformas de podcasting con Iván Patxi">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Especial: Plataformas de podcasting con Iván Patxi</span>
		</a>
	</span>
</li>
<li>
	<span id="item-26">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/12/podcast18.mp3" title="Podcast 18 – Desarrollo de Debian con Laura Arjona y Firefox Quantum">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 18 – Desarrollo de Debian con Laura Arjona y Firefox Quantum</span>
		</a>
	</span>
</li>
<li>
	<span id="item-27">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-75-multiples-gateways-multiples-interfaces.mp3" title="Podcast #75: Multiples gateways con múltiples interfaces">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #75: Multiples gateways con múltiples interfaces</span>
		</a>
	</span>
</li>
<li>
	<span id="item-28">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/12/podcast-74-varias-ips-mala-idea-constante.mp3" title="Podcast #74: Varias IPs en el mismo interfaz es mala idea">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #74: Varias IPs en el mismo interfaz es mala idea</span>
		</a>
	</span>
</li>
<li>
	<span id="item-29">
		<a href="#" data-media="http://www.ivoox.com/165-asi-lo-hacemos-apacoestrada77-aecollado-ayoyo308_mf_22424042_feed_1.mp3" title="#165 Asi? lo hacemos (@pacoestrada77 @ecollado @yoyo308)">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#165 Asi? lo hacemos (@pacoestrada77 @ecollado @yoyo308)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-30">
		<a href="#" data-media="https://anchor.fm/s/106db04/podcast/download/68109/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fanchor-data%2Fstationexports%2Fpodcasts%2FRecomendaciones-Y-Pr-ximo-Ep---4dadac040f951.m4a" title="081. Recomendaciones y Próximos Podcast">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">081. Recomendaciones y Próximos Podcast</span>
		</a>
	</span>
</li>
<li>
	<span id="item-31">
		<a href="#" data-media="http://www.ivoox.com/164-guiller-pedro-sanchez-yo-charleta-de_mf_22404222_feed_1.mp3" title="#164 Guiller, Pedro Sanchez y Yo: Charleta de Norte a Sur">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#164 Guiller, Pedro Sanchez y Yo: Charleta de Norte a Sur</span>
		</a>
	</span>
</li>
<li>
	<span id="item-32">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/especial-maraton-entrevista-jfebles.mp3" title="Especial: Entrevista a Juan Febles del Maratón Linuxero">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Especial: Entrevista a Juan Febles del Maratón Linuxero</span>
		</a>
	</span>
</li>
<li>
	<span id="item-33">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-73-migracion-correo.mp3" title="Podcast #73: Migración de servidor de correo">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #73: Migración de servidor de correo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-34">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-72-el-neogicio-del-dns.mp3" title="Podcast #72: El negocio del DNS">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #72: El negocio del DNS</span>
		</a>
	</span>
</li>
<li>
	<span id="item-35">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-71-lacp.mp3" title="Podcast #71: LACP">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #71: LACP</span>
		</a>
	</span>
</li>
<li>
	<span id="item-36">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-70-mi-web-no-tiene-candado-verde.mp3" title="Podcast #70: He instalado un certificado y mi web no muestra el candado verde">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #70: He instalado un certificado y mi web no muestra el candado verde</span>
		</a>
	</span>
</li>
<li>
	<span id="item-37">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-69-monitorizar-carga-web-desde-un-terminal.mp3" title="Podcast #69: Monitorizar carga de una web desde un terminal">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #69: Monitorizar carga de una web desde un terminal</span>
		</a>
	</span>
</li>
<li>
	<span id="item-38">
		<a href="#" data-media="http://www.ivoox.com/163-paypal-al-mover-dinero-no-te-emociones_mf_22283488_feed_1.mp3" title="#163 Paypal: Al mover dinero no te emociones, ojo con las comisiones">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#163 Paypal: Al mover dinero no te emociones, ojo con las comisiones</span>
		</a>
	</span>
</li>
<li>
	<span id="item-39">
		<a href="#" data-media="https://www.ivoox.com/s02e02-material-educativo-cuota-6-91-firefox-57_mf_22280032_feed_1.mp3" title="S02E02 Material educativo, cuota 6,91% y Firefox 57">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S02E02 Material educativo, cuota 6,91% y Firefox 57</span>
		</a>
	</span>
</li>
<li>
	<span id="item-40">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-68-sobre-dominios.mp3" title="Podcast #68: Sobre dominios">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #68: Sobre dominios</span>
		</a>
	</span>
</li>
<li>
	<span id="item-41">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-67-impresspages.mp3" title="Podcast #67: ImpressPages">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #67: ImpressPages</span>
		</a>
	</span>
</li>
<li>
	<span id="item-42">
		<a href="#" data-media="http://www.ivoox.com/39-gnu-linux-moviles_mf_22214993_feed_1.mp3" title="#39 GNU/Linux y Móviles">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#39 GNU/Linux y Móviles</span>
		</a>
	</span>
</li>
<li>
	<span id="item-43">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-66-medicion-del-ancho-de-banda.mp3" title="Podcast #66: Medición del ancho de banda">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #66: Medición del ancho de banda</span>
		</a>
	</span>
</li>
<li>
	<span id="item-44">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-65-tiendas-online-autogestionadas.mp3" title="Podcast #65: Tiendas online autogestionadas">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #65: Tiendas online autogestionadas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-45">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/11/podcast17.mp3" title="Podcast 17 – Robótica libre con Obijuan y Cumpleaños de Android">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 17 – Robótica libre con Obijuan y Cumpleaños de Android</span>
		</a>
	</span>
</li>
<li>
	<span id="item-46">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-64-migracion-a-firefox-quantum.mp3" title="Podcast #64: Migración a Firefox Quantum">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #64: Migración a Firefox Quantum</span>
		</a>
	</span>
</li>
<li>
	<span id="item-47">
		<a href="#" data-media="http://www.ivoox.com/intel-amd-windows-linux-android_mf_22160116_feed_1.mp3" title="Intel y Amd. Windows y Linux en Android. Chromebooks">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Intel y Amd. Windows y Linux en Android. Chromebooks</span>
		</a>
	</span>
</li>
<li>
	<span id="item-48">
		<a href="#" data-media="http://www.ivoox.com/cesta-tecnologica-sorteo-recaudacion-benefica_mf_22109813_feed_1.mp3" title="Cesta Tecnologica Sorteo y recaudación benéfica">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Cesta Tecnologica Sorteo y recaudación benéfica</span>
		</a>
	</span>
</li>
<li>
	<span id="item-49">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-63-autogestion-de-la-informacion.mp3" title="Podcast #63: Autogestión de la información">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #63: Autogestión de la información</span>
		</a>
	</span>
</li>
<li>
	<span id="item-50">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-62-seguridad-en-aplicaciones-web.mp3" title="Podcast #62: Seguridad en Aplicaciones Web con Sergio R. Solís">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #62: Seguridad en Aplicaciones Web con Sergio R. Solís</span>
		</a>
	</span>
</li>
<li>
	<span id="item-51">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/11/podcast16.mp3" title="Podcast 16 – Resumen LibreCon 2017 y Crossover NoLegalTech Radio">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 16 – Resumen LibreCon 2017 y Crossover NoLegalTech Radio</span>
		</a>
	</span>
</li>
<li>
	<span id="item-52">
		<a href="#" data-media="http://www.ivoox.com/off-topic-acoso-abuso-sexual-banalizacion_mf_22006102_feed_1.mp3" title="Off topic: Acoso y abuso sexual. Banalización">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Off topic: Acoso y abuso sexual. Banalización</span>
		</a>
	</span>
</li>
<li>
	<span id="item-53">
		<a href="#" data-media="https://ia601506.us.archive.org/0/items/80.HRecorderPro_201711/80.H-Recorder-pro.m4a" title="080. Grabadora de Audio en Oferta">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">080. Grabadora de Audio en Oferta</span>
		</a>
	</span>
</li>
<li>
	<span id="item-54">
		<a href="#" data-media="http://www.ivoox.com/162-disponible-opcion-donaciones-para-proyectos-salmorejo_mf_21982463_feed_1.mp3" title="#162 Disponible opción donaciones para los proyectos Salmorejo Geek y Killall Radio">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#162 Disponible opción donaciones para los proyectos Salmorejo Geek y Killall Radio</span>
		</a>
	</span>
</li>
<li>
	<span id="item-55">
		<a href="#" data-media="http://www.ivoox.com/38-linux-connexion-wikimedia-espana_mf_21944072_feed_1.mp3" title="#38 Linux Connexion con Wikimedia España">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#38 Linux Connexion con Wikimedia España</span>
		</a>
	</span>
</li>
<li>
	<span id="item-56">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-61-gestion-contenedores-con-portainer.mp3" title="Podcast #61: Gestión de contenedores Docker con portainer">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #61: Gestión de contenedores Docker con portainer</span>
		</a>
	</span>
</li>
<li>
	<span id="item-57">
		<a href="#" data-media="http://www.ivoox.com/w10-da-miedito-noche-halloween_mf_21890831_feed_1.mp3" title="w10 da miedito en la noche de Halloween">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">w10 da miedito en la noche de Halloween</span>
		</a>
	</span>
</li>
<li>
	<span id="item-58">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/11/podcast-60-primer-aniversario-del-podcast.mp3" title="Podcast #60: Primer aniversario del podcast">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #60: Primer aniversario del podcast</span>
		</a>
	</span>
</li>
<li>
	<span id="item-59">
		<a href="#" data-media="http://www.ivoox.com/161-como-partner-youtube-soy-os_mf_21887997_feed_1.mp3" title="#161 Como partner de Youtube que soy os debo una explicación">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#161 Como partner de Youtube que soy os debo una explicación</span>
		</a>
	</span>
</li>
<li>
	<span id="item-60">
		<a href="#" data-media="https://www.ivoox.com/s02e01-ubuntu-17-10-distros-100-libres_mf_21884774_feed_1.mp3" title="S02E01 Ubuntu 17.10 y distros 100% libres">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S02E01 Ubuntu 17.10 y distros 100% libres</span>
		</a>
	</span>
</li>
<li>
	<span id="item-61">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-59-victor-de-la-nuez.mp3" title="Podcast #59: Víctor de la Nuez de Wifi Canarias">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #59: Víctor de la Nuez de Wifi Canarias</span>
		</a>
	</span>
</li>
<li>
	<span id="item-62">
		<a href="#" data-media="http://www.ivoox.com/160-linux-mint-abandona-kde-corebird-1-7-mini_mf_21746395_feed_1.mp3" title="#160 Linux Mint abandona KDE, Corebird 1.7, mini Podcast personal en Telegram">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#160 Linux Mint abandona KDE, Corebird 1.7, mini Podcast personal en Telegram</span>
		</a>
	</span>
</li>
<li>
	<span id="item-63">
		<a href="#" data-media="https://anchor.fm/s/106db04/podcast/download/47948/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fanchor-data%2Fstationexports%2Fpodcasts%2FComo-enlazo-audios-a-Anchor-b378f648f54ec.m4a" title="079. Novedades Anchor y como enlazo mis Audios">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">079. Novedades Anchor y como enlazo mis Audios</span>
		</a>
	</span>
</li>
<li>
	<span id="item-64">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-58-rip.mp3" title="Podcast #58: RIP">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #58: RIP</span>
		</a>
	</span>
</li>
<li>
	<span id="item-65">
		<a href="#" data-media="https://anchor.fm/s/106db04/podcast/download/47146/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fanchor-data%2Fstationexports%2Fpodcasts%2FAplicaci-n-De-Podcast-Gratis--23f7b134c5844.m4a" title="078. Aplicación Gratis de Podcast y Música Streaming">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">078. Aplicación Gratis de Podcast y Música Streaming</span>
		</a>
	</span>
</li>
<li>
	<span id="item-66">
		<a href="#" data-media="https://anchor.fm/s/106db04/podcast/download/46801/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fanchor-data%2Fstationexports%2Fpodcasts%2FEsExplorer-Y-Otros-Exploradore-1a73fb172fa59.m4a" title="077.Android: Es Explorer y varios exploradores de Carpetas">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">077.Android: Es Explorer y varios exploradores de Carpetas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-67">
		<a href="#" data-media="http://www.ivoox.com/37-cultura-libre_mf_21673527_feed_1.mp3" title="#37 Cultura Libre">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#37 Cultura Libre</span>
		</a>
	</span>
</li>
<li>
	<span id="item-68">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-57-jitsi.mp3" title="Podcast #57: Jitsi">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #57: Jitsi</span>
		</a>
	</span>
</li>
<li>
	<span id="item-69">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-56-internet-y-la-aguja-hipotermica.mp3" title="Podcast #56: Internet y la aguja hipodérmica">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #56: Internet y la aguja hipodérmica</span>
		</a>
	</span>
</li>
<li>
	<span id="item-70">
		<a href="#" data-media="http://www.ivoox.com/159-2-distros-linux-1-swap-solucion-inicio_mf_21604893_feed_1.mp3" title="#159 2 distros Linux 1 Swap: Solución inicio lento (extra ACPI Error)">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#159 2 distros Linux 1 Swap: Solución inicio lento (extra ACPI Error)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-71">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-55-centros-de-datos-tomas-ledo.mp3" title="Podcast #55: Centros de Datos con Tomás Ledo">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #55: Centros de Datos con Tomás Ledo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-72">
		<a href="#" data-media="http://www.ivoox.com/158-un-truco-telegram-para-ser-mas-productivo_mf_21575863_feed_1.mp3" title="#158 Un truco Telegram para ser más productivo">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#158 Un truco Telegram para ser más productivo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-73">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/10/podcast15.mp3" title="Podcast 15 – Desarrollo de Gnome, Red Hat y Fedora . Librecon 2017.">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 15 – Desarrollo de Gnome, Red Hat y Fedora . Librecon 2017.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-74">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-54-hablamos-de-dominios-con-jorge-campanillas.mp3" title="Podcast #54: Hablamos de dominios con Jorge Campanillas">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #54: Hablamos de dominios con Jorge Campanillas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-75">
		<a href="#" data-media="http://www.ivoox.com/157-victorhck-in-the-free-world-gnu-linux-software_mf_21456955_feed_1.mp3" title="#157 Victorhck in The Free World: GNU/Linux, Software Libre, openSUSE y Gatos">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#157 Victorhck in The Free World: GNU/Linux, Software Libre, openSUSE y Gatos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-76">
		<a href="#" data-media="http://www.ivoox.com/36-linux-connexion-atareao_mf_21387751_feed_1.mp3" title="#36 Linux Connexion con Atareao">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#36 Linux Connexion con Atareao</span>
		</a>
	</span>
</li>
<li>
	<span id="item-77">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/10/podcast-53-bgp.mp3" title="Podcast #53: BGP">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #53: BGP</span>
		</a>
	</span>
</li>
<li>
	<span id="item-78">
		<a href="#" data-media="http://www.ivoox.com/156-mi-hdd-1tb-ha-muerto-y_mf_21322964_feed_1.mp3" title="#156 Mi HDD de 1TB ha muerto y se ha llevado parte de mí">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#156 Mi HDD de 1TB ha muerto y se ha llevado parte de mí</span>
		</a>
	</span>
</li>
<li>
	<span id="item-79">
		<a href="#" data-media="http://www.ivoox.com/155-ojo-la-scarlett-2i2-2nd-gen-firmware_mf_21315385_feed_1.mp3" title="#155 OJO: La Scarlett 2i2 2nd gen firmware 1116 no funciona en Linux">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#155 OJO: La Scarlett 2i2 2nd gen firmware 1116 no funciona en Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-80">
		<a href="#" data-media="http://www.ivoox.com/w10-update-creators-google-ia-iphone-mas_mf_21303021_feed_1.mp3" title="W10 Update Creators, Google, IA, Iphone y mas">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">W10 Update Creators, Google, IA, Iphone y mas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-81">
		<a href="#" data-media="http://www.ivoox.com/154-killall-radio-team-international-podcast-day_mf_21210309_feed_1.mp3" title="#154 Killall Radio Team International Podcast Day">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#154 Killall Radio Team International Podcast Day</span>
		</a>
	</span>
</li>
<li>
	<span id="item-82">
		<a href="#" data-media="http://www.ivoox.com/153-eugenia-bahit-el-dinero-no-es-un_mf_21189920_feed_1.mp3" title="#153 Eugenia Bahit: El dinero no es un incentivo, necesito otros retos">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#153 Eugenia Bahit: El dinero no es un incentivo, necesito otros retos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-83">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-52-por-que-el-correo-no-llega.mp3" title="Podcast #52: Por qué el correo no llega">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #52: Por qué el correo no llega</span>
		</a>
	</span>
</li>
<li>
	<span id="item-84">
		<a href="#" data-media="http://www.ivoox.com/152-rim-la-chica-sono-ser_mf_21136402_feed_1.mp3" title="#152 RIM: La chica que soñó con ser linuxera (un año después)">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#152 RIM: La chica que soñó con ser linuxera (un año después)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-85">
		<a href="#" data-media="http://www.ivoox.com/35-formatos-libres_mf_21117524_feed_1.mp3" title="#35 Formatos Libres">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#35 Formatos Libres</span>
		</a>
	</span>
</li>
<li>
	<span id="item-86">
		<a href="#" data-media="http://www.ivoox.com/151-extra-crossover-eduardo-yoyo-septiembre-2017_mf_21108291_feed_1.mp3" title="#151 Extra: Crossover Eduardo y Yoyo Septiembre 2017">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#151 Extra: Crossover Eduardo y Yoyo Septiembre 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-87">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/crossover-yoyo-eduardo-sep-2017.mp3" title="Extra: Crossover Yoyo y Eduardo Septiembre 2017">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Extra: Crossover Yoyo y Eduardo Septiembre 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-88">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/09/podcast14.mp3" title="Podcast 14 – Ordenadores con GNU/Linux preinstalado (Pcubuntu, Vant, Slimbook)">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 14 – Ordenadores con GNU/Linux preinstalado (Pcubuntu, Vant, Slimbook)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-89">
		<a href="#" data-media="http://www.ivoox.com/150-salmorejo-geek-finalista-8-edicion_mf_21046283_feed_1.mp3" title="#150 Salmorejo Geek finalista en la 8ª edición de los Premios de la Asociación Podcast de España">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#150 Salmorejo Geek finalista en la 8ª edición de los Premios de la Asociación Podcast de España</span>
		</a>
	</span>
</li>
<li>
	<span id="item-90">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-51-microweber.mp3" title="Podcast #51: MicroWeber">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #51: MicroWeber</span>
		</a>
	</span>
</li>
<li>
	<span id="item-91">
		<a href="#" data-media="http://www.ivoox.com/149-demasiado-telegram-usar-responsabilidad_mf_20904631_feed_1.mp3" title="#149 Demasiado Telegram, usar con responsabilidad">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#149 Demasiado Telegram, usar con responsabilidad</span>
		</a>
	</span>
</li>
<li>
	<span id="item-92">
		<a href="#" data-media="https://www.ivoox.com/s01extra02-desde-ubucon-europe-entrevistas-alan-pope-martin_mf_20826073_feed_1.mp3" title="S01Extra02 Desde Ubucon Europe: Entrevistas (Alan Pope, Martin Wimpress, Rudy y Miguel) & LexNET">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01Extra02 Desde Ubucon Europe: Entrevistas (Alan Pope, Martin Wimpress, Rudy y Miguel) & LexNET</span>
		</a>
	</span>
</li>
<li>
	<span id="item-93">
		<a href="#" data-media="http://www.ivoox.com/34-directo-maraton-linuxero_mf_20794227_feed_1.mp3" title="#34 Directo Maratón Linuxero">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#34 Directo Maratón Linuxero</span>
		</a>
	</span>
</li>
<li>
	<span id="item-94">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-50-sandstorm.mp3" title="Podcast #50: Sandstorm">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #50: Sandstorm</span>
		</a>
	</span>
</li>
<li>
	<span id="item-95">
		<a href="#" data-media="http://www.ivoox.com/blackview-a7-smartphone-sorprendente_mf_20776730_feed_1.mp3" title="Blackview A7. Smartphone sorprendente">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Blackview A7. Smartphone sorprendente</span>
		</a>
	</span>
</li>
<li>
	<span id="item-96">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-49-youphptube-tu-propio-you-tube.mp3" title="Podcast #49: YouPHPTube, tu propio You Tube">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #49: YouPHPTube, tu propio You Tube</span>
		</a>
	</span>
</li>
<li>
	<span id="item-97">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/09/Podcast13-MaratonLinuxero.mp3" title="Podcast 13 – Maratón Linuxero">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 13 – Maratón Linuxero</span>
		</a>
	</span>
</li>
<li>
	<span id="item-98">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-48-escritorio-en-la-nube-con-x2go.mp3" title="Podcast #48: Escritorio en la nube con x2Go">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #48: Escritorio en la nube con x2Go</span>
		</a>
	</span>
</li>
<li>
	<span id="item-99">
		<a href="#" data-media="https://ia601500.us.archive.org/19/items/076.UnServidorEnMiCasaMaratnLinuxero/076.%20Un%20Servidor%20en%20mi%20Casa%20-%20Marat%C3%B3n%20Linuxero.mp3" title="076. Un Servidor en mi Casa - Podcast del Maratón Linuxero 2017">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">076. Un Servidor en mi Casa - Podcast del Maratón Linuxero 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-100">
		<a href="#" data-media="http://www.ivoox.com/servidor-casero-ugeek-maraton-linuxero-3-9-17_mf_20680980_feed_1.mp3" title="Servidor Casero con ugeek en Maraton Linuxero 3/9/17">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Servidor Casero con ugeek en Maraton Linuxero 3/9/17</span>
		</a>
	</span>
</li>
<li>
	<span id="item-101">
		<a href="#" data-media="https://www.ivoox.com/s01extra01-maraton-linuxero-ubucon-europea-drm-en_mf_20679885_feed_1.mp3" title="S01Extra01 Maratón Linuxero. Ubucon Europea y DRM en HTML5">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01Extra01 Maratón Linuxero. Ubucon Europea y DRM en HTML5</span>
		</a>
	</span>
</li>
<li>
	<span id="item-102">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-47-directo-maraton-linuxero.mp3" title="Podcast #47: Mi intervención en el Maratón Linuxero">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #47: Mi intervención en el Maratón Linuxero</span>
		</a>
	</span>
</li>
<li>
	<span id="item-103">
		<a href="#" data-media="http://www.ivoox.com/148-24-horas-ml_mf_20652331_feed_1.mp3" title="#148 24 horas ML">
			<span class="isplaying"></span>
			<span class="logo salmorejogeek"></span>
			<span class="podcast">Salmorejo Geek</span>
			<span class="track">#148 24 horas ML</span>
		</a>
	</span>
</li>
<li>
	<span id="item-104">
		<a href="#" data-media="https://ia601508.us.archive.org/22/items/075.RespuestaDePreguntasYMaraton/075.%20Respuesta%20de%20Preguntas%20y%20Maraton.mp3" title="075. Respuestas a Preguntas de los Oyentes y Maratón Linuxero">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">075. Respuestas a Preguntas de los Oyentes y Maratón Linuxero</span>
		</a>
	</span>
</li>
<li>
	<span id="item-105">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/09/podcast-46-mejorar-apariencia-gnu-social.mp3" title="Podcast #46: Mejorar la imagen de GNU Social con Qvitter">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #46: Mejorar la imagen de GNU Social con Qvitter</span>
		</a>
	</span>
</li>
<li>
	<span id="item-106">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-45-instalacion-gnu-social.mp3" title="Podcast #45: Instalación de GNUSocial">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #45: Instalación de GNUSocial</span>
		</a>
	</span>
</li>
<li>
	<span id="item-107">
		<a href="#" data-media="https://ia601507.us.archive.org/20/items/074.NotasYFeed/074.%20Notas%20y%20Feed.mp3" title="074. Me explicáis como tomáis vuestras Notas. Y Que es uGeekRadio">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">074. Me explicáis como tomáis vuestras Notas. Y Que es uGeekRadio</span>
		</a>
	</span>
</li>
<li>
	<span id="item-108">
		<a href="#" data-media="http://www.ivoox.com/33-1-directo-podcast-linux_mf_20569029_feed_1.mp3" title="#33 1º Directo Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#33 1º Directo Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-109">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-44-la-red-en-gnu-linux.mp3" title="Podcast #44: Redes en GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #44: Redes en GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-110">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/08/podcast12.mp3" title="Podcast 12 – Empleo y Negocio en software libre con Carlos Rodriguez (Librebit-AGASOL) y Maratón Linuxero.">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 12 – Empleo y Negocio en software libre con Carlos Rodriguez (Librebit-AGASOL) y Maratón Linuxero.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-111">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-43-pfsense.mp3" title="Podcast #43: PfSense">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #43: PfSense</span>
		</a>
	</span>
</li>
<li>
	<span id="item-112">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-42-routers-en-gnu-linux.mp3" title="Podcast #42: Routers sobre GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #42: Routers sobre GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-113">
		<a href="#" data-media="http://www.ivoox.com/32-linux-connexion-reciclanet_mf_20316104_feed_1.mp3" title="#32 Linux Connexion con Reciclanet">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#32 Linux Connexion con Reciclanet</span>
		</a>
	</span>
</li>
<li>
	<span id="item-114">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-41-maraton-grabacion-y-transmision.mp3" title="Podcast #41: Maratón Linuxsero, grabación de podcast y transmisión en vídeo">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #41: Maratón Linuxsero, grabación de podcast y transmisión en vídeo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-115">
		<a href="#" data-media="http://www.ivoox.com/instalacion-nuevo-disco-hibrido-sshd-tests-en_mf_20255876_feed_1.mp3" title="Instalación nuevo disco híbrido SSHD y tests en Linux">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Instalación nuevo disco híbrido SSHD y tests en Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-116">
		<a href="#" data-media="https://ia601501.us.archive.org/17/items/073.PorqueSeDescargaTanRapido/073.%20Porque_se_descarga_tan_rapido.mp3" title="073. ¿Porque se descarga tan rápido la batería de mi Android?">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">073. ¿Porque se descarga tan rápido la batería de mi Android?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-117">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-40-big-data-con-inigo-gonzalez.mp3" title="Podcast #40: Big Data con Iñigo González">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #40: Big Data con Iñigo González</span>
		</a>
	</span>
</li>
<li>
	<span id="item-118">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-39-ispconfig.mp3" title="Podcast #39: ISPConfig">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #39: ISPConfig</span>
		</a>
	</span>
</li>
<li>
	<span id="item-119">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/08/podcast11.mp3" title="Podcast 11 – Comunicación en GNU/Linux con Paul Brown y resumen de Akademy 2017">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 11 – Comunicación en GNU/Linux con Paul Brown y resumen de Akademy 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-120">
		<a href="#" data-media="https://ia601505.us.archive.org/24/items/072.Anchor/072.%20Anchor.mp3" title="072. Anchor">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">072. Anchor</span>
		</a>
	</span>
</li>
<li>
	<span id="item-121">
		<a href="#" data-media="http://www.ivoox.com/amazon-attcliente-vodafone-mas_mf_20173322_feed_1.mp3" title="Amazon AttCliente, Vodafone y más">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Amazon AttCliente, Vodafone y más</span>
		</a>
	</span>
</li>
<li>
	<span id="item-122">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/08/podcast-38-fail2ban.mp3" title="Podcast #38: Fail2ban">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #38: Fail2ban</span>
		</a>
	</span>
</li>
<li>
	<span id="item-123">
		<a href="#" data-media="http://www.ivoox.com/31-especial-tlp2017_mf_20075548_feed_1.mp3" title="#31 Especial TLP2017">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#31 Especial TLP2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-124">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/07/podcast-37-login-radius-en-mikrotik.mp3" title="Podcast #37: Login Radius en Mikrotik">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #37: Login Radius en Mikrotik</span>
		</a>
	</span>
</li>
<li>
	<span id="item-125">
		<a href="#" data-media="https://ia601502.us.archive.org/29/items/071.CopiaRemotaDeVuestraSDMasSnaps/071.%20Copia%20remota%20de%20vuestra%20SD,%20Mas%20snap's.mp3" title="071. Copia Remota De Vuestra SD, Mas Snap's">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">071. Copia Remota De Vuestra SD, Mas Snap's</span>
		</a>
	</span>
</li>
<li>
	<span id="item-126">
		<a href="#" data-media="http://www.ivoox.com/movilidad-sin-pc-libros-uso-datos-compras-y_mf_19915687_feed_1.mp3" title="Movilidad sin PC, libros, uso datos, compras y programación">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Movilidad sin PC, libros, uso datos, compras y programación</span>
		</a>
	</span>
</li>
<li>
	<span id="item-127">
		<a href="#" data-media="http://www.ivoox.com/30-especial-maraton-linuxero_mf_19835582_feed_1.mp3" title="#30 Especial Maratón Linuxero">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#30 Especial Maratón Linuxero</span>
		</a>
	</span>
</li>
<li>
	<span id="item-128">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/07/podcast10.mp3" title="Podcast 10 – Akademy 2017 y China hacia GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 10 – Akademy 2017 y China hacia GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-129">
		<a href="#" data-media="https://ia801500.us.archive.org/2/items/070.EficienciaEnRaspberryYNotas/070.%20Eficiencia%20en%20Raspberry%20y%20Notas.mp3" title="070. Eficiencia de servicios y aplicaciones. Notas entre Keep, OneNote, Paper, Emacs...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">070. Eficiencia de servicios y aplicaciones. Notas entre Keep, OneNote, Paper, Emacs...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-130">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/07/podcast-36-directo-pre-verano.mp3" title="Podcast #36: Directo pre-verano">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #36: Directo pre-verano</span>
		</a>
	</span>
</li>
<li>
	<span id="item-131">
		<a href="#" data-media="https://www.ivoox.com/s01e07-fairphone-fsf_mf_19689764_feed_1.mp3" title="S01E07 Fairphone y FSF">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E07 Fairphone y FSF</span>
		</a>
	</span>
</li>
<li>
	<span id="item-132">
		<a href="#" data-media="http://www.ivoox.com/raspberry-pi-emilcar_mf_19648096_feed_1.mp3" title="Raspberry pi y Emilcar">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Raspberry pi y Emilcar</span>
		</a>
	</span>
</li>
<li>
	<span id="item-133">
		<a href="#" data-media="https://ia601505.us.archive.org/23/items/069.RaspberryPi.SiONo/069.%20Raspberry%20Pi.%20Si%20o%20no.mp3" title="069. Raspberry Pi. ¿Esta hecha para mi?">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">069. Raspberry Pi. ¿Esta hecha para mi?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-134">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/07/podcast9.mp3" title="Podcast 9 – Especial Open Expo 2017">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 9 – Especial Open Expo 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-135">
		<a href="#" data-media="http://www.ivoox.com/29-linux-connexion-alejandro-lopez-2_mf_19635497_feed_1.mp3" title="#29 Linux Connexion con Alejandro López (2)">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#29 Linux Connexion con Alejandro López (2)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-136">
		<a href="#" data-media="https://ia601505.us.archive.org/11/items/68ComoTenerMasEspacioEnTuMovil/68-Como%20tener%20mas%20espacio%20en%20tu%20movil.mp3" title="068. Android: Limpia tu telefono por dentro">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">068. Android: Limpia tu telefono por dentro</span>
		</a>
	</span>
</li>
<li>
	<span id="item-137">
		<a href="#" data-media="https://ia601507.us.archive.org/16/items/67Miscelanea/67-Miscelanea.mp3" title="067. Miscelánea. Nextcloud 12, Resilio, Rsync...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">067. Miscelánea. Nextcloud 12, Resilio, Rsync...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-138">
		<a href="#" data-media="http://www.ivoox.com/canon-digital-vodafone-te-clava-factura-y_mf_19631584_feed_1.mp3" title="Canon Digital, Vodafone te clava en factura y Xiaomi mi 5">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Canon Digital, Vodafone te clava en factura y Xiaomi mi 5</span>
		</a>
	</span>
</li>
<li>
	<span id="item-139">
		<a href="#" data-media="http://www.ivoox.com/28-especial-aniversario_mf_19570639_feed_1.mp3" title="#28 Especial Aniversario">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#28 Especial Aniversario</span>
		</a>
	</span>
</li>
<li>
	<span id="item-140">
		<a href="#" data-media="http://www.ivoox.com/slimbook-pro-linux-ultrabook_mf_19542755_feed_1.mp3" title="Slimbook Pro Linux Ultrabook">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Slimbook Pro Linux Ultrabook</span>
		</a>
	</span>
</li>
<li>
	<span id="item-141">
		<a href="#" data-media="https://ia601507.us.archive.org/15/items/NextcloudResilioSyncthingQueNubeElijoo/Nextcloud%2c%20Resilio%2c%20Syncthing%20%c2%bfQue%20Nube%20elijo%3f.mp3" title="066. Nextcloud, Resilio, Syncthing... ¿Que Nube elijo?">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">066. Nextcloud, Resilio, Syncthing... ¿Que Nube elijo?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-142">
		<a href="#" data-media="https://www.ivoox.com/s01e06-ubuntu-rolling-abandono-arquitectura-32_mf_19444625_feed_1.mp3" title="S01E06 Ubuntu rolling y abandono de arquitectura 32 bits">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E06 Ubuntu rolling y abandono de arquitectura 32 bits</span>
		</a>
	</span>
</li>
<li>
	<span id="item-143">
		<a href="#" data-media="http://www.ivoox.com/era-post-pc-wintablet_mf_19407609_feed_1.mp3" title="Era Post PC con Wintablet">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Era Post PC con Wintablet</span>
		</a>
	</span>
</li>
<li>
	<span id="item-144">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/06/20crossoverlinuxerodirectosobregnom-systeminside-ivoox19395669.mp3" title="Podcast 8 – Crossover Linuxero: Directo sobre GNOME, Plasma y otras hierbas">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 8 – Crossover Linuxero: Directo sobre GNOME, Plasma y otras hierbas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-145">
		<a href="#" data-media="https://ia601502.us.archive.org/7/items/065.Tiddlywiki/065.%20tiddlywiki.mp3" title="065. TiddlyWiki. Una Wiki en un único archivo y multiplataforma.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">065. TiddlyWiki. Una Wiki en un único archivo y multiplataforma.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-146">
		<a href="#" data-media="http://www.ivoox.com/27-especial-slimbook-one_mf_19385447_feed_1.mp3" title="#27 Especial Slimbook One">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#27 Especial Slimbook One</span>
		</a>
	</span>
</li>
<li>
	<span id="item-147">
		<a href="#" data-media="http://www.ivoox.com/27-especial-slimbook-one_mf_21151729_feed_1.mp3" title="#27 Especial Slimbook One">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#27 Especial Slimbook One</span>
		</a>
	</span>
</li>
<li>
	<span id="item-148">
		<a href="#" data-media="http://www.ivoox.com/ipad-pro-sustituto-del-pc_mf_19348017_feed_1.mp3" title="Ipad Pro ¿sustituto del PC?">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Ipad Pro ¿sustituto del PC?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-149">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/06/podcast7.mp3" title="Podcast 7 -Fundación Apache con Ignasi Barrera y el cumpleaños de TUX">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 7 -Fundación Apache con Ignasi Barrera y el cumpleaños de TUX</span>
		</a>
	</span>
</li>
<li>
	<span id="item-150">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/06/podcast-35-montar-dos-routers-bgp.mp3" title="Podcast #35: Montar dos routers frontera BGP">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #35: Montar dos routers frontera BGP</span>
		</a>
	</span>
</li>
<li>
	<span id="item-151">
		<a href="#" data-media="https://ia801501.us.archive.org/34/items/064.ResilioLaNubeDondeElControlLoTienesTu/064.%20Resilio,%20La%20nube%20donde%20el%20control%20lo%20tienes%20tu.mp3" title="064. Resilio. Una Nube Ilimitada, donde el control de tus datos los tienes tu.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">064. Resilio. Una Nube Ilimitada, donde el control de tus datos los tienes tu.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-152">
		<a href="#" data-media="https://ia801502.us.archive.org/3/items/ConLinuxEsPosible/Con%20Linux%20es%20posible.mp3" title="063. Con Linux es posible">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">063. Con Linux es posible</span>
		</a>
	</span>
</li>
<li>
	<span id="item-153">
		<a href="#" data-media="https://www.ivoox.com/s01e05-comprar-pcs-ubuntu-desbandada-desarrolladores-canonical_mf_19187730_feed_1.mp3" title="S01E05 Comprar PCs con Ubuntu, desbandada desarrolladores Canonical y Chrome ha ganado ¿qué puede hacer Mozilla?">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E05 Comprar PCs con Ubuntu, desbandada desarrolladores Canonical y Chrome ha ganado ¿qué puede hacer Mozilla?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-154">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/06/podcast-34-servicio-de-correo.mp3" title="Podcast #34: Servicio de correo">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #34: Servicio de correo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-155">
		<a href="#" data-media="http://www.ivoox.com/slimbook-excalibur-portatil-linux-x3_mf_19185139_feed_1.mp3" title="Slimbook Excálibur Portátil con Linux x3">
			<span class="isplaying"></span>
			<span class="logo mosqueterowebtecnologialinuxchromebooks"></span>
			<span class="podcast">Mosqueteroweb tecnologia, Linux, Chromebooks</span>
			<span class="track">Slimbook Excálibur Portátil con Linux x3</span>
		</a>
	</span>
</li>
<li>
	<span id="item-156">
		<a href="#" data-media="https://ia801505.us.archive.org/28/items/062.DomoticaConMiRasperry./062.%20Domotica%20con%20mi%20Rasperry..mp3" title="062. Domótica con mi Raspberry Pi. Usemos el GPIO">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">062. Domótica con mi Raspberry Pi. Usemos el GPIO</span>
		</a>
	</span>
</li>
<li>
	<span id="item-157">
		<a href="#" data-media="http://www.ivoox.com/26-linux-connexion-ugeek_mf_19127057_feed_1.mp3" title="#26 Linux Connexion con Ugeek">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#26 Linux Connexion con Ugeek</span>
		</a>
	</span>
</li>
<li>
	<span id="item-158">
		<a href="#" data-media="https://www.ivoox.com/s01e04-software-libre-educacion_mf_19068060_feed_1.mp3" title="S01E04 Software libre en la educación">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E04 Software libre en la educación</span>
		</a>
	</span>
</li>
<li>
	<span id="item-159">
		<a href="#" data-media="https://www.ivoox.com/s01e03-seguridad-privacidad_mf_19058066_feed_1.mp3" title="S01E03 Seguridad y privacidad">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E03 Seguridad y privacidad</span>
		</a>
	</span>
</li>
<li>
	<span id="item-160">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/06/podcast-33-virtualizacion-personal.mp3" title="Podcast #33: Virtualiación personal con VMWare Workstation y Virtualbox">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #33: Virtualiación personal con VMWare Workstation y Virtualbox</span>
		</a>
	</span>
</li>
<li>
	<span id="item-161">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/06/podcast-32-especial-openexpo.mp3" title="Podcast #32: Especial OpenExpo 2017">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #32: Especial OpenExpo 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-162">
		<a href="#" data-media="https://ia601502.us.archive.org/23/items/DockerEnMenosDe10Min/Docker%20en%20menos%20de%2010%20min.mp3" title="061. Docker en 10 minutos">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">061. Docker en 10 minutos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-163">
		<a href="#" data-media="https://ia601504.us.archive.org/9/items/TerminalAlias/Terminal%20alias.mp3" title="060. La Terminal mas fácil con alias">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">060. La Terminal mas fácil con alias</span>
		</a>
	</span>
</li>
<li>
	<span id="item-164">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/05/podcast-31-migracion-a-kde-neon.mp3" title="Podcast #31: Migración a KDE Neón 5.9">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #31: Migración a KDE Neón 5.9</span>
		</a>
	</span>
</li>
<li>
	<span id="item-165">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/05/podcast6.mp3" title="Podcast 6 – openSuse y KDE con Antonio Larrosa . OpenExpo2017">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 6 – openSuse y KDE con Antonio Larrosa . OpenExpo2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-166">
		<a href="#" data-media="https://ia801505.us.archive.org/21/items/059.2AplicacinesParaTomarNotas/059.%202%20Aplicaci%C3%B3nes%20para%20tomar%20Notas.mp3" title="059. 2 Aplicaciones de Notas alternativas que utilizo">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">059. 2 Aplicaciones de Notas alternativas que utilizo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-167">
		<a href="#" data-media="https://ia601502.us.archive.org/10/items/058.Android.AppCloneMultipleAccounts/058.%20Android.%20App%20clone%20-%20Multiple%20Accounts.m4a" title="058. Android: Multicuentas. Gestion de Servicios Raspberry Pi">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">058. Android: Multicuentas. Gestion de Servicios Raspberry Pi</span>
		</a>
	</span>
</li>
<li>
	<span id="item-168">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/05/podcast-30-instalacion-freepbx.mp3" title="Podcast #30: Instalación de FreePBX">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #30: Instalación de FreePBX</span>
		</a>
	</span>
</li>
<li>
	<span id="item-169">
		<a href="#" data-media="https://www.ivoox.com/s01e02-gnome3-ubports_mf_18807244_feed_1.mp3" title="S01E02 GNOME3 y UBPorts">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E02 GNOME3 y UBPorts</span>
		</a>
	</span>
</li>
<li>
	<span id="item-170">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/05/podcast-29-calidad-de-servicio-en-linux.mp3" title="Podcast #29: Calidad de servicio en GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #29: Calidad de servicio en GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-171">
		<a href="#" data-media="https://ia801500.us.archive.org/13/items/057.MulticuentaTelegramWire/057.%20Multicuenta%20telegram,%20wire.mp3" title="057. Multicuenta de Telegram en tu PC de escritorio y Wire">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">057. Multicuenta de Telegram en tu PC de escritorio y Wire</span>
		</a>
	</span>
</li>
<li>
	<span id="item-172">
		<a href="#" data-media="https://ia801503.us.archive.org/12/items/056.VideoderYLlamadasTelegram/056.%20Videoder%20y%20llamadas%20Telegram.mp3" title="056. Android: Videoder y llamadas de Telegram">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">056. Android: Videoder y llamadas de Telegram</span>
		</a>
	</span>
</li>
<li>
	<span id="item-173">
		<a href="#" data-media="https://ia801506.us.archive.org/9/items/055.M4aAplicacionesDePodcastYNuevoMicro/055.%20M4a,%20aplicaciones%20de%20Podcast%20y%20nuevo%20micro.mp3" title="055. Nuevos Cambios...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">055. Nuevos Cambios...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-174">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/05/podcast5.mp3" title="Podcast 5 – Radios Libres. Microsoft y su “amor” por GNU/Linux.">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 5 – Radios Libres. Microsoft y su “amor” por GNU/Linux.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-175">
		<a href="#" data-media="https://ia601507.us.archive.org/31/items/054.TelefnicaEstaSiendoAtacada/054.%20Telef%C3%B3nica%20esta%20siendo%20atacada!%20.mp3" title="054. Telefónica esta siendo Atacada!!!">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">054. Telefónica esta siendo Atacada!!!</span>
		</a>
	</span>
</li>
<li>
	<span id="item-176">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/05/podcast-28-ipv6-segunda-parte.mp3" title="Podcast #28: IPv6 (segunda parte)">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #28: IPv6 (segunda parte)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-177">
		<a href="#" data-media="http://www.ivoox.com/24-linux-connexion-davidochobits_mf_18604559_feed_1.mp3" title="#24 Linux Connexion con DavidOchoBits">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#24 Linux Connexion con DavidOchoBits</span>
		</a>
	</span>
</li>
<li>
	<span id="item-178">
		<a href="#" data-media="https://ia601502.us.archive.org/7/items/053.Synapse/053.%20Synapse%20.mp3" title="053. Synapse">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">053. Synapse</span>
		</a>
	</span>
</li>
<li>
	<span id="item-179">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/05/podcast-27-ipv6-primera-parte.mp3" title="Podcast #27: IPv6 (primera parte)">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #27: IPv6 (primera parte)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-180">
		<a href="#" data-media="https://ia601506.us.archive.org/33/items/JekyllOWordpress/Jekyll%20o%20Wordpress.mp3" title="052. ¿Jekyll o WordPress?">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">052. ¿Jekyll o WordPress?</span>
		</a>
	</span>
</li>
<li>
	<span id="item-181">
		<a href="#" data-media="https://ia801502.us.archive.org/5/items/051.AdisBloggerHolaGithub/051.%20Adi%C3%B3s%20Blogger,%20Hola%20Github%20.mp3" title="051. Adiós Blogger, Hola GitHub!">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">051. Adiós Blogger, Hola GitHub!</span>
		</a>
	</span>
</li>
<li>
	<span id="item-182">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/05/podcast-26-odoo-y-transformacion.mp3" title="Podcast #26: Odoo y transformación digital">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #26: Odoo y transformación digital</span>
		</a>
	</span>
</li>
<li>
	<span id="item-183">
		<a href="#" data-media="https://ia801505.us.archive.org/9/items/050.QueAndoHaciendo/050.%20Que%20ando%20haciendo.mp3" title="050. Que ando haciendo, nuevas publicaciones y más...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">050. Que ando haciendo, nuevas publicaciones y más...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-184">
		<a href="#" data-media="https://ia601503.us.archive.org/0/items/049.Syncthing/049.%20Syncthing.mp3" title="049. Instalando Syncthing en Ubuntu, Antergos y Raspberry Pi">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">049. Instalando Syncthing en Ubuntu, Antergos y Raspberry Pi</span>
		</a>
	</span>
</li>
<li>
	<span id="item-185">
		<a href="#" data-media="http://compilando.audio/wp-content/uploads/2017/04/podcast4.mp3" title="Podcast 4 – Jon “maddog” Hall , Open South Code y Linux y Tapas">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 4 – Jon “maddog” Hall , Open South Code y Linux y Tapas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-186">
		<a href="#" data-media="https://ia601503.us.archive.org/28/items/EncuentroDeAmiguetes/Encuentro%20de%20amiguetes.mp3" title="048. Encuentro de amiguetes">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">048. Encuentro de amiguetes</span>
		</a>
	</span>
</li>
<li>
	<span id="item-187">
		<a href="#" data-media="https://www.ivoox.com/s01e01-ubuntu-mata-unity-movil_mf_18361665_feed_1.mp3" title="S01E01 Ubuntu mata Unity y el móvil">
			<span class="isplaying"></span>
			<span class="logo ubuntuyotrashierbas"></span>
			<span class="podcast">Ubuntu y otras hierbas</span>
			<span class="track">S01E01 Ubuntu mata Unity y el móvil</span>
		</a>
	</span>
</li>
<li>
	<span id="item-188">
		<a href="#" data-media="http://www.ivoox.com/23-la-terminal_mf_18347303_feed_1.mp3" title="#23 La Terminal">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#23 La Terminal</span>
		</a>
	</span>
</li>
<li>
	<span id="item-189">
		<a href="#" data-media="http://www.ivoox.com/23-la-terminal_mf_21151730_feed_1.mp3" title="#23 La Terminal">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#23 La Terminal</span>
		</a>
	</span>
</li>
<li>
	<span id="item-190">
		<a href="#" data-media="https://ia801500.us.archive.org/21/items/SeEstropeaLaSDDeMiRasberry/Se%20estropea%20la%20SD%20de%20mi%20rasberry.mp3" title="047. Se quemó la SD. Comparación de consumos entre PC, NAS-Microserver, Raspberry Pi">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">047. Se quemó la SD. Comparación de consumos entre PC, NAS-Microserver, Raspberry Pi</span>
		</a>
	</span>
</li>
<li>
	<span id="item-191">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/04/podcast-25-introduccion-a-docker.mp3" title="Podcast #25: Introducción a Docker">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #25: Introducción a Docker</span>
		</a>
	</span>
</li>
<li>
	<span id="item-192">
		<a href="#" data-media="https://ia601509.us.archive.org/6/items/046SyncthingResilioYDukto/%23046%20Syncthing%2c%20Resilio%20y%20Dukto%20.mp3" title="046. Sincronización de carpetas entre dispositivos. Syncthing, Resilio y Dukto">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">046. Sincronización de carpetas entre dispositivos. Syncthing, Resilio y Dukto</span>
		</a>
	</span>
</li>
<li>
	<span id="item-193">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/04/podcast-24-sobre-vlans.mp3" title="Podcast #24: Sobre Vlans">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #24: Sobre Vlans</span>
		</a>
	</span>
</li>
<li>
	<span id="item-194">
		<a href="#" data-media="http://www.ivoox.com/22-linux-connexion-osl-la_mf_18133189_feed_1.mp3" title="#22 Linux Connexion con la OSL de la Universidad de La Laguna">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#22 Linux Connexion con la OSL de la Universidad de La Laguna</span>
		</a>
	</span>
</li>
<li>
	<span id="item-195">
		<a href="#" data-media="https://ia801505.us.archive.org/27/items/045CrossoverConSalmorejoGeek/%23045%20Crossover%20con%20Salmorejo%20Geek.mp3" title="045. Crossover con Salmorejo Geek, donde hablamos de Mastodon, Ubuntu, Telegram y mucho mas...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">045. Crossover con Salmorejo Geek, donde hablamos de Mastodon, Ubuntu, Telegram y mucho mas...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-196">
		<a href="#" data-media="https://ia801504.us.archive.org/22/items/044WebDeJekyllEnGithub/%23044%20Web%20de%20Jekyll%20en%20Github.mp3" title="044. La web de Jekyll en GitHub, va tomando forma">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">044. La web de Jekyll en GitHub, va tomando forma</span>
		</a>
	</span>
</li>
<li>
	<span id="item-197">
		<a href="#" data-media="https://ia601509.us.archive.org/23/items/043BotDeTelegramDeIFTTT/%23043%20Bot%20de%20Telegram%20de%20IFTTT.mp3" title="043. Bot de Telegram IFTTT">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">043. Bot de Telegram IFTTT</span>
		</a>
	</span>
</li>
<li>
	<span id="item-198">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/04/podcast-23-calcular-mascaras-de-red.mp3" title="Podcast #23: Calcular máscaras de red">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #23: Calcular máscaras de red</span>
		</a>
	</span>
</li>
<li>
	<span id="item-199">
		<a href="#" data-media="https://ia601502.us.archive.org/25/items/042ElAtareaoVisitaElCrossoverDeLaSemana/%23042%20El%20Atareao%20visita%20el%20Crossover%20de%20la%20Semana.mp3" title="042. El Atareao visita el Crossover de la Semana">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">042. El Atareao visita el Crossover de la Semana</span>
		</a>
	</span>
</li>
<li>
	<span id="item-200">
		<a href="#" data-media="https://compilando.audio/wp-content/uploads/2017/04/Podcast_3.mp3" title="Podcast 3 – Entrevista con ” el atareao” y el nuevo rumbo de Ubuntu">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 3 – Entrevista con ” el atareao” y el nuevo rumbo de Ubuntu</span>
		</a>
	</span>
</li>
<li>
	<span id="item-201">
		<a href="#" data-media="https://ia801502.us.archive.org/1/items/041UbuntuYElAdiosAUnity/%23041%20Ubuntu%20y%20el%20adi%c3%b3s%20a%20Unity.mp3" title="041. Ubuntu y el adios de Unity">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">041. Ubuntu y el adios de Unity</span>
		</a>
	</span>
</li>
<li>
	<span id="item-202">
		<a href="#" data-media="https://ia801504.us.archive.org/29/items/40AntergosOCNewsDeNextcloudYJekyll/%2340%20Antergos%2c%20OCNews%20de%20Nextcloud%20y%20Jekyll%20.mp3" title="040. Antergos, Ocnews De Nextcloud Y Jekyll">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">040. Antergos, Ocnews De Nextcloud Y Jekyll</span>
		</a>
	</span>
</li>
<li>
	<span id="item-203">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/04/podcast-22-iptables-en-gnu-linux.mp3" title="Podcast #22: NAT en GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #22: NAT en GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-204">
		<a href="#" data-media="https://ia601508.us.archive.org/2/items/039TelegramNotes/%23039%20Telegram%2c%20Notes.mp3" title="039. Aplicación Notes de Nextcloud y crea tus bots de Telegram">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">039. Aplicación Notes de Nextcloud y crea tus bots de Telegram</span>
		</a>
	</span>
</li>
<li>
	<span id="item-205">
		<a href="#" data-media="https://compilando.audio/wp-content/uploads/2017/04/CompilandoPodcast2.mp3" title="Podcast 2 – Especial Servidores Privados">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 2 – Especial Servidores Privados</span>
		</a>
	</span>
</li>
<li>
	<span id="item-206">
		<a href="#" data-media="https://compilando.audio/wp-content/uploads/2017/04/podcast_1.mp3" title="Podcast 1- Ian Murdock, Debian y el proyecto QSL">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 1- Ian Murdock, Debian y el proyecto QSL</span>
		</a>
	</span>
</li>
<li>
	<span id="item-207">
		<a href="#" data-media="https://archive.org/download/PODCAST0_201704/PODCAST_0.mp3" title="Podcast 0 – Edición de presentación. Stallman y el síndrome Mi Pueblex.">
			<span class="isplaying"></span>
			<span class="logo compilandopodcast"></span>
			<span class="podcast">Compilando Podcast</span>
			<span class="track">Podcast 0 – Edición de presentación. Stallman y el síndrome Mi Pueblex.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-208">
		<a href="#" data-media="https://ia601506.us.archive.org/26/items/38CrossoverConMosqueteroWeb/%23%2038%20Crossover%20con%20MosqueteroWeb.mp3" title="038. Crossover con MosqueteroWeb. Masterclass de FreeNas, Docker y virtualización mediante Proxmox y Esxi.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">038. Crossover con MosqueteroWeb. Masterclass de FreeNas, Docker y virtualización mediante Proxmox y Esxi.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-209">
		<a href="#" data-media="https://ia801503.us.archive.org/18/items/037LlamadasDeTelegram/%23037%20Llamadas%20de%20Telegram.mp3" title="037. Llamadas de Telegram ya estan aquí. Y 3 bots que os encantaran">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">037. Llamadas de Telegram ya estan aquí. Y 3 bots que os encantaran</span>
		</a>
	</span>
</li>
<li>
	<span id="item-210">
		<a href="#" data-media="https://ia601509.us.archive.org/25/items/036PodcastConFrank/%23036%20podcast%20con%20Frank.mp3" title="036. Podcast con Frank de Batería2x100, Servidores Linux y NAS, lo mismo pero  diferente">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">036. Podcast con Frank de Batería2x100, Servidores Linux y NAS, lo mismo pero  diferente</span>
		</a>
	</span>
</li>
<li>
	<span id="item-211">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-21-lets-encrypt.mp3" title="Podcast #21: Let’s Encrypt">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #21: Let’s Encrypt</span>
		</a>
	</span>
</li>
<li>
	<span id="item-212">
		<a href="#" data-media="http://www.ivoox.com/21-gnu-linux-universidad_mf_17834272_feed_1.mp3" title="#21 GNU/Linux en la Universidad">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#21 GNU/Linux en la Universidad</span>
		</a>
	</span>
</li>
<li>
	<span id="item-213">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-20-como-ganar-dinero-con-el-podcast.mp3" title="Podcast #20: Cómo ganar dinero con el podcast">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #20: Cómo ganar dinero con el podcast</span>
		</a>
	</span>
</li>
<li>
	<span id="item-214">
		<a href="#" data-media="https://ia601501.us.archive.org/10/items/035MiG8/%23035%20Mi%20G8.mp3" title="035. Mi HP ProLiant MicroServer Gen8">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">035. Mi HP ProLiant MicroServer Gen8</span>
		</a>
	</span>
</li>
<li>
	<span id="item-215">
		<a href="#" data-media="https://ia801500.us.archive.org/9/items/034BotDeTelegramSustitutoAShazam/%23034%20Bot%20de%20Telegram%20sustituto%20a%20Shazam.mp3" title="034. Bots de Telegram Sustitutos a Shazam y busqueda de articulos dentro del bot de Pocket">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">034. Bots de Telegram Sustitutos a Shazam y busqueda de articulos dentro del bot de Pocket</span>
		</a>
	</span>
</li>
<li>
	<span id="item-216">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-19-openvpn.mp3" title="Podcast #19: OpenVPN">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #19: OpenVPN</span>
		</a>
	</span>
</li>
<li>
	<span id="item-217">
		<a href="#" data-media="https://ia601500.us.archive.org/4/items/033BotDePocketParaTelegram/%23033%20Bot%20de%20Pocket%20para%20Telegram.mp3" title="033. Bots en Telegram. Bot de Pocket">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">033. Bots en Telegram. Bot de Pocket</span>
		</a>
	</span>
</li>
<li>
	<span id="item-218">
		<a href="#" data-media="https://ia601606.us.archive.org/30/items/032MiscelaneaDeViernes/%23032%20Miscel%C3%A1nea%20de%20Viernes.mp3" title="032. Miscelánea de Viernes">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">032. Miscelánea de Viernes</span>
		</a>
	</span>
</li>
<li>
	<span id="item-219">
		<a href="#" data-media="https://ia601606.us.archive.org/14/items/031Keepass.ComoGestionoMisContrasenas/%23031%20Keepass.%20Como%20gestiono%20mis%20contrase%C3%B1as.mp3" title="031. Keepass, como gestiono mis contraseñas">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">031. Keepass, como gestiono mis contraseñas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-220">
		<a href="#" data-media="https://ia601609.us.archive.org/0/items/030Mumble/%23030%20Mumble.mp3" title="030. Mumble, VoIP de Software Libre. Nextcloud, Wallabag y kdenlive">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">030. Mumble, VoIP de Software Libre. Nextcloud, Wallabag y kdenlive</span>
		</a>
	</span>
</li>
<li>
	<span id="item-221">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-18-herramientas-simples-y-utiles-para-un-adminsitrador-de-red.mp3" title="Podcast #18: Herramientas simples y útiles para un adminsitrador de red">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #18: Herramientas simples y útiles para un adminsitrador de red</span>
		</a>
	</span>
</li>
<li>
	<span id="item-222">
		<a href="#" data-media="https://ia601608.us.archive.org/28/items/029MiscelneaDeViernes/%23029%20Miscel%C3%A1nea%20de%20viernes.mp3" title="029. Miscelánea de Viernes.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">029. Miscelánea de Viernes.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-223">
		<a href="#" data-media="https://ia601607.us.archive.org/17/items/ugeekpodcast_gmail_XMPP/XMPP.mp3" title="028. Instala un servidor de mensajeria tipo Whatsapp o Telegram y de Software Libre con XMPP/Jabber">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">028. Instala un servidor de mensajeria tipo Whatsapp o Telegram y de Software Libre con XMPP/Jabber</span>
		</a>
	</span>
</li>
<li>
	<span id="item-224">
		<a href="#" data-media="http://www.ivoox.com/20-linux-connexion-david-montalva-lliurex_mf_17557164_feed_1.mp3" title="#20 Linux Connexion con David Montalva (Lliurex)">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#20 Linux Connexion con David Montalva (Lliurex)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-225">
		<a href="#" data-media="https://ia601606.us.archive.org/3/items/027InstalaTuVpnEnUbuntuORaspberryPi/%23027%20instala%20tu%20vpn%20en%20Ubuntu%20o%20Raspberry%20Pi.mp3" title="027. Instala una VPN (OpenVpn) en Ubuntu o Raspberry Pi con PiVpn">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">027. Instala una VPN (OpenVpn) en Ubuntu o Raspberry Pi con PiVpn</span>
		</a>
	</span>
</li>
<li>
	<span id="item-226">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-17-sistemas-de-monitorizacion-de-sistemas-y-red.mp3" title="Podcast #17: Sistemas de monitorización de sistemas y red">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #17: Sistemas de monitorización de sistemas y red</span>
		</a>
	</span>
</li>
<li>
	<span id="item-227">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-16-directo-11-marzo-2017.mp3" title="Podcast #16: Directo 11 de Marzo 2017">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #16: Directo 11 de Marzo 2017</span>
		</a>
	</span>
</li>
<li>
	<span id="item-228">
		<a href="#" data-media="https://ia601606.us.archive.org/25/items/026PodcastConFrankDeBatera2x100/%23026%20Podcast%20con%20Frank%20de%20Bater%C3%ADa2x100.mp3" title="026. Podcast con Frank de Batería2x100, Hablamos de como gestionamos nuestras Fotos, actualidad y sorteo del libro del año">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">026. Podcast con Frank de Batería2x100, Hablamos de como gestionamos nuestras Fotos, actualidad y sorteo del libro del año</span>
		</a>
	</span>
</li>
<li>
	<span id="item-229">
		<a href="#" data-media="https://ia601600.us.archive.org/16/items/025MtodoMMsCompletoQueParaRecopilarNotasOrgMode/%23025%20M%C3%A9todo%20m%C3%A1s%20completo%20que%20para%20recopilar%20notas%2C%20org%20mode.mp3" title="025. Metodo mas completo para recopilar notas, org Mode">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">025. Metodo mas completo para recopilar notas, org Mode</span>
		</a>
	</span>
</li>
<li>
	<span id="item-230">
		<a href="#" data-media="https://ia601605.us.archive.org/10/items/024ConectateRemotamenteATuRaspberryPiCondataplicity/%23024%20Conectate%20remotamente%20a%20tu%20Raspberry%20Pi%20con%20%22dataplicity%22%20.mp3" title="024. Conectate remotamente a tu Raspberry Pi con "dataplicity"">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">024. Conectate remotamente a tu Raspberry Pi con "dataplicity"</span>
		</a>
	</span>
</li>
<li>
	<span id="item-231">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/03/podcast-15-mumble.mp3" title="Podcast #15: Mumble, tu mesa de reuniones virtual">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #15: Mumble, tu mesa de reuniones virtual</span>
		</a>
	</span>
</li>
<li>
	<span id="item-232">
		<a href="#" data-media="https://ia801609.us.archive.org/20/items/EntrevistaADosDesarrolladoresDeSoftwareLibreDeIgalia/Entrevista%20a%20dos%20desarrolladores%20de%20Software%20Libre%20de%20Igalia.mp3" title="023. Entrevista a Chema y Juan, dos desarrolladores de Software Libre de Igalia.com en el #mwc17">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">023. Entrevista a Chema y Juan, dos desarrolladores de Software Libre de Igalia.com en el #mwc17</span>
		</a>
	</span>
</li>
<li>
	<span id="item-233">
		<a href="#" data-media="https://ia601600.us.archive.org/33/items/EntrevistaConArturoSuarezDirectivoDelCloudDeCanonicalUbuntu/Entrevista%20con%20Arturo%20Suarez,%20Directivo%20del%20Cloud%20de%20Canonical%20Ubuntu.mp3" title="022. Entrevista con Arturo Suarez, DIrectivo del Cloud de Canonical Ubuntu">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">022. Entrevista con Arturo Suarez, DIrectivo del Cloud de Canonical Ubuntu</span>
		</a>
	</span>
</li>
<li>
	<span id="item-234">
		<a href="#" data-media="http://www.ivoox.com/19-gnu-linux-escuela_mf_17289281_feed_1.mp3" title="#19 GNU/Linux en la escuela">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#19 GNU/Linux en la escuela</span>
		</a>
	</span>
</li>
<li>
	<span id="item-235">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/02/podcast-14-radio-o-podcast.mp3" title="Podcast #14: Radio o Podcast, no elijas puedes tener las dos">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #14: Radio o Podcast, no elijas puedes tener las dos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-236">
		<a href="#" data-media="https://ia801606.us.archive.org/21/items/021UbuntuEnMobileWorldCongress/%23021%20ubuntu%20en%20Mobile%20World%20Congress%20.mp3" title="021. Ubuntu en el Mobile World Congress">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">021. Ubuntu en el Mobile World Congress</span>
		</a>
	</span>
</li>
<li>
	<span id="item-237">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/02/podcast-13-ospf-multiarea.mp3" title="Podcast #13: OSPF Multiárea">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #13: OSPF Multiárea</span>
		</a>
	</span>
</li>
<li>
	<span id="item-238">
		<a href="#" data-media="https://ia601601.us.archive.org/7/items/20PodcastConFrankDeBatera2x100HablamosDeComoGestionamosNuestraNotas/%2320%20Podcast%20con%20Frank%20de%20Bater%c3%ada2x100%2c%20Hablamos%20de%20como%20gestionamos%20nuestra%20notas%20.mp3" title="020. Podcast con Frank de Batería2x100, Hablamos de como gestionamos nuestra notas y mucho mas...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">020. Podcast con Frank de Batería2x100, Hablamos de como gestionamos nuestra notas y mucho mas...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-239">
		<a href="#" data-media="https://ia601603.us.archive.org/6/items/019DokuwikiNuevaFormaDeTomarMisNotas/%23019%20Dokuwiki%2c%20nueva%20forma%20de%20tomar%20mis%20notas%20.mp3" title="019. Dokuwiki, nueva forma de tomar mis notas. Monta tu wiki con DokuWiki o MediaWiki.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">019. Dokuwiki, nueva forma de tomar mis notas. Monta tu wiki con DokuWiki o MediaWiki.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-240">
		<a href="#" data-media="https://ia601604.us.archive.org/24/items/018WallabagElPocketOInstapaper/%23018_Wallabag%2c_el_Pocket_o_Instapaper.mp3" title="018. Como montar Wallabag, el Pocket o Instapaper de software libre y lo mejor de todo, en tu servidor">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">018. Como montar Wallabag, el Pocket o Instapaper de software libre y lo mejor de todo, en tu servidor</span>
		</a>
	</span>
</li>
<li>
	<span id="item-241">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/02/podcast-12-atencion-al-cliente-y-migrar-una-web.mp3" title="Podcast #12: Atención al cliente y migrar una web">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #12: Atención al cliente y migrar una web</span>
		</a>
	</span>
</li>
<li>
	<span id="item-242">
		<a href="#" data-media="https://ia801300.us.archive.org/34/items/017PodcastConFrankDeBateria2x100HablandoDePlexNextcloud.../%23017%20Podcast%20con%20Frank%20de%20Bateria2x100%2c%20hablando%20de%20Plex%2c%20Nextcloud....mp3" title="017. Podcast con Frank de Bateria2x100, hablando de Plex, Nextcloud...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">017. Podcast con Frank de Bateria2x100, hablando de Plex, Nextcloud...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-243">
		<a href="#" data-media="https://ia801603.us.archive.org/24/items/016QueEsUnServidor/%23016%20Que%20es%20un%20servidor.mp3" title="016. Que es un Servidor (dudas oyentes), servidor web, ...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">016. Que es un Servidor (dudas oyentes), servidor web, ...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-244">
		<a href="#" data-media="https://ia801603.us.archive.org/20/items/015AlmacenamientoTheNextcloud/%23015_almacenamiento_the_nextcloud.mp3" title="015. Como ampliar el almacenamiento de Nextcloud, combinar con nubes publicas y hacer copias de mis fotos.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">015. Como ampliar el almacenamiento de Nextcloud, combinar con nubes publicas y hacer copias de mis fotos.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-245">
		<a href="#" data-media="https://ia601602.us.archive.org/11/items/NotasEnNextcloud/Notas%20en%20nextcloud.mp3" title="014. Notas en Nextcloud y Markdown">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">014. Notas en Nextcloud y Markdown</span>
		</a>
	</span>
</li>
<li>
	<span id="item-246">
		<a href="#" data-media="https://ia801601.us.archive.org/21/items/013NewsYFreshRSS.GestorDeNoticiasRSS/%23013%20News%20y%20Fresh%20RSS.%20Gestor%20de%20Noticias%20RSS.mp3" title="013. News y FreshRSS. Gestor de Noticias RSS.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">013. News y FreshRSS. Gestor de Noticias RSS.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-247">
		<a href="#" data-media="https://ia801604.us.archive.org/21/items/013FDroidAplicacionesDeSoftwareLibre/%23013%20F-Droid%20Aplicaciones%20de%20Software%20Libre.mp3" title="013. bis F-Droid Tienda Android de aplicaciones de Software Libre y Actualizar las Noticias en Nextcloud.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">013. bis F-Droid Tienda Android de aplicaciones de Software Libre y Actualizar las Noticias en Nextcloud.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-248">
		<a href="#" data-media="https://ia801601.us.archive.org/24/items/012CmoActualizarNextcloudY/%23012_c%c3%b3mo_actualizar_Nextcloud_y.mp3" title="012. Como actualizar Nextcloud y salir del modo de "mantenimiento"">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">012. Como actualizar Nextcloud y salir del modo de "mantenimiento"</span>
		</a>
	</span>
</li>
<li>
	<span id="item-249">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/02/podcast-11-ospf-en-un-area.mp3" title="Podcast #11: OSPF en un único área">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #11: OSPF en un único área</span>
		</a>
	</span>
</li>
<li>
	<span id="item-250">
		<a href="#" data-media="https://ia801602.us.archive.org/16/items/011PodcastConFrankDeBateria2x100/%23011%20Podcast%20con%20Frank%20de%20Bateria2x100.mp3" title="011. Podcast con Frank de Bateria2x100, hablando un poco de todo...">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">011. Podcast con Frank de Bateria2x100, hablando un poco de todo...</span>
		</a>
	</span>
</li>
<li>
	<span id="item-251">
		<a href="#" data-media="https://ia601603.us.archive.org/9/items/010ElSistemaOperativoDeBolsillo/%23010%20El%20Sistema%20Operativo%20de%20bolsillo.mp3" title="010. CloudReady el Chromium OS de bolsillo">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">010. CloudReady el Chromium OS de bolsillo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-252">
		<a href="#" data-media="https://ia601602.us.archive.org/11/items/ComoCrearTuPodcastYTotalmenteGtatis/Como%20crear%20tu%20podcast%20y%20totalmente%20gtatis.mp3" title="009. Crea tu podcast en 3 simples pasos y totalmente gratis">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">009. Crea tu podcast en 3 simples pasos y totalmente gratis</span>
		</a>
	</span>
</li>
<li>
	<span id="item-253">
		<a href="#" data-media="https://ia801900.us.archive.org/13/items/008ComoGestionoMisNotas/%23008%20Como%20gestiono%20mis%20notas.mp3" title="008. Como gestiono mis Notas">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">008. Como gestiono mis Notas</span>
		</a>
	</span>
</li>
<li>
	<span id="item-254">
		<a href="#" data-media="hhttps://ia601902.us.archive.org/28/items/007LinuxEsUnaAlternativaReal/%23007%20Linux%20es%20una%20alternativa%20real.mp3" title="007. Linux es una alternativa real">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">007. Linux es una alternativa real</span>
		</a>
	</span>
</li>
<li>
	<span id="item-255">
		<a href="#" data-media="https://ia601900.us.archive.org/18/items/ElTrelloDeSoftwareLibreWekan/El_Trello_de_software_libre_Wekan.mp3" title="006. El Trello de Software Libre Wekan y Kanboard para Raspberry Pi. El sistema Kanban en tu servidor.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">006. El Trello de Software Libre Wekan y Kanboard para Raspberry Pi. El sistema Kanban en tu servidor.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-256">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/02/podcast-10-dns-y-arp.mp3" title="Podcast #10: Cómo funciona el DNS">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #10: Cómo funciona el DNS</span>
		</a>
	</span>
</li>
<li>
	<span id="item-257">
		<a href="#" data-media="https://ia601603.us.archive.org/9/items/005PaperDeDropbox/%23005%20Paper%20de%20Dropbox.mp3" title="005. Paper de Dropbox">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">005. Paper de Dropbox</span>
		</a>
	</span>
</li>
<li>
	<span id="item-258">
		<a href="#" data-media="http://www.ivoox.com/17-linux-connexion-alexandre-filgueira_mf_16768269_feed_1.mp3" title="#17 Linux Connexion con Alexandre Filgueira">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#17 Linux Connexion con Alexandre Filgueira</span>
		</a>
	</span>
</li>
<li>
	<span id="item-259">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/01/podcast-9-streaming-con-icecat2-mp3.mp3" title="Podcast #9: Streaming con Icecast 2">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #9: Streaming con Icecast 2</span>
		</a>
	</span>
</li>
<li>
	<span id="item-260">
		<a href="#" data-media="https://ia601903.us.archive.org/19/items/004ServidorLinuxVsQNapSynology/%23004%20Servidor%20Linux%20Vs%20QNap-Synology.mp3" title="004. Servidor Linux Vs QNAP-Synology">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">004. Servidor Linux Vs QNAP-Synology</span>
		</a>
	</span>
</li>
<li>
	<span id="item-261">
		<a href="#" data-media="https://ia601903.us.archive.org/4/items/003Nextcloud/%23003%20Nextcloud.mp3" title="003. Nextcloud. Instalar tu Nube en menos de 2 minutos.">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">003. Nextcloud. Instalar tu Nube en menos de 2 minutos.</span>
		</a>
	</span>
</li>
<li>
	<span id="item-262">
		<a href="#" data-media="https://ia801904.us.archive.org/20/items/DeQueVaEstoDeUGeek/De%20que%20va%20esto%20de%20uGeek%3f.mp3" title="002. "De qué va esto de uGeek?"">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">002. "De qué va esto de uGeek?"</span>
		</a>
	</span>
</li>
<li>
	<span id="item-263">
		<a href="#" data-media="https://ia801602.us.archive.org/21/items/HolaMundo_201701/Hola%20Mundo.mp3" title="001. Hola Mundo">
			<span class="isplaying"></span>
			<span class="logo ugeektecnologíaandroidlinuxservidoresymuchomás"></span>
			<span class="podcast">uGeek - Tecnología, Android, Linux, Servidores y mucho más...</span>
			<span class="track">001. Hola Mundo</span>
		</a>
	</span>
</li>
<li>
	<span id="item-264">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/01/podcast-8-el-viaje-de-cargar-una-web.mp3" title="Podcast #8: El viaje de cargar una web">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #8: El viaje de cargar una web</span>
		</a>
	</span>
</li>
<li>
	<span id="item-265">
		<a href="#" data-media="http://www.ivoox.com/16-antergos_mf_16451726_feed_1.mp3" title="#16 Antergos">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#16 Antergos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-266">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2017/01/podcast-7-cableado.mp3" title="Podcast #7: Cableado en un Centro de Datos">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #7: Cableado en un Centro de Datos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-267">
		<a href="#" data-media="http://www.ivoox.com/15-linux-connexion-jen0f0nte_mf_15880251_feed_1.mp3" title="#15 Linux Connexion con Jen0f0nte">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#15 Linux Connexion con Jen0f0nte</span>
		</a>
	</span>
</li>
<li>
	<span id="item-268">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-6-almacenamiento.mp3" title="Podcast #6: Almacenamiento">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #6: Almacenamiento</span>
		</a>
	</span>
</li>
<li>
	<span id="item-269">
		<a href="#" data-media="http://www.ivoox.com/14-especial-slimbook-katana_mf_15380402_feed_1.mp3" title="#14 Especial Slimbook Katana">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#14 Especial Slimbook Katana</span>
		</a>
	</span>
</li>
<li>
	<span id="item-270">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-5-cloud-centros-de-datos.mp3" title="Podcast #5: Introducción al Cloud y servicios de Centros de Datos">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #5: Introducción al Cloud y servicios de Centros de Datos</span>
		</a>
	</span>
</li>
<li>
	<span id="item-271">
		<a href="#" data-media="http://www.ivoox.com/13-ciberseguridad-basica-gnu-linux_mf_14880771_feed_1.mp3" title="#13 Ciberseguridad Básica en GNU/Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#13 Ciberseguridad Básica en GNU/Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-272">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-4-ssl-spam-postventa-de-apple.mp3" title="Podcast #4: SSL, spam y postventa de Apple">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #4: SSL, spam y postventa de Apple</span>
		</a>
	</span>
</li>
<li>
	<span id="item-273">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-3-como-crear-un-podcast.mp3" title="Podcast #3: Cómo crear un podcast">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #3: Cómo crear un podcast</span>
		</a>
	</span>
</li>
<li>
	<span id="item-274">
		<a href="#" data-media="http://www.ivoox.com/12-linux-connexion-alejandro-lopez-slimbook_mf_14164009_feed_1.mp3" title="#12 Linux Connexion con Alejandro López ( Slimbook )">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#12 Linux Connexion con Alejandro López ( Slimbook )</span>
		</a>
	</span>
</li>
<li>
	<span id="item-275">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-2-crud-en-rails-formularios-dinamicos.mp3" title="Podcast #2: Git, CRUD en Rails y Formularios dinámicos en HTML con JavaScript">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #2: Git, CRUD en Rails y Formularios dinámicos en HTML con JavaScript</span>
		</a>
	</span>
</li>
<li>
	<span id="item-276">
		<a href="#" data-media="http://www.ivoox.com/11-linux-connexion-gabriel-viso-pitando-net-podcast_mf_13759097_feed_1.mp3" title="#11 Linux Connexion con Gabriel Viso (Pitando.net). Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#11 Linux Connexion con Gabriel Viso (Pitando.net). Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-277">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-1-presentacion-rails-lynda.mp3" title="Podcast #1: Presentación, Rails y Lynda.com">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #1: Presentación, Rails y Lynda.com</span>
		</a>
	</span>
</li>
<li>
	<span id="item-278">
		<a href="#" data-media="https://media.blubrry.com/eduardocollado/www.eduardocollado.com/wp-content/uploads/2016/12/podcast-0.mp3" title="Podcast #0: Presentación">
			<span class="isplaying"></span>
			<span class="logo podcastdeeduardocollado"></span>
			<span class="podcast">Podcast de Eduardo Collado</span>
			<span class="track">Podcast #0: Presentación</span>
		</a>
	</span>
</li>
<li>
	<span id="item-279">
		<a href="#" data-media="http://www.ivoox.com/09-especial-lenovo-thinkpad-x220_mf_13265714_feed_1.mp3" title="#09 Especial Lenovo ThinkPad X220">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#09 Especial Lenovo ThinkPad X220</span>
		</a>
	</span>
</li>
<li>
	<span id="item-280">
		<a href="#" data-media="http://www.ivoox.com/08-sabores-a-montones_mf_13103580_feed_1.mp3" title="#08 Sabores a montones">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#08 Sabores a montones</span>
		</a>
	</span>
</li>
<li>
	<span id="item-281">
		<a href="#" data-media="http://www.ivoox.com/07-linux-connexion-huezo-grupo-telegram_mf_12912418_feed_1.mp3" title="#07 Linux Connexion con Huezo (Grupo Telegram GNU-Linux)">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#07 Linux Connexion con Huezo (Grupo Telegram GNU-Linux)</span>
		</a>
	</span>
</li>
<li>
	<span id="item-282">
		<a href="#" data-media="http://www.ivoox.com/07-linux-connexion-huezo-grupo-telegram-gnu-linux_mf_13383404_feed_1.mp3" title="#07 Linux Connexion con Huezo (Grupo Telegram GNU/Linux) Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#07 Linux Connexion con Huezo (Grupo Telegram GNU/Linux) Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-283">
		<a href="#" data-media="http://www.ivoox.com/06-conlinuxsisepuede_mf_12737297_feed_1.mp3" title="#06 #ConLinuxSíSePuede">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#06 #ConLinuxSíSePuede</span>
		</a>
	</span>
</li>
<li>
	<span id="item-284">
		<a href="#" data-media="http://www.ivoox.com/06-conlinuxsisepuede-podcast-linux_mf_13383405_feed_1.mp3" title="#06 #ConLinuxSíSePuede. Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#06 #ConLinuxSíSePuede. Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-285">
		<a href="#" data-media="http://www.ivoox.com/05-linux-connexion-yoyo-fernandez_mf_12593330_feed_1.mp3" title="#05 Linux Connexion con Yoyo Fernández">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#05 Linux Connexion con Yoyo Fernández</span>
		</a>
	</span>
</li>
<li>
	<span id="item-286">
		<a href="#" data-media="http://www.ivoox.com/05-linux-connexion-yoyo-fernandez_mf_13383406_feed_1.mp3" title="#05 Linux Connexion con Yoyo Fernández">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#05 Linux Connexion con Yoyo Fernández</span>
		</a>
	</span>
</li>
<li>
	<span id="item-287">
		<a href="#" data-media="http://www.ivoox.com/04-amor-distro-madre_mf_12520959_feed_1.mp3" title="#04 Amor de (Distro) madre">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#04 Amor de (Distro) madre</span>
		</a>
	</span>
</li>
<li>
	<span id="item-288">
		<a href="#" data-media="http://www.ivoox.com/04-amor-distro-madre-podcast-linux_mf_13383407_feed_1.mp3" title="#04 Amor de Distro Madre. Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#04 Amor de Distro Madre. Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-289">
		<a href="#" data-media="http://www.ivoox.com/03-y-no-estaba-muerto-no-no_mf_12374536_feed_1.mp3" title="#03 Y no estaba muerto, no no">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#03 Y no estaba muerto, no no</span>
		</a>
	</span>
</li>
<li>
	<span id="item-290">
		<a href="#" data-media="http://www.ivoox.com/03-y-no-estaba-muerto-no-no-podcast_mf_13383408_feed_1.mp3" title="#03 Y no estaba muerto, no, no. Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#03 Y no estaba muerto, no, no. Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-291">
		<a href="#" data-media="http://www.ivoox.com/02-un-pinguino-mi-usb_mf_12218805_feed_1.mp3" title="#02 Un pingüino en mi USB">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#02 Un pingüino en mi USB</span>
		</a>
	</span>
</li>
<li>
	<span id="item-292">
		<a href="#" data-media="http://www.ivoox.com/02-un-pinguino-mi-usb-podcast-linux_mf_13383409_feed_1.mp3" title="#02 Un pingüino en mi USB Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#02 Un pingüino en mi USB Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-293">
		<a href="#" data-media="http://www.ivoox.com/01-antecedentes_mf_12085902_feed_1.mp3" title="#01 Antecedentes">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#01 Antecedentes</span>
		</a>
	</span>
</li>
<li>
	<span id="item-294">
		<a href="#" data-media="http://www.ivoox.com/00-promo-podcast-linux_mf_12048502_feed_1.mp3" title="#00 Promo Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#00 Promo Podcast Linux</span>
		</a>
	</span>
</li>
<li>
	<span id="item-295">
		<a href="#" data-media="http://www.ivoox.com/00-promo-podcast-linux_mf_13383411_feed_1.mp3" title="#00 Promo Podcast Linux">
			<span class="isplaying"></span>
			<span class="logo podcastlinux"></span>
			<span class="podcast">Podcast Linux</span>
			<span class="track">#00 Promo Podcast Linux</span>
		</a>
	</span>
</li>


            </ul>
        </div>
    </div> <!-- .entry -->
</article> <!-- article -->
