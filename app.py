from flask import Flask,render_template,url_for,request,abort,send_file
from flask_material import Material
from urllib.parse import urlparse
from googlesearch import search
# EDA PKg
import pandas as pd 
import numpy as np 
import urllib.request
from bs4 import BeautifulSoup
import plotly
import json
import plotly.graph_objs as go
from flask import Flask, session
import warnings
import quandl


app = Flask(__name__)
Material(app)
app.secret_key = "jarvis"  
@app.route('/')
def index():
	#df3=pd.read_csv(r"data\DataUCMC\UpcomingBordMeetings.csv")
	return render_template("index.html")

	
@app.route('/download1')
def download_file1():
	myCompany = session.get('myCompany')
	path1 = "data/DataMC/dividends/DIV-MC-"+myCompany+".csv"
	return send_file(path1, as_attachment=True)
@app.route('/download2')	
def download_file2():
	myCompany = session.get('myCompany')
	path2 = "data/DataBS/dividends/DIV-BS-"+myCompany+".csv"
	return send_file(path2, as_attachment=True)


@app.route('/download3')	
def download_file3():
	myCompany = session.get('myCompany')
	path3 = "data/DataMC/rights/RIGHTS-MC-"+myCompany+".csv"
	return send_file(path3, as_attachment=True)
@app.route('/download4')	
def download_file4():
	myCompany = session.get('myCompany')
	path4 = "data/DataBS/rights/RIGHTS-BS-"+myCompany+".csv"
	return send_file(path4, as_attachment=True)


@app.route('/download5')	
def download_file5():
	myCompany = session.get('myCompany')
	path5 = "data/DataMC/splits/SPLITS-MC-"+myCompany+".csv"
	return send_file(path5, as_attachment=True)
@app.route('/download6')	
def download_file6():
	myCompany = session.get('myCompany')
	path6 = "data/DataBS/splits/SPLITS-BS-"+myCompany+".csv"
	return send_file(path6, as_attachment=True)	


@app.route('/download7')	
def download_file7():
	myCompany = session.get('myCompany')
	path7 = "data/DataMC/bonus/BONUS-MC-"+myCompany+".csv"
	return send_file(path7, as_attachment=True)
@app.route('/download8')	
def download_file8():
	myCompany = session.get('myCompany')
	path8 = "data/DataBS/bonus/BONUS-BS-"+myCompany+".csv"
	return send_file(path8, as_attachment=True)	


@app.route('/download9')	
def download_file9():
	myCompany = session.get('myCompany')
	path9 = "data/DataMC/boardmeetings/BOARDMEETINGS-MC-"+myCompany+".csv"
	return send_file(path9, as_attachment=True)
@app.route('/download10')	
def download_file10():
	myCompany = session.get('myCompany')
	path10 = "data/DataBS/boardmeetings/BOARDMEETINGS-BS-"+myCompany+".csv"
	return send_file(path10, as_attachment=True)	


@app.route('/download11')	
def download_file11():
	myCompany = session.get('myCompany')
	path11 = "data/DataMC/aeb/AEB-MC-"+myCompany+".csv"
	return send_file(path11, as_attachment=True)
@app.route('/download12')	
def download_file12():
	myCompany = session.get('myCompany')
	path12 = "data/DataBS/aeb/AEB-BS-"+myCompany+".csv"
	return send_file(path12, as_attachment=True)		




@app.route('/corporate')
def corporate():
	return render_template("analyze.html")
