%define		_name			kde-i18n
%define		kdeacces_epoch		0
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
%define		kdepim_epoch		3
%define		kdesdk_epoch		3
%define		kdetoys_epoch		9
%define		kdeutils_epoch		9
%define		kdevelop_epoch		7
%define		kdevelop_version	3.0.4
%define		kdewebdev_epoch		2
#
Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu jêzyków
Name:		kdemodule-i18n
Version:	3.3.2
Release:	0.1
Epoch:		10
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{_name}-%{version}.tar.bz2
# Source0-md5:	20135e722cd5f94cbe4997765941b455
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
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Bengali
Obsoletes:	kde-i18n-Basque
Obsoletes:	kde-i18n-Farsi
Obsoletes:	kde-i18n-Galician
Obsoletes:	kde-i18n-Low_Saxon
Obsoletes:	kde-i18n-Tajik
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Punjabi
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Upper_Sorbian
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n
Obsoletes:	kdeaccessibility-i18n
Obsoletes:	kdeaddons-i18n
Obsoletes:	kdeadmin-i18n
Obsoletes:	kdeartwork-i18n
Obsoletes:	kdeedu-i18n
Obsoletes:	kdegraphics-i18n
Obsoletes:	kdemultimedia-i18n
Obsoletes:	kdenetwork-i18n
Obsoletes:	kdesdk-i18n
Obsoletes:	kdetoys-i18n
Obsoletes:	kdeutils-i18n
Obsoletes:	kdebase-mailnews-i18n
Obsoletes:	kdeedu-flashkard-i18n

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
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kfind-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kjobviewer-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kpager-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-kmenuedit-i18n
Obsoletes:	kdebase-kicker-i18n 
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
Requires:	kdebase-infocenter = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-infocenter-i18n
Internationalization and localization files for KDE Information
Centre.

%description -n kdebase-infocenter-i18n -l pl
T³umaczenia dla centrum informacji o systemie w KDE.

%package -n kdebase-kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl):	T³umaczenia dla kate
Group:		X11/Applications
Requires:	kdebase-kate = %{kdebase_epoch}:%{version}
Requires:	kdebase-common-filemanagement-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kate-i18n
Internationalization and localization files for kate.

%description -n kdebase-kate-i18n -l pl
T³umaczenia dla kate.

%package -n kdebase-kfind-i18n
Summary:	Internationalization and localization files for kfind
Summary(pl):	T³umaczenia dla kfind
Group:		X11/Applications
Requires:	kdebase-kfind = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kfind-i18n
Internationalization and localization files for kfind.

%description -n kdebase-kfind-i18n -l pl
T³umaczenia dla kfind.

%package -n kdebase-kfontinst-i18n
Summary:	Internationalization and localization files for kfontinst
Summary(pl):	T³umaczenia dla kfontinst
Group:		X11/Applications
Requires:	kdebase-kfontinst = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kfontinst-i18n
Internationalization and localization files for kfontinst.

%description -n kdebase-kfontinst-i18n -l pl
T³umaczenia dla kfontinst.

%package -n kdebase-klipper-i18n
Summary:	Internationalization and localization files for klipper
Summary(pl):	T³umaczenia dla klippera
Group:		X11/Applications
Requires:	kdebase-klipper = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-klipper-i18n
Internationalization and localization files for klipper.

%description -n kdebase-klipper-i18n -l pl
T³umaczenia dla klippera.

%package -n kdebase-konsole-i18n
Summary:	Internationalization and localization files for konsole
Summary(pl):	T³umaczenia dla konsole
Group:		X11/Applications
Requires:	kdebase-konsole = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdebase-ksysguard = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-klipper-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-ksysguard-i18n
Internationalization and localization files for ksysguard.

%description -n kdebase-ksysguard-i18n -l pl
T³umaczenia dla ksysguarda.

%package -n kdebase-kwrite-i18n
Summary:	Internationalization and localization files for kwrite
Summary(pl):	T³umaczenia dla kwrite
Group:		X11/Applications
Requires:	kdebase-kwrite = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kwrite-i18n
Internationalization and localization files for kwrite.

%description -n kdebase-kwrite-i18n -l pl
T³umaczenia dla kwrite.

%package -n kdebase-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	T³umaczenia dla screensavers
Group:		X11/Applications
Requires:	kdebase-screensavers = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdebase-screensavers-i18n -l pl
T³umaczenia dla screensavers.

%package -n kdm-i18n
Summary:	Internationalization and localization files for kdm
Summary(pl):	T³umaczenia dla kdm-a
Group:		X11/Applications
Requires:	kdm = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdm-i18n
Internationalization and localization files for kdm.

%description -n kdm-i18n -l pl
T³umaczenia dla kdm-a.

