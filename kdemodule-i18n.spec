#
%define		_name	kde-i18n
%define		kdelibs_epoch	9
%define		kdebase_epoch	9
%define		kdevelop_epoch 7
%define		kdepim_epoch	3
%define		kdenetwork_epoch	10
%define		kdemultimedia_epoch	9
%define		kdeedu_epoch	8
%define		kdeutils_epoch	
%define		kdeacces_epoch	0
Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu jêzyków
Name:		kdemodules-i18n
Version:	3.2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{_name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{_name}-%{version}.tar.bz2
# Source0-md5:	7a2ff8e848b6347e41e450f5aaaf75a3
Source1:	%{name}-splitmo
Source2:	%{name}-splitdoc
Source3:	%{name}-splitdoc-shared
Patch0:		%{name}-fixes.patch
BuildRequires:	kdelibs >= %{kdelibs_epoch}:%{version}
Url:		http://i18n.kde.org
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - international support.

%description -l pl
KDE - wsparcie dla wielu jêzyków.

%package -n kdelibs-i18n
Summary:	Internationalization and localization files for kdelibs.
Summary(pl):	Pliki umiêdzynarodawiaj±ce kdelibs.
Group:		X11/Libraries
Requires:	kdelibs = %{kdelibs_epoch}:%{version}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
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

%description -n kdelibs-i18n
Translations and localization data for KDE libraries.

%description -n kdelibs-i18n -l pl
T³umaczenia i dane miêdzynarodowe dla bibliotek KDE.

%package -n kdebase-core-i18n
Summary:	Internationalization and localization files for the core part of KDE
Summary(pl):	T³umaczenia dla core KDE
Group:		X11/Applications
Requires:	kdebase-core = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-core-i18n
Internationalization and localization files for KDE:
- Control Center;
- Help Center;
- Print System;
- Crash Handlers;
- A Frontend for "su" program.

%description -n kdebase-core-i18n -l pl
T³umaczenia dla core.

%package -n kdebase-desktop-i18n
Summary:	Internationalization and localization files for the desktop part of KDE
Summary(pl):	T³umaczenia dla desktopu
Group:		X11/Applications
Requires:	kdebase-desktop = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-libs-i18n = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdebase_epoch}:%{version}
Requires:	konqueror-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-kfind-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-kjobviewer-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-kpager-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-kmenuedit-i18n = %{kdebase_epoch}:%{version}
Obsoletes:	kdebase-kicker-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-desktop-i18n
Internationalization and localization files for KDE:
- desktop 
- panel
- splashscreen system
- window manager

%description -n kdebase-desktop-i18n -l pl
T³umaczenia dla desktop.

%package -n kdebase-infocenter-i18n
Summary:	Internationalization and localization files for KDE Information Centre
Summary(pl):	T³umaczenia dla centrum informacji o systemie
Group:		X11/Applications
Requires:	kdebase-infocenter = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-infocenter-i18n
Internationalization and localization files for KDE Information Centre.

%description -n kdebase-infocenter-i18n -l pl
T³umaczenia dla centrum informacji o systemie.

%package -n kdebase-kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl):	T³umaczenia dla kate
Group:		X11/Applications
Requires:	kdebase-kate = %{kdebase_epoch}:%{version}
Requires:	kdebase-common-filemanagement-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kate-i18n
Internationalization and localization files for kate.

%description -n kdebase-kate-i18n -l pl
T³umaczenia dla kate.

%package -n kdebase-kfind-i18n
Summary:	Internationalization and localization files for kfind
Summary(pl):	T³umaczenia dla kfind
Group:		X11/Applications
Requires:	kdebase-kfind = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kfind-i18n
Internationalization and localization files for kfind.

%description -n kdebase-kfind-i18n -l pl
T³umaczenia dla kfind.

%package -n kdebase-kfontinst-i18n
Summary:	Internationalization and localization files for kfontinst
Summary(pl):	T³umaczenia dla kfontinst
Group:		X11/Applications
Requires:	kdebase-kfontinst = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kfontinst-i18n
Internationalization and localization files for kfontinst.

%description -n kdebase-kfontinst-i18n -l pl
T³umaczenia dla kfontinst.

%package -n kdebase-klipper-i18n
Summary:	Internationalization and localization files for klipper
Summary(pl):	T³umaczenia dla klippera
Group:		X11/Applications
Requires:	kdebase-klipper = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-klipper-i18n
Internationalization and localization files for klipper.

%description -n kdebase-klipper-i18n -l pl
T³umaczenia dla klippera.

%package -n kdebase-kmenuedit-i18n
Summary:	Internationalization and localization files for kmenuedit
Summary(pl):	T³umaczenia dla kmenuedit
Group:		X11/Applications
Requires:	kdebase-kmenuedit = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kmenuedit-i18n
Internationalization and localization files for kmenuedit.

%description -n kdebase-kmenuedit-i18n -l pl
T³umaczenia dla kmenuedit.

%package -n kdebase-konsole-i18n
Summary:	Internationalization and localization files for konsole
Summary(pl):	T³umaczenia dla konsole
Group:		X11/Applications
Requires:	kdebase-konsole = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-konsole-i18n
Internationalization and localization files for konsole.

%description -n kdebase-konsole-i18n -l pl
T³umaczenia dla konsole.

%package -n kdebase-kpager-i18n
Summary:	Internationalization and localization files for kpager
Summary(pl):	T³umaczenia dla kpagera
Group:		X11/Applications
Requires:	kdebase-kpager = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = 9:%{version}

%description -n kdebase-kpager-i18n
Internationalization and localization files for kpager.

%description -n kdebase-kpager-i18n -l pl
T³umaczenia dla kpagera.

%package -n kdebase-ksysguard-i18n
Summary:	Internationalization and localization files for ksysguard
Summary(pl):	T³umaczenia dla ksysguarda
Group:		X11/Applications
Requires:	kdebase-ksysguard = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-klipper-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-ksysguard-i18n
Internationalization and localization files for ksysguard.

%description -n kdebase-ksysguard-i18n -l pl
T³umaczenia dla ksysguarda.

%package -n kdebase-kwrite-i18n
Summary:	Internationalization and localization files for kwrite
Summary(pl):	T³umaczenia dla kwrite
Group:		X11/Applications
Requires:	kdebase-kwrite = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kwrite-i18n
Internationalization and localization files for kwrite.

%description -n kdebase-kwrite-i18n -l pl
T³umaczenia dla kwrite.

%package -n kdebase-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	T³umaczenia dla screensavers
Group:		X11/Applications
Requires:	kdebase-screensavers = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdebase-screensavers-i18n -l pl
T³umaczenia dla screensavers.

%package -n kdm-i18n
Summary:	Internationalization and localization files for kdm
Summary(pl):	T³umaczenia dla kdm-a
Group:		X11/Applications
Requires:	kdm = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdm-i18n
Internationalization and localization files for kdm.

%description -n kdm-i18n -l pl
T³umaczenia dla kdm-a.

%package -n konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl):	T³umaczenia dla konquerora
Group:		X11/Applications
Requires:	konqueror = %{kdebase_epoch}:%{version}
Requires:	kdebase-common-filemanagement-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-konsole-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-libkonq-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-mailnews-i18n = %{kdebase_epoch}:%{version}

%description -n konqueror-i18n
Internationalization and localization files for konqueror.

%description -n konqueror-i18n -l pl
T³umaczenia dla konquerora.

%package -n kde-decoration-b2-i18n
Summary:	Internationalization and localization files for kde-decoration-b2
Summary(pl):	T³umaczenia dla kde-decoration-b2
Group:		X11/Applications
Requires:	kde-decoration-b2 = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kde-decoration-b2-i18n
Internationalization and localization files for kde-decoration-b2.

%description -n kde-decoration-b2-i18n -l pl
T³umaczenia dla kde-decoration-b2.

%package -n kde-decoration-modernsys-i18n
Summary:	Internationalization and localization files for kde-decoration-modernsys
Summary(pl):	T³umaczenia dla kde-decoration-modernsys
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}
Requires:	kde-decoration-modernsys = %{kdebase_epoch}:%{version}

%description -n kde-decoration-modernsys-i18n
Internationalization and localization files for kde-decoration-modernsys.

%description -n kde-decoration-modernsys-i18n -l pl
T³umaczenia dla kde-decoration-modernsys.

%package -n kde-decoration-quartz-i18n
Summary:	Internationalization and localization files for kde-decoration-quartz
Summary(pl):	T³umaczenia dla kde-decoration-quartz
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}
Requires:	kde-decoration-quartz = %{kdebase_epoch}:%{version}

%description -n kde-decoration-quartz-i18n
Internationalization and localization files for kde-decoration-quartz.

