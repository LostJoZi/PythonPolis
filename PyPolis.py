import time
import os
import textwrap

achievements = []

def vymazat_obrazovku():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_achievement(achievement):
    achievements.append(achievement)
    print("\n*** Achievement získán: {} ***\n".format(achievement))
    time.sleep(2)

def uvitaci_zprava():
    vymazat_obrazovku()
    print("Milý hráči, vítej v")
    print("")

    ascii_art = [
        " *******             **   **                        *******            ** **",
        "/**////**  **   **  /**  /**                       /**////**          /**//",
        "/**   /** //** **  ******/**       ******  ******* /**   /**  ******  /** **  ******",
        "/*******   //***  ///**/ /******  **////**//**///**/*******  **////** /**/** **//// ",
        "/**////     /**     /**  /**///**/**   /** /**  /**/**////  /**   /** /**/**//*****",
        "/**         **      /**  /**  /**/**   /** /**  /**/**      /**   /** /**/** /////**",
        "/**        **       //** /**  /**//******  ***  /**/**      //******  ***/** ****** ",
        "//        //         //  //   //  //////  ///   // //        //////  /// // //////",
        ""
    ]
    
    for line in ascii_art:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.001)
        print("")
        time.sleep(0.1)

    print("\n")
    input("Stiskni Enter pro pokračování...")

def herni_menu():
    while True:
        print("1. Hrát")
        print("2. Info o hře")
        print("3. Získané achievements")
        volba = input("Herní menu: ")

        if volba == "1":
            spustit_hru()
        elif volba == "2":
            info_o_hre()
        elif volba == "3":
            show_achievements()
        else:
            print("Neplatná volba, zkuste to znovu.")
        vymazat_obrazovku()
        uvitaci_zprava()

def show_achievements():
    vymazat_obrazovku()
    if achievements:
        print("Získané Achievements:")
        for achievement in achievements:
            print(f"- {achievement}")
    else:
        print("Zatím jsi nezískal žádné achievements.")
    input("Stiskni Enter pro návrat do menu...")

def spustit_hru():
    vymazat_obrazovku()
    print(textwrap.fill("Ještě jednou vítej! Tvoje jméno je Petr. Jsi bájný hrdina, který má za úkol vysvobodit USB kabel ze zajetí modré skříně. Ta je ale strážena Honzou, též nadějným bojovníkem.", width=80))
    input("Klikni Enter pro pokračování...")
    vymazat_obrazovku()
    print(textwrap.fill("Jakožto Petr máš v kapse několik věcí, které ti tvou cestu usnadní. Kromě všech možných kravin tam jsou 100% použitelné věci, jako generátor kávy, náhradní Windows, nebo LabVIEW, provaz, kostka molitanu a podobně.", width=80))
    input("Klikni Enter pro pokračování...")
    vymazat_obrazovku()
    print(textwrap.fill("Vysvoboď kabel z Honzovy skříně ještě dnes!", width=80))
    input("Klikni Enter pro pokračování...")
    vymazat_obrazovku()
    rozcestnik()

def info_o_hre():
    vymazat_obrazovku()
    print(textwrap.fill("Hra PythonPolis je textové dobrodružství, kde hráč řídí Petra, který se snaží vysvobodit USB kabel. Během hry se setká s různými výzvami a rozhodnutími, které ovlivňují průběh a konec hry.", width=80))
    print("Verze hry: 1.0")
    print("Více informací najdeš na www.github.com/LostJoZi/PythonPolis")
    input("Stiskni Enter pro návrat do menu...")
    vymazat_obrazovku()

def rozcestnik():
    vymazat_obrazovku()
    print("Začni své dobrodružství:")
    print("1. Vydat se na cestu k modré skříni")
    print("2. Nabrat sílu a odpočinout si")
    print("3. Vyjednat s Honzou odevzdání USB kabelu dobrovolně")
    print("4. Vyhledat pomoc u moudré čarodějnice.")
    print("5. Dát to prozatím dál. Jet na nákup do Makra.")
    volba = input("Zvol možnost (1-5): ")
    zpracuj_rozcestnik(volba)