@app.route('/stockanalysis')
def stockanalysis():
	if 'myCompany' in session:
		myCompany=session['myCompany']
		StockMarketCode=''
		QuandlDict={
			"Aarti Drugs Ltd.":"AARTIDRUGS",
			"Aarti Industries Ltd.":"AARTIIND",
			"Aarvee Denims & Exports Ltd":"AARVEEDEN",
			"Aavas Financiers Ltd":"AAVAS",
			"Aban Offshore Ltd.":"ABAN",
			"ABB India Ltd":"ABB",
			"Abbott India Ltd.":"ABBOTINDIA",
			"Aditya Birla Capital Ltd.":"ABCAPITAL",
			"Aditya Birla ChemicalsLtd":"ABCIL",
			"Aditya Birla Fashion & Retail Ltd.":"ABFRL",
			"ABG Shipyard Ltd.":"ABGSHIP",
			"Abhishek Corporation Ltd":"ABHISHEK",
			"Aditya Birla Nuvo Ltd.":"ABIRLANUVO",
			"ABM International Ltd.":"ABMINTLTD",
			"Aditya Birla Sun Life AMC Ltd.":"ABSLBANETF",
			"ACC Ltd":"ACC",
			"Accelya Solutions India Ltd.":"ACCELYA",
			"Action Construction Equipment Ltd.":"ACE",
			"Acropetal Technologies Ltd":"ACROPETAL",
			"Adani Enterprises Ltd":"ADANIENT",
			"Adani Gas Ltd":"ADANIGAS",
			"Adani Green Energy Ltd.":"ADANIGREEN",
			"Adani Ports & Special Economic Zone Ltd":"ADANIPORTS",
			"Adani Power Limited":"ADANIPOWER",
			"Adani Transmission Ltd":"ADANITRANS",
			"ADF Foods Ltd.":"ADFFOODS",
			"Adhunik Metaliks Ltd.":"ADHUNIK",
			"Adhunik Industries Ltd.":"ADHUNIKIND",
			"Ador Welding Ltd.":"ADORWELD",
			"Adroit Infotech Ltd.":"ADROITINFO",
			"Allied Digital Services Ltd.":"ADSL",
			"Advani Hotels & ResortsLtd.":"ADVANIHOTR",
			"Advanta Ltd.":"ADVANTA",
			"Advanced Enzyme Technologies Ltd":"ADVENZYMES",
			"Aegis Logistics Ltd.":"AEGISCHEM",
			"AffleLtd.":"AFFLE",
			"Inspirisys Solution Ltd.":"AFL",
			"Aftek Ltd":"AFTEK",
			"Agarwal Industrial Corporation Ltd":"AGARIND",
			"AGC Networks Ltd.":"AGCNET",
			"Artemis Global Life Science Ltd.":"AGLSL",
			"Agri-TechLtd.":"AGRITECH",
			"Agro Dutch Industries Ltd.":"AGRODUTCH",
			"Agro Phos India Ltd.":"AGROPHOS",
			"Asian HotelsLtd":"AHLEAST",
			"Ahluwalia ContractsLtd.":"AHLUCONT",
			"AIA Engineering Ltd.":"AIAENG",
			"AI Champdany Industries Ltd.":"AICHAMP",
			"Ashapura Intimates Fashion Ltd":"AIFL",
			"Monnet Ispat & Energy Ltd.":"AIONJSW",
			"Airan Ltd":"AIRAN",
			"Ajanta Pharma Ltd.":"AJANTPHARM",
			"Ajmera Realty & Infra India Ltd":"AJMERA",
			"Akash Infra-Projects Ltd":"AKASH",
			"AksharChemLtd.":"AKSHARCHEM",
			"Aksh Optifibre Ltd.":"AKSHOPTFBR",
			"Akzo Nobel India Ltd.":"AKZOINDIA",
			"Alankit Ltd.":"ALANKIT",
			"Albert David Ltd.":"ALBERTDAVD",
			"Allahabad Bank":"ALBK",
			"Alchemist Ltd.":"ALCHEM",
			"Alembic Ltd.":"ALEMBICLTD",
			"Alfa LavalLtd.":"ALFALAVAL",
			"Alicon Castalloy Ltd":"ALICON",
			"Alkali Metals Ltd":"ALKALI",
			"Alkem Laboratories Limited":"ALKEM",
			"Alkyl Amines Chemicals Ltd.":"ALKYLAMINE",
			"Allcargo Logistics Ltd":"ALLCARGO",
			"Allsec Technologies Ltd.":"ALLSEC",
			"Almondz Global Securities Ltd":"ALMONDZ",
			"Alok Industries Ltd.":"ALOKINDS",
			"Alpa Laboratories Ltd.":"ALPA",
			"AlphageoLtd.":"ALPHAGEO",
			"Alpine Housing Development Corporation Ltd.":"ALPINEHOU",
			"Alps Industries Ltd.":"ALPSINDUS",
			"Amar Remedies Ltd.":"AMAR",
			"Amara Raja Batteries Ltd.":"AMARAJABAT",
			"Amarjothi Spinning Mills Ltd.":"AMARJOTHI",
			"Amber Enterprises India Ltd.":"AMBER",
			"Ambica Agarbathies Aroma & Industries Ltd":"AMBICAAGAR",
			"Ambika Cotton Mills Ltd.":"AMBIKCO",
			"Ambuja Cements Ltd":"AMBUJACEM",
			"AMD Industries Ltd.":"AMDIND",
			"AMJ Land Holdings Ltd.":"AMJLAND",
			"AML Steel Ltd.":"AMLSTEEL",
			"Amrutanjan Health Care Ltd":"AMRUTANJAN",
			"Amtek Auto Ltd.":"AMTEKAUTO",
			"Advance Metering Technology Ltd":"AMTL",
			"Anant Raj Ltd.":"ANANTRAJ",
			"Andhra Bank":"ANDHRABANK",
			"Andhra Cements Ltd.":"ANDHRACEMT",
			"Andhra Paper Ltd.":"ANDHRAPAP",
			"Andhra Sugars Ltd.":"ANDHRSUGAR",
			"ANG Industries Ltd":"ANGIND",
			"Anik Industries Ltd.":"ANIKINDS",
			"Ankit Metal & Power Ltd.":"ANKITMETAL",
			"Ankur Drugs & Pharma Ltd.":"ANKURDRUGS",
			"Ansal Properties & Infrastructure Ltd.":"ANSALAPI",
			"Ansal Housing Ltd.":"ANSALHSG",
			"Antarctica Ltd.":"ANTGRAPHIC",
			"Anup Engineering Ltd.":"ANUP",
			"Apar Industries Ltd.":"APARINDS",
			"Anjani Portland Cement Ltd.":"APCL",
			"Apcotex Industries Ltd":"APCOTEXIND",
			"Apex Frozen Foods Ltd.":"APEX",
			"Aplab Ltd.":"APLAB",
			"APL Apollo Tubes Ltd.":"APLAPOLLO",
			"Alembic Pharmaceuticals Ltd":"APLLTD",
			"Apollo Micro Systems Ltd.":"APOLLO",
			"Apollo Hospitals Enterprises Ltd.":"APOLLOHOSP",
			"Apollo Pipes Ltd.":"APOLLOPIPE",
			"Apollo Tyres Ltd.":"APOLLOTYRE",
			"Apollo Sindoori Hotels Ltd.":"APOLSINHOT",
			"Aptech Ltd.":"APTECHT",
			"Aqua Logistics Limited":"AQUA",
			"Archidply Industries Ltd":"ARCHIDPLY",
			"Archies Ltd.":"ARCHIES",
			"Arcotech Ltd.":"ARCOTECH",
			"Rajdarshan Industries Ltd.":"ARENTERP",
			"Aries Agro Ltd.":"ARIES",
			"Arihant Foundations & Housing Ltd.":"ARIHANT",
			"Arihant Superstructures Ltd":"ARIHANTSUP",
			"Arman Financial Services Ltd":"ARMANFIN",
			"Aro Granite Industries Ltd.":"AROGRANITE",
			"Arrow Greentech Ltd.":"ARROWGREEN",
			"Arrow Textile Ltd":"ARROWTEX",
			"Arshiya Ltd":"ARSHIYA",
			"ARSS Infrastructure Projects Ltd.":"ARSSINFRA",
			"Artemis Medicare Services Ltd.":"ARTEMISMED",
			"Arvind Ltd.":"ARVIND",
			"Arvind Fashions Ltd.":"ARVINDFASN",
			"Arvind Remedies Ltd.":"ARVINDREM",
			"Arvind SmartSpaces Ltd.":"ARVSMART",
			"Asahi India Glass Ltd.":"ASAHIINDIA",
			"Asahi Songwon Colors Ltd.":"ASAHISONG",
			"Automotive Stampings & Assemblies Ltd.":"ASAL",
			"Associated Alcohols & Breweries Ltd.":"ASALCBR",
			"Ashapura Minechem Ltd.":"ASHAPURMIN",
			"Ashco Niulab Industries Ltd":"ASHCONIUL",
			"Ashiana Housing Ltd.":"ASHIANA",
			"Ashima Ltd.":"ASHIMASYN",
			"Ashoka Buildcon Ltd":"ASHOKA",
			"Ashok Leyland Ltd.":"ASHOKLEY",
			"Asian Electronics Ltd.":"ASIANELEC",
			"Asian HotelsLtd.":"ASIANHOTNR",
			"Asian Paints Ltd.":"ASIANPAINT",
			"Asian Granito India Ltd.":"ASIANTILES",
			"Amit Spinning Industries Ltd.":"ASIL",
			"Aspinwall & Co. Ltd":"ASPINWALL",
			"Assam Co. India Ltd":"ASSAMCO",
			"Astec Lifesciences Limited":"ASTEC",
			"Aster DM Healthcare Ltd":"ASTERDM",
			"AstraZeneca Pharma India Ltd.":"ASTRAIDL",
			"Astral Poly Technik Ltd.":"ASTRAL",
			"Astra Microwave Products Ltd.":"ASTRAMICRO",
			"Astron Paper & Board Mill Ltd.":"ASTRON",
			"Agro Tech Foods Ltd.":"ATFL",
			"Atlanta Ltd.":"ATLANTA",
			"Atlas Cycles Ltd.":"ATLASCYCLE",
			"ATN International Ltd.":"ATNINTER",
			"Atul Ltd.":"ATUL",
			"Atul Auto Ltd.":"ATULAUTO",
			"AU Small Finance Bank Limited":"AUBANK",
			"Aurionpro Solutions Ltd.":"AURIONPRO",
			"Aurobindo Pharma Ltd.":"AUROPHARMA",
			"Ausom Enterprise Ltd":"AUSOMENT",
			"Greenearth Resources & Projects Ltd.":"AUSTRAL",
			"Automotive Axles Ltd.":"AUTOAXLES",
			"Autoline Industries Ltd.":"AUTOIND",
			"AutoliteLtd.":"AUTOLITIND",
			"Avadh Sugar & Energy Ltd.":"AVADHSUGAR",
			"Avanti Feeds Ltd.":"AVANTIFEED",
			"AVT Natural Products Ltd.":"AVTNPL",
			"Axis Bank Ltd":"AXISBANK",
			"AXISCADES Engineering Technologies Ltd":"AXISCADES",
			"Axis Asset Management Company Limited":"AXISGOLD",
			"AYM Syntex Ltd.":"AYMSYNTEX",
			"Aztecsoft Ltd":"AZTECSOFT",
			"Bafna Pharmaceuticals Ltd":"BAFNAPH",
			"B.A.G. Films & Media Ltd.":"BAGFILMS",
			"Bajaj Auto Ltd":"BAJAJ_AUTO",
			"Bajaj Consumer Care Ltd.":"BAJAJCON",
			"Bajaj Electricals Ltd.":"BAJAJELEC",
			"Bajaj Finserv Ltd":"BAJAJFINSV",
			"Bajaj Hindusthan Sugar Ltd.":"BAJAJHIND",
			"Bajaj Holdings & Investment Ltd":"BAJAJHLDNG",
			"Bajaj Finance Ltd":"BAJFINANCE",
			"Balaji Telefilms Ltd.":"BALAJITELE",
			"Balaji Amines Ltd.":"BALAMINES",
			"Shri Ramrupai Balaji Steels Ltd.":"BALASTEELS",
			"Balaxi Ventures Ltd.":"BALAXI",
			"Balkrishna Paper Mills Ltd.":"BALKRISHNA",
			"Balkrishna Industries Ltd.":"BALKRISIND",
			"Ballarpur Industries Ltd.":"BALLARPUR",
			"Balmer Lawrie & Co. Ltd.":"BALMLAWRIE",
			"Bal Pharma Ltd.":"BALPHARMA",
			"Balrampur Chini Mills Ltd.":"BALRAMCHIN",
			"Banaras Beads Ltd.":"BANARBEADS",
			"Bannari Amman Sugars Ltd.":"BANARISUG",
			"Banco ProductsLtd.":"BANCOINDIA",
			"Bandhan Bank Ltd":"BANDHANBNK",
			"Bang Overseas Ltd":"BANG",
			"Bank of Baroda":"BANKBARODA",
			"Nippon Life India Asset Management Ltd.":"BANKBEES",
			"Bank of India":"BANKINDIA",
			"Bank of Rajasthan Ltd.":"BANKRAJAS",
			"Banswara Syntex Ltd.":"BANSWRAS",
			"Bartronics India Ltd.":"BARTRONICS",
			"BASF India Ltd.":"BASF",
			"Bannari Amman Spinning Mills Ltd.":"BASML",
			"Bata India Ltd.":"BATAINDIA",
			"Batliboi Ltd.":"BATLIBOI",
			"Bayer CropScience Ltd.":"BAYERCROP",
			"Bharat Bijlee Ltd.":"BBL",
			"Bombay Burmah Trading Corporation Ltd.":"BBTC",
			"Brightcom Group Ltd.":"BCG",
			"B.C. Power Controls Ltd":"BCP",
			"Bharat Dynamics Ltd.":"BDL",
			"Beardsell Ltd.":"BEARDSELL",
			"Best & Crompton Engg. Ltd.":"BECREL",
			"Bedmutha Industries Ltd":"BEDMUTHA",
			"Bharat Electronics Ltd.":"BEL",
			"Bell Ceramics Ltd.":"BELLCERATL",
			"BEML Ltd.":"BEML",
			"Bhansali Engineering Polymers Ltd.":"BEPL",
			"Berger Paints India Ltd.":"BERGEPAINT",
			"BF Investment Ltd":"BFINVEST",
			"BF Utilities Ltd.":"BFUTILITIE",
			"Bharatiya Global Infomedia Ltd":"BGLOBAL",
			"BGR Energy Systems Ltd":"BGRENERGY",
			"Bhageria Industries Ltd.":"BHAGERIA",
			"Bhagyanagar India Ltd.":"BHAGYANGR",
			"Bhagyanagar Properties Ltd.":"BHAGYAPROP",
			"Bhandari Hosiery Exports Ltd.":"BHANDARI",
			"Bharat Financial Inclusion Ltd":"BHARATFIN",
			"Bharat Forge Ltd.":"BHARATFORG",
			"Bharat Gears Ltd.":"BHARATGEAR",
			"Bharati Defence & Infrastructure Ltd":"BHARATIDIL",
			"Bharat Rasayan Ltd.":"BHARATRAS",
			"Bharat Wire Ropes Ltd.":"BHARATWIRE",
			"Bharti Airtel Ltd.":"BHARTIARTL",
			"Bharat Heavy Electricals Ltd.":"BHEL",
			"Bigbloc Construction Ltd.":"BIGBLOC",
			"Bhartiya International Ltd.":"BIL",
			"Bil Energy Systems Ltd.":"BILENERGY",
			"Bilpower Ltd.":"BILPOWER",
			"Bimetal Bearings Ltd.":"BIMETAL",
			"Binani Cement Ltd.":"BINANICEM",
			"Binani Industries Ltd.":"BINANIIND",
			"Oswal Green Tech Ltd":"BINDALAGRO",
			"Biocon":"BIOCON",
			"Biofil Chemicals & Pharmaceuticals Ltd.":"BIOFILCHEM",
			"Birla Cable Ltd":"BIRLACABLE",
			"Birla Corporation Ltd.":"BIRLACORPN",
			"Birla CotsynLtd":"BIRLACOT",
			"Aditya Birla Money Ltd":"BIRLAMONEY",
			"Birla Power Solutions Ltd.":"BIRLAPOWER",
			"Birla Tyres Ltd.":"BIRLATYRE",
			"BKM Industries Ltd.":"BKMINDST",
			"BLB Ltd.":"BLBLIMITED",
			"Bliss GVS Pharma Ltd.":"BLISSGVS",
			"B.L. Kashyap & Sons Ltd.":"BLKASHYAP",
			"Blow Plast Ltd.":"BLOWPLAST",
			"BLS International Services Ltd":"BLS",
			"Blue BirdLtd.":"BLUEBIRD",
			"Blue BlendsLtd.":"BLUEBLENDS",
			"Blue Chip India Ltd.":"BLUECHIP",
			"Blue Coast Hotels Ltd":"BLUECOAST",
			"Blue Dart Express Ltd.":"BLUEDART",
			"Blue Star Ltd.":"BLUESTARCO",
			"Blue Star Infotech Ltd.":"BLUESTINFO",
			"Bodal Chemicals Ltd.":"BODALCHEM",
			"Bodhtree Consulting Ltd":"BODHTREE",
			"Bombay Dyeing & Manufacturing Co. Ltd.":"BOMDYEING",
			"Bongaigaon Refinery & Petrochemicals Ltd.":"BONGAIREFN",
			"Borosil Renewables Ltd.":"BORORENEW",
			"Bosch Chassis Systems India Ltd.":"BOSCHCHASY",
			"Bosch Ltd.":"BOSCHLTD",
			"Bharat Petroleum Corporation Ltd.":"BPCL",
			"BPL Ltd.":"BPL",
			"BPL Engineering Ltd.":"BPLENGG",
			"Brabourne Enterprises Ltd":"BRABOURNE",
			"Brandhouse Retails Ltd":"BRANDHOUSE",
			"Bombay Rayon Fashions Ltd.":"BRFL",
			"Brigade Enterprises Ltd.":"BRIGADE",
			"Britannia Industries Ltd.":"BRITANNIA",
			"Bharat Road Network Ltd.":"BRNL",
			"Broadcast Initiatives Ltd.":"BROADCAST",
			"Brooks Laboratories Ltd":"BROOKS",
			"BENCHMARK SPLIT CAPFUND-A":"BSCFAUG08A",
			"BENCHMARK SPLIT CAPFUND-B":"BSCFAUG08B",
			"BSE Ltd":"BSE",
			"BSEL Infrastructure Realty Ltd.":"BSELINFRA",
			"BSL Ltd.":"BSL",
			"Aditya Birla Sun Life AMC Ltd.":"BSLGOLDETF",
			"BS Ltd.":"BSLIMITED",
			"Aditya Birla Sun Life AMC Ltd.":"BSLNIFTY",
			"Birlasoft Ltd.":"BSOFT",
			"Burnpur Cement Ltd.":"BURNPUR",
			"Butterfly Gandhimathi Appliances Ltd":"BUTTERFLY",
			"Barak Valley Cements Ltd.":"BVCL",
			"Byke Hospitality Ltd":"BYKE",
			"Cadila Healthcare Ltd.":"CADILAHC",
			"Cairn India Ltd.":"CAIRN",
			"California Software Co. Ltd.":"CALSOFT",
			"Camlin Fine Sciences Ltd":"CAMLINFINE",
			"Canara Bank":"CANBK",
			"C & C Constructions Ltd.":"CANDC",
			"Can Fin Homes Ltd.":"CANFINHOME",
			"Cantabil Retail India Ltd":"CANTABIL",
			"Capacit`e Infraprojects Ltd.":"CAPACITE",
			"Capital First Ltd.":"CAPF",
			"Caplin Point Laboratories Ltd.":"CAPLIPOINT",
			"Capital Trust Ltd.":"CAPTRUST",
			"Carborundum Universal Ltd.":"CARBORUNIV",
			"Career Point Ltd":"CAREERP",
			"CARE Ratings Ltd.":"CARERATING",
			"Carol Info Services Ltd":"CAROLINFO",
			"Castex Technologies Ltd.":"CASTEXTECH",
			"CastrolLtd.":"CASTROLIND",
			"Consolidated Construction Consortium Ltd.":"CCCL",
			"Country Club Hospitality & Holidays Ltd.":"CCHHL",
			"CCL ProductsLtd.":"CCL",
			"Central Depository ServicesLtd.":"CDSL",
			"Ceat Ltd.":"CEATLTD",
			"Commercial Engineers & Body Builders Co Limited":"CEBBCO",
			"Celebrity Fashions Ltd.":"CELEBRITY",
			"Celestial Biolabs Ltd":"CELESTIAL",
			"Centurion Bank of Punjab Ltd.":"CENTBOP",
			"Century Enka Ltd.":"CENTENKA",
			"Century Extrusions Ltd.":"CENTEXT",
			"Central Bank of India":"CENTRALBK",
			"Centrum Capital Ltd.":"CENTRUM",
			"Centum Electronics Ltd.":"CENTUM",
			"Century PlyboardsLtd.":"CENTURYPLY",
			"Century Textile & Industries Ltd.":"CENTURYTEX",
			"Cera Sanitaryware Ltd.":"CERA",
			"Cerebra Integrated Technologies Ltd.":"CEREBRAINT",
			"CESC Ltd.":"CESC",
			"CESC Ventures Ltd.":"CESCVENT",
			"Capri Global Capital Ltd":"CGCL",
			"CG Power & Industrial Solutions Ltd.":"CGPOWER",
			"Chalet Hotels Ltd.":"CHALET",
			"Chambal Fertilizers & Chemicals Ltd.":"CHAMBLFERT",
			"Chembond Chemicals Ltd.":"CHEMBOND",
			"Chemfab Alkalis Ltd":"CHEMFAB",
			"Chemfab Alkalis Ltd.":"CHEMFALKAL",
			"Chemplast Sanmar Ltd.":"CHEMPLAST",
			"Chennai Petroleum Corporation Ltd.":"CHENNPETRO",
			"Cheslind Textiles Ltd.":"CHESLINTEX",
			"Chettinad Cement Corporation Ltd.":"CHETTINAD",
			"CHI Investments Ltd ":"CHI",
			"Cholamandalam Investment and Finance Company Ltd.":"CHOLAFIN",
			"Cholamandalam Financial Holdings Ltd.":"CHOLAHLDNG",
			"Chromatic India Ltd.":"CHROMATIC",
			"Cigniti Technologies Ltd":"CIGNITITEC",
			"Cimmco Ltd.":"CIMMCO",
			"Cineline India Ltd":"CINELINE",
			"Cinemax India Ltd":"CINEMAXIN",
			"Cinevista Ltd":"CINEVISTA",
			"Cipla Ltd.":"CIPLA",
			"Cox & Kings Financial Service Ltd.":"CKFSL",
			"Classic DiamondsLtd.":"CLASSIC",
			"CL Educate Ltd":"CLEDUCATE",
			"Clariant ChemicalsLtd.":"CLNINDIA",
			"Clutch Auto Ltd.":"CLUTCHAUTO",
			"C. Mahendra Ltd":"CMAHENDRA",
			"CMC Ltd.":"CMC",
			"CMI Ltd. ":"CMICABLES",
			"CIL Nova Petrochemicals Ltd":"CNOVAPETRO",
			"Coal India Limited":"COALINDIA",
			"Cochin Shipyard Ltd":"COCHINSHIP",
			"Coffee Day Enterprises Ltd":"COFFEEDAY",
			"Colgate-PalmoliveLtd.":"COLPAL",
			"Compuage Infocom Ltd":"COMPINFO",
			"Compucom Software Ltd.":"COMPUSOFT",
			"Computech International Ltd.":"COMPUTECH",
			"Compulink Systems Ltd.":"COMSYS",
			"Container Corporation of India Ltd.":"CONCOR",
			"Confidence Petroleum India Ltd.":"CONFIPET",
			"Consolidated Finvest & Holdings Ltd.":"CONSOFINVT",
			"Control Print Ltd":"CONTROLPR",
			"Coral India Finance & Housing Ltd.":"CORALFINAC",
			"Coral Hub Ltd.":"CORAL_HUB",
			"Cords Cable Industries Ltd":"CORDSCABLE",
			"Core Education & Technologies Ltd":"COREEDUTEC",
			"Coromandel Engineering Co. Ltd.":"COROENGG",
			"Coromandel International Ltd":"COROMANDEL",
			"Corporation Bank":"CORPBANK",
			"Cosmo Films Ltd.":"COSMOFILMS",
			"Country Condo`s Ltd":"COUNCODOS",
			"Cox and Kings Ltd.":"COX_KINGS",
			"Nippon Life India Asset Management Ltd.":"CPSEETF",
			"Cranes Software International Ltd.":"CRANESSOFT",
			"Creative Peripherals & Distribution Ltd":"CREATIVE",
			"Creative Eye Ltd.":"CREATIVEYE",
			"CreditAccess Grameen Ltd.":"CREDITACC",
			"Crest Ventures Ltd.":"CREST",
			"Crest Animation Studios Ltd.":"CRESTANI",
			"Crew B.O.S. Products Ltd.":"CREWBOS",
			"Crisil Ltd.":"CRISIL",
			"Canara Robeco Asset Management Company Ltd":"CRMFGETF",
			"Crompton Greaves Consumer Electrical Ltd":"CROMPTON",
			"CSB Bank Ltd.":"CSBBANK",
			"Cambridge Technology Enterprises Ltd.":"CTE",
			"City Union Bank Ltd.":"CUB",
			"Cubex Tubings Ltd.":"CUBEXTUB",
			"Cummins India Ltd.":"CUMMINSIND",
			"Cupid Ltd.":"CUPID",
			"Cura Technologies Ltd":"CURATECH",
			"Cyber MediaLtd.":"CYBERMEDIA",
			"Cybertech Systems & Software Ltd.":"CYBERTECH",
			"Cyient Ltd.":"CYIENT",
			"LT Foods Ltd.":"DAAWAT",
			"Dabur India Ltd.":"DABUR",
			"Dalmia Bharat Ltd.":"DALBHARAT",
			"Dalmia Bharat Ltd":"DALMIABHA",
			"Dalmia Refractories Ltd.":"DALMIAREF",
			"Dalmia Bharat Sugar and Industries Ltd":"DALMIASUG",
			"Damodar Industries Ltd":"DAMODARIND",
			"Datamatics Global Services Ltd":"DATAMATICS",
			"D.B. Corp Limited":"DBCORP",
			"Dilip Buildcon Ltd":"DBL",
			"D B Realty Limited":"DBREALTY",
			"DBStock Brokers Ltd.":"DBSTOCKBRO",
			"Dishman Carbogen Amcis Ltd.":"DCAL",
			"DCB Bank Ltd.":"DCBBANK",
			"Deccan Chronicle Holdings Ltd.":"DCHL",
			"DCM Ltd.":"DCM",
			"DCM Financial Services Ltd.":"DCMFINSERV",
			"DCM Nouvelle Ltd.":"DCMNVL",
			"DCM Shriram Ltd.":"DCMSHRIRAM",
			"DCW Ltd.":"DCW",
			"Deccan Cements Ltd.":"DECCANCE",
			"Decolight Ceramics Ltd.":"DECOLIGHT",
			"Deepak Fertilisers & Petrochemicals Corp. Ltd.":"DEEPAKFERT",
			"Deepak Nitrite Ltd.":"DEEPAKNTR",
			"Deep Industries Ltd.":"DEEPIND",
			"Delta Corp Ltd":"DELTACORP",
			"Delta Manufacturing Ltd.":"DELTAMAGNT",
			"Den Networks Limited":"DEN",
			"Dena Bank":"DENABANK",
			"De Nora India Ltd.":"DENORA",
			"Denso India Ltd.":"DENSO",
			"DFM Foods Ltd.":"DFMFOODS",
			"Digicontent Ltd.":"DGCONTENT",
			"Dhampur Sugar Mills Ltd":"DHAMPURSUG",
			"Dhanlaxmi Bank Ltd.":"DHANBANK",
			"Dhanuka Agritech Ltd":"DHANUKA",
			"Dhanus Technologies Ltd.":"DHANUS",
			"Dharani Sugars & Chemicals Ltd.":"DHARSUGAR",
			"Dewan Housing Finance Corporation Ltd.":"DHFL",
			"Dhunseri Investments Ltd":"DHUNINV",
			"Prataap Snacks Ltd.":"DIAMONDYD",
			"Diamond Power Infrastructure Ltd.":"DIAPOWER",
			"DIC India Ltd.":"DICIND",
			"DiGiSPICE Technologies Ltd.":"DIGISPICE",
			"Digjam Ltd":"DIGJAM",
			"Digjam Ltd.":"DIGJAMLTD",
			"Dishman Pharmaceuticals & Chemicals Ltd.":"DISHMAN",
			"Dish TV India Ltd":"DISHTV",
			"Divi`s Laboratories Ltd.":"DIVISLAB",
			"Dixon TechnologiesLtd":"DIXON",
			"DLF Ltd.":"DLF",
			"D-LinkLtd.":"DLINKINDIA",
			"Avenue Supermarts Ltd":"DMART",
			"Diligent Media Corporation Limited":"DNAMEDIA",
			"Dolat Investments Ltd.":"DOLAT",
			"Dollar Industries Ltd":"DOLLAR",
			"Dolphin Offshore EnterprisesLtd.":"DOLPHINOFF",
			"Donear Industries Ltd.":"DONEAR",
			"India Power Corporation Ltd":"DPSCLTD",
			"D P Wires Ltd.":"DPWIRES",
			"DQ EntertainmentLtd.":"DQE",
			"Dr. Datsons Labs Ltd":"DRDATSONS",
			"Dredging Corporation of India Ltd.":"DREDGECORP",
			"Dr. Reddy`s Laboratories Ltd.":"DRREDDY",
			"Standard Chartered plc":"DRSTAN",
			"D.S. Kulkarni Developers Ltd.":"DSKULKARNI",
			"Dynacons Systems & Solutions Ltd.":"DSSL",
			"Dhunseri Tea & Industries Ltd":"DTIL",
			"Ducon Infratechnologies Ltd.":"DUCON",
			"Duncans Industries Ltd.":"DUNCANSLTD",
			"Dhunseri Ventures Ltd.":"DVL",
			"Dwarikesh Sugar Industries Ltd.":"DWARKESH",
			"Dynamatic Technologies Ltd.":"DYNAMATECH",
			"Dynemic Products Ltd.":"DYNPRO",
			"ECE Industries Ltd.":"ECEIND",
			"eClerx Services Ltd.":"ECLERX",
			"Edelweiss Financial Services Ltd":"EDELWEISS",
			"Empee Distilleries Ltd.":"EDL",
			"Edserv Softsystems Limited":"EDSERV",
			"Educomp Solutions Ltd.":"EDUCOMP",
			"Eicher Ltd.":"EICHER",
			"Eicher Motors Ltd.":"EICHERMOT",
			"E.I.D.-ParryLtd.":"EIDPARRY",
			"EIH Associated Hotels Ltd.":"EIHAHOTELS",
			"EIH Ltd.":"EIHOTEL",
			"Eimco EleconLtd.":"EIMCOELECO",
			"Everest Kanto Cylinder Ltd.":"EKC",
			"E-Land Apparel Ltd.":"ELAND",
			"Elder Pharmaceuticals Ltd.":"ELDERPHARM",
			"Elecon Engineering Co. Ltd.":"ELECON",
			"Electrosteel Castings Ltd.":"ELECTCAST",
			"ElectrothermLtd.":"ELECTHERM",
			"Electrosteel Steels Ltd":"ELECTROSL",
			"El Forge Ltd.":"ELFORGE",
			"Elgi Equipments Ltd.":"ELGIEQUIP",
			"Elgi Rubber Company Ltd":"ELGIRUBBER",
			"Elgi Rubber Co Ltd":"ELGIRUBCO",
			"Elnet Technologies Ltd.":"ELNET",
			"Emami Ltd.":"EMAMILTD",
			"Emami Paper Mills Ltd":"EMAMIPAP",
			"Emami Realty Ltd.":"EMAMIREAL",
			"Emco Ltd.":"EMCO",
			"Emkay Global Financial Services Ltd":"EMKAY",
			"Emmbi Industries Ltd":"EMMBI",
			"Empee Sugars & Chemicals Ltd.":"EMPEESUG",
			"Endurance Technologies Ltd":"ENDURANCE",
			"Energy Development Co. Ltd.":"ENERGYDEV",
			"Engineers India Ltd.":"ENGINERSIN",
			"Entertainment NetworkLtd.":"ENIL",
			"Entegra Ltd.":"ENTEGRA",
			"Eon Electric Ltd":"EON",
			"Equitas Holding Ltd":"EQUITAS",
			"Era Infra Engineering Ltd.":"ERAINFRA",
			"Eris Lifesciences Ltd.":"ERIS",
			"Eros International Media Ltd":"EROSMEDIA",
			"ESAB India Ltd.":"ESABINDIA",
			"Escorts Ltd.":"ESCORTS",
			"Essar Oil Ltd.":"ESSAROIL",
			"Essar Ports Ltd":"ESSARPORTS",
			"Essar Ports Ltd":"ESSARSHIP",
			"Essar Shipping Ltd":"ESSARSHPNG",
			"Ess Dee Aluminium Ltd.":"ESSDEE",
			"Essel Propack Ltd":"ESSELPACK",
			"Ester Industries Ltd.":"ESTER",
			"Essar Steel Ltd.":"ESTL",
			"ETC Network Ltd.":"ETC",
			"Euro Ceramics Ltd.":"EUROCERA",
			"Euro Multivision Ltd":"EUROMULTI",
			"Eurotex Industries & Exports Ltd.":"EUROTEXIND",
			"Eveready Industries India Ltd.":"EVEREADY",
			"Everest Industries Ltd.":"EVERESTIND",
			"Everonn Education Ltd":"EVERONN",
			"Evinix Industries Ltd.":"EVINIX",
			"Excel Realty N Infra Ltd":"EXCEL",
			"Excel Crop Care Ltd.":"EXCELCROP",
			"Excel Industries Ltd.":"EXCELINDUS",
			"Exide Industries Ltd.":"EXIDEIND",
			"Expleo Solutions Ltd.":"EXPLEOSOL",
			"Fertilisers & Chemicals Travancore Ltd.":"FACT",
			"Fairchem Speciality Ltd.":"FAIRCHEM",
			"Fame India Ltd":"FAME",
			"Farmax India Ltd":"FARMAXIND",
			"Fineotex Chemical Ltd":"FCL",
			"Future Consumer Ltd":"FCONSUMER",
			"FCS Software Solutions Ltd.":"FCSSOFT",
			"FDC Ltd.":"FDC",
			"Fedders Electric & Engineering Ltd":"FEDDERELEC",
			"Federal Bank Ltd.":"FEDERALBNK",
			"Future Enterprises Ltd.":"FEL",
			"Future Enterprises Ltd.":"FELDVR",
			"Fiem Industries Ltd.":"FIEMIND",
			"Filatex India Ltd.":"FILATEX",
			"Finolex Cables Ltd.":"FINCABLES",
			"Fine Organic Industries Ltd.":"FINEORG",
			"Finolex Industries Ltd.":"FINPIPE",
			"First Leasing Co. of India Ltd.":"FIRSTLEASE",
			"First Winner Industries Ltd":"FIRSTWIN",
			"Fresenius Kabi Oncology Ltd":"FKONCO",
			"Uflex Ltd.":"FLEX",
			"Flexituff Ventures International Limited":"FLEXITUFF",
			"Future Lifestyle Fashions Ltd":"FLFL",
			"Gujarat Fluorochemicals Ltd":"FLUOROCHEM",
			"Federal Mogul GoetzeLtd.":"FMGOETZE",
			"Future Market Networks Ltd":"FMNL",
			"Force Motors Ltd.":"FORCEMOT",
			"Fortis Healthcare Ltd":"FORTIS",
			"Foseco India Ltd.":"FOSECOIND",
			"Future Retail Ltd.":"FRETAIL",
			"Future Supply Chain Solutions Ltd.":"FSC",
			"Firstsource Solutions Ltd.":"FSL",
			"Gabriel India Ltd.":"GABRIEL",
			"Gujarat Ambuja Exports Ltd.":"GAEL",
			"GailLtd.":"GAIL",
			"Gyscoal Alloys Ltd":"GAL",
			"Galaxy Surfactants Ltd.":"GALAXYSURF",
			"Gallantt Metal Ltd.":"GALLANTT",
			"Gallantt Ispat Ltd":"GALLISPAT",
			"Gammon Infrastructure Projects Ltd":"GAMMNINFRA",
			"Gammon India Ltd.":"GAMMONIND",
			"Gandhi Special Tubes Ltd.":"GANDHITUBE",
			"Ganesha Ecosphere Ltd":"GANECOS",
			"Ganesh Housing Corporation Ltd.":"GANESHHOUC",
			"Ganges Securities Ltd.":"GANGESSECU",
			"Gangotri Textiles Ltd.":"GANGOTRI",
			"Garden Silk Mills Ltd.":"GARDENSILK",
			"Garware Technical Fibres Ltd.":"GARFIBRES",
			"Gati Ltd.":"GATI",
			"Gayatri Highways Ltd.":"GAYAHWS",
			"Gayatri Projects Ltd.":"GAYAPROJ",
			"Gateway Distriparks Ltd.":"GDL",
			"GeeCee Ventures Ltd":"GEECEE",
			"Geekay Wires Ltd.":"GEEKAYWIRE",
			"GEI Industrial Systems Ltd.":"GEINDSYS",
			"Gemini Communications Ltd.":"GEMINI",
			"Genesys International Corporation Ltd.":"GENESYS",
			"Genus Paper & Boards Ltd.":"GENUSPAPER",
			"Genus Power Infrastructures Ltd":"GENUSPOWER",
			"Geodesic Ltd":"GEODESIC",
			"Geojit Financial Services Ltd.":"GEOJITFSL",
			"Geometric Ltd.":"GEOMETRIC",
			"GE Power India Ltd":"GEPIL",
			"Great Eastern Shipping Co. Ltd.":"GESHIP",
			"GFL Ltd.":"GFLLIMITED",
			"Grand Foundry Ltd.":"GFSTEELS",
			"GHCL Ltd.":"GHCL",
			"GIC Housing Finance Ltd.":"GICHSGFIN",
			"General Insurance Corporation of India":"GICRE",
			"Gillanders Arbuthnot & Co. Ltd.":"GILLANDERS",
			"Gillette India Ltd.":"GILLETTE",
			"Ginni Filaments Ltd.":"GINNIFILA",
			"Gujarat Industries Power Co. Ltd.":"GIPCL",
			"GI Engineering Solutions Ltd.":"GISOLUTION",
			"Gitanjali Gems Ltd.":"GITANJALI",
			"GKB Ophthalmics Ltd.":"GKB",
			"GKW Ltd.":"GKWLIMITED",
			"GlaxoSmithkline Pharmaceuticals Ltd":"GLAXO",
			"Glenmark Pharmaceuticals Ltd.":"GLENMARK",
			"Gujarat Lease Financing Ltd.":"GLFL",
			"Global Vectra Helicorp Ltd.":"GLOBALVECT",
			"Global Offshore Services Ltd":"GLOBOFFS",
			"Globus Spirits Ltd":"GLOBUSSPR",
			"Glodyne Technoserve Ltd":"GLODYNE",
			"Glory Films Ltd":"GLORY",
			"G.M. Breweries Ltd.":"GMBREW",
			"Gujarat Mineral Development Corporation Ltd.":"GMDCLTD",
			"GMM Pfaudler Ltd.":"GMMPFAUDLR",
			"GMR Infrastructure Ltd.":"GMRINFRA",
			"G N A Axles Ltd.":"GNA",
			"Gujarat Narmada Valley Fertilizers & Chemicals Ltd":"GNFC",
			"Goa Carbon Ltd.":"GOACARBON",
			"GOCL Corporation Ltd.":"GOCLCORP",
			"Godavari Fertilisers & Chemicals Ltd.":"GODAVRFERT",
			"Godfrey Phillips India Ltd.":"GODFRYPHLP",
			"Godrej Agrovet Limited":"GODREJAGRO",
			"Godrej Consumer Products Ltd":"GODREJCP",
			"Godrej Industries Ltd.":"GODREJIND",
			"Godrej Properties Limited":"GODREJPROP",
			"Goenka Diamond & Jewels Limited":"GOENKA",
			"Gokaldas Exports Ltd.":"GOKEX",
			"Gokul Refoils & Solvent Ltd.":"GOKUL",
			"Gokul Agro Resources Ltd.":"GOKULAGRO",
			"Nippon Life India Asset Management Ltd.":"GOLDBEES",
			"Golden Tobacco Ltd":"GOLDENTOBC",
			"Goldiam International Ltd.":"GOLDIAM",
			"Unit Trust of India":"GOLDSHARE",
			"Goldstone Technologies Ltd":"GOLDTECH",
			"Goodluck India Ltd.":"GOODLUCK",
			"Godawari Power & Ispat Ltd.":"GPIL",
			"Gujarat Pipavav Port Ltd":"GPPL",
			"GPT Infraprojects Ltd":"GPTINFRA",
			"Grabal Alok Impex Ltd.":"GRABALALK",
			"Granules India Ltd.":"GRANULES",
			"Graphite India Ltd":"GRAPHITE",
			"Grasim Industries Ltd.":"GRASIM",
			"Gravita India Limited":"GRAVITA",
			"Greaves Cotton Ltd.":"GREAVESCOT",
			"Greenlam Industries Ltd.":"GREENLAM",
			"GREENLAM INDUSTRIES LTD.":"GREENLAM_1",
			"Greenpanel Industries Ltd.":"GREENPANEL",
			"Greenply Industries Ltd.":"GREENPLY",
			"Orient Green Power Company Limited":"GREENPOWER",
			"Grindwell Norton Ltd.":"GRINDWELL",
			"Grob Tea Co Ltd":"GROBTEA",
			"GRP Ltd.":"GRPLTD",
			"Garden Reach Shipbuilders & Engineers Ltd.":"GRSE",
			"GRUH Finance Ltd.":"GRUH",
			"Gujarat Sidhee Cement Ltd.":"GSCLCEMENT",
			"Gujarat State Fertilizers & Chemicals Ltd.":"GSFC",
			"GlaxoSmithkline Consumer Healthcare Ltd.":"GSKCONS",
			"GSL Nova Petrochemicals Ltd":"GSLNOVA",
			"Gujarat State Petronet Ltd.":"GSPL",
			"GSS Infotech Ltd.":"GSS",
			"GTL Ltd.":"GTL",
			"GTL Infrastucture Ltd":"GTLINFRA",
			"GTN Industries Ltd.":"GTNIND",
			"GTN Textiles Ltd.":"GTNTEX",
			"GOL Offshore Ltd":"GTOFFSHORE",
			"GTPL Hathway Ltd":"GTPL",
			"Gufic Biosciences Ltd.":"GUFICBIO",
			"Gujarat Alkalies & Chemicals Ltd.":"GUJALKALI",
			"Gujarat Apollo Industries Ltd.":"GUJAPOLLO",
			"Gujarat Gas Ltd":"GUJGASLTD",
			"Gujarat NRE Coke Ltd":"GUJNRECOKE",
			"Gujarat NRE Coke Ltd":"GUJNREDVR",
			"Gujarat Raffia Industries Ltd.":"GUJRAFFIA",
			"Gujarat Gas Co. Ltd.":"GUJRATGAS",
			"Gujarat State Financial Corporation":"GUJSTATFIN",
			"Gulf Oil Lubricants India Ltd":"GULFOILLUB",
			"GP Petroleums Ltd.":"GULFPETRO",
			"Gulshan Polyols Ltd":"GULPOLY",
			"GVK Power & Infrastructure Ltd.":"GVKPIL",
			"Hindustan Aeronautics Ltd.":"HAL",
			"Hanung Toys & Textiles Ltd.":"HANUNG",
			"Harita Seating Systems Ltd.":"HARITASEAT",
			"Harrisons Malayalam Ltd.":"HARRMALAYA",
			"Hathway Cable & Datacom Limited":"HATHWAY",
			"Hatsun Agro Products Ltd.":"HATSUN",
			"Havells India Ltd.":"HAVELLS",
			"Sri Havisha Hospitality & Infrastructure Ltd.":"HAVISHA",
			"HBL Power Systems Ltd.":"HBLPOWER",
			"HB Stockholdings Ltd.":"HBSL",
			"Hindustan Construction Co. Ltd.":"HCC",
			"HealthCare Global Enterprises Ltd":"HCG",
			"BOND 0% 2022 TR-2 SR-II":"HCIDFCBANK",
			"HCL Infosystems Ltd.":"HCL_INSYS",
			"HCL Technologies Ltd.":"HCLTECH",
			"Housing Development Finance Corporation Ltd.":"HDFC",
			"HDFC Asset Management Company Ltd.":"HDFCAMC",
			"HDFC Bank Ltd.":"HDFCBANK",
			"HDFC Life Insurance Co. Ltd.":"HDFCLIFE",
			"HDFC Asset Management Company Ltd.":"HDFCMFGETF",
			"HDFC Asset Management Company Ltd.":"HDFCNIFETF",
			"HDFC Asset Management Company Ltd.":"HDFCSENETF",
			" ":"HDIDFCBANK",
			"Housing Development & Infrastructure Ltd.":"HDIL",
			"H.E.G. Ltd.":"HEG",
			"HeidelbergCement India Ltd":"HEIDELBERG",
			"Helios & Matheson Information Technology Ltd.":"HELIOSMATH",
			"Hercules Hoists Ltd.":"HERCULES",
			"Heritage Foods Ltd":"HERITGFOOD",
			"Hero MotoCorp Ltd":"HEROMOTOCO",
			"Hester Biosciences Ltd":"HESTERBIO",
			"Hexa Tradex Ltd":"HEXATRADEX",
			"Hexaware Technologies Ltd.":"HEXAWARE",
			"HFCL Ltd.":"HFCL",
			"H.G. Infra Engineering Ltd.":"HGINFRA",
			"Hinduja Global Solutions Ltd.":"HGS",
			"High Ground Enterprise Ltd":"HIGHGROUND",
			"Hikal Ltd.":"HIKAL",
			"HIL Ltd":"HIL",
			"Hilton Metal Forging Ltd.":"HILTON",
			"Himatsingka Seide Ltd.":"HIMATSEIDE",
			"Hindalco Industries Ltd.":"HINDALCO",
			"Hindustan Composites Ltd.":"HINDCOMPOS",
			"Hindustan Copper Ltd.":"HINDCOPPER",
			"Hindustan Dorr-Oliver Ltd.":"HINDDORROL",
			"Hindustan Motors Ltd.":"HINDMOTORS",
			"Hindusthan National Glass & Industries Ltd.":"HINDNATGLS",
			"Hindustan Oil Exploration Co. Ltd.":"HINDOILEXP",
			"Hindustan Petroleum Corporation Ltd.":"HINDPETRO",
			"Hind Syntex Ltd.":"HINDSYNTEX",
			"Hinduja Foundries Ltd.":"HINDUJAFO",
			"Hindustan Unilever Ltd.":"HINDUNILVR",
			"Hindustan Zinc Ltd.":"HINDZINC",
			"HSBC InvestDirectLtd":"HINVDIR",
			"Hira Ferro Alloys Ltd":"HIRAFERRO",
			"Hind Rectifiers Ltd.":"HIRECT",
			"Hisar Metal Industries Ltd.":"HISARMETAL",
			"Hi-Tech Pipes Ltd.":"HITECH",
			"Hitech Corporation Ltd.":"HITECHCORP",
			"The Hi-Tech Gears Ltd":"HITECHGEAR",
			"HLV Ltd.":"HLVLTD",
			"HMT Ltd.":"HMT",
			"Hindustan Media Ventures Limited":"HMVL",
			"Hindustan Foods Ltd.":"HNDFDS",
			"Nippon Life India Asset Management Ltd.":"HNGSNGBEES",
			"Hindustan Organic Chemicals Ltd.":"HOCL",
			"Honeywell Automation India Ltd.":"HONAUT",
			"Honda SIEL Power Products Ltd.":"HONDAPOWER",
			"Hotel Rugby Ltd.":"HOTELRUGBY",
			"HOV Services Ltd.":"HOVS",
			"HPL Electric & Power Ltd.":"HPL",
			"Himadri Speciality Chemical Ltd.":"HSCL",
			"HSIL Ltd":"HSIL",
			"HT Media Ltd.":"HTMEDIA",
			"Hubtown Ltd":"HUBTOWN",
			"Housing & Urban Development Corporation Ltd":"HUDCO",
			"Indiabulls Asset Management Company Ltd.":"IBMFNIFTY",
			"IBP Co. Ltd.":"IBP",
			"Indiabulls Real Estate Ltd.":"IBREALEST",
			"Indiabulls Housing Finance Limited":"IBULHSGFIN",
			"Indiabulls Integrated Services Ltd.":"IBULISL",
			"Indiabulls Ventures Ltd.":"IBVENTURES",
			"Indo Count Industries Ltd.":"ICIL",
			"ICRA Ltd.":"ICRA",
			"I.C.S.ALtd":"ICSA",
			"IDBI Bank Ltd":"IDBI",
			"IDBI Bank Ltd":"IDBIGOLD",
			"Vodafone Idea Ltd.":"IDEA",
			"IDFC Ltd":"IDFC",
			"IDFC First Bank Ltd.":"IDFCFIRSTB",
			"IDFC Asset Management Company Limited":"IDFNIFTYET",
			"Nifty Pvt Bank":"IDNIFTYPBK",
			"Indian Energy Exchange Ltd.":"IEX",
			"IFB Agro Industries Ltd.":"IFBAGRO",
			"IFB Industries Ltd.":"IFBIND",
			"IFCI Ltd.":"IFCI",
			"IFGL Refractories Ltd":"IFGLEXPOR",
			"IFGL Refractories Ltd.":"IFGLREFRAC",
			"India Foils Ltd.":"IFL",
			"Igarashi Motors India Ltd.":"IGARASHI",
			"Indraprastha Gas":"IGL",
			"ICICI PRUDENTIAL GOLD ETF":"IGOLD",
			"I G Petrochemicals Ltd.":"IGPL",
			"iGate Global Solutions Ltd.":"IGS",
			"IIFL Finance Ltd.":"IIFL",
			"India Infoline Asset Management Co. Ltd":"IIFLNIFTY",
			"IIFL Securities Limited":"IIFLSEC",
			"IIFL Wealth Management Ltd":"IIFLWAM",
			"Industrial Investment Trust Ltd.":"IITL",
			"ACC LIMITED":"ILACC",
			"ADVANTA INDIA LTD":"ILADVANTA",
			"ALLAHABAD BANK":"ILALBK",
			"ANDHRA BANK":"ILANDHRABANK",
			"AXIS BANK LIMITED":"ILAXISBANK",
			"BANK OF BARODA":"ILBANKBARODA",
			"BANK OF INDIA":"ILBANKINDIA",
			"BHARTI AIRTEL LIMITED":"ILBHARTIARTL",
			"BRANDHOUSE RETAILS LTD":"ILBRANDHOUSE",
			"CANARA BANK":"ILCANBK",
			"CARBORUNDUM UNIVERSAL LTD":"ILCARBORUNIV",
			"CENTURION BANK OF PUNJAB":"ILCENTBOP",
			"CMC LTD":"ILCMC",
			"CONTAINER CORP OF IND LTD":"ILCONCOR",
			"CITY UNION BANK LTD":"ILCUB",
			"D.B.CORP LTD":"ILDBCORP",
			"DECCAN CHRONICLE HOLD LTD":"ILDCHL",
			"DENA BANK":"ILDENABANK",
			"DYNAMATIC TECHNOLOGIES":"ILDYNAMATECH",
			"ENTERTAIN NET. IND. LTD.":"ILENIL",
			"FEDERAL BANK LTD":"ILFEDERALBNK",
			"FORTIS HEALTHCARE LTD":"ILFORTIS",
			"FUTURE RETAIL LIMITED":"ILFRL",
			"IL&FS Engineering and Construction Co Ltd":"IL_FSENGG",
			"IL&FS Transportation Networks Ltd.":"IL_FSTRANS",
			"GUJARAT PIPAVAV PORT LTD":"ILGPPL",
			"GRASIM INDUSTRIES LTD":"ILGRASIM",
			"HATHWAY CABLE & DATACOM":"ILHATHWAY",
			"ICICI BANK LTD.":"ILICICIBANK",
			"IDFC LIMITED":"ILIDFC",
			"IFCI LTD":"ILIFCI",
			"INDRAPRASTHA GAS LTD":"ILIGL",
			"INDUSIND BANK LIMITED":"ILINDUSINDBK",
			"ING VYSYA BANK LTD":"ILINGVYSYABK",
			"INDIAN OVERSEAS BANK":"ILIOB",
			"IPCA LABORATORIES LTD":"ILIPCALAB",
			"JAGRAN PRAKASHAN LIMITED":"ILJAGRAN",
			"JKUMAR INFR.LTD.":"ILJKIL",
			"JAIPRAKASH ASSOCIATES LTD":"ILJPASSOCIAT",
			"JUBILANT FOODWORKS LTD":"ILJUBLFOOD",
			"KALINDEE RAIL NR.LTD":"ILKALINDEE",
			"KARUR VYSYA BANK LTD":"ILKARURVYSYA",
			"KOTAK MAHINDRA BANK LTD":"ILKOTAKBANK",
			"LUPIN LIMITED":"ILLUPIN",
			"MARUTI SUZUKI INDIA LTD.":"ILMARUTI",
			"MULTI COMMODITY EXCHANGE":"ILMCX",
			"PANTALOON RETAILLTD":"ILPANTALOONR",
			"PATNI COMPUTER SYST LTD":"ILPATNI",
			"PERSISTENT SYSTEMS LTD":"ILPERSISTENT",
			"PETRONET LNG LIMITED":"ILPETRONET",
			"PUNJAB NATIONAL BANK":"ILPNB",
			"POWER GRID CORP. LTD.":"ILPOWERGRID",
			"PRESTIGE ESTATE LTD":"ILPRESTIGE",
			"RURAL ELEC CORP. LTD.":"ILRECLTD",
			"REPCO HOME FINANCE LTD":"ILREPCOHOME",
			"STATE BANK OF INDIA":"ILSBIN",
			"SESA GOA LTD":"ILSESAGOA",
			"THE SOUTH INDIAN BANK LTD":"ILSOUTHBANK",
			"STRIDES ACROLAB LIMITED":"ILSTAR",
			"TATA STEEL LIMITED":"ILTATASTEEL",
			"TITAN COMPANY LIMITED":"ILTITAN",
			"TITAN INDUSTRIES LTD":"ILTITAN_1",
			"UNION BANK OF INDIA":"ILUNIONBANK",
			"UPL LIMITED":"ILUPL",
			"VIJAYA BANK":"ILVIJAYABANK",
			"VMART RETAIL LTD":"ILVMART",
			"YES BANK LIMITED":"ILYESBANK",
			"ZEE NEWS LIMITED":"ILZEENEWS",
			"Imagicaaworld Entertainment Ltd.":"IMAGICAA",
			"Indian Metals & Ferro Alloys Ltd.":"IMFA",
			"India Motor Parts & Accessories Ltd.":"IMPAL",
			"Impex Ferro Tech Ltd.":"IMPEXFERRO",
			"Indbank Merchant Banking Services Ltd.":"INDBANK",
			"Indian Hotels Co. Ltd.":"INDHOTEL",
			"Indiabulls Financial Services":"INDIABULLS",
			"India Cements Ltd.":"INDIACEM",
			"India Glycols Ltd.":"INDIAGLYCO",
			"Indiamart Intermesh Ltd.":"INDIAMART",
			"Indian Bank":"INDIANB",
			"Indian Card Clothing Co. Ltd.":"INDIANCARD",
			"Indian Hume Pipe Co. Ltd.":"INDIANHUME",
			"InterGlobe Aviation Ltd.":"INDIGO",
			"IMP Powers Ltd":"INDLMETER",
			"India Nippon Electricals Ltd.":"INDNIPPON",
			"Indoco Remedies Ltd":"INDOCO",
			"Indo Rama Synthetics Ltd.":"INDORAMA",
			"Indo Rama Textiles Ltd.":"INDORAMTEX",
			"Indosolar Ltd":"INDOSOLAR",
			"Indostar Capital Finance Ltd":"INDOSTAR",
			"Indo Tech Transformers Ltd.":"INDOTECH",
			"Indo Thai Securities Ltd":"INDOTHAI",
			"Indowind Energy Ltd.":"INDOWIND",
			"Indraprastha Medical Corporation Ltd.":"INDRAMEDCO",
			"Ind-Swift Laboratories Ltd.":"INDSWFTLAB",
			"Ind-Swift Ltd.":"INDSWFTLTD",
			"Indian Terrain Fashions Ltd.":"INDTERRAIN",
			"Indus Fila Ltd.":"INDUSFILA",
			"IndusInd Bank Ltd.":"INDUSINDBK",
			"INEOS Styrolution India Ltd.":"INEOSSTYRO",
			"Infibeam Avenues Ltd.":"INFIBEAM",
			"Infinite Computer SolutionsLtd":"INFINITE",
			"InfoBeans Technologies Ltd":"INFOBEAN",
			"Info-Drive Software Ltd.":"INFODRIVE",
			"Infomedia Press Ltd":"INFOMEDIA",
			"Nippon Life India Asset Management Ltd.":"INFRABEES",
			"Bharti Infratel Ltd":"INFRATEL",
			"Infosys Ltd":"INFY",
			"Ingersoll RandLtd.":"INGERRAND",
			"Ing Vysya Bank Ltd.":"INGVYSYABK",
			"ICICIPRAMC NIFETF":"INIFTY",
			"Innoventive Industries Ltd":"INNOIND",
			"INOX Leisure Ltd.":"INOXLEISUR",
			"Inox Wind Ltd":"INOXWIND",
			"InsecticidesLtd.":"INSECTICID",
			"Inspirisys Solutions Ltd.":"INSPIRISYS",
			"Integra Garments & Textiles Ltd":"INTEGRA",
			"Intellect Design Arena Ltd":"INTELLECT",
			"Intense Technologies Ltd.":"INTENTECH",
			"Inventure Growth and Securities Ltd":"INVENTURE",
			"Indian Overseas Bank":"IOB",
			"Indian Oil Corporation Ltd.":"IOC",
			"IOL Chemicals & Pharmaceuticals Ltd.":"IOLCP",
			"IOL Netcom Ltd.":"IOLN",
			"Ipca Laboratories Ltd.":"IPCALAB",
			"Indian Petrochemicals Corporation Ltd.":"IPCL",
			"IP Rings Ltd.":"IPRINGLTD",
			"IRB Infrastructure Developers Ltd":"IRB",
			"IRCON International Ltd":"IRCON",
			"Indian Railway Catering & Tourism Corporation Ltd.":"IRCTC",
			"ICICI Securities Ltd":"ISEC",
			"Intrasoft Technologies Limited":"ISFT",
			"ISMT Ltd.":"ISMTLTD",
			"BDR Buildcon Ltd":"ITBDR",
			"ITC Ltd.":"ITC",
			"India Tourism Development Corporation Ltd.":"ITDC",
			"ITD Cementation India Ltd.":"ITDCEM",
			"Frog Cellsat Ltd.":"ITFROGCELL",
			"GIR Natureview Resorts Ltd.":"ITGIRRESORTS",
			"ITI Ltd.":"ITI",
			"InfoBeans Technologies Ltd":"ITINFOBEANS",
			"K A Wires Ltd.":"ITKAWIRES",
			"MIG Media Neurons Ltd":"ITMMNL",
			"Mohini Fibers Ltd.":"ITMOHINI",
			"M.R. Organisation Ltd":"ITMRO",
			"QVC Realty Co. Ltd":"ITQVC",
			"IL & FS Investment Managers Ltd.":"IVC",
			"India Grid Trust":"IVINDIGRID",
			"IndInfravit Trust":"IVINDINFR",
			"IRB InvIT Fund":"IVIRBINVIT",
			"IVP Ltd.":"IVP",
			"IVRCL Assets & Holdings Ltd":"IVRCLAH",
			"IVRCL Ltd":"IVRCLINFRA",
			"Invesco Asset ManagementPvt. Ltd.":"IVZINGOLD",
			"Invesco Asset ManagementPvt. Ltd.":"IVZINNIFTY",
			"izmo Ltd.":"IZMO",
			"Jagran Prakashan Ltd.":"JAGRAN",
			"Jagsonpal Pharmaceuticals Ltd.":"JAGSNPHARM",
			"Jai Balaji Industries Ltd.":"JAIBALAJI",
			"Jai Corp Ltd.":"JAICORPLTD",
			"Jaihind Projects Ltd.":"JAIHINDPRO",
			"Jain Studios Ltd.":"JAINSTUDIO",
			"Jamna Auto Industries Ltd.":"JAMNAAUTO",
			"Jash Engineering Ltd.":"JASH",
			"Jayant Agro-Organics Ltd.":"JAYAGROGN",
			"Jay Bharat Maruti Ltd.":"JAYBARMARU",
			"Jayaswal NECO Industries Ltd.":"JAYNECOIND",
			"Jaypee Hotels Ltd.":"JAYPEEHOT",
			"Jay Shree Tea & Industries Ltd.":"JAYSREETEA",
			"J.B. Chemicals & Pharmaceuticals Ltd.":"JBCHEPHARM",
			"JBF Industries Ltd.":"JBFIND",
			"JBM Auto Ltd":"JBMA",
			"Johnson Controls-Hitachi Air Conditioning India Ltd.":"JCHAC",
			"JCT Electronics Ltd.":"JCTEL",
			"J D Orgochem Ltd":"JDORGOCHEM",
			"Jenson & NicholsonLtd.":"JENSONICOL",
			"Jet Airways India":"JETAIRWAYS",
			"Jeypore Sugar Co. Ltd.":"JEYPORE",
			"JHS Svendgaard Laboratories Ltd.":"JHS",
			"JIK Industries Ltd.":"JIKIND",
			"JIK Industries Ltd.":"JIKINDS",
			"Jindal Photo Ltd.":"JINDALPHOT",
			"Jindal Poly Films Ltd.":"JINDALPOLY",
			"Jindal SAW Ltd.":"JINDALSAW",
			"Jindal Steel & Power Ltd.":"JINDALSTEL",
			"Jindal Cotex Limited.":"JINDCOT",
			"Jindal Drilling & Industries Ltd.":"JINDRILL",
			"Jindal Worldwide Ltd.":"JINDWORLD",
			"Jain Irrigation Systems Ltd.":"JISLDVREQS",
			"Jain Irrigation Systems Ltd.":"JISLJALEQS",
			"JITF Infralogistics Ltd":"JITFINFRA",
			"Jiya Eco-Products Ltd.":"JIYAECO",
			"Jammu & Kashmir Bank Ltd.":"J_KBANK",
			"J.K. Cement Ltd.":"JKCEMENT",
			"J.Kumar Infraprojects Ltd":"JKIL",
			"JK Lakshmi Cement Ltd.":"JKLAKSHMI",
			"JK Paper Ltd":"JKPAPER",
			"JK Tyre & Industries Ltd.":"JKTYRE",
			"Jullundur Motor AgencyLtd.":"JMA",
			"JMC ProjectsLtd.":"JMCPROJECT",
			"JM Financial Ltd.":"JMFINANCIL",
			"JMT Auto Ltd.":"JMTAUTOLTD",
			"Jocil Ltd":"JOCIL",
			"Jaiprakash Associates Ltd.":"JPASSOCIAT",
			"Jaypee Infratech Ltd":"JPINFRATEC",
			"Jindal Poly Investment & Finance Co. Ltd.":"JPOLYINVST",
			"Jaiprakash Power Ventures Ltd":"JPPOWER",
			"Jindal Stainless Ltd":"JSL",
			"Jindal StainlessLtd":"JSLHISAR",
			"JSW Energy Ltd":"JSWENERGY",
			"JSW Holdings Ltd":"JSWHL",
			"JSW ISPAT Steel Ltd":"JSWISPAT",
			"JSW Steel Ltd.":"JSWSTEEL",
			"JTEKT India Ltd.":"JTEKTINDIA",
			"Jubilant Life Sciences Ltd":"JUBILANT",
			"Jubilant FoodWorks Limited":"JUBLFOOD",
			"Jubilant Industries Ltd":"JUBLINDS",
			"Jumbo Bag Ltd.":"JUMBO",
			"Jump Networks Ltd.":"JUMPNET",
			"Nippon Life India Asset Management Ltd.":"JUNIORBEES",
			"Jupiter Bioscience Ltd.":"JUPITER",
			"Just Dial Ltd":"JUSTDIAL",
			"JVL Agro Industries Ltd":"JVLAGRO",
			"Jyothy Labs Ltd.":"JYOTHYLAB",
			"Jyoti Structures Ltd.":"JYOTISTRUC",
			"ICICI -INDEX WARRANTS":"K1ICICI",
			"Kabra Extrusiontechnik Ltd.":"KABRAEXTRU",
			"Kajaria Ceramics Ltd.":"KAJARIACER",
			"Kakatiya Cement Sugar & Industries Ltd.":"KAKATCEM",
			"Kalindee Rail NirmanLtd.":"KALINDEE",
			"Kalpataru Power Transmission Ltd.":"KALPATPOWR",
			"Kalyani Forge Ltd.":"KALYANIFRG",
			"Kamat HotelsLtd":"KAMATHOTEL",
			"Kamdhenu Ltd.":"KAMDHENU",
			"Kanani Industries Ltd.":"KANANIIND",
			"Kandagiri Spinning Mills Ltd.":"KANDAGIRI",
			"Kanoria Chemicals & Industries Ltd.":"KANORICHEM",
			"Kansai Nerolac Paints Ltd.":"KANSAINER",
			"Karda Constructions Ltd.":"KARDA",
			"Karma Energy Ltd.":"KARMAENG",
			"Karur K.C.P. Packkagings Ltd.":"KARURKCP",
			"Karur Vysya Bank Ltd.":"KARURVYSYA",
			"Kaushalya Infrastructure Development Corp.Ltd.":"KAUSHALYA",
			"Kavveri Telecom Products Ltd.":"KAVVERITEL",
			"Kaya Ltd.":"KAYA",
			"Kirloskar Brothers Investments Ltd":"KBIL",
			"KCP Ltd.":"KCP",
			"K.C.P. Sugar & Industries Corporation Ltd.":"KCPSUGIND",
			"KDDL Ltd":"KDDL",
			"KEC International Ltd.":"KEC",
			"Kirloskar Electric Co. Ltd.":"KECL",
			"KEI Industries Ltd.":"KEI",
			"Kellton Tech Solutions Ltd":"KELLTONTEC",
			"Kemrock Industries & Exports Ltd.":"KEMROCK",
			"Kennametal India Ltd.":"KENNAMET",
			"Kernex MicrosystemsLtd.":"KERNEX",
			"Kesar Enterprises Ltd.":"KESARENT",
			"Kesoram Industries Ltd.":"KESORAMIND",
			"Keynote Financial Services Ltd.":"KEYFINSERV",
			"Kingfisher Airlines Ltd":"KFA",
			"Karuturi Global Ltd":"KGL",
			"Khadim India Ltd":"KHADIM",
			"Khaitan Electricals Ltd.":"KHAITANELE",
			"KhaitanLtd.":"KHAITANLTD",
			"Khandwala Securities Ltd.":"KHANDSE",
			"Kalyani Investment Co Ltd":"KICL",
			"Kilitch DrugsLtd.":"KILITCH",
			"Kinetic Motor Co. Ltd.":"KINETICMOT",
			"Kingfa Science & TechnologyLtd.":"KINGFA",
			"KIOCL Ltd.":"KIOCL",
			"Kiri Industries Ltd":"KIRIINDUS",
			"Kirloskar Ferrous Industries Ltd.":"KIRLFER",
			"Kirloskar Brothers Ltd.":"KIRLOSBROS",
			"Kirloskar Oil Engines Ltd":"KIRLOSENG",
			"Kirloskar Industries Ltd.":"KIRLOSIND",
			"Kitex Garments Ltd.":"KITEX",
			"Kitply Industries Ltd.":"KITPLYIND",
			"Kewal Kiran Clothing Ltd.":"KKCL",
			"KLG Systel Ltd.":"KLGSYSTEL",
			"KLRF Ltd":"KLRF",
			"K.M. Sugar Mills Ltd.":"KMSUGAR",
			"KNR Constructions Ltd":"KNRCON",
			"Kohinoor Foods Ltd.":"KOHINOOR",
			"Kojam Fininvest Ltd.":"KOJAMFIN",
			"Kokuyo Camlin Ltd":"KOKUYOCMLN",
			"Kolte-Patil Developers Ltd.":"KOLTEPATIL",
			"KDL Biotech Ltd.":"KOPDRUGS",
			"Kopran Ltd.":"KOPRAN",
			"Kotak Mahindra Bank Ltd.":"KOTAKBANK",
			"Kotak Mahindra Asset Management Company Ltd":"KOTAKBKETF",
			"Kotak Mahindra Asset Management Company Ltd":"KOTAKGOLD",
			"Kotak Mahindra Asset Management Company Ltd":"KOTAKPSUBK",
			"Kothari Sugars & Chemicals Ltd.":"KOTARISUG",
			"Kothari Petrochemicals Ltd.":"KOTHARIPET",
			"Kothari Products Ltd.":"KOTHARIPRO",
			"Koutons Retail India Ltd.":"KOUTONS",
			"Kovai Medical Center & Hospital Ltd.":"KOVAI",
			"KPIT Technologies Ltd.":"KPITTECH",
			"K.P.R. Mill Ltd.":"KPRMILL",
			"KRBL Ltd.":"KRBL",
			"Krebs Biochemicals & Industries Ltd.":"KREBSBIO",
			"Kridhan Infra Ltd":"KRIDHANINF",
			"Krishana Phoschem Ltd":"KRISHANA",
			"Krishna Engineering Works Ltd.":"KRISHNAENG",
			"Kriti IndustriesLtd.":"KRITIIND",
			"KSB Ltd.":"KSB",
			"Kaveri Seed Co. Ltd.":"KSCL",
			"KSE Ltd.":"KSE",
			"KSS Ltd":"KSERASERA",
			"KSK Energy Ventures Ltd":"KSK",
			"Kalyani Steels Ltd.":"KSL",
			"K.S. Oils Ltd.":"KSOILS",
			"Kesar Terminals & Infrastructure Ltd.":"KTIL",
			"Karnataka Bank Ltd.":"KTKBANK",
			"Kuantum Papers Ltd":"KUANTUM",
			"Kwality Ltd":"KWALITY",
			"Lakshmi Precision Screws Ltd.":"LAKPRE",
			"Lakshmi Energy and Foods Ltd":"LAKSHMIEFL",
			"Lakshmi Mills Co. Ltd.":"LAKSHMIMIL",
			"Lakshmi Vilas Bank Ltd.":"LAKSHVILAS",
			"Dr. Lal PathLabs Ltd.":"LALPATHLAB",
			"Lambodhara Textile Ltd.":"LAMBODHARA",
			"La Opala RG Ltd.":"LAOPALA",
			"Lasa Supergenerics Ltd.":"LASA",
			"Laurus Labs Ltd.":"LAURUSLABS",
			"Lakshmi Machine Works Ltd.":"LAXMIMACH",
			"LCC Infotech Ltd.":"LCCINFOTEC",
			"LEEL Electricals Ltd":"LEEL",
			"Lemon Tree Hotels Ltd.":"LEMONTREE",
			"Lakshmi Finance & Industrial Corporation Ltd":"LFIC",
			"L.G. Balakrishnan & Bros Ltd.":"LGBBROSLTD",
			"LGB Forge Ltd.":"LGBFORGE",
			"Libas Designs Ltd.":"LIBAS",
			"Liberty Shoes Ltd.":"LIBERTSHOE",
			"LIC Housing Finance Ltd.":"LICHSGFIN",
			"Lincoln Pharmaceuticals Ltd.":"LINCOLN",
			"Linc Pen & Plastics Ltd.":"LINCPEN",
			"Linde India Ltd":"LINDEINDIA",
			"Nippon Life India Asset Management Ltd.":"LIQUIDBEES",
			"DSP BlackRock Investment Managers Private Limited":"LIQUIDETF",
			"Lanco Infratech Ltd.":"LITL",
			"Lloyds Finance Ltd.":"LLOYDFIN",
			"LML Ltd.":"LML",
			"Lokesh Machines Ltd.":"LOKESHMACH",
			"Lotte India Corporation Ltd.":"LOTTEINDIA",
			"Lotus Eye Hospital and Institute Ltd":"LOTUSEYE",
			"Lovable Lingerie Ltd":"LOVABLE",
			"Landmark Property Development Company Ltd":"LPDC",
			"Lloyds Steels Industries Ltd.":"LSIL",
			"Larsen & Toubro Ltd.":"LT",
			"Larsen & Toubro Infotech Ltd.":"LTI",
			"L&T Technology Services Ltd":"LTTS",
			"Lumax Automotive Systems Ltd.":"LUMAXAUTO",
			"Lumax Industries Ltd.":"LUMAXIND",
			"Lumax Auto Technologies Ltd.":"LUMAXTECH",
			"Lupin Ltd":"LUPIN",
			"Lux Industries Ltd.":"LUXIND",
			"Lyka Labs Ltd.":"LYKALABS",
			"Lypsa Gems & Jewellery Ltd":"LYPSAGEMS",
			"Motilal Oswal Asset Management Company Limited":"M100",
			"ICICI Bank Ltd.":"M1ICICI",
			"Motilal Oswal Asset Management Company Limited":"M50",
			"Maan Aluminium Ltd":"MAANALU",
			"Maars Software International Ltd.":"MAARSOFTW",
			"Madhav Marbles & Granites Ltd.":"MADHAV",
			"Madhucon Projects Ltd.":"MADHUCON",
			"Madras Fertilizers Ltd.":"MADRASFERT",
			"Magadh Sugar & Energy Ltd.":"MAGADSUGAR",
			"Magma Fincorp Ltd":"MAGMA",
			"Magnum Ventures Ltd.":"MAGNUM",
			"Bank of Maharashtra":"MAHABANK",
			"Maha Rashtra Apex Corporation Ltd.":"MAHAPEXLTD",
			"Mahamaya Steel Industries Ltd":"MAHASTEEL",
			"Mahindra EPC Irrigation Ltd.":"MAHEPC",
			"Maheshwari Logistics Ltd.":"MAHESHWARI",
			"Mahindra CIE Automotive Ltd.":"MAHINDCIE",
			"Mahindra Ugine Steel Co. Ltd.":"MAHINDUGIN",
			"Mahindra Lifespace Developers Ltd.":"MAHLIFE",
			"Mahindra Logistics Ltd.":"MAHLOG",
			"Maharashtra Scooters Ltd.":"MAHSCOOTER",
			"Maharashtra Seamless Ltd.":"MAHSEAMLES",
			"Maithan Alloys Ltd":"MAITHANALL",
			"Majesco Ltd":"MAJESCO",
			"Marico Kaya Enterprises Ltd":"MAKE",
			"Madras Aluminium Co Ltd":"MALCO",
			"Malu Paper Mills Ltd.":"MALUPAPER",
			"Malwa Cotton Spinning Mills Ltd.":"MALWACOTT",
			"Mirae Asset Investment ManagersPvt Ltd":"MAN50ETF",
			"Manaksia Aluminium Co. Ltd.":"MANAKALUCO",
			"Manaksia Coated Metals & Industries Ltd.":"MANAKCOAT",
			"Manaksia Ltd.":"MANAKSIA",
			"Manaksia Steels Ltd.":"MANAKSTEEL",
			"Manali Petrochemicals Ltd":"MANALIPETC",
			"Manappuram Finance Ltd":"MANAPPURAM",
			"Mangalam Drugs & Organics Ltd.":"MANGALAM",
			"Mangalore Chemicals & Fertilisers Ltd.":"MANGCHEFER",
			"Mangalam Cement Ltd.":"MANGLMCEM",
			"Mangalam Timber Products Ltd.":"MANGTIMBER",
			"Man IndustriesLtd.":"MANINDS",
			"Man Infraconstruction Ltd.":"MANINFRA",
			"Manjeera Constructions Ltd":"MANJEERA",
			"Manjushree Technopack Ltd":"MANJUSHREE",
			"Manpasand Beverages Ltd":"MANPASAND",
			"Manugraph India Ltd.":"MANUGRAPH",
			"Mirae Asset Investment ManagersPvt Ltd":"MANXT50",
			"Maral Overseas Ltd.":"MARALOVER",
			"Marathon Nextgen Realty Ltd.":"MARATHON",
			"Marg Ltd.":"MARG",
			"Marico Ltd.":"MARICO",
			"Marksans Pharma Ltd .":"MARKSANS",
			"Maruti Suzuki India Ltd.":"MARUTI",
			"MAS Financial Services Limited":"MASFIN",
			"Mask Investments Ltd":"MASKINVEST",
			"Mastek Ltd.":"MASTEK",
			"Matrimony.com Ltd.":"MATRIMONY",
			"Matrix Laboratories Ltd.":"MATRIXLABS",
			"Mawana Sugars Ltd.":"MAWANA",
			"Mawana Sugars Ltd":"MAWANASUG",
			"Max India Ltd":"MAXINDIA",
			"Max Ventures & Industries Ltd.":"MAXVIL",
			"Mayur Uniquoters Ltd.":"MAYURUNIQ",
			"Mazda Ltd.":"MAZDA",
			"Madhya Bharat Agro Products Ltd.":"MBAPL",
			"McNally Bharat Engineering Co. Ltd.":"MBECL",
			"MBL Infrastructures Limited":"MBLINFRA",
			"McDowell Holdings Ltd":"MCDHOLDING",
			"McLeod Russel India Ltd":"MCLEODRUSS",
			"Multi Commodity Exchange of India Ltd":"MCX",
			"Megasoft Ltd.":"MEGASOFT",
			"Meghmani Organics Limited":"MEGH",
			"Melstar Information Technologies Ltd.":"MELSTAR",
			"Menon Bearings Ltd.":"MENONBE",
			"MEP Infrastructure Developers Ltd.":"MEP",
			"Mercator Ltd":"MERCATOR",
			"Metalyst Forgings Ltd.":"METALFORGE",
			"Metkore Alloys & Industries Ltd":"METKORE",
			"Metropolis Healthcare Ltd.":"METROPOLIS",
			"Mahanagar Gas Ltd.":"MGL",
			"Motilal Oswal Asset Management Company Limited":"MGOLD",
			"Mahindra Holidays & Resorts India Limited":"MHRIL",
			"MIC Electronics Ltd.":"MIC",
			"Micro Inks Ltd.":"MICRO",
			"Micro TechnologiesLtd.":"MICROTECH",
			"Mishra Dhatu Nigam Ltd.":"MIDHANI",
			" ":"MIMINDAIND",
			"Minda Corporation Ltd":"MINDACORP",
			"Minda Industries Ltd.":"MINDAIND",
			"MindteckLtd.":"MINDTECK",
			"MindTree Ltd":"MINDTREE",
			"Mirc Electronics Ltd.":"MIRCELECTR",
			"Mirza International Ltd.":"MIRZAINT",
			"Mittal Life Style Ltd.":"MITTAL",
			"Mahindra & Mahindra Ltd.":"M_M",
			"Mahindra & Mahindra Financial Services Ltd.":"M_MFIN",
			"M M Forgings Ltd.":"MMFL",
			"MMP Industries Ltd.":"MMP",
			"MMTC Ltd.":"MMTC",
			"Media Matrix Worldwide Ltd.":"MMWL",
			"Modi Rubber Ltd.":"MODIRUBBER",
			"Mohit Industries Ltd.":"MOHITIND",
			"Mohota Industries Ltd.":"MOHOTAIND",
			"MOIL Ltd":"MOIL",
			"Mold-Tek Technologies Ltd.":"MOLDTECH",
			"Moldtek Packaging Ltd":"MOLDTKPAC",
			"Monsanto India Ltd.":"MONSANTO",
			"Monte Carlo Fashions Ltd.":"MONTECARLO",
			"Morarjee Textiles Ltd.":"MORARJEE",
			"Morepen Laboratories Ltd.":"MOREPENLAB",
			"MORGAN STANLEY":"MORGANSTAN",
			"Moser Baer India Ltd.":"MOSERBAER",
			"Motherson Sumi Systems Ltd.":"MOTHERSUMI",
			"Motilal Oswal Financial Services Ltd.":"MOTILALOFS",
			"Motor & General Finance Ltd.":"MOTOGENFIN",
			"Mphasis Ltd":"MPHASIS",
			"MPS Ltd":"MPSLTD",
			"MRF Ltd.":"MRF",
			"MRO-TEK Realty Ltd.":"MRO_TEK",
			"Mangalore Refinery & Petrochemicals Ltd.":"MRPL",
			"MSP Steel & Power Ltd.":"MSPL",
			"MSTC Ltd.":"MSTCLTD",
			"MT Educare Ltd":"MTEDUCARE",
			"Mahanagar Telephone Nigam Ltd.":"MTNL",
			"Mukand Engineers Ltd.":"MUKANDENGG",
			"Mukand Ltd.":"MUKANDLTD",
			"Mukta Arts Ltd.":"MUKTAARTS",
			"Munjal Auto Industries Ltd.":"MUNJALAU",
			"Munjal Showa Ltd.":"MUNJALSHOW",
			"Murli Industries Ltd.":"MURLIIND",
			"Murudeshwar Ceramics Ltd.":"MURUDCERA",
			"Muthoot Capital Services Ltd.":"MUTHOOTCAP",
			"Muthoot Finance Ltd.":"MUTHOOTFIN",
			"MVL Ltd":"MVL",
			"State Bank of Mysore":"MYSOREBANK",
			"NACL Industries Ltd.":"NACLIND",
			"Nagarjuna Fertilizers & Chemicals Ltd.":"NAGAFERT",
			"Nagarjuna Fertilizers & Chemicals Ltd.":"NAGARFERT",
			"Nagarjuna Oil Refinery Ltd":"NAGAROIL",
			"Nagreeka Capital & Infrastructure Ltd.":"NAGREEKCAP",
			"Nagreeka Exports Ltd.":"NAGREEKEXP",
			"Nahar Capital & Financial Services Ltd.":"NAHARCAP",
			"Nahar Industrial Enterprises Ltd.":"NAHARINDUS",
			"Nahar Poly Films Ltd":"NAHARPOLY",
			"Nahar Spinning Mills Ltd.":"NAHARSPG",
			"Nahar Spinning Mills Ltd.":"NAHARSPING",
			"India Infoline Finance Ltd":"NAIIFLFIN",
			"Nakoda Ltd.":"NAKODA",
			"Nippon Life India Asset Management Ltd.":"NAM_INDIA",
			"Muthoot Finance Ltd.":"NAMUTHOOTFIN",
			"Rural Electrification Corporation Ltd":"NARECLTD",
			"Narmada Chematur Petrochemicals Ltd.":"NARMDCHEMA",
			"Shriram City Union Finance Ltd.":"NASHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NASRTRANSFIN",
			"NATCO Pharma Ltd.":"NATCOPHARM",
			"Nath Bio-GensLtd.":"NATHBIOGEN",
			"National Aluminium Co. Ltd.":"NATIONALUM",
			"National Steel and Agro Industries Ltd.":"NATNLSTEEL",
			"Info EdgeLtd.":"NAUKRI",
			"Navin Fluorine International Ltd.":"NAVINFLUOR",
			"Navkar Corporation Ltd.":"NAVKARCORP",
			"Navneet Education Ltd":"NAVNETEDUL",
			"NBCCLtd.":"NBCC",
			"N.B.I. Industrial Finance Co. Ltd":"NBIFIN",
			"India Infoline Finance Ltd":"NBIIFLFIN",
			"Muthoot Finance Ltd.":"NBMUTHOOTFIN",
			"Shriram City Union Finance Ltd.":"NBSHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NBSRTRANSFIN",
			"Nava Bharat Ventures Ltd.":"NBVENTURES",
			"NCC Ltd":"NCC",
			"NCL Industries Ltd.":"NCLIND",
			"Nissan Copper Ltd.":"NCOPPER",
			"Shriram City Union Finance Ltd.":"NCSHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NCSRTRANSFIN",
			"Naga Dhunseri Group Ltd.":"NDGL",
			"Nandan Denim Ltd":"NDL",
			"Shriram City Union Finance Ltd.":"NDSHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NDSRTRANSFIN",
			"New Delhi Television Ltd.":"NDTV",
			"North Eastern Carrying Corporation Ltd":"NECCLTD",
			"Nectar Lifesciences Ltd.":"NECLIFE",
			"Neha International Ltd.":"NEHAINT",
			"Nelcast Ltd.":"NELCAST",
			"NELCO Ltd.":"NELCO",
			"Neo Corp International Ltd":"NEOCORP",
			"Neogen Chemicals Ltd.":"NEOGEN",
			"NEPC India Ltd.":"NEPCMICON",
			"NESCO Ltd.":"NESCO",
			"Shriram City Union Finance Ltd.":"NESHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NESRTRANSFIN",
			"Nestle India Ltd.":"NESTLEIND",
			"Network 18 Media & Investments Ltd.":"NETWORK18",
			"Neuland Laboratories Ltd.":"NEULANDLAB",
			"Newgen Software Technologies Ltd.":"NEWGEN",
			"Next Mediaworks Ltd":"NEXTMEDIA",
			"National Fertilizers Ltd.":"NFL",
			"Shriram City Union Finance Ltd.":"NFSHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NFSRTRANSFIN",
			"Shriram City Union Finance Ltd.":"NGSHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NGSRTRANSFIN",
			"Narayana Hrudayalaya Ltd":"NH",
			"NHPC Limited":"NHPC",
			"Shriram City Union Finance Ltd.":"NHSHRIRAMCIT",
			"Shriram Transport Finance Co. Ltd.":"NHSRTRANSFIN",
			"New India Assurance Co. Ltd":"NIACL",
			"NRB Industrial Bearings Ltd":"NIBL",
			"NICCO Corporation Ltd.":"NICCO",
			"Nippon Life India Asset Management Ltd.":"NIFTYBEES",
			"Edelweiss Asset Management Ltd.":"NIFTYEES",
			"NIIT Ltd.":"NIITLTD",
			"NIIT Technologies Ltd.":"NIITTECH",
			"Nila Infrastructures Ltd.":"NILAINFRA",
			"Nila Spaces Ltd.":"NILASPACES",
			"Nilkamal Ltd.":"NILKAMAL",
			"Indo-National Ltd":"NIPPOBATRY",
			"Nirma Ltd.":"NIRMA",
			"Shriram Transport Finance Co. Ltd.":"NISRTRANSFIN",
			"Nitco Ltd":"NITCO",
			"NEL Holdings Ltd.":"NITESHEST",
			"Nitin Fire Protection Industries Ltd.":"NITINFIRE",
			"Nitin Spinners Ltd.":"NITINSPIN",
			"We Internet Ltd.":"NIVINFRA",
			"Shriram Transport Finance Co. Ltd.":"NJSRTRANSFIN",
			"N.K. Industries Ltd.":"NKIND",
			"NLC India Ltd":"NLCINDIA",
			"Shriram Transport Finance Co. Ltd.":"NLSRTRANSFIN",
			"NMDC Ltd.":"NMDC",
			"Shriram Transport Finance Co. Ltd.":"NMSRTRANSFIN",
			"Shriram Transport Finance Co. Ltd.":"NNSRTRANSFIN",
			"NOCIL Ltd.":"NOCIL",
			"Noesis Industries Ltd.":"NOESISIND",
			"Noida Toll Bridge Co. Ltd.":"NOIDATOLL",
			"National Oxygen Ltd.":"NOL",
			"Norben Tea & Exports Ltd.":"NORBTEAEXP",
			"Shriram Transport Finance Co. Ltd.":"NOSRTRANSFIN",
			"Novopan Industries Ltd":"NOVOPANIND",
			"Tata Asset Management Limited":"NPBET",
			"Shriram Transport Finance Co. Ltd.":"NPSRTRANSFIN",
			"Shriram Transport Finance Co. Ltd.":"NQSRTRANSFIN",
			"N.R. Agarwal Industries Ltd.":"NRAIL",
			"NRB Bearings Ltd.":"NRBBEARING",
			"NRC Ltd.":"NRC",
			"Shriram Transport Finance Co. Ltd.":"NRSRTRANSFIN",
			"Nalwa Sons Investments Ltd.":"NSIL",
			"Shriram Transport Finance Co. Ltd.":"NSSRTRANSFIN",
			"Neueon Towers Ltd.":"NTL",
			"NTPC Ltd.":"NTPC",
			"Shriram Transport Finance Co. Ltd.":"NTSRTRANSFIN",
			"Nuchem Ltd.":"NUCHEM",
			"Nucleus Software Exports Ltd.":"NUCLEUS",
			"Shriram Transport Finance Co. Ltd.":"NUSRTRANSFIN",
			"Nu Tek India Ltd":"NUTEK",
			"Shriram Transport Finance Co. Ltd.":"NVSRTRANSFIN",
			"Shriram Transport Finance Co. Ltd.":"NWSRTRANSFIN",
			"Shriram Transport Finance Co. Ltd.":"NXSRTRANSFIN",
			"NXTDigital Ltd.":"NXTDIGITAL",
			"Shriram Transport Finance Co. Ltd.":"NYSRTRANSFIN",
			"Shriram Transport Finance Co. Ltd.":"NZSRTRANSFIN",
			"Oriental Aromatics Ltd.":"OAL",
			"Oberoi Realty Limited":"OBEROIRLTY",
			"Oriental Carbon & Chemicals Ltd.":"OCCL",
			"OCL India Ltd.":"OCL",
			"Octav Investments Ltd":"OCTAV",
			"FCI OEN Connectors Ltd.":"OENCONNECT",
			"Oracle Financial Services Software Ltd":"OFSS",
			"Oil India Ltd":"OIL",
			"Oil Country Tubular Ltd.":"OILCOUNTUB",
			"OCL Iron & Steel Ltd":"OISL",
			"Olectra Greentech Ltd.":"OLECTRA",
			"Omax Autos Ltd.":"OMAXAUTO",
			"Omaxe Ltd.":"OMAXE",
			"Omkar Speciality Chemicals Ltd":"OMKARCHEM",
			"OM Metals Infraprojects Ltd.":"OMMETALS",
			"Omnitech Infosolutions Ltd.":"OMNITECH",
			"OneLife Capital Advisors Ltd":"ONELIFECAP",
			"One Point One Solutions Ltd.":"ONEPOINT",
			"Oil & Natural Gas Corporation Ltd.":"ONGC",
			"OnMobile Global Ltd":"ONMOBILE",
			"Onward Technologies Ltd.":"ONWARDTEC",
			"Optiemus Infracom Ltd":"OPTIEMUS",
			"Opto CircuitsLtd.":"OPTOCIRCUI",
			"Orbit Corporation Ltd.":"ORBITCORP",
			"Orbit Exports Ltd.":"ORBTEXP",
			"Orchid Pharma Ltd":"ORCHIDPHAR",
			"ORG Informatics Ltd.":"ORGINFO",
			"Oricon Enterprises Ltd.":"ORICONENT",
			"Orient Abrasives Ltd.":"ORIENTABRA",
			"Oriental Trimex Ltd.":"ORIENTALTL",
			"Oriental Bank of Commerce":"ORIENTBANK",
			"Orient Bell Ltd":"ORIENTBELL",
			"Orient Cement Ltd":"ORIENTCEM",
			"Orient Electric Ltd.":"ORIENTELEC",
			"Oriental Hotels Ltd.":"ORIENTHOT",
			"Orient Information Technology Ltd.":"ORIENTINFO",
			"Orient Press Ltd.":"ORIENTLTD",
			"Orient Paper & Industries Ltd.":"ORIENTPPR",
			"Orient Refractories Ltd":"ORIENTREF",
			"Orissa Minerals Development Co Ltd":"ORISSAMINE",
			"Ortel Communications Ltd.":"ORTEL",
			"Ortin Laboratories Ltd.":"ORTINLABSS",
			"Oswal Agro Mills Ltd.":"OSWALAGRO",
			"Oswal Minerals Ltd":"OSWALMIN",
			"Oudh Sugar Mills Ltd.":"OUDHSUG",
			"PAE Ltd.":"PAEL",
			"Page Industries Ltd.":"PAGEIND",
			"Paisalo Digital Ltd.":"PAISALO",
			"Palash Securities Ltd.":"PALASHSECU",
			"Palred Technologies Ltd.":"PALREDTEC",
			"Panacea Biotec Ltd.":"PANACEABIO",
			"Panache Digilife Ltd":"PANACHE",
			"Panama Petrochem Ltd.":"PANAMAPET",
			"Panasonic Appliances India Co. Ltd":"PANASONIC",
			"Panasonic Carbon India Co. Ltd.":"PANCARBON",
			"Panchsheel Organics Ltd.":"PANCHSHEEL",
			"Panoramic Universal Ltd":"PANORAMUNI",
			"Huhtamaki PPL Ltd.":"PAPERPROD",
			"Parabolic Drugs Ltd":"PARABDRUGS",
			"Paramount Communications Ltd":"PARACABLES",
			"Parag Milk Foods Ltd":"PARAGMILK",
			"Parekh Aluminex Ltd.":"PARAL",
			"Paramount Printpackaging Ltd":"PARAPRINT",
			"Paras Petrofils Ltd.":"PARASPETRO",
			"Parekh Platinum Ltd.":"PAREKHPLAT",
			"Parry Sugar Industries Ltd":"PARRYSUGAR",
			"Parsvnath Developers Ltd.":"PARSVNATH",
			"Pasupati Fabrics Ltd.":"PASUPATI",
			"Patel Engineering Ltd.":"PATELENG",
			"Patel Integrated Logistics Ltd.":"PATINTLOG",
			"Patni Computer Systems":"PATNI",
			"Patspin India Ltd.":"PATSPINLTD",
			"Panasonic AVC Networks India Co. Ltd.":"PAVCI",
			"PBA Infrastructure Ltd.":"PBAINFRA",
			"PC Jeweller Ltd":"PCJEWELLER",
			"Pudumjee Paper Products Ltd.":"PDMJEPAPER",
			"Parenteral DrugsLtd.":"PDPL",
			"PDS Multinational Fashions Ltd":"PDSMFL",
			"Pearl Global Ltd.":"PEARLGLOBL",
			"Pearl Polymers Ltd.":"PEARLPOLY",
			"Piramal Enterprises Ltd":"PEL",
			"Pennar Industries Ltd.":"PENIND",
			"Peninsula Land Ltd.":"PENINLAND",
			"Pennar Engineered Building Systems Ltd.":"PENPEBS",
			"Pearl Engineering Polymers Ltd.":"PEPL",
			"Persistent Systems Ltd.":"PERSISTENT",
			"Petron Engineering Construction Ltd.":"PETRONENGG",
			"Petronet LNG Ltd.":"PETRONET",
			"Power Finance Corporation Ltd.":"PFC",
			"Pfizer Ltd.":"PFIZER",
			"Prime Focus Ltd.":"PFOCUS",
			"PTC India Financial Services Ltd.":"PFS",
			"PG Electroplast Ltd":"PGEL",
			"Procter & Gamble Hygiene & Health Care Ltd.":"PGHH",
			"Procter & Gamble Health Ltd.":"PGHL",
			"Pearl Global Industries Ltd":"PGIL",
			"Kore Foods Ltd.":"PHILCORP",
			"Phillips Carbon Black Ltd.":"PHILIPCARB",
			"Phoenix Lamps Ltd":"PHOENIXLL",
			"Phoenix Mills Ltd.":"PHOENIXLTD",
			"Pidilite Industries Ltd.":"PIDILITIND",
			"PI Industries Ltd.":"PIIND",
			"Pilani Investment & Industries Corporation Ltd":"PILANIINVS",
			"PIL Italica Lifestyle Ltd.":"PILITA",
			"Pincon Spirit Ltd":"PINCON",
			"Pioneer Distilleries Ltd.":"PIONDIST",
			"Pioneer Embroideries Ltd.":"PIONEEREMB",
			"Piramal Glass Ltd":"PIRGLASS",
			"Piramal Phytocare Ltd":"PIRPHYTO",
			"Pitti Engineering Ltd.":"PITTIENG",
			"Peria Karamalai Tea & Produce Co Ltd":"PKTEA",
			"Plastiblends India Ltd.":"PLASTIBLEN",
			"Plethico Pharmaceuticals Ltd.":"PLETHICO",
			"Punjab National Bank":"PNB",
			"PNB Gilts Ltd.":"PNBGILTS",
			"PNB Housing Finance Ltd.":"PNBHOUSING",
			"Pritish Nandy Communications Ltd.":"PNC",
			"PNC Infratech Ltd.":"PNCINFRA",
			"Pneumatic Holdings Ltd.":"PNEUMATIC",
			"Pochiraju Industries Ltd.":"POCHIRAJU",
			"Poddar Housing & Development Ltd.":"PODDARHOUS",
			"Poddar Pigments Ltd.":"PODDARMENT",
			"Pokarna Ltd.":"POKARNA",
			"Polar Industries Ltd.":"POLARIND",
			"Polaris Consulting & Services Ltd":"POLARIS",
			"Polycab India Ltd.":"POLYCAB",
			"Poly Medicure Ltd.":"POLYMED",
			"Polyplex Corporation Ltd.":"POLYPLEX",
			"Pondy Oxides & Chemicals Ltd.":"PONDYOXIDE",
			"Ponni SugarsLtd.":"PONNIERODE",
			"Power Grid Corporation of India Ltd.":"POWERGRID",
			"ABB Power Products & Systems India Ltd.":"POWERINDIA",
			"Power Mech Projects Ltd.":"POWERMECH",
			"PPAP Automotive Ltd.":"PPAP",
			"Prakash Pipes Ltd.":"PPL",
			"Prabhat Dairy Ltd.":"PRABHAT",
			"Pradip Overseas Ltd.":"PRADIP",
			"Prajay Engineers Syndicate Ltd.":"PRAENG",
			"Praj Industries Ltd.":"PRAJIND",
			"Prakash Industries Ltd.":"PRAKASH",
			"Prakash Steelage Ltd":"PRAKASHSTL",
			"Pratibha Industries Ltd.":"PRATIBHA",
			"Praxis Home Retail Ltd.":"PRAXIS",
			"Precision Camshafts Ltd.":"PRECAM",
			"Precot Meridian Ltd.":"PRECOT",
			"Precision Wires India Ltd.":"PRECWIRE",
			"Premier Explosives Ltd.":"PREMEXPLN",
			"Premier Ltd.":"PREMIER",
			"Premier Polyfilm Ltd.":"PREMIERPOL",
			"Pressman Advertising Ltd":"PRESSMN",
			"Prestige Estates Projects Limited":"PRESTIGE",
			"Pricol Ltd":"PRICOL",
			"Pricol Ltd.":"PRICOLLTD",
			"Prime Securities Ltd.":"PRIMESECU",
			"Prince Pipes & Fittings Ltd.":"PRINCEPIPE",
			"Prithvi Information Solutions Ltd.":"PRITHVI",
			"Prithvi Softech Ltd.":"PRITHVISOF",
			"Proseed India Ltd.":"PROSEED",
			"ProvogueLtd.":"PROVOGE",
			"Prozone Intu Properties Ltd":"PROZONINTU",
			"Prism Johnson Ltd.":"PRSMJOHNSN",
			"Punjab & Sind Bank":"PSB",
			"PSL Ltd.":"PSL",
			"PSP Projects Ltd":"PSPPROJECT",
			"Pyramid Saimira Theatre Ltd.":"PSTL",
			"Nippon Life India Asset Management Ltd.":"PSUBNKBEES",
			"PTC India Ltd.":"PTC",
			"PTL Enterprises Ltd.":"PTL",
			"Punjab Chemicals & Crop Protection Ltd.":"PUNJABCHEM",
			"Punjab Tractors Ltd.":"PUNJABTRAC",
			"Punj Lloyd Ltd.":"PUNJLLOYD",
			"Puravankara Ltd.":"PURVA",
			"PVP Ventures Ltd":"PVP",
			"PVR Ltd.":"PVR",
			"Quantum Asset Management Co Pvt Ltd":"QGOLDHALF",
			"Quantum Asset Management Co Pvt Ltd":"QNIFTY",
			"Quess Corp Ltd":"QUESS",
			"Quick Heal Technologies Ltd":"QUICKHEAL",
			"Quintegra Solutions Ltd.":"QUINTEGRA",
			"Radaan Mediaworks India Ltd.":"RADAAN",
			"Radico Khaitan Ltd":"RADICO",
			"Music Broadcast Ltd":"RADIOCITY",
			"Rain Industries Ltd":"RAIN",
			"Rainbow Papers Ltd.":"RAINBOWPAP",
			"Rain Calcining Ltd.":"RAINCALCIN",
			"Rajesh Exports Ltd.":"RAJESHEXPO",
			"Raj Oil Mills Ltd":"RAJOIL",
			"Rajapalayam Mills Ltd.":"RAJPALAYAM",
			"Raj Rayon Industries Ltd.":"RAJRAYON",
			"Rajshree Sugars & Chemicals Ltd.":"RAJSREESUG",
			"Raj Television Network Ltd.":"RAJTV",
			"Rajvir Industries Ltd.":"RAJVIR",
			"Rallis India Ltd.":"RALLIS",
			"Shree Rama Newsprint Ltd":"RAMANEWS",
			"Rama Steel Tubes Ltd":"RAMASTEEL",
			"Ramco Cements Ltd":"RAMCOCEM",
			"Ramco Industries Ltd.":"RAMCOIND",
			"Ramco Systems Ltd.":"RAMCOSYS",
			"Ramgopal Polytex Ltd.":"RAMGOPOLY",
			"Ramky Infrastructure Ltd":"RAMKY",
			"Ramsarup Industries Ltd.":"RAMSARUP",
			"Rana Sugars Ltd.":"RANASUG",
			"Ranbaxy Laboratories Ltd.":"RANBAXY",
			"Rane Brake Linings Ltd.":"RANEBRAKE",
			"Rane Engine Valve Ltd":"RANEENGINE",
			"Rane Holdings Ltd.":"RANEHOLDIN",
			"Ranklin Solutions Ltd":"RANKLIN",
			"Rasoya Proteins Ltd.":"RASOYPR",
			"Ratnamani Metals & Tubes Ltd.":"RATNAMANI",
			"Raymond Ltd.":"RAYMOND",
			"Rane Brake Lining Ltd":"RBL",
			"RBL Bank Ltd":"RBLBANK",
			"Reliance Broadcast Network Ltd":"RBN",
			"Rashtriya Chemicals & Fertilizers Ltd.":"RCF",
			"Reliance Communications Ltd.":"RCOM",
			"REC Ltd.":"RECLTD",
			"RedingtonLtd.":"REDINGTON",
			"Refex Industries Ltd.":"REFEX",
			"Regency Ceramics Ltd.":"REGENCERAM",
			"REI Agro Ltd.":"REIAGROLTD",
			"REI Six Ten Retail Ltd":"REISIXTEN",
			"Relaxo Footwears Ltd.":"RELAXO",
			"Reliance Nippon Life Asset Management Ltd.":"RELBANK",
			"Reliance Capital Ltd.":"RELCAPITAL",
			"Reliance Nippon Life Asset Management Ltd.":"RELGOLD",
			"Reliance Industries Ltd.":"RELIANCE",
			"Religare Enterprises Ltd.":"RELIGARE",
			"Reliance Infrastructure Ltd":"RELINFRA",
			"Reliance MediaWorks Ltd":"RELMEDIA",
			"Reliance Nippon Life Asset Management Ltd.":"RELNIFTY",
			"Remsons Industries Ltd.":"REMSONSIND",
			"Shree Renuka Sugars Ltd.":"RENUKA",
			"Repco Home Finance Ltd":"REPCOHOME",
			"Repro India Ltd.":"REPRO",
			" ":"RERDAVIIPADG",
			"Responsive Industries Ltd":"RESPONIND",
			"Revathi Equipment Ltd.":"REVATHI",
			"Rane Engine Valves Ltd.":"REVL",
			"Renaissance Global Ltd.":"RGL",
			"Reliance Home Finance Limited":"RHFL",
			"Rico Auto Industries Ltd.":"RICOAUTO",
			"Reliance Industrial Infrastructure Ltd.":"RIIL",
			"RITES Ltd.":"RITES",
			"Ravi Kumar Distilleries Limited":"RKDL",
			"Ramkrishna Forgings Ltd.":"RKFORGE",
			"Radha Madhav Corporation Ltd.":"RMCL",
			"RaneLtd":"RML",
			"Resurgere Mines & Minerals India Ltd":"RMMIL",
			"Reliance Naval & Engineering Ltd.":"RNAVAL",
			"Reliance Natural Resources Ltd.":"RNRL",
			"Rohit Ferro-Tech Ltd.":"ROHITFERRO",
			"Royal Orchid Hotels Ltd.":"ROHLTD",
			"Rollatainers Ltd":"ROLLT",
			"Rolta India Ltd.":"ROLTA",
			"Rossell India Ltd":"ROSSELLIND",
			"RPG Cables Ltd.":"RPGCABLES",
			"RPG Life Sciences Ltd":"RPGLIFE",
			"RPG Transmission Ltd.":"RPGTLTD",
			"Reliance Petroleum Ltd.":"RPL",
			"Reliance Power Ltd":"RPOWER",
			"R.P.P. Infra Projects Limited":"RPPINFRA",
			"Embassy Office Parks REIT":"RREMBASSY",
			"R.S SoftwareLtd.":"RSSOFTWARE",
			"RSWM Ltd.":"RSWM",
			"R Systems International Ltd.":"RSYSTEMS",
			"RattanIndia Infrastructure Ltd.":"RTNINFRA",
			"RattanIndia Power Ltd.":"RTNPOWER",
			"Ruby Mills Ltd.":"RUBYMILLS",
			"Ruchi Soya Industries Ltd.":"RUCHI",
			"Ruchi Infrastructure Ltd.":"RUCHINFRA",
			"Ruchira Papers Ltd.":"RUCHIRA",
			"Rupa & Company Ltd":"RUPA",
			"Rushil Decor Ltd":"RUSHIL",
			"Rail Vikas Nigam Ltd.":"RVNL",
			"Sabero Organics Gujarat Ltd.":"SABERORGAN",
			"SAB Events & Governance Now Media Ltd":"SABEVENTS",
			"Sri Adhikari Brothers Television Network Ltd.":"SABTN",
			"Sadbhav Engineering Ltd.":"SADBHAV",
			"Sadbhav Infrastructure Project Limited":"SADBHIN",
			"Safari IndustriesLtd.":"SAFARI",
			"Sagardeep Alloys Ltd":"SAGARDEEP",
			"Sagar Cements Ltd.":"SAGCEM",
			"Steel Authority of India Ltd.":"SAIL",
			"Sakar Healthcare Ltd.":"SAKAR",
			"Sakthi Sugars Ltd.":"SAKHTISUG",
			"Saksoft Ltd.":"SAKSOFT",
			"Sakthi Finance Ltd.":"SAKTHIFIN",
			"Sakuma Exports Ltd.":"SAKUMA",
			"Salasar Techno Engineering Ltd.":"SALASAR",
			"Salona Cotspin Ltd.":"SALONA",
			"Salora International Ltd.":"SALORAINTL",
			"SAL Steel Ltd":"SALSTEEL",
			"Salzer Electronics Ltd.":"SALZERELEC",
			"Sambandam Spinning Mills Ltd.":"SAMBANDAM",
			"Sambhaav Media Ltd.":"SAMBHAAV",
			"Sam Industries Ltd.":"SAMINDUS",
			"Samrudhhi Cement Ltd":"SAMRUDDHI",
			"Samtel Color Ltd.":"SAMTEL",
			"Sanco Industries Ltd":"SANCO",
			"Sandesh Ltd.":"SANDESH",
			"Sandhar Technologies Ltd":"SANDHAR",
			"SangamLtd.":"SANGAMIND",
			"Sanghi Industries Ltd.":"SANGHIIND",
			"Sanghi Polysters Ltd.":"SANGHIPOLY",
			"Sanghvi Forging and Engineering Ltd":"SANGHVIFOR",
			"Sanghvi Movers Ltd.":"SANGHVIMOV",
			"Sanginita Chemicals Ltd":"SANGINITA",
			"Sanofi India Ltd":"SANOFI",
			"Sanwaria Consumer Ltd.":"SANWARIA",
			"South Asian Petrochem Ltd":"SAPL",
			"Sarda Energy & Minerals Ltd.":"SARDAEN",
			"Saregama India Ltd.":"SAREGAMA",
			"Sarla Performance Fibers Ltd.":"SARLAPOLY",
			"Sarthak Industries Ltd.":"SARTHAKIND",
			"Sasken Technologies Ltd.":"SASKEN",
			"Sastasundar Ventures Ltd.":"SASTASUNDR",
			"Sathavahana Ispat Ltd.":"SATHAISPAT",
			"Satia Industries Ltd.":"SATIA",
			"Satin Creditcare Network Ltd":"SATIN",
			"Satyam Computer Services Ltd.":"SATYAMCOMP",
			"Savera Industries Ltd.":"SAVERA",
			"Sayaji Hotels Ltd.":"SAYAJIHOTL",
			"State Bank of Bikaner & Jaipur Ltd.":"SBBJ",
			"SBI Cards & Payment Services Limited":"SBICARD",
			"SBI Funds Management Private Limited":"SBIETFQLTY",
			"SBI Life Insurance Co. Ltd.":"SBILIFE",
			"State Bank of India":"SBIN",
			"State Bank of Travancore":"SBT",
			"S.B.& T. International Ltd.":"SB_TINTL",
			"Stampede Capital Ltd":"SCAPDVR",
			"Schaeffler India Ltd.":"SCHAEFFLER",
			"S Chand & Co. Ltd":"SCHAND",
			"Schneider Electric Infrastructure Ltd":"SCHNEIDER",
			"Shipping Corporation of India Ltd.":"SCI",
			"Som Distilleries & Breweries Ltd.":"SDBL",
			"Seamec Ltd.":"SEAMECLTD",
			"Selan Exploration Technology Ltd.":"SELAN",
			"SEL Manufacturing Co. Ltd.":"SELMCL",
			"S.E. Power Ltd":"SEPOWER",
			"Sequent Scientific Ltd":"SEQUENT",
			"Servalakshmi Paper Ltd":"SERVALL",
			"Seshasayee Paper & Boards Ltd.":"SESHAPAPER",
			"Setco Automotive Ltd.":"SETCO",
			"SBI Funds Management Private Limited":"SETF10GILT",
			"SBI Funds Management Private Limited":"SETFGOLD",
			"SBI Funds Management Private Limited":"SETFNIF50",
			"SBI Funds Management Private Limited":"SETFNIFBK",
			"SBI Funds Management Private Limited":"SETFNN50",
			"Setubandhan Infrastructure Ltd.":"SETUINFRA",
			"Seya Industries Ltd":"SEYAIND",
			"Sejal Glass Ltd":"SEZAL",
			"Star Ferro & Cement Ltd.":"SFCL",
			"Sheela Foam Ltd":"SFL",
			"Shree Ganesh Forgings Ltd.":"SGFL",
			"Shree Ganesh Jewellery HouseLtd.":"SGJHL",
			"STL Global Limited":"SGL",
			"Shah Alloys Ltd.":"SHAHALLOYS",
			"Shakti PumpsLtd.":"SHAKTIPUMP",
			"Shalby Ltd.":"SHALBY",
			"Shalimar Paints Ltd.":"SHALPAINTS",
			"Shankara Building Products Ltd":"SHANKARA",
			"Shanthi Gears Ltd.":"SHANTIGEAR",
			"Sharda Cropchem Ltd.":"SHARDACROP",
			"Sharda Motor Industries Ltd":"SHARDAMOTR",
			"Nippon Life India Asset Management Ltd.":"SHARIABEES",
			"Sharon Bio-Medicine Ltd.":"SHARONBIO",
			"Shasun Pharmaceuticals Ltd":"SHASUNPHAR",
			"Shemaroo Entertainment Ltd.":"SHEMAROO",
			"Somany Home Innovation Ltd.":"SHIL",
			"Shilpa Medicare Ltd.":"SHILPAMED",
			"Shilpi Cable Technologies Ltd":"SHILPI",
			"Shirpur Gold Refinery Ltd.":"SHIRPUR_G",
			"Shivam Autotech Ltd":"SHIVAMAUTO",
			"Shiva Mills Ltd.":"SHIVAMILLS",
			"Shiva Texyarn Ltd.":"SHIVATEX",
			"S H Kelkar & Co. Ltd.":"SHK",
			"Shri Lakshmi Cotsyn Ltd":"SHLAKSHMI",
			"Shoppers Stop Ltd":"SHOPERSTOP",
			"Shree Precoated Steels Ltd":"SHPRE",
			"Shree Digvijay Cement Co. Ltd.":"SHREDIGCEM",
			"Shree Ashtavinayak Cine Vision Ltd.":"SHREEASHTA",
			"Shree Cement Ltd.":"SHREECEM",
			"Shree Pushkar Chemicals & Fertilisers Ltd":"SHREEPUSHK",
			"Shree Rama Multi-Tech Ltd.":"SHREERAMA",
			"Shrenik Ltd":"SHRENIK",
			"Shrenuj & Co. Ltd.":"SHRENUJ",
			"Shreyans Industries Ltd.":"SHREYANIND",
			"Shreyas Shipping & Logistics Ltd.":"SHREYAS",
			"Shri Aster Silicates Ltd":"SHRIASTER",
			"Shriram Pistons & Rings Ltd":"SHRIPISTON",
			"Shriram City Union Finance Ltd.":"SHRIRAMCIT",
			"Shriram EPC Ltd":"SHRIRAMEPC",
			"Shyam Century Ferrous Ltd.":"SHYAMCENT",
			"Shyam Telecom Ltd.":"SHYAMTEL",
			"Sicagen India Ltd":"SICAGEN",
			"Sical Logistics Ltd":"SICAL",
			"Siemens Ltd.":"SIEMENS",
			"Signet Industries Ltd.":"SIGIND",
			"SI Group - India Ltd.":"SIGROUPIND",
			"Standard Industries Ltd.":"SIL",
			"SIL Investments Ltd.":"SILINV",
			"Simbhaoli Sugars Ltd.":"SIMBHALS",
			"Simbhaoli Sugars Ltd":"SIMBHSUGAR",
			"Simplex Projects Ltd.":"SIMPLEX",
			"Simplex Castings Ltd.":"SIMPLEXCAS",
			"Simplex Infrastructure Ltd":"SIMPLEXINF",
			"Sintex Industries Ltd.":"SINTEX",
			"Sirca Paints India Ltd.":"SIRCA",
			"Sirpur Paper Mills Ltd.":"SIRPAPER",
			"Security & Intelligence Services India Ltd":"SIS",
			"Sita Shree Food Products Ltd":"SITASHREE",
			"Siti Networks Ltd.":"SITINET",
			"Siyaram Silk Mills Ltd.":"SIYSIL",
			"SJVN Ltd.":"SJVN",
			"SKF India Ltd.":"SKFINDIA",
			"SKIL Infrastructure Ltd.":"SKIL",
			"Skipper Ltd":"SKIPPER",
			"SKM Egg Products ExportLtd.":"SKMEGGPROD",
			"S. Kumars Nationwide Ltd.":"SKUMARSYNF",
			"Aakash Exploration Services Ltd.":"SMAAKASH",
			"Aaron Industries Ltd.":"SMAARON",
			"Aarvi Encon Ltd.":"SMAARVI",
			"A B Infrabuild Ltd.":"SMABINFRA",
			"Accord Synergy Ltd":"SMACCORD",
			"Accuracy Shipping Ltd.":"SMACCURACY",
			"Ace Integrated Solutions Ltd.":"SMACEINTEG",
			"Ahimsa Industries Ltd.":"SMAHIMSA",
			"Ahlada Engineers Ltd.":"SMAHLADA",
			"Airo Lam Ltd.":"SMAIROLAM",
			"ANI Integrated Services Ltd.":"SMAISL",
			"Ajooni Biotech Ltd.":"SMAJOONI",
			"AKG Exim Ltd.":"SMAKG",
			"Ambani Organics Ltd.":"SMAMBANIORG",
			"A & M Jumbo Bags Ltd.":"SMAMJUMBO",
			"Artedz Fabs Ltd.":"SMARTEDZ",
			"Smartlink Holdings Ltd.":"SMARTLINK",
			"Art Nirman Ltd.":"SMARTNIRMAN",
			"Arvee LaboratoriesLtd.":"SMARVEE",
			"Ascom Leasing & Investments Ltd.":"SMASCOM",
			"ASL Industries Ltd.":"SMASLIND",
			"Aurangabad Distillery Ltd.":"SMAURDIS",
			"AVG Logistics Ltd.":"SMAVG",
			"Avro India Ltd.":"SMAVROIND",
			"AVSL Industries Ltd.":"SMAVSL",
			"Baba Agro Food Ltd.":"SMBABAFOOD",
			"Banka BioLoo Ltd.":"SMBANKA",
			"Bansal Multiflex Ltd.":"SMBANSAL",
			"B&B Triplewall Containers Ltd.":"SMBBTCL",
			"Brand Concepts Ltd.":"SMBCONCEPTS",
			"Beta Drugs Ltd.":"SMBETA",
			"Bohra Industries Ltd":"SMBOHRA",
			"Bright Solar Ltd.":"SMBRIGHT",
			"Bombay Super Hybrid Seeds Ltd.":"SMBSHSL",
			"CadsysLtd.":"SMCADSYS",
			"CKP Leisure Ltd.":"SMCKPLEISURE",
			"CKP Products Ltd":"SMCKPPRODUCT",
			"CMM Infraprojects Ltd":"SMCMMIPL",
			"Continental Seeds & Chemicals Ltd.":"SMCONTI",
			"Crown Lifters Ltd.":"SMCROWN",
			"Dangee Dums Ltd.":"SMDANGEE",
			"DC Infotech & Communication Ltd.":"SMDCI",
			"Dev Information Technology Ltd":"SMDEVIT",
			"D. P. Abhushan Ltd.":"SMDPABHUSHAN",
			"Dhanuka Realty Ltd":"SMDRL",
			"DRS Dilip Roadlines Ltd.":"SMDRSDILIP",
			"Debock Sales & Marketing Ltd.":"SMDSML",
			"E2E Networks Ltd.":"SME2E",
			"Euro India Fresh Foods Ltd":"SMEIFFL",
			"Emkay Taps & Cutting Tools Ltd.":"SMEMKAYTOOLS",
			"Felix Industries Ltd.":"SMFELIX",
			"Five Core Electronics Ltd.":"SMFIVECORE",
			"Focus Lighting & Fixtures Ltd.":"SMFOCUS",
			"Fourth Dimension Solutions Ltd.":"SMFOURTHDIM",
			"Ganga Forging Ltd.":"SMGANGAFORGE",
			"Globe International Carriers Ltd.":"SMGICL",
			"Giriraj Civil Developers Ltd.":"SMGIRIRAJ",
			"Global Education Ltd.":"SMGLOBAL",
			"Globe TextileLtd":"SMGLOBE",
			"Godha Cabcon & Insulation Ltd.":"SMGODHA",
			"Goldstar Power Ltd.":"SMGOLDSTAR",
			"Gretex Industries Ltd":"SMGRETEX",
			"HEC Infra Projects Ltd":"SMHECPROJECT",
			"HEC INFRA PROJECTS LTD.":"SMHECPROJECT_1",
			"Hindcon Chemicals Ltd.":"SMHINDCON",
			"Hindprakash Industries Ltd.":"SMHPIL",
			"Husys Consulting Ltd.":"SMHUSYSLTD",
			"Ice Make Refrigeration Ltd.":"SMICEMAKE",
			"Innovana Thinklabs Ltd.":"SMINNOVANA",
			"Innovative Tyres & Tubes Ltd.":"SMINNOVATIVE",
			"Iris Clothings Ltd.":"SMIRISDOREME",
			"Jakharia Fabric Ltd.":"SMJAKHARIA",
			"Jalan TransolutionsLtd":"SMJALAN",
			"Jet Freight Logistics Ltd.":"SMJETFREIGHT",
			"Jet Knitwears Ltd":"SMJETKNIT",
			"Kapston Facilities Management Ltd.":"SMKAPSTON",
			"Keerti Knowledge & Skills Ltd.":"SMKEERTI",
			"KHFM Hospitality & Facility Management Services Ltd.":"SMKHFM",
			"KKV Agro Powers Ltd.":"SMKKVAPOW",
			"Kritika Wires Ltd.":"SMKRITIKA",
			"Kshitij Polyline Ltd.":"SMKSHITIJPOL",
			"Lagnam Spintex Ltd.":"SMLAGNAM",
			"Latteys Industries Ltd.":"SMLATTEYS",
			"Laxmi Cotspin Ltd":"SMLAXMICOT",
			"Lexus GranitoLtd.":"SMLEXUS",
			"Laxmi Goldorna House Ltd.":"SMLGHL",
			"SML Isuzu Ltd":"SMLISUZU",
			"Macpower CNC Machines Ltd.":"SMMACPOWER",
			"Mahickra Chemicals Ltd.":"SMMAHICKRA",
			"Manav Infra Projects Ltd.":"SMMANAV",
			"Marine ElectricalsLtd.":"SMMARINE",
			"Marshall Machines Ltd.":"SMMARSHALL",
			"Madhav Copper Ltd.":"SMMCL",
			"Marvel Decor Ltd.":"SMMDL",
			"Mangalam Global Enterprise Ltd.":"SMMGEL",
			"Mohini Health & Hygiene Ltd.":"SMMHHL",
			"Milton Industries Ltd.":"SMMILTON",
			"Mindpool Technologies Ltd.":"SMMINDPOOL",
			"MITCON Consultancy & Engineering Services Ltd":"SMMITCON",
			"M K Proteins Ltd":"SMMKPL",
			"Moksh Ornaments Ltd.":"SMMOKSH",
			"Momai Apparels Ltd":"SMMOMAI",
			"Madhya Pradesh Today Media Ltd.":"SMMPTODAY",
			"Nandani Creation Ltd":"SMNANDANI",
			"Narmada Agrobase Ltd.":"SMNARMADA",
			"Nitiraj Engineers Ltd":"SMNITIRAJ",
			"Omfurn India Ltd.":"SMOMFURN",
			"Opal Luxury Time Products Ltd":"SMOPAL",
			"Osia Hyper Retail Ltd.":"SMOSIAHYPER",
			"ShreeOswal Seeds & Chemicals Ltd.":"SMOSWALSEEDS",
			"Pansari Developers Ltd":"SMPANSARI",
			"Par Drugs & Chemicals Ltd.":"SMPAR",
			"Parin Furniture Ltd.":"SMPARIN",
			"Pashupati Cotspin Ltd.":"SMPASHUPATI",
			"Penta Gold Ltd.":"SMPENTAGOLD",
			"Perfect Infraengineers Ltd.":"SMPERFECT",
			"Power & InstrumentationLtd.":"SMPIGL",
			"Splendid Metal Products Ltd.":"SMPL",
			"Powerful Technologies Ltd.":"SMPOWERFUL",
			"Priti International Ltd.":"SMPRITI",
			"Prolife Industries Ltd.":"SMPROLIFE",
			"Pulz Electronics Ltd.":"SMPULZ",
			"Pushpanjali Realms & Infratech Ltd.":"SMPUSHPREALM",
			"Rajnandini Metal Ltd.":"SMRAJMET",
			"Reliable Data Services Ltd.":"SMRELIABLE",
			"Rudrabhishek Enterprises Ltd.":"SMREPL",
			"RKEC Projects Ltd.":"SMRKEC",
			"R M Drip & Sprinklers Systems Ltd.":"SMRMDRIP",
			"Rajshree Polypack Ltd.":"SMRPPL",
			"Sarveshwar Foods Ltd.":"SMSARVESHWAR",
			"Salasar Exteriors & Contour Ltd.":"SMSECL",
			"SecUR Credentials Ltd":"SMSECURCRED",
			"Servotech Power Systems Ltd":"SMSERVOTECH",
			"Shaival Reality Ltd.":"SMSHAIVAL",
			"Shanti OverseasLtd.":"SMSHANTI",
			"Shiv Aum Steels Ltd.":"SMSHIVAUM",
			"Shradha Infraprojects Ltd.":"SMSHRADHA",
			"Shubhlaxmi Jewel Art Ltd.":"SMSHUBHLAXMI",
			"SupremeImpex Ltd.":"SMSIIL",
			"Sikko Industries Ltd":"SMSIKKO",
			"Silgo Retail Ltd.":"SMSILGO",
			"Silly Monks Entertainment Ltd.":"SMSILLYMONKS",
			"Silver Touch Technologies Ltd.":"SMSILVERTUC",
			"Sintercom India Ltd.":"SMSINTERCOM",
			"S K S Textiles Ltd.":"SMSKSTEXTILE",
			"SMS Lifesciences India Ltd.":"SMSLIFE",
			"SMVD Poly Pack Ltd.":"SMSMVD",
			"Softtech Engineers Ltd.":"SMSOFTTECH",
			"Solex Energy Ltd.":"SMSOLEX",
			"Sona Hi Sona JewellersLtd.":"SMSONAHISONA",
			"Sonam Clock Ltd.":"SMSONAMCLOCK",
			"Soni Soya Products Ltd.":"SMSONISOYA",
			"Spectrum Electrical Industries Ltd.":"SMSPECTRUM",
			"SMS Pharmaceuticals Ltd.":"SMSPHARMA",
			"Shri Ram Switchgeras Ltd":"SMSRIRAM",
			"Shree Ram Proteins Ltd.":"SMSRPL",
			"S.S. Infrastructure Development Consultants Ltd.":"SMSSINFRA",
			"Supreme Engineering Ltd.":"SMSUPREMEENG",
			"Surani Steel Tubes Ltd.":"SMSURANI",
			"Surevin BPO Services Ltd":"SMSUREVIN",
			"Suumaya Lifestyle Ltd.":"SMSUULD",
			"Shree Vasu Logistics Ltd.":"SMSVLL",
			"Tara Chand Logistic Solutions Ltd.":"SMTARACHAND",
			"Tembo Global Industries Ltd.":"SMTEMBO",
			"Thejo Engineering Ltd":"SMTHEJO",
			"Shree Tirupati Balajee FIBC Ltd.":"SMTIRUPATI",
			"Tirupati Forge Ltd.":"SMTIRUPATIFL",
			"Total Transport Systems Ltd":"SMTOTAL",
			"Transwind Infrastructures Ltd.":"SMTRANSWIND",
			"Ushanti Colour Chem Ltd.":"SMUCL",
			"Uniinfo Telecom Services Ltd.":"SMUNIINFO",
			"United Polyfab Gujarat Ltd":"SMUNITEDPOLY",
			"Univastu India Ltd.":"SMUNIVASTU",
			"Uravi T & Wedge Lamps Ltd.":"SMURAVI",
			"Ultra Wiring Connectivity Systems Ltd.":"SMUWCSL",
			"Vasa Retail & Overseas Ltd.":"SMVASA",
			"Vaxtex Cotfab Ltd.":"SMVCL",
			"Vera Synthetic Ltd.":"SMVERA",
			"Vertoz Advertising Ltd.":"SMVERTOZ",
			"Vinny Overseas Ltd.":"SMVINNY",
			"Vadivarhe Speciality Chemicals Ltd":"SMVSCL",
			"Wealth First Portfolio Managers Ltd.":"SMWEALTH",
			"Wonder Fibromats Ltd.":"SMWFL",
			"Worth Peripherals Ltd.":"SMWORTH",
			"Zodiac Energy Ltd.":"SMZODIAC",
			"SMZS Chemicals Ltd.":"SMZSCHEM",
			"Snowman Logistics Ltd.":"SNOWMAN",
			"Sobha Ltd.":"SOBHA",
			"STG Lifecare Ltd":"SOFTTECHGR",
			"Solara Active Pharma Sciences Ltd.":"SOLARA",
			"Solar Industries India Ltd":"SOLARINDS",
			"Solectron EMS India Ltd.":"SOLEMS",
			"Somany Ceramics Ltd.":"SOMANYCERA",
			"Soma Textiles & Industries Ltd.":"SOMATEX",
			"Somi Conveyor Beltings Ltd":"SOMICONVEY",
			"Sonata Software Ltd.":"SONATSOFTW",
			"SORIL Infra Resources Ltd.":"SORILINFRA",
			"Savita Oil Technologies Ltd":"SOTL",
			"Southern Ispat & Energy Ltd":"SOUISPAT",
			"South Indian Bank Ltd.":"SOUTHBANK",
			"South West Pinnacle Exploration Ltd.":"SOUTHWEST",
			"S.P. Apparels Ltd":"SPAL",
			"Spanco Ltd":"SPANCO",
			"Spandana Sphoorty Financial Limited":"SPANDANA",
			"Sun Pharma Advanced Research Co. Ltd":"SPARC",
			"Spacenet Enterprises India Ltd.":"SPCENET",
			"Speciality Restaurants Ltd":"SPECIALITY",
			"Spectacle Ventures Ltd":"SPECTACLE",
			"Spencers Retail Ltd.":"SPENCERS",
			"CLC Industries Ltd.":"SPENTEX",
			"SPHERE GLOBAL SERVICE LTD":"SPHEREGSL",
			"Southern Petrochemicals Industries Corporation Ltd":"SPIC",
			"Spicejet Ltd":"SPICEJET",
			"Spice Communications Ltd.":"SPICETELE",
			"SPL Industries Ltd":"SPLIL",
			"Somany Ceramics Ltd.":"SPLLTD",
			"SPML Infra Ltd.":"SPMLINFRA",
			"Sintex Plastics Technology Ltd.":"SPTL",
			"Shekhawati Poly-Yarn Limited":"SPYL",
			"Sreeleathers Ltd":"SREEL",
			"SREI Infrastructure Finance Ltd.":"SREINFRA",
			"SRF Ltd.":"SRF",
			"PAN India Corporation Ltd.":"SRGINFOTEC",
			"SRHHL Industries Ltd":"SRHHLINDST",
			"Sree Rayalaseema Hi-Strength Hypo Ltd.":"SRHHYPOLTD",
			"Sri Chamundeswari Sugars Ltd":"SRICHAMUND",
			"Srikalahasthi Pipes Ltd":"SRIPIPES",
			"SRS Ltd":"SRSLTD",
			"Shriram Transport Finance Co. Ltd.":"SRTRANSFIN",
			"Steel Strips Wheels Ltd.":"SSWL",
			"Stampede Capital Ltd":"STAMPEDE",
			"Strides Pharma Science Ltd.":"STAR",
			"Star Cement Ltd.":"STARCEMENT",
			"Star Paper Mills Ltd.":"STARPAPER",
			"State Trading Corporation of India Ltd.":"STCINDIA",
			"Steel City Securities Ltd.":"STEELCITY",
			"Steel Tubes of India Ltd.":"STEELTUBES",
			"Steel Exchange India Ltd.":"STEELXIND",
			"STEL Holdings Ltd":"STEL",
			"Sterlite IndustriesLtd.":"STER",
			"Sterling Biotech Ltd.":"STERLINBIO",
			"Sterling Tools Ltd.":"STERTOOLS",
			"International Constructions Ltd.":"SUBCAPCITY",
			"Subex Ltd.":"SUBEX",
			"Subros Ltd.":"SUBROS",
			"Sudar Industries Ltd":"SUDAR",
			"Sudarshan Chemical Industries Ltd.":"SUDARSCHEM",
			"Sujana Universal Industries Ltd.":"SUJANAUNI",
			"Sumeet Industries Ltd.":"SUMEETINDS",
			"Sumitomo Chemical India Ltd.":"SUMICHEM",
			"Sumit Woods Ltd.":"SUMIT",
			"Summit Securities Ltd":"SUMMIT",
			"Summit Securities Ltd":"SUMMITSEC",
			"Sundaram-Clayton Ltd.":"SUNCLAYLTD",
			"Sundaram Multi Pap Ltd.":"SUNDARAM",
			"Sundaram Finance Ltd.":"SUNDARMFIN",
			"Sundaram Finance Holdings Ltd.":"SUNDARMHLD",
			"Sundaram Brake Linings Ltd.":"SUNDRMBRAK",
			"Sundram Fasteners Ltd":"SUNDRMFAST",
			"Sunflag Iron & Steel Co. Ltd.":"SUNFLAG",
			"Sunil Hitech Engineers Ltd.":"SUNILHITEC",
			"Sun Pharmaceutical Industries Ltd.":"SUNPHARMA",
			"Sunteck Realty Ltd.":"SUNTECK",
			"Sun TV Network Ltd.":"SUNTV",
			"Super Sales India Ltd.":"SUPER",
			"Superhouse Ltd.":"SUPERHOUSE",
			"Super Spinning Mills Ltd.":"SUPERSPIN",
			"Supreme Petrochem Ltd.":"SUPPETRO",
			"Suprajit Engineering Ltd.":"SUPRAJIT",
			"Supreme Industries Ltd.":"SUPREMEIND",
			"Supreme Infrastructure India Ltd.":"SUPREMEINF",
			"Supreme Tex mart Ltd":"SUPREMETEX",
			"Surana Corporation Ltd.":"SURANACORP",
			"Surana Industries Ltd.":"SURANAIND",
			"Surana Solar Ltd.":"SURANASOL",
			"Surana Telecom and Power Ltd.":"SURANAT_P",
			"Suryajyoti Spinning Mills Ltd.":"SURYAJYOTI",
			"Suryalakshmi Cotton Mills Ltd.":"SURYALAXMI",
			"Surya Pharmaceutical Ltd.":"SURYAPHARM",
			"Surya Roshni Ltd.":"SURYAROSNI",
			"SIL Investments Ltd.":"SUTLEJINDS",
			"Sutlej Textiles and Industries Ltd":"SUTLEJTEX",
			"Suven Life Sciences Ltd.":"SUVEN",
			"Suven Pharmaceuticals Ltd.":"SUVENPHAR",
			"Suzlon Energy Ltd.":"SUZLON",
			"SVOGL Oil Gas & Energy Ltd.":"SVOGL",
			"Swan Energy Ltd":"SWANENERGY",
			"Swaraj Engines Ltd.":"SWARAJENG",
			"Swelect Energy Systems Ltd":"SWELECTES",
			"Sterling and Wilson Solar Ltd":"SWSOLAR",
			"Symphony Ltd.":"SYMPHONY",
			"Syncom Healthcare Limited":"SYNCOM",
			"Syndicate Bank":"SYNDIBANK",
			"Syngene International Ltd.":"SYNGENE",
			"Tainwala Chemicals & PlasticsLtd.":"TAINWALCHM",
			"Taj GVK Hotels & Resorts Ltd.":"TAJGVK",
			"Take Solutions Ltd.":"TAKE",
			"Taksheel Solutions Ltd":"TAKSHEEL",
			"Talbros Automotive Components Ltd.":"TALBROAUTO",
			"Talwalkars Better Value Fitness Ltd.":"TALWALKARS",
			"Talwalkars Healthclubs Ltd.":"TALWGYM",
			"TANFAC Industries Ltd.":"TANFACIND",
			"Tanla Solutions Ltd.":"TANLA",
			"Tantia Constructions Ltd.":"TANTIACONS",
			"Tara Jewels Ltd":"TARAJEWELS",
			"Tarapur Transformers Ltd.":"TARAPUR",
			"Tarmat Ltd":"TARMAT",
			"Tasty Bite Eatables Ltd.":"TASTYBITE",
			"Tata Chemicals Ltd.":"TATACHEM",
			"Tata Coffee Ltd.":"TATACOFFEE",
			"Tata Communications Ltd.":"TATACOMM",
			"Tata Consumer Products Ltd.":"TATACONSUM",
			"Tata Elxsi Ltd.":"TATAELXSI",
			"Tata Investment Corporation Ltd.":"TATAINVEST",
			"Tata Metaliks Ltd.":"TATAMETALI",
			"Tata Motors Ltd.":"TATAMOTORS",
			"Tata Motors Ltd.":"TATAMTRDVR",
			"Tata Power Co. Ltd.":"TATAPOWER",
			"Tata Steel Ltd.":"TATASTEEL",
			"Tata Steel BSL Ltd.":"TATASTLBSL",
			"Tata Steel Long Products Ltd.":"TATASTLLP",
			"Tribhovandas Bhimji Zaveri Ltd":"TBZ",
			"Transport Corporation of India Ltd.":"TCI",
			"TCI Developers Ltd.":"TCIDEVELOP",
			"TCI Express Ltd":"TCIEXP",
			"TCI Finance Ltd.":"TCIFINANCE",
			"TCNS Clothing Co. Ltd.":"TCNSBRANDS",
			"TCPL Packaging Ltd":"TCPLPACK",
			"TCP Ltd.":"TCPLTD",
			"Tata Consultancy Services":"TCS",
			"TD Power Systems Ltd":"TDPOWERSYS",
			"TeamLease Services Ltd":"TEAMLEASE",
			"Techindia Nirman Ltd":"TECHIN",
			"Tech Mahindra Ltd.":"TECHM",
			"Techno Electric & Engineering Co. Ltd.":"TECHNO",
			"Techno Electric & Engineering Co Ltd":"TECHNOE",
			"Techno Electric & Engineering Co. Ltd.":"TECHNOELEC",
			"Technofab Engineering Ltd":"TECHNOFAB",
			"Tecpro Systems Ltd":"TECPRO",
			"Tejas Networks Ltd":"TEJASNET",
			"Agnite Education Ltd":"TELEDATAGL",
			"Teledata Technology Solutions Ltd":"TELEDATAIT",
			"Teledata Marine Solutions Ltd":"TELEMARINE",
			"Tera Software Ltd.":"TERASOFT",
			"Texmaco Infrastructure & Holdings Ltd":"TEXINFRA",
			"Texmo Pipes and Products Ltd.":"TEXMOPIPES",
			"Texmaco Rail & Engineering Ltd":"TEXRAIL",
			"Tourism Finance Corporation of India Ltd.":"TFCILTD",
			"Transwarranty Finance Ltd.":"TFL",
			"TGB Banquets & Hotels Ltd":"TGBHOTELS",
			"Thangamayil Jewellery Limited":"THANGAMAYL",
			"Investment Trust of India Ltd.":"THEINVEST",
			"Themis Medicare Ltd.":"THEMISMED",
			"Thermax Ltd.":"THERMAX",
			"Thiru Arooran Sugars Ltd.":"THIRUSUGAR",
			"Thomas CookLtd.":"THOMASCOOK",
			"Thomas ScottLtd":"THOMASCOTT",
			"Thyrocare Technologies Limited":"THYROCARE",
			"Tilaknagar Industries Ltd.":"TI",
			"Tide Water OilLtd.":"TIDEWATER",
			"Technocraft IndustriesLtd.":"TIIL",
			"Tube Investments of India Ltd.":"TIINDIA",
			"Tijaria Polypipes Ltd":"TIJARIA",
			"TIL Ltd.":"TIL",
			"Timbor Home Ltd":"TIMBOR",
			"Times Guaranty Ltd.":"TIMESGTY",
			"Time Technoplast Ltd.":"TIMETECHNO",
			"Timken India Ltd.":"TIMKEN",
			"Tinplate Company of India Ltd.":"TINPLATE",
			"Tips Industries Ltd.":"TIPSINDLTD",
			"Thirumalai Chemicals Ltd.":"TIRUMALCHM",
			"Titan Co. Ltd":"TITAN",
			"Mandhana Retail Ventures Ltd":"TMRVL",
			"Tamilnadu Petroproducts Ltd.":"TNPETRO",
			"Tamil Nadu Newsprint & Papers Ltd.":"TNPL",
			"Tamilnadu Telecommunications Ltd.":"TNTELE",
			"Today`s Writing Instruments Ltd":"TODAYS",
			"Tokyo Plast International Ltd.":"TOKYOPLAST",
			"Torrent Pharmaceuticals Ltd.":"TORNTPHARM",
			"Torrent Power Ltd.":"TORNTPOWER",
			"Touchwood Entertainment Ltd.":"TOUCHWOOD",
			"TPL Plastech Ltd.":"TPLPLASTEH",
			"Treadsdirect Ltd":"TREADS",
			"Tree House Education & Accessories Ltd":"TREEHOUSE",
			"Trejhara Solutions Ltd.":"TREJHARA",
			"Trent Ltd.":"TRENT",
			"TRF Ltd.":"TRF",
			"Tricom India Ltd":"TRICOM",
			"Trident Ltd":"TRIDENT",
			"Trigyn Technologies Ltd.":"TRIGYN",
			"Transformers & RectifiersLtd.":"TRIL",
			"Triveni Turbine Ltd.":"TRITURBINE",
			"Triveni Engineering & Industries Ltd.":"TRIVENI",
			"TTK Healthcare Ltd.":"TTKHLTCARE",
			"TTK Prestige Ltd.":"TTKPRESTIG",
			"T T Ltd.":"TTL",
			"Tata TeleservicesLtd.":"TTML",
			"Tulip Telecom Ltd":"TULIP",
			"Tulsi Extrusions Ltd":"TULSI",
			"Tulsyan NEC Ltd.":"TULSYAN",
			"TV18 Broadcast Ltd":"TV18BRDCST",
			"TVS Electronics Ltd..":"TVSELECT",
			"TVS Motor Co Ltd.":"TVSMOTOR",
			"TVS Srichakra Ltd.":"TVSSRICHAK",
			"TV Today Network":"TVTODAY",
			"TV Vision Ltd":"TVVISION",
			"Twilight Litaka Pharmaceuticals Ltd.":"TWILITAKA",
			"Titagarh Wagons Ltd":"TWL",
			"UB Engineering Ltd.":"UBENGG",
			"United Breweries Holdings Ltd.":"UBHOLDINGS",
			"United Breweries Ltd":"UBL",
			"UCAL Fuel Systems Ltd.":"UCALFUEL",
			"UCO Bank":"UCOBANK",
			"Uflex Ltd.":"UFLEX",
			"UFO Moviez India Ltd.":"UFO",
			"Ugar Sugar Works Ltd.":"UGARSUGAR",
			"Ujaas Energy Ltd":"UJAAS",
			"Ujjivan Financial Services Ltd":"UJJIVAN",
			"Ujjivan Small Finance Bank Limited":"UJJIVANSFB",
			"UltraTech Cement Ltd.":"ULTRACEMCO",
			"Umang Dairies Ltd":"UMANGDAIRY",
			"Usha Martin Education & Solutions Ltd":"UMESLTD",
			"Unichem Laboratories Ltd.":"UNICHEMLAB",
			"Uniphos Enterprises Ltd.":"UNIENTER",
			"Union Bank of India":"UNIONBANK",
			"Uniply Industries Ltd":"UNIPLY",
			"Unitech Ltd.":"UNITECH",
			"United Bank of India":"UNITEDBNK",
			"United Nilgiri Tea Estates Co. Ltd.":"UNITEDTEA",
			"Unity Infraprojects Ltd.":"UNITY",
			"Universal Cables Ltd.":"UNIVCABLES",
			"Universus Photo Imagings Ltd.":"UNIVPHOTO",
			"Upper Ganges Sugar & Industries Ltd.":"UPERGANGES",
			"UPL Ltd":"UPL",
			"Urja Global Ltd":"URJA",
			"Usha Martin Ltd.":"USHAMART",
			"Usher Agro Ltd.":"USHERAGRO",
			"UTI Asset Management Company Ltd":"UTINEXT50",
			"UTI Asset Management Company Ltd":"UTINIFTETF",
			"UTI Asset Management Company Ltd":"UTISENSETF",
			"Unit Trust of India":"UTISUNDER",
			"UTI Asset Management Company Ltd":"UTISXN50",
			"Uttam Galva Steels Ltd.":"UTTAMSTL",
			"Uttam Sugar Mills Ltd.":"UTTAMSUGAR",
			"UTV Software Communications Ltd.":"UTVSOF",
			"Uttam Value Steels Ltd":"UVSL",
			"V2 Retail Ltd":"V2RETAIL",
			"Vadilal Industries Ltd.":"VADILALIND",
			"Vaibhav Global Ltd":"VAIBHAVGBL",
			"Vaishali Pharma Ltd":"VAISHALI",
			"Vakrangee Ltd":"VAKRANGEE",
			"Valecha Engineering Ltd.":"VALECHAENG",
			"Value Industries Ltd":"VALUEIND",
			"Vardhman Acrylics Ltd.":"VARDHACRLC",
			"Vardhman Polytex Ltd.":"VARDMNPOLY",
			"Varroc Engineering Limited":"VARROC",
			"Varun Industries Ltd.":"VARUN",
			"Varun Shipping Co. Ltd.":"VARUNSHIP",
			"Vascon Engineers Limited":"VASCONEQ",
			"Vaswani Industries Ltd":"VASWANI",
			"Lila World Wide Ltd":"VATSMUSC",
			"Varun Bevarages Limited":"VBL",
			"Vedanta Ltd":"VEDL",
			"Venky`sLtd.":"VENKEYS",
			"Venus Remedies Ltd.":"VENUSREM",
			"Vesuvius India Ltd.":"VESUVIUS",
			"Veto Switchgears & Cables Ltd.":"VETO",
			"V-Guard Industries Ltd":"VGUARD",
			"Vardhman Holdings Ltd.":"VHL",
			"Viceroy Hotels Ltd.":"VICEROY",
			"Videocon Industries Ltd.":"VIDEOIND",
			"Vidhi Specialty Food Ingredients Ltd.":"VIDHIING",
			"Vijaya Bank":"VIJAYABANK",
			"Viji Finance Ltd.":"VIJIFIN",
			"Vijay Shanthi Builders Ltd.":"VIJSHAN",
			"Vikas EcoTech Ltd.":"VIKASECO",
			"Vikash Metal & Power Ltd.":"VIKASHMET",
			"Vikas Multicorp Ltd.":"VIKASMCORP",
			"Vikas Proppant & Granite Ltd.":"VIKASPROP",
			"Vikas WSP Ltd.":"VIKASWSP",
			"Vimal Oil & Foods Ltd.":"VIMALOIL",
			"Vimta Labs Ltd.":"VIMTALABS",
			"Vinati Organics Ltd.":"VINATIORGA",
			"Vintage Cards & Creations Ltd.":"VINCARDS",
			"Vindhya Telelinks Ltd.":"VINDHYATEL",
			"Vinyl ChemicalsLtd.":"VINYLINDIA",
			"VIP Clothing Ltd.":"VIPCLOTHNG",
			"V.I.P. Industries Ltd.":"VIPIND",
			"Vipul Ltd.":"VIPULLTD",
			"Visaka Industries Ltd.":"VISAKAIND",
			"Visa Steel Ltd.":"VISASTEEL",
			"MPS Infotecnics Ltd.":"VISESHINFO",
			"Vishal Fabrics Ltd":"VISHAL",
			"Vishal Exports Overseas Ltd.":"VISHALEXPO",
			"Vishnu Chemicals Ltd":"VISHNU",
			"Vishwaraj Sugar Industries Ltd.":"VISHWARAJ",
			"Visualsoft Technologies Ltd.":"VISUALSOFT",
			"Visu International Ltd.":"VISUINTL",
			"Visagar Polytex Ltd":"VIVIDHA",
			"Vivimed Labs Ltd.":"VIVIMEDLAB",
			"VKS Projects Ltd":"VKSPL",
			"VLS Finance Ltd.":"VLSFINANCE",
			"V-Mart Retail Ltd":"VMART",
			"Voltamp Transformers Ltd.":"VOLTAMP",
			"Voltas Ltd.":"VOLTAS",
			"VRL Logistics Ltd":"VRLLOG",
			"Vardhman Special Steels Ltd.":"VSSL",
			"VST Industries Ltd.":"VSTIND",
			"VST Tillers Tractors Ltd.":"VSTTILLERS",
			"Vardhman Textiles Ltd":"VTL",
			"VTM Ltd.":"VTMLTD",
			"VTX Industries Ltd":"VTXIND",
			"Va Tech Wabag Ltd":"WABAG",
			"WABCO India Ltd":"WABCOINDIA",
			"Walchandnagar Industries Ltd.":"WALCHANNAG",
			"Wanbury Ltd.":"WANBURY",
			"Wartsila India Ltd.":"WARTSILA",
			"Waterbase Ltd.":"WATERBASE",
			"Websol Energy System Ltd":"WEBELSOLAR",
			"Weizmann Ltd.":"WEIZMANIND",
			"Welspun Corp Ltd.":"WELCORP",
			"Welspun Enterprises Ltd.":"WELENT",
			"Welspun Global Brands Ltd.":"WELGLOB",
			"Welspun Investments & Commercials Ltd":"WELINV",
			"WELSPUN SYNTEX LIMITED":"WELSYNTEX",
			"WendtLtd.":"WENDT",
			"Westlife Development Ltd":"WESTLIFE",
			"Wheels India Ltd.":"WHEELS",
			"Whirlpool of India Ltd.":"WHIRLPOOL",
			"Williamson Magor & Co. Ltd.":"WILLAMAGOR",
			"Windsor Machines Ltd.":"WINDMACHIN",
			"Winsome Yarns Ltd.":"WINSOME",
			"Winsome Diamonds & Jewellery Ltd":"WINSOMEDJ",
			"Western India Plywoods Ltd.":"WIPL",
			"Wipro Ltd.":"WIPRO",
			"Wockhardt Ltd.":"WOCKPHARMA",
			"Wonderla Holidays Ltd":"WONDERLA",
			"W.S. IndustriesLtd.":"WSI",
			"West Coast Paper Mills Ltd.":"WSTCSTPAPR",
			"Wyeth Ltd.":"WYETH",
			"Xchanging Solution Ltd":"XCHANGING",
			"Xelpmoc Design & Tech Ltd.":"XELPMOC",
			"XL Energy Ltd.":"XLENERGY",
			"Xpro India Ltd.":"XPROINDIA",
			"Yes Bank Ltd.":"YESBANK",
			"Yokogawa India Ltd.":"YOKOGAWA",
			"Zandu Realty Ltd":"ZANDUREALT",
			"Zee Entertainment Enterprises Ltd":"ZEEL",
			"Zee Learn Ltd":"ZEELEARN",
			"Zee Media Corporation Ltd":"ZEEMEDIA",
			"Zenith BirlaLtd":"ZENITHBIR",
			"Zenith Computer Ltd.":"ZENITHCOMP",
			"Zenith Exports Ltd.":"ZENITHEXPO",
			"Zenith Infotech Ltd.":"ZENITHINFO",
			"Zensar Technologies Ltd.":"ZENSARTECH",
			"Zen Technologies Ltd.":"ZENTEC",
			"Zicom Electronic Security Systems Ltd.":"ZICOM",
			"Zodiac Clothing Co. Ltd.":"ZODIACLOTH",
			"Zodiac-JRD-MKJ Ltd.":"ZODJRDMKJ",
			"Zota Health Care Ltd":"ZOTA",
			"Zuari Agro Chemicals Ltd":"ZUARI",
			"Zuari Global Ltd":"ZUARIGLOB",
			"Zydus Wellness Ltd":"ZYDUSWELL",
			"Zylog Systems Ltd.":"ZYLOG",
			}
		StockMarketCode=''
		myCompanyName=myCompany.strip()
		if myCompanyName in QuandlDict.keys():
				StockMarketCode=QuandlDict.get(myCompanyName)
		mydata =quandl.get("NSE/"+StockMarketCode,authtoken="ikBXESLhQBzC5Rgfb5RS")
		mydata.to_csv("data/StockMarket/"+StockMarketCode+".csv")
		st = pd.read_csv("data/StockMarket/"+StockMarketCode+".csv")
		#st = pd.read_csv(r"data\StockMarket\SBIN.csv")
		#C:\Users\sreya\Desktop\Tarunk9\EdithT\data\DataMC\splits\SPLITS-MC-Adani Power Limited  .csv
		div = pd.read_csv("data/DataMC/dividends/DIV-MC-"+myCompany+".csv")
		agm = pd.read_csv("data/DataMC/aeb/AEB-MC-"+myCompany+".csv")
		#bm = pd.read_csv("data/DataMC/boardmeetings/boardmeetings"+myCompany+".csv")
		bo = pd.read_csv("data/DataMC/bonus/BONUS-MC-"+myCompany+".csv")   
		ri = pd.read_csv("data/DataMC/rights/RIGHTS-MC-"+myCompany+".csv")
		sp = pd.read_csv("data/DataMC/splits/SPLITS-MC-"+myCompany+".csv")

	#Converting dates to datetime format 
		st['Date'] = pd.to_datetime(st.Date)

		div['Announcement_Date'] = pd.to_datetime(div.Announcement_Date)

		agm['Announcement_Date'] = pd.to_datetime(agm.Announcement_Date)

		#bm['Meeting_Date'] = pd.to_datetime(bm.Meeting_Date)

		bo['Announcement_Date'] = pd.to_datetime(bo.Announcement_Date)

		ri['Announcement_Date'] = pd.to_datetime(ri.Announcement_Date)

		sp['Announcement_Date'] = pd.to_datetime(sp.Announcement_Date)

		ri['Announcement_Date'] = pd.to_datetime(ri.Announcement_Date)

		sp['Announcement_Date'] = pd.to_datetime(sp.Announcement_Date)

	#Sorting and adding Dates 
		div = div.sort_values(by='Announcement_Date')
		agm = agm.sort_values(by='Announcement_Date')
		#bm = bm.sort_values(by='Meeting_Date')
		bo = bo.sort_values(by='Announcement_Date')
		ri =ri.sort_values(by='Announcement_Date')
		sp = sp.sort_values(by='Announcement_Date')

		div['Date'] = div['Announcement_Date']
		agm['Date'] = agm['Announcement_Date']
		#bm['Date'] = bm['Meeting_Date']
		bo['Date'] = bo['Announcement_Date']
		ri['Date'] = ri['Announcement_Date']
		sp['Date'] = sp['Announcement_Date']

	#Setting & restting index
		st = st.set_index('Date')
		div = div.set_index('Date')
		agm = agm.set_index('Date')
		#bm = bm.set_index('Date')
		bo = bo.set_index('Date')
		ri = ri.set_index('Date')
		sp = sp.set_index('Date')

	#final dataframe
		finaldiv = pd.concat([st,div],axis=1)
		finalagm = pd.concat([st,agm],axis=1)
		#finalbm = pd.concat([st,bm],axis=1)
		finalbo = pd.concat([st,bo],axis=1)
		finalri = pd.concat([st,ri],axis=1)
		finalsp = pd.concat([st,sp],axis=1)

		finaldiv = finaldiv.reset_index()
		finalagm = finalagm.reset_index()
		#finalbm = finalbm.reset_index()
		finalbo = finalbo.reset_index()
		finalri = finalri.reset_index()
		finalsp = finalsp.reset_index()

		x0 = finaldiv['Date']

		y0 = finaldiv['Close'] 

		xdiv = finaldiv['Announcement_Date']

		ydiv = finaldiv['Dividend']

		xagm = finalagm['Announcement_Date']

		#xbm = finalbm['Meeting_Date']

		xbo = finalbo['Announcement_Date']

		xri = finalri['Announcement_Date']

		xsp = finalsp['Announcement_Date']

	# Create traces

		fig0=go.Candlestick(x=x0,
						open=finaldiv['Open'],
						high=finaldiv['High'],
						low=finaldiv['Low'],
						close=y0)

		fig1_1=go.Scatter(x=x0, y=y0,
							mode='lines',
							name='Stock Price')

		fig1_2=go.Scatter(x=xdiv, y=y0,
							mode='markers', name='Announcement Date')

		fig1_3=go.Scatter(x=xdiv, y=ydiv,
							mode='markers', name='Dividends Amount')
			
		

		fig2_1=go.Scatter(x=x0, y=y0,
							mode='lines',
							name='Stock Price')

		fig2_2=go.Scatter(x=xagm, y=y0,
							mode='markers', name='Announcement Date')



	
		#fig3_1=go.Scatter(x=x0, y=y0,mode='lines',name='Stock Price')

		#fig3_2=go.Scatter(x=xbm, y=y0,mode='markers', name='Meeting Date')


		

		fig4_1=go.Scatter(x=x0, y=y0,
							mode='lines',
							name='Stock Price')

		fig4_2=go.Scatter(x=xbo, y=y0,
							mode='markers', name='Announcement Date')



		fig5_1=go.Scatter(x=x0, y=y0,
							mode='lines',
							name='Stock Price')

		fig5_2=go.Scatter(x=xri, y=y0,
							mode='markers', name='Announcement Date')

			
		
		fig6_1=go.Scatter(x=x0, y=y0,
							mode='lines',
							name='Stock Price')

		fig6_2=go.Scatter(x=xsp, y=y0,
							mode='markers', name='Announcement Date')


			
		data0 = [fig0]
		data1 = [fig1_1,fig1_2,fig1_3]
		data2 = [fig2_1,fig2_2]
		#data3 = [fig3_1,fig3_2]
		data4 = [fig4_1,fig4_2]
		data5 = [fig5_1,fig5_2]
		data6 = [fig6_1,fig6_2]

		graphJSON0 = json.dumps(data0, cls=plotly.utils.PlotlyJSONEncoder)
		graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
		graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)
		#graphJSON3 = json.dumps(data3, cls=plotly.utils.PlotlyJSONEncoder)
		graphJSON4 = json.dumps(data4, cls=plotly.utils.PlotlyJSONEncoder)
		graphJSON5 = json.dumps(data5, cls=plotly.utils.PlotlyJSONEncoder)
		graphJSON6 = json.dumps(data6, cls=plotly.utils.PlotlyJSONEncoder)