%description -n kde-decoration-quartz-i18n -l pl
T³umaczenia dla kde-decoration-quartz.

%package -n kdebase-common-filemanagement-i18n
Summary:	Internationalization and localization files for common-filemanagement
Summary(pl):	T³umaczenia dla common-filemanagement
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-common-filemanagement = %{kdebase_epoch}:%{version}

%description -n kdebase-common-filemanagement-i18n
Internationalization and localization files for common-filemanagement.

%description -n kdebase-common-filemanagement-i18n -l pl
T³umaczenia dla common-filemanagement.

%package -n kdebase-desktop-libs-i18n
Summary:	Internationalization and localization files for desktop-libs
Summary(pl):	T³umaczenia dla desktop-libs
Group:		X11/Applications
Requires:	kdebase-desktop-libs = %{kdebase_epoch}:%{version}
Obsoletes:	kdebase-kicker-libs = %{kdebase_epoch}:%{version}

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
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kdcop-i18n
Internationalization and localization files for kdcop.

%description -n kdebase-kdcop-i18n -l pl
T³umaczenia dla kdcopa.

%package -n kdebase-kdeprintfax-i18n
Summary:	Internationalization and localization files for kdeprintfax
Summary(pl):	T³umaczenia dla kdeprintfax
Group:		X11/Applications
Requires:	kdebase-kdeprintfax = %{kdebase_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

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
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kjobviewer-i18n
Internationalization and localization files for kjobviewer.

%description -n kdebase-kjobviewer-i18n -l pl
T³umaczenia dla kjobviewera.

%package -n kdebase-kpersonalizer-i18n
Summary:	Internationalization and localization files for kpersonalizer
Summary(pl):	T³umaczenia dla kpersonalizera
Group:		X11/Applications
Requires:	kdebase-kpersonalizer = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-kpersonalizer-i18n
Internationalization and localization files for kpersonalizer.

%description -n kdebase-kpersonalizer-i18n -l pl
T³umaczenia dla kpersonalizera.

%package -n kdebase-ksystraycmd-i18n
Summary:	Internationalization and localization files for ksystraycmd
Summary(pl):	T³umaczenia dla ksystraycmd
Group:		X11/Applications
Requires:	kdebase-ksystraycmd = %{kdebase_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdebase-ksystraycmd-i18n
Internationalization and localization files for ksystraycmd.

%description -n kdebase-ksystraycmd-i18n -l pl
T³umaczenia dla ksystraycmd.

%package -n kdebase-libkonq-i18n
Summary:	Internationalization and localization files for libkonq
Summary(pl):	T³umaczenia dla libkonq
Group:		X11/Applications
Requires:	kdebase-libkonq = %{kdebase_epoch}:%{version}

%description -n kdebase-libkonq-i18n
Internationalization and localization files for libkonq.

%description -n kdebase-libkonq-i18n -l pl
T³umaczenia dla libkonq.

%package -n kdebase-mailnews-i18n
Summary:	Internationalization and localization files for mailnews
Summary(pl):	T³umaczenia dla mailnews
Group:		X11/Applications
Requires:	kdebase-mailnews = %{kdebase_epoch}:%{version}

%description -n kdebase-mailnews-i18n
Internationalization and localization files for mailnews.

%description -n kdebase-mailnews-i18n -l pl
T³umaczenia dla mailnews.

%package -n kdevelop-i18n
Summary:	Internationalization and localization files for kdevelop
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdevelopa
Group:  	X11/Applications
Requires:	kdevelop = %{kdevelop_epoch}:%{kdevelop_version}
Requires:	kdelibs-i18n = 9:%{version}

%description -n kdevelop-i18n
Internationalization and localization files for kdevelop.

%description -n kdevelop-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdevelopa.

%package -n kdepim-kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl):	T³umaczenia dla kaddressbook
Group:		X11/Applications
Requires:	kdepim-kaddressbook = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdepim-kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description -n kdepim-kaddressbook-i18n -l pl
T³umaczenia dla kaddressbook.

%package -n kdepim-kandy-i18n
Summary:	Internationalization and localization files for kandy
Summary(pl):	T³umaczenia dla kandy
Group:		X11/Applications
Requires:	kdepim-kandy = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdepim-kandy-i18n
Internationalization and localization files for kandy.

%description -n kdepim-kandy-i18n -l pl
T³umaczenia dla kandy.

%package -n kdepim-karm-i18n
Summary:	Internationalization and localization files for karm
Summary(pl):	T³umaczenia dla karm
Group:		X11/Applications
Requires:	kdepim-karm = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-karm-i18n
Internationalization and localization files for karm.

%description -n kdepim-karm-i18n -l pl
T³umaczenia dla karm.

%package -n kdepim-kmail-i18n
Summary:	Internationalization and localization files for kmail
Summary(pl):	T³umaczenia dla kmaila
Group:		X11/Applications
Requires:	kdepim-kmail = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdenetwork-i18n = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}
Requires:	kdepim-kmail-libs-i18n = %{kdepim_epoch}:%{version}
Requires:	kdebase-mailnews-i18n = %{kdebase_epoch}:%{version}
Obsolets:	kdepim-ktnef-i18n 

%description -n kdepim-kmail-i18n
Internationalization and localization files for kmail.

%description -n kdepim-kmail-i18n -l pl
T³umaczenia dla kmaila.

%package -n kdepim-knode-i18n
Summary:	Internationalization and localization files for knode
Summary(pl):	T³umaczenia dla knode
Group:		X11/Applications
Requires:	kdepim-knode = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdenetwork-i18n = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}
Requires:	kdebase-mailnews-i18n = %{kdebase_epoch}:%{version}

%description -n kdepim-knode-i18n
Internationalization and localization files for knode.

%description -n kdepim-knode-i18n -l pl
T³umaczenia dla knode.

%package -n kdepim-knotes-i18n
Summary:	Internationalization and localization files for knotes
Summary(pl):	T³umaczenia dla knotes
Group:		X11/Applications
Requires:	kdepim-knotes = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-knotes-i18n
Internationalization and localization files for knotes.

%description -n kdepim-knotes-i18n -l pl
T³umaczenia dla knotes.

%package -n kdepim-konsolekalendar-i18n
Summary:	Internationalization and localization files for konsolekalendar
Summary(pl):	T³umaczenia dla konsolekalendara
Group:		X11/Applications
Requires:	kdepim-konsolekalendar = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-konsolekalendar-i18n
Internationalization and localization files for konsolekalendar.

%description -n kdepim--l pl konsolekalendar-i18n
T³umaczenia dla konsolekalendara.

%package -n kdepim-kontact-i18n
Summary:	Internationalization and localization files for kontact
Summary(pl):	T³umaczenia dla kontacta
Group:		X11/Applications
Requires:	kdepim-kontact = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-kontact-i18n
Internationalization and localization files for kontact.

%description -n kdepim-kontact-i18n -l pl
T³umaczenia dla kontacta.

%package -n kdepim-korganizer-i18n
Summary:	Internationalization and localization files for korganizer
Summary(pl):	T³umaczenia dla korganizera
Group:		X11/Applications
Requires:	kdepim-korganizer = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-korganizer-i18n
Internationalization and localization files for korganizer.

%description -n kdepim-korganizer-i18n -l pl
T³umaczenia dla korganizera.

%package -n kdepim-korn-i18n
Summary:	Internationalization and localization files for korn
Summary(pl):	T³umaczenia dla korna
Group:		X11/Applications
Requires:	kdepim-korn = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdenetwork-i18n = %{kdepim_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdepim-korn-i18n
Internationalization and localization files for korn.

%description -n kdepim-korn-i18n -l pl
T³umaczenia dla korna.

%package -n kdepim-kpilot-i18n
Summary:	Internationalization and localization files for kpilot
Summary(pl):	T³umaczenia dla kpilota
Group:		X11/Applications
Requires:	kdepim-kpilot = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdepim-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-kpilot-i18n
Internationalization and localization files for kpilot.

%description -n kdepim-kpilot-i18n -l pl
T³umaczenia dla kpilota.

%package -n kdepim-libkdepim-i18n
Summary:	Internationalization and localization files for libkdepim
Summary(pl):	T³umaczenia dla libkdepim
Group:		X11/Applications
Requires:	kdepim-libkdepim = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}
Obsoletes:	kdepim-libkcal-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-libkdgantt-i18n

%description -n kdepim-libkdepim-i18n
Internationalization and localization files for libkdepim.

%description -n kdepim-libkdepim-i18n -l pl
T³umaczenia dla libkdepim.

