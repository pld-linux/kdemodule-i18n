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
Requires:	kdepim-libkmailprivate-i18n = %{kdepim_epoch}:%{version}
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

%package -n kdepim-libkmailprivate-i18n
Summary:	Internationalization and localization files for libkmailprivate
Summary(pl):	T³umaczenia dla libkmailprivate
Group:		X11/Applications
Requires:	kdepim-libkdepim = %{kdepim_epoch}:%{version}
Requires:	kdepim-libkdenetwork = %{kdepim_epoch}:%{version}
Requires:	kdelibs-i18n = %{kdelibs_epoch}:%{version}
Obsoletes:	kdepim-libksieve-i18n = %{kdepim_epoch}:%{version}

%description -n kdepim-libkmailprivate-i18n
Internationalization and localization files for libkmailprivate.

%description -n kdepim-libkmailprivate-i18n -l pl
T³umaczenia dla libkmailprivate.

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