##############################################################################################################################
		
								
	return render_template("stockanalysis.html",graphJSON0=graphJSON0,
			graphJSON1=graphJSON1,
			graphJSON2=graphJSON2,
			graphJSON4=graphJSON4,
			graphJSON5=graphJSON5,
			graphJSON6=graphJSON6,)
@app.route('/upcoming')
def upcoming():

	#UPcoming
	#specify the url
	caBonus1 = "https://www.moneycontrol.com/stocks/marketinfo/bonus/index.php?sel_year=2020"
	#Query the website and return the html to the variable 'page'
	pageB1 = urllib.request.urlopen(caBonus1)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soupB1 = BeautifulSoup(pageB1)
	right_tableB1=soupB1.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	A1UpcomingBonus=[]
	B1UpcomingBonus=[]
	C1UpcomingBonus=[]
	D1UpcomingBonus=[]
	E1UpcomingBonus=[]
	for row1 in right_tableB1.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==5: #Only extract table body not heading
			A1UpcomingBonus.append(cells1[0].find(text=True))
			B1UpcomingBonus.append(cells1[1].find(text=True))
			C1UpcomingBonus.append(cells1[2].find(text=True))
			D1UpcomingBonus.append(cells1[3].find(text=True))
			E1UpcomingBonus.append(cells1[4].find(text=True))
	dfUpcomingBonus=pd.DataFrame(A1UpcomingBonus,columns=['Company'])
	dfUpcomingBonus['Bonus_Ratio']=B1UpcomingBonus
	dfUpcomingBonus['Announcement']=C1UpcomingBonus
	dfUpcomingBonus['Record_Date']=D1UpcomingBonus
	dfUpcomingBonus['Ex-Bonus_Date']=E1UpcomingBonus
	#dfUpcomingBonus.to_csv(r"C:\UserUpcomingBonuss\sreya\Desktop\MajorProject\Jarvis\data\DataUCMC\UpcomingBonus.csv")
	#dfUpcomingBonus.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0'], level=None, inplace=False, errors='raise')

	caBordMeetings1 = "https://www.moneycontrol.com/stocks/marketinfo/meetings.php?opttopic=brdmeeting"
	#Query the website and return the html to the variable 'page'
	pageBordMeetings1 = urllib.request.urlopen(caBordMeetings1)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soupBordMeetings1 = BeautifulSoup(pageBordMeetings1)
	right_tableBordMeetings1=soupBordMeetings1.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	AUpcomingBordMeetings1=[]
	BUpcomingBordMeetings1=[]
	CUpcomingBordMeetings1=[]

	for row1 in right_tableBordMeetings1.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==3: #Only extract table body not heading
			AUpcomingBordMeetings1.append(cells1[0].find(text=True))
			BUpcomingBordMeetings1.append(cells1[1].find(text=True))
			CUpcomingBordMeetings1.append(cells1[2].find(text=True))
	dfUpcomingBordMeetings=pd.DataFrame(AUpcomingBordMeetings1,columns=['Company'])
	dfUpcomingBordMeetings['Date']=BUpcomingBordMeetings1
	dfUpcomingBordMeetings['Agenda']=CUpcomingBordMeetings1
	#specify the url
	caAGM = "https://www.moneycontrol.com/stocks/marketinfo/agm_egm.php"
	#Query the website and return the html to the variable 'page'
	pageAGM = urllib.request.urlopen(caAGM)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soupAGM = BeautifulSoup(pageAGM)
	right_tableAGM=soupAGM.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	AUpcomingAGM=[]
	BUpcomingAGM=[]
	CUpcomingAGM=[]
	DUpcomingAGM=[]
	EUpcomingAGM=[]
	FUpcomingAGM=[]

	for row1 in right_tableAGM.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==6: #Only extract table body not heading
			AUpcomingAGM.append(cells1[0].find(text=True))
			BUpcomingAGM.append(cells1[1].find(text=True))
			CUpcomingAGM.append(cells1[2].find(text=True))
			DUpcomingAGM.append(cells1[3].find(text=True))
			EUpcomingAGM.append(cells1[4].find(text=True))
			FUpcomingAGM.append(cells1[4].find(text=True))
	dfUpcomingAGM=pd.DataFrame(AUpcomingAGM,columns=['Company'])
	dfUpcomingAGM['Date']=BUpcomingAGM
	dfUpcomingAGM['Purpose']=CUpcomingAGM
	dfUpcomingAGM['Start']=DUpcomingAGM
	dfUpcomingAGM['End']=EUpcomingAGM
	dfUpcomingAGM['Agenda']=FUpcomingAGM

	#specify the url
	caSplits = "https://www.moneycontrol.com/stocks/marketinfo/splits/index.php"
	#Query the website and return the html to the variable 'page'
	pageSplits = urllib.request.urlopen(caSplits)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soupSplits = BeautifulSoup(pageSplits)
	right_tableSplits=soupSplits.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	AUpcomingSplits=[]
	BUpcomingSplits=[]
	CUpcomingSplits=[]
	DUpcomingSplits=[]

	for row1 in right_tableSplits.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==4: #Only extract table body not heading
			AUpcomingSplits.append(cells1[0].find(text=True))
			BUpcomingSplits.append(cells1[1].find(text=True))
			CUpcomingSplits.append(cells1[2].find(text=True))
			DUpcomingSplits.append(cells1[3].find(text=True))
	dfUpcomingSplits=pd.DataFrame(AUpcomingSplits,columns=['Company'])
	dfUpcomingSplits['Old_FV']=BUpcomingSplits
	dfUpcomingSplits['New_FV']=CUpcomingSplits
	dfUpcomingSplits['Split_Date']=DUpcomingSplits
	#specify the url
	caDividends = "https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php?sel_year=2020"
	#Query the website and return the html to the variable 'page'
	pageDividends = urllib.request.urlopen(caDividends)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soupDividends = BeautifulSoup(pageDividends)
	right_tableDividends=soupDividends.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	AUpcomingDividends=[]
	BUpcomingDividends=[]
	CUpcomingDividends=[]
	DUpcomingDividends=[]
	EUpcomingDividends=[]
	FUpcomingDividends=[]


	for row1 in right_tableDividends.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==6: #Only extract table body not heading
			AUpcomingDividends.append(cells1[0].find(text=True))
			BUpcomingDividends.append(cells1[1].find(text=True))
			CUpcomingDividends.append(cells1[2].find(text=True))
			DUpcomingDividends.append(cells1[3].find(text=True))
			EUpcomingDividends.append(cells1[4].find(text=True))
			FUpcomingDividends.append(cells1[5].find(text=True))
	dfUpcomingDividends=pd.DataFrame(AUpcomingDividends,columns=['Company'])
	dfUpcomingDividends['Dividends_Type']=BUpcomingDividends
	dfUpcomingDividends['Dividends_%']=CUpcomingDividends
	dfUpcomingDividends['Announcement']=DUpcomingDividends
	dfUpcomingDividends['Record']=EUpcomingDividends
	dfUpcomingDividends['Ex_Dividend']=FUpcomingDividends

	#specify the url
	cabookclosure = "https://www.moneycontrol.com/stocks/marketinfo/meetings.php?opttopic=bookclosure"
	#Query the website and return the html to the variable 'page'
	pagebookclosure = urllib.request.urlopen(cabookclosure)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soupbookclosure = BeautifulSoup(pagebookclosure)
	right_tablebookclosure=soupbookclosure.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	AUpcomingbookclosure=[]
	BUpcomingbookclosure=[]
	CUpcomingbookclosure=[]
	DUpcomingbookclosure=[]



	for row1 in right_tablebookclosure.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==4: #Only extract table body not heading
			AUpcomingbookclosure.append(cells1[0].find(text=True))
			BUpcomingbookclosure.append(cells1[1].find(text=True))
			CUpcomingbookclosure.append(cells1[2].find(text=True))
			DUpcomingbookclosure.append(cells1[3].find(text=True))
	dfUpcomingbookclosure=pd.DataFrame(AUpcomingbookclosure,columns=['Company'])
	dfUpcomingbookclosure['Start_Date']=BUpcomingbookclosure
	dfUpcomingbookclosure['End_Date']=CUpcomingbookclosure
	dfUpcomingbookclosure['Agenda']=DUpcomingbookclosure
	#specify the url
	carights = "https://www.moneycontrol.com/stocks/marketinfo/rights/index.php"
	#Query the website and return the html to the variable 'page'
	pagerights= urllib.request.urlopen(carights)
	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	souprights = BeautifulSoup(pagerights)
	right_tablerights=souprights.find('table', class_='b_12 dvdtbl tbldata14')
	#Generate lists
	AUpcomingrights=[]
	BUpcomingrights=[]
	CUpcomingrights=[]
	DUpcomingrights=[]
	EUpcomingrights=[]
	FUpcomingrights=[]
	GUpcomingrights=[]

	for row1 in right_tablerights.findAll("tr"):
		cells1 = row1.findAll('td')
		if len(cells1)==7: #Only extract table body not heading
			AUpcomingrights.append(cells1[0].find(text=True))
			BUpcomingrights.append(cells1[1].find(text=True))
			CUpcomingrights.append(cells1[2].find(text=True))
			DUpcomingrights.append(cells1[3].find(text=True))
			EUpcomingrights.append(cells1[4].find(text=True))
			FUpcomingrights.append(cells1[5].find(text=True))
			GUpcomingrights.append(cells1[6].find(text=True))
	dfUpcomingrights=pd.DataFrame(AUpcomingrights,columns=['Company'])
	dfUpcomingrights['Rights_Ratio']=BUpcomingrights
	dfUpcomingrights['FV']=CUpcomingrights
	dfUpcomingrights['Premium']=DUpcomingrights
	dfUpcomingrights['Announcement']=EUpcomingrights
	dfUpcomingrights['Record']=FUpcomingrights
	dfUpcomingrights['Ex-Rights']=GUpcomingrights
	return render_template("upcoming.html",	dfUpcomingrights=dfUpcomingrights,
			dfUpcomingbookclosure=dfUpcomingbookclosure,
			dfUpcomingDividends=dfUpcomingDividends,
			dfUpcomingSplits=dfUpcomingSplits,
			dfUpcomingAGM=dfUpcomingAGM,
			dfUpcomingBordMeetings=dfUpcomingBordMeetings,
			dfUpcomingBonus=dfUpcomingBonus)



