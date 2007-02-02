# NOTE
# - difference between kdemodule-i18n and kde-i18n is that one is per
#   package and other is per language.
# TODO:
# - tons of unpackaged files (see end of install section for more)
#   http://glen.alkohol.ee/pld/kdemodule-i18n-3.5.5_3.txt
#
%define		_name			kde-i18n
%define		kdeaddons_epoch		1
%define		kdeadmin_epoch		8
%define		kdeartwork_epoch	8
%define		kdebase_epoch		9
%define		kdeedu_epoch		8
%define		kdegames_epoch		8
%define		kdegraphics_epoch	9
%define		kdelibs_epoch		9
%define		kdemultimedia_epoch	9
%define		kdenetwork_epoch	10
%define		kdepim_epoch		9
%define		kdesdk_epoch		3
%define		kdetoys_epoch		9
%define		kdeutils_epoch		9
%define		kdevelop_epoch		7
%define		kdevelop_version	3.3.5
%define		kdewebdev_epoch		2
#
Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu jêzyków
Name:		kdemodule-i18n
Version:	3.5.6
Release:	1
Epoch:		10
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-af-%{version}.tar.bz2
# Source0-md5:	7771bdb76b76323a68da4700bd5eaf26
Source1:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ar-%{version}.tar.bz2
# Source1-md5:	e79ef203dfc9196ea75089dfcd99339d
Source2:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-az-%{version}.tar.bz2
# Source2-md5:	416e628f6c3d27a334d26f1c5bd83406
Source3:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-bg-%{version}.tar.bz2
# Source3-md5:	a34d5e307d418fc87bcbb6ab150bc046
Source4:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-bn-%{version}.tar.bz2
# Source4-md5:	f5153ad329e8d7305aefa12f7ddfdfa3
Source5:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-br-%{version}.tar.bz2
# Source5-md5:	5c4ae705596f83ac2ee5df83a7900e5b
Source6:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-bs-%{version}.tar.bz2
# Source6-md5:	df40c6f49ebbc00155eea55f913d1600
Source7:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ca-%{version}.tar.bz2
# Source7-md5:	84b3a011b9d594ce26fdee77cccdfb52
Source8:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-cs-%{version}.tar.bz2
# Source8-md5:	b2dab45ea572efbb2569781211c2a7fc
Source9:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-cy-%{version}.tar.bz2
# Source9-md5:	3d3ddcd729b5ade752b498a42aeac39c
Source10:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-da-%{version}.tar.bz2
# Source10-md5:	913550e6604b9423cea605d95a8a664f
Source11:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-de-%{version}.tar.bz2
# Source11-md5:	c8a52e825c610ae5779ef84d1bf7e3c5
Source12:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-el-%{version}.tar.bz2
# Source12-md5:	f395db170010c2a4ee9a7e27b1c8772e
Source13:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-en_GB-%{version}.tar.bz2
# Source13-md5:	6b81bfa733c5e1c8ae4d16208093f648
Source14:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-eo-%{version}.tar.bz2
# Source14-md5:	7f17faa2bda08f31e1f33a3242f0b960
Source15:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-es-%{version}.tar.bz2
# Source15-md5:	75f2b236131bcf89b6f2302c1fb8780f
Source16:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-et-%{version}.tar.bz2
# Source16-md5:	55647fdaf91b9626618015017be954b4
Source17:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-eu-%{version}.tar.bz2
# Source17-md5:	6413e62d868721be5b269e50e979d4b1
Source18:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-fa-%{version}.tar.bz2
# Source18-md5:	be881e4b7be80e289b9dcdf00753ce79
Source19:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-fi-%{version}.tar.bz2
# Source19-md5:	227d47ad0232daf190653b4f8d9cd508
Source20:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-fr-%{version}.tar.bz2
# Source20-md5:	f700524f68cf6d34770784c69f9cc293
Source21:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-fy-%{version}.tar.bz2
# Source21-md5:	f69c07af129e084a4166cdfb3e5db173
Source22:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ga-%{version}.tar.bz2
# Source22-md5:	0ffdca99a102c4e1320916de3bf35adb
Source23:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-gl-%{version}.tar.bz2
# Source23-md5:	590bd015071b21ba0dcd55fc2955ca55
Source24:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-he-%{version}.tar.bz2
# Source24-md5:	b416073a3503a01056e14107fc797dae
Source25:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-hi-%{version}.tar.bz2
# Source25-md5:	25f0b08c99c952f443f32a86d5d4d4ad
Source26:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-hr-%{version}.tar.bz2
# Source26-md5:	99a94e8fc1fcdf1837f7030760c3deeb
Source27:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-hu-%{version}.tar.bz2
# Source27-md5:	575734a98fa2984f47adb49d6c023cc0
Source28:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-is-%{version}.tar.bz2
# Source28-md5:	f41752647ef59cb9fd179e2e1f77738c
Source29:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-it-%{version}.tar.bz2
# Source29-md5:	3a9bea48fb5ac7d3703abfdaa8a50c3c
Source30:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ja-%{version}.tar.bz2
# Source30-md5:	79b62e00ae4bbcc0d874588ccba177be
Source31:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-kk-%{version}.tar.bz2
# Source31-md5:	f878ce771f32ea800c285e5a813b17e7
Source32:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-km-%{version}.tar.bz2
# Source32-md5:	2f83f915e5ee4932ce8c7f26abb8b542
Source33:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ko-%{version}.tar.bz2
# Source33-md5:	eb47d4c6f46c161835c5255f399e1ac9
Source34:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-lt-%{version}.tar.bz2
# Source34-md5:	2769c90376add2e49addcaa2f39df577
Source35:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-lv-%{version}.tar.bz2
# Source35-md5:	c3f7cca71708d2894510bdd30b264bff
Source36:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-mk-%{version}.tar.bz2
# Source36-md5:	2e374c32eb02a6421b2076ac305926a2
Source37:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-mn-%{version}.tar.bz2
# Source37-md5:	7158b53fec42b7ed43525bacfa57e0e4
Source38:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ms-%{version}.tar.bz2
# Source38-md5:	edeaa43311fc0935d0a5b79b5db8f39e
Source39:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-nb-%{version}.tar.bz2
# Source39-md5:	bf087b3c116770dcffa008da74e767e2
Source40:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-nds-%{version}.tar.bz2
# Source40-md5:	a12623e0d68f3737447b663e070e3f61
Source41:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-nl-%{version}.tar.bz2
# Source41-md5:	6f4eea25839984463e70d1c635813a11
Source42:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-nn-%{version}.tar.bz2
# Source42-md5:	9dc810b75c2cb7c864ec5bf82a2bed2f
Source43:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-pa-%{version}.tar.bz2
# Source43-md5:	6a9be2176930ceb07600913cbee525e3
Source44:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-pl-%{version}.tar.bz2
# Source44-md5:	71852ce8f2549cfc19ffe71468a82349
Source45:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-pt-%{version}.tar.bz2
# Source45-md5:	ee8322ab521d796fbfafef471d845d6d
Source46:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-pt_BR-%{version}.tar.bz2
# Source46-md5:	29836d3d914f41a2cab1567d1df6feff
Source47:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ro-%{version}.tar.bz2
# Source47-md5:	af2fc2dbc745614c7286a430a7874a54
Source48:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ru-%{version}.tar.bz2
# Source48-md5:	348d72dfa83d51cbb65f6c7e964d64b3
Source49:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-rw-%{version}.tar.bz2
# Source49-md5:	8d07d207bb2e933a7b0130e593313842
Source50:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-se-%{version}.tar.bz2
# Source50-md5:	11d5888678814a442589c995d6307cd8
Source51:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-sk-%{version}.tar.bz2
# Source51-md5:	3a7b1b8bd44c92713d5e4db52655915b
Source52:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-sl-%{version}.tar.bz2
# Source52-md5:	2064f33c3f76ee60ddf1aef010d92399
Source53:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-sr-%{version}.tar.bz2
# Source53-md5:	e38ff9abe6f68bc69e0df5891e7bce69
Source54:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-sr@Latn-%{version}.tar.bz2
# Source54-md5:	9dcf67d0837f8ad2448d07c3ba3d5015
Source55:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ss-%{version}.tar.bz2
# Source55-md5:	7ecd86abba7c02c73b248ba5452c4bed
Source56:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-sv-%{version}.tar.bz2
# Source56-md5:	a826fb26b9378b12dae31b15ac22d995
Source57:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-ta-%{version}.tar.bz2
# Source57-md5:	11da7704ec348481c392cfd47af85caa
Source58:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-tg-%{version}.tar.bz2
# Source58-md5:	33f3b735e9cbd8a736146dae8a764d06
Source59:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-tr-%{version}.tar.bz2
# Source59-md5:	b56062b9908ecb6909bc4a7e4c4bb62a
Source60:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-uk-%{version}.tar.bz2
# Source60-md5:	82f0f3f3567d551307c03ebad12f3a1c
Source61:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-uz-%{version}.tar.bz2
# Source61-md5:	2208bb14ae419e20f2179d586ba49ff5
Source62:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-vi-%{version}.tar.bz2
# Source62-md5:	58602a074a5868b3c1ae299080289d9a
Source63:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-zh_CN-%{version}.tar.bz2
# Source63-md5:	a74fb6fee6d36a8bd975bb7b1b97fb4c
Source64:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{_name}-zh_TW-%{version}.tar.bz2
# Source64-md5:	f6211661d09cf7dcc381147d084537a7
URL:		http://i18n.kde.org/
BuildRequires:	kdelibs-devel >= %{kdelibs_epoch}:%{version}
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - international support.

%description -l pl
KDE - wsparcie dla wielu jêzyków.

%package -n kdelibs-i18n
Summary:	Internationalization and localization files for kdelibs
Summary(pl):	Pliki umiêdzynarodawiaj±ce kdelibs
Group:		X11/Libraries
Requires:	kdelibs = %{kdelibs_epoch}:%{version}
Obsoletes:	kde-i18n
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Basque
Obsoletes:	kde-i18n-Bengali
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Farsi
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Galician
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Low_Saxon
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Punjabi
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tajik
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Upper_Sorbian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kdeaccessibility-i18n
Obsoletes:	kdeaddons-i18n
Obsoletes:	kdeaddons-kvim-i18n
Obsoletes:	kdeadmin-i18n
Obsoletes:	kdeartwork-i18n
Obsoletes:	kdebase-mailnews-i18n
Obsoletes:	kdeedu-flashkard-i18n
Obsoletes:	kdeedu-i18n
Obsoletes:	kdeedu-kmessedwords-i18n
Obsoletes:	kdegraphics-i18n
Obsoletes:	kdemultimedia-i18n
Obsoletes:	kdenetwork-i18n
Obsoletes:	kdenetwork-rss-i18n
Obsoletes:	kdesdk-i18n
Obsoletes:	kdetoys-i18n
Obsoletes:	kdeutils-i18n

%description -n kdelibs-i18n
Translations and localization data for KDE libraries.

%description -n kdelibs-i18n -l pl
T³umaczenia i dane miêdzynarodowe dla bibliotek KDE.

%package -n kdebase-core-i18n
Summary:	Internationalization and localization files for the core part of KDE
Summary(pl):	T³umaczenia dla podstawowej czê¶ci KDE
Group:		X11/Applications
Requires:	kdebase-core = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-common-filemanagement-i18n

%description -n kdebase-core-i18n
Internationalization and localization files for KDE:
- Control Center;
- Help Center;
- Print System;
- Crash Handlers;
- A Frontend for "su" program.

%description -n kdebase-core-i18n -l pl
T³umaczenia dla podstawowej czê¶ci KDE, obejmuj±cej m.in.:
- Centrum sterownika
- Centrum pomocy
- System wydruków
- Obs³ugê b³êdów
- frontend dla programu "su".

%package -n kdebase-desktop-i18n
Summary:	Internationalization and localization files for the desktop part of KDE
Summary(pl):	T³umaczenia dla desktopowej czê¶ci KDE
Group:		X11/Applications
Requires:	kdebase-desktop = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kfind-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kjobviewer-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kpager-i18n = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kde-decoration-b2-i18n
Obsoletes:	kde-decoration-cde-i18n
Obsoletes:	kde-decoration-glow-i18n
Obsoletes:	kde-decoration-icewm-i18n
Obsoletes:	kde-decoration-kde1-i18n
Obsoletes:	kde-decoration-kstep-i18n
Obsoletes:	kde-decoration-modernsys-i18n
Obsoletes:	kde-decoration-openlook-i18n
Obsoletes:	kde-decoration-plastik-i18n
Obsoletes:	kde-decoration-quartz-i18n
Obsoletes:	kde-decoration-riscos-i18n
Obsoletes:	kde-decoration-system-i18n
Obsoletes:	kde-style-plastik-i18n
Obsoletes:	kdebase-kicker-i18n
Obsoletes:	kdebase-kmenuedit-i18n
Obsoletes:	kdebase-ksystraycmd-i18n

%description -n kdebase-desktop-i18n
Internationalization and localization files for KDE:
- desktop
- panel
- splashscreen system
- window manager

%description -n kdebase-desktop-i18n -l pl
T³umaczenia dla desktopowej czê¶ci KDE, obejmuj±cej:
- pulpit
- panel
- system splashscreenów
- zarz±dcê okien.

%package -n kdebase-infocenter-i18n
Summary:	Internationalization and localization files for KDE Information Centre
Summary(pl):	T³umaczenia dla centrum informacji o systemie w KDE
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-infocenter = %{kdebase_epoch}:%{version}

%description -n kdebase-infocenter-i18n
Internationalization and localization files for KDE Information
Centre.

%description -n kdebase-infocenter-i18n -l pl
T³umaczenia dla centrum informacji o systemie w KDE.

%package -n kdebase-kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl):	T³umaczenia dla kate
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kate = %{kdebase_epoch}:%{version}

%description -n kdebase-kate-i18n
Internationalization and localization files for kate.

%description -n kdebase-kate-i18n -l pl
T³umaczenia dla kate.

%package -n kdebase-kfind-i18n
Summary:	Internationalization and localization files for kfind
Summary(pl):	T³umaczenia dla kfind
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kfind = %{kdebase_epoch}:%{version}

%description -n kdebase-kfind-i18n
Internationalization and localization files for kfind.

%description -n kdebase-kfind-i18n -l pl
T³umaczenia dla kfind.

%package -n kdebase-kfontinst-i18n
Summary:	Internationalization and localization files for kfontinst
Summary(pl):	T³umaczenia dla kfontinst
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kfontinst = %{kdebase_epoch}:%{version}

%description -n kdebase-kfontinst-i18n
Internationalization and localization files for kfontinst.

%description -n kdebase-kfontinst-i18n -l pl
T³umaczenia dla kfontinst.

