from Crypto.Util.number import *

c1 = 100776616618807028967089219449265405071201136149888325503066976161385989280095043995479704654682317351096497342938505283042432267709317726426539632743334442675055923303474260441968484038930475510547243408944979760077047844226093364211037167226135498952107848076477961767429609695798154764534296070676826481789984471071997068649531460720329432528404712498228353590265694478783802152324478513635349982749298190544059243245694817419642808779310834461588833985961398652162479862083492029475724652725823631724412465424885428393207046785329738152473132861059808030651760372742716834485469258739404405368896924250402606552678013205678223667552410900179333996030468982478180240097513760285000826494781027190623494276934337014320152318485437966386440371695603892681695876138924455442971906418145061033300829161099438856632988078053927084223982774030449146778669537591823820044297770134792912341260127034284530661825103241525373195686890475621436401458474734561997666364455549176209584571676374100850012143999073406972211417126921878045170120865041723071908531200545009281484984466062376436062994216908391649170412014362194389999219602959030582939905894808029928879604285955704644379450940562185436197864894767861347748667197143861753352777019
c2 = 235008810074005549856654004592701056849037147914410589495126335361512423615719290820758861786340805470070747985027984994111780662995458198624971596443198125867281055664089532704381037910132407368723825385305767149465589239575303817853556320278758359177026377037233810513301001496075482581619021516460163440435488033578453462667851174473017691909941130499527662657030979499200554653385269345495025688497001202215310144568739181292522753449340768918870579062521723378818011901450491817388924494928553609396663775658980249620952619241933661156606422162079538547450077237826164265412729757362938072491573267501636079691861108306680319685844265503234338740348591605243428899674318280013687917231856374074571604649294944698983751136135283834485554132519042593928778758706264942193011114591246225666712637357663428675827823000495295447140236053827028811295946995960711448639648196591801574650490590163776149584000458101462962244850898210258454886309068403424576889658710930330450851126257254033523447742918196481005924830498786753543816054714946258027056448398040103791619713585803347163588906496256888829576271741215446245287050223325018892813864912852520694221232727284720800841829367927041023920895013093757187640791725761259411211125966
c = 247814735586006746976223291660861541476740593115519763800538673473511734778564476398392732274683462269786498212849513837812402283828188579739789423342926455856829574949948115146622407497296348358212104597489343923011087705493704192288365628135370378532581335608097582274013252390063946320426212597719692341370750742414656158901755447802694279682458880991412254858976945733648898929267131575853410677316489223405340426758662780526115117975246811865609359569030460320668816997844506015411377582243416295490969013257607457965002906035840002388353338798762838287015942712207311914160302690606027766025659187088036000738215295680033260510504064554689966894352136023190867448829414762447860339831999736892220134868714982725422959504812307048882794024795551385990978284987729868301538947729695076168941674923713848290879229366987513958604693744760275765390565646300162133615336186917752671003640138233890153242621084731966288412262668444942249416480099925445129631313667831761824291038740510589831347633635769438463262003324444284282648950529606002219062618648307350203134651047244422601455845053107520932656554986625725338496505174761708038971092110176787007726828621382698136873898926589430670083350781674367950037096734269021655415627393
n = 511343494439105633094671320561148541729860613390466176578495862502776943297652918344581473567929791753108858472599204080675941782430314624688301865738767660170555284323321610241741247662258001210922817418698236472866120242310019443542131408591046181279120895577052002307473794468894741887592784143099397729967248961010667395133464171254369801423129610314673429427353216702865155602679669008793784650552636881116435823965996102139489906990579969031922295883497326449945755673205134657722667577304259463951525615885776705877494102162146999746242237151771476622454230654113014278482194972049472860824486633506888059694234954536919709706893655293245206367659248054474759508237474988507027643488463872439600608345099830316917770366267294158747910098207321342878197111826825495516968290403253307801597475487965878054074535724528498925512631860848038290580970365243024349490826462278999500991099997222615700528296127705613969495934980111167429157244320447536621371616696128844393939655143088165841906489060390684066256871541827751283460072661768979847781514838888060796495981513265447851401934692630171882400550838237875104400737330698337876946208972469031692685123889638852027904248354922135733001780236324162027601878136532090225465315871
e1=651245335468721456874632716543564189756724
e2=312564687351120557683216874563168735762335
'''
output1=pow((p-2*q),coef1,n)
output2=pow((p+3*q),coef2,n)
eq1 = (806892+46899725093250350043148792960985514831721955480204070411**(p-1)*(q-1)) % n

Modular binomial
'''
q=GCD(n, pow(c1, e2, n)*pow(3,e1*e2,n) - pow(c2, e1, n)*pow(2,e1*e2,n))
p=n//q
phi = (p-1)*(q-1)
l=46899725093250350043148792960985514831721955480204070411
e =pow(l,phi,n) + 806892
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))