%package -n kdepim-libkdenetwork-i18n
Summary:	Internationalization and localization files for libkdenetwork
Summary(pl):	T³umaczenia dla libkdenetwork
Group:		X11/Applications
Requires:	kdepim-libkdenetwork = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdepim-libkdenetwork-i18n
Internationalization and localization files for libkdenetwork.

%description -n kdepim-libkdenetwork-i18n -l pl
T³umaczenia dla libkdenetwork.

%package -n kdepim-kmail-libs-i18n
Summary:	Internationalization and localization files for kmail-libs
Summary(pl):	T³umaczenia dla kmail-libs
Group:		X11/Applications
Requires:	kdepim-libkdepim = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdenetwork = %{kdepim_epoch}:%{version}
Requires:	kdepim-kmail-libs = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}
Obsoletes:	kdepim-libksieve-i18n = %{kdepim_epoch}:%{version}
Obsoletes:	kdepim-libkmailprivate-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-kmail-libs-i18n
Internationalization and localization files for kmail-libs.

%description -n kdepim-kmail-libs-i18n -l pl
T³umaczenia dla kmail-libs.

%package -n kdeutils-ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arka
Group:		X11/Applications
Requires:	kdeutils-ark = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-ark-i18n
Internationalization and localization files for ark.

%description -n kdeutils-ark-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arka.

%package -n kdeutils-kcalc-i18n
Summary:	Internationalization and localization files for kcalc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcalca
Group:		X11/Applications
Requires:	kdeutils-kcalc = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kcalc-i18n
Internationalization and localization files for kcalc.

%description -n kdeutils-kcalc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcalca.

%package -n kdeutils-kcharselect-i18n
Summary:	Internationalization and localization files for kcharselect
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharselecta
Group:		X11/Applications
Requires:	kdeutils-kcharselect = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kcharselect-i18n
Internationalization and localization files for kcharselect.

%description -n kdeutils-kcharselect-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharselecta.

%package -n kdeutils-kdf-i18n
Summary:	Internationalization and localization files for kdf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdf
Group:		X11/Applications
Requires:	kdeutils-kdf = %{kdeutils_epoch}:%{version}
Requires:	kdebase-infocenter-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kdf-i18n
Internationalization and localization files for kdf.

%description -n kdeutils-kdf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdf.

%package -n kdeutils-kedit-i18n
Summary:	Internationalization and localization files for kedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	kdeutils-kedit = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kedit-i18n
Internationalization and localization files for kedit.

%description -n kdeutils-kedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kedita.

%package -n kdeutils-kmilo-i18n
Summary:	Internationalization and localization files for kmilo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	kdeutils-kmilo = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kmilo-i18n
Internationalization and localization files for kmilo.

%description -n kdeutils-kmilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmilo.

%package -n kdeutils-kfloppy-i18n
Summary:	Internationalization and localization files for kfloppy
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfloppy
Group:		X11/Applications
Requires:	kdeutils-kfloppy = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kfloppy-i18n
Internationalization and localization files for kfloppy.

%description -n kdeutils-kfloppy-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfloppy.

%package -n kdeutils-kgpg-i18n
Summary:	Internationalization and localization files for kgpg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgpg
Group:		X11/Applications
Requires:	kdeutils-kgpg = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kgpg-i18n
Internationalization and localization files for kgpg.

%description -n kdeutils-kgpg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgpg.

%package -n kdeutils-khexedit-i18n
Summary:	Internationalization and localization files for khexedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khexedita
Group:		X11/Applications
Requires:	kdeutils-khexedit = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-khexedit-i18n
Internationalization and localization files for khexedit.

%description -n kdeutils-khexedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khexedita.

%package -n kdeutils-kjots-i18n
Summary:	Internationalization and localization files for kjots
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjots
Group:		X11/Applications
Requires:	kdeutils-kjots = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kjots-i18n
Internationalization and localization files for kjots.

%description -n kdeutils-kjots-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjots.

%package -n kdeutils-klaptopdaemon-i18n
Summary:	Internationalization and localization files for klaptopdaemon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klaptopdaemona
Group:		X11/Applications
Requires:	kdeutils-klaptopdaemon = %{kdeutils_epoch}:%{version}
Requires:	kdebase-infocenter-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-klaptopdaemon-i18n
Internationalization and localization files for klaptopdaemon.

%description -n kdeutils-klaptopdaemon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klaptopdaemona.

%package -n kdeutils-kregexpeditor-i18n
Summary:	Internationalization and localization files for kregexpeditor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kregexpeditora
Group:		X11/Applications
Requires:	kdeutils-kregexpeditor = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kregexpeditor-i18n
Internationalization and localization files for kregexpeditor.

%description -n kdeutils-kregexpeditor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kregexpeditora.