%package -n kdebase-klipper-i18n
Summary:	Internationalization and localization files for klipper
Summary(pl):	T³umaczenia dla klippera
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-klipper = %{kdebase_epoch}:%{version}

%description -n kdebase-klipper-i18n
Internationalization and localization files for klipper.

%description -n kdebase-klipper-i18n -l pl
T³umaczenia dla klippera.

%package -n kdebase-konsole-i18n
Summary:	Internationalization and localization files for konsole
Summary(pl):	T³umaczenia dla konsole
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-konsole = %{kdebase_epoch}:%{version}

%description -n kdebase-konsole-i18n
Internationalization and localization files for konsole.

%description -n kdebase-konsole-i18n -l pl
T³umaczenia dla konsole.

%package -n kdebase-kpager-i18n
Summary:	Internationalization and localization files for kpager
Summary(pl):	T³umaczenia dla kpagera
Group:		X11/Applications
Requires:	kdebase-kpager = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kpager-i18n
Internationalization and localization files for kpager.

%description -n kdebase-kpager-i18n -l pl
T³umaczenia dla kpagera.

%package -n kdebase-ksysguard-i18n
Summary:	Internationalization and localization files for ksysguard
Summary(pl):	T³umaczenia dla ksysguarda
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-klipper-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-ksysguard = %{kdebase_epoch}:%{version}

%description -n kdebase-ksysguard-i18n
Internationalization and localization files for ksysguard.

%description -n kdebase-ksysguard-i18n -l pl
T³umaczenia dla ksysguarda.

%package -n kdebase-kwrite-i18n
Summary:	Internationalization and localization files for kwrite
Summary(pl):	T³umaczenia dla kwrite
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kwrite = %{kdebase_epoch}:%{version}

%description -n kdebase-kwrite-i18n
Internationalization and localization files for kwrite.

%description -n kdebase-kwrite-i18n -l pl
T³umaczenia dla kwrite.

%package -n kdebase-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	T³umaczenia dla screensavers
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-screensavers = %{kdebase_epoch}:%{version}

%description -n kdebase-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdebase-screensavers-i18n -l pl
T³umaczenia dla screensavers.

%package -n kdm-i18n
Summary:	Internationalization and localization files for kdm
Summary(pl):	T³umaczenia dla kdm-a
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdm = %{kdebase_epoch}:%{version}

%description -n kdm-i18n
Internationalization and localization files for kdm.

%description -n kdm-i18n -l pl
T³umaczenia dla kdm-a.

%package -n konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl):	T³umaczenia dla konquerora
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-konsole-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror = %{kdebase_epoch}:%{version}
Requires:	konqueror-libs-i18n = %{epoch}:%{version}-%{release}

%description -n konqueror-i18n
Internationalization and localization files for konqueror.

%description -n konqueror-i18n -l pl
T³umaczenia dla konquerora.

%package -n kde-decoration-b2-i18n
Summary:	Internationalization and localization files for kde-decoration-b2
Summary(pl):	T³umaczenia dla kde-decoration-b2
Group:		X11/Applications
Requires:	kde-decoration-b2 = %{kdebase_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-b2-i18n
Internationalization and localization files for kde-decoration-b2.

%description -n kde-decoration-b2-i18n -l pl
T³umaczenia dla kde-decoration-b2.

%package -n kde-decoration-modernsys-i18n
Summary:	Internationalization and localization files for kde-decoration-modernsys
Summary(pl):	T³umaczenia dla kde-decoration-modernsys
Group:		X11/Applications
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-modernsys = %{kdebase_epoch}:%{version}

%description -n kde-decoration-modernsys-i18n
Internationalization and localization files for
kde-decoration-modernsys.

%description -n kde-decoration-modernsys-i18n -l pl
T³umaczenia dla kde-decoration-modernsys.

%package -n kde-decoration-quartz-i18n
Summary:	Internationalization and localization files for kde-decoration-quartz
Summary(pl):	T³umaczenia dla kde-decoration-quartz
Group:		X11/Applications
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-quartz = %{kdebase_epoch}:%{version}

%description -n kde-decoration-quartz-i18n
Internationalization and localization files for kde-decoration-quartz.

%description -n kde-decoration-quartz-i18n -l pl
T³umaczenia dla kde-decoration-quartz.

%package -n kdebase-desktop-libs-i18n
Summary:	Internationalization and localization files for desktop-libs
Summary(pl):	T³umaczenia dla desktop-libs
Group:		X11/Applications
Requires:	kdebase-desktop-libs = %{kdebase_epoch}:%{version}
Obsoletes:	kdebase-kicker-libs-i18n

%description -n kdebase-desktop-libs-i18n
Internationalization and localization files for desktop-libs.

%description -n kdebase-desktop-libs-i18n -l pl
T³umaczenia dla desktop-libs.

%package -n kdebase-kappfinder-i18n
Summary:	Internationalization and localization files for kappfinder
Summary(pl):	T³umaczenia dla kappfindera
Group:		X11/Applications
Requires:	kdebase-kappfinder = %{kdebase_epoch}:%{version}

%description -n kdebase-kappfinder-i18n
Internationalization and localization files for kappfinder.

%description -n kdebase-kappfinder-i18n -l pl
T³umaczenia dla kappfindera.

%package -n kdebase-kdcop-i18n
Summary:	Internationalization and localization files for kdcop
Summary(pl):	T³umaczenia dla kdcopa
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kdcop = %{kdebase_epoch}:%{version}

%description -n kdebase-kdcop-i18n
Internationalization and localization files for kdcop.

%description -n kdebase-kdcop-i18n -l pl
T³umaczenia dla kdcopa.

%package -n kdebase-kdeprintfax-i18n
Summary:	Internationalization and localization files for kdeprintfax
Summary(pl):	T³umaczenia dla kdeprintfax
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kdeprintfax = %{kdebase_epoch}:%{version}

%description -n kdebase-kdeprintfax-i18n
Internationalization and localization files for kdeprintfax.

%description -n kdebase-kdeprintfax-i18n -l pl
T³umaczenia dla kdeprintfax.

%package -n kdebase-kdialog-i18n
Summary:	Internationalization and localization files for kdialog
Summary(pl):	T³umaczenia dla kdialoga
Group:		X11/Applications
Requires:	kdebase-kdialog = %{kdebase_epoch}:%{version}

%description -n kdebase-kdialog-i18n
Internationalization and localization files for kdialog.

%description -n kdebase-kdialog-i18n -l pl
T³umaczenia dla kdialoga.

%package -n kdebase-kjobviewer-i18n
Summary:	Internationalization and localization files for kjobviewer
Summary(pl):	T³umaczenia dla kjobviewera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kjobviewer = %{kdebase_epoch}:%{version}

%description -n kdebase-kjobviewer-i18n
Internationalization and localization files for kjobviewer.

%description -n kdebase-kjobviewer-i18n -l pl
T³umaczenia dla kjobviewera.

%package -n kdebase-kpersonalizer-i18n
Summary:	Internationalization and localization files for kpersonalizer
Summary(pl):	T³umaczenia dla kpersonalizera
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kpersonalizer = %{kdebase_epoch}:%{version}

%description -n kdebase-kpersonalizer-i18n
Internationalization and localization files for kpersonalizer.

%description -n kdebase-kpersonalizer-i18n -l pl
T³umaczenia dla kpersonalizera.

%package -n konqueror-libs-i18n
Summary:	Internationalization and localization files for libkonq
Summary(pl):	T³umaczenia dla libkonq
Group:		X11/Applications
Requires:	konqueror-libs = %{kdebase_epoch}:%{version}
Obsoletes:	kdebase-libkonq-i18n

%description -n konqueror-libs-i18n
Internationalization and localization files for libkonq.

%description -n konqueror-libs-i18n -l pl
T³umaczenia dla libkonq.

%package -n kde-kio-ldap-i18n
Summary:	Internationalization and localization files for ldap ioslave
Summary(pl):	T³umaczenia dla ldap ioslave
Group:		X11/Applications
Requires:	kde-kio-ldap = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	konqueror-i18n < %{epoch}:%{version}-%{release}

%description -n kde-kio-ldap-i18n
Internationalization and localization files for ldap ioslave.

%description -n kde-kio-ldap-i18n -l pl
T³umaczenia dla ldap ioslave.

%package -n kde-kio-smtp-i18n
Summary:	Internationalization and localization files for smtp ioslave
Summary(pl):	T³umaczenia dla smtp ioslave
Group:		X11/Applications
Requires:	kde-kio-smtp = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-smtp-i18n
Internationalization and localization files for smtp ioslave.

%description -n kde-kio-smtp-i18n -l pl
T³umaczenia dla smtp ioslave.

%package -n kde-kio-pop3-i18n
Summary:	Internationalization and localization files for pop3 ioslave
Summary(pl):	T³umaczenia dla pop3 ioslave
Group:		X11/Applications
Requires:	kde-kio-pop3 = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-pop3-i18n
Internationalization and localization files for pop3 ioslave.

%description -n kde-kio-pop3-i18n -l pl
T³umaczenia dla pop3 ioslave.

%package -n kde-kio-imap4-i18n
Summary:	Internationalization and localization files for imap4 ioslave
Summary(pl):	T³umaczenia dla imap4 ioslave
Group:		X11/Applications
Requires:	kde-kio-imap4 = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kde-kio-newimap4-i18n
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-imap4-i18n
Internationalization and localization files for imap4 ioslave.

%description -n kde-kio-imap4-i18n -l pl
T³umaczenia dla imap4 ioslave.

%package -n kde-kio-nntp-i18n
Summary:	Internationalization and localization files for nntp ioslave
Summary(pl):	T³umaczenia dla nntp ioslave
Group:		X11/Applications
Requires:	kde-kio-nntp = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-nntp-i18n
Internationalization and localization files for nntp ioslave.

%description -n kde-kio-nntp-i18n -l pl
T³umaczenia dla nntp ioslave.

%package -n kdevelop-i18n
Summary:	Internationalization and localization files for kdevelop
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdevelopa
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdevelop >= %{kdevelop_epoch}:%{kdevelop_version}

%description -n kdevelop-i18n
Internationalization and localization files for kdevelop.

%description -n kdevelop-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdevelopa.

%package -n kdepim-kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl):	T³umaczenia dla kaddressbook
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kaddressbook = %{kdepim_epoch}:%{version}

%description -n kdepim-kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description -n kdepim-kaddressbook-i18n -l pl
T³umaczenia dla kaddressbook.

%package -n kdepim-kandy-i18n
Summary:	Internationalization and localization files for kandy
Summary(pl):	T³umaczenia dla kandy
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kandy = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-kandy-i18n
Internationalization and localization files for kandy.

%description -n kdepim-kandy-i18n -l pl
T³umaczenia dla kandy.

%package -n kdepim-karm-i18n
Summary:	Internationalization and localization files for karm
Summary(pl):	T³umaczenia dla karm
Group:		X11/Applications
Requires:	kdepim-karm = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-karm-i18n
Internationalization and localization files for karm.

%description -n kdepim-karm-i18n -l pl
T³umaczenia dla karm.

%package -n kdepim-kmail-i18n
Summary:	Internationalization and localization files for kmail
Summary(pl):	T³umaczenia dla kmaila
Group:		X11/Applications
Requires:	kde-kio-imap4-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-pop3-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-smtp-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kmail = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-ktnef-i18n

%description -n kdepim-kmail-i18n
Internationalization and localization files for kmail.

%description -n kdepim-kmail-i18n -l pl
T³umaczenia dla kmaila.

%package -n kdepim-knode-i18n
Summary:	Internationalization and localization files for knode
Summary(pl):	T³umaczenia dla knode
Group:		X11/Applications
Requires:	kde-kio-nntp-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-smtp-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-knode = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-knode-i18n
Internationalization and localization files for knode.

%description -n kdepim-knode-i18n -l pl
T³umaczenia dla knode.

%package -n kdepim-knotes-i18n
Summary:	Internationalization and localization files for knotes
Summary(pl):	T³umaczenia dla knotes
Group:		X11/Applications
Requires:	kdepim-knotes = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-knotes-i18n
Internationalization and localization files for knotes.

%description -n kdepim-knotes-i18n -l pl
T³umaczenia dla knotes.

%package -n kdepim-konsolekalendar-i18n
Summary:	Internationalization and localization files for konsolekalendar
Summary(pl):	T³umaczenia dla konsolekalendara
Group:		X11/Applications
Requires:	kdepim-konsolekalendar = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-konsolekalendar-i18n
Internationalization and localization files for konsolekalendar.

%description -n kdepim-konsolekalendar-i18n -l pl
T³umaczenia dla konsolekalendara.

%package -n kdepim-i18n
Summary:	Internationalization and localization files for kdepim
Summary(pl):	T³umaczenia dla kdepim
Group:		X11/Applications
Requires:	kdepim = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdeaddons-kontact-i18n
Obsoletes:	kdepim-kontact-i18n
Obsoletes:	kdepim-korganizer-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-kresources-i18n

%description -n kdepim-i18n
Internationalization and localization files for kdepim.

%description -n kdepim-i18n -l pl
T³umaczenia dla kdepim.

%package -n kdepim-korn-i18n
Summary:	Internationalization and localization files for korn
Summary(pl):	T³umaczenia dla korna
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-korn = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-korn-i18n
Internationalization and localization files for korn.

%description -n kdepim-korn-i18n -l pl
T³umaczenia dla korna.

%package -n kdepim-kpilot-i18n
Summary:	Internationalization and localization files for kpilot
Summary(pl):	T³umaczenia dla kpilota
Group:		X11/Applications
Requires:	kdepim-kpilot = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-kpilot-i18n
Internationalization and localization files for kpilot.

%description -n kdepim-kpilot-i18n -l pl
T³umaczenia dla kpilota.

%package -n kdepim-libs-i18n
Summary:	Internationalization and localization files for libkdepim
Summary(pl):	T³umaczenia dla libkdepim
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-libs = %{kdepim_epoch}:%{version}
Obsoletes:	kdepim-kmail-libs-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-libkcal-i18n
Obsoletes:	kdepim-libkdenetwork-i18n
Obsoletes:	kdepim-libkdepim-i18n
Obsoletes:	kdepim-libkdgantt-i18n

%description -n kdepim-libs-i18n
Internationalization and localization files for kdepim libraries.

%description -n kdepim-libs-i18n -l pl
T³umaczenia dla bibliotek kdepim.

%package -n kdeutils-ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arka
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-ark = %{kdeutils_epoch}:%{version}

%description -n kdeutils-ark-i18n
Internationalization and localization files for ark.

%description -n kdeutils-ark-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arka.

%package -n kdeutils-kcalc-i18n
Summary:	Internationalization and localization files for kcalc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcalca
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kcalc = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kcalc-i18n
Internationalization and localization files for kcalc.

%description -n kdeutils-kcalc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcalca.