def zpracuj_rozcestnik(volba):
    if volba == "1":
        cesta_k_modre_skrine()
    elif volba == "2":
        nabrat_silu()
    elif volba == "3":
        vyjednat_s_honzou()
        display_achievement("Mistr vyjednávač")
    elif volba == "4":
        vyhledat_lenku()
        display_achievement("Dobrodruh")
    elif volba == "5":
        makro_pribeh()
    elif volba == "6":
        secret_pribeh()
        display_achievement("Tajemství Polis")
    else:
        print("Neplatná volba! Zadej číslo možnosti od 1 do 4.")
        input("Stiskni Enter pro návrat do rozcestníku...")
        vymazat_obrazovku()
        rozcestnik()

def secret_pribeh():
    vymazat_obrazovku()
    print("  ********                                  **"),
    print(" **//////                                  /**  "),
    print("/**         *****   *****  ******  *****  ******"),
    print("/********* **///** **///**//**//* **///**///**/ "),
    print("////////**/*******/**  //  /** / /*******  /** "),
    print("       /**/**//// /**   ** /**   /**////   /**"),
    print(" ******** //******//***** /***   //******  //** "),
    print("////////   //////  /////  ///     //////    //"),
    print("")
    print(textwrap.fill("Nečetl jsi snad jasně? Máš zadat čísla 1, až 5! Upřímně. Myslím, že sis už užil dost. Nezbývá, než poděkovat."))
    input("Stiskni enter pro pokračování...")
    secret_konec()

def secret_konec():
    vymazat_obrazovku()
    print(" *******   ** **                                             **"),
    print("/**////** // /**      **   **                               /**"),
    print("/**    /** **/**  ** //** **    **********   ******   ***** /**"),
    print("/**    /**/**/** **   //***    //**//**//** **////** **///**/**"),
    print("/**    /**/**/****     /**      /** /** /**/**   /**/**  // /**"),
    print("/**    ** /**/**/**    **       /** /** /**/**   /**/**   **//"),
    print("/*******  /**/**//**  **        *** /** /**//****** //*****  **"),
    print("///////   // //  //  //        ///  //  //  //////   /////  // "),
    print("")
    print("V pozadí si představ písničku Díky moc od Wohnoutů :D")
    print("")
    print(textwrap.fill("Možná přemýšlíš, co teda bylo pravým smyslem této hry. Ukázat, jaký je Honza hlupák a jak se chová ke kabelům? Ne. Ukázat ti, jak správně se v životě rozhodovat? Proč se vlastně tahle hra jmenovala PythonPolis, když se o příběh města vůbec nejednalo?"))
    input("Stiskni enter pro pokračování...")
    print(textwrap.fill("Ještě, než ti prozradím pravý důvod, dovol mi, abych ti složil poděkování. Tím, že sis tuhle hru zahrál a dostal se až sem jsi dokázal, že máš inteligenci na levelu studenta Excelence 3. A to se celkem do života hodí. Ostatně, je také dost možné, že právě ty se jednoho krásného dne přidáš to týmu profesorů, abys mohl tento úžasný koníček, myšlěno programování, rozdávat dále. Ještě jednou moc díky."))
    input("Stiskni enter pro pokračování...")
    print(textwrap.fill("Tak. Jdeme na ten důvod. PythonPolis jsem vůbec nevymyslel tak, že jsem se o hodině informatiky fakt hodně nudil a vymášlel různé spojení slov. A pak mi to došlo. PYTHONPOLIS TU NENÍ OD TOHO, ABY TI DALA NĚJAKÝ ÚŽASNÝ HERNÍ ZÁŽITEK. KONEC KONCŮ SE JEDNÁ JEN O TEXT-BASED PŘÍBĚHOVKU, ALE TO, ŽE SI TEĎ MŮŽEŠ OTEVŘÍT CELÝ KÓD A MOŽNÁ TĚ TO MOTIVUJE K VYTVOŘENÍ NĚČEHO PODOBNÉHO A PŘEDÁNÍ TOHO DÁL. <3 To jest od autora opravdový konec."))
    input("Finálně stiskni Enter, rozluč se s PythonPolis a pohlédni do jejího kódu.")
    display_achievement("Díky moc")
    exit()