%package -n kdeutils-ksim-i18n
Summary:	Internationalization and localization files for ksim
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksima
Group:		X11/Applications
Requires:	kdeutils-ksim = %{kdeutils_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-ksim-i18n
Internationalization and localization files for ksim.

%description -n kdeutils-ksim-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksima.

%package -n kdeutils-ktimer-i18n
Summary:	Internationalization and localization files for ktimer
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktimera
Group:		X11/Applications
Requires:	kdeutils-ktimer = %{kdeutils_epoch}:%{version}
Requires:	kdelibs-i18n >= %{kdelibs_epoch}:%{version}

%description -n kdeutils-ktimer-i18n
Internationalization and localization files for ktimer.

%description -n kdeutils-ktimer-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktimera.

%package -n kdeutils-kwalletmanager-i18n
Summary:	Internationalization and localization files for kwalletmanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwalletmanagera
Group:		X11/Applications
Requires:	kdeutils-kwalletmanager = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kwalletmanager-i18n
Internationalization and localization files for kwalletmanager.

%description -n kdeutils-kwalletmanager-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwalletmanagera.

%package -n kdeutils-kdelirc-i18n
Summary:	Internationalization and localization files for kdelirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdelirca
Group:		X11/Applications
Requires:	kdeutils-kdelirc = %{kdeutils_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeutils-kdelirc-i18n
Internationalization and localization files for kdelirc.

%description -n kdeutils-kdelirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdelirca.

%package -n kdeutils-userinfo-i18n
Summary:	Internationalization and localization files for userinfo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla userinfo
Group:		X11/Applications
Requires:	kdeutils-userinfo = %{kdeutils_epoch}:%{version}
Requires:	kdm-i18n >= %{kdebase_epoch}:%{version}

%description -n kdeutils-userinfo-i18n
Internationalization and localization files for userinfo.

%description -n kdeutils-userinfo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla userinfo.

%package -n kdeutils-kdessh-i18n
Summary:	Internationalization and localization files for kdessh
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdessh
Group:		X11/Applications
Requires:	kdeutils-kdessh = %{kdeutils_epoch}:%{version}
Requires:	kdelibs-i18n >= %{kdelibs_epoch}:%{version}

%description -n kdeutils-kdessh-i18n
Internationalization and localization files for kdessh.

%description -n kdeutils-kdessh-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdessh.

%package -n kdeutils-kdepasswd-i18n
Summary:	Internationalization and localization files for kdepasswd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdepasswd
Group:		X11/Applications
Requires:	kdeutils-kdepasswd = %{kdeutils_epoch}:%{version}
Requires:	kdelibs-i18n >= %{kdelibs_epoch}:%{version}

%description -n kdeutils-kdepasswd-i18n
Internationalization and localization files for kdepasswd.

%description -n kdeutils-kdepasswd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdepasswd.

%package -n kdeaccessibility-kmag-i18n
Summary:	Internationalization and localization files for kmag
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmag
Group:		X11/Applications
Requires:	kdeaccessibility-kmag = %{kdeacces_epoch}:%{version}
Requires:	kdelibs-i18n >= %{kdelibs_epoch}:%{version}

%description -n kdeaccessibility-kmag-i18n
Internationalization and localization files for kmag.

%description -n kdeaccessibility-kmag-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmag.

%package -n kdeaccessibility-kmousetool-i18n
Summary:	Internationalization and localization files for kmousetool
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmousetool
Group:		X11/Applications
Requires:	kdeaccessibility-kmousetool = %{kdeacces_epoch}:%{version}
Requires:	kdelibs-i18n >= %{kdelibs_epoch}:%{version}

%description -n kdeaccessibility-kmousetool-i18n
Internationalization and localization files for kmousetool.

%description -n kdeaccessibility-kmousetool-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmousetool.

%package -n kdeaccessibility-kmouth-i18n
Summary:	Internationalization and localization files for kmouth
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmouth
Group:		X11/Applications
Requires:	kdeaccessibility-kmouth = %{kdeacces_epoch}:%{version}
Requires:	kdelibs-i18n >= %{kdelibs_epoch}:%{version}

%description -n kdeaccessibility-kmouth-i18n
Internationalization and localization files for kmouth.

%description -n kdeaccessibility-kmouth-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmouth.


%package -n kdenetwork-kdict-i18n
Summary:	Internationalization and localization files for kdict
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdict
Group:		X11/Applications
Requires:	kdenetwork-kdict = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-kdict-i18n
Internationalization and localization files for kdict.

%description -n kdenetwork-kdict-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdict.

%package -n kdenetwork-kinetd-i18n
Summary:	Internationalization and localization files for kinetd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kinetd
Group:		X11/Applications
Requires:	kdenetwork-kinetd = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdenetwork-kinetd-i18n
Internationalization and localization files for kinetd.

%description -n kdenetwork-kinetd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kinetd.

%package -n kdenetwork-kget-i18n
Summary:	Internationalization and localization files for kget
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgeta
Group:		X11/Applications
Requires:	kdenetwork-kget = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-kget-i18n
Internationalization and localization files for kget.

%description -n kdenetwork-kget-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgeta.

%package -n kdenetwork-knewsticker-i18n
Summary:	Internationalization and localization files for knewsticker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla knewstickera
Group:		X11/Applications
Requires:	kdenetwork-knewsticker = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-knewsticker-i18n
Internationalization and localization files for knewsticker.

%description -n kdenetwork-knewsticker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla knewstickera.

%package -n kdenetwork-kopete-i18n
Summary:	Internationalization and localization files for kopete
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kopete
Group:		X11/Applications
Requires:	kdenetwork-kopete = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdenetwork-kopete-i18n
Internationalization and localization files for kopete.

%description -n kdenetwork-kopete-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kopete.

%package -n kdenetwork-kpf-i18n
Summary:	Internationalization and localization files for kpf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpf
Group:		X11/Applications
Requires:	kdenetwork-kpf = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-kpf-i18n
Internationalization and localization files for kpf.

%description -n kdenetwork-kpf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpf.

%package -n kdenetwork-kppp-i18n
Summary:	Internationalization and localization files for kppp
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kppp
Group:		X11/Applications
Requires:	kdenetwork-kppp = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-kppp-i18n
Internationalization and localization files for kppp.

%description -n kdenetwork-kppp-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kppp.

%package -n kdenetwork-krfb-i18n
Summary:	Internationalization and localization files for krfb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krfb
Group:		X11/Applications
Requires:	kdenetwork-krfb = %{kdenetwork_epoch}:%{version}
Requires:	kdenetwork-kinetd-i18n = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-krfb-i18n
Internationalization and localization files for krfb.

%description -n kdenetwork-krfb-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krfb.

%package -n kdenetwork-ksirc-i18n
Summary:	Internationalization and localization files for ksirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirc
Group:		X11/Applications
Requires:	kdenetwork-ksirc = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-ksirc-i18n
Internationalization and localization files for ksirc.

%description -n kdenetwork-ksirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksirc.

%package -n kdenetwork-ktalkd-i18n
Summary:	Internationalization and localization files for ktalkd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktalkd
Group:		X11/Applications
Requires:	kdenetwork-ktalkd = %{kdenetwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-ktalkd-i18n
Internationalization and localization files for ktalkd.

%description -n kdenetwork-ktalkd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktalkd.

%package -n kdenetwork-kwifimanager-i18n
Summary:	Internationalization and localization files for kwifimanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwifimanagera
Group:		X11/Applications
Requires:	kdenetwork-kwifimanager = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdenetwork-kwifimanager-i18n
Internationalization and localization files for kwifimanager.

%description -n kdenetwork-kwifimanager-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwifimanagera.

%package -n kdenetwork-lanbrowser-i18n
Summary:	Internationalization and localization files for lanbrowser
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lanbrowsera
Group:		X11/Applications
Requires:	kdenetwork-lanbrowser = %{kdenetwork_epoch}:%{version}
Requires:	konqueror-i18n = %{kdebase_epoch}:%{version}

%description -n kdenetwork-lanbrowser-i18n
Internationalization and localization files for lanbrowser.

%description -n kdenetwork-lanbrowser-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla lanbrowsera.

%package -n kdenetwork-rss-i18n
Summary:	Internationalization and localization files for rss
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla rss
Group:		X11/Applications
Requires:	kdenetwork-rss = %{kdenetwork_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdenetwork-rss-i18n
Internationalization and localization files for rss.

%description -n kdenetwork-rss-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla rss.

%package -n kdemultimedia-artsbuilder-i18n
Summary:	Internationalization and localization files for artsbuilder
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artsbuildera
Group:		X11/Applications
Requires:	kdemultimedia-artsbuilder = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-arts-i18n = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-artsbuilder-i18n
Internationalization and localization files for artsbuilder.

%description -n kdemultimedia-artsbuilder-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artsbuildera.

%package -n kdemultimedia-artscontrol-i18n
Summary:	Internationalization and localization files for artscontrol
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artscontrol
Group:		X11/Applications
Requires:	kdemultimedia-artscontrol = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-arts-i18n = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-artscontrol-i18n
Internationalization and localization files for artscontrol.

%description -n kdemultimedia-artscontrol-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artscontrol.

%package -n kdemultimedia-arts-i18n
Summary:	Internationalization and localization files for arts
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arts
Group:		X11/Applications
Requires:	kdemultimedia-arts = %{kdemultimedia_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdemultimedia-arts-i18n
Internationalization and localization files for arts.

%description -n kdemultimedia-arts-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arts.

%package -n kdemultimedia-juk-i18n
Summary:	Internationalization and localization files for juk
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla juk
Group:		X11/Applications
Requires:	kdemultimedia-juk = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-juk-i18n
Internationalization and localization files for juk.

%description -n kdemultimedia-juk-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla juk.

%package -n kdemultimedia-kaboodle-i18n
Summary:	Internationalization and localization files for kaboodle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaboodle
Group:		X11/Applications
Requires:	kdemultimedia-kaboodle = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-kaboodle-i18n
Internationalization and localization files for kaboodle.

%description -n kdemultimedia-kaboodle-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaboodle.

%package -n kdemultimedia-kmid-i18n
Summary:	Internationalization and localization files for kmid
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmid
Group:		X11/Applications
Requires:	kdemultimedia-kmid = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-kmid-i18n
Internationalization and localization files for kmid.

%description -n kdemultimedia-kmid-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmid.

%package -n kdemultimedia-kmix-i18n
Summary:	Internationalization and localization files for kmix
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmix
Group:		X11/Applications
Requires:	kdemultimedia-kmix = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-kmix-i18n
Internationalization and localization files for kmix.

%description -n kdemultimedia-kmix-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmix.

%package -n kdemultimedia-kscd-i18n
Summary:	Internationalization and localization files for kscd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kscd
Group:		X11/Applications
Requires:	kdemultimedia-kscd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-kscd-i18n
Internationalization and localization files for kscd.

%description -n kdemultimedia-kscd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kscd.

%package -n kdemultimedia-krec-i18n
Summary:	Internationalization and localization files for krec
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krec
Group:		X11/Applications
Requires:	kdemultimedia-krec = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-artscontrol-i18n = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-kmix-i18n = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-krec-i18n
Internationalization and localization files for krec.

%description -n kdemultimedia-krec-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krec.

%package -n kdemultimedia-noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla noatun
Group:		X11/Applications
Requires:	kdemultimedia-noatun = %{kdemultimedia_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-noatun-i18n
Internationalization and localization files for noatun.

%description -n kdemultimedia-noatun-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla noatun.

%package -n kdemultimedia-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfile
Group:		X11/Applications
Requires:	kdemultimedia-kfile = %{kdemultimedia_epoch}:%{version}
Requires:	konqueror-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdemultimedia-kfile-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfile.

%package -n kdemultimedia-audiocd-i18n
Summary:	Internationalization and localization files for audiocd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla audiocd
Group:		X11/Applications
Requires:	kdemultimedia-audiocd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{kdemultimedia_epoch}:%{version}
Requires:	konqueror-i18n = %{kdebase_epoch}:%{version}

%description -n kdemultimedia-audiocd-i18n
Internationalization and localization files for audiocd.

%description -n kdemultimedia-audiocd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla audiocd.

%package -n kdemultimedia-libkcddb-i18n
Summary:	Internationalization and localization files for libkcddb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla libkcddb
Group:		X11/Applications
Requires:	kdemultimedia-libkcddb = %{kdemultimedia_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}

%description -n kdemultimedia-libkcddb-i18n
Internationalization and localization files for libkcddb.

%description -n kdemultimedia-libkcddb-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla libkcddb.

%package -n kdemultimedia-kaudiocreator-i18n
Summary:	Internationalization and localization files for kaudiocreator
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaudiocreatora
Group:		X11/Applications
Requires:	kdemultimedia-kaudiocreator = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kaudiocreator-i18n
Internationalization and localization files for kaudiocreator.

%description -n kdemultimedia-kaudiocreator-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaudiocreatora.

%package -n kdeadmin-kcron-i18n
Summary:	Internationalization and localization files for kcron
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcrona
Group:		X11/Applications
Requires:	kdeadmin-kcron = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-kcron-i18n
Internationalization and localization files for kcron.

%description -n kdeadmin-kcron-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcrona.

%package -n kdeadmin-kdat-i18n
Summary:	Internationalization and localization files for kdat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdat
Group:		X11/Applications
Requires:	kdeadmin-kdat = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-kdat-i18n
Internationalization and localization files for kdat.

%description -n kdeadmin-kdat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdat.

%package -n kdeadmin-kpackage-i18n
Summary:	Internationalization and localization files for kpackage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpackage
Group:		X11/Applications
Requires:	kdeadmin-kpackage = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-kpackage-i18n
Internationalization and localization files for kpackage.

%description -n kdeadmin-kpackage-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpackage.

%package -n kdeadmin-ksysv-i18n
Summary:	Internationalization and localization files for ksysv
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksysv
Group:		X11/Applications
Requires:	kdeadmin-ksysv = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-ksysv-i18n
Internationalization and localization files for ksysv.

%description -n kdeadmin-ksysv-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksysv.

%package -n kdeadmin-kuser-i18n
Summary:	Internationalization and localization files for kuser
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kusera
Group:		X11/Applications
Requires:	kdeadmin-kuser = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-kuser-i18n
Internationalization and localization files for kuser.

%description -n kdeadmin-kuser-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kusera.

%package -n kdeadmin-kcmlilo-i18n
Summary:	Internationalization and localization files for kcmlilo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcmlilo
Group:		X11/Applications
Requires:	kdeadmin-kcmlilo = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-kcmlilo-i18n
Internationalization and localization files for kcmlilo.

%description -n kdeadmin-kcmlilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlilo.

%package -n kdeadmin-kcmlinuz-i18n
Summary:	Internationalization and localization files for kcmlinuz
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcmlinuz
Group:		X11/Applications
Requires:	kdeadmin-kcmlinuz = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeadmin-kcmlinuz-i18n
Internationalization and localization files for kcmlinuz.

%description -n kdeadmin-kcmlinuz-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlinuz.

%package -n kde-decoration-cde-i18n
Summary:	Internationalization and localization files for kde-decoration-cde
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-cde
Group:		X11/Applications
Requires:	kde-decoration-cde = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kde-decoration-cde-i18n
Internationalization and localization files for kde-decoration-cde.

%description -n kde-decoration-cde-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-cde.

%package -n kde-decoration-icewm-i18n
Summary:	Internationalization and localization files for kde-decoration-icewm
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm
Group:		X11/Applications
Requires:	kde-decoration-icewm = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kde-decoration-icewm-i18n
Internationalization and localization files for kde-decoration-icewm.

%description -n kde-decoration-icewm-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm.

%package -n kde-decoration-glow-i18n
Summary:	Internationalization and localization files for kde-decoration-glow
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow
Group:		X11/Applications
Requires:	kde-decoration-glow = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kde-decoration-glow-i18n
Internationalization and localization files for kde-decoration-glow.

%description -n kde-decoration-glow-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow.

%package -n kde-decoration-plastik-i18n
Summary:	Internationalization and localization files for kde-decoration-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik
Group:		X11/Applications
Requires:	kde-decoration-plastik = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{kdebase_epoch}:%{version}

%description -n kde-decoration-plastik-i18n
Internationalization and localization files for kde-decoration-plastik.

%description -n kde-decoration-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik.

%package -n kde-style-plastik-i18n
Summary:	Internationalization and localization files for kde-style-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-style-plastik
Group:		X11/Applications
Requires:	kde-style-plastik = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kde-style-plastik-i18n
Internationalization and localization files for kde-style-plastik.

%description -n kde-style-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-style-plastik.

%package -n kdeartwork-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla screensavers
Group:		X11/Applications
Requires:	kdeartwork-screensavers = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-screensavers-i18n = %{kdebase_epoch}:%{version}

%description -n kdeartwork-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdeartwork-screensavers-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla screensavers.

%package -n kdeedu-flashkard-i18n
Summary:	Internationalization and localization files for flashkard
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla flashkarda
Group:		X11/Applications
Requires:	kdeedu-flashkard = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-flashkard-i18n
Internationalization and localization files for flashkard.

%description -n kdeedu-flashkard-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla flashkarda.

%package -n kdeedu-kalzium-i18n
Summary:	Internationalization and localization files for kalzium
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kalzium
Group:		X11/Applications
Requires:	kdeedu-kalzium = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kalzium-i18n
Internationalization and localization files for kalzium.

%description -n kdeedu-kalzium-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kalzium.

%package -n kdeedu-kbruch-i18n
Summary:	Internationalization and localization files for kbruch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbrucha
Group:		X11/Applications
Requires:	kdeedu-kbruch = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kbruch-i18n
Internationalization and localization files for kbruch.

%description -n kdeedu-kbruch-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbrucha.

%package -n kdeedu-keduca-i18n
Summary:	Internationalization and localization files for keduca
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla keduca
Group:		X11/Applications
Requires:	kdeedu-keduca = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-keduca-i18n
Internationalization and localization files for keduca.

%description -n kdeedu-keduca-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla keduca.

%package -n kdeedu-khangman-i18n
Summary:	Internationalization and localization files for khangman
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khangmana
Group:		X11/Applications
Requires:	kdeedu-khangman = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-khangman-i18n
Internationalization and localization files for khangman.

%description -n kdeedu-khangman-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khangmana.

%package -n kdeedu-kig-i18n
Summary:	Internationalization and localization files for kig
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kig
Group:		X11/Applications
Requires:	kdeedu-kig = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kig-i18n
Internationalization and localization files for kig.

%description -n kdeedu-kig-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kig.

%package -n kdeedu-kiten-i18n
Summary:	Internationalization and localization files for kiten
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kiten
Group:		X11/Applications
Requires:	kdeedu-kiten = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kiten-i18n
Internationalization and localization files for kiten.

%description -n kdeedu-kiten-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kiten.

%package -n kdeedu-klettres-i18n
Summary:	Internationalization and localization files for klettres
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klettres
Group:		X11/Applications
Requires:	kdeedu-klettres = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-klettres-i18n
Internationalization and localization files for klettres.

%description -n kdeedu-klettres-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klettres.

%package -n kdeedu-kmessedwords-i18n
Summary:	Internationalization and localization files for kmessedwords
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmessedwords
Group:		X11/Applications
Requires:	kdeedu-kmessedwords = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kmessedwords-i18n
Internationalization and localization files for kmessedwords.

%description -n kdeedu-kmessedwords-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmessedwords.

%package -n kdeedu-kmplot-i18n
Summary:	Internationalization and localization files for kmplot
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmplot
Group:		X11/Applications
Requires:	kdeedu-kmplot = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kmplot-i18n
Internationalization and localization files for kmplot.

%description -n kdeedu-kmplot-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmplot.

%package -n kdeedu-kpercentage-i18n
Summary:	Internationalization and localization files for kpercentage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpercentage
Group:		X11/Applications
Requires:	kdeedu-kpercentage = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kpercentage-i18n
Internationalization and localization files for kpercentage.

%description -n kdeedu-kpercentage-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpercentage.

%package -n kdeedu-kstars-i18n
Summary:	Internationalization and localization files for kstars
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstars
Group:		X11/Applications
Requires:	kdeedu-kstars = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kstars-i18n
Internationalization and localization files for kstars.

%description -n kdeedu-kstars-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kstars.

%package -n kdeedu-ktouch-i18n
Summary:	Internationalization and localization files for ktouch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktouch
Group:		X11/Applications
Requires:	kdeedu-ktouch = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-ktouch-i18n
Internationalization and localization files for ktouch.

%description -n kdeedu-ktouch-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktouch.

%package -n kdeedu-kverbos-i18n
Summary:	Internationalization and localization files for kverbos
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kverbos
Group:		X11/Applications
Requires:	kdeedu-kverbos = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kverbos-i18n
Internationalization and localization files for kverbos.

%description -n kdeedu-kverbos-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kverbos.

%package -n kdeedu-kvoctrain-i18n
Summary:	Internationalization and localization files for kvoctrain
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kvoctrain
Group:		X11/Applications
Requires:	kdeedu-kvoctrain = %{kdeedu_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdeedu-kvoctrain-i18n
Internationalization and localization files for kvoctrain.

%description -n kdeedu-kvoctrain-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kvoctrain.

%package -n kdegames-kmahjongg-i18n
Summary:	Internationalization and localization files for kmahjongg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmahjongga
Group:		X11/Applications
Requires:	kdegames-kmahjongg = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kmahjongg-i18n
Internationalization and localization files for kmahjongg.

%description -n kdegames-kmahjongg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmahjongga.

%package -n kdegames-ksmiletris-i18n
Summary:	Internationalization and localization files for ksmiletris
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksmiletrisa
Group:		X11/Applications
Requires:	kdegames-ksmiletris = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ksmiletris-i18n
Internationalization and localization files for ksmiletris.

%description -n kdegames-ksmiletris-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksmiletrisa.

%package -n kdegames-atlantik-i18n
Summary:	Internationalization and localization files for atlantik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla atlantika
Group:		X11/Applications
Requires:	kdegames-atlantik = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-atlantik-i18n
Internationalization and localization files for atlantik.

%description -n kdegames-atlantik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla atlantika.

%package -n kdegames-kasteroids-i18n
Summary:	Internationalization and localization files for kasteroids
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kasteroids
Group:		X11/Applications
Requires:	kdegames-kasteroids = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kasteroids-i18n
Internationalization and localization files for kasteroids.

%description -n kdegames-kasteroids-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kasteroids.

%package -n kdegames-katomic-i18n
Summary:	Internationalization and localization files for katomic
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla katomic
Group:		X11/Applications
Requires:	kdegames-katomic = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-katomic-i18n
Internationalization and localization files for katomic.

%description -n kdegames-katomic-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla katomic.

%package -n kdegames-kbackgammon-i18n
Summary:	Internationalization and localization files for kbackgammon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbackgammona
Group:		X11/Applications
Requires:	kdegames-kbackgammon = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kbackgammon-i18n
Internationalization and localization files for kbackgammon.

%description -n kdegames-kbackgammon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbackgammona.

%package -n kdegames-kbattleship-i18n
Summary:	Internationalization and localization files for kbattleship
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbattleship
Group:		X11/Applications
Requires:	kdegames-kbattleship = %{kdegames_epoch}:%{version}

Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kbattleship-i18n
Internationalization and localization files for kbattleship.

%description -n kdegames-kbattleship-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbattleship.

%package -n kdegames-kblackbox-i18n
Summary:	Internationalization and localization files for kblackbox
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kblackboksa
Group:		X11/Applications
Requires:	kdegames-kblackbox = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kblackbox-i18n
Internationalization and localization files for kblackbox.

%description -n kdegames-kblackbox-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kblackboksa.

%package -n kdegames-kbounce-i18n
Summary:	Internationalization and localization files for kbounce
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbounce
Group:		X11/Applications
Requires:	kdegames-kbounce = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kbounce-i18n
Internationalization and localization files for kbounce.

%description -n kdegames-kbounce-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kbounce.

%package -n kdegames-kenolaba-i18n
Summary:	Internationalization and localization files for kenolaba
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kenolaby
Group:		X11/Applications
Requires:	kdegames-kenolaba = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kenolaba-i18n
Internationalization and localization files for kenolaba.

%description -n kdegames-kenolaba-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kenolaby.

%package -n kdegames-kfouleggs-i18n
Summary:	Internationalization and localization files for kfouleggs
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfouleggs
Group:		X11/Applications
Requires:	kdegames-kfouleggs = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kfouleggs-i18n
Internationalization and localization files for kfouleggs.

%description -n kdegames-kfouleggs-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfouleggs.

%package -n kdegames-kgoldrunner-i18n
Summary:	Internationalization and localization files for kgoldrunner
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgoldrunnera
Group:		X11/Applications
Requires:	kdegames-kgoldrunner = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kgoldrunner-i18n
Internationalization and localization files for kgoldrunner.

%description -n kdegames-kgoldrunner-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgoldrunnera.

%package -n kdegames-kjumpingcube-i18n
Summary:	Internationalization and localization files for kjumpingcube
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjumpingcube
Group:		X11/Applications
Requires:	kdegames-kjumpingcube = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kjumpingcube-i18n
Internationalization and localization files for kjumpingcube.

%description -n kdegames-kjumpingcube-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjumpingcube.

%package -n kdegames-klickety-i18n
Summary:	Internationalization and localization files for klickety
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klickety
Group:		X11/Applications
Requires:	kdegames-klickety = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-klickety-i18n
Internationalization and localization files for klickety.

%description -n kdegames-klickety-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klickety.

%package -n kdegames-klines-i18n
Summary:	Internationalization and localization files for klines
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klines
Group:		X11/Applications
Requires:	kdegames-klines = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-klines-i18n
Internationalization and localization files for klines.

%description -n kdegames-klines-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klines.

%package -n kdegames-kmines-i18n
Summary:	Internationalization and localization files for kmines
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmines
Group:		X11/Applications
Requires:	kdegames-kmines = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kmines-i18n
Internationalization and localization files for kmines.

%description -n kdegames-kmines-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmines.

%package -n kdegames-kolf-i18n
Summary:	Internationalization and localization files for kolf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kolfa
Group:		X11/Applications
Requires:	kdegames-kolf = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kolf-i18n
Internationalization and localization files for kolf.

%description -n kdegames-kolf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kolfa.

%package -n kdegames-konquest-i18n
Summary:	Internationalization and localization files for konquest
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla konquesta
Group:		X11/Applications
Requires:	kdegames-konquest = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-konquest-i18n
Internationalization and localization files for konquest.

%description -n kdegames-konquest-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla konquesta.

%package -n kdegames-kpat-i18n
Summary:	Internationalization and localization files for kpat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpata
Group:		X11/Applications
Requires:	kdegames-kpat = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kpat-i18n
Internationalization and localization files for kpat.

%description -n kdegames-kpat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpata.

%package -n kdegames-kpoker-i18n
Summary:	Internationalization and localization files for kpoker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpokera
Group:		X11/Applications
Requires:	kdegames-kpoker = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kpoker-i18n
Internationalization and localization files for kpoker.

%description -n kdegames-kpoker-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpokera.

%package -n kdegames-kreversi-i18n
Summary:	Internationalization and localization files for kreversi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kreversi
Group:		X11/Applications
Requires:	kdegames-kreversi = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kreversi-i18n
Internationalization and localization files for kreversi.

%description -n kdegames-kreversi-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kreversi.

%package -n kdegames-ksame-i18n
Summary:	Internationalization and localization files for ksame
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksame
Group:		X11/Applications
Requires:	kdegames-ksame = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ksame-i18n
Internationalization and localization files for ksame.

%description -n kdegames-ksame-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksame.

%package -n kdegames-kshisen-i18n
Summary:	Internationalization and localization files for kshisen
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kshisen
Group:		X11/Applications
Requires:	kdegames-kshisen = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kshisen-i18n
Internationalization and localization files for kshisen.

%description -n kdegames-kshisen-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kshisen.

%package -n kdegames-ksirtet-i18n
Summary:	Internationalization and localization files for ksirtet
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirteta
Group:		X11/Applications
Requires:	kdegames-ksirtet = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ksirtet-i18n
Internationalization and localization files for ksirtet.

%description -n kdegames-ksirtet-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksirteta.

%package -n kdegames-ksnake-i18n
Summary:	Internationalization and localization files for ksnake
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksnake'a
Group:		X11/Applications
Requires:	kdegames-ksnake = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ksnake-i18n
Internationalization and localization files for ksnake.

%description -n kdegames-ksnake-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksnake'a.

%package -n kdegames-ksokoban-i18n
Summary:	Internationalization and localization files for ksokoban
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksokobana
Group:		X11/Applications
Requires:	kdegames-ksokoban = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ksokoban-i18n
Internationalization and localization files for ksokoban.

%description -n kdegames-ksokoban-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksokobana.

%package -n kdegames-kspaceduel-i18n
Summary:	Internationalization and localization files for kspaceduel
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspaceduel
Group:		X11/Applications
Requires:	kdegames-kspaceduel = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kspaceduel-i18n
Internationalization and localization files for kspaceduel.

%description -n kdegames-kspaceduel-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kspaceduel.

%package -n kdegames-ktron-i18n
Summary:	Internationalization and localization files for ktron
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktrona
Group:		X11/Applications
Requires:	kdegames-ktron = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ktron-i18n
Internationalization and localization files for ktron.

%description -n kdegames-ktron-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktrona.

%package -n kdegames-ktuberling-i18n
Summary:	Internationalization and localization files for ktuberling
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktuberlinga
Group:		X11/Applications
Requires:	kdegames-ktuberling = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-ktuberling-i18n
Internationalization and localization files for ktuberling.

%description -n kdegames-ktuberling-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktuberlinga.

%package -n kdegames-kwin4-i18n
Summary:	Internationalization and localization files for kwin4
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwin4
Group:		X11/Applications
Requires:	kdegames-kwin4 = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-kwin4-i18n
Internationalization and localization files for kwin4.

%description -n kdegames-kwin4-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwin4.

%package -n kdegames-lskat-i18n
Summary:	Internationalization and localization files for lskat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lskata
Group:		X11/Applications
Requires:	kdegames-lskat = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-lskat-i18n
Internationalization and localization files for lskat.

%description -n kdegames-lskat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla lskata.

%package -n kdegames-megami-i18n
Summary:	Internationalization and localization files for megami
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla megami
Group:		X11/Applications
Requires:	kdegames-megami = %{kdegames_epoch}:%{version}
Requires:	kdebase-core-i18n = %{kdebase_epoch}:%{version}

%description -n kdegames-megami-i18n
Internationalization and localization files for megami.

%description -n kdegames-megami-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla megami.



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
%find_lang flashkard	--with-kde
%find_lang kalzium	--with-kde
%find_lang kbruch	--with-kde
%find_lang keduca	--with-kde
%find_lang khangman	--with-kde
%find_lang kig		--with-kde
%find_lang kiten	--with-kde
%find_lang klettres	--with-kde
%find_lang kmathtool	--with-kde
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

> %{name}.lang
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
	windowmanagement"

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

%find_lang	kate		--with-kde
%find_lang	kcmkonsole	--with-kde
%find_lang	kdm		--with-kde
%find_lang	kfind		--with-kde
%find_lang	kcmfontinst	--with-kde
%find_lang	kinfocenter	--with-kde
%find_lang	kioslave	--with-kde
%find_lang	klipper		--with-kde
%find_lang	kmenuedit	--with-kde
%find_lang	konsole		--with-kde
%find_lang	ksysguard	--with-kde
%find_lang	kpager		--with-kde
%find_lang	kwrite		--with-kde
%find_lang	screensaver	--with-kde

cat kcmkonsole.lang	>> konsole.lang
cat kioslave.lang	>> kinfocenter.lang

files="core \
kdebase \
kicker \
konqueror \
konsole \
kinfocenter \
kate \
kdm \
kfind \
kioslave \
klipper \
kmenuedit \
ksysguard \
kpager \
kwrite \
screensaver \
kcmfontinst"

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
kcmmidi"

for i in $desktop;
do
	%find_lang $i	--with-kde
	cat $i.lang >> %{name}.lang
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

%find_lang kwriteconfig	--with-kde
cat kwriteconfig.lang >> kwrite.lang

%find_lang libkonq	--with-kde

mn="kio_imap4 \
kio_pop3 \
kio_nntp \
kio_smtp"

for i in $mn;
do
	%find_lang $i	--with-kde
	cat $i.lang >> mailnews.lang
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






for i in $RPM_BUILD_ROOT%{_datadir}/apps/sounds/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e s,${RPM_BUILD_ROOT}%{_datadir}/apps/sounds/,,`
	echo %lang\($z\) %{_datadir}/apps/sounds/$z >> ktuberling.lang
	fi
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

cat kalarm.lang >> korganizer.lang
cat kalarmd.lang >> korganizer.lang
cat kgpgcertmanager.lang >> kmail.lang

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

# Not packaging kmobile, it was disabled by coolo
%find_lang kdgantt		--with-kde
%find_lang ktnef		--with-kde

%find_lang libkcal		--with-kde
%find_lang libkcalsystem	--with-kde
cat libkcalsystem.lang >> libkcal.lang

%find_lang libkdenetwork	--with-kde
%find_lang libkdepim		--with-kde
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
mv -f libksieve.lang kmail_libs.lang
%find_lang kdict		--with-kde
%find_lang kget			--with-kde
%find_lang knewsticker		--with-kde
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

#%%find_lang kxmlrpcd		--with-kde
#%%find_lang kcmkxmlrpcd		--with-kde
#cat kcmkxmlrpcd.lang >> kxmlrpcd.lang

%find_lang ktalkd		--with-kde
%find_lang kcmtalkd		--with-kde
%find_lang kcmktalkd		--with-kde
cat kcmtalkd.lang >> ktalkd.lang
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
> kdf.lang
%find_lang kdf			--with-kde
%find_lang blockdevices		--with-kde
cat blockdevices.lang >> kdf.lang
%find_lang kedit		--with-kde
%find_lang kfloppy		--with-kde
%find_lang kgpg			--with-kde
%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
%find_lang klaptopdaemon        --with-kde
%find_lang kcmlowbatcrit	--with-kde
%find_lang kcmlowbatwarn	--with-kde
%find_lang laptop		--with-kde
%find_lang powerctrl		--with-kde
cat {kcmlowbatcrit,kcmlowbatwarn,laptop,powerctrl}.lang >> klaptopdaemon.lang
%find_lang ksim			--with-kde
%find_lang ktimer		--with-kde
%find_lang kwallet		--with-kde
%find_lang kdelirc              --with-kde
%find_lang irkick	        --with-kde
%find_lang kcmlirc              --with-kde
cat irkick.lang >> kdelirc.lang
cat kcmlirc.lang >> kdelirc.lang

%find_lang kwalletmanager	--with-kde
cat kwalletmanager.lang >> kwallet.lang
%find_lang kcmkwallet		--with-kde
cat kcmkwallet.lang >> kwallet.lang

%find_lang kcmlaptop		--with-kde
cat kcmlaptop.lang >> klaptopdaemon.lang
%find_lang kcmkvaio		--with-kde
cat kcmkvaio.lang >> kmilo.lang

%find_lang kregexpeditor	--with-kde
cat kregexpeditor.lang >> KRegExpEditor.lang

%find_lang kcharselectapplet	--with-kde
cat kcharselectapplet.lang >> kcharselect.lang

%find_lang userinfo		--with-kde
%find_lang kdessh		--with-kde
%find_lang kdepasswd            --with-kde
# We dont buidl kcardchooser (disabled by default by coolo) 
# renaableing it would be posssible, but what for?
# %find_lang kcardchooser            --with-kde
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
wav"
> kfile.lang

for i in $kfile;
do
	%find_lang kfile_${i} --with-kde
	cat kfile_${i}.lang >> kfile.lang
done

for i in $libz;
do
	%find_lang libz --with-kde
	cat $i.lang >> kdelibs.lang
done


%files -n kdelibs-i18n -f kdelibs.lang
%files -n kdeadmin-kcron-i18n -f kcron.lang
%files -n kdeadmin-kdat-i18n -f kdat.lang
%files -n kdeadmin-kpackage-i18n -f kpackage.lang
%files -n kdeadmin-ksysv-i18n -f ksysv.lang
%files -n kdeadmin-kuser-i18n -f kuser.lang
%files -n kdeadmin-kcmlinuz-i18n -f kcmlinuz.lang
%files -n kde-decoration-cde-i18n -f kwin_cde_config.lang
%files -n kde-decoration-icewm-i18n -f kwin_icewm_config.lang
%files -n kde-decoration-glow-i18n -f kwin_glow_config.lang
%files -n kde-decoration-plastik-i18n -f kwin_plastik_config.lang
%files -n kde-style-plastik-i18n -f kstyle_plastik_config.lang
%files -n kdeartwork-screensavers-i18n -f screensavers.lang
%files -n kdeedu-flashkard-i18n -f flashkard.lang
%files -n kdeedu-kalzium-i18n -f kalzium.lang
%files -n kdeedu-kbruch-i18n -f kbruch.lang
%files -n kdeedu-keduca-i18n -f keduca.lang
%files -n kdeedu-khangman-i18n -f khangman.lang
%files -n kdeedu-kig-i18n -f kig.lang
%files -n kdeedu-kiten-i18n -f kiten.lang
%files -n kdeedu-klettres-i18n -f klettres.lang
%files -n kdeedu-kmessedwords-i18n -f kmessedwords.lang
%files -n kdeedu-kmplot-i18n -f kmplot.lang
%files -n kdeedu-kpercentage-i18n -f kpercentage.lang
%files -n kdeedu-kstars-i18n -f kstars.lang
%files -n kdeedu-ktouch-i18n -f ktouch.lang
%files -n kdeedu-kverbos-i18n -f kverbos.lang
%files -n kdeedu-kvoctrain-i18n -f kvoctrain.lang
%files -n kdegames-ksmiletris-i18n -f ksmiletris.lang
%files -n kdegames-kmahjongg-i18n -f kmahjongg.lang
%files -n kdegames-atlantik-i18n -f atlantik.lang
%files -n kdegames-kasteroids-i18n -f kasteroids.lang
%files -n kdegames-katomic-i18n -f katomic.lang
%files -n kdegames-kbackgammon-i18n -f kbackgammon.lang
%files -n kdegames-kbattleship-i18n -f kbattleship.lang
%files -n kdegames-kblackbox-i18n -f kblackbox.lang
%files -n kdegames-kbounce-i18n -f kbounce.lang
%files -n kdegames-kenolaba-i18n -f kenolaba.lang
%files -n kdegames-kfouleggs-i18n -f kfouleggs.lang
%files -n kdegames-kgoldrunner-i18n -f kgoldrunner.lang
%files -n kdegames-kjumpingcube-i18n -f kjumpingcube.lang
%files -n kdegames-klickety-i18n -f klickety.lang
%files -n kdegames-klines-i18n -f klines.lang
%files -n kdegames-kmines-i18n -f kmines.lang
%files -n kdegames-kolf-i18n -f kolf.lang
%files -n kdegames-konquest-i18n -f konquest.lang
%files -n kdegames-kpat-i18n -f kpat.lang
%files -n kdegames-kpoker-i18n -f kpoker.lang
%files -n kdegames-kreversi-i18n -f kreversi.lang
%files -n kdegames-ksame-i18n -f ksame.lang
%files -n kdegames-kshisen-i18n -f kshisen.lang
%files -n kdegames-ksirtet-i18n -f ksirtet.lang
%files -n kdegames-ksnake-i18n -f ksnake.lang
%files -n kdegames-ksokoban-i18n -f ksokoban.lang
%files -n kdegames-kspaceduel-i18n -f kspaceduel.lang
%files -n kdegames-ktron-i18n -f ktron.lang
%files -n kdegames-ktuberling-i18n -f ktuberling.lang
%files -n kdegames-kwin4-i18n -f kwin4.lang
%files -n kdegames-lskat-i18n -f lskat.lang
##%%files -n kdegames-megami-i18n -f megami.lang
%files -n kdebase-core-i18n -f core.lang
%files -n kdebase-desktop-i18n -f kdebase.lang
%files -n kdebase-infocenter-i18n -f kinfocenter.lang
%files -n kdebase-kate-i18n -f kate.lang
%files -n kdebase-kfind-i18n -f kfind.lang
%files -n kdebase-kfontinst-i18n -f kcmfontinst.lang
%files -n kdebase-klipper-i18n -f klipper.lang
%files -n kdebase-kmenuedit-i18n -f kmenuedit.lang
%files -n kdebase-konsole-i18n -f konsole.lang
%files -n kdebase-kpager-i18n -f kpager.lang
%files -n kdebase-ksysguard-i18n -f ksysguard.lang
%files -n kdebase-kwrite-i18n -f kwrite.lang
%files -n kdebase-screensavers-i18n -f screensaver.lang
%files -n kdebase-common-filemanagement-i18n -f kcmfileshare.lang
%files -n kdebase-desktop-libs-i18n -f ksplashthemes.lang
%files -n kdebase-kappfinder-i18n -f kappfinder.lang
%files -n kdebase-kdcop-i18n -f kdcop.lang
%files -n kdebase-kdeprintfax-i18n -f kdeprintfax.lang
%files -n kdebase-kdialog-i18n -f kdialog.lang
%files -n kdebase-kjobviewer-i18n -f kjobviewer.lang
%files -n kdebase-kpersonalizer-i18n -f kpersonalizer.lang
%files -n kdebase-ksystraycmd-i18n -f ksystraycmd.lang
%files -n kdebase-libkonq-i18n -f libkonq.lang
%files -n kdebase-mailnews-i18n -f mailnews.lang
%files -n kdm-i18n -f kdm.lang
%files -n konqueror-i18n -f konqueror.lang
%files -n kde-decoration-b2-i18n -f kwin_b2_config.lang
%files -n kde-decoration-modernsys-i18n -f kwin_modernsys_config.lang
%files -n kde-decoration-quartz-i18n -f kwin_quartz_config.lang
%files -n kdepim-kaddressbook-i18n -f kaddressbook.lang
%files -n kdepim-kandy-i18n -f kandy.lang
%files -n kdepim-karm-i18n -f karm.lang
%files -n kdepim-kmail-i18n -f kmail.lang
%files -n kdepim-knode-i18n -f knode.lang
%files -n kdepim-knotes-i18n -f knotes.lang
%files -n kdepim-konsolekalendar-i18n -f konsolekalendar.lang
%files -n kdepim-kontact-i18n -f kontact.lang
%files -n kdepim-korganizer-i18n -f korganizer.lang
%files -n kdepim-korn-i18n -f korn.lang
%files -n kdepim-kpilot-i18n -f kpilot.lang
%files -n kdepim-libkdepim-i18n -f libkdepim.lang
%files -n kdepim-libkdenetwork-i18n -f libkdenetwork.lang
%files -n kdepim-kmail-libs-i18n -f kmail_libs.lang
%files  -n kdenetwork-kdict-i18n -f kdict.lang
%files  -n kdenetwork-kget-i18n -f kget.lang
%files  -n kdenetwork-knewsticker-i18n -f knewsticker.lang
%files  -n kdenetwork-kopete-i18n -f kopete.lang
%files  -n kdenetwork-kpf-i18n -f kpf.lang
%files  -n kdenetwork-kppp-i18n -f kppp.lang
%files  -n kdenetwork-krfb-i18n -f krfb.lang
%files  -n kdenetwork-ksirc-i18n -f ksirc.lang
%files  -n kdenetwork-ktalkd-i18n -f ktalkd.lang
%files  -n kdenetwork-kwifimanager-i18n -f kwifimanager.lang
%files  -n kdenetwork-lanbrowser-i18n -f lisa.lang
%files  -n kdenetwork-kinetd-i18n -f kinetd.lang
%files  -n kdenetwork-rss-i18n -f dcopservice.lang
%files  -n kdeaccessibility-kmag-i18n -f kmag.lang
%files  -n kdeaccessibility-kmousetool-i18n -f kmousetool.lang
%files  -n kdeaccessibility-kmouth-i18n -f kmouth.lang
%files  -n kdeutils-ark-i18n -f ark.lang
%files  -n kdeutils-kcalc-i18n -f kcalc.lang
%files  -n kdeutils-kcharselect-i18n -f kcharselect.lang
%files  -n kdeutils-kdf-i18n -f kdf.lang
%files  -n kdeutils-kedit-i18n -f kedit.lang
%files  -n kdeutils-kfloppy-i18n -f kfloppy.lang
%files  -n kdeutils-kgpg-i18n -f kgpg.lang
%files  -n kdeutils-khexedit-i18n -f khexedit.lang
%files  -n kdeutils-kjots-i18n -f kjots.lang
%files  -n kdeutils-klaptopdaemon-i18n -f klaptopdaemon.lang
%files  -n kdeutils-kregexpeditor-i18n -f KRegExpEditor.lang
%files  -n kdeutils-ksim-i18n -f ksim.lang
%files  -n kdeutils-ktimer-i18n -f ktimer.lang
%files  -n kdeutils-kwalletmanager-i18n -f kwallet.lang
%files  -n kdeutils-kdelirc-i18n -f kdelirc.lang
%files  -n kdeutils-userinfo-i18n -f userinfo.lang
%files  -n kdeutils-kdessh-i18n -f kdessh.lang
%files  -n kdeutils-kdepasswd-i18n -f kdepasswd.lang
%files  -n kdeutils-kmilo-i18n -f kmilo.lang
%files  -n kdemultimedia-artsbuilder-i18n -f artsbuilder.lang
%files  -n kdemultimedia-artscontrol-i18n -f artscontrol.lang
%files  -n kdemultimedia-arts-i18n -f arts.lang
%files  -n kdemultimedia-juk-i18n -f juk.lang
%files  -n kdemultimedia-kaboodle-i18n -f kaboodle.lang
%files  -n kdemultimedia-kmid-i18n -f kmid.lang
%files  -n kdemultimedia-kmix-i18n -f kmix.lang
%files  -n kdemultimedia-kscd-i18n -f kscd.lang
%files  -n kdemultimedia-krec-i18n -f krec.lang
%files  -n kdemultimedia-noatun-i18n -f noatun.lang
%files  -n kdemultimedia-kfile-i18n -f kfile.lang
%files  -n kdemultimedia-audiocd-i18n -f kio_audiocd.lang
%files  -n kdemultimedia-kaudiocreator-i18n -f kaudiocreator.lang
%files  -n kdemultimedia-libkcddb-i18n -f libkcddb.lang

%ifarch %{ix86} 
%files -n kdeadmin-kcmlilo-i18n -f kcmlilo.lang
%endif