%package -n kdeutils-kcharselect-i18n
Summary:	Internationalization and localization files for kcharselect
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharselecta
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kcharselect = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kcharselect-i18n
Internationalization and localization files for kcharselect.

%description -n kdeutils-kcharselect-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharselecta.

%package -n kdeutils-kdf-i18n
Summary:	Internationalization and localization files for kdf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdf
Group:		X11/Applications
Requires:	kdebase-infocenter-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kdf = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kdf-i18n
Internationalization and localization files for kdf.

%description -n kdeutils-kdf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdf.

%package -n kdeutils-kedit-i18n
Summary:	Internationalization and localization files for kedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kedit = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kedit-i18n
Internationalization and localization files for kedit.

%description -n kdeutils-kedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kedita.

%package -n kdeutils-kmilo-i18n
Summary:	Internationalization and localization files for kmilo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kmilo = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kmilo-i18n
Internationalization and localization files for kmilo.

%description -n kdeutils-kmilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmilo.

%package -n kdeutils-kfloppy-i18n
Summary:	Internationalization and localization files for kfloppy
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfloppy
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kfloppy = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kfloppy-i18n
Internationalization and localization files for kfloppy.

%description -n kdeutils-kfloppy-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfloppy.

%package -n kdeutils-kgpg-i18n
Summary:	Internationalization and localization files for kgpg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgpg
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kgpg = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kgpg-i18n
Internationalization and localization files for kgpg.

%description -n kdeutils-kgpg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgpg.

%package -n kdeutils-khexedit-i18n
Summary:	Internationalization and localization files for khexedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khexedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-khexedit = %{kdeutils_epoch}:%{version}

%description -n kdeutils-khexedit-i18n
Internationalization and localization files for khexedit.

%description -n kdeutils-khexedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khexedita.

%package -n kdeutils-kjots-i18n
Summary:	Internationalization and localization files for kjots
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjots
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kjots = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kjots-i18n
Internationalization and localization files for kjots.

%description -n kdeutils-kjots-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjots.

%package -n kdeutils-klaptopdaemon-i18n
Summary:	Internationalization and localization files for klaptopdaemon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klaptopdaemona
Group:		X11/Applications
Requires:	kdebase-infocenter-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-klaptopdaemon = %{kdeutils_epoch}:%{version}

%description -n kdeutils-klaptopdaemon-i18n
Internationalization and localization files for klaptopdaemon.

%description -n kdeutils-klaptopdaemon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klaptopdaemona.

%package -n kdeutils-kregexpeditor-i18n
Summary:	Internationalization and localization files for kregexpeditor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kregexpeditora
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kregexpeditor = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kregexpeditor-i18n
Internationalization and localization files for kregexpeditor.

%description -n kdeutils-kregexpeditor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kregexpeditora.

%package -n kdeutils-ksim-i18n
Summary:	Internationalization and localization files for ksim
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksima
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-ksim = %{kdeutils_epoch}:%{version}

%description -n kdeutils-ksim-i18n
Internationalization and localization files for ksim.

%description -n kdeutils-ksim-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksima.

%package -n kdeutils-ktimer-i18n
Summary:	Internationalization and localization files for ktimer
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktimera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-ktimer = %{kdeutils_epoch}:%{version}

%description -n kdeutils-ktimer-i18n
Internationalization and localization files for ktimer.

%description -n kdeutils-ktimer-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktimera.

%package -n kdeutils-kwalletmanager-i18n
Summary:	Internationalization and localization files for kwalletmanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwalletmanagera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kwalletmanager = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kwalletmanager-i18n
Internationalization and localization files for kwalletmanager.

%description -n kdeutils-kwalletmanager-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwalletmanagera.

%package -n kdeutils-kdelirc-i18n
Summary:	Internationalization and localization files for kdelirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdelirca
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kdelirc = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kdelirc-i18n
Internationalization and localization files for kdelirc.

%description -n kdeutils-kdelirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdelirca.

%package -n kdeutils-kdessh-i18n
Summary:	Internationalization and localization files for kdessh
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdessh
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kdessh = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kdessh-i18n
Internationalization and localization files for kdessh.

%description -n kdeutils-kdessh-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdessh.

%package -n kdebase-useraccount-i18n
Summary:	Internationalization and localization files for useraccount
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla useraccount
Group:		X11/Applications
Requires:	kdebase-useraccount = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdeutils-kdepasswd-i18n
Obsoletes:	kdeutils-userinfo-i18n

%description -n kdebase-useraccount-i18n
Internationalization and localization files for useraccount.

%description -n kdebase-useraccount-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla useraccount.

%package -n kdeaccessibility-kmag-i18n
Summary:	Internationalization and localization files for kmag
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmag
Group:		X11/Applications
Requires:	kdeaccessibility-kmag = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmag-i18n
Internationalization and localization files for kmag.

%description -n kdeaccessibility-kmag-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmag.

%package -n kdeaccessibility-kmousetool-i18n
Summary:	Internationalization and localization files for kmousetool
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmousetool
Group:		X11/Applications
Requires:	kdeaccessibility-kmousetool = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmousetool-i18n
Internationalization and localization files for kmousetool.

%description -n kdeaccessibility-kmousetool-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmousetool.

%package -n kdeaccessibility-kmouth-i18n
Summary:	Internationalization and localization files for kmouth
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmouth
Group:		X11/Applications
Requires:	kdeaccessibility-kmouth = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmouth-i18n
Internationalization and localization files for kmouth.

%description -n kdeaccessibility-kmouth-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmouth.

%package -n kdenetwork-filesharing-i18n
Summary:	Internationalization and localization files for fileshare
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla fileshare
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-filesharing = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-filesharing-i18n
Internationalization and localization files for fileshare.

%description -n kdenetwork-filesharing-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla fileshare.

%package -n kdenetwork-kdict-i18n
Summary:	Internationalization and localization files for kdict
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdict
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kdict = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kdict-i18n
Internationalization and localization files for kdict.

%description -n kdenetwork-kdict-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdict.

%package -n kdenetwork-kinetd-i18n
Summary:	Internationalization and localization files for kinetd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kinetd
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kinetd = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kinetd-i18n
Internationalization and localization files for kinetd.

%description -n kdenetwork-kinetd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kinetd.

%package -n kdenetwork-kget-i18n
Summary:	Internationalization and localization files for kget
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgeta
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kget = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kget-i18n
Internationalization and localization files for kget.

%description -n kdenetwork-kget-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgeta.

%package -n kdenetwork-knewsticker-i18n
Summary:	Internationalization and localization files for knewsticker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla knewstickera
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-knewsticker = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-knewsticker-i18n
Internationalization and localization files for knewsticker.

%description -n kdenetwork-knewsticker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla knewstickera.

%package -n kdenetwork-kopete-i18n
Summary:	Internationalization and localization files for kopete
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kopete
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kopete = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kopete-i18n
Internationalization and localization files for kopete.

%description -n kdenetwork-kopete-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kopete.

%package -n kdenetwork-kpf-i18n
Summary:	Internationalization and localization files for kpf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpf
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kpf = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kpf-i18n
Internationalization and localization files for kpf.

%description -n kdenetwork-kpf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpf.

%package -n kdenetwork-kppp-i18n
Summary:	Internationalization and localization files for kppp
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kppp
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kppp = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kppp-i18n
Internationalization and localization files for kppp.

%description -n kdenetwork-kppp-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kppp.

%package -n kdenetwork-krfb-i18n
Summary:	Internationalization and localization files for krfb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krfb
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kinetd-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-krfb = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-krfb-i18n
Internationalization and localization files for krfb.

%description -n kdenetwork-krfb-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krfb.

%package -n kdenetwork-ksirc-i18n
Summary:	Internationalization and localization files for ksirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirc
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-ksirc = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-ksirc-i18n
Internationalization and localization files for ksirc.

%description -n kdenetwork-ksirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksirc.

%package -n kdenetwork-ktalkd-i18n
Summary:	Internationalization and localization files for ktalkd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktalkd
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-ktalkd = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-ktalkd-i18n
Internationalization and localization files for ktalkd.

%description -n kdenetwork-ktalkd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktalkd.

%package -n kdenetwork-kwifimanager-i18n
Summary:	Internationalization and localization files for kwifimanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwifimanagera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kwifimanager = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kwifimanager-i18n
Internationalization and localization files for kwifimanager.

%description -n kdenetwork-kwifimanager-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwifimanagera.