@app.route('/analyze',methods=["POST"])
def analyze():

	#getting data from form and session starting
	if request.method == 'POST':
		session['myCompany']=request.form['myCompany']  
		#session['ca_type']=request.form['ca_type']
		#session['stock_company']=request.form['stock_company']   
		myCompany = request.form['myCompany']
		myCompany=myCompany.strip()
		#ca_type = request.form['ca_type']
		#stock_company = request.form['stock_company']
		CompanyNameMC=""
		CompanyCodeMC=""
		#takings sites in list
		sites=["corporate actions money control","corporate actions business standard"]
		for i in range (0,len(sites)):
			query=myCompany+sites[i]
			#scrapping data from site 2
			if sites[i]=="corporate actions money control":
				for j in search(query, tld="co.in", num=10, stop=1, pause=2):
					data=urlparse(j)
					str1=data.path
					l1=str1.split("/")
					if l1[2]=="stockpricequote":
						CompanyNameMC=l1[4]
						CompanyCodeMC=l1[5]
					elif l1[1]=="company-facts" or l1[1]=="company-notices":
						CompanyNameMC=l1[2]
						CompanyCodeMC=l1[4]	
				#if ca_type=='rights':
					#specify the url
					caRights = "https://www.moneycontrol.com/company-facts/"+CompanyNameMC+"/rights/"+CompanyCodeMC
					#Query the website and return the html to the variable 'page'
					pageRights = urllib.request.urlopen(caRights)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soupRights = BeautifulSoup(pageRights,features="lxml")
					right_tableRights=soupRights.find('table', class_='mctable1')
					#Generate lists
					ARights=[]
					BRights=[]
					CRights=[]
					DRights=[]
					ERights=[]
					FRights=[]
					for rowRights in right_tableRights.findAll("tr"):
						cellsRights = rowRights.findAll('td')
						if len(cellsRights)==6: #Only extract table body not heading
							ARights.append(cellsRights[0].find(text=True))
							BRights.append(cellsRights[1].find(text=True))
							CRights.append(cellsRights[2].find(text=True))
							DRights.append(cellsRights[3].find(text=True))
							ERights.append(cellsRights[4].find(text=True))
							FRights.append(cellsRights[5].find(text=True))	
					dfMCRights=pd.DataFrame(ARights,columns=['Announcement_Date'])
					dfMCRights['Rights_Ratio']=BRights
					dfMCRights['Face_Value']=CRights
					dfMCRights['Premium']=DRights
					dfMCRights['Record_Date']=ERights
					dfMCRights['Ex-Rights_Date']=FRights
					dfMCRights.to_csv(r"data\DataMC\rights\RIGHTS-MC-"+myCompany+".csv")
				#elif ca_type=='splits':
					#specify the url
					caSplits = "https://www.moneycontrol.com/company-facts/"+CompanyNameMC+"/splits/"+CompanyCodeMC
					#Query the website and return the html to the variable 'page'
					pageSplits = urllib.request.urlopen(caSplits)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soupSplits = BeautifulSoup(pageSplits,features="lxml")
					right_tableSplits=soupSplits.find('table', class_='mctable1')
					#Generate lists
					ASplits=[]
					BSplits=[]
					CSplits=[]
					DSplits=[]
					for rowSplits in right_tableSplits.findAll("tr"):
						cellsSplits = rowSplits.findAll('td')
						if len(cellsSplits)==4: #Only extract table body not heading
							ASplits.append(cellsSplits[0].find(text=True))
							BSplits.append(cellsSplits[1].find(text=True))
							CSplits.append(cellsSplits[2].find(text=True))
							DSplits.append(cellsSplits[3].find(text=True))
					dfMCSplits=pd.DataFrame(ASplits,columns=['Announcement_Date'])
					dfMCSplits['Old_FV']=BSplits
					dfMCSplits['New_FV']=CSplits
					dfMCSplits['Ex-Split_Date']=DSplits
					dfMCSplits.to_csv(r"data\DataMC\splits\SPLITS-MC-"+myCompany+".csv")
				#elif ca_type=='bonus':
					caBonus = "https://www.moneycontrol.com/company-facts/"+CompanyNameMC+"/bonus/"+CompanyCodeMC
					#Query the website and return the html to the variable 'page'
					pageB = urllib.request.urlopen(caBonus)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soupB = BeautifulSoup(pageB,features="lxml")
					right_tableB=soupB.find('table', class_='mctable1 MT20')
					#Generate lists
					A1=[]
					B1=[]
					C1=[]
					D1=[]
					for row1 in right_tableB.findAll("tr"):
						cells1 = row1.findAll('td')
						if len(cells1)==4: #Only extract table body not heading
							A1.append(cells1[0].find(text=True))
							B1.append(cells1[1].find(text=True))
							C1.append(cells1[2].find(text=True))
							D1.append(cells1[3].find(text=True))
					dfMCBonus=pd.DataFrame(A1,columns=['Announcement_Date'])
					dfMCBonus['Bonus_Ratio']=B1
					dfMCBonus['Record_Date']=C1
					dfMCBonus['Ex-Bonus_Date']=D1
					dfMCBonus.to_csv(r"data\DataMC\bonus\BONUS-MC-"+myCompany+".csv")
				#elif ca_type=='dividends':
					#specify the urlz
					ca = "https://www.moneycontrol.com/company-facts/"+CompanyNameMC+"/dividends/"+CompanyCodeMC
					#Query the website and return the html to the variable 'page'
					page = urllib.request.urlopen(ca)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup = BeautifulSoup(page,features="lxml")
					right_table=soup.find('table', class_='mctable1')
					#Generate lists
					A=[]
					B=[]
					C=[]
					D=[]
					E=[]
					for row in right_table.findAll("tr"):
						cells = row.findAll('td')
						if len(cells)==5: #Only extract table body not heading
							A.append(cells[0].find(text=True))
							B.append(cells[1].find(text=True))
							C.append(cells[2].find(text=True))
							D.append(cells[3].find(text=True))
							E.append(cells[4].find(text=True))
					dfMCDividens=pd.DataFrame(A,columns=['Announcement_Date'])
					dfMCDividens['Effective_Date']=B
					dfMCDividens['Dividend_Type']=C
					dfMCDividens['Dividend']=D
					dfMCDividens['Remarks']=E
					dfMCDividens.to_csv(r"data\DataMC\dividends\DIV-MC-"+myCompany+".csv")
				#elif ca_type=='aeb':
					#specify the url
					caagm_egm = "https://www.moneycontrol.com/company-facts/"+CompanyNameMC+"/agm-egm/"+CompanyCodeMC
					#Query the website and return the html to the variable 'page'
					pageagm_egm = urllib.request.urlopen(caagm_egm)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soupagm_egm = BeautifulSoup(pageagm_egm,features="lxml")
					right_tableagm_egm=soupagm_egm.find('table', class_='mctable1')
					#Generate lists
					Aagm_egm=[]
					Bagm_egm=[]
					Cagm_egm=[]
					Dagm_egm=[]
					Eagm_egm=[]
					Fagm_egm=[]
					for rowagm_egm in right_tableagm_egm.findAll("tr"):
						cellsagm_egm = rowagm_egm.findAll('td')
						if len(cellsagm_egm)==6: #Only extract table body not heading
							Aagm_egm.append(cellsagm_egm[0].find(text=True))
							Bagm_egm.append(cellsagm_egm[1].find(text=True))
							Cagm_egm.append(cellsagm_egm[2].find(text=True))
							Dagm_egm.append(cellsagm_egm[3].find(text=True))
							Eagm_egm.append(cellsagm_egm[4].find(text=True))
							Fagm_egm.append(cellsagm_egm[5].find(text=True))
					dfMCAgmEgm=pd.DataFrame(Aagm_egm,columns=['Announcement_Date'])
					dfMCAgmEgm['Purpose']=Bagm_egm
					dfMCAgmEgm['Date']=Cagm_egm
					dfMCAgmEgm['Book_Closure_From']=Dagm_egm
					dfMCAgmEgm['Book_Closure_To']=Eagm_egm
					dfMCAgmEgm['Remark']=Fagm_egm
					dfMCAgmEgm.to_csv(r"data\DataMC\aeb\AEB-MC-"+myCompany+".csv")
				#elif ca_type=='boardmeetings':
					#specify the url
					caboard_meetings = "https://www.moneycontrol.com/company-facts/"+CompanyNameMC+"/board-meetings/"+CompanyCodeMC
					#Query the website and return the html to the variable 'page'
					pageboard_meetings = urllib.request.urlopen(caboard_meetings)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soupboard_meetings = BeautifulSoup(pageboard_meetings,features="lxml")
					right_tableboard_meetings=soupboard_meetings.find('table', class_='mctable1 MT20 board-meeting-table')
					#Generate lists
					Aboard_meetings=[]
					Bboard_meetings=[]
					for rowboard_meetings in right_tableboard_meetings.findAll("tr"):
						cellsboard_meetings = rowboard_meetings.findAll('td')
						if len(cellsboard_meetings)==2: #Only extract table body not heading
							Aboard_meetings.append(cellsboard_meetings[0].find(text=True))
							Bboard_meetings.append(cellsboard_meetings[1].find(text=True))
					dfMCBoardmeetings=pd.DataFrame(Aboard_meetings,columns=['Meeting_Date'])
					dfMCBoardmeetings['Remark']=Bboard_meetings
					dfMCBoardmeetings.to_csv(r"data\DataMC\boardmeetings\BOARDMEETINGS-MC-"+myCompany+".csv")
				#getting link for site 1
				
			elif sites[i]=="corporate actions business standard":
				for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
					spl_word = 'https://www.business-standard.com/company/'
					if(spl_word in j):
							res = j.partition(spl_word)[2] 
							spl_word1='/'
							res1 = res.partition(spl_word1)[0] 
					companyNameBScodeNew=res1
					#scrapping from site 1
					#if ca_type=='rights':
						#specify the url
					ca_rights_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=rights&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_rights_Bs = urllib.request.urlopen(ca_rights_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_rights_Bs = BeautifulSoup(page_rights_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_rights_Bs=soup_rights_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_rights_Bs=[]
					B_rights_Bs=[]
					C_rights_Bs=[]
					D_rights_Bs=[]
					E_rights_Bs=[]
					F_rights_Bs=[]
					for row in right_div_rights_Bs.findAll("tr"):
						cells_rights_Bs = row.findAll('td')
						if len(cells_rights_Bs)==6: #Only extract table body not heading
							A_rights_Bs.append(cells_rights_Bs[0].find(text=True))
							B_rights_Bs.append(cells_rights_Bs[1].find(text=True))
							C_rights_Bs.append(cells_rights_Bs[2].find(text=True))
							D_rights_Bs.append(cells_rights_Bs[3].find(text=True))
							E_rights_Bs.append(cells_rights_Bs[4].find(text=True))
							F_rights_Bs.append(cells_rights_Bs[5].find(text=True))
					dfBSRights=pd.DataFrame(A_rights_Bs,columns=['Announcement_Date'])
					dfBSRights['PURPOSE']=B_rights_Bs
					dfBSRights['RECORD_DATE']=C_rights_Bs
					dfBSRights['EX_BONUS_DATE']=D_rights_Bs
					dfBSRights['RATIO']=E_rights_Bs
					dfBSRights['PREMIUM']=F_rights_Bs
					dfBSRights.to_csv(r"data\DataBS\rights\RIGHTS-BS-"+myCompany+".csv")
				#scrapping dividends
				#elif ca_type=='dividends':
					#specify the url
					ca_dividend_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=dividend&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					pageca_dividend_Bs = urllib.request.urlopen(ca_dividend_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_dividend_Bs = BeautifulSoup(pageca_dividend_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_dividend_Bs=soup_dividend_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_dividend_Bs=[]
					B_dividend_Bs=[]
					C_dividend_Bs=[]
					D_dividend_Bs=[]
					E_dividend_Bs=[]
					F_dividend_Bs=[]
					for row in right_div_dividend_Bs.findAll("tr"):
						cells_dividend_Bs = row.findAll('td')
						if len(cells_dividend_Bs)==6: #Only extract table body not heading
							A_dividend_Bs.append(cells_dividend_Bs[0].find(text=True))
							B_dividend_Bs.append(cells_dividend_Bs[1].find(text=True))
							C_dividend_Bs.append(cells_dividend_Bs[2].find(text=True))
							D_dividend_Bs.append(cells_dividend_Bs[3].find(text=True))
							E_dividend_Bs.append(cells_dividend_Bs[4].find(text=True))
							F_dividend_Bs.append(cells_dividend_Bs[5].find(text=True))
					dfBSDividends=pd.DataFrame(A_dividend_Bs,columns=['Announcement_Date'])
					dfBSDividends['PURPOSE']=B_dividend_Bs
					dfBSDividends['DIVIDEND_%']=C_dividend_Bs
					dfBSDividends['DIVIDEND_TYPE']=D_dividend_Bs
					dfBSDividends['EX_DIVIDEND_DATE']=E_dividend_Bs
					dfBSDividends['BOOK_CLOSURER_DATE']=F_dividend_Bs
					dfBSDividends.to_csv(r"data\DataBS\dividends\DIV-BS-"+myCompany+".csv")
				#scrapping Bonus
				#elif ca_type == 'bonus':
					ca_bonus_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=bonus&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_bonus_Bs = urllib.request.urlopen(ca_bonus_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_bonus_Bs = BeautifulSoup(page_bonus_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_bonus_Bs=soup_bonus_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_bonus_Bs=[]
					B_bonus_Bs=[]
					C_bonus_Bs=[]
					D_bonus_Bs=[]
					E_bonus_Bs=[]
					for row in right_div_bonus_Bs.findAll("tr"):
						cells_bonus_Bs = row.findAll('td')
						if len(cells_bonus_Bs)==5: #Only extract table body not heading
							A_bonus_Bs.append(cells_bonus_Bs[0].find(text=True))
							B_bonus_Bs.append(cells_bonus_Bs[1].find(text=True))
							C_bonus_Bs.append(cells_bonus_Bs[2].find(text=True))
							D_bonus_Bs.append(cells_bonus_Bs[3].find(text=True))
							E_bonus_Bs.append(cells_bonus_Bs[4].find(text=True))	
					dfBSBonus=pd.DataFrame(A_bonus_Bs,columns=['Announcement_Date'])
					dfBSBonus['PURPOSE']=B_bonus_Bs
					dfBSBonus['RECORD_DATE']=C_bonus_Bs
					dfBSBonus['EX_BONUS_DATE']=D_bonus_Bs
					dfBSBonus['Ratio']=E_bonus_Bs
					dfBSBonus.to_csv(r"data\DataBS\bonus\BONUS-BS-"+myCompany+".csv")
				#elif ca_type == 'splits':
					#specify the url
					ca_split_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=split&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_split_Bs = urllib.request.urlopen(ca_split_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_split_Bs = BeautifulSoup(page_split_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_split_Bs=soup_split_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_split_Bs=[]
					B_split_Bs=[]
					C_split_Bs=[]
					D_split_Bs=[]
					E_split_Bs=[]
					F_split_Bs=[]
					for row in right_div_split_Bs.findAll("tr"):
						cells_split_Bs = row.findAll('td')
						if len(cells_split_Bs)==6: #Only extract table body not heading
							A_split_Bs.append(cells_split_Bs[0].find(text=True))
							B_split_Bs.append(cells_split_Bs[1].find(text=True))
							C_split_Bs.append(cells_split_Bs[2].find(text=True))
							D_split_Bs.append(cells_split_Bs[3].find(text=True))
							E_split_Bs.append(cells_split_Bs[4].find(text=True))
							F_split_Bs.append(cells_split_Bs[5].find(text=True))
					dfBSSplits=pd.DataFrame(A_split_Bs,columns=['Announcement_Date'])
					dfBSSplits['PURPOSE']=B_split_Bs
					dfBSSplits['SPLIT_DATE_BSE']=C_split_Bs
					dfBSSplits['SPLIT_DATE_NSE']=D_split_Bs
					dfBSSplits['FROM']=E_split_Bs
					dfBSSplits['TO']=F_split_Bs
					dfBSSplits.to_csv(r"data\DataBS\splits\SPLITS-BS-"+myCompany+".csv")
				#elif ca_type == 'boardmeetings':
					#specify the url
					ca_board_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=board&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_board_Bs = urllib.request.urlopen(ca_board_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_board_Bs = BeautifulSoup(page_board_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_board_Bs=soup_board_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_board_Bs=[]
					B_board_Bs=[]
					C_board_Bs=[]
					for row in right_div_board_Bs.findAll("tr"):
						cells_board_Bs = row.findAll('td')
						if len(cells_board_Bs)==3: #Only extract table body not heading
							A_board_Bs.append(cells_board_Bs[0].find(text=True))
							B_board_Bs.append(cells_board_Bs[1].find(text=True))
							C_board_Bs.append(cells_board_Bs[2].find(text=True))
					dfBSBoardmeetings=pd.DataFrame(A_board_Bs,columns=['Announcement_Date'])
					dfBSBoardmeetings['PURPOSE']=B_board_Bs
					dfBSBoardmeetings['REMARKS']=C_board_Bs
					dfBSBoardmeetings.to_csv(r"data\DataBS\boardmeetings\BOARDMEETINGS-BS-"+myCompany+".csv")
				#scrapping AGM EGM BookClosure Others from BS at once
				#elif ca_type == 'aeb':	
					#specify the url
					ca_agm_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=agm&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_agm_Bs = urllib.request.urlopen(ca_agm_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_agm_Bs = BeautifulSoup(page_agm_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_agm_Bs=soup_agm_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_agm_Bs=[]
					B_agm_Bs=[]
					C_agm_Bs=[]
					D_agm_Bs=[]
					for row in right_div_agm_Bs.findAll("tr"):
						cells_agm_Bs = row.findAll('td')
						if len(cells_agm_Bs)==4: #Only extract table body not heading
							A_agm_Bs.append(cells_agm_Bs[0].find(text=True))
							B_agm_Bs.append(cells_agm_Bs[1].find(text=True))
							C_agm_Bs.append(cells_agm_Bs[2].find(text=True))
							D_agm_Bs.append(cells_agm_Bs[3].find(text=True))       
					dfBSAeb=pd.DataFrame(A_agm_Bs,columns=['Announcement_Date'])
					dfBSAeb['PURPOSE']=B_agm_Bs
					dfBSAeb['AGM_DATE']=C_agm_Bs
					dfBSAeb['REMARKS']=D_agm_Bs
					dfBSAeb.to_csv(r"data\DataBS\Agm\AEB-BS-"+myCompany+".csv")
					#specify the url
					ca_egm_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=egm&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_egm_Bs = urllib.request.urlopen(ca_egm_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_egm_Bs = BeautifulSoup(page_egm_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_egm_Bs=soup_egm_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_egm_Bs=[]
					B_egm_Bs=[]
					C_egm_Bs=[]
					D_egm_Bs=[]
					for row in right_div_egm_Bs.findAll("tr"):
						cells_egm_Bs = row.findAll('td')
						if len(cells_egm_Bs)==4: #Only extract table body not heading
							A_egm_Bs.append(cells_egm_Bs[0].find(text=True))
							B_egm_Bs.append(cells_egm_Bs[1].find(text=True))
							C_egm_Bs.append(cells_egm_Bs[2].find(text=True))
							D_egm_Bs.append(cells_egm_Bs[3].find(text=True))       
					dfBSaEb=pd.DataFrame(A_egm_Bs,columns=['Announcement_Date'])
					dfBSaEb['PURPOSE']=B_egm_Bs
					dfBSaEb['EGM_DATE']=C_egm_Bs
					dfBSaEb['REMARKS']=D_egm_Bs    
					dfBSaEb.to_csv(r"data\DataBS\egm\AEB-BS-"+myCompany+".csv")
					#specify the url
					ca_book_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=book&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="
					#Query the website and return the html to the variable 'page'
					page_book_Bs = urllib.request.urlopen(ca_book_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_book_Bs = BeautifulSoup(page_book_Bs,features="lxml")
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_book_Bs=soup_book_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_book_Bs=[]
					B_book_Bs=[]
					C_book_Bs=[]
					D_book_Bs=[]
					E_book_Bs=[]

					for row in right_div_book_Bs.findAll("tr"):
						cells_book_Bs = row.findAll('td')
						if len(cells_book_Bs)==5: #Only extract table body not heading
							A_book_Bs.append(cells_book_Bs[0].find(text=True))
							B_book_Bs.append(cells_book_Bs[1].find(text=True))
							C_book_Bs.append(cells_book_Bs[2].find(text=True))
							D_book_Bs.append(cells_book_Bs[3].find(text=True))
							E_book_Bs.append(cells_book_Bs[4].find(text=True))
							
					dfBSaeB=pd.DataFrame(A_book_Bs,columns=['Announcement_Date'])
					dfBSaeB['PURPOSE']=B_book_Bs
					dfBSaeB['FROM']=C_book_Bs
					dfBSaeB['TO']=D_book_Bs
					dfBSaeB['REMARKS']=E_book_Bs
					dfBSaeB.to_csv(r"data\DataBS\BookClosure\AEB-BS-"+myCompany+".csv")	
		
											#specify the url
					ca_others_Bs="https://www.business-standard.com/company/"+companyNameBScodeNew+"/corporate-action?purpose=others&fromDay=&fromMonth=&fromYear=&toDay=&toMonth=&toYear="

					#Query the website and return the html to the variable 'page'
					page_others_Bs = urllib.request.urlopen(ca_others_Bs)
					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					soup_others_Bs = BeautifulSoup(page_others_Bs,features="lxml")

					#Parse the html in the 'page' variable, and store it in Beautiful Soup format
					right_div_others_Bs=soup_others_Bs.find('div', class_='table table-BG-grey mT20')
					#Generate lists
					A_others_Bs=[]
					B_others_Bs=[]
					C_others_Bs=[]
					for row in right_div_others_Bs.findAll("tr"):
						cells_others_Bs = row.findAll('td')
						if len(cells_others_Bs)==3: #Only extract table body not heading
							A_others_Bs.append(cells_others_Bs[0].find(text=True))
							B_others_Bs.append(cells_others_Bs[1].find(text=True))
							C_others_Bs.append(cells_others_Bs[2].find(text=True))
					df=pd.DataFrame(A_others_Bs,columns=['Announcement_Date'])
					df['PURPOSE']=B_others_Bs
					df['REMARKS']=C_others_Bs	
					df.to_csv(r"data\DataBS\Others\AEB-BS-"+myCompany+".csv")
		dfd2 = pd.read_csv("data/DataMC/dividends/DIV-MC-"+myCompany+".csv")
		dfd1 = pd.read_csv("data/DataBS/dividends/DIV-BS-"+myCompany+".csv")
		df1dividends=dfd1.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0','PURPOSE','BOOK_CLOSURER_DATE'],level=None, inplace=False, errors='raise')
		df2Dropped=dfd2.drop(labels=None, axis=0, index=None, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		df2dividends=df2Dropped.rename(columns={"Announcement_Date": "Announcement_Date","Effective_Date":"EX_DIVIDEND_DATE", "Dividend_Type": "DIVIDEND_TYPE","Dividend":"DIVIDEND_%"})
		#bonus
		dfb2=pd.read_csv("data/DataMC/bonus/BONUS-MC-"+myCompany+".csv")
		dfb1=pd.read_csv("data/DataBS/bonus/BONUS-BS-"+myCompany+".csv")
		df1bonus=dfb1.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0','PURPOSE'], level=None, inplace=False, errors='raise')
		dfb2Dropped=dfb2.drop(labels=None, axis=0, index=None, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		df2bonus=dfb2Dropped.rename(columns={"Announcement_Date": "Announcement_Date","Bonus_Ratio":"Ratio", "Record_Date": "RECORD_DATE","Ex-Bonus_Date":"EX_BONUS_DATE"})
		#boardmeetings
		dfbm1=pd.read_csv("data/DataBS/boardmeetings/BOARDMEETINGS-BS-"+myCompany+".csv")
		dfbm2=pd.read_csv("data/DataMc/boardmeetings/BOARDMEETINGS-MC-"+myCompany+".csv")
		df1boardmeetings=dfbm1.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0','PURPOSE'], level=None, inplace=False, errors='raise')
		dfbm2Cleaned=dfbm2.drop(labels=None, axis=0, index=None, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		df2boardmeetings=dfbm2Cleaned.rename(columns={"Meeting_Date": "Announcement_Date","Remark":"REMARKS"})
		#splits
		dfs1=pd.read_csv("data/DataBS/splits/SPLITS-BS-"+myCompany+".csv")
		dfs2=pd.read_csv("data/DataMC/splits/SPLITS-MC-"+myCompany+".csv")
		dfs1Dropped=dfs1.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0','PURPOSE','SPLIT_DATE_BSE'], level=None, inplace=False, errors='raise')
		df2splits=dfs2.drop(labels=None, axis=0, index=None, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		df1splits=dfs1Dropped.rename(columns={"Announcement_Date": "Announcement_Date","SPLIT_DATE_NSE":"Ex-Split_Date","FROM":"Old_FV","TO":"New_FV"})
		#rights
		dfr1=pd.read_csv("data/DataBS/rights/RIGHTS-BS-"+myCompany+".csv")
		dfr2=pd.read_csv("data/DataMC/rights/RIGHTS-MC-"+myCompany+".csv")
		dfr1Dropped=dfr1.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0','PURPOSE'], level=None, inplace=False, errors='raise')
		df2rights=dfr2.drop(labels=None, axis=0, index=None, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		df1rights=dfr1Dropped.rename(columns={"Announcement_Date": "Announcement_Date","RECORD_DATE":"Record_Date","EX_BONUS_DATE":"Ex-Rights_Date","RATIO":"Rights_Ratio","PREMIUM":"Premium"})
		#aeb
		dfaeb1=pd.read_csv("data/DataMC/aeb/AEB-MC-"+myCompany+".csv")
		dfA2=pd.read_csv("data/DataBS/Agm/AEB-BS-"+myCompany+".csv")
		dfE2=pd.read_csv("data/DataBS/egm/AEB-BS-"+myCompany+".csv")
		dfB2=pd.read_csv("data/DataBS/bookclosure/AEB-BS-"+myCompany+".csv")
		dfO2=pd.read_csv("data/DataBS/Others/AEB-BS-"+myCompany+".csv")
		dfaeb1Dropped=dfaeb1.drop(labels=None, axis=0, index=None, columns=['Unnamed: 0'], level=None, inplace=False, errors='raise')
		dfA2Cleaned=dfA2.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		dfE2Cleaned=dfE2.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		dfB2Cleaned=dfB2.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		dfO2Cleaned=dfO2.drop(labels=None, axis=0, index=0, columns=['Unnamed: 0'] ,level=None, inplace=False, errors='raise')
		df1aeb=dfaeb1Dropped.rename(columns={"Announcement_Date": "Announcement_Date","Purpose":"PURPOSE","Remark":"REMARKS"})
		dfB2CleanedR=dfB2Cleaned.rename(columns={"Announcement_Date": "Announcement_Date","FROM":"Book_Closure_From","TO":"Book_Closure_To"})
		dfA2CleanedR=dfA2Cleaned.rename(columns={"AGM_DATE": "AnnualGenralMeeting_DATE"})
		frames=[dfA2CleanedR,dfE2Cleaned,dfB2CleanedR,dfO2Cleaned]
		#dfE2Cleaned
		df = pd.concat(frames)
		# sorting by first name 
		df['Announcement_Date'] =pd.to_datetime(df.Announcement_Date)
		df.sort_values(by='Announcement_Date',inplace = True)
		df2aeb=df.sort_index()
							
		return render_template('preview.html',df_view_aeb=df1aeb,df_view_aeb2=df2aeb,
			df_view_rights=df1rights,df_view_rights2=df2rights,
			df_view_splits=df1splits,df_view_splits2=df2splits,
			df_view_boardmeetings=df1boardmeetings,df_view_boardmeetings2=df2boardmeetings,
			df_view_bonus=df1bonus,df_view_bonus2=df2bonus,
			df_view_dividends=df1dividends,df_view_dividends2=df2dividends,myCompany=myCompany)
	#except:
	#	return render_template("404.html")
if __name__ == '__main__':
	app.run(debug=True)