%package -n konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl):	T³umaczenia dla konquerora
Group:		X11/Applications
Requires:	konqueror = %{kdebase_epoch}:%{version}
Requires:	kdebase-common-filemanagement-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-konsole-i18n = %{epoch}:%{version}-%{release}
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
Requires:	kde-decoration-modernsys = %{kdebase_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-modernsys-i18n
Internationalization and localization files for
kde-decoration-modernsys.

%description -n kde-decoration-modernsys-i18n -l pl
T³umaczenia dla kde-decoration-modernsys.

%package -n kde-decoration-quartz-i18n
Summary:	Internationalization and localization files for kde-decoration-quartz
Summary(pl):	T³umaczenia dla kde-decoration-quartz
Group:		X11/Applications
Requires:	kde-decoration-quartz = %{kdebase_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-quartz-i18n
Internationalization and localization files for kde-decoration-quartz.

%description -n kde-decoration-quartz-i18n -l pl
T³umaczenia dla kde-decoration-quartz.

%package -n kdebase-common-filemanagement-i18n
Summary:	Internationalization and localization files for common-filemanagement
Summary(pl):	T³umaczenia dla common-filemanagement
Group:		X11/Applications
Requires:	kdebase-common-filemanagement = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-common-filemanagement-i18n
Internationalization and localization files for common-filemanagement.

%description -n kdebase-common-filemanagement-i18n -l pl
T³umaczenia dla common-filemanagement.

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
Requires:	kdebase-kdcop = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kdcop-i18n
Internationalization and localization files for kdcop.

%description -n kdebase-kdcop-i18n -l pl
T³umaczenia dla kdcopa.

%package -n kdebase-kdeprintfax-i18n
Summary:	Internationalization and localization files for kdeprintfax
Summary(pl):	T³umaczenia dla kdeprintfax
Group:		X11/Applications
Requires:	kdebase-kdeprintfax = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdebase-kjobviewer = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kjobviewer-i18n
Internationalization and localization files for kjobviewer.

%description -n kdebase-kjobviewer-i18n -l pl
T³umaczenia dla kjobviewera.

%package -n kdebase-kpersonalizer-i18n
Summary:	Internationalization and localization files for kpersonalizer
Summary(pl):	T³umaczenia dla kpersonalizera
Group:		X11/Applications
Requires:	kdebase-kpersonalizer = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

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

%package -n kde-kio-newimap4-i18n
Summary:	Internationalization and localization files for newimap4 ioslave
Summary(pl):	T³umaczenia dla newimap4 ioslave
Group:		X11/Applications
Requires:	kde-kio-newimap4 = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kde-kio-newimap4-i18n
Internationalization and localization files for newimap4 ioslave.

%description -n kde-kio-newimap4-i18n -l pl
T³umaczenia dla newimap4 ioslave.

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
Requires:	kdevelop = %{kdevelop_epoch}:%{kdevelop_version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdevelop-i18n
Internationalization and localization files for kdevelop.

%description -n kdevelop-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdevelopa.

%package -n kdepim-kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl):	T³umaczenia dla kaddressbook
Group:		X11/Applications
Requires:	kdepim-kaddressbook = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description -n kdepim-kaddressbook-i18n -l pl
T³umaczenia dla kaddressbook.

%package -n kdepim-kandy-i18n
Summary:	Internationalization and localization files for kandy
Summary(pl):	T³umaczenia dla kandy
Group:		X11/Applications
Requires:	kdepim-kandy = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdepim-kmail = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-smtp-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-imap4-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-pop3-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-ktnef-i18n

%description -n kdepim-kmail-i18n
Internationalization and localization files for kmail.

%description -n kdepim-kmail-i18n -l pl
T³umaczenia dla kmaila.

%package -n kdepim-knode-i18n
Summary:	Internationalization and localization files for knode
Summary(pl):	T³umaczenia dla knode
Group:		X11/Applications
Requires:	kdepim-knode = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-smtp-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-nntp-i18n = %{epoch}:%{version}-%{release}

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
Obsoletes:	kdepim-korganizer-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-kontact-i18n
Obsoletes:	kdepim-kresources-i18n
Obsoletes:	kdeaddons-kontact-i18n

%description -n kdepim-i18n
Internationalization and localization files for kdepim.

%description -n kdepim-i18n -l pl
T³umaczenia dla kdepim.

%package -n kdepim-korn-i18n
Summary:	Internationalization and localization files for korn
Summary(pl):	T³umaczenia dla korna
Group:		X11/Applications
Requires:	kdepim-korn = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdepim-libs = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-libkcal-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-libkdgantt-i18n
Obsoletes:	kdepim-libkdepim-i18n
Obsoletes:	kdepim-libkdenetwork-i18n
Obsoletes:	kdepim-kmail-libs-i18n

%description -n kdepim-libs-i18n
Internationalization and localization files for kdepim libraries.

%description -n kdepim-libs-i18n -l pl
T³umaczenia dla bibliotek kdepim.

%package -n kdeutils-ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arka
Group:		X11/Applications
Requires:	kdeutils-ark = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-ark-i18n
Internationalization and localization files for ark.

%description -n kdeutils-ark-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arka.

%package -n kdeutils-kcalc-i18n
Summary:	Internationalization and localization files for kcalc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcalca
Group:		X11/Applications
Requires:	kdeutils-kcalc = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kcalc-i18n
Internationalization and localization files for kcalc.

%description -n kdeutils-kcalc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcalca.

%package -n kdeutils-kcharselect-i18n
Summary:	Internationalization and localization files for kcharselect
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharselecta
Group:		X11/Applications
Requires:	kdeutils-kcharselect = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kcharselect-i18n
Internationalization and localization files for kcharselect.

%description -n kdeutils-kcharselect-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharselecta.

%package -n kdeutils-kdf-i18n
Summary:	Internationalization and localization files for kdf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdf
Group:		X11/Applications
Requires:	kdeutils-kdf = %{kdeutils_epoch}:%{version}
Requires:	kdebase-infocenter-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kdf-i18n
Internationalization and localization files for kdf.

%description -n kdeutils-kdf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdf.

%package -n kdeutils-kedit-i18n
Summary:	Internationalization and localization files for kedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	kdeutils-kedit = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kedit-i18n
Internationalization and localization files for kedit.

%description -n kdeutils-kedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kedita.

%package -n kdeutils-kmilo-i18n
Summary:	Internationalization and localization files for kmilo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	kdeutils-kmilo = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kmilo-i18n
Internationalization and localization files for kmilo.

%description -n kdeutils-kmilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmilo.

%package -n kdeutils-kfloppy-i18n
Summary:	Internationalization and localization files for kfloppy
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfloppy
Group:		X11/Applications
Requires:	kdeutils-kfloppy = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kfloppy-i18n
Internationalization and localization files for kfloppy.

%description -n kdeutils-kfloppy-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfloppy.

%package -n kdeutils-kgpg-i18n
Summary:	Internationalization and localization files for kgpg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgpg
Group:		X11/Applications
Requires:	kdeutils-kgpg = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kgpg-i18n
Internationalization and localization files for kgpg.

%description -n kdeutils-kgpg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgpg.

%package -n kdeutils-khexedit-i18n
Summary:	Internationalization and localization files for khexedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khexedita
Group:		X11/Applications
Requires:	kdeutils-khexedit = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-khexedit-i18n
Internationalization and localization files for khexedit.

%description -n kdeutils-khexedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khexedita.

%package -n kdeutils-kjots-i18n
Summary:	Internationalization and localization files for kjots
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjots
Group:		X11/Applications
Requires:	kdeutils-kjots = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kjots-i18n
Internationalization and localization files for kjots.

%description -n kdeutils-kjots-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjots.

%package -n kdeutils-klaptopdaemon-i18n
Summary:	Internationalization and localization files for klaptopdaemon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klaptopdaemona
Group:		X11/Applications
Requires:	kdeutils-klaptopdaemon = %{kdeutils_epoch}:%{version}
Requires:	kdebase-infocenter-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-klaptopdaemon-i18n
Internationalization and localization files for klaptopdaemon.

%description -n kdeutils-klaptopdaemon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klaptopdaemona.

%package -n kdeutils-kregexpeditor-i18n
Summary:	Internationalization and localization files for kregexpeditor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kregexpeditora
Group:		X11/Applications
Requires:	kdeutils-kregexpeditor = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kregexpeditor-i18n
Internationalization and localization files for kregexpeditor.

%description -n kdeutils-kregexpeditor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kregexpeditora.

%package -n kdeutils-ksim-i18n
Summary:	Internationalization and localization files for ksim
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksima
Group:		X11/Applications
Requires:	kdeutils-ksim = %{kdeutils_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-ksim-i18n
Internationalization and localization files for ksim.

%description -n kdeutils-ksim-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksima.

%package -n kdeutils-ktimer-i18n
Summary:	Internationalization and localization files for ktimer
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktimera
Group:		X11/Applications
Requires:	kdeutils-ktimer = %{kdeutils_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-ktimer-i18n
Internationalization and localization files for ktimer.

%description -n kdeutils-ktimer-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktimera.

%package -n kdeutils-kwalletmanager-i18n
Summary:	Internationalization and localization files for kwalletmanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwalletmanagera
Group:		X11/Applications
Requires:	kdeutils-kwalletmanager = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kwalletmanager-i18n
Internationalization and localization files for kwalletmanager.

%description -n kdeutils-kwalletmanager-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwalletmanagera.

%package -n kdeutils-kdelirc-i18n
Summary:	Internationalization and localization files for kdelirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdelirca
Group:		X11/Applications
Requires:	kdeutils-kdelirc = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeutils-kdelirc-i18n
Internationalization and localization files for kdelirc.

%description -n kdeutils-kdelirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdelirca.

%package -n kdeutils-kdessh-i18n
Summary:	Internationalization and localization files for kdessh
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdessh
Group:		X11/Applications
Requires:	kdeutils-kdessh = %{kdeutils_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

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
Obsoletes:	kdeutils-userinfo-i18n
Obsoletes:	kdeutils-kdepasswd-i18n

%description -n kdebase-useraccount-i18n
Internationalization and localization files for useraccount.

%description -n kdebase-useraccount-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla useraccount.

%package -n kdeaccessibility-kmag-i18n
Summary:	Internationalization and localization files for kmag
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmag
Group:		X11/Applications
Requires:	kdeaccessibility-kmag = %{kdeacces_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmag-i18n
Internationalization and localization files for kmag.

%description -n kdeaccessibility-kmag-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmag.

%package -n kdeaccessibility-kmousetool-i18n
Summary:	Internationalization and localization files for kmousetool
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmousetool
Group:		X11/Applications
Requires:	kdeaccessibility-kmousetool = %{kdeacces_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmousetool-i18n
Internationalization and localization files for kmousetool.

%description -n kdeaccessibility-kmousetool-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmousetool.

%package -n kdeaccessibility-kmouth-i18n
Summary:	Internationalization and localization files for kmouth
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmouth
Group:		X11/Applications
Requires:	kdeaccessibility-kmouth = %{kdeacces_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmouth-i18n
Internationalization and localization files for kmouth.

%description -n kdeaccessibility-kmouth-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmouth.

%package -n kdenetwork-filesharing-i18n
Summary:	Internationalization and localization files for fileshare
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla fileshare
Group:		X11/Applications
Requires:	kdenetwork-filesharing = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-filesharing-i18n
Internationalization and localization files for fileshare.

%description -n kdenetwork-filesharing-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla fileshare.

%package -n kdenetwork-kdict-i18n
Summary:	Internationalization and localization files for kdict
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdict
Group:		X11/Applications
Requires:	kdenetwork-kdict = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-kdict-i18n
Internationalization and localization files for kdict.

%description -n kdenetwork-kdict-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdict.

%package -n kdenetwork-kinetd-i18n
Summary:	Internationalization and localization files for kinetd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kinetd
Group:		X11/Applications
Requires:	kdenetwork-kinetd = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-kinetd-i18n
Internationalization and localization files for kinetd.

%description -n kdenetwork-kinetd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kinetd.

%package -n kdenetwork-kget-i18n
Summary:	Internationalization and localization files for kget
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgeta
Group:		X11/Applications
Requires:	kdenetwork-kget = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-kget-i18n
Internationalization and localization files for kget.

%description -n kdenetwork-kget-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgeta.

%package -n kdenetwork-knewsticker-i18n
Summary:	Internationalization and localization files for knewsticker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla knewstickera
Group:		X11/Applications
Requires:	kdenetwork-knewsticker = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-knewsticker-i18n
Internationalization and localization files for knewsticker.

%description -n kdenetwork-knewsticker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla knewstickera.

%package -n kdenetwork-kopete-i18n
Summary:	Internationalization and localization files for kopete
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kopete
Group:		X11/Applications
Requires:	kdenetwork-kopete = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-kopete-i18n
Internationalization and localization files for kopete.

%description -n kdenetwork-kopete-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kopete.

%package -n kdenetwork-kpf-i18n
Summary:	Internationalization and localization files for kpf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpf
Group:		X11/Applications
Requires:	kdenetwork-kpf = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-kpf-i18n
Internationalization and localization files for kpf.

%description -n kdenetwork-kpf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpf.

%package -n kdenetwork-kppp-i18n
Summary:	Internationalization and localization files for kppp
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kppp
Group:		X11/Applications
Requires:	kdenetwork-kppp = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-kppp-i18n
Internationalization and localization files for kppp.

%description -n kdenetwork-kppp-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kppp.

%package -n kdenetwork-krfb-i18n
Summary:	Internationalization and localization files for krfb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krfb
Group:		X11/Applications
Requires:	kdenetwork-krfb = %{kdenetwork_epoch}:%{version}
Requires:	kdenetwork-kinetd-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-krfb-i18n
Internationalization and localization files for krfb.

%description -n kdenetwork-krfb-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krfb.

%package -n kdenetwork-ksirc-i18n
Summary:	Internationalization and localization files for ksirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirc
Group:		X11/Applications
Requires:	kdenetwork-ksirc = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-ksirc-i18n
Internationalization and localization files for ksirc.

%description -n kdenetwork-ksirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksirc.

%package -n kdenetwork-ktalkd-i18n
Summary:	Internationalization and localization files for ktalkd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktalkd
Group:		X11/Applications
Requires:	kdenetwork-ktalkd = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-ktalkd-i18n
Internationalization and localization files for ktalkd.

%description -n kdenetwork-ktalkd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktalkd.

%package -n kdenetwork-kwifimanager-i18n
Summary:	Internationalization and localization files for kwifimanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwifimanagera
Group:		X11/Applications
Requires:	kdenetwork-kwifimanager = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdenetwork-rss = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-rss-i18n
Internationalization and localization files for rss.

%description -n kdenetwork-rss-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla rss.

%package -n kdemultimedia-artsbuilder-i18n
Summary:	Internationalization and localization files for artsbuilder
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artsbuildera
Group:		X11/Applications
Requires:	kdemultimedia-artsbuilder = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-arts-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-artsbuilder-i18n
Internationalization and localization files for artsbuilder.

%description -n kdemultimedia-artsbuilder-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artsbuildera.

%package -n kdemultimedia-artscontrol-i18n
Summary:	Internationalization and localization files for artscontrol
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artscontrol
Group:		X11/Applications
Requires:	kdemultimedia-artscontrol = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-arts-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-artscontrol-i18n
Internationalization and localization files for artscontrol.

%description -n kdemultimedia-artscontrol-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artscontrol.

%package -n kdemultimedia-arts-i18n
Summary:	Internationalization and localization files for arts
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arts
Group:		X11/Applications
Requires:	kdemultimedia-arts = %{kdemultimedia_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-arts-i18n
Internationalization and localization files for arts.

%description -n kdemultimedia-arts-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arts.

%package -n kdemultimedia-juk-i18n
Summary:	Internationalization and localization files for juk
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla juk
Group:		X11/Applications
Requires:	kdemultimedia-juk = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-juk-i18n
Internationalization and localization files for juk.

%description -n kdemultimedia-juk-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla juk.

%package -n kdemultimedia-kaboodle-i18n
Summary:	Internationalization and localization files for kaboodle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaboodle
Group:		X11/Applications
Requires:	kdemultimedia-kaboodle = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kaboodle-i18n
Internationalization and localization files for kaboodle.

%description -n kdemultimedia-kaboodle-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaboodle.

%package -n kdemultimedia-kmid-i18n
Summary:	Internationalization and localization files for kmid
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmid
Group:		X11/Applications
Requires:	kdemultimedia-kmid = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kmid-i18n
Internationalization and localization files for kmid.

%description -n kdemultimedia-kmid-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmid.

%package -n kdemultimedia-kmix-i18n
Summary:	Internationalization and localization files for kmix
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmix
Group:		X11/Applications
Requires:	kdemultimedia-kmix = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kmix-i18n
Internationalization and localization files for kmix.

%description -n kdemultimedia-kmix-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmix.

%package -n kdemultimedia-kscd-i18n
Summary:	Internationalization and localization files for kscd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kscd
Group:		X11/Applications
Requires:	kdemultimedia-kscd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kscd-i18n
Internationalization and localization files for kscd.

%description -n kdemultimedia-kscd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kscd.

%package -n kdemultimedia-krec-i18n
Summary:	Internationalization and localization files for krec
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krec
Group:		X11/Applications
Requires:	kdemultimedia-krec = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-artscontrol-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmix-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-krec-i18n
Internationalization and localization files for krec.

%description -n kdemultimedia-krec-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krec.

%package -n kdemultimedia-noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla noatun
Group:		X11/Applications
Requires:	kdemultimedia-noatun = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdemultimedia-libkcddb = %{kdemultimedia_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

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

%description -n kdeadmin-kcmlilo-i18n
Internationalization and localization files for kcmlilo.

%description -n kdeadmin-kcmlilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlilo.

%package -n kdeadmin-kcmlinuz-i18n
Summary:	Internationalization and localization files for kcmlinuz
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcmlinuz
Group:		X11/Applications
Requires:	kdeadmin-kcmlinuz = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kcmlinuz-i18n
Internationalization and localization files for kcmlinuz.

%description -n kdeadmin-kcmlinuz-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlinuz.

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
Requires:	kde-decoration-icewm = %{kdeartwork_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-icewm-i18n
Internationalization and localization files for kde-decoration-icewm.

%description -n kde-decoration-icewm-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm.

%package -n kde-decoration-glow-i18n
Summary:	Internationalization and localization files for kde-decoration-glow
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow
Group:		X11/Applications
Requires:	kde-decoration-glow = %{kdeartwork_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-glow-i18n
Internationalization and localization files for kde-decoration-glow.

%description -n kde-decoration-glow-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow.

%package -n kde-decoration-plastik-i18n
Summary:	Internationalization and localization files for kde-decoration-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik
Group:		X11/Applications
Requires:	kde-decoration-plastik = %{kdeartwork_epoch}:%{version}
Requires:	kde-decoration-common-i18n = %{epoch}:%{version}-%{release}

%description -n kde-decoration-plastik-i18n
Internationalization and localization files for
kde-decoration-plastik.

%description -n kde-decoration-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik.

%package -n kde-style-plastik-i18n
Summary:	Internationalization and localization files for kde-style-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-style-plastik
Group:		X11/Applications
Requires:	kde-style-plastik = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kde-style-plastik-i18n
Internationalization and localization files for kde-style-plastik.

%description -n kde-style-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-style-plastik.

%package -n kde-decoration-common-i18n
Summary:	Common internationalization and localization files for kwin decorations
Summary(pl):	Wspólne pliki umiêdzynarodawiaj±ce dla dekoracji kwin
Group:		X11/Applications

%description -n kde-decoration-common-i18n
Common internationalization and localization files for kwin decorations.

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
Requires:	kdeedu-kwordquiz = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kwordquiz-i18n
Internationalization and localization files for kwordquiz.

%description -n kdeedu-kwordquiz-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwordquiz.

%package -n kdeedu-kturtle-i18n
Summary:	Internationalization and localization files for kturtle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kturtle
Group:		X11/Applications
Requires:	kdeedu-kturtle = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kturtle-i18n
Internationalization and localization files for kturtle.

%description -n kdeedu-kturtle-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kturtle.

%package -n kdeedu-klatin-i18n
Summary:	Internationalization and localization files for klatin
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klatin
Group:		X11/Applications
Requires:	kdeedu-klatin = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-klatin-i18n
Internationalization and localization files for klatin.

%description -n kdeedu-klatin-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klatin.

%package -n kdeedu-flashkard-i18n
Summary:	Internationalization and localization files for flashkard
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla flashkarda
Group:		X11/Applications
Requires:	kdeedu-flashkard = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-flashkard-i18n
Internationalization and localization files for flashkard.

%description -n kdeedu-flashkard-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla flashkarda.

%package -n kdeedu-kalzium-i18n
Summary:	Internationalization and localization files for kalzium
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kalzium
Group:		X11/Applications
Requires:	kdeedu-kalzium = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kalzium-i18n
Internationalization and localization files for kalzium.

%description -n kdeedu-kalzium-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kalzium.

%package -n kdeedu-kbruch-i18n
Summary:	Internationalization and localization files for kbruch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbrucha
Group:		X11/Applications
Requires:	kdeedu-kbruch = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kbruch-i18n
Internationalization and localization files for kbruch.

%description -n kdeedu-kbruch-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbrucha.

%package -n kdeedu-keduca-i18n
Summary:	Internationalization and localization files for keduca
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla keduca
Group:		X11/Applications
Requires:	kdeedu-keduca = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-keduca-i18n
Internationalization and localization files for keduca.

%description -n kdeedu-keduca-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla keduca.

%package -n kdeedu-khangman-i18n
Summary:	Internationalization and localization files for khangman
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khangmana
Group:		X11/Applications
Requires:	kdeedu-khangman = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-khangman-i18n
Internationalization and localization files for khangman.

%description -n kdeedu-khangman-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khangmana.

%package -n kdeedu-kig-i18n
Summary:	Internationalization and localization files for kig
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kig
Group:		X11/Applications
Requires:	kdeedu-kig = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kig-i18n
Internationalization and localization files for kig.

%description -n kdeedu-kig-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kig.

%package -n kdeedu-kiten-i18n
Summary:	Internationalization and localization files for kiten
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kiten
Group:		X11/Applications
Requires:	kdeedu-kiten = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kiten-i18n
Internationalization and localization files for kiten.

%description -n kdeedu-kiten-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kiten.

%package -n kdeedu-klettres-i18n
Summary:	Internationalization and localization files for klettres
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klettres
Group:		X11/Applications
Requires:	kdeedu-klettres = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-klettres-i18n
Internationalization and localization files for klettres.

%description -n kdeedu-klettres-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klettres.

%package -n kdeedu-kmessedwords-i18n
Summary:	Internationalization and localization files for kmessedwords
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmessedwords
Group:		X11/Applications
Requires:	kdeedu-kmessedwords = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kmessedwords-i18n
Internationalization and localization files for kmessedwords.

%description -n kdeedu-kmessedwords-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmessedwords.

%package -n kdeedu-kmplot-i18n
Summary:	Internationalization and localization files for kmplot
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmplot
Group:		X11/Applications
Requires:	kdeedu-kmplot = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kmplot-i18n
Internationalization and localization files for kmplot.

%description -n kdeedu-kmplot-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmplot.

%package -n kdeedu-kpercentage-i18n
Summary:	Internationalization and localization files for kpercentage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpercentage
Group:		X11/Applications
Requires:	kdeedu-kpercentage = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kpercentage-i18n
Internationalization and localization files for kpercentage.

%description -n kdeedu-kpercentage-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpercentage.

%package -n kdeedu-kstars-i18n
Summary:	Internationalization and localization files for kstars
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstars
Group:		X11/Applications
Requires:	kdeedu-kstars = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kstars-i18n
Internationalization and localization files for kstars.

%description -n kdeedu-kstars-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kstars.

%package -n kdeedu-ktouch-i18n
Summary:	Internationalization and localization files for ktouch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktouch
Group:		X11/Applications
Requires:	kdeedu-ktouch = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-ktouch-i18n
Internationalization and localization files for ktouch.

%description -n kdeedu-ktouch-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktouch.

%package -n kdeedu-kverbos-i18n
Summary:	Internationalization and localization files for kverbos
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kverbos
Group:		X11/Applications
Requires:	kdeedu-kverbos = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kverbos-i18n
Internationalization and localization files for kverbos.

%description -n kdeedu-kverbos-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kverbos.

%package -n kdeedu-kvoctrain-i18n
Summary:	Internationalization and localization files for kvoctrain
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kvoctrain
Group:		X11/Applications
Requires:	kdeedu-kvoctrain = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeedu-kvoctrain-i18n
Internationalization and localization files for kvoctrain.

%description -n kdeedu-kvoctrain-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kvoctrain.

%package -n kdegames-i18n
Summary:	Internationalization and localization files for kdegames libs
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla bibliotek kdegames
Group:		X11/Applications
Requires:	kdegames = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-i18n
Internationalization and localization files for kdegames libs.

%description -n kdegames-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla bibliotek kdegames.

%package -n kdegames-kmahjongg-i18n
Summary:	Internationalization and localization files for kmahjongg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmahjongga
Group:		X11/Applications
Requires:	kdegames-kmahjongg = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kmahjongg-i18n
Internationalization and localization files for kmahjongg.

%description -n kdegames-kmahjongg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmahjongga.

%package -n kdegames-ksmiletris-i18n
Summary:	Internationalization and localization files for ksmiletris
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksmiletrisa
Group:		X11/Applications
Requires:	kdegames-ksmiletris = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdegames-kasteroids = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kasteroids-i18n
Internationalization and localization files for kasteroids.

%description -n kdegames-kasteroids-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kasteroids.

%package -n kdegames-katomic-i18n
Summary:	Internationalization and localization files for katomic
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla katomic
Group:		X11/Applications
Requires:	kdegames-katomic = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-katomic-i18n
Internationalization and localization files for katomic.

%description -n kdegames-katomic-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla katomic.

%package -n kdegames-kbackgammon-i18n
Summary:	Internationalization and localization files for kbackgammon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbackgammona
Group:		X11/Applications
Requires:	kdegames-kbackgammon = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kbackgammon-i18n
Internationalization and localization files for kbackgammon.

%description -n kdegames-kbackgammon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbackgammona.

%package -n kdegames-kbattleship-i18n
Summary:	Internationalization and localization files for kbattleship
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbattleship
Group:		X11/Applications
Requires:	kdegames-kbattleship = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kbattleship-i18n
Internationalization and localization files for kbattleship.

%description -n kdegames-kbattleship-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbattleship.

%package -n kdegames-kblackbox-i18n
Summary:	Internationalization and localization files for kblackbox
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kblackboksa
Group:		X11/Applications
Requires:	kdegames-kblackbox = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kblackbox-i18n
Internationalization and localization files for kblackbox.

%description -n kdegames-kblackbox-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kblackboksa.

%package -n kdegames-kbounce-i18n
Summary:	Internationalization and localization files for kbounce
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbounce
Group:		X11/Applications
Requires:	kdegames-kbounce = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kbounce-i18n
Internationalization and localization files for kbounce.

%description -n kdegames-kbounce-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbounce.

%package -n kdegames-kenolaba-i18n
Summary:	Internationalization and localization files for kenolaba
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kenolaby
Group:		X11/Applications
Requires:	kdegames-kenolaba = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kenolaba-i18n
Internationalization and localization files for kenolaba.

%description -n kdegames-kenolaba-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kenolaby.

%package -n kdegames-kfouleggs-i18n
Summary:	Internationalization and localization files for kfouleggs
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfouleggs
Group:		X11/Applications
Requires:	kdegames-kfouleggs = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kfouleggs-i18n
Internationalization and localization files for kfouleggs.

%description -n kdegames-kfouleggs-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfouleggs.

%package -n kdegames-kgoldrunner-i18n
Summary:	Internationalization and localization files for kgoldrunner
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgoldrunnera
Group:		X11/Applications
Requires:	kdegames-kgoldrunner = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kgoldrunner-i18n
Internationalization and localization files for kgoldrunner.

%description -n kdegames-kgoldrunner-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgoldrunnera.

%package -n kdegames-kjumpingcube-i18n
Summary:	Internationalization and localization files for kjumpingcube
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjumpingcube
Group:		X11/Applications
Requires:	kdegames-kjumpingcube = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kjumpingcube-i18n
Internationalization and localization files for kjumpingcube.

%description -n kdegames-kjumpingcube-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjumpingcube.

%package -n kdegames-klickety-i18n
Summary:	Internationalization and localization files for klickety
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klickety
Group:		X11/Applications
Requires:	kdegames-klickety = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-klickety-i18n
Internationalization and localization files for klickety.

%description -n kdegames-klickety-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klickety.

%package -n kdegames-klines-i18n
Summary:	Internationalization and localization files for klines
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klines
Group:		X11/Applications
Requires:	kdegames-klines = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-klines-i18n
Internationalization and localization files for klines.

%description -n kdegames-klines-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klines.

%package -n kdegames-kmines-i18n
Summary:	Internationalization and localization files for kmines
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmines
Group:		X11/Applications
Requires:	kdegames-kmines = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kmines-i18n
Internationalization and localization files for kmines.

%description -n kdegames-kmines-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmines.

%package -n kdegames-kolf-i18n
Summary:	Internationalization and localization files for kolf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kolfa
Group:		X11/Applications
Requires:	kdegames-kolf = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kolf-i18n
Internationalization and localization files for kolf.

%description -n kdegames-kolf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kolfa.

%package -n kdegames-konquest-i18n
Summary:	Internationalization and localization files for konquest
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla konquesta
Group:		X11/Applications
Requires:	kdegames-konquest = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-konquest-i18n
Internationalization and localization files for konquest.

%description -n kdegames-konquest-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla konquesta.

%package -n kdegames-kpat-i18n
Summary:	Internationalization and localization files for kpat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpata
Group:		X11/Applications
Requires:	kdegames-kpat = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kpat-i18n
Internationalization and localization files for kpat.

%description -n kdegames-kpat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpata.

%package -n kdegames-kpoker-i18n
Summary:	Internationalization and localization files for kpoker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpokera
Group:		X11/Applications
Requires:	kdegames-kpoker = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kpoker-i18n
Internationalization and localization files for kpoker.

%description -n kdegames-kpoker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpokera.

%package -n kdegames-kreversi-i18n
Summary:	Internationalization and localization files for kreversi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kreversi
Group:		X11/Applications
Requires:	kdegames-kreversi = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kreversi-i18n
Internationalization and localization files for kreversi.

%description -n kdegames-kreversi-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kreversi.

%package -n kdegames-ksame-i18n
Summary:	Internationalization and localization files for ksame
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksame
Group:		X11/Applications
Requires:	kdegames-ksame = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-ksame-i18n
Internationalization and localization files for ksame.

%description -n kdegames-ksame-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksame.

%package -n kdegames-kshisen-i18n
Summary:	Internationalization and localization files for kshisen
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kshisen
Group:		X11/Applications
Requires:	kdegames-kshisen = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kshisen-i18n
Internationalization and localization files for kshisen.

%description -n kdegames-kshisen-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kshisen.

%package -n kdegames-ksirtet-i18n
Summary:	Internationalization and localization files for ksirtet
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirteta
Group:		X11/Applications
Requires:	kdegames-ksirtet = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-ksirtet-i18n
Internationalization and localization files for ksirtet.

%description -n kdegames-ksirtet-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksirteta.

%package -n kdegames-ksnake-i18n
Summary:	Internationalization and localization files for ksnake
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksnake'a
Group:		X11/Applications
Requires:	kdegames-ksnake = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-ksnake-i18n
Internationalization and localization files for ksnake.

%description -n kdegames-ksnake-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksnake'a.

%package -n kdegames-ksokoban-i18n
Summary:	Internationalization and localization files for ksokoban
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksokobana
Group:		X11/Applications
Requires:	kdegames-ksokoban = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-ksokoban-i18n
Internationalization and localization files for ksokoban.

%description -n kdegames-ksokoban-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksokobana.

%package -n kdegames-kspaceduel-i18n
Summary:	Internationalization and localization files for kspaceduel
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspaceduel
Group:		X11/Applications
Requires:	kdegames-kspaceduel = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kspaceduel-i18n
Internationalization and localization files for kspaceduel.

%description -n kdegames-kspaceduel-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kspaceduel.

%package -n kdegames-ktron-i18n
Summary:	Internationalization and localization files for ktron
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktrona
Group:		X11/Applications
Requires:	kdegames-ktron = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-ktron-i18n
Internationalization and localization files for ktron.

%description -n kdegames-ktron-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktrona.

%package -n kdegames-ktuberling-i18n
Summary:	Internationalization and localization files for ktuberling
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktuberlinga
Group:		X11/Applications
Requires:	kdegames-ktuberling = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-ktuberling-i18n
Internationalization and localization files for ktuberling.

%description -n kdegames-ktuberling-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktuberlinga.

%package -n kdegames-kwin4-i18n
Summary:	Internationalization and localization files for kwin4
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwin4
Group:		X11/Applications
Requires:	kdegames-kwin4 = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-kwin4-i18n
Internationalization and localization files for kwin4.

%description -n kdegames-kwin4-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwin4.

%package -n kdegames-lskat-i18n
Summary:	Internationalization and localization files for lskat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lskata
Group:		X11/Applications
Requires:	kdegames-lskat = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-lskat-i18n
Internationalization and localization files for lskat.

%description -n kdegames-lskat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla lskata.

%package -n kdegames-megami-i18n
Summary:	Internationalization and localization files for megami
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla megami
Group:		X11/Applications
Requires:	kdegames-megami = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdesdk-cervisia = %{kdesdk_epoch}:%{version}
Requires:	kdesdk-libcvsservice-i18n = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-cervisia-i18n
Internationalization and localization files for cervisia.

%description -n kdesdk-cervisia-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla cervisii.

%package -n kdesdk-kbabel-i18n
Summary:	Internationalization and localization files for kbabel
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbabel
Group:		X11/Applications
Requires:	kdesdk-kbabel = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kbabel-i18n
Internationalization and localization files for kbabel.

%description -n kdesdk-kbabel-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbabel.

%package -n kdesdk-kbugbuster-i18n
Summary:	Internationalization and localization files for kbugbuster
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbugbustera
Group:		X11/Applications
Requires:	kdesdk-kbugbuster = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kbugbuster-i18n
Internationalization and localization files for kbugbuster.

%description -n kdesdk-kbugbuster-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbugbustera.

%package -n kdesdk-kcachegrind-i18n
Summary:	Internationalization and localization files for kcachegrind
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcachegrinda
Group:		X11/Applications
Requires:	kdesdk-kcachegrind = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kcachegrind-i18n
Internationalization and localization files for kcachegrind.

%description -n kdesdk-kcachegrind-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcachegrinda.

%package -n kdesdk-kompare-i18n
Summary:	Internationalization and localization files for kompare
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kompare
Group:		X11/Applications
Requires:	kdesdk-kompare = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kompare-i18n
Internationalization and localization files for kompare.

%description -n kdesdk-kompare-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kompare.

%package -n kdesdk-kstartperf-i18n
Summary:	Internationalization and localization files for kstartperf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstartperfa
Group:		X11/Applications
Requires:	kdesdk-kstartperf = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kstartperf-i18n
Internationalization and localization files for kstartperf.

%description -n kdesdk-kstartperf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kstartperfa.

%package -n kdesdk-kuiviewer-i18n
Summary:	Internationalization and localization files for kuiviewer
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kuiviewera
Group:		X11/Applications
Requires:	kdesdk-kuiviewer = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kuiviewer-i18n
Internationalization and localization files for kuiviewer.

%description -n kdesdk-kuiviewer-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kuiviewera.

%package -n kdesdk-kspy-i18n
Summary:	Internationalization and localization files for kspy
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspy
Group:		X11/Applications
Requires:	kdesdk-kspy = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-spy-i18n

%description -n kdesdk-kspy-i18n
Internationalization and localization files for spy.

%description -n kdesdk-kspy-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla spy.

%package -n kdesdk-umbrello-i18n
Summary:	Internationalization and localization files for umbrello
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla umbrello
Group:		X11/Applications
Requires:	kdesdk-umbrello = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-umbrello-i18n
Internationalization and localization files for umbrello.

%description -n kdesdk-umbrello-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla umbrello.

%package -n kdetoys-amor-i18n
Summary:	Internationalization and localization files for amor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla amora
Group:		X11/Applications
Requires:	kdetoys-amor = %{kdetoys_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-amor-i18n
Internationalization and localization files for amor.

%description -n kdetoys-amor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla amora.

%package -n kdetoys-kmoon-i18n
Summary:	Internationalization and localization files for kmoon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmoon
Group:		X11/Applications
Requires:	kdetoys-kmoon = %{kdetoys_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kmoon-i18n
Internationalization and localization files for kmoon.

%description -n kdetoys-kmoon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmoon.

%package -n kdetoys-kodo-i18n
Summary:	Internationalization and localization files for kodo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kodo
Group:		X11/Applications
Requires:	kdetoys-kodo = %{kdetoys_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kodo-i18n
Internationalization and localization files for kodo.

%description -n kdetoys-kodo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kodo.

%package -n kdetoys-kteatime-i18n
Summary:	Internationalization and localization files for kteatime
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kteatime
Group:		X11/Applications
Requires:	kdetoys-kteatime = %{kdetoys_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kteatime-i18n
Internationalization and localization files for kteatime.

%description -n kdetoys-kteatime-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kteatime.

%package -n kdetoys-kweather-i18n
Summary:	Internationalization and localization files for kweather
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kweather
Group:		X11/Applications
Requires:	kdetoys-kweather = %{kdetoys_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kweather-i18n
Internationalization and localization files for kweather.

%description -n kdetoys-kweather-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kweather.

%package -n kdetoys-kworldclock-i18n
Summary:	Internationalization and localization files for kworldclock
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kworldclocka
Group:		X11/Applications
Requires:	kdetoys-kworldclock = %{kdetoys_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kworldclock-i18n
Internationalization and localization files for kworldclock.

%description -n kdetoys-kworldclock-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kworldclocka.

%package -n kdetoys-ktux-i18n
Summary:	Internationalization and localization files for ktux
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktuksa
Group:		X11/Applications
Requires:	kdetoys-ktux = %{kdetoys_epoch}:%{version}
Requires:	kdebase-screensavers-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-ktux-i18n
Internationalization and localization files for ktux.

%description -n kdetoys-ktux-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktuksa.

%package -n kdetoys-fifteen-i18n
Summary:	Internationalization and localization files for fifteen
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla fifteen
Group:		X11/Applications
Requires:	kdetoys-fifteen = %{kdetoys_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-fifteen-i18n
Internationalization and localization files for fifteen.

%description -n kdetoys-fifteen-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla fifteen.

%package -n kdegraphics-kamera-i18n
Summary:	Internationalization and localization files for kamera
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla programu kamera
Group:		X11/Applications
Requires:	kdegraphics-kamera = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kamera-i18n
Internationalization and localization files for kamera.

%description -n kdegraphics-kamera-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla programu kamera.

%package -n kdegraphics-kcoloredit-i18n
Summary:	Internationalization and localization files for kcoloredit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcoloredita
Group:		X11/Applications
Requires:	kdegraphics-kcoloredit = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kcoloredit-i18n
Internationalization and localization files for kcoloredit.

%description -n kdegraphics-kcoloredit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcoloredita.

%package -n kdegraphics-kdvi-i18n
Summary:	Internationalization and localization files for kdvi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdvi
Group:		X11/Applications
Requires:	kdegraphics-kdvi = %{kdegraphics_epoch}:%{version}
Requires:	kdegraphics-kview-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kdvi-i18n
Internationalization and localization files for kdvi.

%description -n kdegraphics-kdvi-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdvi.

%package -n kdegraphics-kgamma-i18n
Summary:	Internationalization and localization files for kgamma
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgamma
Group:		X11/Applications
Requires:	kdegraphics-kgamma = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kgamma-i18n
Internationalization and localization files for kgamma.

%description -n kdegraphics-kgamma-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgamma.

%package -n kdegraphics-kghostview-i18n
Summary:	Internationalization and localization files for kghostview
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kghostview
Group:		X11/Applications
Requires:	kdegraphics-kghostview = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kghostview-i18n
Internationalization and localization files for kghostview.

%description -n kdegraphics-kghostview-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kghostview.

%package -n kdegraphics-kiconedit-i18n
Summary:	Internationalization and localization files for kiconedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kiconedita
Group:		X11/Applications
Requires:	kdegraphics-kiconedit = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kiconedit-i18n
Internationalization and localization files for kiconedit.

%description -n kdegraphics-kiconedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kiconedita.

%package -n kdegraphics-kooka-i18n
Summary:	Internationalization and localization files for kooka
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kooki
Group:		X11/Applications
Requires:	kdegraphics-kooka = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kooka-i18n
Internationalization and localization files for kooka.

%description -n kdegraphics-kooka-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kooki.

%package -n kdegraphics-kolourpaint-i18n
Summary:	Internationalization and localization files for kolourpaint
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kolourpaint
Group:		X11/Applications
Requires:	kdegraphics-kolourpaint = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdegraphics-kpaint-i18n

%description -n kdegraphics-kolourpaint-i18n
Internationalization and localization files for kolourpaint.

%description -n kdegraphics-kolourpaint-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kolourpaint.

%package -n kdegraphics-kpdf-i18n
Summary:	Internationalization and localization files for kpdf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpdf
Group:		X11/Applications
Requires:	kdegraphics-kpdf = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kpdf-i18n
Internationalization and localization files for kpdf.

%description -n kdegraphics-kpdf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpdf.

%package -n kdegraphics-kpovmodeler-i18n
Summary:	Internationalization and localization files for kpovmodeler
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpovmodelera
Group:		X11/Applications
Requires:	kdegraphics-kpovmodeler = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kpovmodeler-i18n
Internationalization and localization files for kpovmodeler.

%description -n kdegraphics-kpovmodeler-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpovmodelera.

%package -n kdegraphics-kruler-i18n
Summary:	Internationalization and localization files for kruler
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krulera
Group:		X11/Applications
Requires:	kdegraphics-kruler = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kruler-i18n
Internationalization and localization files for kruler.

%description -n kdegraphics-kruler-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krulera.

%package -n kdegraphics-ksnapshot-i18n
Summary:	Internationalization and localization files for ksnapshot
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksnapshota
Group:		X11/Applications
Requires:	kdegraphics-ksnapshot = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-ksnapshot-i18n
Internationalization and localization files for ksnapshot.

%description -n kdegraphics-ksnapshot-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksnapshota.

%package -n kdegraphics-kuickshow-i18n
Summary:	Internationalization and localization files for kuickshow
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kuickshow
Group:		X11/Applications
Requires:	kdegraphics-kuickshow = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kuickshow-i18n
Internationalization and localization files for kuickshow.

%description -n kdegraphics-kuickshow-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kuickshow.

%package -n kdegraphics-kview-i18n
Summary:	Internationalization and localization files for kview
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kview
Group:		X11/Applications
Requires:	kdegraphics-kview = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdegraphics-kfax = %{kdegraphics_epoch}:%{version}
Requires:	kdegraphics-kview-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kfax-i18n
Internationalization and localization files for kfax.

%description -n kdegraphics-kfax-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfaksa.

%package -n kdegraphics-kmrml-i18n
Summary:	Internationalization and localization files for kmrml
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmrml
Group:		X11/Applications
Requires:	kdegraphics-kmrml = %{kdegraphics_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

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
Requires:	kdewebdev-kfilereplace = %{kdewebdev_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-kfilereplace-i18n

%description -n kdewebdev-kfilereplace-i18n
Internationalization and localization files for kfilereplace.

%description -n kdewebdev-kfilereplace-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfilereplace.

%package -n kdewebdev-kimagemapeditor-i18n
Summary:	Internationalization and localization files for kimagemapeditor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kimagemapeditor
Group:		X11/Applications
Requires:	kdewebdev-kimagemapeditor = %{kdewebdev_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdewebdev-kimagemapeditor-i18n
Internationalization and localization files for kimagemapeditor.

%description -n kdewebdev-kimagemapeditor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kimagemapeditor.

%package -n kdewebdev-klinkstatus-i18n
Summary:	Internationalization and localization files for klinkstatus
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klinkstatus
Group:		X11/Applications
Requires:	kdewebdev-klinkstatus = %{kdewebdev_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdewebdev-klinkstatus-i18n
Internationalization and localization files for klinkstatus.

%description -n kdewebdev-klinkstatus-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klinkstatus.

%package -n kdewebdev-kommander-i18n
Summary:	Internationalization and localization files for kommander
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kommander
Group:		X11/Applications
Requires:	kdewebdev-kommander = %{kdewebdev_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdewebdev-kommander-i18n
Internationalization and localization files for kommander.

%description -n kdewebdev-kommander-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kommander.

%package -n kdewebdev-kxsldbg-i18n
Summary:	Internationalization and localization files for kxsldbg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kxsldbg
Group:		X11/Applications
Requires:	kdewebdev-kxsldbg = %{kdewebdev_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdewebdev-kxsldbg-i18n
Internationalization and localization files for kxsldbg.

%description -n kdewebdev-kxsldbg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kxsldbg.

%package -n kdewebdev-quanta-i18n
Summary:	Internationalization and localization files for quanta
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla quanta
Group:		X11/Applications
Requires:	kdewebdev-quanta = %{kdewebdev_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
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
%setup -q -n %{_name}-%{version}

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_libs_htmldir="%{_kdedocdir}"; export kde_libs_htmldir

LDFLAGS="%{rpmldflags}"
#export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

rm -rf *.lang

%find_lang quanta	--with-kde
%find_lang kommander	--with-kde
%find_lang kxsldbg	--with-kde
%find_lang kimagemapeditor --with-kde
%find_lang klinkstatus	--with-kde

> kdegames.lang
gamez="libkdegames \
libkdehighscores"
for i in $gamez;
do
	%find_lang $i --with-kde
	cat $i.lang >> kdegames.lang
done

%find_lang kgreet_classic	--with-kde

%find_lang kcron	--with-kde
%find_lang kdat		--with-kde
%find_lang kpackage	--with-kde
%find_lang ksysv	--with-kde
%find_lang kuser	--with-kde
%find_lang kcmlinuz	--with-kde
%find_lang kcmlilo	--with-kde
%find_lang kfile_deb	--with-kde
cat kfile_deb.lang >> kpackage.lang
%find_lang kfile_rpm	--with-kde
cat kfile_rpm.lang >> kpackage.lang
%find_lang secpolicy	--with-kde
cat secpolicy.lang >> ksysv.lang
%find_lang kstyle_plastik_config --with-kde
%find_lang kwin_cde_config --with-kde
%find_lang kwin_glow_config --with-kde
%find_lang kwin_icewm_config --with-kde
%find_lang kwin_plastik_config --with-kde
> screensavers.lang
%find_lang klock --with-kde
cat klock.lang >> screensavers.lang
%find_lang kpartsaver --with-kde
cat kpartsaver.lang >> screensavers.lang
%find_lang kxsconfig --with-kde
cat kxsconfig.lang >> screensavers.lang
%find_lang	klatin		--with-kde
%find_lang	kturtle		--with-kde
%find_lang	kwordquiz	--with-kde
#find_lang flashkard	--with-kde
%find_lang kalzium	--with-kde
%find_lang kbruch	--with-kde
%find_lang keduca	--with-kde
%find_lang khangman	--with-kde
%find_lang kig		--with-kde
%find_lang kfile_drgeo		--with-kde
%find_lang kfile_kig		--with-kde
cat kfile_drgeo.lang >> kig.lang
cat kfile_kig.lang >> kig.lang
%find_lang kiten	--with-kde
%find_lang klettres	--with-kde
# DONT PACKAGE KMATHTOOL
%find_lang kmessedwords	--with-kde
%find_lang kmplot	--with-kde
%find_lang kpercentage	--with-kde
%find_lang kstars	--with-kde
%find_lang ktouch	--with-kde
%find_lang kverbos	--with-kde
%find_lang kvoctrain	--with-kde
%find_lang atlantik	--with-kde
%find_lang kasteroids	--with-kde
%find_lang katomic	--with-kde
%find_lang kbackgammon	--with-kde
%find_lang kbattleship	--with-kde
%find_lang kblackbox	--with-kde
%find_lang kbounce	--with-kde
%find_lang kenolaba	--with-kde
%find_lang kfouleggs	--with-kde
%find_lang kgoldrunner	--with-kde
%find_lang kjumpingcube	--with-kde
%find_lang klickety	--with-kde
%find_lang klines	--with-kde
%find_lang kmines	--with-kde
%find_lang kolf		--with-kde
%find_lang konquest	--with-kde
%find_lang kpat		--with-kde
%find_lang kpoker	--with-kde
%find_lang kreversi	--with-kde
%find_lang ksame	--with-kde
%find_lang kshisen	--with-kde
%find_lang ksirtet	--with-kde
%find_lang ksnake	--with-kde
%find_lang ksokoban	--with-kde
%find_lang kspaceduel	--with-kde
%find_lang ktron	--with-kde
%find_lang ktuberling	--with-kde
%find_lang kwin4	--with-kde
%find_lang lskat	--with-kde
%find_lang libksirtet	--with-kde
cat libksirtet.lang >> ksirtet.lang
%find_lang kmahjongg	--with-kde
%find_lang ksmiletris	--with-kde
> i18n.lang
%find_lang libkdegames	--with-kde
cat libkdegames.lang >> i18n.lang
%find_lang libkdehighscores	--with-kde
cat libkdehighscores.lang >> i18n.lang

> core.lang
programs=" \
	colors \
	fonts \
	kcmstyle \
	kdeprint \
	kdebugdialog \
	kdesu \
	khelpcenter \
	language"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> core.lang
done

> kdebase.lang
programs=" \
	arts \
	background \
	bell \
	desktop \
	desktopbehavior \
	energy \
	kcmaccess \
	kcmlaunch \
	kcmnotify \
	kcmsmserver \
	keyboard \
	keys \
	ksplashml \
	kwindecoration \
	kxkb \
	mouse \
	passwords \
	spellchecking \
	windowmanagement \
	kcmenergy \
	kcmbell \
	kcmarts \
	kcmbackground \
	privacy \
	libkickermenu_tom \
	display \
	kcmcomponentchooser \
	kcmemail \
	kcminput \
	kcmkeys \
	kcmkwindecoration \
	kcmkwintheme \
	kcmkwm \
	kcmmidi \
	kcmspellchecking \
	kdesktop \
	kwin \
	kwin_default_config \
	kwin_keramik_config \
	kstart \
	kcmxinerama \
	ksmserver \
	kcmxinerama \
	ktip \
	ksplash \
	krandr \
	kreadconfig \
	krdb \
	kcmkwinrules \
	kcmkxmlrpcd \
	kxmlrpcd \
	kthememanager \
	kmenuedit \
	kcmthemes"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdebase.lang
done

%find_lang kicker	--with-kde
programs=" \
	clock \
	kcmtaskbar \
	panel \
	panelappearance"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kicker.lang
done

%find_lang konqueror	--with-kde
programs="\
	cache \
	cookies \
	crypto \
	ebrowsing \
	email \
	filemanager \
	filetypes \
	icons \
	kcmcss \
	khtml \
	netpref \
	proxy \
	smb \
	useragent"

for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> konqueror.lang
done

%find_lang	kio_ldap	--with-kde
%find_lang	kate		--with-kde
%find_lang	kcmkonsole	--with-kde
%find_lang	kdm		--with-kde
%find_lang	kfind		--with-kde
%find_lang	kcmfontinst	--with-kde
%find_lang	kinfocenter	--with-kde
%find_lang	kioslave	--with-kde
%find_lang	klipper		--with-kde
%find_lang	konsole		--with-kde
%find_lang	ksysguard	--with-kde
%find_lang	kpm	--with-kde
cat kpm.lang >> ksysguard.lang
%find_lang	kpager		--with-kde
%find_lang	kwrite		--with-kde
%find_lang	screensaver	--with-kde

cat kcmkonsole.lang	>> konsole.lang
cat kioslave.lang	>> kinfocenter.lang

#files="core \
#kdebase \
#kicker \
#konqueror \
#konsole \
#kinfocenter \
#kate \
#kdm \
#kfind \
#kioslave \
#klipper \
#ksysguard \
#kpager \
#kwrite \
#screensaver \
#kcmfontinst"

%find_lang kwin_b2_config	--with-kde
%find_lang kwin_modernsys_config	--with-kde
%find_lang kwin_quartz_config	--with-kde
%find_lang kcmfileshare	--with-kde

core="kdesud \
kcmaccessibility \
kcmprintmgr \
klegacyimport \
kpartapp \
kprinter \
kcmcolors \
kcmfonts \
kcmkded \
kcmlocale \
kdeprint_part \
kio_man \
kio_settings \
kstyle_keramik_config \
drkonqi"

for i in $core;
do
	%find_lang $i	--with-kde
	cat $i.lang >> core.lang
done

desktop="kcmkwintheme \
kcmkwm \
kwin \
krandr \
privacy \
kcmspellchecking \
kcminput \
kcmxinerama \
display \
ktip \
kaccess \
krdb \
kreadconfig \
ksplash \
kstart \
kwin_default_config \
kcmarts \
kcmbackground \
kcmbell \
kcmcomponentchooser \
kcmemail \
kcmenergy \
kcmkeys \
kcmkwindecoration \
khotkeys \
kdesktop \
ksmserver \
kwin_keramik_config \
kcmmidi \
khotkeys \
joystick"

for i in $desktop;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kdebase.lang
done

%find_lang ksplashthemes	--with-kde

info="kcminfo \
kcmioslaveinfo \
kcmnic \
kcmsamba \
kcmusb \
kcmview1394"

for i in $info;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kinfocenter.lang
done

%find_lang kappfinder	--with-kde

%find_lang katedefaultproject	--with-kde
cat katedefaultproject.lang >> kate.lang
%find_lang katetabbarextension --with-kde
cat katetabbarextension.lang >> kate.lang

%find_lang kdcop	--with-kde

%find_lang kdeprintfax	--with-kde

%find_lang kdialog	--with-kde

%find_lang kfindpart	--with-kde
cat kfindpart.lang >> kfind.lang

%find_lang kfontinst	--with-kde
cat kfontinst.lang >> kcmfontinst.lang
%find_lang fontinst	--with-kde
cat fontinst.lang >> kcmfontinst.lang

kicker="kcmkclock \
kcmkicker \
lockout \
ktaskbarapplet \
libkicker \
libkickermenu_kdeprint \
libkickermenu_konsole \
libkickermenu_prefmenu \
libkickermenu_recentdocs \
ksystemtrayapplet \
childpanelextension \
clockapplet \
kmenuapplet \
kminipagerapplet \
krunapplet \
devicesapplet \
dockbarextension \
kasbarextension \
naughtyapplet \
quicklauncher \
taskbarextension"

for i in $kicker;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kicker.lang
done

%find_lang libtaskbar	--with-kde
%find_lang libtaskmanager	--with-kde
cat libtaskmanager.lang >> libtaskbar.lang

%find_lang kjobviewer	--with-kde

%find_lang kpersonalizer	--with-kde

%find_lang ksystraycmd	--with-kde
cat ksystraycmd.lang >> kdebase.lang

%find_lang kwriteconfig	--with-kde
cat kwriteconfig.lang >> kwrite.lang

%find_lang libkonq	--with-kde

mn="kio_imap4 \
kio_pop3 \
kio_nntp \
kio_smtp \
kio_newimap4"

for i in $mn;
do
	%find_lang $i	--with-kde
done

screen="kscreensaver \
kcmscreensaver"

for i in $screen;
do
	%find_lang $i	--with-kde
	cat $i.lang >> screensaver.lang
done

kdm="kdmchooser \
kdmconfig \
kdmgreet"

for i in $kdm;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kdm.lang
done

konqueror="appletproxy \
nsplugin \
kcmhtmlsearch \
kcmsocks \
kcmlayout \
htmlsearch \
extensionproxy \
kfmclient \
kio_devices \
kcmcgi \
kcmcrypto \
kcmicons \
kcmkio \
kcmkonq \
kcmkonqhtml \
kcmkurifilt \
kcmperformance \
kfile_font \
kio_finger \
kio_fish \
kio_floppy \
kio_mac \
kio_nfs \
kio_print \
kio_sftp \
kio_smb \
kio_smbro"

for i in $konqueror;
do
	%find_lang $i	--with-kde
	cat $i.lang >> konqueror.lang
done
cat kicker.lang >> kdebase.lang
cat libtaskbar.lang >> ksplashthemes.lang

%find_lang useraccount		--with-kde
%find_lang kdepasswd		--with-kde
cat kdepasswd.lang >> useraccount.lang 

for i in $RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e s,${RPM_BUILD_ROOT}%{_datadir}/apps/ktuberling/sounds/,,`
	echo "%lang($z) %{_datadir}/apps/ktuberling/sounds/$z" >> ktuberling.lang
	fi
done

> kdepim.lang

kdepim="kdepimwizards \
kabc_slox \
kres_exchange \
kres_imap \
kres_xmlrpc \
kres_remote"
for i in $kdepim ;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kdepim.lang
done

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	kmail		--with-kde
%find_lang	knode		--with-kde
%find_lang	knotes		--with-kde
%find_lang	konsolekalendar	--with-kde
%find_lang	kontact		--with-kde
%find_lang	korganizer	--with-kde
%find_lang	korn		--with-kde
%find_lang	kgpgcertmanager	--with-kde
%find_lang	kpilot		--with-kde
%find_lang	kfile_palm	--with-kde
%find_lang	kwatchgnupg	--with-kde
%find_lang	kmail_text_calendar_plugin	--with-kde
%find_lang	kmail_text_vcard_plugin		--with-kde
cat kfile_palm.lang >> kpilot.lang
cat kalarm.lang >> korganizer.lang
cat kalarmd.lang >> korganizer.lang
cat kgpgcertmanager.lang >> kmail.lang
cat kwatchgnupg.lang >> kmail.lang
cat kmail_text_calendar_plugin.lang  >> kmail.lang
cat kmail_text_vcard_plugin.lang >> kmail.lang

%find_lang alarmdaemonctrl	--with-kde
cat alarmdaemonctrl.lang >> korganizer.lang
%find_lang kalarmdgui		--with-kde
cat kalarmdgui.lang >> korganizer.lang
%find_lang ksync		--with-kde
cat ksync.lang >> korganizer.lang
%find_lang libcalendarresources --with-kde
cat libcalendarresources.lang >> korganizer.lang

%find_lang kmailcvt		--with-kde
cat kmailcvt.lang >> kmail.lang

%find_lang kleopatra		--with-kde
cat kleopatra.lang >> kmail.lang

%find_lang kfile_rfc822		--with-kde
cat kfile_rfc822.lang >> kmail.lang
%find_lang kio_sieve		--with-kde
cat kio_sieve.lang >> kmail.lang

%find_lang kabc2mutt		--with-kde
cat kabc2mutt.lang >> kaddressbook.lang
%find_lang kcmkabconfig		--with-kde
cat kcmkabconfig.lang >> kaddressbook.lang
%find_lang kfile_vcf		--with-kde
cat kfile_vcf.lang >> kaddressbook.lang

%find_lang libkdepim		--with-kde
# Not packaging kmobile, it was disabled by coolo
%find_lang kdgantt		--with-kde
cat kdgantt.lang >> libkdepim.lang
%find_lang libkleopatra		--with-kde
cat libkleopatra.lang >> libkdepim.lang
%find_lang ktnef		--with-kde

%find_lang libkcal		--with-kde
%find_lang libkcalsystem	--with-kde
cat libkcalsystem.lang >> libkcal.lang

%find_lang libkdenetwork	--with-kde
%find_lang libksieve		--with-kde
%find_lang libksync		--with-kde
mv {libksync,korganizer-libs}.lang
%find_lang kgantt		--with-kde
cat kgantt.lang >> korganizer-libs.lang
%find_lang libkpimexchange	--with-kde
cat libkpimexchange.lang >> korganizer-libs.lang

cat libkcal.lang >> libkdepim.lang
cat korganizer-libs.lang >> libkdepim.lang
cat ktnef.lang >> kmail.lang
cat libkdenetwork.lang >> libkdepim.lang
cat libksieve.lang >> libkdepim.lang
cat kontact.lang >> kdepim.lang
cat korganizer.lang >> kdepim.lang

%find_lang	kfileshare	--with-kde
%find_lang	kcm_sambaconf	--with-kde
cat kcm_sambaconf.lang >> kfileshare.lang
%find_lang kdict		--with-kde
%find_lang kget			--with-kde
%find_lang knewsticker		--with-kde
%find_lang kcmnewsticker	--with-kde
cat kcmnewsticker.lang >> knewsticker.lang
%find_lang kopete		--with-kde
%find_lang kpf			--with-kde
%find_lang kppp			--with-kde
%find_lang krdc			--with-kde
%find_lang krfb			--with-kde
cat krdc.lang >> krfb.lang
%find_lang ksirc		--with-kde
%find_lang kwifimanager		--with-kde
%find_lang lisa			--with-kde
%find_lang lanbrowser		--with-kde
cat lanbrowser.lang >> lisa.lang

%find_lang ktalkd		--with-kde
#find_lang kcmtalkd		--with-kde
%find_lang kcmktalkd		--with-kde
#cat kcmtalkd.lang >> ktalkd.lang
cat kcmktalkd.lang >> ktalkd.lang

%find_lang kcm_krfb		--with-kde
cat kcm_krfb.lang >> krfb.lang

%find_lang kcmlanbrowser	--with-kde
cat kcmlanbrowser.lang >> lisa.lang
%find_lang kio_lan		--with-kde
cat kio_lan.lang >> lisa.lang

%find_lang kppplogview		--with-kde
cat kppplogview.lang >> kppp.lang

%find_lang kwireless		--with-kde
cat kwireless.lang >> kwifimanager.lang
%find_lang kcmwifi		--with-kde
cat kcmwifi.lang >> kwifimanager.lang

%find_lang kdictapplet		--with-kde
cat kdictapplet.lang >> kdict.lang

%find_lang dcopservice		--with-kde
%find_lang kinetd		--with-kde
%find_lang kmag		--with-kde
%find_lang kmousetool	--with-kde
%find_lang kmouth	--with-kde
%find_lang ark			--with-kde
%find_lang KRegExpEditor	--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde
##find_lang kcharselecapplet	--with-kde
##cat kcharselecapplet.lang << kcharselect

> kdf.lang
%find_lang kdf			--with-kde
%find_lang blockdevices		--with-kde
cat blockdevices.lang >> kdf.lang
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
%find_lang kcmkwallet		--with-kde
cat kcmkwallet.lang >> kwallet.lang

%find_lang kcmlaptop		--with-kde
cat kcmlaptop.lang >> klaptopdaemon.lang
%find_lang kcmkvaio		--with-kde
cat kcmkvaio.lang >> kmilo.lang

milo="kmilo_generic \
kmilo_kvaio \
kmilo_powerbook \
kmilo_thinkpad \
kmilod \
kcmthinkpad"
for i in $milo ;
do
%find_lang $i		--with-kde
cat ${i}.lang >> kmilo.lang
done

%find_lang kcmthinkpad	--with-kde
cat kcmthinkpad.lang >> kmilo.lang

%find_lang kregexpeditor	--with-kde
cat kregexpeditor.lang >> KRegExpEditor.lang

%find_lang kcharselectapplet	--with-kde
cat kcharselectapplet.lang >> kcharselect.lang

%find_lang kdessh		--with-kde

# We dont buidl kcardchooser (disabled by default by coolo)
# renaableing it would be posssible, but what for?
# %find_lang kcardchooser	--with-kde
%find_lang artsbuilder	--with-kde
%find_lang juk		--with-kde
%find_lang kaboodle	--with-kde
%find_lang kmid		--with-kde
# No kmidi
# %find_lang kmidi	--with-kde
%find_lang kmix		--with-kde
%find_lang kmixcfg	--with-kde
cat kmixcfg.lang >> kmix.lang
%find_lang krec		--with-kde
%find_lang kscd		--with-kde
%find_lang noatun	--with-kde
%find_lang libkcddb	--with-kde
%find_lang kcmcddb	--with-kde
cat kcmcddb.lang >> libkcddb.lang

%find_lang kio_audiocd	--with-kde
%find_lang kcmaudiocd	--with-kde
cat kcmaudiocd.lang >> kio_audiocd.lang

%find_lang kaudiocreator --with-kde
%find_lang artscontrol	--with-kde
%find_lang artsmodules	--with-kde
mv artsmodules.lang arts.lang

%find_lang kcmkmix	--with-kde
cat kcmkmix.lang >> kmix.lang

kfile="au \
avi \
flac \
m3u \
mp3 \
ogg \
wav \
sid \
mpc \
mp32 \
theora"
> kfile_mm.lang

for i in $kfile;
do
	%find_lang kfile_${i} --with-kde
	cat kfile_${i}.lang >> kfile_mm.lang
done

> kdelibs.spec
%find_lang	kdelibs --with-kde
ziew="cupsdconf kabc_dir kabc_file kabc_ldap kabc_ldapkio kabc_net kabc_sql kabcformat_binary katepart kdelibs_colors kdeprint kfileaudiopreview kio kio_help kioexec kmcop knotify ktexteditor_insertfile ktexteditor_isearch ktexteditor_kdatatool libkscreensaver ppdtranslations timezones common kspell ktexteditor_docwordcompletion"
for i in $ziew;
do
	%find_lang $i --with-kde
	cat $i.lang >> kdelibs.lang
done
for i in `find $RPM_BUILD_ROOT%{_kdedocdir}  -maxdepth 1 -mindepth 1 -printf "%f\n"` ;
do
		echo "%dir %{_kdedocdir}/${i}" >> kdelibs.lang
done

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kcachegrind	--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde
%find_lang	umbrello	--with-kde

kfile="cpp \
diff \
po \
ts \
desktop"

for i in $kfile;
do
	%find_lang kfile_${i} --with-kde
	cat kfile_${i}.lang >> kfile_sdk.lang
done
%find_lang cvsservice	--with-kde

%find_lang kfilereplace		--with-kde
%find_lang kstartperf		--with-kde
%find_lang kuiviewer		--with-kde
%find_lang spy			--with-kde

%find_lang amor			--with-kde
%find_lang kmoon		--with-kde
%find_lang kodo			--with-kde
%find_lang kteatime		--with-kde
%find_lang kweather		--with-kde
%find_lang kworldclock		--with-kde
%find_lang kfifteenapplet	--with-kde
%find_lang ktux			--with-kde

%find_lang kamera		--with-kde
%find_lang kcoloredit		--with-kde
%find_lang kgamma		--with-kde
%find_lang kdvi			--with-kde
%find_lang kghostview		--with-kde
%find_lang kiconedit		--with-kde
%find_lang kooka		--with-kde
%find_lang kolourpaint		--with-kde
%find_lang kpdf			--with-kde
%find_lang kpovmodeler		--with-kde
%find_lang kruler		--with-kde
%find_lang ksnapshot		--with-kde
%find_lang kuickshow		--with-kde
%find_lang kview		--with-kde

kview="_scale \
browserplugin \
canvas \
effectsplugin \
presenterplugin \
scannerplugin \
shell \
templateplugin \
viewer"

for i in $kview;
do
	%find_lang kview${i} --with-kde
	cat kview${i}.lang >> kview.lang
done

%find_lang kcm_kviewcanvasconfig --with-kde
%find_lang kcm_kviewgeneralconfig --with-kde
%find_lang kcm_kviewpluginsconfig --with-kde
%find_lang kcm_kviewviewerpluginsconfig --with-kde
cat kcm_kviewcanvasconfig.lang >> kview.lang
cat kcm_kviewgeneralconfig.lang >> kview.lang
cat kcm_kviewpluginsconfig.lang >> kview.lang
cat kcm_kviewviewerpluginsconfig.lang >> kview.lang

%find_lang kcmkamera --with-kde
cat kcmkamera.lang >> kamera.lang

%find_lang kfax --with-kde
%find_lang kmrml --with-kde
%find_lang kcmkmrml --with-kde
cat kcmkmrml.lang >> kmrml.lang
%find_lang ksvgplugin --with-kde
%find_lang libkscan --with-kde
cat libkscan.lang >> kooka.lang

kfile="bmp \
dvi \
gif \
ico \
jpeg \
pcx \
pdf \
png \
pnm \
ps \
tga \
tiff \
xbm \
exr \
rgb"

for i in $kfile;
do
	%find_lang kfile_${i} --with-kde
	cat kfile_${i}.lang >> kfile_gra.lang
done

%find_lang	ark_plugin	--with-kde
%find_lang	kfile_lnk	--with-kde
%find_lang	rellinks	--with-kde
cat kfile_lnk.lang >> rellinks.lang

%find_lang	kate-plugins	--with-kde
%find_lang	kicker-applets	--with-kde
%find_lang	konq-plugins	--with-kde
%find_lang	fsview		--with-kde
%find_lang	atlantikdesigner	--with-kde
%find_lang	kcmkontactnt		--with-kde
cat kcmkontactnt.lang >> kdepim.lang
%find_lang	ksig		--with-kde
%find_lang	libkaddrbk_geo_xxport	--with-kde

decos="cde \
clients \
glow \
icewm \
kde1 \
kstep \
openlook \
plastik \
riscos \
system"

for i in $decos ;
do
%find_lang	kwin_$i	--with-kde
done
cat kwin_clients.lang >> kdebase.lang
cat kwin_cde_config.lang >> kwin_cde.lang 
cat kwin_icewm_config.lang >> kwin_icewm.lang 
cat kwin_glow_config.lang >> kwin_glow.lang 
cat kwin_plastik_config.lang >> kwin_plastik.lang 

kicker="kbinaryclock \
kolourpicker \
ktimemon \
mediacontrol \
kcmmediacontrol \
kmathapplet"

for i in $kicker;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kicker-applets.lang
done

vim="kcmvim \
vimpart"

for i in $vim;
do
	%find_lang $i	--with-kde
	cat $i.lang >> vim.lang
done

noatun="alsaplayerui \
charlatanui \
dub \
ffrs \
jefferson \
lyrics \
nexscope \
pitchablespeed \
synaescope \
tippecanoe \
tyler \
wakeup \
wavecapture"

for i in $noatun;
do
	%find_lang $i	--with-kde
	cat $i.lang >> noatun_add.lang
done

konqueror="khtmlsettingsplugin \
konqsidebar_mediaplayer \
konq_smbmounterplugin \
validatorsplugin \
autorefresh \
babelfish \
crashesplugin \
dirfilterplugin \
imgalleryplugin \
kcmkuick \
minitoolsplugin \
uachangerplugin \
kuick_plugin \
audiorename_plugin \
imagerename_plugin \
kfile_folder \
kfile_html \
kfile_txt \
searchbarplugin \
konqsidebar_news"

for i in $konqueror;
do
	%find_lang $i	--with-kde
	cat $i.lang >> konq-plugins.lang
done

%find_lang webarchiver
%find_lang domtreeviewer
cat webarchiver.lang domtreeviewer.lang >> konq-plugins.lang

kate="katecppsymbolviewer \
katefll_initplugin \
katefll_plugin \
katehelloworld \
katehtmltools \
kateinsertcommand \
katemake \
katemodeline \
kateopenheader \
kateprojectmanager \
katepybrowse \
katespell \
katetextfilter \
katexmlcheck \
katexmltools \
ktexteditor_autobookmarker \
katefiletemplates \
katekjswrapper"

for i in $kate;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kate-plugins.lang
done

%find_lang kdevelop --with-kde
%find_lang kdevdesigner	--with-kde
cat kdevdesigner.lang >> kdevelop.lang
%find_lang kdevtipofday --with-kde
cat kdevtipofday.lang >> kdevelop.lang
%find_lang qeditor --with-kde
cat qeditor.lang >> kdevelop.lang
%find_lang kde_app_devel --with-kde
cat kde_app_devel.lang >> kdevelop.lang
%find_lang kdearch --with-kde
cat kdearch.lang >> kdevelop.lang
%find_lang kwin_art_clients --with-kde

for i in $RPM_BUILD_ROOT%{_datadir}/locale/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e s,${RPM_BUILD_ROOT}%{_datadir}/locale/,,`
	echo "%lang($z) %{_datadir}/locale/$z/[cef]*" >> core.lang
	fi
done
%find_lang kcontrol --with-kde
grep '\.mo' kcontrol.lang >> core.lang

sed -e "s,%{_prefix},%dir %{_prefix},g" kcontrol.lang |grep HTML >> core.lang

for i in $RPM_BUILD_ROOT%{_kdedocdir}/*/kcontrol/index.docbook ;
do
	echo $i
	if [ -f $i ] ; then
	z=`echo $i|sed -e "s,${RPM_BUILD_ROOT}%{_kdedocdir},,g"`
	lang=`echo $z|cut -d'/' -f2`
	if [ -n "$lang" ] ; then
	echo -e "%lang($lang) %{_kdedocdir}/$lang/kcontrol/*.*" >> core.lang
	fi
	fi
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e s,${RPM_BUILD_ROOT}%{_datadir}/apps/khangman/data/,,`
	echo "%lang($z) %{_datadir}/apps/khangman/data/$z" >> khangman.lang
	fi
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/klettres/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e s,${RPM_BUILD_ROOT}%{_datadir}/apps/klettres/,,`
	echo "%lang($z) %{_datadir}/apps/klettres/$z" >> klettres.lang
	fi
done

# Get rid of stupid messages about files listed twice.
for i in *.lang ;
do
cat ${i}|sort|uniq > ${i}.niedakh
mv ${i}.niedakh ${i}
done

%files -n kde-decoration-common-i18n  -f kwin_art_clients.lang
%defattr(644,root,root,755)
%files -n kde-kgreet-classic-i18n -f kgreet_classic.lang
%defattr(644,root,root,755)
%files -n kdegames-i18n -f kdegames.lang
%defattr(644,root,root,755)
%files -n kdewebdev-quanta-i18n -f quanta.lang
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
%files -n kdelibs-i18n -f kdelibs.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kcron-i18n -f kcron.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kdat-i18n -f kdat.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kpackage-i18n -f kpackage.lang
%defattr(644,root,root,755)
%files -n kdeadmin-ksysv-i18n -f ksysv.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kuser-i18n -f kuser.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kcmlinuz-i18n -f kcmlinuz.lang
%defattr(644,root,root,755)
%files -n kde-decoration-cde-i18n -f kwin_cde.lang
%defattr(644,root,root,755)
%files -n kde-decoration-icewm-i18n -f kwin_icewm.lang
%defattr(644,root,root,755)
%files -n kde-decoration-glow-i18n -f kwin_glow.lang
%defattr(644,root,root,755)
%files -n kde-decoration-plastik-i18n -f kwin_plastik.lang
%defattr(644,root,root,755)
%files -n kde-style-plastik-i18n -f kstyle_plastik_config.lang
%defattr(644,root,root,755)
%files -n kdeartwork-screensavers-i18n -f screensavers.lang
%defattr(644,root,root,755)
%files -n kdeedu-kturtle-i18n -f kturtle.lang
%defattr(644,root,root,755)
%files -n kdeedu-klatin-i18n -f klatin.lang
%defattr(644,root,root,755)
%files -n kdeedu-kwordquiz-i18n -f kwordquiz.lang
%defattr(644,root,root,755)
#files -n kdeedu-flashkard-i18n -f flashkard.lang
#defattr(644,root,root,755)
%files -n kdeedu-kalzium-i18n -f kalzium.lang
%defattr(644,root,root,755)
%files -n kdeedu-kbruch-i18n -f kbruch.lang
%defattr(644,root,root,755)
%files -n kdeedu-keduca-i18n -f keduca.lang
%defattr(644,root,root,755)
%files -n kdeedu-khangman-i18n -f khangman.lang
%defattr(644,root,root,755)
%files -n kdeedu-kig-i18n -f kig.lang
%defattr(644,root,root,755)
%files -n kdeedu-kiten-i18n -f kiten.lang
%defattr(644,root,root,755)
%files -n kdeedu-klettres-i18n -f klettres.lang
%defattr(644,root,root,755)
%files -n kdeedu-kmessedwords-i18n -f kmessedwords.lang
%defattr(644,root,root,755)
%files -n kdeedu-kmplot-i18n -f kmplot.lang
%defattr(644,root,root,755)
%files -n kdeedu-kpercentage-i18n -f kpercentage.lang
%defattr(644,root,root,755)
%files -n kdeedu-kstars-i18n -f kstars.lang
%defattr(644,root,root,755)
%files -n kdeedu-ktouch-i18n -f ktouch.lang
%defattr(644,root,root,755)
%files -n kdeedu-kverbos-i18n -f kverbos.lang
%defattr(644,root,root,755)
%files -n kdeedu-kvoctrain-i18n -f kvoctrain.lang
%defattr(644,root,root,755)
%files -n kdegames-ksmiletris-i18n -f ksmiletris.lang
%defattr(644,root,root,755)
%files -n kdegames-kmahjongg-i18n -f kmahjongg.lang
%defattr(644,root,root,755)
%files -n kdegames-atlantik-i18n -f atlantik.lang
%defattr(644,root,root,755)
%files -n kdegames-kasteroids-i18n -f kasteroids.lang
%defattr(644,root,root,755)
%files -n kdegames-katomic-i18n -f katomic.lang
%defattr(644,root,root,755)
%files -n kdegames-kbackgammon-i18n -f kbackgammon.lang
%defattr(644,root,root,755)
%files -n kdegames-kbattleship-i18n -f kbattleship.lang
%defattr(644,root,root,755)
%files -n kdegames-kblackbox-i18n -f kblackbox.lang
%defattr(644,root,root,755)
%files -n kdegames-kbounce-i18n -f kbounce.lang
%defattr(644,root,root,755)
%files -n kdegames-kenolaba-i18n -f kenolaba.lang
%defattr(644,root,root,755)
%files -n kdegames-kfouleggs-i18n -f kfouleggs.lang
%defattr(644,root,root,755)
%files -n kdegames-kgoldrunner-i18n -f kgoldrunner.lang
%defattr(644,root,root,755)
%files -n kdegames-kjumpingcube-i18n -f kjumpingcube.lang
%defattr(644,root,root,755)
%files -n kdegames-klickety-i18n -f klickety.lang
%defattr(644,root,root,755)
%files -n kdegames-klines-i18n -f klines.lang
%defattr(644,root,root,755)
%files -n kdegames-kmines-i18n -f kmines.lang
%defattr(644,root,root,755)
%files -n kdegames-kolf-i18n -f kolf.lang
%defattr(644,root,root,755)
%files -n kdegames-konquest-i18n -f konquest.lang
%defattr(644,root,root,755)
%files -n kdegames-kpat-i18n -f kpat.lang
%defattr(644,root,root,755)
%files -n kdegames-kpoker-i18n -f kpoker.lang
%defattr(644,root,root,755)
%files -n kdegames-kreversi-i18n -f kreversi.lang
%defattr(644,root,root,755)
%files -n kdegames-ksame-i18n -f ksame.lang
%defattr(644,root,root,755)
%files -n kdegames-kshisen-i18n -f kshisen.lang
%defattr(644,root,root,755)
%files -n kdegames-ksirtet-i18n -f ksirtet.lang
%defattr(644,root,root,755)
%files -n kdegames-ksnake-i18n -f ksnake.lang
%defattr(644,root,root,755)
%files -n kdegames-ksokoban-i18n -f ksokoban.lang
%defattr(644,root,root,755)
%files -n kdegames-kspaceduel-i18n -f kspaceduel.lang
%defattr(644,root,root,755)
%files -n kdegames-ktron-i18n -f ktron.lang
%defattr(644,root,root,755)
%files -n kdegames-ktuberling-i18n -f ktuberling.lang
%defattr(644,root,root,755)
%files -n kdegames-kwin4-i18n -f kwin4.lang
%defattr(644,root,root,755)
%files -n kdegames-lskat-i18n -f lskat.lang
%defattr(644,root,root,755)
##%%files -n kdegames-megami-i18n -f megami.lang
%files -n kdebase-useraccount-i18n -f useraccount.lang 
%defattr(644,root,root,755)
%files -n kdebase-core-i18n -f core.lang
%defattr(644,root,root,755)
%files -n kdebase-desktop-i18n -f kdebase.lang
%defattr(644,root,root,755)
%files -n kdebase-infocenter-i18n -f kinfocenter.lang
%defattr(644,root,root,755)
%files -n kdebase-kate-i18n -f kate.lang
%defattr(644,root,root,755)
%files -n kdebase-kfind-i18n -f kfind.lang
%defattr(644,root,root,755)
%files -n kdebase-kfontinst-i18n -f kcmfontinst.lang
%defattr(644,root,root,755)
%files -n kdebase-klipper-i18n -f klipper.lang
%defattr(644,root,root,755)
%files -n kdebase-konsole-i18n -f konsole.lang
%defattr(644,root,root,755)
%files -n kdebase-kpager-i18n -f kpager.lang
%defattr(644,root,root,755)
%files -n kdebase-ksysguard-i18n -f ksysguard.lang
%defattr(644,root,root,755)
%files -n kdebase-kwrite-i18n -f kwrite.lang
%defattr(644,root,root,755)
%files -n kdebase-screensavers-i18n -f screensaver.lang
%defattr(644,root,root,755)
%files -n kdebase-common-filemanagement-i18n -f kcmfileshare.lang
%defattr(644,root,root,755)
%files -n kdebase-desktop-libs-i18n -f ksplashthemes.lang
%defattr(644,root,root,755)
%files -n kdebase-kappfinder-i18n -f kappfinder.lang
%defattr(644,root,root,755)
%files -n kdebase-kdcop-i18n -f kdcop.lang
%defattr(644,root,root,755)
%files -n kdebase-kdeprintfax-i18n -f kdeprintfax.lang
%defattr(644,root,root,755)
%files -n kdebase-kdialog-i18n -f kdialog.lang
%defattr(644,root,root,755)
%files -n kdebase-kjobviewer-i18n -f kjobviewer.lang
%defattr(644,root,root,755)
%files -n kdebase-kpersonalizer-i18n -f kpersonalizer.lang
%defattr(644,root,root,755)
%files -n konqueror-libs-i18n -f libkonq.lang
%defattr(644,root,root,755)
%files -n kdm-i18n -f kdm.lang
%defattr(644,root,root,755)
%files -n konqueror-i18n -f konqueror.lang
%defattr(644,root,root,755)
%files -n kde-kio-ldap-i18n -f kio_ldap.lang
%defattr(644,root,root,755)
%files -n kde-decoration-b2-i18n -f kwin_b2_config.lang
%defattr(644,root,root,755)
%files -n kde-decoration-modernsys-i18n -f kwin_modernsys_config.lang
%defattr(644,root,root,755)
%files -n kde-decoration-quartz-i18n -f kwin_quartz_config.lang
%defattr(644,root,root,755)
%files -n kde-kio-smtp-i18n -f kio_smtp.lang
%defattr(644,root,root,755)
%files -n kde-kio-nntp-i18n -f kio_nntp.lang
%defattr(644,root,root,755)
%files -n kde-kio-imap4-i18n -f kio_imap4.lang
%defattr(644,root,root,755)
%files -n kde-kio-pop3-i18n -f kio_pop3.lang
%defattr(644,root,root,755)
%files -n kde-kio-newimap4-i18n -f kio_newimap4.lang
%defattr(644,root,root,755)
%files -n kdepim-kaddressbook-i18n -f kaddressbook.lang
%defattr(644,root,root,755)
%files -n kdepim-kandy-i18n -f kandy.lang
%defattr(644,root,root,755)
%files -n kdepim-karm-i18n -f karm.lang
%defattr(644,root,root,755)
%files -n kdepim-kmail-i18n -f kmail.lang
%defattr(644,root,root,755)
%files -n kdepim-knode-i18n -f knode.lang
%defattr(644,root,root,755)
%files -n kdepim-knotes-i18n -f knotes.lang
%defattr(644,root,root,755)
%files -n kdepim-konsolekalendar-i18n -f konsolekalendar.lang
%defattr(644,root,root,755)
%files -n kdepim-korn-i18n -f korn.lang
%defattr(644,root,root,755)
%files -n kdepim-kpilot-i18n -f kpilot.lang
%defattr(644,root,root,755)
%files -n kdepim-i18n -f kdepim.lang
%defattr(644,root,root,755)
%files -n kdepim-libs-i18n -f libkdepim.lang
%defattr(644,root,root,755)
%files -n kdenetwork-filesharing-i18n -f kfileshare.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kdict-i18n -f kdict.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kget-i18n -f kget.lang
%defattr(644,root,root,755)
%files -n kdenetwork-knewsticker-i18n -f knewsticker.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kopete-i18n -f kopete.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kpf-i18n -f kpf.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kppp-i18n -f kppp.lang
%defattr(644,root,root,755)
%files -n kdenetwork-krfb-i18n -f krfb.lang
%defattr(644,root,root,755)
%files -n kdenetwork-ksirc-i18n -f ksirc.lang
%defattr(644,root,root,755)
%files -n kdenetwork-ktalkd-i18n -f ktalkd.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kwifimanager-i18n -f kwifimanager.lang
%defattr(644,root,root,755)
%files -n kdenetwork-lanbrowser-i18n -f lisa.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kinetd-i18n -f kinetd.lang
%defattr(644,root,root,755)
%files -n kdenetwork-rss-i18n -f dcopservice.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmag-i18n -f kmag.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmousetool-i18n -f kmousetool.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmouth-i18n -f kmouth.lang
%defattr(644,root,root,755)
%files -n kdeutils-ark-i18n -f ark.lang
%defattr(644,root,root,755)
%files -n kdeutils-kcalc-i18n -f kcalc.lang
%defattr(644,root,root,755)
%files -n kdeutils-kcharselect-i18n -f kcharselect.lang
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
%files -n kdeutils-kregexpeditor-i18n -f KRegExpEditor.lang
%defattr(644,root,root,755)
%files -n kdeutils-ksim-i18n -f ksim.lang
%defattr(644,root,root,755)
%files -n kdeutils-ktimer-i18n -f ktimer.lang
%defattr(644,root,root,755)
%files -n kdeutils-kwalletmanager-i18n -f kwallet.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdelirc-i18n -f kdelirc.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdessh-i18n -f kdessh.lang
%defattr(644,root,root,755)
%files -n kdeutils-kmilo-i18n -f kmilo.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-artsbuilder-i18n -f artsbuilder.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-artscontrol-i18n -f artscontrol.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-arts-i18n -f arts.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-juk-i18n -f juk.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kaboodle-i18n -f kaboodle.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kmid-i18n -f kmid.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kmix-i18n -f kmix.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kscd-i18n -f kscd.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-krec-i18n -f krec.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-noatun-i18n -f noatun.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kfile-i18n -f kfile_mm.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-audiocd-i18n -f kio_audiocd.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-kaudiocreator-i18n -f kaudiocreator.lang
%defattr(644,root,root,755)
%files -n kdemultimedia-libkcddb-i18n -f libkcddb.lang
%defattr(644,root,root,755)
%files -n kdesdk-libcvsservice-i18n -f cvsservice.lang
%defattr(644,root,root,755)
%files -n kdesdk-kfile-i18n -f kfile_sdk.lang
%defattr(644,root,root,755)
%files -n kdesdk-cervisia-i18n -f cervisia.lang
%defattr(644,root,root,755)
%files -n kdesdk-kbabel-i18n -f kbabel.lang
%defattr(644,root,root,755)
%files -n kdesdk-kbugbuster-i18n -f kbugbuster.lang
%defattr(644,root,root,755)
%files -n kdesdk-kcachegrind-i18n -f kcachegrind.lang
%defattr(644,root,root,755)
%files -n kdesdk-kompare-i18n -f kompare.lang
%defattr(644,root,root,755)
%files -n kdesdk-kstartperf-i18n -f kstartperf.lang
%defattr(644,root,root,755)
%files -n kdesdk-kuiviewer-i18n -f kuiviewer.lang
%defattr(644,root,root,755)
%files -n kdesdk-kspy-i18n -f spy.lang
%defattr(644,root,root,755)
%files -n kdesdk-umbrello-i18n -f umbrello.lang
%defattr(644,root,root,755)
%files -n kdetoys-amor-i18n -f amor.lang
%defattr(644,root,root,755)
%files -n kdetoys-kmoon-i18n -f kmoon.lang
%defattr(644,root,root,755)
%files -n kdetoys-kodo-i18n -f kodo.lang
%defattr(644,root,root,755)
%files -n kdetoys-kteatime-i18n -f kteatime.lang
%defattr(644,root,root,755)
%files -n kdetoys-kweather-i18n -f kweather.lang
%defattr(644,root,root,755)
%files -n kdetoys-kworldclock-i18n -f kworldclock.lang
%defattr(644,root,root,755)
%files -n kdetoys-fifteen-i18n -f kfifteenapplet.lang
%defattr(644,root,root,755)
%files -n kdetoys-ktux-i18n -f ktux.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kamera-i18n -f kamera.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kcoloredit-i18n -f kcoloredit.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kdvi-i18n -f kdvi.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kgamma-i18n -f kgamma.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kghostview-i18n -f kghostview.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kiconedit-i18n -f kiconedit.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kooka-i18n -f kooka.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kolourpaint-i18n -f kolourpaint.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kpdf-i18n -f kpdf.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kpovmodeler-i18n -f kpovmodeler.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kruler-i18n -f kruler.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-ksnapshot-i18n -f ksnapshot.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kuickshow-i18n -f kuickshow.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kview-i18n -f kview.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kfile-i18n -f kfile_gra.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kmrml-i18n -f kmrml.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-ksvg-i18n -f ksvgplugin.lang
%defattr(644,root,root,755)
%files  -n kdegraphics-kfax-i18n -f kfax.lang
%defattr(644,root,root,755)
%files -n kde-decoration-kde1-i18n -f kwin_kde1.lang
%defattr(644,root,root,755)
%files -n kde-decoration-kstep-i18n -f kwin_kstep.lang
%defattr(644,root,root,755)
%files -n kde-decoration-openlook-i18n -f kwin_openlook.lang
%defattr(644,root,root,755)
%files -n kde-decoration-riscos-i18n -f kwin_riscos.lang
%defattr(644,root,root,755)
%files -n kde-decoration-system-i18n -f kwin_system.lang
%defattr(644,root,root,755)
%files -n kdeaddons-ark-i18n -f ark_plugin.lang
%defattr(644,root,root,755)
%files -n kdeaddons-lnkforward-i18n -f rellinks.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kate-i18n -f kate-plugins.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kicker-i18n -f kicker-applets.lang
%defattr(644,root,root,755)
%files -n kdeaddons-konqueror-i18n -f konq-plugins.lang
%defattr(644,root,root,755)
%files -n kdeaddons-atlantikdesigner-i18n -f atlantikdesigner.lang
%defattr(644,root,root,755)
#files -n kdeaddons-kontact-i18n -f kcmkontactnt.lang
#defattr(644,root,root,755)
%files -n kdeaddons-ksig-i18n -f ksig.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kaddressbook-i18n -f libkaddrbk_geo_xxport.lang
%defattr(644,root,root,755)
%files -n kdeaddons-fsview-i18n -f fsview.lang
%defattr(644,root,root,755)
%files -n kdeaddons-noatun-i18n -f noatun_add.lang
%defattr(644,root,root,755)
%files -n kdeaddons-kvim-i18n -f vim.lang
%defattr(644,root,root,755)
%files -n kdeadmin-kcmlilo-i18n -f kcmlilo.lang
%defattr(644,root,root,755)
%files -n kdevelop-i18n -f kdevelop.lang
%defattr(644,root,root,755)

%clean
rm -rf $RPM_BUILD_ROOT