def cesta_k_modre_skrine():
    vymazat_obrazovku()
    print("Pokračuješ lesem a najednou si uvědomíš, že jsi se ztratil.")
    volba = input("Máš na výběr: 1 - Použít RealTime GPS LabVIEW Ultra Pro S Max Mini mapu ze své kapsy, 2 - Kašlat na to a jít dál bez mapy:")

    if volba == "1":
        print("Použil jsi RealTime GPS LabVIEW Ultra Pro S Max Mini Mapu a podle mapy dorazil k jeskyni, na které je vyryto 'A110'.")
        vstup_do_jeskyně()
    elif volba == "2":
        print("Rozhodl jsi se jít dál bez mapy, ale bohužel jsi se ještě více ztratil v temném lese. Musíš začít znovu.")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    else:
        print("Neplatná volba! Zkus to znovu.")
        return False  # Indikuje, že volba byla neplatná

def vstup_do_jeskyně():
    vymazat_obrazovku()
    print("Vítej v Honzově jeskyni! Vstoupil jsi dovnitř a na podlaze jsi spatřil lezoucí stonožku.")
    volba = input("Máš na výběr: 1 - Spočítat její nohy, 2 - Nechat stonožku být a pokračovat dál:")

    if volba == "1":
        print("Rozhodl jsi se spočítat nohy stonožky. Proč bys to dělal? Ty máš za úkol osvobodit kabel! Promiň, ale končíš.")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    elif volba == "2":
        print("Rozhodl jsi se nechat stonožku být. Pokračuj v dobrodružství dál.")
        odemknout_skříň()
    else:
        print("Neplatná volba! Zkus to znovu.")
        return False  # Indikuje, že volba byla neplatná

def nabrat_silu():
    vymazat_obrazovku()
    print("Vybral sis možnost 2: Nabrat sílu a odpočinout si. Chceš si to trochu urovnat v hlavě.")
    volba = input("Máš na výběr: 1 - Napsat Honzovi, 2 - Dál odpočívat:")
    if volba == "1":
        napsat_honzovi()
    elif volba == "2":
        print("Nemůžeš furt jen odpočívat! Takhle se kabel nevysvobodí...")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    else:
        print("Neplatná volba! Zkus to znovu.")
        nabrat_silu()

def napsat_honzovi():
    vymazat_obrazovku()
    print("Rozhodl jsi se napsat Honzovi.")
    volba = input("Máš na výběr: 1 - Počkat na odpověď, 2 - Pingnout ho:")
    if volba == "1":
        cekat_na_odpoved()
    elif volba == "2":
        print("PINGnul jsi Honzu. A to se nedělá.")
        input("Zkus to znovu. Stiskni enter..")
        exit()
    else:
        print("Neplatná volba! Zkus to znovu.")
        napsat_honzovi()

def cekat_na_odpoved():
    vymazat_obrazovku()
    print("Rozhodl jsi se počkat na odpověď od Honzy.")
    print("...")
    print("Po několika minutách Honza odepsal.")
    print("Kabel ti nikdy nedám!'")
    volba = input("Máš na výběr: 1 - Dej mi ho, fakt prosím, 2 - Dojdu si pro něj, i kdyby mě to mělo stát život, 3 - OK:")
    if volba == "1" or volba == "3":
        print("To není úplně správně. To si říkáš hrdina? Zkus to znovu.")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    elif volba == "2":
        print(textwrap.fill("Dobře. Líbí se mi, jak jsi sebevědomý. Tak tedy pojď do mého sídla! Budeš to muset vzít přes les. Možná mě tam uvidíš, možná ne."))
        time.sleep(5)
        cesta_lesem()
    else:
        print("Neplatná volba! Zkus to znovu.")
        cekat_na_odpoved()

def vyjednat_s_honzou():
    vymazat_obrazovku()
    print("Vybral sis možnost 3: Vyjednat s Honzou odevzdání USB kabelu dobrovolně.")
    print("...")
    print("Honza: Chceš vyjednávat? Přijď do mého tajného sídla.")
    volba = input("Máš na výběr: 1 - Cesta lesem, 2 - Přes hory, 3 - Jet přes přes Fugnerku (nebezpečná místa, ale zkratka):")
    if volba == "1":
        cesta_lesem()
    elif volba == "2":
        pres_hory()
        display_achievement("Průzkumník")
    elif volba == "3":
        nebezpecna_mista()
    else:
        print("Neplatná volba! Zkus to znovu.")
        vyjednat_s_honzou()