%package -n kdenetwork-lanbrowser-i18n
Summary:	Internationalization and localization files for lanbrowser
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lanbrowsera
Group:		X11/Applications
Requires:	kdenetwork-lanbrowser = %{kdenetwork_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-lanbrowser-i18n
Internationalization and localization files for lanbrowser.

%description -n kdenetwork-lanbrowser-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla lanbrowsera.

%package -n kdenetwork-rss-i18n
Summary:	Internationalization and localization files for rss
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla rss
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-rss = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-rss-i18n
Internationalization and localization files for rss.

%description -n kdenetwork-rss-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla rss.

%package -n kdemultimedia-artsbuilder-i18n
Summary:	Internationalization and localization files for artsbuilder
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artsbuildera
Group:		X11/Applications
Requires:	kdemultimedia-arts-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-artsbuilder = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-artsbuilder-i18n
Internationalization and localization files for artsbuilder.

%description -n kdemultimedia-artsbuilder-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artsbuildera.

%package -n kdemultimedia-artscontrol-i18n
Summary:	Internationalization and localization files for artscontrol
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artscontrol
Group:		X11/Applications
Requires:	kdemultimedia-arts-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-artscontrol = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-artscontrol-i18n
Internationalization and localization files for artscontrol.

%description -n kdemultimedia-artscontrol-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artscontrol.

%package -n kdemultimedia-arts-i18n
Summary:	Internationalization and localization files for arts
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arts
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-arts = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-arts-i18n
Internationalization and localization files for arts.

%description -n kdemultimedia-arts-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arts.

%package -n kdemultimedia-juk-i18n
Summary:	Internationalization and localization files for juk
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla juk
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-juk = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-juk-i18n
Internationalization and localization files for juk.

%description -n kdemultimedia-juk-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla juk.

%package -n kdemultimedia-kaboodle-i18n
Summary:	Internationalization and localization files for kaboodle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaboodle
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kaboodle = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kaboodle-i18n
Internationalization and localization files for kaboodle.

%description -n kdemultimedia-kaboodle-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaboodle.

%package -n kdemultimedia-kmid-i18n
Summary:	Internationalization and localization files for kmid
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmid
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmid = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kmid-i18n
Internationalization and localization files for kmid.

%description -n kdemultimedia-kmid-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmid.

%package -n kdemultimedia-kmix-i18n
Summary:	Internationalization and localization files for kmix
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmix
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmix = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kmix-i18n
Internationalization and localization files for kmix.

%description -n kdemultimedia-kmix-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmix.

%package -n kdemultimedia-kscd-i18n
Summary:	Internationalization and localization files for kscd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kscd
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kscd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kscd-i18n
Internationalization and localization files for kscd.

%description -n kdemultimedia-kscd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kscd.

%package -n kdemultimedia-krec-i18n
Summary:	Internationalization and localization files for krec
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krec
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-artscontrol-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmix-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-krec = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-krec-i18n
Internationalization and localization files for krec.

%description -n kdemultimedia-krec-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krec.

%package -n kdemultimedia-noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla noatun
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-noatun = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-noatun-i18n
Internationalization and localization files for noatun.

%description -n kdemultimedia-noatun-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla noatun.

%package -n kdemultimedia-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfile
Group:		X11/Applications
Requires:	kdemultimedia-kfile = %{kdemultimedia_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdemultimedia-kfile-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfile.

%package -n kdemultimedia-audiocd-i18n
Summary:	Internationalization and localization files for audiocd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla audiocd
Group:		X11/Applications
Requires:	kdemultimedia-audiocd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-audiocd-i18n
Internationalization and localization files for audiocd.

%description -n kdemultimedia-audiocd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla audiocd.

%package -n kdemultimedia-libkcddb-i18n
Summary:	Internationalization and localization files for libkcddb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla libkcddb
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-libkcddb = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-libkcddb-i18n
Internationalization and localization files for libkcddb.

%description -n kdemultimedia-libkcddb-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla libkcddb.

%package -n kdemultimedia-kaudiocreator-i18n
Summary:	Internationalization and localization files for kaudiocreator
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaudiocreatora
Group:		X11/Applications
Requires:	kdemultimedia-kaudiocreator = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kaudiocreator-i18n
Internationalization and localization files for kaudiocreator.

%description -n kdemultimedia-kaudiocreator-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaudiocreatora.

%package -n kdeadmin-kcron-i18n
Summary:	Internationalization and localization files for kcron
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcrona
Group:		X11/Applications
Requires:	kdeadmin-kcron = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kcron-i18n
Internationalization and localization files for kcron.

%description -n kdeadmin-kcron-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcrona.

%package -n kdeadmin-kdat-i18n
Summary:	Internationalization and localization files for kdat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdat
Group:		X11/Applications
Requires:	kdeadmin-kdat = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kdat-i18n
Internationalization and localization files for kdat.

%description -n kdeadmin-kdat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdat.

%package -n kdeadmin-kpackage-i18n
Summary:	Internationalization and localization files for kpackage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpackage
Group:		X11/Applications
Requires:	kdeadmin-kpackage = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kpackage-i18n
Internationalization and localization files for kpackage.

%description -n kdeadmin-kpackage-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpackage.

%package -n kdeadmin-ksysv-i18n
Summary:	Internationalization and localization files for ksysv
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksysv
Group:		X11/Applications
Requires:	kdeadmin-ksysv = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-ksysv-i18n
Internationalization and localization files for ksysv.

%description -n kdeadmin-ksysv-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksysv.

%package -n kdeadmin-kuser-i18n
Summary:	Internationalization and localization files for kuser
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kusera
Group:		X11/Applications
Requires:	kdeadmin-kuser = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kuser-i18n
Internationalization and localization files for kuser.

%description -n kdeadmin-kuser-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kusera.

%package -n kdeadmin-kcmlilo-i18n
Summary:	Internationalization and localization files for kcmlilo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcmlilo
Group:		X11/Applications
Requires:	kdeadmin-kcmlilo = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdeadmin-kcmlinuz-i18n

%description -n kdeadmin-kcmlilo-i18n
Internationalization and localization files for kcmlilo.

%description -n kdeadmin-kcmlilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlilo.

%package -n kde-decoration-cde-i18n
Summary:	Internationalization and localization files for kde-decoration-cde
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-cde
Group:		X11/Applications
Requires:	kde-decoration-cde = %{kdeartwork_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-cde-i18n
Internationalization and localization files for kde-decoration-cde.

%description -n kde-decoration-cde-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-cde.

%package -n kde-decoration-icewm-i18n
Summary:	Internationalization and localization files for kde-decoration-icewm
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm
Group:		X11/Applications
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-icewm = %{kdeartwork_epoch}:%{version}

%description -n kde-decoration-icewm-i18n
Internationalization and localization files for kde-decoration-icewm.

%description -n kde-decoration-icewm-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm.

%package -n kde-decoration-glow-i18n
Summary:	Internationalization and localization files for kde-decoration-glow
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow
Group:		X11/Applications
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-glow = %{kdeartwork_epoch}:%{version}

%description -n kde-decoration-glow-i18n
Internationalization and localization files for kde-decoration-glow.

%description -n kde-decoration-glow-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow.

%package -n kde-decoration-plastik-i18n
Summary:	Internationalization and localization files for kde-decoration-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik
Group:		X11/Applications
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-decoration-plastik = %{kdeartwork_epoch}:%{version}

%description -n kde-decoration-plastik-i18n
Internationalization and localization files for
kde-decoration-plastik.

%description -n kde-decoration-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik.

%package -n kde-decoration-common-i18n
Summary:	Common internationalization and localization files for kwin decorations
Summary(pl):	Wspólne pliki umiêdzynarodawiaj±ce dla dekoracji kwin
Group:		X11/Applications

%description -n kde-decoration-common-i18n
Common internationalization and localization files for kwin
decorations.

%description -n kde-decoration-common-i18n -l pl
Wspólne pliki umiêdzynarodawiaj±ce dla dekoracji kwin.

%package -n kdeartwork-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla screensavers
Group:		X11/Applications
Requires:	kdeartwork-screensavers = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-screensavers-i18n = %{epoch}:%{version}-%{release}

%description -n kdeartwork-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdeartwork-screensavers-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla screensavers.

%package -n kdeedu-kwordquiz-i18n
Summary:	Internationalization and localization files for kwordquiz
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwordquiz
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kwordquiz = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kwordquiz-i18n
Internationalization and localization files for kwordquiz.

%description -n kdeedu-kwordquiz-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwordquiz.

%package -n kdeedu-kturtle-i18n
Summary:	Internationalization and localization files for kturtle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kturtle
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kturtle = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kturtle-i18n
Internationalization and localization files for kturtle.

%description -n kdeedu-kturtle-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kturtle.

%package -n kdeedu-klatin-i18n
Summary:	Internationalization and localization files for klatin
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klatin
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-klatin = %{kdeedu_epoch}:%{version}

%description -n kdeedu-klatin-i18n
Internationalization and localization files for klatin.

%description -n kdeedu-klatin-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klatin.

%package -n kdeedu-flashkard-i18n
Summary:	Internationalization and localization files for flashkard
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla flashkarda
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-flashkard = %{kdeedu_epoch}:%{version}

%description -n kdeedu-flashkard-i18n
Internationalization and localization files for flashkard.

%description -n kdeedu-flashkard-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla flashkarda.

%package -n kdeedu-kalzium-i18n
Summary:	Internationalization and localization files for kalzium
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kalzium
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kalzium = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kalzium-i18n
Internationalization and localization files for kalzium.

%description -n kdeedu-kalzium-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kalzium.

%package -n kdeedu-kbruch-i18n
Summary:	Internationalization and localization files for kbruch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbrucha
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kbruch = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kbruch-i18n
Internationalization and localization files for kbruch.

%description -n kdeedu-kbruch-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbrucha.

%package -n kdeedu-keduca-i18n
Summary:	Internationalization and localization files for keduca
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla keduca
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-keduca = %{kdeedu_epoch}:%{version}

%description -n kdeedu-keduca-i18n
Internationalization and localization files for keduca.

%description -n kdeedu-keduca-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla keduca.

%package -n kdeedu-khangman-i18n
Summary:	Internationalization and localization files for khangman
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khangmana
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-khangman = %{kdeedu_epoch}:%{version}

%description -n kdeedu-khangman-i18n
Internationalization and localization files for khangman.

%description -n kdeedu-khangman-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khangmana.

%package -n kdeedu-kig-i18n
Summary:	Internationalization and localization files for kig
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kig
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kig = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kig-i18n
Internationalization and localization files for kig.

%description -n kdeedu-kig-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kig.

%package -n kdeedu-kiten-i18n
Summary:	Internationalization and localization files for kiten
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kiten
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kiten = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kiten-i18n
Internationalization and localization files for kiten.

%description -n kdeedu-kiten-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kiten.

%package -n kdeedu-klettres-i18n
Summary:	Internationalization and localization files for klettres
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klettres
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-klettres = %{kdeedu_epoch}:%{version}

%description -n kdeedu-klettres-i18n
Internationalization and localization files for klettres.

%description -n kdeedu-klettres-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klettres.

%package -n kdeedu-kanagram-i18n
Summary:	Internationalization and localization files for kanagram
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kanagram
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kanagram = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kanagram-i18n
Internationalization and localization files for kanagram.

%description -n kdeedu-kanagram-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kanagram.

%package -n kdeedu-kmplot-i18n
Summary:	Internationalization and localization files for kmplot
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmplot
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kmplot = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kmplot-i18n
Internationalization and localization files for kmplot.

%description -n kdeedu-kmplot-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmplot.

%package -n kdeedu-kpercentage-i18n
Summary:	Internationalization and localization files for kpercentage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpercentage
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kpercentage = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kpercentage-i18n
Internationalization and localization files for kpercentage.

%description -n kdeedu-kpercentage-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpercentage.

%package -n kdeedu-kstars-i18n
Summary:	Internationalization and localization files for kstars
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstars
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kstars = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kstars-i18n
Internationalization and localization files for kstars.

%description -n kdeedu-kstars-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kstars.

%package -n kdeedu-ktouch-i18n
Summary:	Internationalization and localization files for ktouch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktouch
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-ktouch = %{kdeedu_epoch}:%{version}

%description -n kdeedu-ktouch-i18n
Internationalization and localization files for ktouch.

%description -n kdeedu-ktouch-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktouch.

%package -n kdeedu-kverbos-i18n
Summary:	Internationalization and localization files for kverbos
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kverbos
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kverbos = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kverbos-i18n
Internationalization and localization files for kverbos.

%description -n kdeedu-kverbos-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kverbos.

%package -n kdeedu-kvoctrain-i18n
Summary:	Internationalization and localization files for kvoctrain
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kvoctrain
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kvoctrain = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kvoctrain-i18n
Internationalization and localization files for kvoctrain.

%description -n kdeedu-kvoctrain-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kvoctrain.

%package -n kdegames-i18n
Summary:	Internationalization and localization files for kdegames libs
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla bibliotek kdegames
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames = %{kdegames_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-i18n
Internationalization and localization files for kdegames libs.

%description -n kdegames-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla bibliotek kdegames.

%package -n kdegames-kmahjongg-i18n
Summary:	Internationalization and localization files for kmahjongg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmahjongga
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kmahjongg = %{kdegames_epoch}:%{version}

%description -n kdegames-kmahjongg-i18n
Internationalization and localization files for kmahjongg.

%description -n kdegames-kmahjongg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmahjongga.

%package -n kdegames-ksmiletris-i18n
Summary:	Internationalization and localization files for ksmiletris
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksmiletrisa
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksmiletris = %{kdegames_epoch}:%{version}

%description -n kdegames-ksmiletris-i18n
Internationalization and localization files for ksmiletris.

%description -n kdegames-ksmiletris-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksmiletrisa.

%package -n kdegames-atlantik-i18n
Summary:	Internationalization and localization files for atlantik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla atlantika
Group:		X11/Applications
Requires:	kdegames-atlantik = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-atlantik-i18n
Internationalization and localization files for atlantik.

%description -n kdegames-atlantik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla atlantika.

%package -n kdegames-kasteroids-i18n
Summary:	Internationalization and localization files for kasteroids
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kasteroids
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kasteroids = %{kdegames_epoch}:%{version}

%description -n kdegames-kasteroids-i18n
Internationalization and localization files for kasteroids.

%description -n kdegames-kasteroids-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kasteroids.

%package -n kdegames-katomic-i18n
Summary:	Internationalization and localization files for katomic
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla katomic
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-katomic = %{kdegames_epoch}:%{version}

%description -n kdegames-katomic-i18n
Internationalization and localization files for katomic.

%description -n kdegames-katomic-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla katomic.

%package -n kdegames-kbackgammon-i18n
Summary:	Internationalization and localization files for kbackgammon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbackgammona
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kbackgammon = %{kdegames_epoch}:%{version}

%description -n kdegames-kbackgammon-i18n
Internationalization and localization files for kbackgammon.

%description -n kdegames-kbackgammon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbackgammona.

%package -n kdegames-kbattleship-i18n
Summary:	Internationalization and localization files for kbattleship
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbattleship
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kbattleship = %{kdegames_epoch}:%{version}

%description -n kdegames-kbattleship-i18n
Internationalization and localization files for kbattleship.

%description -n kdegames-kbattleship-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbattleship.

%package -n kdegames-kblackbox-i18n
Summary:	Internationalization and localization files for kblackbox
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kblackboksa
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kblackbox = %{kdegames_epoch}:%{version}

%description -n kdegames-kblackbox-i18n
Internationalization and localization files for kblackbox.

%description -n kdegames-kblackbox-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kblackboksa.

%package -n kdegames-kbounce-i18n
Summary:	Internationalization and localization files for kbounce
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbounce
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kbounce = %{kdegames_epoch}:%{version}

%description -n kdegames-kbounce-i18n
Internationalization and localization files for kbounce.

%description -n kdegames-kbounce-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbounce.

%package -n kdegames-kenolaba-i18n
Summary:	Internationalization and localization files for kenolaba
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kenolaby
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kenolaba = %{kdegames_epoch}:%{version}

%description -n kdegames-kenolaba-i18n
Internationalization and localization files for kenolaba.

%description -n kdegames-kenolaba-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kenolaby.

%package -n kdegames-kfouleggs-i18n
Summary:	Internationalization and localization files for kfouleggs
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfouleggs
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kfouleggs = %{kdegames_epoch}:%{version}

%description -n kdegames-kfouleggs-i18n
Internationalization and localization files for kfouleggs.

%description -n kdegames-kfouleggs-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfouleggs.

%package -n kdegames-kgoldrunner-i18n
Summary:	Internationalization and localization files for kgoldrunner
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgoldrunnera
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kgoldrunner = %{kdegames_epoch}:%{version}

%description -n kdegames-kgoldrunner-i18n
Internationalization and localization files for kgoldrunner.

%description -n kdegames-kgoldrunner-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgoldrunnera.

%package -n kdegames-kjumpingcube-i18n
Summary:	Internationalization and localization files for kjumpingcube
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjumpingcube
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kjumpingcube = %{kdegames_epoch}:%{version}

%description -n kdegames-kjumpingcube-i18n
Internationalization and localization files for kjumpingcube.

%description -n kdegames-kjumpingcube-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjumpingcube.

%package -n kdegames-klickety-i18n
Summary:	Internationalization and localization files for klickety
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klickety
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-klickety = %{kdegames_epoch}:%{version}

%description -n kdegames-klickety-i18n
Internationalization and localization files for klickety.

%description -n kdegames-klickety-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klickety.

%package -n kdegames-klines-i18n
Summary:	Internationalization and localization files for klines
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klines
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-klines = %{kdegames_epoch}:%{version}

%description -n kdegames-klines-i18n
Internationalization and localization files for klines.

%description -n kdegames-klines-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klines.

%package -n kdegames-kmines-i18n
Summary:	Internationalization and localization files for kmines
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmines
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kmines = %{kdegames_epoch}:%{version}

%description -n kdegames-kmines-i18n
Internationalization and localization files for kmines.

%description -n kdegames-kmines-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmines.

%package -n kdegames-kolf-i18n
Summary:	Internationalization and localization files for kolf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kolfa
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kolf = %{kdegames_epoch}:%{version}

%description -n kdegames-kolf-i18n
Internationalization and localization files for kolf.

%description -n kdegames-kolf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kolfa.

%package -n kdegames-konquest-i18n
Summary:	Internationalization and localization files for konquest
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla konquesta
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-konquest = %{kdegames_epoch}:%{version}

%description -n kdegames-konquest-i18n
Internationalization and localization files for konquest.

%description -n kdegames-konquest-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla konquesta.

%package -n kdegames-kpat-i18n
Summary:	Internationalization and localization files for kpat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpata
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kpat = %{kdegames_epoch}:%{version}

%description -n kdegames-kpat-i18n
Internationalization and localization files for kpat.

%description -n kdegames-kpat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpata.

%package -n kdegames-kpoker-i18n
Summary:	Internationalization and localization files for kpoker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpokera
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kpoker = %{kdegames_epoch}:%{version}

%description -n kdegames-kpoker-i18n
Internationalization and localization files for kpoker.

%description -n kdegames-kpoker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpokera.

%package -n kdegames-kreversi-i18n
Summary:	Internationalization and localization files for kreversi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kreversi
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kreversi = %{kdegames_epoch}:%{version}

%description -n kdegames-kreversi-i18n
Internationalization and localization files for kreversi.

%description -n kdegames-kreversi-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kreversi.

%package -n kdegames-ksame-i18n
Summary:	Internationalization and localization files for ksame
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksame
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksame = %{kdegames_epoch}:%{version}

%description -n kdegames-ksame-i18n
Internationalization and localization files for ksame.

%description -n kdegames-ksame-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksame.

%package -n kdegames-kshisen-i18n
Summary:	Internationalization and localization files for kshisen
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kshisen
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kshisen = %{kdegames_epoch}:%{version}

%description -n kdegames-kshisen-i18n
Internationalization and localization files for kshisen.

%description -n kdegames-kshisen-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kshisen.

%package -n kdegames-ksirtet-i18n
Summary:	Internationalization and localization files for ksirtet
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirteta
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksirtet = %{kdegames_epoch}:%{version}

%description -n kdegames-ksirtet-i18n
Internationalization and localization files for ksirtet.

%description -n kdegames-ksirtet-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksirteta.

%package -n kdegames-ksnake-i18n
Summary:	Internationalization and localization files for ksnake
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksnake'a
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksnake = %{kdegames_epoch}:%{version}

%description -n kdegames-ksnake-i18n
Internationalization and localization files for ksnake.

%description -n kdegames-ksnake-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksnake'a.

%package -n kdegames-ksokoban-i18n
Summary:	Internationalization and localization files for ksokoban
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksokobana
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksokoban = %{kdegames_epoch}:%{version}

%description -n kdegames-ksokoban-i18n
Internationalization and localization files for ksokoban.

%description -n kdegames-ksokoban-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksokobana.

%package -n kdegames-kspaceduel-i18n
Summary:	Internationalization and localization files for kspaceduel
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspaceduel
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kspaceduel = %{kdegames_epoch}:%{version}

%description -n kdegames-kspaceduel-i18n
Internationalization and localization files for kspaceduel.

%description -n kdegames-kspaceduel-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kspaceduel.

%package -n kdegames-ktron-i18n
Summary:	Internationalization and localization files for ktron
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktrona
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ktron = %{kdegames_epoch}:%{version}

%description -n kdegames-ktron-i18n
Internationalization and localization files for ktron.

%description -n kdegames-ktron-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktrona.

%package -n kdegames-ktuberling-i18n
Summary:	Internationalization and localization files for ktuberling
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktuberlinga
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ktuberling = %{kdegames_epoch}:%{version}

%description -n kdegames-ktuberling-i18n
Internationalization and localization files for ktuberling.

%description -n kdegames-ktuberling-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktuberlinga.

%package -n kdegames-kwin4-i18n
Summary:	Internationalization and localization files for kwin4
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwin4
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kwin4 = %{kdegames_epoch}:%{version}

%description -n kdegames-kwin4-i18n
Internationalization and localization files for kwin4.

%description -n kdegames-kwin4-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwin4.

%package -n kdegames-lskat-i18n
Summary:	Internationalization and localization files for lskat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lskata
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-lskat = %{kdegames_epoch}:%{version}

%description -n kdegames-lskat-i18n
Internationalization and localization files for lskat.

%description -n kdegames-lskat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla lskata.

%package -n kdegames-megami-i18n
Summary:	Internationalization and localization files for megami
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla megami
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-megami = %{kdegames_epoch}:%{version}

%description -n kdegames-megami-i18n
Internationalization and localization files for megami.

%description -n kdegames-megami-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla megami.

%package -n kdesdk-libcvsservice-i18n
Summary:	Internationalization and localization files for libcvsservice
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla libcvsservice
Group:		X11/Applications
Requires:	kdesdk-libcvsservice = %{kdesdk_epoch}:%{version}
Conflicts:	kdesdk-cervisia-i18n < %{epoch}:%{version}-%{release}

%description -n kdesdk-libcvsservice-i18n
Internationalization and localization files for libcvsservice.

%description -n kdesdk-libcvsservice-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla libcvsservice.

%package -n kdesdk-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfile
Group:		X11/Applications
Requires:	kdesdk-kfile = %{kdesdk_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdesdk-kfile-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfile.

%package -n kdesdk-cervisia-i18n
Summary:	Internationalization and localization files for cervisia
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla cervisii
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-cervisia = %{kdesdk_epoch}:%{version}
Requires:	kdesdk-libcvsservice-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-cervisia-i18n
Internationalization and localization files for cervisia.

%description -n kdesdk-cervisia-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla cervisii.

%package -n kdesdk-kbabel-i18n
Summary:	Internationalization and localization files for kbabel
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbabel
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kbabel = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kbabel-i18n
Internationalization and localization files for kbabel.

%description -n kdesdk-kbabel-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbabel.

%package -n kdesdk-kbugbuster-i18n
Summary:	Internationalization and localization files for kbugbuster
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbugbustera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kbugbuster = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kbugbuster-i18n
Internationalization and localization files for kbugbuster.

%description -n kdesdk-kbugbuster-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbugbustera.

%package -n kdesdk-kcachegrind-i18n
Summary:	Internationalization and localization files for kcachegrind
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcachegrinda
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kcachegrind = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kcachegrind-i18n
Internationalization and localization files for kcachegrind.

%description -n kdesdk-kcachegrind-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcachegrinda.

%package -n kdesdk-kompare-i18n
Summary:	Internationalization and localization files for kompare
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kompare
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kompare = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kompare-i18n
Internationalization and localization files for kompare.

%description -n kdesdk-kompare-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kompare.

%package -n kdesdk-kstartperf-i18n
Summary:	Internationalization and localization files for kstartperf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstartperfa
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kstartperf = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kstartperf-i18n
Internationalization and localization files for kstartperf.

%description -n kdesdk-kstartperf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kstartperfa.

%package -n kdesdk-kuiviewer-i18n
Summary:	Internationalization and localization files for kuiviewer
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kuiviewera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kuiviewer = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kuiviewer-i18n
Internationalization and localization files for kuiviewer.

%description -n kdesdk-kuiviewer-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kuiviewera.

%package -n kdesdk-kspy-i18n
Summary:	Internationalization and localization files for kspy
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspy
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kspy = %{kdesdk_epoch}:%{version}
Obsoletes:	kdesdk-spy-i18n

%description -n kdesdk-kspy-i18n
Internationalization and localization files for spy.

%description -n kdesdk-kspy-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla spy.

%package -n kdesdk-umbrello-i18n
Summary:	Internationalization and localization files for umbrello
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla umbrello
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-umbrello = %{kdesdk_epoch}:%{version}

%description -n kdesdk-umbrello-i18n
Internationalization and localization files for umbrello.

%description -n kdesdk-umbrello-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla umbrello.

%package -n kdetoys-amor-i18n
Summary:	Internationalization and localization files for amor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla amora
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-amor = %{kdetoys_epoch}:%{version}

%description -n kdetoys-amor-i18n
Internationalization and localization files for amor.

%description -n kdetoys-amor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla amora.

%package -n kdetoys-kmoon-i18n
Summary:	Internationalization and localization files for kmoon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmoon
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kmoon = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kmoon-i18n
Internationalization and localization files for kmoon.

%description -n kdetoys-kmoon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmoon.

%package -n kdetoys-kodo-i18n
Summary:	Internationalization and localization files for kodo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kodo
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kodo = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kodo-i18n
Internationalization and localization files for kodo.

%description -n kdetoys-kodo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kodo.

%package -n kdetoys-kteatime-i18n
Summary:	Internationalization and localization files for kteatime
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kteatime
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kteatime = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kteatime-i18n
Internationalization and localization files for kteatime.

%description -n kdetoys-kteatime-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kteatime.

%package -n kdetoys-kweather-i18n
Summary:	Internationalization and localization files for kweather
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kweather
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kweather = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kweather-i18n
Internationalization and localization files for kweather.

%description -n kdetoys-kweather-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kweather.

%package -n kdetoys-kworldclock-i18n
Summary:	Internationalization and localization files for kworldclock
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kworldclocka
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kworldclock = %{kdetoys_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kworldclock-i18n
Internationalization and localization files for kworldclock.

%description -n kdetoys-kworldclock-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kworldclocka.

%package -n kdetoys-ktux-i18n
Summary:	Internationalization and localization files for ktux
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktuksa
Group:		X11/Applications
Requires:	kdebase-screensavers-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-ktux = %{kdetoys_epoch}:%{version}

%description -n kdetoys-ktux-i18n
Internationalization and localization files for ktux.

%description -n kdetoys-ktux-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktuksa.

%package -n kdetoys-fifteen-i18n
Summary:	Internationalization and localization files for fifteen
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla fifteen
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-fifteen = %{kdetoys_epoch}:%{version}

%description -n kdetoys-fifteen-i18n
Internationalization and localization files for fifteen.

%description -n kdetoys-fifteen-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla fifteen.

%package -n kdegraphics-kamera-i18n
Summary:	Internationalization and localization files for kamera
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla programu kamera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kamera = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kamera-i18n
Internationalization and localization files for kamera.

%description -n kdegraphics-kamera-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla programu kamera.

%package -n kdegraphics-kcoloredit-i18n
Summary:	Internationalization and localization files for kcoloredit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcoloredita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kcoloredit = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kcoloredit-i18n
Internationalization and localization files for kcoloredit.

%description -n kdegraphics-kcoloredit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcoloredita.

%package -n kdegraphics-kdvi-i18n
Summary:	Internationalization and localization files for kdvi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdvi
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kdvi = %{kdegraphics_epoch}:%{version}
Requires:	kdegraphics-kview-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kdvi-i18n
Internationalization and localization files for kdvi.

%description -n kdegraphics-kdvi-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdvi.

%package -n kdegraphics-kgamma-i18n
Summary:	Internationalization and localization files for kgamma
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgamma
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kgamma = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kgamma-i18n
Internationalization and localization files for kgamma.

%description -n kdegraphics-kgamma-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgamma.

%package -n kdegraphics-kghostview-i18n
Summary:	Internationalization and localization files for kghostview
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kghostview
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kghostview = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kghostview-i18n
Internationalization and localization files for kghostview.

%description -n kdegraphics-kghostview-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kghostview.

%package -n kdegraphics-kiconedit-i18n
Summary:	Internationalization and localization files for kiconedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kiconedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kiconedit = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kiconedit-i18n
Internationalization and localization files for kiconedit.

%description -n kdegraphics-kiconedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kiconedita.

%package -n kdegraphics-kooka-i18n
Summary:	Internationalization and localization files for kooka
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kooki
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kooka = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kooka-i18n
Internationalization and localization files for kooka.

%description -n kdegraphics-kooka-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kooki.

%package -n kdegraphics-kolourpaint-i18n
Summary:	Internationalization and localization files for kolourpaint
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kolourpaint
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kolourpaint = %{kdegraphics_epoch}:%{version}
Obsoletes:	kdegraphics-kpaint-i18n

%description -n kdegraphics-kolourpaint-i18n
Internationalization and localization files for kolourpaint.

%description -n kdegraphics-kolourpaint-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kolourpaint.

%package -n kdegraphics-kpdf-i18n
Summary:	Internationalization and localization files for kpdf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpdf
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kpdf = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kpdf-i18n
Internationalization and localization files for kpdf.

%description -n kdegraphics-kpdf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpdf.

%package -n kdegraphics-kpovmodeler-i18n
Summary:	Internationalization and localization files for kpovmodeler
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpovmodelera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kpovmodeler = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kpovmodeler-i18n
Internationalization and localization files for kpovmodeler.

%description -n kdegraphics-kpovmodeler-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpovmodelera.

%package -n kdegraphics-kruler-i18n
Summary:	Internationalization and localization files for kruler
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krulera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kruler = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kruler-i18n
Internationalization and localization files for kruler.

%description -n kdegraphics-kruler-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krulera.

%package -n kdegraphics-ksnapshot-i18n
Summary:	Internationalization and localization files for ksnapshot
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksnapshota
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-ksnapshot = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-ksnapshot-i18n
Internationalization and localization files for ksnapshot.

%description -n kdegraphics-ksnapshot-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksnapshota.

%package -n kdegraphics-kuickshow-i18n
Summary:	Internationalization and localization files for kuickshow
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kuickshow
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kuickshow = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kuickshow-i18n
Internationalization and localization files for kuickshow.

%description -n kdegraphics-kuickshow-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kuickshow.

%package -n kdegraphics-kview-i18n
Summary:	Internationalization and localization files for kview
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kview
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kview = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kview-i18n
Internationalization and localization files for kview.

%description -n kdegraphics-kview-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kview.

%package -n kdegraphics-ksvg-i18n
Summary:	Internationalization and localization files for ksvg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksvg
Group:		X11/Applications
Requires:	kdegraphics-ksvg = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-ksvg-i18n
Internationalization and localization files for ksvg.

%description -n kdegraphics-ksvg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksvg.

%package -n kdegraphics-kfax-i18n
Summary:	Internationalization and localization files for kfax
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfaksa
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kfax = %{kdegraphics_epoch}:%{version}
Requires:	kdegraphics-kview-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kfax-i18n
Internationalization and localization files for kfax.

%description -n kdegraphics-kfax-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfaksa.

%package -n kdegraphics-kmrml-i18n
Summary:	Internationalization and localization files for kmrml
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmrml
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kmrml = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kmrml-i18n
Internationalization and localization files for kmrml.

%description -n kdegraphics-kmrml-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmrml.

%package -n kdegraphics-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfile'a
Group:		X11/Applications
Requires:	kdegraphics-kfile = %{kdegraphics_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdegraphics-kfile-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfile'a.

%package -n kdeaddons-ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ark
Group:		X11/Applications
Requires:	kdeaddons-ark = %{kdeaddons_epoch}:%{version}
Requires:	kdeutils-ark-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-ark-i18n
Internationalization and localization files for ark.

%description -n kdeaddons-ark-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ark.

%package -n kdeaddons-lnkforward-i18n
Summary:	Internationalization and localization files for lnkforward
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lnkforward
Group:		X11/Applications
Requires:	kdeaddons-lnkforward = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-lnkforward-i18n
Internationalization and localization files for lnkforward.

%description -n kdeaddons-lnkforward-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla lnkforward.

%package -n kdeaddons-kvim-i18n
Summary:	Internationalization and localization files for kvim
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kvima
Group:		X11/Applications
Requires:	kdeaddons-kvim = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kvim-i18n
Internationalization and localization files for kvim.

%description -n kdeaddons-kvim-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kvima.

%package -n kde-decoration-kde1-i18n
Summary:	Internationalization and localization files for kde1
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde1
Group:		X11/Applications
Requires:	kde-decoration-kde1 = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-kde1-i18n
Internationalization and localization files for kde1.

%description -n kde-decoration-kde1-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde1.

%package -n kde-decoration-kstep-i18n
Summary:	Internationalization and localization files for kstep
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstep
Group:		X11/Applications
Requires:	kde-decoration-kstep = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-kstep-i18n
Internationalization and localization files for kstep.

%description -n kde-decoration-kstep-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kstep.

%package -n kde-decoration-openlook-i18n
Summary:	Internationalization and localization files for openlook
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla openlook
Group:		X11/Applications
Requires:	kde-decoration-openlook = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-openlook-i18n
Internationalization and localization files for openlook.

%description -n kde-decoration-openlook-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla openlook.

%package -n kde-decoration-riscos-i18n
Summary:	Internationalization and localization files for riscos
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla riscos
Group:		X11/Applications
Requires:	kde-decoration-riscos = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-riscos-i18n
Internationalization and localization files for riscos.

%description -n kde-decoration-riscos-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla riscos.

%package -n kde-decoration-system-i18n
Summary:	Internationalization and localization files for system
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla system
Group:		X11/Applications
Requires:	kde-decoration-system = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-system-i18n
Internationalization and localization files for system.

%description -n kde-decoration-system-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla system.

%package -n kdeaddons-kicker-i18n
Summary:	Internationalization and localization files for kicker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kickera
Group:		X11/Applications
Requires:	kdeaddons-kicker = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kicker-i18n
Internationalization and localization files for kicker.

%description -n kdeaddons-kicker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kickera.

%package -n kdeaddons-konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla konquerora
Group:		X11/Applications
Requires:	kdeaddons-konqueror = %{kdeaddons_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-konqueror-i18n
Internationalization and localization files for konqueror.

%description -n kdeaddons-konqueror-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla konquerora.

%package -n kdeaddons-kontact-i18n
Summary:	Internationalization and localization files for kontact
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kontact
Group:		X11/Applications
Requires:	kdeaddons-kontact = %{kdeaddons_epoch}:%{version}
Requires:	kdenetwork-knewsticker-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kontact-i18n
Internationalization and localization files for kontact.

%description -n kdeaddons-kontact-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kontact.

%package -n kdeaddons-ksig-i18n
Summary:	Internationalization and localization files for ksig
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksig
Group:		X11/Applications
Requires:	kdeaddons-ksig = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-ksig-i18n
Internationalization and localization files for ksig.

%description -n kdeaddons-ksig-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksig.

%package -n kdeaddons-kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaddressbook
Group:		X11/Applications
Requires:	kdeaddons-kaddressbook-plugins = %{kdeaddons_epoch}:%{version}
Requires:	kdepim-kaddressbook-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description -n kdeaddons-kaddressbook-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaddressbook.

%package -n kdeaddons-kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kate
Group:		X11/Applications
Requires:	kdeaddons-kate = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-kate-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kate-i18n
Internationalization and localization files for kate.

%description -n kdeaddons-kate-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kate.

%package -n kdeaddons-fsview-i18n
Summary:	Internationalization and localization files for fsview
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla fsview
Group:		X11/Applications
Requires:	kdeaddons-fsview = %{kdeaddons_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-fsview-i18n
Internationalization and localization files for fsview.

%description -n kdeaddons-fsview-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla fsview.

%package -n kdeaddons-noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla noatun
Group:		X11/Applications
Requires:	kdeaddons-noatun = %{kdeaddons_epoch}:%{version}
Requires:	kdemultimedia-noatun-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-noatun-i18n
Internationalization and localization files for noatun.

%description -n kdeaddons-noatun-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla noatun.

%package -n kdeaddons-atlantikdesigner-i18n
Summary:	Internationalization and localization files for atlantikdesigner
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla atlantikdesigner
Group:		X11/Applications
Requires:	kdeaddons-atlantikdesigner = %{kdeaddons_epoch}:%{version}
Requires:	kdegames-atlantik-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-atlantikdesigner-i18n
Internationalization and localization files for atlantikdesigner.

%description -n kdeaddons-atlantikdesigner-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla atlantikdesigner.

%package -n kdewebdev-kfilereplace-i18n
Summary:	Internationalization and localization files for kfilereplace
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfilereplace
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kfilereplace = %{kdewebdev_epoch}:%{version}
Obsoletes:	kdesdk-kfilereplace-i18n

%description -n kdewebdev-kfilereplace-i18n
Internationalization and localization files for kfilereplace.

%description -n kdewebdev-kfilereplace-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfilereplace.

%package -n kdewebdev-kimagemapeditor-i18n
Summary:	Internationalization and localization files for kimagemapeditor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kimagemapeditor
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kimagemapeditor = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-kimagemapeditor-i18n
Internationalization and localization files for kimagemapeditor.

%description -n kdewebdev-kimagemapeditor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kimagemapeditor.

%package -n kdewebdev-klinkstatus-i18n
Summary:	Internationalization and localization files for klinkstatus
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klinkstatus
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-klinkstatus = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-klinkstatus-i18n
Internationalization and localization files for klinkstatus.

%description -n kdewebdev-klinkstatus-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klinkstatus.

%package -n kdewebdev-kommander-i18n
Summary:	Internationalization and localization files for kommander
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kommander
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kommander = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-kommander-i18n
Internationalization and localization files for kommander.

%description -n kdewebdev-kommander-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kommander.

%package -n kdewebdev-kxsldbg-i18n
Summary:	Internationalization and localization files for kxsldbg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kxsldbg
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kxsldbg = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-kxsldbg-i18n
Internationalization and localization files for kxsldbg.

%description -n kdewebdev-kxsldbg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kxsldbg.

%package -n kdewebdev-quanta-i18n
Summary:	Internationalization and localization files for quanta
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla quanta
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-quanta = %{kdewebdev_epoch}:%{version}
Obsoletes:	quanta-i18n

%description -n kdewebdev-quanta-i18n
Internationalization and localization files for quanta.

%description -n kdewebdev-quanta-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla quanta.

%package -n kde-kgreet-classic-i18n
Summary:	KDE greeter libraries - i18n
Summary(pl):	Biblioteki s³u¿±ce do zapytañ o has³o - t³umaczenia
Group:		X11/Applications
Requires:	kde-kgreet-classic = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kde-kgreet-classic-i18n
Tools for asking for passwords in the classic, default look - i18n.

%description -n kde-kgreet-classic-i18n -l pl
Narzêdzia s³u¿±ce do zapytañ o has³o - klasyczny, domy¶lny motyw
wygl±du - t³umaczenia.

%prep
%setup -qcT %(seq -f '-a %g' 0 64 | xargs)

%build
export kde_htmldir="%{_kdedocdir}"
export kde_libs_htmldir="%{_kdedocdir}"

LDFLAGS="%{rpmldflags}"

for dir in kde-i18n-*-%{version}; do
	cd "$dir"
	%configure
	%{__make} \
		RPM_OPT_FLAGS="%{rpmcflags}" \
		kde_htmldir="%{_kdedocdir}" \
		kde_libs_htmldir="%{_kdedocdir}"
	cd ..
done

%install
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in kde-i18n-*-%{version}; do
		%{__make} -C "$dir" install \
			DESTDIR=$RPM_BUILD_ROOT \
			kde_htmldir="%{_kdedocdir}" \
			kde_libs_htmldir="%{_kdedocdir}"
	done

	# remove zero-length file
	find $RPM_BUILD_ROOT%{_kdedocdir} -size 0 -print0 | xargs -0 rm -vf

	# remove empty language catalogs (= 1 message only)
	find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

	rm -f __find.*
	touch installed.stamp
fi

rm -f *.lang

kde_find_lang() {
	%{?debug:set -x}
	local out=$1.lang
	shift
	> $out
	for a in $*; do
		%find_lang $a --with-kde tmp.lang
		cat tmp.lang >> $out
	done
	rm -f tmp.lang
}

kde_find_lang kde-decoration-common-i18n kwin_art_clients
kde_find_lang kde-kgreet-classic-i18n kgreet_classic
kde_find_lang kde-kio-imap4-i18n kio_imap4
kde_find_lang kde-kio-ldap-i18n kio_ldap
kde_find_lang kde-kio-nntp-i18n kio_nntp
kde_find_lang kde-kio-pop3-i18n kio_pop3
kde_find_lang kde-kio-smtp-i18n kio_smtp
kde_find_lang kdeaccessibility-kmag-i18n kmag
kde_find_lang kdeaccessibility-kmousetool-i18n kmousetool
kde_find_lang kdeaccessibility-kmouth-i18n kmouth
kde_find_lang kdeaddons-ark-i18n ark_plugin
kde_find_lang kdeaddons-atlantikdesigner-i18n atlantikdesigner
kde_find_lang kdeaddons-fsview-i18n fsview
kde_find_lang kdeaddons-kaddressbook-i18n libkaddrbk_geo_xxport
kde_find_lang kdeaddons-kate-i18n "
	kate-plugins
	katecppsymbolviewer
	katefiletemplates
	katefll_initplugin
	katefll_plugin
	katehelloworld
	katehtmltools
	kateinsertcommand
	katekjswrapper
	katemake
	katemodeline
	kateopenheader
	katepybrowse
	katetextfilter
	katexmlcheck
	katexmltools
	ktexteditor_autobookmarker
"

kde_find_lang kdeaddons-kicker-i18n "
	kicker-applets
	kmathapplet
	kolourpicker
	ktimemon
	mediacontrol
"

kde_find_lang kdeaddons-konqueror-i18n "
	audiorename_plugin
	autorefresh
	babelfish
	crashesplugin
	dirfilterplugin
	domtreeviewer
	imagerename_plugin
	imgalleryplugin
	kcmkuick
	kfile_cert
	kfile_folder
	kfile_html
	kfile_mhtml
	kfile_txt
	khtmlsettingsplugin
	konq-plugins
	konqsidebar_delicious
	konqsidebar_mediaplayer
	konqsidebar_metabar
	konqsidebar_news
	kuick_plugin
	minitoolsplugin
	searchbarplugin
	uachangerplugin
	validatorsplugin
	webarchiver
"

kde_find_lang kdeaddons-ksig-i18n ksig
kde_find_lang kdeaddons-lnkforward-i18n rellinks kfile_lnk
kde_find_lang kdeaddons-noatun-i18n "
	alsaplayerui
	charlatanui
	dub
	ffrs
	lyrics
	nexscope
	pitchablespeed
	synaescope
	tippecanoe
	tyler
	wakeup
	wavecapture
"

kde_find_lang kdeadmin-kcmlilo-i18n kcmlilo
kde_find_lang kdeadmin-kcron-i18n kcron
kde_find_lang kdeadmin-kdat-i18n kdat
kde_find_lang kdeadmin-kpackage-i18n kpackage kfile_deb kfile_rpm
kde_find_lang kdeadmin-ksysv-i18n ksysv secpolicy
kde_find_lang kdeadmin-kuser-i18n kuser
kde_find_lang kdeartwork-screensavers-i18n klock kpartsaver kxsconfig
kde_find_lang kdebase-core-i18n "
	colors
	drkonqi
	fonts
	kcmaccessibility
	kcmcolors
	kcmfonts
	kcmkded
	kcmlocale
	kcmprintmgr
	kcmstyle
	kdebugdialog
	kdeprint
	kdeprint_part
	kdesu
	kdesud
	khelpcenter
	khtmlkttsd
	kio_home
	kio_man
	kio_settings
	kio_thumbnail
	knetattach
	kprinter
	kstyle_keramik_config
	language
"
kde_find_lang kdebase-desktop-i18n "
	arts
	background
	bell
	clock
	clockapplet
	desktop
	desktopbehavior
	display
	dockbarextension
	energy
	joystick
	kaccess
	kasbarextension
	kbinaryclock
	kcmaccess
	kcmarts
	kcmbackground
	kcmbell
	kcmcomponentchooser
	kcmenergy
	kcminput
	kcmkclock
	kcmkeys
	kcmkicker
	kcmkwindecoration
	kcmkwinrules
	kcmkwm
	kcmkxmlrpcd
	kcmlaunch
	kcmnotify
	kcmsmserver
	kcmspellchecking
	kcmtaskbar
	kcmxinerama
	kdesktop
	keyboard
	keys
	khotkeys
	kicker
	kickermenu_kate
	kmenuapplet
	kmenuedit
	kminipagerapplet
	krandr
	krdb
	kreadconfig
	krunapplet
	ksmserver
	ksplash
	ksplashml
	kstart
	kstyle_plastik_config
	ksystemtrayapplet
	ksystraycmd
	ktaskbarapplet
	kthememanager
	ktip
	kwin
	kwindecoration
	kxkb
	kxmlrpcd
	libkicker
	libkickermenu_kdeprint
	libkickermenu_konsole
	libkickermenu_prefmenu
	libkickermenu_recentdocs
	libkickermenu_tom
	lockout
	mediaapplet
	mouse
	naughtyapplet
	panel
	panelappearance
	passwords
	privacy
	quicklauncher
	spellchecking
	taskbarextension
	windowmanagement
"
kde_find_lang kdebase-desktop-libs-i18n "
	ksplashthemes
	libtaskbar
	libtaskmanager
"

kde_find_lang kdebase-infocenter-i18n "
	kcminfo
	kcmioslaveinfo
	kcmnic
	kcmsamba
	kcmusb
	kcmview1394
	kinfocenter
	kioslave
"
kde_find_lang kdebase-kappfinder-i18n kappfinder
kde_find_lang kdebase-kate-i18n "
	kate
	katedefaultproject
	katetabbarextension
"
kde_find_lang kdebase-kdcop-i18n kdcop
kde_find_lang kdebase-kdeprintfax-i18n kdeprintfax
kde_find_lang kdebase-kdialog-i18n kdialog
kde_find_lang kdebase-kfind-i18n kfind kfindpart
kde_find_lang kdebase-kfontinst-i18n kcmfontinst kfontinst
kde_find_lang kdebase-kjobviewer-i18n kjobviewer
kde_find_lang kdebase-klipper-i18n klipper
kde_find_lang kdebase-konsole-i18n konsole kcmkonsole
kde_find_lang kdebase-kpager-i18n kpager
kde_find_lang kdebase-kpersonalizer-i18n kpersonalizer
kde_find_lang kdebase-ksysguard-i18n ksysguard
# XXX kwriteconfig != kwrite
kde_find_lang kdebase-kwrite-i18n kwrite kwriteconfig
kde_find_lang kdebase-screensavers-i18n screensaver kcmscreensaver kscreensaver
kde_find_lang kdebase-useraccount-i18n useraccount kdepasswd
kde_find_lang kdeedu-kalzium-i18n kalzium
kde_find_lang kdeedu-kanagram-i18n kanagram
kde_find_lang kdeedu-kbruch-i18n kbruch
kde_find_lang kdeedu-keduca-i18n keduca
kde_find_lang kdeedu-khangman-i18n khangman
kde_find_lang kdeedu-kig-i18n kig kfile_drgeo kfile_kig
kde_find_lang kdeedu-kiten-i18n kiten
kde_find_lang kdeedu-klatin-i18n klatin
kde_find_lang kdeedu-klettres-i18n klettres
kde_find_lang kdeedu-kmplot-i18n kmplot
kde_find_lang kdeedu-kpercentage-i18n kpercentage
kde_find_lang kdeedu-kstars-i18n kstars
kde_find_lang kdeedu-ktouch-i18n ktouch
kde_find_lang kdeedu-kturtle-i18n kturtle
kde_find_lang kdeedu-kverbos-i18n kverbos
kde_find_lang kdeedu-kvoctrain-i18n kvoctrain
kde_find_lang kdeedu-kwordquiz-i18n kwordquiz
kde_find_lang kdegames-atlantik-i18n atlantik
kde_find_lang kdegames-i18n libkdegames
kde_find_lang kdegames-kasteroids-i18n kasteroids
kde_find_lang kdegames-katomic-i18n katomic
kde_find_lang kdegames-kbackgammon-i18n kbackgammon
kde_find_lang kdegames-kbattleship-i18n kbattleship
kde_find_lang kdegames-kblackbox-i18n kblackbox
kde_find_lang kdegames-kbounce-i18n kbounce
kde_find_lang kdegames-kenolaba-i18n kenolaba
kde_find_lang kdegames-kfouleggs-i18n kfouleggs
kde_find_lang kdegames-kgoldrunner-i18n kgoldrunner
kde_find_lang kdegames-kjumpingcube-i18n kjumpingcube
kde_find_lang kdegames-klickety-i18n klickety
kde_find_lang kdegames-klines-i18n klines
kde_find_lang kdegames-kmahjongg-i18n kmahjongg
kde_find_lang kdegames-kmines-i18n kmines
kde_find_lang kdegames-kolf-i18n kolf
kde_find_lang kdegames-konquest-i18n konquest
kde_find_lang kdegames-kpat-i18n kpat
kde_find_lang kdegames-kpoker-i18n kpoker
kde_find_lang kdegames-kreversi-i18n kreversi
kde_find_lang kdegames-ksame-i18n ksame
kde_find_lang kdegames-kshisen-i18n kshisen
kde_find_lang kdegames-ksirtet-i18n ksirtet libksirtet
kde_find_lang kdegames-ksmiletris-i18n ksmiletris
kde_find_lang kdegames-ksnake-i18n ksnake
kde_find_lang kdegames-ksokoban-i18n ksokoban
kde_find_lang kdegames-kspaceduel-i18n kspaceduel
kde_find_lang kdegames-ktron-i18n ktron
kde_find_lang kdegames-ktuberling-i18n ktuberling
kde_find_lang kdegames-kwin4-i18n kwin4
kde_find_lang kdegames-lskat-i18n lskat
kde_find_lang kdegraphics-kamera-i18n kamera kcmkamera
kde_find_lang kdegraphics-kcoloredit-i18n kcoloredit
kde_find_lang kdegraphics-kdvi-i18n kdvi
kde_find_lang kdegraphics-kfax-i18n kfax
kde_find_lang kdegraphics-kfile-i18n "
	kfile_bmp
	kfile_dvi
	kfile_exr
	kfile_gif
	kfile_ico
	kfile_jpeg
	kfile_pcx
	kfile_pdf
	kfile_png
	kfile_pnm
	kfile_ps
	kfile_rgb
	kfile_tga
	kfile_tiff
	kfile_xbm
"
kde_find_lang kdegraphics-kgamma-i18n kgamma
kde_find_lang kdegraphics-kghostview-i18n kghostview
kde_find_lang kdegraphics-kiconedit-i18n kiconedit
kde_find_lang akmrml-i18n kmrml
kde_find_lang kdegraphics-kolourpaint-i18n kolourpaint # 'kpaint' obsoleted by kolourpaint?
kde_find_lang kdegraphics-kooka-i18n kooka libkscan
kde_find_lang kdegraphics-kpdf-i18n kpdf
kde_find_lang kdegraphics-kpovmodeler-i18n kpovmodeler
kde_find_lang kdegraphics-kruler-i18n kruler
kde_find_lang kdegraphics-ksnapshot-i18n ksnapshot
kde_find_lang kdegraphics-ksvg-i18n ksvgplugin
kde_find_lang kdegraphics-kuickshow-i18n kuickshow
kde_find_lang kdegraphics-kview-i18n "
	kcm_kviewcanvasconfig
	kcm_kviewgeneralconfig
	kcm_kviewpluginsconfig
	kcm_kviewviewerpluginsconfig
	kview
	kview_scale
	kviewbrowserplugin
	kviewcanvas
	kvieweffectsplugin
	kviewpresenterplugin
	kviewscannerplugin
	kviewshell
	kviewviewer
"
kde_find_lang kdelibs-i18n "
	common
	cupsdconf
	kabc_dir
	kabc_file
	kabc_ldapkio
	kabc_net
	kabc_sql
	kabcformat_binary
	katepart
	kcmshell
	kdelibs
	kdelibs_colors
	kdeprint
	kfileaudiopreview
	kio
	kio_help
	kioexec
	kmcop
	knotify
	kspell
	kstyle_highcontrast_config
	ktexteditor_docwordcompletion
	ktexteditor_insertfile
	ktexteditor_isearch
	ktexteditor_kdatatool
	kttsd
	libkholidays
	libkscreensaver
	ppdtranslations
	timezones
"
kde_find_lang kdemultimedia-arts-i18n artsmodules
kde_find_lang kdemultimedia-artsbuilder-i18n artsbuilder
kde_find_lang kdemultimedia-artscontrol-i18n artscontrol
kde_find_lang kdemultimedia-audiocd-i18n audiocd_encoder_lame audiocd_encoder_vorbis kcmaudiocd kio_audiocd
kde_find_lang kdemultimedia-juk-i18n juk
kde_find_lang kdemultimedia-kaboodle-i18n kaboodle
kde_find_lang kdemultimedia-kaudiocreator-i18n kaudiocreator
kde_find_lang kdemultimedia-kfile-i18n "
	kfile_au
	kfile_avi
	kfile_flac
	kfile_m3u
	kfile_mp3
	kfile_mpc
	kfile_ogg
	kfile_sid
	kfile_theora
	kfile_wav
"
kde_find_lang kdemultimedia-kmid-i18n kmid
kde_find_lang kdemultimedia-kmix-i18n kmix kmixcfg
kde_find_lang kdemultimedia-krec-i18n krec
kde_find_lang kdemultimedia-kscd-i18n kscd
kde_find_lang kdemultimedia-libkcddb-i18n libkcddb kcmcddb
kde_find_lang kdemultimedia-noatun-i18n noatun
kde_find_lang kdenetwork-filesharing-i18n kfileshare
kde_find_lang kdenetwork-kdict-i18n kdict kdictapplet
kde_find_lang kdenetwork-kget-i18n kget
kde_find_lang kdenetwork-kinetd-i18n kinetd
kde_find_lang kdenetwork-knewsticker-i18n knewsticker
kde_find_lang kdenetwork-kopete-i18n kopete kio_jabberdisco
kde_find_lang kdenetwork-kpf-i18n kpf
kde_find_lang kdenetwork-kppp-i18n kppp kppplogview
kde_find_lang kdenetwork-krfb-i18n kcm_krfb krfb krdc
kde_find_lang kdenetwork-ksirc-i18n ksirc
kde_find_lang kdenetwork-ktalkd-i18n ktalkd kcmktalkd
kde_find_lang kdenetwork-kwifimanager-i18n kwifimanager kwireless kcmwifi
kde_find_lang kdenetwork-lanbrowser-i18n lisa lanbrowser kcmlanbrowser kio_lan
kde_find_lang kdepim-i18n "
	akregator
	akregator_konqplugin
	kabc_slox
	kalarm
	kalarmd
	kcmkontactnt
	kdepimwizards
	kfile_ics
	kitchensync
	kontact
	korganizer
	kres_exchange
	kres_imap
	kres_remote
	kres_xmlrpc
	ksync
	multisynk
"
kde_find_lang kdepim-kaddressbook-i18n kabc2mutt kaddressbook kcmkabconfig kfile_vcf
kde_find_lang kdepim-kandy-i18n kandy
kde_find_lang kdepim-karm-i18n karm
kde_find_lang kdepim-kmail-i18n "
	kfile_rfc822
	kio_sieve
	kleopatra
	kmail
	kmail_text_calendar_plugin
	kmail_text_vcard_plugin
	kmailcvt
	ktnef
	kwatchgnupg
"
kde_find_lang kdepim-knode-i18n knode
kde_find_lang kdepim-knotes-i18n knotes
kde_find_lang kdepim-konsolekalendar-i18n konsolekalendar
kde_find_lang kdepim-korn-i18n korn
kde_find_lang kdepim-kpilot-i18n kpilot kfile_palm
kde_find_lang kdepim-libs-i18n "
	kdgantt
	kgantt
	libkcal
	libkdepim
	libkitchensync
	libkleopatra
	libkmime
	libkpgp
	libkpimexchange
	libksieve
	libksync
"
kde_find_lang kdesdk-cervisia-i18n cervisia
kde_find_lang kdesdk-kbabel-i18n kbabel
kde_find_lang kdesdk-kbugbuster-i18n kbugbuster
kde_find_lang kdesdk-kcachegrind-i18n kcachegrind
kde_find_lang kdesdk-kfile-i18n "
	kfile_cpp
	kfile_desktop
	kfile_diff
	kfile_po
	kfile_ts
"
kde_find_lang kdesdk-kompare-i18n kompare
kde_find_lang kdesdk-kspy-i18n spy
kde_find_lang kdesdk-kstartperf-i18n kstartperf
kde_find_lang kdesdk-kuiviewer-i18n kuiviewer
kde_find_lang kdesdk-libcvsservice-i18n cvsservice
kde_find_lang kdesdk-umbrello-i18n umbrello






%find_lang quanta	--with-kde
%find_lang kommander	--with-kde
%find_lang kxsldbg	--with-kde
%find_lang kimagemapeditor --with-kde
%find_lang klinkstatus	--with-kde


for a in $RPM_BUILD_ROOT%{_datadir}/apps/klatin/data/vocabs/*; do
	lang=${a##*/}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> kdeedu-klatin-i18n.lang
done

for a in $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/*.xml; do
	t=${a##*logokeywords.}
	lang=${t%.xml}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> kdeedu-kturtle-i18n.lang
done

for a in $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/*; do
	lang=${a##*/}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> kdeedu-kturtle-i18n.lang
done


# DON'T PACKAGE KMATHTOOL
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kmathtool.mo
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/*/kmathtool

for a in $RPM_BUILD_ROOT%{_datadir}/apps/kanagram/data/*; do
	lang=${a##*/}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> kdeedu-kanagram-i18n.lang
done


> i18n.lang
%find_lang libkdegames	--with-kde
cat libkdegames.lang >> i18n.lang
rm -f libkdegames.lang

%find_lang libkonq	--with-kde

%find_lang	kdm		--with-kde
a="
kdmconfig
kdmgreet
"
for i in $a; do
	%find_lang $i	--with-kde
	cat $i.lang >> kdm.lang
	rm -f $i.lang
done

%find_lang konqueror --with-kde
a="
appletproxy
cache
cookies
crypto
ebrowsing
email
extensionproxy
filemanager
filetypes
htmlsearch
icons
kcmcgi
kcmcrypto
kcmcss
kcmhtmlsearch
kcmicons
kcmkio
kcmkonq
kcmkonqhtml
kcmkurifilt
kcmlayout
kcmperformance
kfile_font
kfmclient
khtml
kio_finger
kio_fish
kio_floppy
kio_mac
kio_media
kio_nfs
kio_print
kio_remote
kio_sftp
kio_smb
kio_system
kio_tar
kio_trash
netpref
nsplugin
proxy
smb
useragent
"
for i in $a; do
	%find_lang $i	--with-kde
	cat $i.lang >> konqueror.lang
	rm -f $i.lang
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/*; do
	if [ -d $i ]; then
		z=`echo $i|sed -e s,$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/,,`
		echo "%lang($z) %{_datadir}/apps/ktuberling/sounds/$z" >> kdegames-ktuberling-i18n.lang
	fi
done



# Not packaging kmobile, it was disabled by coolo

%find_lang ark			--with-kde
%find_lang KRegExpEditor	--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde

%find_lang kdf			--with-kde
%find_lang blockdevices		--with-kde
cat blockdevices.lang >> kdf.lang
rm -f blockdevices.lang

%find_lang kedit		--with-kde
%find_lang kfloppy		--with-kde
%find_lang kgpg			--with-kde
%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
%find_lang klaptopdaemon	--with-kde
%find_lang kcmlowbatcrit	--with-kde
%find_lang kcmlowbatwarn	--with-kde
%find_lang laptop		--with-kde
%find_lang powerctrl		--with-kde
cat {kcmlowbatcrit,kcmlowbatwarn,laptop,powerctrl}.lang >> klaptopdaemon.lang
rm -f {kcmlowbatcrit,kcmlowbatwarn,laptop,powerctrl}.lang

%find_lang ksim			--with-kde
%find_lang ktimer		--with-kde
%find_lang kwallet		--with-kde
%find_lang kdelirc		--with-kde
%find_lang irkick		--with-kde
%find_lang kcmlirc		--with-kde
grep '\.mo' irkick.lang >> kdelirc.lang
grep '\.mo' kcmlirc.lang >> kdelirc.lang

%find_lang kwalletmanager	--with-kde
cat kwalletmanager.lang >> kwallet.lang
rm -f kwalletmanager.lang
%find_lang kcmkwallet		--with-kde
cat kcmkwallet.lang >> kwallet.lang
rm -f kcmkwallet.lang

%find_lang kcmlaptop		--with-kde
cat kcmlaptop.lang >> klaptopdaemon.lang
rm -f kcmlaptop.lang

a="
kcmkvaio
kcmthinkpad
kcmthinkpad
kmilo_delli8k
kmilo_generic
kmilo_kvaio
kmilo_powerbook
kmilo_thinkpad
kmilod
"
for i in $a; do
	%find_lang $i		--with-kde
	cat $i.lang >> kmilo.lang
	rm -f $i.lang
done

%find_lang kregexpeditor	--with-kde
cat kregexpeditor.lang >> KRegExpEditor.lang
rm -f kregexpeditor.lang

%find_lang kcharselectapplet	--with-kde
cat kcharselectapplet.lang >> kcharselect.lang
rm -f kcharselectapplet.lang

%find_lang kdessh		--with-kde

# We don't build kcardchooser (disabled by default by coolo)
# re-enabling it would be posssible, but what for?

for i in $(find $RPM_BUILD_ROOT%{_kdedocdir}  -maxdepth 1 -mindepth 1 -printf "%f\n"); do
	echo "%dir %{_kdedocdir}/${i}" >> kdelibs-i18n.lang
done

for a in $RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.*.xml; do
	t=${a##*/logohighlightstyle.}
	lang=${t%.xml}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> kdelibs-i18n.lang
done

%find_lang kfilereplace		--with-kde

%find_lang amor			--with-kde
%find_lang kmoon		--with-kde
%find_lang kodo			--with-kde
%find_lang kteatime		--with-kde
%find_lang kweather		--with-kde
%find_lang kworldclock		--with-kde
%find_lang kfifteenapplet	--with-kde
%find_lang ktux			--with-kde


%find_lang kdevelop --with-kde
a="
kde_app_devel
kdearch
kdevdesigner
kdevtipofday
qeditor
"
for i in $a; do
	%find_lang $i	--with-kde
	cat $i.lang >> kdevelop.lang
	rm -f $i.lang
done

for i in $RPM_BUILD_ROOT%{_datadir}/locale/*; do
	echo $i
	if [ -d $i ] ; then
		z=`echo $i|sed -e s,$RPM_BUILD_ROOT%{_datadir}/locale/,,`
		echo "%lang($z) %{_datadir}/locale/$z/[cef]*" >> kdebase-core-i18n.lang
	fi
done

%find_lang kcontrol --with-kde
grep '\.mo' kcontrol.lang >> kdebase-core-i18n.lang

sed -e 's,%{_prefix},%dir %{_prefix},g' kcontrol.lang | grep HTML >> kdebase-core-i18n.lang

for i in $RPM_BUILD_ROOT%{_kdedocdir}/*/kcontrol/index.docbook; do
	echo $i
	if [ -f $i ]; then
		z=`echo $i | sed -e "s,$RPM_BUILD_ROOT%{_kdedocdir},,g"`
		lang=`echo $z | cut -d'/' -f2`
		if [ -n "$lang" ] ; then
			echo -e "%lang($lang) %{_kdedocdir}/$lang/kcontrol/*.*" >> kdebase-core-i18n.lang
		fi
	fi
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/*; do
	echo $i
	if [ -d $i ]; then
		z=`echo $i|sed -e s,$RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/,,`
		echo "%lang($z) %{_datadir}/apps/khangman/data/$z" >> kdeedu-khangman-i18n.lang
	fi
done
for a in $RPM_BUILD_ROOT%{_datadir}/apps/khangman/*.txt; do
	t=${a##*/}
	lang=${t%.txt}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> kdeedu-khangman-i18n.lang
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/klettres/*; do
	echo $i
	if [ -d $i ]; then
		z=`echo $i|sed -e s,$RPM_BUILD_ROOT%{_datadir}/apps/klettres/,,`
		echo "%lang($z) %{_datadir}/apps/klettres/$z" >> kdeedu-klettres-i18n.lang
	fi
done

%if 0
#"
# TODO these *.lang are created but not included in any %package yet
%find_lang blinken --with-kde
#%find_lang flashkard --with-kde # obsoleted?
%find_lang kapptemplate --with-kde
%find_lang kdesvn-build --with-kde
%find_lang kgeography --with-kde
#%find_lang kmessedwords --with-kde # obsoleted?
%find_lang kmidi --with-kde
%find_lang knetworkconf --with-kde
%find_lang kompmgr --with-kde
%find_lang kttsd --with-kde
%find_lang kwuftpd --with-kde
%find_lang kxconfig --with-kde
%find_lang lilo-config --with-kde
%find_lang megami --with-kde
%find_lang multisynk --with-kde
%find_lang scripts --with-kde
%find_lang superkaramba --with-kde
%find_lang xsldbg --with-kde
%find_lang kcmsmartcard --with-kde
%find_lang kio_mobile --with-kde
%endif

# Get rid of messages about files listed twice.
for i in *.lang; do
	sort -u $i > $i.tmp && mv $i.tmp $i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-common-i18n -f kde-decoration-common-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kgreet-classic-i18n -f kde-kgreet-classic-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kio-imap4-i18n -f kde-kio-imap4-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kio-ldap-i18n -f kde-kio-ldap-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kio-nntp-i18n -f kde-kio-nntp-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kio-pop3-i18n -f kde-kio-pop3-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kio-smtp-i18n -f kde-kio-smtp-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmag-i18n -f kdeaccessibility-kmag-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmousetool-i18n -f kdeaccessibility-kmousetool-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmouth-i18n -f kdeaccessibility-kmouth-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-ark-i18n -f kdeaddons-ark-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-atlantikdesigner-i18n -f kdeaddons-atlantikdesigner-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-fsview-i18n -f kdeaddons-fsview-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kaddressbook-i18n -f kdeaddons-kaddressbook-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kate-i18n -f kdeaddons-kate-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kicker-i18n -f kdeaddons-kicker-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-konqueror-i18n -f kdeaddons-konqueror-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-ksig-i18n -f kdeaddons-ksig-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-lnkforward-i18n -f kdeaddons-lnkforward-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaddons-noatun-i18n -f kdeaddons-noatun-i18n.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kcmlilo-i18n -f kdeadmin-kcmlilo-i18n.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kcron-i18n -f kdeadmin-kcron-i18n.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kdat-i18n -f kdeadmin-kdat-i18n.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kpackage-i18n -f kdeadmin-kpackage-i18n.lang
%defattr(644,root,root,755)
%files -n kdeadmin-ksysv-i18n -f kdeadmin-ksysv-i18n.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kuser-i18n -f kdeadmin-kuser-i18n.lang
%defattr(644,root,root,755)
%files -n kdeartwork-screensavers-i18n -f kdeartwork-screensavers-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-core-i18n -f kdebase-core-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-desktop-i18n -f kdebase-desktop-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-desktop-libs-i18n -f kdebase-desktop-libs-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-infocenter-i18n -f kdebase-infocenter-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kappfinder-i18n -f kdebase-kappfinder-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kate-i18n -f kdebase-kate-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kdcop-i18n -f kdebase-kdcop-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kdeprintfax-i18n -f kdebase-kdeprintfax-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kdialog-i18n -f kdebase-kdialog-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kfind-i18n -f kdebase-kfind-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kfontinst-i18n -f kdebase-kfontinst-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kjobviewer-i18n -f kdebase-kjobviewer-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-klipper-i18n -f kdebase-klipper-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-konsole-i18n -f kdebase-konsole-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kpager-i18n -f kdebase-kpager-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kpersonalizer-i18n -f kdebase-kpersonalizer-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-ksysguard-i18n -f kdebase-ksysguard-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-kwrite-i18n -f kdebase-kwrite-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-screensavers-i18n -f kdebase-screensavers-i18n.lang
%defattr(644,root,root,755)
%files -n kdebase-useraccount-i18n -f kdebase-useraccount-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kalzium-i18n -f kdeedu-kalzium-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kanagram-i18n -f kdeedu-kanagram-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kbruch-i18n -f kdeedu-kbruch-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-keduca-i18n -f kdeedu-keduca-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-khangman-i18n -f kdeedu-khangman-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kig-i18n -f kdeedu-kig-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kiten-i18n -f kdeedu-kiten-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-klatin-i18n -f kdeedu-klatin-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-klettres-i18n -f kdeedu-klettres-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kmplot-i18n -f kdeedu-kmplot-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kpercentage-i18n -f kdeedu-kpercentage-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kstars-i18n -f kdeedu-kstars-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-ktouch-i18n -f kdeedu-ktouch-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kturtle-i18n -f kdeedu-kturtle-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kverbos-i18n -f kdeedu-kverbos-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kvoctrain-i18n -f kdeedu-kvoctrain-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kwordquiz-i18n -f kdeedu-kwordquiz-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-atlantik-i18n -f kdegames-atlantik-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-i18n -f kdegames-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kasteroids-i18n -f kdegames-kasteroids-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-katomic-i18n -f kdegames-katomic-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kbackgammon-i18n -f kdegames-kbackgammon-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kbattleship-i18n -f kdegames-kbattleship-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kblackbox-i18n -f kdegames-kblackbox-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kbounce-i18n -f kdegames-kbounce-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kenolaba-i18n -f kdegames-kenolaba-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kfouleggs-i18n -f kdegames-kfouleggs-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kgoldrunner-i18n -f kdegames-kgoldrunner-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kjumpingcube-i18n -f kdegames-kjumpingcube-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-klickety-i18n -f kdegames-klickety-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-klines-i18n -f kdegames-klines-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kmahjongg-i18n -f kdegames-kmahjongg-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kmines-i18n -f kdegames-kmines-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kolf-i18n -f kdegames-kolf-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-konquest-i18n -f kdegames-konquest-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kpat-i18n -f kdegames-kpat-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kpoker-i18n -f kdegames-kpoker-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kreversi-i18n -f kdegames-kreversi-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ksame-i18n -f kdegames-ksame-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kshisen-i18n -f kdegames-kshisen-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ksirtet-i18n -f kdegames-ksirtet-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ksmiletris-i18n -f kdegames-ksmiletris-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ksnake-i18n -f kdegames-ksnake-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ksokoban-i18n -f kdegames-ksokoban-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kspaceduel-i18n -f kdegames-kspaceduel-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ktron-i18n -f kdegames-ktron-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-ktuberling-i18n -f kdegames-ktuberling-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-kwin4-i18n -f kdegames-kwin4-i18n.lang
%defattr(644,root,root,755)
%files -n kdegames-lskat-i18n -f kdegames-lskat-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kamera-i18n -f kdegraphics-kamera-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kcoloredit-i18n -f kdegraphics-kcoloredit-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kdvi-i18n -f kdegraphics-kdvi-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kfax-i18n -f kdegraphics-kfax-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kfile-i18n -f kdegraphics-kfile-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kgamma-i18n -f kdegraphics-kgamma-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kghostview-i18n -f kdegraphics-kghostview-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kiconedit-i18n -f kdegraphics-kiconedit-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kmrml-i18n -f kdegraphics-kmrml-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kolourpaint-i18n -f kdegraphics-kolourpaint-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kooka-i18n -f kdegraphics-kooka-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kpdf-i18n -f kdegraphics-kpdf-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kpovmodeler-i18n -f kdegraphics-kpovmodeler-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kruler-i18n -f kdegraphics-kruler-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-ksnapshot-i18n -f kdegraphics-ksnapshot-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-ksvg-i18n -f kdegraphics-ksvg-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kuickshow-i18n -f kdegraphics-kuickshow-i18n.lang
%defattr(644,root,root,755)
%files -n kdegraphics-kview-i18n -f kdegraphics-kview-i18n.lang
%defattr(644,root,root,755)
%files -n kdelibs-i18n -f kdelibs-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-arts-i18n -f kdemultimedia-arts-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-artsbuilder-i18n -f kdemultimedia-artsbuilder-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-artscontrol-i18n -f kdemultimedia-artscontrol-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-audiocd-i18n -f kdemultimedia-audiocd-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-juk-i18n -f kdemultimedia-juk-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kaboodle-i18n -f kdemultimedia-kaboodle-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kaudiocreator-i18n -f kdemultimedia-kaudiocreator-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kfile-i18n -f kdemultimedia-kfile-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kmid-i18n -f kdemultimedia-kmid-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kmix-i18n -f kdemultimedia-kmix-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-krec-i18n -f kdemultimedia-krec-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kscd-i18n -f kdemultimedia-kscd-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-libkcddb-i18n -f kdemultimedia-libkcddb-i18n.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-noatun-i18n -f kdemultimedia-noatun-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-filesharing-i18n -f kdenetwork-filesharing-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kdict-i18n -f kdenetwork-kdict-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kget-i18n -f kdenetwork-kget-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kinetd-i18n -f kdenetwork-kinetd-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-knewsticker-i18n -f kdenetwork-knewsticker-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kopete-i18n -f kdenetwork-kopete-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kpf-i18n -f kdenetwork-kpf-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kppp-i18n -f kdenetwork-kppp-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-krfb-i18n -f kdenetwork-krfb-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-ksirc-i18n -f kdenetwork-ksirc-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-ktalkd-i18n -f kdenetwork-ktalkd-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kwifimanager-i18n -f kdenetwork-kwifimanager-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-lanbrowser-i18n -f kdenetwork-lanbrowser-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-i18n -f kdepim-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-kaddressbook-i18n -f kdepim-kaddressbook-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-kandy-i18n -f kdepim-kandy-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-karm-i18n -f kdepim-karm-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-kmail-i18n -f kdepim-kmail-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-knode-i18n -f kdepim-knode-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-knotes-i18n -f kdepim-knotes-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-konsolekalendar-i18n -f kdepim-konsolekalendar-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-korn-i18n -f kdepim-korn-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-kpilot-i18n -f kdepim-kpilot-i18n.lang
%defattr(644,root,root,755)
%files -n kdepim-libs-i18n -f kdepim-libs-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-cervisia-i18n -f kdesdk-cervisia-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kbabel-i18n -f kdesdk-kbabel-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kbugbuster-i18n -f kdesdk-kbugbuster-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kcachegrind-i18n -f kdesdk-kcachegrind-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kfile-i18n -f kdesdk-kfile-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kompare-i18n -f kdesdk-kompare-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kspy-i18n -f kdesdk-kspy-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kstartperf-i18n -f kdesdk-kstartperf-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-kuiviewer-i18n -f kdesdk-kuiviewer-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-libcvsservice-i18n -f kdesdk-libcvsservice-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-umbrello-i18n -f kdesdk-umbrello-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-amor-i18n -f amor.lang
%defattr(644,root,root,755)
%files -n kdetoys-fifteen-i18n -f kfifteenapplet.lang
%defattr(644,root,root,755)
%files -n kdetoys-kmoon-i18n -f kmoon.lang
%defattr(644,root,root,755)
%files -n kdetoys-kodo-i18n -f kodo.lang
%defattr(644,root,root,755)
%files -n kdetoys-kteatime-i18n -f kteatime.lang
%defattr(644,root,root,755)
%files -n kdetoys-ktux-i18n -f ktux.lang
%defattr(644,root,root,755)
%files -n kdetoys-kweather-i18n -f kweather.lang
%defattr(644,root,root,755)
%files -n kdetoys-kworldclock-i18n -f kworldclock.lang
%defattr(644,root,root,755)
%files -n kdeutils-ark-i18n -f ark.lang
%defattr(644,root,root,755)
%files -n kdeutils-kcalc-i18n -f kcalc.lang
%defattr(644,root,root,755)
%files -n kdeutils-kcharselect-i18n -f kcharselect.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdelirc-i18n -f kdelirc.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdessh-i18n -f kdessh.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdf-i18n -f kdf.lang
%defattr(644,root,root,755)
%files -n kdeutils-kedit-i18n -f kedit.lang
%defattr(644,root,root,755)
%files -n kdeutils-kfloppy-i18n -f kfloppy.lang
%defattr(644,root,root,755)
%files -n kdeutils-kgpg-i18n -f kgpg.lang
%defattr(644,root,root,755)
%files -n kdeutils-khexedit-i18n -f khexedit.lang
%defattr(644,root,root,755)
%files -n kdeutils-kjots-i18n -f kjots.lang
%defattr(644,root,root,755)
%files -n kdeutils-klaptopdaemon-i18n -f klaptopdaemon.lang
%defattr(644,root,root,755)
%files -n kdeutils-kmilo-i18n -f kmilo.lang
%defattr(644,root,root,755)
%files -n kdeutils-kregexpeditor-i18n -f KRegExpEditor.lang
%defattr(644,root,root,755)
%files -n kdeutils-ksim-i18n -f ksim.lang
%defattr(644,root,root,755)
%files -n kdeutils-ktimer-i18n -f ktimer.lang
%defattr(644,root,root,755)
%files -n kdeutils-kwalletmanager-i18n -f kwallet.lang
%defattr(644,root,root,755)
%files -n kdevelop-i18n -f kdevelop.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kfilereplace-i18n -f kfilereplace.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kimagemapeditor-i18n -f kimagemapeditor.lang
%defattr(644,root,root,755)
%files -n kdewebdev-klinkstatus-i18n -f klinkstatus.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kommander-i18n -f kommander.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kxsldbg-i18n -f kxsldbg.lang
%defattr(644,root,root,755)
%files -n kdewebdev-quanta-i18n -f quanta.lang
%defattr(644,root,root,755)
%files -n kdm-i18n -f kdm.lang
%defattr(644,root,root,755)
%files -n konqueror-i18n -f konqueror.lang
%defattr(644,root,root,755)
%files -n konqueror-libs-i18n -f libkonq.lang
%defattr(644,root,root,755)
