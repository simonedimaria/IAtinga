from bs4 import BeautifulSoup
import requests

# Example HTML content
html_content = """

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="TODO">
        <meta name="keywords" content="TODO">
        <meta name="author" content="Alberto Harka">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Iotinga</title>
        <link rel="icon" type="image/png" href="assets/favicon.png"/>

        <!-- <link rel="stylesheet" href="assets/css/animations.css"/>
        <link rel="stylesheet" href="assets/css/style.css"/>
        <link rel="stylesheet" href="assets/css/style-tablet.css"/>
        <link rel="stylesheet" href="assets/css/style-mobile.css"/>
        <link rel="stylesheet" href="assets/css/loader.css"/>
        <link rel="stylesheet" href="assets/css/scroll.css"/>
        <script type="text/javascript" src="assets/js/loader.js"></script>
        <script type="text/javascript" src="assets/js/scripts.js"></script>
        <script type="text/javascript" src="assets/js/jquery-3.6.0.min.js"></script> -->
        <link rel="stylesheet" href="assets/css/style.min.css"/>
        <script type="text/javascript" src="assets/js/scripts.min.js"></script>
        <script type="text/javascript" src="assets/js/jquery-3.6.0.min.js"></script>
        <style>
          img.prize {
            height:110px;
            width:auto;
          }
          @media only screen and (max-width: 1200px) {}
          @media only screen and (min-width: 1366px) {}
          @media only screen and (max-width: 1164px) {}
          @media only screen and (max-width: 768px) {
              img.prize {
                display: none;
              }
          }
          @media only screen and (max-width: 376px) {}
        </style>
    </head>
    <body>
        <div id="loader-wrapper" class="loader-wrapper">
            <span class="loader"><span class="loader-inner"></span></span>
        </div>
        <div id="main-wrapper" class="main-wrapper">
            <section id="space-section" class="space-section">
                <div class="hero">
                    <div class="header">
                        <div class="logo-container"><a href="/">
                            <?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 26.0.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Livello_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 183.88 196.67" style="enable-background:new 0 0 183.88 196.67;" xml:space="preserve" nopulse>

<g class="st0">
	<g class="st1">
		<path class="st2" d="M642.92-247.46v18.08h4.97v5.34h-16.64v-5.34h5.01v-18.08h-5.01v-5.34h16.64v5.34H642.92z"/>
	</g>
	<g class="st1">
		<path class="st2" d="M651.1-238.42c0-8.55,6.66-14.88,15.74-14.88c9.04,0,15.74,6.29,15.74,14.88c0,8.59-6.7,14.88-15.74,14.88
			C657.76-223.55,651.1-229.88,651.1-238.42z M675.84-238.42c0-5.47-3.86-9.21-9-9.21c-5.14,0-9,3.74-9,9.21c0,5.46,3.86,9.2,9,9.2
			C671.97-229.22,675.84-232.96,675.84-238.42z"/>
	</g>
	<g class="st1">
		<path class="st2" d="M707.65-244.75c-2.47-1.44-5.05-2.34-7.93-2.75v23.46h-6.66v-23.46c-2.83,0.41-5.46,1.32-7.97,2.75
			l-2.26-4.97c3.99-2.38,8.71-3.58,13.52-3.58c4.85,0,9.62,1.19,13.56,3.58L707.65-244.75z"/>
		<path class="st2" d="M722.77-247.46v18.08h4.97v5.34H711.1v-5.34h5.01v-18.08h-5.01v-5.34h16.64v5.34H722.77z"/>
		<path class="st2" d="M758.9-240.89v16.85h-6.66v-16.64c0-4.73-2.38-6.94-6.12-6.94c-3.86,0-6.7,2.34-6.7,7.4v16.19h-6.66v-28.76
			h6.45v3.49c1.97-2.67,5.01-3.99,8.79-3.99C754.83-253.3,758.9-248.9,758.9-240.89z"/>
		<path class="st2" d="M784.91-238.87h6.08v14.83h-5.01v-1.73c-2.05,1.52-4.68,2.22-7.72,2.22c-7.85,0-14.59-5.18-14.59-14.63
			c0-8.92,6.66-15.12,15.82-15.12c5.05,0,9.25,1.73,12.04,4.97l-4.27,3.94c-2.1-2.22-4.52-3.25-7.44-3.25
			c-5.59,0-9.41,3.74-9.41,9.41c0,6.08,4.07,9.12,8.63,9.12c2.18,0,4.23-0.62,5.88-1.97V-238.87z"/>
		<path class="st2" d="M823.3-239.78v15.74h-6.66v-6.9h-13.15v6.9h-6.58v-15.74c0-8.75,5.3-13.52,13.19-13.52
			S823.3-248.53,823.3-239.78z M816.64-236.29v-4.11c0-4.89-2.63-7.23-6.58-7.23c-3.99,0-6.57,2.34-6.57,7.23v4.11H816.64z"/>
	</g>
</g>
<g>
	<path d="M148.15,45.07c2.46,7.48-1.62,15.53-9.1,17.99c-7.48,2.46-15.53-1.62-17.99-9.1c-2.46-7.48,1.62-15.53,9.09-17.99
		C137.64,33.52,145.69,37.59,148.15,45.07"/>
	<path d="M155.84,77.35c-1.68-5.1-3.91-9.87-6.6-14.25c-2.22,2.4-5.07,4.29-8.4,5.38c-10.47,3.44-21.75-2.26-25.19-12.74
		c-2.21-6.73-0.64-13.8,3.54-18.9c-14.69-6.52-31.76-7.82-48.23-2.41c-35.29,11.59-54.5,49.6-42.91,84.89
		c11.59,35.29,49.6,54.5,84.89,42.91C148.21,150.64,167.43,112.64,155.84,77.35 M139.36,124.08c-2.28,19.42-19.87,33.32-39.29,31.04
		c-19.42-2.28-33.32-19.87-31.04-39.29c2.28-19.42,19.87-33.32,39.29-31.04C127.74,87.07,141.64,104.66,139.36,124.08"/>
</g>
</svg>

                        </a>
                        </div>
                        <div class="menu-container" style="display: none;">
                            <a selected><b>Home</b></a>
                            <a href="/progetti">Progetti</a>
                            <!-- <a href="mailto:info@iotinga.it" special>Lavora Con Noi</a> -->
                            <a href="mailto:info@iotinga.it" special>Lavora Con Noi</a>
                            <a href="/contatti">Contatti</a>
                        </div>
                        <div class="mobile-menu" onclick="mobileMenuClick(this)" style="display: none;">
                            <div class="bar1"></div>
                            <div class="bar2"></div>
                            <div class="bar3"></div>
                        </div>
                    </div>
                    <div class="space-header-content">
                        <div id="iotinga-center-logo" class="iotinga-center-logo" style="position: relative">
                            <div style="position: absolute; width: 100%; height: 80vh;">
                                <?xml version="1.0" encoding="utf-8"?>
                                <!-- Generator: Adobe Illustrator 26.0.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
                                <svg version="1.1" id="Livello_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                    viewBox="0 0 227.94 84.94" style="enable-background:new 0 0 227.94 84.94;" xml:space="preserve">
                                <style type="text/css">
                                    .st0{display:none;}
                                    .st1{display:inline;}
                                </style>
                                <g>
                                    <g>
                                        <path d="M26.81,33.43v18.08h4.97v5.34H15.14v-5.34h5.01V33.43h-5.01v-5.34h16.64v5.34H26.81z"/>
                                    </g>
                                    <g>
                                        <path d="M34.99,42.47c0-8.55,6.66-14.88,15.74-14.88c9.04,0,15.74,6.29,15.74,14.88c0,8.59-6.7,14.88-15.74,14.88
                                            C41.65,57.34,34.99,51.02,34.99,42.47z M59.73,42.47c0-5.47-3.86-9.21-9-9.21c-5.14,0-9,3.74-9,9.21c0,5.46,3.86,9.2,9,9.2
                                            C55.87,51.67,59.73,47.93,59.73,42.47z"/>
                                    </g>
                                    <g>
                                        <path d="M91.54,36.14c-2.47-1.44-5.05-2.34-7.93-2.75v23.46h-6.66V33.39c-2.83,0.41-5.46,1.32-7.97,2.75l-2.26-4.97
                                            c3.99-2.38,8.71-3.58,13.52-3.58c4.85,0,9.62,1.19,13.56,3.58L91.54,36.14z"/>
                                        <path d="M106.67,33.43v18.08h4.97v5.34H95v-5.34h5.01V33.43H95v-5.34h16.64v5.34H106.67z"/>
                                        <path d="M142.79,40v16.85h-6.66V40.21c0-4.73-2.38-6.94-6.12-6.94c-3.86,0-6.7,2.34-6.7,7.4v16.19h-6.66V28.09h6.45v3.49
                                            c1.97-2.67,5.01-3.99,8.79-3.99C138.72,27.59,142.79,31.99,142.79,40z"/>
                                        <path d="M168.8,42.02h6.08v14.83h-5.01v-1.73c-2.05,1.52-4.68,2.22-7.72,2.22c-7.85,0-14.59-5.18-14.59-14.63
                                            c0-8.92,6.66-15.12,15.82-15.12c5.05,0,9.25,1.73,12.04,4.97l-4.27,3.94c-2.1-2.22-4.52-3.25-7.44-3.25
                                            c-5.59,0-9.41,3.74-9.41,9.41c0,6.08,4.07,9.12,8.63,9.12c2.18,0,4.23-0.62,5.88-1.97V42.02z"/>
                                        <path d="M207.19,41.11v15.74h-6.66v-6.9h-13.15v6.9h-6.58V41.11c0-8.75,5.3-13.52,13.19-13.52S207.19,32.36,207.19,41.11z
                                            M200.53,44.61V40.5c0-4.89-2.63-7.23-6.58-7.23c-3.99,0-6.57,2.34-6.57,7.23v4.11H200.53z"/>
                                    </g>
                                </g>
                                <g class="st0">
                                    <path class="st1" d="M148.15-10.8c2.46,7.48-1.62,15.53-9.1,17.99c-7.48,2.46-15.53-1.62-17.99-9.1
                                        c-2.46-7.48,1.62-15.53,9.09-17.99C137.64-22.35,145.69-18.28,148.15-10.8"/>
                                    <path class="st1" d="M155.84,21.48c-1.68-5.1-3.91-9.87-6.6-14.25c-2.22,2.4-5.07,4.29-8.4,5.38
                                        c-10.47,3.44-21.75-2.26-25.19-12.74c-2.21-6.73-0.64-13.8,3.54-18.9c-14.69-6.52-31.76-7.82-48.23-2.41
                                        c-35.29,11.59-54.5,49.6-42.91,84.89c11.59,35.29,49.6,54.5,84.89,42.91C148.21,94.78,167.43,56.77,155.84,21.48 M139.36,68.22
                                        c-2.28,19.42-19.87,33.32-39.29,31.04c-19.42-2.28-33.32-19.87-31.04-39.29c2.28-19.42,19.87-33.32,39.29-31.04
                                        C127.74,31.2,141.64,48.79,139.36,68.22"/>
                                </g>
                                </svg>

                            </div>
                        </div>
                        <img id="satellite" class="satellite-img" src="assets/img/head/sat.png" disable768>
                        <img class="head-cloud-img" src="assets/img/head/cloud.png" disable768>
                        <img id="commodore" class="commodore" src="assets/img/head/commodore.png" disable768>
                        <img id="starman" class="starman" src="assets/img/head/starman.png" disable768>
                        <img class="hand" src="assets/img/head/hand.png" disable768>
                        <img id="rocket" class="rocket" src="assets/img/head/rocket.png" disable768>
                        <img id="satellite-responsive" class="satellite-responsive" src="assets/img/head/sat.png" enable768>
                    </div>
                </div>
                <div class="main-description">
                    <img id="pc" class="pc" src="assets/img/head/pc.png">
                    <img id="cloud-2" class="cloud-2" src="assets/img/head/cloud-2.png">
                    <img id="cloud-3" class="cloud-3" src="assets/img/head/cloud-3.png">
                    <div class="text-elements">
                        <p>Il pluri premiato team di esperti<br>che aiuta le aziende a progettare, sviluppare e produrre<br>prodotti innovativi connessi ad Internet</p>
                        <p>
                          <br><br><br>
                          <b>Iotinga è la Soluzione che stavi cercando</b>
                          <br><br><br>
                        </p>
                        <p>
                          <img class="prize" src="assets/img/head/H2020-Seal-of-Excellence.png">
                          <img class="prize" src="assets/img/head/CES2019-Innovation-awards_Honoree.png">
                          <img class="prize" src="assets/img/head/CES2022-Best-of-Innovation.png">
                          <img class="prize" src="assets/img/head/il-tuo-progetto-qui.png">
                        </p>
                    </div>
                    <div class="head-divider">
                        <img id="pointer" class="pointer" src="assets/img/head/pointer.png">
                        <img id="stamp" class="stamp" src="assets/img/head/stamp.png">
                        <img id="cloud-4" class="cloud-4" src="assets/img/head/cloud.png">
                    </div>

                </div>
            </section>
            <div class="blue-section">
                <div class="section-content">
                    <div class="blue-section-header">
                        <h1>CHI SIAMO</h1>
                        <hr>
                        <p>Iotinga nasce dall’esperienza unica dei propri collaboratori, maturata in svariati settori dell’industria: trasporti, telecomunicazioni, HVAC ed elettronica di consumo</p>
                    </div>
                    <div class="blue-section-row" first>
                        <div class="img-column mac">
                            <img src="assets/img/who/mac.png">
                        </div>
                        <div class="text-column">
                            <p>Offriamo un servizio unico in Italia per completezza e professionalità. Gestiamo per te l’intero processo, adattandoci alle tue esigenze</p>
                        </div>
                    </div>
                    <div class="blue-section-row" second>
                        <div class="img-column vhs" mobile-enable>
                            <img src="assets/img/who/vhs.png">
                        </div>
                        <div class="text-column">
                            <p>Il nostro mantra è <b>DO IT BETTER</b>, ed il nostro metodo lo dimostra: affrontiamo le sfide con un approccio integrato, volto al miglioramento continuo. Facciamo tesoro dei tuoi feedback ed investiamo costantemente nello sviluppo di solide competenze settoriali</p>
                        </div>
                        <div class="img-column vhs" mobile-disable>
                            <img src="assets/img/who/vhs.png">
                        </div>
                    </div>
                </div>
                <div class="blue-section-footer">
                        <img id="laptop" class="laptop" src="assets/img/who/laptop.png">
                        <img id="cloud-blue" class="cloud-blue" src="assets/img/head/cloud.png">
                        <img id="cabinato" class="cabinato" src="assets/img/who/cabinato.png">
                </div>

            </div>
            <div class="magenta-section">
                <div class="section-content">
                    <div class="magenta-section-header">
                        <h1>COSA FACCIAMO</h1>
                        <p class="spacer">Aggiungiamo valore e vantaggio competitivo alla tua azienda.<br><br>E lo facciamo
                            meglio e in meno tempo degli altri</p>
                        <p class="smaller">Affianchiamo la tua organizzazione per facilitare<br>l'avvio e l’integrazione del progetto
                                secondo le necessità<br>ed i ritmi del tuo mercato</p>
                    </div>
                    <div class="magenta-section-row">
                        <div class="img-column olivetti" mobile-enable>
                            <img src="assets/img/how/olivetti.png">
                        </div>
                        <div class="text-column">
                            <p>Raccogliamo continuamente feedback e ti aiutiamo a scoprire come la tecnologia può aiutarti a catturare l’interesse dei tuoi clienti, oppure a innovare i tuoi processi aziendali.<br>Per noi innovare significa semplificare</p>
                        </div>
                        <div class="img-column olivetti" mobile-disable>
                            <img src="assets/img/how/olivetti.png">
                        </div>
                    </div>
                    <div class="magenta-section-row" >
                        <div class="img-column napoleon">
                            <img src="assets/img/how/napoleone.png">
                        </div>
                        <div class="text-column">
                            <p>“Prendi tempo per riflettere, ma quanto è giunta l’ora di agire smetti di pensare e scendi in campo” - Analizziamo il contesto e definiamo insieme una strategia che ci permetta di aggredire i problemi, portando l’innovazione sul mercato in 6 mesi</p>
                        </div>
                    </div>
                </div>
                <div class="magenta-section-footer">
                    <p>Iotinga è una azienda innovativa, può seguire progetti di Ricerca e Sviluppo e consentirti di accedere a benefit ed agevolazioni specifiche, in base alla natura della tua azienda e del tuo progetto, per un ritorno dell’investimento sicuro ed immediato.</p>
                </div>
            </div>
            <div class="splitted-section" desktop>
                <div class="buisness-card">
                    <div>
                        <svg version="1.1" id="Livello_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                viewBox="0 0 227.94 309.74" style="enable-background:new 0 0 227.94 309.74;" xml:space="preserve">
                            <g>
                                <g>
                                    <path d="M29.62,258.23v18.08h4.97v5.34H17.95v-5.34h5.01v-18.08h-5.01v-5.34h16.64v5.34H29.62z"/>
                                </g>
                                <g>
                                    <path d="M37.8,267.27c0-8.55,6.66-14.88,15.74-14.88c9.04,0,15.74,6.29,15.74,14.88c0,8.59-6.7,14.88-15.74,14.88
                                        C44.45,282.14,37.8,275.81,37.8,267.27z M62.53,267.27c0-5.47-3.86-9.21-9-9.21c-5.14,0-9,3.74-9,9.21c0,5.46,3.86,9.2,9,9.2
                                        C58.67,276.47,62.53,272.73,62.53,267.27z"/>
                                </g>
                                <g>
                                    <path d="M94.35,260.94c-2.47-1.44-5.05-2.34-7.93-2.75v23.46h-6.66v-23.46c-2.83,0.41-5.46,1.32-7.97,2.75l-2.26-4.97
                                        c3.99-2.38,8.71-3.58,13.52-3.58c4.85,0,9.62,1.19,13.56,3.58L94.35,260.94z"/>
                                    <path d="M109.47,258.23v18.08h4.97v5.34H97.8v-5.34h5.01v-18.08H97.8v-5.34h16.64v5.34H109.47z"/>
                                    <path d="M145.59,264.8v16.85h-6.66v-16.64c0-4.73-2.38-6.94-6.12-6.94c-3.86,0-6.7,2.34-6.7,7.4v16.19h-6.66v-28.76h6.45v3.49
                                        c1.97-2.67,5.01-3.99,8.79-3.99C141.52,252.39,145.59,256.79,145.59,264.8z"/>
                                    <path d="M171.61,266.82h6.08v14.83h-5.01v-1.73c-2.05,1.52-4.68,2.22-7.72,2.22c-7.85,0-14.59-5.18-14.59-14.63
                                        c0-8.92,6.66-15.12,15.82-15.12c5.05,0,9.25,1.73,12.04,4.97l-4.27,3.94c-2.1-2.22-4.52-3.25-7.44-3.25
                                        c-5.59,0-9.41,3.74-9.41,9.41c0,6.08,4.07,9.12,8.63,9.12c2.18,0,4.23-0.62,5.88-1.97V266.82z"/>
                                    <path d="M210,265.91v15.74h-6.66v-6.9h-13.15v6.9h-6.58v-15.74c0-8.75,5.3-13.52,13.19-13.52S210,257.16,210,265.91z
                                        M203.34,269.4v-4.11c0-4.89-2.63-7.23-6.58-7.23c-3.99,0-6.57,2.34-6.57,7.23v4.11H203.34z"/>
                                </g>
                            </g>
                            <g>
                                <path d="M198.56,37.04c3.7,11.26-2.43,23.38-13.69,27.07c-11.26,3.7-23.38-2.43-27.07-13.69c-3.7-11.26,2.43-23.38,13.69-27.07
                                    C182.75,19.66,194.87,25.79,198.56,37.04"/>
                                <path d="M210.13,85.62c-2.52-7.68-5.88-14.85-9.93-21.45c-3.35,3.61-7.63,6.45-12.65,8.1c-15.76,5.18-32.74-3.4-37.91-19.17
                                    c-3.33-10.13-0.97-20.76,5.32-28.44c-22.11-9.81-47.79-11.77-72.58-3.63C29.28,38.48,0.37,95.68,17.81,148.79
                                    c17.44,53.11,74.64,82.02,127.75,64.58C198.66,195.92,227.58,138.73,210.13,85.62 M185.33,155.95
                                    c-3.43,29.23-29.9,50.14-59.13,46.72c-29.23-3.43-50.14-29.9-46.72-59.13c3.43-29.23,29.9-50.14,59.13-46.72
                                    C167.85,100.25,188.76,126.72,185.33,155.95"/>
                            </g>
                        </svg>
                        <p>Viale Del Lavoro, 33 37036<br>San Martino Buon Albergo, Verona - Italy<br><br>info@iotinga.it - iotinga@pec.it<br><br><a href="/assets/privacy-policy-80030478.pdf" style="color:#ffffff">Privacy Policy</a></p>
                    </div>
                </div>
                <div class="nokia-container"><img src="assets/img/foot/nokia.png"></div>
                <div class="work-with-us"><div><p>Vuoi lavorare con noi?</p><a href="mailto:info@iotinga.it">Contattaci</a></div></div>
            </div>
            <div class="splitted-section" mobile>
                <div class="work-with-us"><div><p>Vuoi lavorare con noi?</p><a href="mailto:info@iotinga.it">Contattaci</a></div></div>
                <div class="nokia-container"><img src="assets/img/foot/nokia.png"></div>
                <div class="buisness-card">
                    <div>
                        <svg version="1.1" id="Livello_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                viewBox="0 0 227.94 309.74" style="enable-background:new 0 0 227.94 309.74;" xml:space="preserve">
                            <g>
                                <g>
                                    <path d="M29.62,258.23v18.08h4.97v5.34H17.95v-5.34h5.01v-18.08h-5.01v-5.34h16.64v5.34H29.62z"/>
                                </g>
                                <g>
                                    <path d="M37.8,267.27c0-8.55,6.66-14.88,15.74-14.88c9.04,0,15.74,6.29,15.74,14.88c0,8.59-6.7,14.88-15.74,14.88
                                        C44.45,282.14,37.8,275.81,37.8,267.27z M62.53,267.27c0-5.47-3.86-9.21-9-9.21c-5.14,0-9,3.74-9,9.21c0,5.46,3.86,9.2,9,9.2
                                        C58.67,276.47,62.53,272.73,62.53,267.27z"/>
                                </g>
                                <g>
                                    <path d="M94.35,260.94c-2.47-1.44-5.05-2.34-7.93-2.75v23.46h-6.66v-23.46c-2.83,0.41-5.46,1.32-7.97,2.75l-2.26-4.97
                                        c3.99-2.38,8.71-3.58,13.52-3.58c4.85,0,9.62,1.19,13.56,3.58L94.35,260.94z"/>
                                    <path d="M109.47,258.23v18.08h4.97v5.34H97.8v-5.34h5.01v-18.08H97.8v-5.34h16.64v5.34H109.47z"/>
                                    <path d="M145.59,264.8v16.85h-6.66v-16.64c0-4.73-2.38-6.94-6.12-6.94c-3.86,0-6.7,2.34-6.7,7.4v16.19h-6.66v-28.76h6.45v3.49
                                        c1.97-2.67,5.01-3.99,8.79-3.99C141.52,252.39,145.59,256.79,145.59,264.8z"/>
                                    <path d="M171.61,266.82h6.08v14.83h-5.01v-1.73c-2.05,1.52-4.68,2.22-7.72,2.22c-7.85,0-14.59-5.18-14.59-14.63
                                        c0-8.92,6.66-15.12,15.82-15.12c5.05,0,9.25,1.73,12.04,4.97l-4.27,3.94c-2.1-2.22-4.52-3.25-7.44-3.25
                                        c-5.59,0-9.41,3.74-9.41,9.41c0,6.08,4.07,9.12,8.63,9.12c2.18,0,4.23-0.62,5.88-1.97V266.82z"/>
                                    <path d="M210,265.91v15.74h-6.66v-6.9h-13.15v6.9h-6.58v-15.74c0-8.75,5.3-13.52,13.19-13.52S210,257.16,210,265.91z
                                        M203.34,269.4v-4.11c0-4.89-2.63-7.23-6.58-7.23c-3.99,0-6.57,2.34-6.57,7.23v4.11H203.34z"/>
                                </g>
                            </g>
                            <g>
                                <path d="M198.56,37.04c3.7,11.26-2.43,23.38-13.69,27.07c-11.26,3.7-23.38-2.43-27.07-13.69c-3.7-11.26,2.43-23.38,13.69-27.07
                                    C182.75,19.66,194.87,25.79,198.56,37.04"/>
                                <path d="M210.13,85.62c-2.52-7.68-5.88-14.85-9.93-21.45c-3.35,3.61-7.63,6.45-12.65,8.1c-15.76,5.18-32.74-3.4-37.91-19.17
                                    c-3.33-10.13-0.97-20.76,5.32-28.44c-22.11-9.81-47.79-11.77-72.58-3.63C29.28,38.48,0.37,95.68,17.81,148.79
                                    c17.44,53.11,74.64,82.02,127.75,64.58C198.66,195.92,227.58,138.73,210.13,85.62 M185.33,155.95
                                    c-3.43,29.23-29.9,50.14-59.13,46.72c-29.23-3.43-50.14-29.9-46.72-59.13c3.43-29.23,29.9-50.14,59.13-46.72
                                    C167.85,100.25,188.76,126.72,185.33,155.95"/>
                            </g>
                        </svg>
                        <p>Viale Del Lavoro, 33 37036<br>San Martino Buon Albergo, Verona - Italy<br><br>info@iotinga.it - iotinga@pec.it<br><br><a href="/assets/privacy-policy-80030478.pdf" style="color:#ffffff">Privacy Policy</a></p>
                    </div>
                </div>

            </div>
            <div class="footer">
                <p>CF e P.IVA IT04656900232 - CAP. SOCIALE 13.555,56 &euro; i.v. - REA: VR438472</p>
		<p>SEDE LEGALE: Via Vittorio Veneto, 18/A 37053 Cerea, Verona - Italy</p>
            </div>
        </div>
    </body>
</html>

"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract text content
text_content = soup.get_text(separator='\n', strip=True)

# Print the text content
print(text_content)