def nebezpecna_mista():
    vymazat_obrazovku()
    print("Rozhodl jsi se projet přes Fugnerku.")
    print("Cestou potkáš skupinu zvláštních figurín, které tě nuceně přesvědčují o kouzlech důchodcovského zpěvu.")
    print("Máš na výběr: 1 - Vyslechnout si píseň a riskovat ztrátu času, 2 - Ignorovat a pokračovat dál rychleji:")
    volba = input("Zvol možnost (1-2): ")
    if volba == "1":
        print("Vyslechneš si píseň. Je to tak dlouhé, že se stmívá, ale aspoň máš nové hudební zážitky. Nakonec se dostaneš k Honzovu sídlu později.")
    elif volba == "2":
        print("Ignoruješ a spěcháš dál. Tvůj odhodlaný postoj ti umožňuje rychlejší postup.")
    prijit_k_honzovi()

def cesta_lesem():
    vymazat_obrazovku()
    print("Vybral jsi cestu lesem.")
    cesta_k_modre_skrine()

def pres_hory():
    vymazat_obrazovku()
    print("Vybral jsi cestu přes hory.")
    print("Jdeš horami a vidíš most přes propast. Ten ti pomůže dostat se na druhou stranu. Má ale vadu. Lana onoho mostu jsou přetrhaná. Můžeš je ale opravit.")
    volba = input("Máš na výběr: 1 - Opravíš most lanem ze své kapsy, 2 - Zkusíš Svartajump:")
    if volba == "1":
        print("Rozhodl jsi se opravit most lanem ze své kapsy.")
        print("Podařilo se ti opravit most a bezpečně přejít na druhou stranu.")
        prijit_k_honzovi()
    elif volba == "2":
        print("Zkusil jsi Svartajump, ale bohužel to nevyšlo. Spadl jsi do propasti.")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    else:
        print("Neplatná volba! Zkus to znovu.")
        pres_hory()

def prijit_k_honzovi():
    vymazat_obrazovku()
    print("Najednou uvidíš Honzovo sídlo.")
    print("Honza: Tak jsi nakonec přišel? Hodně jsem o tom přemýšlel a rozhodl jsem se, že ho s tebou za něco vyměním.")
    print("Honza: Máš ještě flashku s náhradním LabVIEW? Instaloval jsem nový PC a tu instalačku už nemám. Dáš mi ji? Na oplátku ti vrátím kabel.")
    volba = input("Máš na výběr: 1 - Dát mu flashku z kapsy, 2 - Nedám ti ji! Stáhni si ji někde jinde, 3 - Nabídnout něco jiného jako výměnu: ")
    if volba == "1":
        print("Dáváš Honzovi flashku s náhradním LabVIEW.")
        print("Kabel je zachráněn. Honza následující den zemřel na instalaci LabVIEW.")
        time.sleep(2.5)
        konecna_zprava()
        return True
    elif volba == "2":
        print("Rozhodl jsi se Honzovi flashku nedat.")
        print("Honza: Tak to tedy nedopadlo podle mých plánů. Uvidíme se v boji!")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    elif volba == "3":
        print("Nabídl jsi Honzovi starou kazetu s hudebními hity 80. let jako nostalgickou výměnu.")
        print("Honza je překvapen, ale přijímá tuto netradiční nabídku a vrací ti kabel.")
        display_achievement("Mistr vyjednávače")
        konecna_zprava()
    else:
        print("Neplatná volba! Zkus to znovu.")
        return False

def vyhledat_lenku():
    vymazat_obrazovku()
    print("Vybral sis možnost 4: Vyhledat pomoc u moudré čarodějnice.")
    put_to_witch()

def put_to_witch():
    print("Kráčíš hlubokým lesem. Jdeš bažinou. Najednou dostaneš žízeň.")
    volba = input("Máš na výběr: 1 - Napij se ze šťávy pomeranče s příchutí citronu, 2 - Jdi dál bez pití:")
    if volba == "1":
        print("Napiješ se a cítíš se lépe.")
        time.sleep(3)
    elif volba == "2":
        print("Rozhodl jsi se nepít a cítíš rostoucí žízeň.")
        display_achievement("Vytrvalý žíznivec")
        time.sleep(3)
    vymazat_obrazovku()
    print("Dojdeš k chatce známé čarodějnice Lenky. Zaklepeš na dveře a po vyzvání vejdeš dovnitř. Lenka tě s radostí vítá a nabízí ti pomoc.")
    print("Říká, že Honzu je nejlepší něčím rozptýlit. V kapse máš rozbitý generátor kávy. Kvůli cestě v bažinách je ale rozbitý a potřebuje vyschnout.")
    print("Lenka navrhuje, že by se mohl vysušit v rýži, ale nemá žádnou doma.")
    volba = input("Máš na výběr: 1 - Vydat se za rýží, 2 - Vymyslet s Lenkou jinou možnost:")
    if volba == "1":
        find_rice()
    elif volba == "2":
        find_alternative_with_lenka()

def find_rice():
    vymazat_obrazovku()
    print("Rozhodl jsi se vydat za rýží. Lenka ti dává pokyny, kde ji můžeš najít.")
    print("Rozhodl jsi se vydat do města a v obchodě koupit rýži.")
    print("Dorazil jsi k obchodu, ale zjistil jsi, že nemáš žádné peníze.")
    choice = input("Prodáš kostku molitanu? Ano (1), Ne (2): ")
    if choice == "1":
        print("Prodal jsi molitan, koupil jsi rýži a jsi připraven pokračovat.")
        return_to_lenka_with_rice()
    else:
        print("Nemáš peníze, nemůžeš koupit rýži. Hra končí.")
        input("Stiskni Enter pro ukončení hry...")
        exit()

def return_to_lenka_with_rice():
    vymazat_obrazovku()
    print("S rýží se vracíš k Lence. Pomáhá ti generátor kávy vysušit.")
    print("Generátor kávy je funkční!")
    proceed_to_honza()

def find_alternative_with_lenka():
    vymazat_obrazovku()
    print("Rozhodl jsi se vymyslet s Lenkou jinou možnost.")
    print("Lenka si vzpomněla, že má ve sklepě starou sušičku, kterou můžete použít k opravě generátoru.")
    print("Sušička fungovala! Generátor kávy je znovu funkční.")
    proceed_to_honza()

def proceed_to_honza():
    vymazat_obrazovku()
    print("S opraveným generátorem kávy se vydáváš do Honzovy jeskyně.")
    print("Podařilo se ti vklouznout dovnitř a umístit generátor kávy.")
    print("Generátor začíná vyrábět kávu a naplňuje jeskyni. Honza je zaneprázdněný a nevšimne si tvé přítomnosti. Jamile teď otevře dveře dílny, zatopí ho to! Získal jsi čas na osvobození kabelu.")
    odemknout_skříň()

def steal_the_cable():
    print("Dorazil jsi do Honzovy jeskyně.")
    odemknout_skříň()

def odemknout_skříň():
    vymazat_obrazovku()
    print("Náhle uvidíš zamčenou skříň s počítačem. Počítač vypadá jako klíč k odemknutí skříně, ale má jeden problém - na sobě nemá žádný operační systém. Ty ale naštěstí ve své kapse máš flashku s náhradními operačními systémy.")
    volba = input("Máš na výběr: 1 - Nainstalovat náhradní Windows z flashky, 2 - Nainstalovat náhradní Linux z flashky:")

    if volba == "1":
        print("Rozhodl jsi se nainstalovat náhradní Windows z flashky. Jako vážně sis myslel, že by Honza ve svých systémech použil Windows? Ty jsi fakt naivní. No nic, končíš.")
        input("Stiskni Enter pro ukončení hry...")
        exit()
    elif volba == "2":
        print("Rozhodl jsi se nainstalovat náhradní Linux z flashky. Vypadá to, že to funguje.")
        display_achievement("Šifrař")
        konecna_zprava()
    else:
        print("Neplatná volba! Zkus to znovu.")
        return False

def makro_pribeh():
    vymazat_obrazovku()
    print("Mám na to času dost. Jedu si nakoupit do Makra.")
    print("Začneš si psát nákupní seznam: Maso, maso, maso, maso, maso, maso, maso, maso, maso, dietní hořčice.")
    print("Vyrážíš do Makra:")
    print("   ______")
    print(" /|_||_\\`.__")
    print("(   _    _ _\\")
    print("=`-(_)--(_)-'")
    time.sleep(5)
    vymazat_obrazovku()
    nakupni_dobrodruzstvi()

def nakupni_dobrodruzstvi():
    print("Jedeš do Makra...")
    print("Vcházíš dovnitř, vezmeš košík a přijedeš s vozíkem k pečivu.")
    volba = input("Dostaneš hlad. Sežereš tajně jeden rohlík? Ano (1), Ne (2): ")
    if volba == "1":
        print("Už sice hlad nemáš, ale všimla si tě bába v šíleně barevném letním tričku a klíčenkou TV Šlágr. (Česká verze kamerového špionážního systému)")
        print("Začne vřískat něco o zkažené mládeži. Přijde ochranka.")
        volba_utek = input("Máš 2 možnosti: Utéct jim, ale nákupní košík vzít sebou (1), Utéct jim, ale bez košíku (2): ")
        if volba_utek == "1":
            print("Jde to těžce, ale daří se ti kličkovat mezi důchodci a paletami se zbožím podprůměrné kvality.")
            print("Nakonec se ti podaří utéct i bez placení. A dokonce máš i maso.")
        elif volba_utek == "2":
            print("Rychle utíkáš a unikáš ochrance, ale bez nákupu.")
    elif volba == "2":
        print("Vydržím to domů: Projíždíš dál supermarketem a pokračuješ k pokladnám.")
        volba_pokladna = input("Máš na výběr: Použít pokladny s NPC lidmi (1), Použít samoobslužné pokladny (2), Utéct bez placení (3): ")
        if volba_pokladna == "1":
            print("Normálně zaplatíš a nakoupíš. Bylo to trochu dražší, než jsi čekal.")
        elif volba_pokladna == "2":
            print("Jejda, samoobslužné pokladny jsou obsazené důchodci a strašně jim to trvá.")
        elif volba_pokladna == "3":
            print("Utekl jsi z Makra bez placení. To dopadne špatně.")
    konecna_faze()

def konecna_faze():
    print("Tak. Úspěšně jsi nakoupil a přežil.")
    volba = input("Teď si vyber, co s nákupem uděláš: Uvařit baštu pro oddíl (1), uspořádat Party pro celou TULku (2), Všechno zbaštit (3): ")
    if volba == "1":
        print("Rozhodl jsi se jet na svou skautskou klubovnu. Uvařil jsi delikátní baštu. Dokonale jsi nakrmil skautský oddíl.")
    elif volba == "2":
        print("Přijel jsi odpoledne na TULku. Chystáš gigantickou párty.")
        volba_gril = input("Zapomněl sis doma gril. Máš 2 možnosti: Stavit se pro něj domů (1), Sestrojit gril z transformátoru a LEGO Mindstorms (2): ")
        if volba_gril == "1":
            print("Vyzvedl sis doma svůj balkónový gril. Pokračuješ.")
        elif volba_gril == "2":
            print("Sestrojil jsi geniální gril. Nevíme, jak dlouho vydrží, ale funguje.")
    elif volba == "3":
        print("Rozhodl jsi se všechno sníst. Následující den jsi odpálil záchod.")
        time.sleep(5)
    konecna_zprava()

def konecna_zprava():
    vymazat_obrazovku()

    print("   ********                     **            **            ** **   **")
    print("  **//////**                   /**           /**           // //   /**")
    print(" **      //  ******  ******   ****** **   ** /** **   **    ** **  /**")
    print("/**         //**//* //////** ///**/ /**  /** /**/**  /**   /**/**  /**")
    print("/**    ***** /** /   *******   /**  /**  /** /**/**  /**   /**/**  /**")
    print("//**  ////** /**    **////**   /**  /**  /** /**/**  /** **/**/**  // ")
    print(" //******** /***   //********  //** //****** ***//******//*** /**   **")
    print("  ////////  ///     ////////    //   ////// ///  //////  ///  //   // ")
    print("")
    print("Podařilo se ti dokončit jeden z konců!")
    print("Je to velmi ohromující. Tento velký úspěch jsi oslavil Pizzou podle pejska a kočičky.")
    input("Stisknutím Enteru se vrať do menu a zkus si jiný konec :)")
    vymazat_obrazovku()
    uvitaci_zprava()
    
# Volání funkcí

uvitaci_zprava()
herni_menu()
rozcestnik()

volba_validni = False
while not volba_validni:
    volba = input("Zvol možnost (1-4): ")
    volba_validni = zpracuj_rozcestnik(volba)
