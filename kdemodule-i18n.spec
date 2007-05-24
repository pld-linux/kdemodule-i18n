# NOTE
# - difference between kdemodule-i18n and kde-i18n is that one is per
#   package and other is per language.
# - do not add %%ifarch here, as it's noarch package
#
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
%define		kdevelop_version	3.4.1
%define		kdewebdev_epoch		2
#
%define		_state		stable
%define		_name		kde-i18n
#
Summary:	K Desktop Environment - international support
Summary(pl.UTF-8):	KDE - wsparcie dla wielu języków
Name:		kdemodule-i18n
Version:	3.5.7
Release:	1
Epoch:		10
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-af-%{version}.tar.bz2
# Source0-md5:	9fc56e59816271c09922f08738ebce6f
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ar-%{version}.tar.bz2
# Source1-md5:	d2d0628ce887766965b6bca2015f99c8
Source2:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-az-%{version}.tar.bz2
# Source2-md5:	c2039b4e65e61dbbe095032d6a6f5e38
Source3:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-bg-%{version}.tar.bz2
# Source3-md5:	f865993d0be0eef709e86fcefd4e9d01
Source4:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-bn-%{version}.tar.bz2
# Source4-md5:	9e329981b6938e358c9b6647fb07b8c2
Source5:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-br-%{version}.tar.bz2
# Source5-md5:	d112abe01375048fde57c58f2e60e63a
Source6:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-bs-%{version}.tar.bz2
# Source6-md5:	4828cc85cdb5b242c37af963432d1792
Source7:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ca-%{version}.tar.bz2
# Source7-md5:	4ca083e7a1702365f2de35ff79fd41e0
Source8:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-cs-%{version}.tar.bz2
# Source8-md5:	350a29c5166640bb7f4030dc45da6c48
Source9:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-csb-%{version}.tar.bz2
# Source9-md5:	ef5fbce181df8ac2ea0c0d773e10f6c4
Source10:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-cy-%{version}.tar.bz2
# Source10-md5:	49b3d60531a0fbb050ec30df8135c07f
Source11:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-da-%{version}.tar.bz2
# Source11-md5:	a13e84cbdb6b6fd89034efa33ea87266
Source12:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-de-%{version}.tar.bz2
# Source12-md5:	ffba95578d4ffd07dd5488a6610cb3c8
Source13:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-el-%{version}.tar.bz2
# Source13-md5:	995d8c13bc0eccacc5c53d40b948e03e
Source14:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-en_GB-%{version}.tar.bz2
# Source14-md5:	1efad85761ec1fa03290204e562adac4
Source15:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-eo-%{version}.tar.bz2
# Source15-md5:	853f24c711ed787adfd901d6be5f5b3f
Source16:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-es-%{version}.tar.bz2
# Source16-md5:	cc0c23885bc71637cb045069896545b5
Source17:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-et-%{version}.tar.bz2
# Source17-md5:	4103433d895c818c4213993ec818aad1
Source18:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-eu-%{version}.tar.bz2
# Source18-md5:	e11781e87059cc9cc1570fcd4d3c9279
Source19:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-fa-%{version}.tar.bz2
# Source19-md5:	bc71ddcd6b6c6fa765591d12befefc66
Source20:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-fi-%{version}.tar.bz2
# Source20-md5:	18682d8351c70d2b483c2b55706025f0
Source21:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-fr-%{version}.tar.bz2
# Source21-md5:	f6ddf4a9eeb3748fcbf781ff4c3c4edb
Source22:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-fy-%{version}.tar.bz2
# Source22-md5:	d6c5182349c6b448edcd63a8cb737859
Source23:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ga-%{version}.tar.bz2
# Source23-md5:	e33342045b81dd4df200f56d615d3590
Source24:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-gl-%{version}.tar.bz2
# Source24-md5:	7a25eef435e4daca31f6507be216b060
Source25:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-he-%{version}.tar.bz2
# Source25-md5:	0f2fb7c7538ce15fbbfb5a4f19e78b73
Source26:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-hi-%{version}.tar.bz2
# Source26-md5:	46cc5b60e42f260a6ee4d4b5cc53851b
Source27:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-hr-%{version}.tar.bz2
# Source27-md5:	7ec644927e8d4606caf0a017f5c177ea
Source28:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-hu-%{version}.tar.bz2
# Source28-md5:	f10056e1dbb1955f2ba3cbba8a50a08b
Source29:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-is-%{version}.tar.bz2
# Source29-md5:	b86b28fec7ff948c97df15c972553900
Source30:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-it-%{version}.tar.bz2
# Source30-md5:	a04a26135303cef25f74373e07df0157
Source31:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ja-%{version}.tar.bz2
# Source31-md5:	797df078ef3dc7f3cd095311a62c56e2
Source32:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-kk-%{version}.tar.bz2
# Source32-md5:	0d8295e47c2ee65da1845e224470c5dd
Source33:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-km-%{version}.tar.bz2
# Source33-md5:	b1564f042ba6f7cd5cb2341d3f18f86f
Source34:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ko-%{version}.tar.bz2
# Source34-md5:	32ede9542bdc84f33ea56d5d4b33c7f2
Source35:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-lt-%{version}.tar.bz2
# Source35-md5:	6774803f35f4accba712a7fa1fce50d8
Source36:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-lv-%{version}.tar.bz2
# Source36-md5:	2e67dcb10511415f09f33e2142ebc504
Source37:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-mk-%{version}.tar.bz2
# Source37-md5:	a8fafdfe962f310ca968a81a7db0adbe
Source38:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-mn-%{version}.tar.bz2
# Source38-md5:	a375fb5e27447e566a95660057af122e
Source39:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ms-%{version}.tar.bz2
# Source39-md5:	566168896b51d93f9e1c11a0ec84db68
Source40:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-nb-%{version}.tar.bz2
# Source40-md5:	0b66b0265556c7892f13d20d30f61423
Source41:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-nds-%{version}.tar.bz2
# Source41-md5:	f5c1fd976b345bfa5a5ec91aec0c1d29
Source42:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-nl-%{version}.tar.bz2
# Source42-md5:	0bc7c76717a67da18a5bcfb1dda278ef
Source43:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-nn-%{version}.tar.bz2
# Source43-md5:	9364ceaf89c1e3b1d5d957d0f8cc9826
Source44:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-pa-%{version}.tar.bz2
# Source44-md5:	20d4043b002dad7fc9ff4aa319561f27
Source45:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-pl-%{version}.tar.bz2
# Source45-md5:	c5a58fb84ce0f19e908b3a65f699e880
Source46:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-pt-%{version}.tar.bz2
# Source46-md5:	696b4d75f81231e43f898e7c703d133d
Source47:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-pt_BR-%{version}.tar.bz2
# Source47-md5:	c7fc3d50c3fb27d8560412156dc464fb
Source48:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ro-%{version}.tar.bz2
# Source48-md5:	81eb9ede8fa9073a997d3366ca236f96
Source49:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ru-%{version}.tar.bz2
# Source49-md5:	b0a0edf56a5444d74dca527556a59ae3
Source50:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-rw-%{version}.tar.bz2
# Source50-md5:	69240b537d68e84a727ecbc54a471cb0
Source51:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-se-%{version}.tar.bz2
# Source51-md5:	a5dc3120ccbea37cc4e6423d4bb2fbac
Source52:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-sk-%{version}.tar.bz2
# Source52-md5:	b2c5da89f8b5df63991deb47674bdbb9
Source53:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-sl-%{version}.tar.bz2
# Source53-md5:	5b2eff146028bffeb84315aaafa5ea5d
Source54:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-sr-%{version}.tar.bz2
# Source54-md5:	06099c0a4a7c84115e06c40256ed97ff
Source55:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-sr@Latn-%{version}.tar.bz2
# Source55-md5:	1cbde47602550b462e91e4a7b5bbe8c8
Source56:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ss-%{version}.tar.bz2
# Source56-md5:	def410b2a9ff67e03138c2acd98382a3
Source57:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-sv-%{version}.tar.bz2
# Source57-md5:	26fcaf78f44e67e3bda09e187fa85374
Source58:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-ta-%{version}.tar.bz2
# Source58-md5:	c6798c99e32ea3b1e4817b1f1e2857b5
Source59:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-tg-%{version}.tar.bz2
# Source59-md5:	41b096c7409bcdc7d32aa97f3547d4bc
Source60:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-th-%{version}.tar.bz2
# Source60-md5:	11a49cc84cc87306dad4c61286ae0048
Source61:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-tr-%{version}.tar.bz2
# Source61-md5:	90326b113d8e77497a3eb1d0d87ed65c
Source62:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-uk-%{version}.tar.bz2
# Source62-md5:	cee28788e68efeb77fd672a31e206e8e
Source63:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-uz-%{version}.tar.bz2
# Source63-md5:	068da2a91ee5a06a4c9c18853336074e
Source64:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-vi-%{version}.tar.bz2
# Source64-md5:	f8aa01eea219b5ed34ecc312a42c50fe
Source65:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-zh_CN-%{version}.tar.bz2
# Source65-md5:	ef0bf6dcdf3c05bf6a775abfae1944b9
Source66:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{_name}-zh_TW-%{version}.tar.bz2
# Source66-md5:	d5a68ed78b436874bb41c1e9c423b3ac

URL:		http://i18n.kde.org/
BuildRequires:	kdelibs-devel >= %{kdelibs_epoch}:%{version}
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_py_hardlink	1

%description
K Desktop Environment - international support.

%description -l pl.UTF-8
KDE - wsparcie dla wielu języków.

%package -n kde-decoration-common-i18n
Summary:	Common internationalization and localization files for kwin decorations
Summary(pl.UTF-8):	Wspólne pliki umiędzynarodawiające dla dekoracji kwin
Group:		X11/Applications

%description -n kde-decoration-common-i18n
Common internationalization and localization files for kwin
decorations.

%description -n kde-decoration-common-i18n -l pl.UTF-8
Wspólne pliki umiędzynarodawiające dla dekoracji kwin.

%package -n kde-kgreet-classic-i18n
Summary:	KDE greeter libraries - i18n
Summary(pl.UTF-8):	Biblioteki służące do zapytań o hasło - tłumaczenia
Group:		X11/Applications
Requires:	kde-kgreet-classic = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kde-kgreet-classic-i18n
Tools for asking for passwords in the classic, default look - i18n.

%description -n kde-kgreet-classic-i18n -l pl.UTF-8
Narzędzia służące do zapytań o hasło - klasyczny, domyślny
motyw wyglądu - tłumaczenia.

%package -n kde-kio-groupwise-i18n
Summary:	Internationalization and localization files for groupwise ioslave
Summary(pl.UTF-8):	Tłumaczenia dla groupwise ioslave
Group:		X11/Applications
Requires:	kde-kio-groupwise = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kde-kio-groupwise-i18n
Internationalization and localization files for groupwise ioslave.

%description -n kde-kio-groupwise-i18n -l pl.UTF-8
Tłumaczenia dla groupwise ioslave.

%package -n kde-kio-imap4-i18n
Summary:	Internationalization and localization files for imap4 ioslave
Summary(pl.UTF-8):	Tłumaczenia dla imap4 ioslave
Group:		X11/Applications
Requires:	kde-kio-imap4 = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kde-kio-newimap4-i18n
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-imap4-i18n
Internationalization and localization files for imap4 ioslave.

%description -n kde-kio-imap4-i18n -l pl.UTF-8
Tłumaczenia dla imap4 ioslave.

%package -n kde-kio-ldap-i18n
Summary:	Internationalization and localization files for ldap ioslave
Summary(pl.UTF-8):	Tłumaczenia dla ldap ioslave
Group:		X11/Applications
Requires:	kde-kio-ldap = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	konqueror-i18n < %{epoch}:%{version}-%{release}

%description -n kde-kio-ldap-i18n
Internationalization and localization files for ldap ioslave.

%description -n kde-kio-ldap-i18n -l pl.UTF-8
Tłumaczenia dla ldap ioslave.

%package -n kde-kio-nntp-i18n
Summary:	Internationalization and localization files for nntp ioslave
Summary(pl.UTF-8):	Tłumaczenia dla nntp ioslave
Group:		X11/Applications
Requires:	kde-kio-nntp = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-nntp-i18n
Internationalization and localization files for nntp ioslave.

%description -n kde-kio-nntp-i18n -l pl.UTF-8
Tłumaczenia dla nntp ioslave.

%package -n kde-kio-pop3-i18n
Summary:	Internationalization and localization files for pop3 ioslave
Summary(pl.UTF-8):	Tłumaczenia dla pop3 ioslave
Group:		X11/Applications
Requires:	kde-kio-pop3 = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-pop3-i18n
Internationalization and localization files for pop3 ioslave.

%description -n kde-kio-pop3-i18n -l pl.UTF-8
Tłumaczenia dla pop3 ioslave.

%package -n kde-kio-smtp-i18n
Summary:	Internationalization and localization files for smtp ioslave
Summary(pl.UTF-8):	Tłumaczenia dla smtp ioslave
Group:		X11/Applications
Requires:	kde-kio-smtp = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-mailnews-i18n

%description -n kde-kio-smtp-i18n
Internationalization and localization files for smtp ioslave.

%description -n kde-kio-smtp-i18n -l pl.UTF-8
Tłumaczenia dla smtp ioslave.

%package -n kde-kio-svn-i18n
Summary:	Internationalization and localization files for svn ioslave
Summary(pl.UTF-8):	Tłumaczenia dla svn ioslave
Group:		X11/Applications
Requires:	kde-kio-svn = %{kdesdk_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kde-kio-svn-i18n
Internationalization and localization files for svn ioslave.

%description -n kde-kio-svn-i18n -l pl.UTF-8
Tłumaczenia dla svn ioslave.

%package -n kde-resource-bugzilla-i18n
Summary:	Internationalization and localization files for bugzilla plugin for the KDE PIM framework
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla wtyczki bugzilla do szkieletu KDE PIM
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kde-resource-bugzilla = %{kdesdk_epoch}:%{version}

%description -n kde-resource-bugzilla-i18n
Internationalization and localization files for KDE PIM plugin that
allows creating bugzilla TODO lists.

%description -n kde-resource-bugzilla-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla wtyczki KDE PIM pozwalającej na
tworzenie list rzeczy do zrobienia (TODO) w bugzilli.

%package -n kdeaccessibility-kbstateapplet-i18n
Summary:	Internationalization and localization files for kbstateapplet
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbstateapplet
Group:		X11/Applications
Requires:	kdeaccessibility-kbstateapplet = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kbstateapplet-i18n
Internationalization and localization files for kbstateapplet.

%description -n kdeaccessibility-kbstateapplet-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbstateapplet.

%package -n kdeaccessibility-kmag-i18n
Summary:	Internationalization and localization files for kmag
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmag
Group:		X11/Applications
Requires:	kdeaccessibility-kmag = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmag-i18n
Internationalization and localization files for kmag.

%description -n kdeaccessibility-kmag-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmag.

%package -n kdeaccessibility-kmousetool-i18n
Summary:	Internationalization and localization files for kmousetool
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmousetool
Group:		X11/Applications
Requires:	kdeaccessibility-kmousetool = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmousetool-i18n
Internationalization and localization files for kmousetool.

%description -n kdeaccessibility-kmousetool-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmousetool.

%package -n kdeaccessibility-kmouth-i18n
Summary:	Internationalization and localization files for kmouth
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmouth
Group:		X11/Applications
Requires:	kdeaccessibility-kmouth = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kmouth-i18n
Internationalization and localization files for kmouth.

%description -n kdeaccessibility-kmouth-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmouth.

%package -n kdeaccessibility-ksayit-i18n
Summary:	Internationalization and localization files for ksayit
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksayit
Group:		X11/Applications
Requires:	kdeaccessibility-ksayit = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-ksayit-i18n
Internationalization and localization files for ksayit.

%description -n kdeaccessibility-ksayit-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksayit.

%package -n kdeaccessibility-kttsd-i18n
Summary:	Internationalization and localization files for kttsd
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kttsd
Group:		X11/Applications
Requires:	kdeaccessibility-kttsd = %{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaccessibility-kttsd-i18n
Internationalization and localization files for kttsd.

%description -n kdeaccessibility-kttsd-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kttsd.

%package -n kdeaddons-ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ark
Group:		X11/Applications
Requires:	kdeaddons-ark = %{kdeaddons_epoch}:%{version}
Requires:	kdeutils-ark-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-ark-i18n
Internationalization and localization files for ark.

%description -n kdeaddons-ark-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ark.

%package -n kdeaddons-atlantikdesigner-i18n
Summary:	Internationalization and localization files for atlantikdesigner
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla atlantikdesigner
Group:		X11/Applications
Requires:	kdeaddons-atlantikdesigner = %{kdeaddons_epoch}:%{version}
Requires:	kdegames-atlantik-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-atlantikdesigner-i18n
Internationalization and localization files for atlantikdesigner.

%description -n kdeaddons-atlantikdesigner-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla atlantikdesigner.

%package -n kdeaddons-fsview-i18n
Summary:	Internationalization and localization files for fsview
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla fsview
Group:		X11/Applications
Requires:	kdeaddons-fsview = %{kdeaddons_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-fsview-i18n
Internationalization and localization files for fsview.

%description -n kdeaddons-fsview-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla fsview.

%package -n kdeaddons-kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kaddressbook
Group:		X11/Applications
Requires:	kdeaddons-kaddressbook-plugins = %{kdeaddons_epoch}:%{version}
Requires:	kdepim-kaddressbook-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description -n kdeaddons-kaddressbook-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kaddressbook.

%package -n kdeaddons-kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kate
Group:		X11/Applications
Requires:	kdeaddons-kate = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-kate-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kate-i18n
Internationalization and localization files for kate.

%description -n kdeaddons-kate-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kate.

%package -n kdeaddons-kicker-i18n
Summary:	Internationalization and localization files for kicker
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kickera
Group:		X11/Applications
Requires:	kdeaddons-kicker = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-kicker-i18n
Internationalization and localization files for kicker.

%description -n kdeaddons-kicker-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kickera.

%package -n kdeaddons-konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla konquerora
Group:		X11/Applications
Requires:	kdeaddons-konqueror = %{kdeaddons_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-konqueror-i18n
Internationalization and localization files for konqueror.

%description -n kdeaddons-konqueror-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla konquerora.

%package -n kdeaddons-ksig-i18n
Summary:	Internationalization and localization files for ksig
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksig
Group:		X11/Applications
Requires:	kdeaddons-ksig = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-ksig-i18n
Internationalization and localization files for ksig.

%description -n kdeaddons-ksig-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksig.

%package -n kdeaddons-lnkforward-i18n
Summary:	Internationalization and localization files for lnkforward
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla lnkforward
Group:		X11/Applications
Requires:	kdeaddons-lnkforward = %{kdeaddons_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-lnkforward-i18n
Internationalization and localization files for lnkforward.

%description -n kdeaddons-lnkforward-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla lnkforward.

%package -n kdeaddons-noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla noatun
Group:		X11/Applications
Requires:	kdeaddons-noatun = %{kdeaddons_epoch}:%{version}
Requires:	kdemultimedia-noatun-i18n = %{epoch}:%{version}-%{release}

%description -n kdeaddons-noatun-i18n
Internationalization and localization files for noatun.

%description -n kdeaddons-noatun-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla noatun.

%package -n kdeadmin-kcmlilo-i18n
Summary:	Internationalization and localization files for kcmlilo
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcmlilo
Group:		X11/Applications
Requires:	kdeadmin-kcmlilo = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdeadmin-kcmlinuz-i18n

%description -n kdeadmin-kcmlilo-i18n
Internationalization and localization files for kcmlilo.

%description -n kdeadmin-kcmlilo-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcmlilo.

%package -n kdeadmin-kcron-i18n
Summary:	Internationalization and localization files for kcron
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcrona
Group:		X11/Applications
Requires:	kdeadmin-kcron = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kcron-i18n
Internationalization and localization files for kcron.

%description -n kdeadmin-kcron-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcrona.

%package -n kdeadmin-kdat-i18n
Summary:	Internationalization and localization files for kdat
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdat
Group:		X11/Applications
Requires:	kdeadmin-kdat = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kdat-i18n
Internationalization and localization files for kdat.

%description -n kdeadmin-kdat-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdat.

%package -n kdeadmin-knetworkconf-i18n
Summary:	Internationalization and localization files for knetworkconf
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla knetworkconf
Group:		X11/Applications
Requires:	kdeadmin-knetworkconf = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-knetworkconf-i18n
Internationalization and localization files for knetworkconf.

%description -n kdeadmin-knetworkconf-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla knetworkconf.

%package -n kdeadmin-kpackage-i18n
Summary:	Internationalization and localization files for kpackage
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpackage
Group:		X11/Applications
Requires:	kdeadmin-kpackage = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kpackage-i18n
Internationalization and localization files for kpackage.

%description -n kdeadmin-kpackage-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpackage.

%package -n kdeadmin-ksysv-i18n
Summary:	Internationalization and localization files for ksysv
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksysv
Group:		X11/Applications
Requires:	kdeadmin-ksysv = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-ksysv-i18n
Internationalization and localization files for ksysv.

%description -n kdeadmin-ksysv-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksysv.

%package -n kdeadmin-kuser-i18n
Summary:	Internationalization and localization files for kuser
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kusera
Group:		X11/Applications
Requires:	kdeadmin-kuser = %{kdeadmin_epoch}:%{version}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}

%description -n kdeadmin-kuser-i18n
Internationalization and localization files for kuser.

%description -n kdeadmin-kuser-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kusera.

%package -n kdeartwork-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla screensavers
Group:		X11/Applications
Requires:	kdeartwork-screensavers = %{kdeartwork_epoch}:%{version}
Requires:	kdebase-screensavers-i18n = %{epoch}:%{version}-%{release}

%description -n kdeartwork-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdeartwork-screensavers-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla screensavers.

%package -n kdebase-core-i18n
Summary:	Internationalization and localization files for the core part of KDE
Summary(pl.UTF-8):	Tłumaczenia dla podstawowej części KDE
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

%description -n kdebase-core-i18n -l pl.UTF-8
Tłumaczenia dla podstawowej części KDE, obejmującej m.in.:
- Centrum sterownika
- Centrum pomocy
- System wydruków
- Obsługę błędów
- frontend dla programu "su".

%package -n kdebase-desktop-i18n
Summary:	Internationalization and localization files for the desktop part of KDE
Summary(pl.UTF-8):	Tłumaczenia dla desktopowej części KDE
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

%description -n kdebase-desktop-i18n -l pl.UTF-8
Tłumaczenia dla desktopowej części KDE, obejmującej:
- pulpit
- panel
- system splashscreenów
- zarządcę okien.

%package -n kdebase-desktop-libs-i18n
Summary:	Internationalization and localization files for desktop-libs
Summary(pl.UTF-8):	Tłumaczenia dla desktop-libs
Group:		X11/Applications
Requires:	kdebase-desktop-libs = %{kdebase_epoch}:%{version}
Obsoletes:	kdebase-kicker-libs-i18n

%description -n kdebase-desktop-libs-i18n
Internationalization and localization files for desktop-libs.

%description -n kdebase-desktop-libs-i18n -l pl.UTF-8
Tłumaczenia dla desktop-libs.

%package -n kdebase-infocenter-i18n
Summary:	Internationalization and localization files for KDE Information Centre
Summary(pl.UTF-8):	Tłumaczenia dla centrum informacji o systemie w KDE
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-infocenter = %{kdebase_epoch}:%{version}

%description -n kdebase-infocenter-i18n
Internationalization and localization files for KDE Information
Centre.

%description -n kdebase-infocenter-i18n -l pl.UTF-8
Tłumaczenia dla centrum informacji o systemie w KDE.

%package -n kdebase-kappfinder-i18n
Summary:	Internationalization and localization files for kappfinder
Summary(pl.UTF-8):	Tłumaczenia dla kappfindera
Group:		X11/Applications
Requires:	kdebase-kappfinder = %{kdebase_epoch}:%{version}

%description -n kdebase-kappfinder-i18n
Internationalization and localization files for kappfinder.

%description -n kdebase-kappfinder-i18n -l pl.UTF-8
Tłumaczenia dla kappfindera.

%package -n kdebase-kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl.UTF-8):	Tłumaczenia dla kate
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kate = %{kdebase_epoch}:%{version}

%description -n kdebase-kate-i18n
Internationalization and localization files for kate.

%description -n kdebase-kate-i18n -l pl.UTF-8
Tłumaczenia dla kate.

%package -n kdebase-kdcop-i18n
Summary:	Internationalization and localization files for kdcop
Summary(pl.UTF-8):	Tłumaczenia dla kdcopa
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kdcop = %{kdebase_epoch}:%{version}

%description -n kdebase-kdcop-i18n
Internationalization and localization files for kdcop.

%description -n kdebase-kdcop-i18n -l pl.UTF-8
Tłumaczenia dla kdcopa.

%package -n kdebase-kdeprintfax-i18n
Summary:	Internationalization and localization files for kdeprintfax
Summary(pl.UTF-8):	Tłumaczenia dla kdeprintfax
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kdeprintfax = %{kdebase_epoch}:%{version}

%description -n kdebase-kdeprintfax-i18n
Internationalization and localization files for kdeprintfax.

%description -n kdebase-kdeprintfax-i18n -l pl.UTF-8
Tłumaczenia dla kdeprintfax.

%package -n kdebase-kdialog-i18n
Summary:	Internationalization and localization files for kdialog
Summary(pl.UTF-8):	Tłumaczenia dla kdialoga
Group:		X11/Applications
Requires:	kdebase-kdialog = %{kdebase_epoch}:%{version}

%description -n kdebase-kdialog-i18n
Internationalization and localization files for kdialog.

%description -n kdebase-kdialog-i18n -l pl.UTF-8
Tłumaczenia dla kdialoga.

%package -n kdebase-kfind-i18n
Summary:	Internationalization and localization files for kfind
Summary(pl.UTF-8):	Tłumaczenia dla kfind
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kfind = %{kdebase_epoch}:%{version}

%description -n kdebase-kfind-i18n
Internationalization and localization files for kfind.

%description -n kdebase-kfind-i18n -l pl.UTF-8
Tłumaczenia dla kfind.

%package -n kdebase-kfontinst-i18n
Summary:	Internationalization and localization files for kfontinst
Summary(pl.UTF-8):	Tłumaczenia dla kfontinst
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kfontinst = %{kdebase_epoch}:%{version}

%description -n kdebase-kfontinst-i18n
Internationalization and localization files for kfontinst.

%description -n kdebase-kfontinst-i18n -l pl.UTF-8
Tłumaczenia dla kfontinst.

%package -n kdebase-kjobviewer-i18n
Summary:	Internationalization and localization files for kjobviewer
Summary(pl.UTF-8):	Tłumaczenia dla kjobviewera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kjobviewer = %{kdebase_epoch}:%{version}

%description -n kdebase-kjobviewer-i18n
Internationalization and localization files for kjobviewer.

%description -n kdebase-kjobviewer-i18n -l pl.UTF-8
Tłumaczenia dla kjobviewera.

%package -n kdebase-klipper-i18n
Summary:	Internationalization and localization files for klipper
Summary(pl.UTF-8):	Tłumaczenia dla klippera
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-klipper = %{kdebase_epoch}:%{version}

%description -n kdebase-klipper-i18n
Internationalization and localization files for klipper.

%description -n kdebase-klipper-i18n -l pl.UTF-8
Tłumaczenia dla klippera.

%package -n kdebase-konsole-i18n
Summary:	Internationalization and localization files for konsole
Summary(pl.UTF-8):	Tłumaczenia dla konsole
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-konsole = %{kdebase_epoch}:%{version}

%description -n kdebase-konsole-i18n
Internationalization and localization files for konsole.

%description -n kdebase-konsole-i18n -l pl.UTF-8
Tłumaczenia dla konsole.

%package -n kdebase-kpager-i18n
Summary:	Internationalization and localization files for kpager
Summary(pl.UTF-8):	Tłumaczenia dla kpagera
Group:		X11/Applications
Requires:	kdebase-kpager = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}

%description -n kdebase-kpager-i18n
Internationalization and localization files for kpager.

%description -n kdebase-kpager-i18n -l pl.UTF-8
Tłumaczenia dla kpagera.

%package -n kdebase-kpersonalizer-i18n
Summary:	Internationalization and localization files for kpersonalizer
Summary(pl.UTF-8):	Tłumaczenia dla kpersonalizera
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kpersonalizer = %{kdebase_epoch}:%{version}

%description -n kdebase-kpersonalizer-i18n
Internationalization and localization files for kpersonalizer.

%description -n kdebase-kpersonalizer-i18n -l pl.UTF-8
Tłumaczenia dla kpersonalizera.

%package -n kdebase-ksysguard-i18n
Summary:	Internationalization and localization files for ksysguard
Summary(pl.UTF-8):	Tłumaczenia dla ksysguarda
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-klipper-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-ksysguard = %{kdebase_epoch}:%{version}

%description -n kdebase-ksysguard-i18n
Internationalization and localization files for ksysguard.

%description -n kdebase-ksysguard-i18n -l pl.UTF-8
Tłumaczenia dla ksysguarda.

%package -n kdebase-kwrite-i18n
Summary:	Internationalization and localization files for kwrite
Summary(pl.UTF-8):	Tłumaczenia dla kwrite
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kwrite = %{kdebase_epoch}:%{version}

%description -n kdebase-kwrite-i18n
Internationalization and localization files for kwrite.

%description -n kdebase-kwrite-i18n -l pl.UTF-8
Tłumaczenia dla kwrite.

%package -n kdebase-screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl.UTF-8):	Tłumaczenia dla screensavers
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-screensavers = %{kdebase_epoch}:%{version}

%description -n kdebase-screensavers-i18n
Internationalization and localization files for screensavers.

%description -n kdebase-screensavers-i18n -l pl.UTF-8
Tłumaczenia dla screensavers.

%package -n kdebase-useraccount-i18n
Summary:	Internationalization and localization files for useraccount
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla useraccount
Group:		X11/Applications
Requires:	kdebase-useraccount = %{kdebase_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdeutils-kdepasswd-i18n
Obsoletes:	kdeutils-userinfo-i18n

%description -n kdebase-useraccount-i18n
Internationalization and localization files for useraccount.

%description -n kdebase-useraccount-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla useraccount.

%package -n kdeedu-blinken-i18n
Summary:	Internationalization and localization files for blinken
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla blinken
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-blinken = %{kdeedu_epoch}:%{version}

%description -n kdeedu-blinken-i18n
Internationalization and localization files for blinken.

%description -n kdeedu-blinken-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla blinken.

%package -n kdeedu-kalzium-i18n
Summary:	Internationalization and localization files for kalzium
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kalzium
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kalzium = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kalzium-i18n
Internationalization and localization files for kalzium.

%description -n kdeedu-kalzium-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kalzium.

%package -n kdeedu-kanagram-i18n
Summary:	Internationalization and localization files for kanagram
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kanagram
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kanagram = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kanagram-i18n
Internationalization and localization files for kanagram.

%description -n kdeedu-kanagram-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kanagram.

%package -n kdeedu-kbruch-i18n
Summary:	Internationalization and localization files for kbruch
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbrucha
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kbruch = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kbruch-i18n
Internationalization and localization files for kbruch.

%description -n kdeedu-kbruch-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbrucha.

%package -n kdeedu-keduca-i18n
Summary:	Internationalization and localization files for keduca
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla keduca
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-keduca = %{kdeedu_epoch}:%{version}

%description -n kdeedu-keduca-i18n
Internationalization and localization files for keduca.

%description -n kdeedu-keduca-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla keduca.

%package -n kdeedu-kgeography-i18n
Summary:	Internationalization and localization files for kgeography
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kgeography
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kgeography = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kgeography-i18n
Internationalization and localization files for kgeography.

%description -n kdeedu-kgeography-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kgeography.

%package -n kdeedu-khangman-i18n
Summary:	Internationalization and localization files for khangman
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla khangmana
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-khangman = %{kdeedu_epoch}:%{version}

%description -n kdeedu-khangman-i18n
Internationalization and localization files for khangman.

%description -n kdeedu-khangman-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla khangmana.

%package -n kdeedu-kig-i18n
Summary:	Internationalization and localization files for kig
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kig
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kig = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kig-i18n
Internationalization and localization files for kig.

%description -n kdeedu-kig-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kig.

%package -n kdeedu-kiten-i18n
Summary:	Internationalization and localization files for kiten
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kiten
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kiten = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kiten-i18n
Internationalization and localization files for kiten.

%description -n kdeedu-kiten-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kiten.

%package -n kdeedu-klatin-i18n
Summary:	Internationalization and localization files for klatin
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla klatin
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-klatin = %{kdeedu_epoch}:%{version}

%description -n kdeedu-klatin-i18n
Internationalization and localization files for klatin.

%description -n kdeedu-klatin-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla klatin.

%package -n kdeedu-klettres-i18n
Summary:	Internationalization and localization files for klettres
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla klettres
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-klettres = %{kdeedu_epoch}:%{version}

%description -n kdeedu-klettres-i18n
Internationalization and localization files for klettres.

%description -n kdeedu-klettres-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla klettres.

%package -n kdeedu-kmplot-i18n
Summary:	Internationalization and localization files for kmplot
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmplot
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kmplot = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kmplot-i18n
Internationalization and localization files for kmplot.

%description -n kdeedu-kmplot-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmplot.

%package -n kdeedu-kpercentage-i18n
Summary:	Internationalization and localization files for kpercentage
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpercentage
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kpercentage = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kpercentage-i18n
Internationalization and localization files for kpercentage.

%description -n kdeedu-kpercentage-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpercentage.

%package -n kdeedu-kstars-i18n
Summary:	Internationalization and localization files for kstars
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kstars
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kstars = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kstars-i18n
Internationalization and localization files for kstars.

%description -n kdeedu-kstars-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kstars.

%package -n kdeedu-ktouch-i18n
Summary:	Internationalization and localization files for ktouch
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ktouch
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-ktouch = %{kdeedu_epoch}:%{version}

%description -n kdeedu-ktouch-i18n
Internationalization and localization files for ktouch.

%description -n kdeedu-ktouch-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ktouch.

%package -n kdeedu-kturtle-i18n
Summary:	Internationalization and localization files for kturtle
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kturtle
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kturtle = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kturtle-i18n
Internationalization and localization files for kturtle.

%description -n kdeedu-kturtle-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kturtle.

%package -n kdeedu-kverbos-i18n
Summary:	Internationalization and localization files for kverbos
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kverbos
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kverbos = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kverbos-i18n
Internationalization and localization files for kverbos.

%description -n kdeedu-kverbos-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kverbos.

%package -n kdeedu-kvoctrain-i18n
Summary:	Internationalization and localization files for kvoctrain
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kvoctrain
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kvoctrain = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kvoctrain-i18n
Internationalization and localization files for kvoctrain.

%description -n kdeedu-kvoctrain-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kvoctrain.

%package -n kdeedu-kwordquiz-i18n
Summary:	Internationalization and localization files for kwordquiz
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kwordquiz
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-kwordquiz = %{kdeedu_epoch}:%{version}

%description -n kdeedu-kwordquiz-i18n
Internationalization and localization files for kwordquiz.

%description -n kdeedu-kwordquiz-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kwordquiz.

%package -n kdeedu-libkdeeduui-i18n
Summary:	Internationalization and localization files for libkdeeduui
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla libkdeeduui
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeedu-libkdeeduui = %{kdeedu_epoch}:%{version}

%description -n kdeedu-libkdeeduui-i18n
Internationalization and localization files for libkdeeduui.

%description -n kdeedu-libkdeeduui-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla libkdeeduui.

%package -n kdegames-atlantik-i18n
Summary:	Internationalization and localization files for atlantik
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla atlantika
Group:		X11/Applications
Requires:	kdegames-atlantik = %{kdegames_epoch}:%{version}
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}

%description -n kdegames-atlantik-i18n
Internationalization and localization files for atlantik.

%description -n kdegames-atlantik-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla atlantika.

%package -n kdegames-i18n
Summary:	Internationalization and localization files for kdegames libs
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla bibliotek kdegames
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames = %{kdegames_epoch}:%{version}
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdegames-megami-i18n

%description -n kdegames-i18n
Internationalization and localization files for kdegames libs.

%description -n kdegames-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla bibliotek kdegames.

%package -n kdegames-kasteroids-i18n
Summary:	Internationalization and localization files for kasteroids
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kasteroids
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kasteroids = %{kdegames_epoch}:%{version}

%description -n kdegames-kasteroids-i18n
Internationalization and localization files for kasteroids.

%description -n kdegames-kasteroids-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kasteroids.

%package -n kdegames-katomic-i18n
Summary:	Internationalization and localization files for katomic
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla katomic
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-katomic = %{kdegames_epoch}:%{version}

%description -n kdegames-katomic-i18n
Internationalization and localization files for katomic.

%description -n kdegames-katomic-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla katomic.

%package -n kdegames-kbackgammon-i18n
Summary:	Internationalization and localization files for kbackgammon
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbackgammona
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kbackgammon = %{kdegames_epoch}:%{version}

%description -n kdegames-kbackgammon-i18n
Internationalization and localization files for kbackgammon.

%description -n kdegames-kbackgammon-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbackgammona.

%package -n kdegames-kbattleship-i18n
Summary:	Internationalization and localization files for kbattleship
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbattleship
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kbattleship = %{kdegames_epoch}:%{version}

%description -n kdegames-kbattleship-i18n
Internationalization and localization files for kbattleship.

%description -n kdegames-kbattleship-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbattleship.

%package -n kdegames-kblackbox-i18n
Summary:	Internationalization and localization files for kblackbox
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kblackboksa
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kblackbox = %{kdegames_epoch}:%{version}

%description -n kdegames-kblackbox-i18n
Internationalization and localization files for kblackbox.

%description -n kdegames-kblackbox-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kblackboksa.

%package -n kdegames-kbounce-i18n
Summary:	Internationalization and localization files for kbounce
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbounce
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kbounce = %{kdegames_epoch}:%{version}

%description -n kdegames-kbounce-i18n
Internationalization and localization files for kbounce.

%description -n kdegames-kbounce-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbounce.

%package -n kdegames-kenolaba-i18n
Summary:	Internationalization and localization files for kenolaba
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kenolaby
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kenolaba = %{kdegames_epoch}:%{version}

%description -n kdegames-kenolaba-i18n
Internationalization and localization files for kenolaba.

%description -n kdegames-kenolaba-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kenolaby.

%package -n kdegames-kfouleggs-i18n
Summary:	Internationalization and localization files for kfouleggs
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfouleggs
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kfouleggs = %{kdegames_epoch}:%{version}

%description -n kdegames-kfouleggs-i18n
Internationalization and localization files for kfouleggs.

%description -n kdegames-kfouleggs-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfouleggs.

%package -n kdegames-kgoldrunner-i18n
Summary:	Internationalization and localization files for kgoldrunner
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kgoldrunnera
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kgoldrunner = %{kdegames_epoch}:%{version}

%description -n kdegames-kgoldrunner-i18n
Internationalization and localization files for kgoldrunner.

%description -n kdegames-kgoldrunner-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kgoldrunnera.

%package -n kdegames-kjumpingcube-i18n
Summary:	Internationalization and localization files for kjumpingcube
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kjumpingcube
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kjumpingcube = %{kdegames_epoch}:%{version}

%description -n kdegames-kjumpingcube-i18n
Internationalization and localization files for kjumpingcube.

%description -n kdegames-kjumpingcube-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kjumpingcube.

%package -n kdegames-klickety-i18n
Summary:	Internationalization and localization files for klickety
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla klickety
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-klickety = %{kdegames_epoch}:%{version}

%description -n kdegames-klickety-i18n
Internationalization and localization files for klickety.

%description -n kdegames-klickety-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla klickety.

%package -n kdegames-klines-i18n
Summary:	Internationalization and localization files for klines
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla klines
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-klines = %{kdegames_epoch}:%{version}

%description -n kdegames-klines-i18n
Internationalization and localization files for klines.

%description -n kdegames-klines-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla klines.

%package -n kdegames-kmahjongg-i18n
Summary:	Internationalization and localization files for kmahjongg
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmahjongga
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kmahjongg = %{kdegames_epoch}:%{version}

%description -n kdegames-kmahjongg-i18n
Internationalization and localization files for kmahjongg.

%description -n kdegames-kmahjongg-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmahjongga.

%package -n kdegames-kmines-i18n
Summary:	Internationalization and localization files for kmines
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmines
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kmines = %{kdegames_epoch}:%{version}

%description -n kdegames-kmines-i18n
Internationalization and localization files for kmines.

%description -n kdegames-kmines-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmines.

%package -n kdegames-knetwalk-i18n
Summary:	Internationalization and localization files for knetwalk
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla knetwalk
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-knetwalk = %{kdegames_epoch}:%{version}

%description -n kdegames-knetwalk-i18n
Internationalization and localization files for knetwalk.

%description -n kdegames-knetwalk-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla knetwalk.

%package -n kdegames-kolf-i18n
Summary:	Internationalization and localization files for kolf
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kolfa
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kolf = %{kdegames_epoch}:%{version}

%description -n kdegames-kolf-i18n
Internationalization and localization files for kolf.

%description -n kdegames-kolf-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kolfa.

%package -n kdegames-konquest-i18n
Summary:	Internationalization and localization files for konquest
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla konquesta
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-konquest = %{kdegames_epoch}:%{version}

%description -n kdegames-konquest-i18n
Internationalization and localization files for konquest.

%description -n kdegames-konquest-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla konquesta.

%package -n kdegames-kpat-i18n
Summary:	Internationalization and localization files for kpat
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpata
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kpat = %{kdegames_epoch}:%{version}

%description -n kdegames-kpat-i18n
Internationalization and localization files for kpat.

%description -n kdegames-kpat-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpata.

%package -n kdegames-kpoker-i18n
Summary:	Internationalization and localization files for kpoker
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpokera
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kpoker = %{kdegames_epoch}:%{version}

%description -n kdegames-kpoker-i18n
Internationalization and localization files for kpoker.

%description -n kdegames-kpoker-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpokera.

%package -n kdegames-kreversi-i18n
Summary:	Internationalization and localization files for kreversi
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kreversi
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kreversi = %{kdegames_epoch}:%{version}

%description -n kdegames-kreversi-i18n
Internationalization and localization files for kreversi.

%description -n kdegames-kreversi-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kreversi.

%package -n kdegames-ksame-i18n
Summary:	Internationalization and localization files for ksame
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksame
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksame = %{kdegames_epoch}:%{version}

%description -n kdegames-ksame-i18n
Internationalization and localization files for ksame.

%description -n kdegames-ksame-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksame.

%package -n kdegames-kshisen-i18n
Summary:	Internationalization and localization files for kshisen
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kshisen
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kshisen = %{kdegames_epoch}:%{version}

%description -n kdegames-kshisen-i18n
Internationalization and localization files for kshisen.

%description -n kdegames-kshisen-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kshisen.

%package -n kdegames-ksirtet-i18n
Summary:	Internationalization and localization files for ksirtet
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksirteta
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksirtet = %{kdegames_epoch}:%{version}

%description -n kdegames-ksirtet-i18n
Internationalization and localization files for ksirtet.

%description -n kdegames-ksirtet-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksirteta.

%package -n kdegames-ksmiletris-i18n
Summary:	Internationalization and localization files for ksmiletris
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksmiletrisa
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksmiletris = %{kdegames_epoch}:%{version}

%description -n kdegames-ksmiletris-i18n
Internationalization and localization files for ksmiletris.

%description -n kdegames-ksmiletris-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksmiletrisa.

%package -n kdegames-ksnake-i18n
Summary:	Internationalization and localization files for ksnake
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksnake'a
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksnake = %{kdegames_epoch}:%{version}

%description -n kdegames-ksnake-i18n
Internationalization and localization files for ksnake.

%description -n kdegames-ksnake-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksnake'a.

%package -n kdegames-ksokoban-i18n
Summary:	Internationalization and localization files for ksokoban
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksokobana
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ksokoban = %{kdegames_epoch}:%{version}

%description -n kdegames-ksokoban-i18n
Internationalization and localization files for ksokoban.

%description -n kdegames-ksokoban-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksokobana.

%package -n kdegames-kspaceduel-i18n
Summary:	Internationalization and localization files for kspaceduel
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kspaceduel
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kspaceduel = %{kdegames_epoch}:%{version}

%description -n kdegames-kspaceduel-i18n
Internationalization and localization files for kspaceduel.

%description -n kdegames-kspaceduel-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kspaceduel.

%package -n kdegames-ktron-i18n
Summary:	Internationalization and localization files for ktron
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ktrona
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ktron = %{kdegames_epoch}:%{version}

%description -n kdegames-ktron-i18n
Internationalization and localization files for ktron.

%description -n kdegames-ktron-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ktrona.

%package -n kdegames-ktuberling-i18n
Summary:	Internationalization and localization files for ktuberling
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ktuberlinga
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-ktuberling = %{kdegames_epoch}:%{version}

%description -n kdegames-ktuberling-i18n
Internationalization and localization files for ktuberling.

%description -n kdegames-ktuberling-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ktuberlinga.

%package -n kdegames-kwin4-i18n
Summary:	Internationalization and localization files for kwin4
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kwin4
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-kwin4 = %{kdegames_epoch}:%{version}

%description -n kdegames-kwin4-i18n
Internationalization and localization files for kwin4.

%description -n kdegames-kwin4-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kwin4.

%package -n kdegames-lskat-i18n
Summary:	Internationalization and localization files for lskat
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla lskata
Group:		X11/Applications
Requires:	kdegames-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-lskat = %{kdegames_epoch}:%{version}

%description -n kdegames-lskat-i18n
Internationalization and localization files for lskat.

%description -n kdegames-lskat-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla lskata.

%package -n kdegraphics-kamera-i18n
Summary:	Internationalization and localization files for kamera
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla programu kamera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kamera = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kamera-i18n
Internationalization and localization files for kamera.

%description -n kdegraphics-kamera-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla programu kamera.

%package -n kdegraphics-kcoloredit-i18n
Summary:	Internationalization and localization files for kcoloredit
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcoloredita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kcoloredit = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kcoloredit-i18n
Internationalization and localization files for kcoloredit.

%description -n kdegraphics-kcoloredit-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcoloredita.

%package -n kdegraphics-kdvi-i18n
Summary:	Internationalization and localization files for kdvi
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdvi
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kdvi = %{kdegraphics_epoch}:%{version}
Requires:	kdegraphics-kview-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kdvi-i18n
Internationalization and localization files for kdvi.

%description -n kdegraphics-kdvi-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdvi.

%package -n kdegraphics-kfax-i18n
Summary:	Internationalization and localization files for kfax
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfaksa
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kfax = %{kdegraphics_epoch}:%{version}
Requires:	kdegraphics-kview-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kfax-i18n
Internationalization and localization files for kfax.

%description -n kdegraphics-kfax-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfaksa.

%package -n kdegraphics-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfile'a
Group:		X11/Applications
Requires:	kdegraphics-kfile = %{kdegraphics_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdegraphics-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdegraphics-kfile-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfile'a.

%package -n kdegraphics-kgamma-i18n
Summary:	Internationalization and localization files for kgamma
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kgamma
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kgamma = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kgamma-i18n
Internationalization and localization files for kgamma.

%description -n kdegraphics-kgamma-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kgamma.

%package -n kdegraphics-kghostview-i18n
Summary:	Internationalization and localization files for kghostview
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kghostview
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kghostview = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kghostview-i18n
Internationalization and localization files for kghostview.

%description -n kdegraphics-kghostview-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kghostview.

%package -n kdegraphics-kiconedit-i18n
Summary:	Internationalization and localization files for kiconedit
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kiconedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kiconedit = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kiconedit-i18n
Internationalization and localization files for kiconedit.

%description -n kdegraphics-kiconedit-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kiconedita.

%package -n kdegraphics-kmrml-i18n
Summary:	Internationalization and localization files for kmrml
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmrml
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kmrml = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kmrml-i18n
Internationalization and localization files for kmrml.

%description -n kdegraphics-kmrml-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmrml.

%package -n kdegraphics-kolourpaint-i18n
Summary:	Internationalization and localization files for kolourpaint
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kolourpaint
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kolourpaint = %{kdegraphics_epoch}:%{version}
Obsoletes:	kdegraphics-kpaint-i18n

%description -n kdegraphics-kolourpaint-i18n
Internationalization and localization files for kolourpaint.

%description -n kdegraphics-kolourpaint-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kolourpaint.

%package -n kdegraphics-kooka-i18n
Summary:	Internationalization and localization files for kooka
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kooki
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kooka = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kooka-i18n
Internationalization and localization files for kooka.

%description -n kdegraphics-kooka-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kooki.

%package -n kdegraphics-kpdf-i18n
Summary:	Internationalization and localization files for kpdf
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpdf
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kpdf = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kpdf-i18n
Internationalization and localization files for kpdf.

%description -n kdegraphics-kpdf-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpdf.

%package -n kdegraphics-kpovmodeler-i18n
Summary:	Internationalization and localization files for kpovmodeler
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpovmodelera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kpovmodeler = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kpovmodeler-i18n
Internationalization and localization files for kpovmodeler.

%description -n kdegraphics-kpovmodeler-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpovmodelera.

%package -n kdegraphics-kruler-i18n
Summary:	Internationalization and localization files for kruler
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla krulera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kruler = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kruler-i18n
Internationalization and localization files for kruler.

%description -n kdegraphics-kruler-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla krulera.

%package -n kdegraphics-ksnapshot-i18n
Summary:	Internationalization and localization files for ksnapshot
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksnapshota
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-ksnapshot = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-ksnapshot-i18n
Internationalization and localization files for ksnapshot.

%description -n kdegraphics-ksnapshot-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksnapshota.

%package -n kdegraphics-ksvg-i18n
Summary:	Internationalization and localization files for ksvg
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksvg
Group:		X11/Applications
Requires:	kdegraphics-ksvg = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-ksvg-i18n
Internationalization and localization files for ksvg.

%description -n kdegraphics-ksvg-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksvg.

%package -n kdegraphics-kuickshow-i18n
Summary:	Internationalization and localization files for kuickshow
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kuickshow
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kuickshow = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kuickshow-i18n
Internationalization and localization files for kuickshow.

%description -n kdegraphics-kuickshow-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kuickshow.

%package -n kdegraphics-kview-i18n
Summary:	Internationalization and localization files for kview
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kview
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kview = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kview-i18n
Internationalization and localization files for kview.

%description -n kdegraphics-kview-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kview.

%package -n kdegraphics-kviewshell-i18n
Summary:	Internationalization and localization files for kviewshell
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kviewshell
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegraphics-kviewshell = %{kdegraphics_epoch}:%{version}

%description -n kdegraphics-kviewshell-i18n
Internationalization and localization files for kviewshell.

%description -n kdegraphics-kviewshell-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kviewshell.

%package -n kdelibs-i18n
Summary:	Internationalization and localization files for kdelibs
Summary(pl.UTF-8):	Pliki umiędzynarodawiające kdelibs
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

%description -n kdelibs-i18n -l pl.UTF-8
Tłumaczenia i dane międzynarodowe dla bibliotek KDE.

%package -n kdemultimedia-arts-i18n
Summary:	Internationalization and localization files for arts
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla arts
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-arts = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-arts-i18n
Internationalization and localization files for arts.

%description -n kdemultimedia-arts-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla arts.

%package -n kdemultimedia-artsbuilder-i18n
Summary:	Internationalization and localization files for artsbuilder
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla artsbuildera
Group:		X11/Applications
Requires:	kdemultimedia-arts-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-artsbuilder = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-artsbuilder-i18n
Internationalization and localization files for artsbuilder.

%description -n kdemultimedia-artsbuilder-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla artsbuildera.

%package -n kdemultimedia-artscontrol-i18n
Summary:	Internationalization and localization files for artscontrol
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla artscontrol
Group:		X11/Applications
Requires:	kdemultimedia-arts-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-artscontrol = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-artscontrol-i18n
Internationalization and localization files for artscontrol.

%description -n kdemultimedia-artscontrol-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla artscontrol.

%package -n kdemultimedia-audiocd-i18n
Summary:	Internationalization and localization files for audiocd
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla audiocd
Group:		X11/Applications
Requires:	kdemultimedia-audiocd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-audiocd-i18n
Internationalization and localization files for audiocd.

%description -n kdemultimedia-audiocd-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla audiocd.

%package -n kdemultimedia-juk-i18n
Summary:	Internationalization and localization files for juk
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla juk
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-juk = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-juk-i18n
Internationalization and localization files for juk.

%description -n kdemultimedia-juk-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla juk.

%package -n kdemultimedia-kaboodle-i18n
Summary:	Internationalization and localization files for kaboodle
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kaboodle
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kaboodle = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kaboodle-i18n
Internationalization and localization files for kaboodle.

%description -n kdemultimedia-kaboodle-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kaboodle.

%package -n kdemultimedia-kaudiocreator-i18n
Summary:	Internationalization and localization files for kaudiocreator
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kaudiocreatora
Group:		X11/Applications
Requires:	kdemultimedia-kaudiocreator = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kaudiocreator-i18n
Internationalization and localization files for kaudiocreator.

%description -n kdemultimedia-kaudiocreator-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kaudiocreatora.

%package -n kdemultimedia-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfile
Group:		X11/Applications
Requires:	kdemultimedia-kfile = %{kdemultimedia_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdemultimedia-kfile-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfile.

%package -n kdemultimedia-kmid-i18n
Summary:	Internationalization and localization files for kmid
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmid
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmid = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kmid-i18n
Internationalization and localization files for kmid.

%description -n kdemultimedia-kmid-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmid.

%package -n kdemultimedia-kmix-i18n
Summary:	Internationalization and localization files for kmix
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmix
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmix = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-kmix-i18n
Internationalization and localization files for kmix.

%description -n kdemultimedia-kmix-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmix.

%package -n kdemultimedia-krec-i18n
Summary:	Internationalization and localization files for krec
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla krec
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-artscontrol-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kmix-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-krec = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-krec-i18n
Internationalization and localization files for krec.

%description -n kdemultimedia-krec-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla krec.

%package -n kdemultimedia-kscd-i18n
Summary:	Internationalization and localization files for kscd
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kscd
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-kscd = %{kdemultimedia_epoch}:%{version}
Requires:	kdemultimedia-libkcddb-i18n = %{epoch}:%{version}-%{release}

%description -n kdemultimedia-kscd-i18n
Internationalization and localization files for kscd.

%description -n kdemultimedia-kscd-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kscd.

%package -n kdemultimedia-libkcddb-i18n
Summary:	Internationalization and localization files for libkcddb
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla libkcddb
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-libkcddb = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-libkcddb-i18n
Internationalization and localization files for libkcddb.

%description -n kdemultimedia-libkcddb-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla libkcddb.

%package -n kdemultimedia-noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla noatun
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-noatun = %{kdemultimedia_epoch}:%{version}

%description -n kdemultimedia-noatun-i18n
Internationalization and localization files for noatun.

%description -n kdemultimedia-noatun-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla noatun.

%package -n kdenetwork-filesharing-i18n
Summary:	Internationalization and localization files for fileshare
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla fileshare
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-filesharing = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-filesharing-i18n
Internationalization and localization files for fileshare.

%description -n kdenetwork-filesharing-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla fileshare.

%package -n kdenetwork-kdict-i18n
Summary:	Internationalization and localization files for kdict
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdict
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kdict = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kdict-i18n
Internationalization and localization files for kdict.

%description -n kdenetwork-kdict-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdict.

%package -n kdenetwork-kdnssd-i18n
Summary:	Internationalization and localization files for kdnssd
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdnssd
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kdnssd = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kdnssd-i18n
Internationalization and localization files for kdnssd.

%description -n kdenetwork-kdnssd-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdnssd.

%package -n kdenetwork-kfile-torrent-i18n
Summary:	Internationalization and localization files for kfile_torrent
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfile_torrent
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kfile-torrent = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kfile-torrent-i18n
Internationalization and localization files for kfile_torrent.

%description -n kdenetwork-kfile-torrent-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfile_torrent.

%package -n kdenetwork-kget-i18n
Summary:	Internationalization and localization files for kget
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kgeta
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kget = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kget-i18n
Internationalization and localization files for kget.

%description -n kdenetwork-kget-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kgeta.

%package -n kdenetwork-kinetd-i18n
Summary:	Internationalization and localization files for kinetd
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kinetd
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kinetd = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kinetd-i18n
Internationalization and localization files for kinetd.

%description -n kdenetwork-kinetd-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kinetd.

%package -n kdenetwork-knewsticker-i18n
Summary:	Internationalization and localization files for knewsticker
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla knewstickera
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-knewsticker = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-knewsticker-i18n
Internationalization and localization files for knewsticker.

%description -n kdenetwork-knewsticker-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla knewstickera.

%package -n kdenetwork-kopete-i18n
Summary:	Internationalization and localization files for kopete
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kopete
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kopete = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kopete-i18n
Internationalization and localization files for kopete.

%description -n kdenetwork-kopete-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kopete.

%package -n kdenetwork-kpf-i18n
Summary:	Internationalization and localization files for kpf
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpf
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kpf = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kpf-i18n
Internationalization and localization files for kpf.

%description -n kdenetwork-kpf-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpf.

%package -n kdenetwork-kppp-i18n
Summary:	Internationalization and localization files for kppp
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kppp
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kppp = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kppp-i18n
Internationalization and localization files for kppp.

%description -n kdenetwork-kppp-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kppp.

%package -n kdenetwork-krfb-i18n
Summary:	Internationalization and localization files for krfb
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla krfb
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kinetd-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-krfb = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-krfb-i18n
Internationalization and localization files for krfb.

%description -n kdenetwork-krfb-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla krfb.

%package -n kdenetwork-ksirc-i18n
Summary:	Internationalization and localization files for ksirc
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksirc
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-ksirc = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-ksirc-i18n
Internationalization and localization files for ksirc.

%description -n kdenetwork-ksirc-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksirc.

%package -n kdenetwork-ktalkd-i18n
Summary:	Internationalization and localization files for ktalkd
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ktalkd
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-ktalkd = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-ktalkd-i18n
Internationalization and localization files for ktalkd.

%description -n kdenetwork-ktalkd-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ktalkd.

%package -n kdenetwork-kwifimanager-i18n
Summary:	Internationalization and localization files for kwifimanager
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kwifimanagera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdenetwork-kwifimanager = %{kdenetwork_epoch}:%{version}

%description -n kdenetwork-kwifimanager-i18n
Internationalization and localization files for kwifimanager.

%description -n kdenetwork-kwifimanager-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kwifimanagera.

%package -n kdenetwork-lanbrowser-i18n
Summary:	Internationalization and localization files for lanbrowser
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla lanbrowsera
Group:		X11/Applications
Requires:	kdenetwork-lanbrowser = %{kdenetwork_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdenetwork-lanbrowser-i18n
Internationalization and localization files for lanbrowser.

%description -n kdenetwork-lanbrowser-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla lanbrowsera.

%package -n kdepim-i18n
Summary:	Internationalization and localization files for kdepim
Summary(pl.UTF-8):	Tłumaczenia dla kdepim
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

%description -n kdepim-i18n -l pl.UTF-8
Tłumaczenia dla kdepim.

%package -n kdepim-kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl.UTF-8):	Tłumaczenia dla kaddressbook
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kaddressbook = %{kdepim_epoch}:%{version}

%description -n kdepim-kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description -n kdepim-kaddressbook-i18n -l pl.UTF-8
Tłumaczenia dla kaddressbook.

%package -n kdepim-kandy-i18n
Summary:	Internationalization and localization files for kandy
Summary(pl.UTF-8):	Tłumaczenia dla kandy
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kandy = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-kandy-i18n
Internationalization and localization files for kandy.

%description -n kdepim-kandy-i18n -l pl.UTF-8
Tłumaczenia dla kandy.

%package -n kdepim-karm-i18n
Summary:	Internationalization and localization files for karm
Summary(pl.UTF-8):	Tłumaczenia dla karm
Group:		X11/Applications
Requires:	kdepim-karm = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-karm-i18n
Internationalization and localization files for karm.

%description -n kdepim-karm-i18n -l pl.UTF-8
Tłumaczenia dla karm.

%package -n kdepim-kmail-i18n
Summary:	Internationalization and localization files for kmail
Summary(pl.UTF-8):	Tłumaczenia dla kmaila
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

%description -n kdepim-kmail-i18n -l pl.UTF-8
Tłumaczenia dla kmaila.

%package -n kdepim-knode-i18n
Summary:	Internationalization and localization files for knode
Summary(pl.UTF-8):	Tłumaczenia dla knode
Group:		X11/Applications
Requires:	kde-kio-nntp-i18n = %{epoch}:%{version}-%{release}
Requires:	kde-kio-smtp-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-knode = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-knode-i18n
Internationalization and localization files for knode.

%description -n kdepim-knode-i18n -l pl.UTF-8
Tłumaczenia dla knode.

%package -n kdepim-knotes-i18n
Summary:	Internationalization and localization files for knotes
Summary(pl.UTF-8):	Tłumaczenia dla knotes
Group:		X11/Applications
Requires:	kdepim-knotes = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-knotes-i18n
Internationalization and localization files for knotes.

%description -n kdepim-knotes-i18n -l pl.UTF-8
Tłumaczenia dla knotes.

%package -n kdepim-konsolekalendar-i18n
Summary:	Internationalization and localization files for konsolekalendar
Summary(pl.UTF-8):	Tłumaczenia dla konsolekalendara
Group:		X11/Applications
Requires:	kdepim-konsolekalendar = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-konsolekalendar-i18n
Internationalization and localization files for konsolekalendar.

%description -n kdepim-konsolekalendar-i18n -l pl.UTF-8
Tłumaczenia dla konsolekalendara.

%package -n kdepim-korn-i18n
Summary:	Internationalization and localization files for korn
Summary(pl.UTF-8):	Tłumaczenia dla korna
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-korn = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-korn-i18n
Internationalization and localization files for korn.

%description -n kdepim-korn-i18n -l pl.UTF-8
Tłumaczenia dla korna.

%package -n kdepim-kpilot-i18n
Summary:	Internationalization and localization files for kpilot
Summary(pl.UTF-8):	Tłumaczenia dla kpilota
Group:		X11/Applications
Requires:	kdepim-kpilot = %{kdepim_epoch}:%{version}
Requires:	kdepim-libs-i18n = %{epoch}:%{version}-%{release}

%description -n kdepim-kpilot-i18n
Internationalization and localization files for kpilot.

%description -n kdepim-kpilot-i18n -l pl.UTF-8
Tłumaczenia dla kpilota.

%package -n kdepim-libs-i18n
Summary:	Internationalization and localization files for libkdepim
Summary(pl.UTF-8):	Tłumaczenia dla libkdepim
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

%description -n kdepim-libs-i18n -l pl.UTF-8
Tłumaczenia dla bibliotek kdepim.

%package -n kdesdk-cervisia-i18n
Summary:	Internationalization and localization files for cervisia
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla cervisii
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-cervisia = %{kdesdk_epoch}:%{version}
Requires:	kdesdk-libcvsservice-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-cervisia-i18n
Internationalization and localization files for cervisia.

%description -n kdesdk-cervisia-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla cervisii.

%package -n kdesdk-kapptemplate-i18n
Summary:	Internationalization and localization files for kapptemplate
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kapptemplate
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kapptemplate = %{kdesdk_epoch}:%{version}
Requires:	kdesdk-libcvsservice-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kapptemplate-i18n
Internationalization and localization files for kapptemplate.

%description -n kdesdk-kapptemplate-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kapptemplate.

%package -n kdesdk-kbabel-i18n
Summary:	Internationalization and localization files for kbabel
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbabel
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kbabel = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kbabel-i18n
Internationalization and localization files for kbabel.

%description -n kdesdk-kbabel-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbabel.

%package -n kdesdk-kbugbuster-i18n
Summary:	Internationalization and localization files for kbugbuster
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kbugbustera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kbugbuster = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kbugbuster-i18n
Internationalization and localization files for kbugbuster.

%description -n kdesdk-kbugbuster-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kbugbustera.

%package -n kdesdk-kcachegrind-i18n
Summary:	Internationalization and localization files for kcachegrind
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcachegrinda
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kcachegrind = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kcachegrind-i18n
Internationalization and localization files for kcachegrind.

%description -n kdesdk-kcachegrind-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcachegrinda.

%package -n kdesdk-kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfile
Group:		X11/Applications
Requires:	kdesdk-kfile = %{kdesdk_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdesdk-kfile-i18n
Internationalization and localization files for kfile.

%description -n kdesdk-kfile-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfile.

%package -n kdesdk-kompare-i18n
Summary:	Internationalization and localization files for kompare
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kompare
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kompare = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kompare-i18n
Internationalization and localization files for kompare.

%description -n kdesdk-kompare-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kompare.

%package -n kdesdk-kspy-i18n
Summary:	Internationalization and localization files for kspy
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kspy
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kspy = %{kdesdk_epoch}:%{version}
Obsoletes:	kdesdk-spy-i18n

%description -n kdesdk-kspy-i18n
Internationalization and localization files for spy.

%description -n kdesdk-kspy-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla spy.

%package -n kdesdk-kstartperf-i18n
Summary:	Internationalization and localization files for kstartperf
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kstartperfa
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kstartperf = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kstartperf-i18n
Internationalization and localization files for kstartperf.

%description -n kdesdk-kstartperf-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kstartperfa.

%package -n kdesdk-kuiviewer-i18n
Summary:	Internationalization and localization files for kuiviewer
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kuiviewera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-kuiviewer = %{kdesdk_epoch}:%{version}

%description -n kdesdk-kuiviewer-i18n
Internationalization and localization files for kuiviewer.

%description -n kdesdk-kuiviewer-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kuiviewera.

%package -n kdesdk-libcvsservice-i18n
Summary:	Internationalization and localization files for libcvsservice
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla libcvsservice
Group:		X11/Applications
Requires:	kdesdk-libcvsservice = %{kdesdk_epoch}:%{version}
Conflicts:	kdesdk-cervisia-i18n < %{epoch}:%{version}-%{release}

%description -n kdesdk-libcvsservice-i18n
Internationalization and localization files for libcvsservice.

%description -n kdesdk-libcvsservice-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla libcvsservice.

%package -n kdesdk-scripts-developer-i18n
Summary:	Internationalization and localization files for KDE developer scripts
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla KDE developer scripts
Group:		X11/Applications
Requires:	kdesdk-libcvsservice = %{kdesdk_epoch}:%{version}
Conflicts:	kdesdk-cervisia-i18n < %{epoch}:%{version}-%{release}

%description -n kdesdk-scripts-developer-i18n
Internationalization and localization files for KDE developer scripts.

%description -n kdesdk-scripts-developer-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla KDE developer scripts

%package -n kdesdk-umbrello-i18n
Summary:	Internationalization and localization files for umbrello
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla umbrello
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdesdk-umbrello = %{kdesdk_epoch}:%{version}

%description -n kdesdk-umbrello-i18n
Internationalization and localization files for umbrello.

%description -n kdesdk-umbrello-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla umbrello.

%package -n kdetoys-amor-i18n
Summary:	Internationalization and localization files for amor
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla amora
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-amor = %{kdetoys_epoch}:%{version}

%description -n kdetoys-amor-i18n
Internationalization and localization files for amor.

%description -n kdetoys-amor-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla amora.

%package -n kdetoys-fifteen-i18n
Summary:	Internationalization and localization files for fifteen
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla fifteen
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-fifteen = %{kdetoys_epoch}:%{version}

%description -n kdetoys-fifteen-i18n
Internationalization and localization files for fifteen.

%description -n kdetoys-fifteen-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla fifteen.

%package -n kdetoys-kmoon-i18n
Summary:	Internationalization and localization files for kmoon
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kmoon
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kmoon = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kmoon-i18n
Internationalization and localization files for kmoon.

%description -n kdetoys-kmoon-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmoon.

%package -n kdetoys-kodo-i18n
Summary:	Internationalization and localization files for kodo
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kodo
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kodo = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kodo-i18n
Internationalization and localization files for kodo.

%description -n kdetoys-kodo-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kodo.

%package -n kdetoys-kteatime-i18n
Summary:	Internationalization and localization files for kteatime
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kteatime
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kteatime = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kteatime-i18n
Internationalization and localization files for kteatime.

%description -n kdetoys-kteatime-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kteatime.

%package -n kdetoys-ktux-i18n
Summary:	Internationalization and localization files for ktux
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ktuksa
Group:		X11/Applications
Requires:	kdebase-screensavers-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-ktux = %{kdetoys_epoch}:%{version}

%description -n kdetoys-ktux-i18n
Internationalization and localization files for ktux.

%description -n kdetoys-ktux-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ktuksa.

%package -n kdetoys-kweather-i18n
Summary:	Internationalization and localization files for kweather
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kweather
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kweather = %{kdetoys_epoch}:%{version}

%description -n kdetoys-kweather-i18n
Internationalization and localization files for kweather.

%description -n kdetoys-kweather-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kweather.

%package -n kdetoys-kworldclock-i18n
Summary:	Internationalization and localization files for kworldclock
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kworldclocka
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdetoys-kworldclock = %{kdetoys_epoch}:%{version}
Requires:	konqueror-i18n = %{epoch}:%{version}-%{release}

%description -n kdetoys-kworldclock-i18n
Internationalization and localization files for kworldclock.

%description -n kdetoys-kworldclock-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kworldclocka.

%package -n kdeutils-ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla arka
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-ark = %{kdeutils_epoch}:%{version}

%description -n kdeutils-ark-i18n
Internationalization and localization files for ark.

%description -n kdeutils-ark-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla arka.

%package -n kdeutils-kcalc-i18n
Summary:	Internationalization and localization files for kcalc
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcalca
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kcalc = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kcalc-i18n
Internationalization and localization files for kcalc.

%description -n kdeutils-kcalc-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcalca.

%package -n kdeutils-kcharselect-i18n
Summary:	Internationalization and localization files for kcharselect
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcharselecta
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kcharselect = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kcharselect-i18n
Internationalization and localization files for kcharselect.

%description -n kdeutils-kcharselect-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcharselecta.

%package -n kdeutils-kdelirc-i18n
Summary:	Internationalization and localization files for kdelirc
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdelirca
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kdelirc = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kdelirc-i18n
Internationalization and localization files for kdelirc.

%description -n kdeutils-kdelirc-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdelirca.

%package -n kdeutils-kdessh-i18n
Summary:	Internationalization and localization files for kdessh
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdessh
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kdessh = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kdessh-i18n
Internationalization and localization files for kdessh.

%description -n kdeutils-kdessh-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdessh.

%package -n kdeutils-kdf-i18n
Summary:	Internationalization and localization files for kdf
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdf
Group:		X11/Applications
Requires:	kdebase-infocenter-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kdf = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kdf-i18n
Internationalization and localization files for kdf.

%description -n kdeutils-kdf-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdf.

%package -n kdeutils-kedit-i18n
Summary:	Internationalization and localization files for kedit
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kedit = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kedit-i18n
Internationalization and localization files for kedit.

%description -n kdeutils-kedit-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kedita.

%package -n kdeutils-kfloppy-i18n
Summary:	Internationalization and localization files for kfloppy
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfloppy
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kfloppy = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kfloppy-i18n
Internationalization and localization files for kfloppy.

%description -n kdeutils-kfloppy-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfloppy.

%package -n kdeutils-kgpg-i18n
Summary:	Internationalization and localization files for kgpg
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kgpg
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kgpg = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kgpg-i18n
Internationalization and localization files for kgpg.

%description -n kdeutils-kgpg-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kgpg.

%package -n kdeutils-khexedit-i18n
Summary:	Internationalization and localization files for khexedit
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla khexedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-khexedit = %{kdeutils_epoch}:%{version}

%description -n kdeutils-khexedit-i18n
Internationalization and localization files for khexedit.

%description -n kdeutils-khexedit-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla khexedita.

%package -n kdeutils-kjots-i18n
Summary:	Internationalization and localization files for kjots
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kjots
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kjots = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kjots-i18n
Internationalization and localization files for kjots.

%description -n kdeutils-kjots-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kjots.

%package -n kdeutils-klaptopdaemon-i18n
Summary:	Internationalization and localization files for klaptopdaemon
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla klaptopdaemona
Group:		X11/Applications
Requires:	kdebase-infocenter-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-klaptopdaemon = %{kdeutils_epoch}:%{version}

%description -n kdeutils-klaptopdaemon-i18n
Internationalization and localization files for klaptopdaemon.

%description -n kdeutils-klaptopdaemon-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla klaptopdaemona.

%package -n kdeutils-kmilo-i18n
Summary:	Internationalization and localization files for kmilo
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kedita
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kmilo = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kmilo-i18n
Internationalization and localization files for kmilo.

%description -n kdeutils-kmilo-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kmilo.

%package -n kdeutils-kregexpeditor-i18n
Summary:	Internationalization and localization files for kregexpeditor
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kregexpeditora
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kregexpeditor = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kregexpeditor-i18n
Internationalization and localization files for kregexpeditor.

%description -n kdeutils-kregexpeditor-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kregexpeditora.

%package -n kdeutils-ksim-i18n
Summary:	Internationalization and localization files for ksim
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ksima
Group:		X11/Applications
Requires:	kdebase-desktop-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-ksim = %{kdeutils_epoch}:%{version}

%description -n kdeutils-ksim-i18n
Internationalization and localization files for ksim.

%description -n kdeutils-ksim-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ksima.

%package -n kdeutils-ktimer-i18n
Summary:	Internationalization and localization files for ktimer
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla ktimera
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-ktimer = %{kdeutils_epoch}:%{version}

%description -n kdeutils-ktimer-i18n
Internationalization and localization files for ktimer.

%description -n kdeutils-ktimer-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla ktimera.

%package -n kdeutils-kwalletmanager-i18n
Summary:	Internationalization and localization files for kwalletmanager
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kwalletmanagera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-kwalletmanager = %{kdeutils_epoch}:%{version}

%description -n kdeutils-kwalletmanager-i18n
Internationalization and localization files for kwalletmanager.

%description -n kdeutils-kwalletmanager-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kwalletmanagera.

%package -n kdeutils-superkaramba-i18n
Summary:	Internationalization and localization files for superkaramba
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kwalletmanagera
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdeutils-superkaramba = %{kdeutils_epoch}:%{version}

%description -n kdeutils-superkaramba-i18n
Internationalization and localization files for superkaramba.

%description -n kdeutils-superkaramba-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla superkaramba.

%package -n kdevelop-i18n
Summary:	Internationalization and localization files for kdevelop
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kdevelopa
Group:		X11/Applications
Requires:	kdelibs-i18n = %{epoch}:%{version}-%{release}
Requires:	kdevelop >= %{kdevelop_epoch}:%{kdevelop_version}

%description -n kdevelop-i18n
Internationalization and localization files for kdevelop.

%description -n kdevelop-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kdevelopa.

%package -n kdewebdev-kfilereplace-i18n
Summary:	Internationalization and localization files for kfilereplace
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kfilereplace
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kfilereplace = %{kdewebdev_epoch}:%{version}
Obsoletes:	kdesdk-kfilereplace-i18n

%description -n kdewebdev-kfilereplace-i18n
Internationalization and localization files for kfilereplace.

%description -n kdewebdev-kfilereplace-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kfilereplace.

%package -n kdewebdev-kimagemapeditor-i18n
Summary:	Internationalization and localization files for kimagemapeditor
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kimagemapeditor
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kimagemapeditor = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-kimagemapeditor-i18n
Internationalization and localization files for kimagemapeditor.

%description -n kdewebdev-kimagemapeditor-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kimagemapeditor.

%package -n kdewebdev-klinkstatus-i18n
Summary:	Internationalization and localization files for klinkstatus
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla klinkstatus
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-klinkstatus = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-klinkstatus-i18n
Internationalization and localization files for klinkstatus.

%description -n kdewebdev-klinkstatus-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla klinkstatus.

%package -n kdewebdev-kommander-i18n
Summary:	Internationalization and localization files for kommander
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kommander
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kommander = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-kommander-i18n
Internationalization and localization files for kommander.

%description -n kdewebdev-kommander-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kommander.

%package -n kdewebdev-kxsldbg-i18n
Summary:	Internationalization and localization files for kxsldbg
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kxsldbg
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-kxsldbg = %{kdewebdev_epoch}:%{version}

%description -n kdewebdev-kxsldbg-i18n
Internationalization and localization files for kxsldbg.

%description -n kdewebdev-kxsldbg-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla kxsldbg.

%package -n kdewebdev-quanta-i18n
Summary:	Internationalization and localization files for quanta
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla quanta
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdewebdev-quanta = %{kdewebdev_epoch}:%{version}
Obsoletes:	quanta-i18n

%description -n kdewebdev-quanta-i18n
Internationalization and localization files for quanta.

%description -n kdewebdev-quanta-i18n -l pl.UTF-8
Pliki umiędzynarodawiające dla quanta.

%package -n kdm-i18n
Summary:	Internationalization and localization files for kdm
Summary(pl.UTF-8):	Tłumaczenia dla kdm-a
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdm = %{kdebase_epoch}:%{version}

%description -n kdm-i18n
Internationalization and localization files for kdm.

%description -n kdm-i18n -l pl.UTF-8
Tłumaczenia dla kdm-a.

%package -n konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl.UTF-8):	Tłumaczenia dla konquerora
Group:		X11/Applications
Requires:	kdebase-core-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-konsole-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror = %{kdebase_epoch}:%{version}
Requires:	konqueror-libs-i18n = %{epoch}:%{version}-%{release}

%description -n konqueror-i18n
Internationalization and localization files for konqueror.

%description -n konqueror-i18n -l pl.UTF-8
Tłumaczenia dla konquerora.

%package -n konqueror-libs-i18n
Summary:	Internationalization and localization files for libkonq
Summary(pl.UTF-8):	Tłumaczenia dla libkonq
Group:		X11/Applications
Requires:	konqueror-libs = %{kdebase_epoch}:%{version}
Obsoletes:	kdebase-libkonq-i18n

%description -n konqueror-libs-i18n
Internationalization and localization files for libkonq.

%description -n konqueror-libs-i18n -l pl.UTF-8
Tłumaczenia dla libkonq.

%prep
%setup -qcT %(seq -f '-a %g' 0 66 | xargs)

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

%if "%{version}" == "3.5.7"
	# - kcmsmartcard - kdebase-3.5.6/kcontrol/smartcard - not packaged in pld
	rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kcmsmartcard.mo
	# - kres_blogging.mo - kdepim-3.5.6/kresources/blogging/ - not packged in pld
	rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kres_blogging.mo
	# - kmobile - kdepim-3.5.6/kmobile/ - not built in pld
	rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kmobile.mo
	# - kio_mobile - kdepim-3.5.6/kmobile/kioslave/ - not built in pld
	rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kio_mobile.mo

	# - kstyle_phase_config kdeartwork-3.5.6/styles/phase/config/kstyle_phase_config.la
	rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kstyle_phase_config.mo
	# - kres_tvanytime.mo - kdepim-3.5.6/kresources/tvanytime/
	rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kres_tvanytime.mo
%endif

	# XXX check this rename
	mv $RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.mk{_MK,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.mk{_MK,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/mk{_MK,}

	# (probably) no longer in kde
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/jefferson.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/katekttsd.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/katepartkttsd.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kateprojectmanager.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/katespell.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kcmkmix.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kcmmediacontrol.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kcmvim.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kio_newimap4.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/klegacyimport.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/konq_smbmounterplugin.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kres_opengroupware.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kviewtemplateplugin.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/libcalendarresources.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/libkcalsystem.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/libkdehighscores.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/libkdenetwork.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/vimpart.mo
	rm $RPM_BUILD_ROOT%{_datadir}/locale/ro/LC_MESSAGES/kviewtemplateplugin.mo

	# kmessedwords renamed to kanagram
	rm $RPM_BUILD_ROOT%{_datadir}/locale/km/LC_MESSAGES/kmessedwords.mo
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/*/kmessedwords

	# kpaint renamed (obsoleted) by kolourpaint
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/es/kpaint

	# kdeadmin/kxconfig - not in kde tarballs, moved to kdenonbeta
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/*/kxconfig
	# kdeadmin/kwuftpd - not in kde tarballs, moved to kdenonbeta
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/*/kwuftpd
	# kdemultimedia/kmidi - moved to kdenonbeta
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/*/kmidi

	# kdegames/megami - obsoleted
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/*/megami
	# kdeedu/flashkard - obsoleted
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/*/flashkard

	# useless for the user
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fa/COPYING
	rm $RPM_BUILD_ROOT%{_datadir}/locale/nb/README
	rm $RPM_BUILD_ROOT%{_datadir}/locale/se/ChangeLog
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/nbsp_gui_fr.txt
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/relecture_docs
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/relecture_gui
	rm $RPM_BUILD_ROOT%{_datadir}/locale/da/da.compendium
	rm -r $RPM_BUILD_ROOT%{_kdedocdir}/pt_BR/api
	rm $RPM_BUILD_ROOT%{_kdedocdir}/es/api/*.png

	# junk
	rm $RPM_BUILD_ROOT%{_datadir}/locale/mn/30x16.png
	rm $RPM_BUILD_ROOT%{_datadir}/locale/mn/60x40.png

	# old ones, by some coolo:
	# DON'T PACKAGE KMATHTOOL
	rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/kmathtool.mo
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/*/kmathtool
	# Not packaging kmobile, it was disabled by coolo
	# We don't build kcardchooser (disabled by default by coolo)
	# re-enabling it would be posssible, but what for?

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
		%find_lang $a --with-kde lang.tmp > /dev/null
		cat lang.tmp >> $out
	done
}

kde_find_lang kde-decoration-common-i18n kwin_art_clients
kde_find_lang kde-kgreet-classic-i18n kgreet_classic
kde_find_lang kde-kio-groupwise-i18n kio_groupwise
kde_find_lang kde-kio-imap4-i18n kio_imap4
kde_find_lang kde-kio-ldap-i18n kio_ldap
kde_find_lang kde-kio-nntp-i18n kio_nntp
kde_find_lang kde-kio-pop3-i18n kio_pop3
kde_find_lang kde-kio-smtp-i18n kio_smtp
kde_find_lang kde-kio-svn-i18n kio_svn
kde_find_lang kde-resource-bugzilla-i18n kres_bugzilla
kde_find_lang kdeaccessibility-kbstateapplet-i18n kbstateapplet
kde_find_lang kdeaccessibility-kmag-i18n kmag
kde_find_lang kdeaccessibility-kmousetool-i18n kmousetool
kde_find_lang kdeaccessibility-kmouth-i18n kmouth
kde_find_lang kdeaccessibility-ksayit-i18n ksayit
kde_find_lang kdeaccessibility-kttsd-i18n "
	kcmkttsd
	ktexteditor_kttsd
	kttsd
	kttsd_commandplugin
	kttsd_eposplugin
	kttsd_fliteplugin
	kttsd_freettsplugin
	kttsd_sbdplugin
	kttsd_xmltransformerplugin
	kttsmgr
	libKTTSD
"
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
	katesnippets
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
	mf_konqplugin
	minitoolsplugin
	searchbarplugin
	uachangerplugin
	validatorsplugin
"
# webarchiver and domtreeviewer are subdirs of konq-plugins in %{_kdedocdir}
# which we already scanned but they are also as .mo, so scan just .mo
%find_lang domtreeviewer
%find_lang webarchiver
cat domtreeviewer.lang webarchiver.lang >> kdeaddons-konqueror-i18n.lang
rm -f domtreeviewer.lang webarchiver.lang

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

# Hack: 'BuildArch: noarch' and %%ifarch do not work, so we create empty packages.
# TH: In reality the arches would get full tarball anyway
# These arch's don't bave kcmlilo package: %{ix86} %{x8664} sparc sparc64
> kdeadmin-kcmlilo-i18n.lang
kde_find_lang kdeadmin-kcmlilo-i18n kcmlilo lilo-config || :

kde_find_lang kdeadmin-kcron-i18n kcron
kde_find_lang kdeadmin-kdat-i18n kdat
kde_find_lang kdeadmin-knetworkconf-i18n knetworkconf
kde_find_lang kdeadmin-kpackage-i18n kpackage kfile_deb kfile_rpm
kde_find_lang kdeadmin-ksysv-i18n ksysv secpolicy
kde_find_lang kdeadmin-kuser-i18n kuser
kde_find_lang kdeartwork-screensavers-i18n klock kpartsaver kxsconfig
kde_find_lang kdebase-core-i18n "
	drkonqi
	kcmaccessibility
	kcmcolors
	kcmfonts
	kcmkded
	kcmlocale
	kcmprintmgr
	kcontrol
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
	kompmgr
	kprinter
	kstyle_keramik_config
"
# kcmstyle is subdir of kcontrol in %{_kdedocdir} which we already scanned but
# it's are also as .mo, so scan just .mo
%find_lang kcmstyle
cat kcmstyle.lang >> kdebase-core-i18n.lang
rm -f kcmstyle

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
	kay
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
	kcmmedia
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
	kthememanager
	ktip
	kwin
	kwin_clients
	kwindecoration
	kwin_lib
	kwriteconfig
	kxkb
	kxmlrpcd
	libkicker
	libkickermenu_kdeprint
	libkickermenu_konsole
	libkickermenu_prefmenu
	libkickermenu_recentdocs
	libkickermenu_remotemenu
	libkickermenu_systemmenu
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
	trashapplet
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
	katetabbarextension
"
kde_find_lang kdebase-kdcop-i18n kdcop dcoprss
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
kde_find_lang kdebase-kwrite-i18n kwrite
kde_find_lang kdebase-screensavers-i18n screensaver kcmscreensaver kscreensaver
kde_find_lang kdebase-useraccount-i18n useraccount kdepasswd
kde_find_lang kdeedu-blinken-i18n blinken
kde_find_lang kdeedu-kalzium-i18n kalzium
kde_find_lang kdeedu-kanagram-i18n kanagram
kde_find_lang kdeedu-kbruch-i18n kbruch
kde_find_lang kdeedu-keduca-i18n keduca
kde_find_lang kdeedu-kgeography-i18n kgeography
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
kde_find_lang kdeedu-libkdeeduui-i18n libkdeedu
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
kde_find_lang kdegames-knetwalk-i18n knetwalk
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
kde_find_lang kdegraphics-kfax-i18n kfax kfaxview libkfaximgage
kde_find_lang kdegraphics-kfile-i18n "
	kfile_bmp
	kfile_dds
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
	kfile_xpm
"
kde_find_lang kdegraphics-kgamma-i18n kgamma
kde_find_lang kdegraphics-kghostview-i18n kghostview
kde_find_lang kdegraphics-kiconedit-i18n kiconedit
kde_find_lang kdegraphics-kmrml-i18n kmrml
kde_find_lang kdegraphics-kolourpaint-i18n kolourpaint
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
	kviewviewer
"
kde_find_lang kdegraphics-kviewshell-i18n kviewshell kdjview
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
	kfile_mpeg
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
kde_find_lang kdenetwork-kdnssd-i18n kio_zeroconf kcmkdnssd
kde_find_lang kdenetwork-kfile-torrent-i18n kfile_torrent
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
	konnector_dummy
	konnector_kabc
	konnector_kcal
	konnector_local
	konnector_qtopia
	konnector_remote
	kontact
	korganizer
	kres_birthday
	kres_exchange
	kres_imap
	kres_kolab
	kres_remote
	kres_xmlrpc
	ksync
	multisynk
"
kde_find_lang kdepim-kaddressbook-i18n kabc2mutt kaddressbook kcmkabconfig kfile_vcf libkaddrbk_gmx_xxport
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
	kdepimresources
	kdgantt
	kgantt
	kres_featureplan
	kres_groupware
	kres_groupwise
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
kde_find_lang kdesdk-kapptemplate-i18n kapptemplate
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
kde_find_lang kdesdk-scripts-developer-i18n scripts kdesvn-build
kde_find_lang kdesdk-umbrello-i18n umbrello
kde_find_lang kdetoys-amor-i18n amor
kde_find_lang kdetoys-fifteen-i18n kfifteenapplet
kde_find_lang kdetoys-kmoon-i18n kmoon
kde_find_lang kdetoys-kodo-i18n kodo
kde_find_lang kdetoys-kteatime-i18n kteatime
kde_find_lang kdetoys-ktux-i18n ktux
kde_find_lang kdetoys-kweather-i18n kweather
kde_find_lang kdetoys-kworldclock-i18n kworldclock
kde_find_lang kdeutils-ark-i18n ark
kde_find_lang kdeutils-kcalc-i18n kcalc
kde_find_lang kdeutils-kcharselect-i18n kcharselect kcharselectapplet
kde_find_lang kdeutils-kdelirc-i18n kdelirc irkick kcmlirc
kde_find_lang kdeutils-kdessh-i18n kdessh
kde_find_lang kdeutils-kdf-i18n kdf blockdevices
kde_find_lang kdeutils-kedit-i18n kedit
kde_find_lang kdeutils-kfloppy-i18n kfloppy
kde_find_lang kdeutils-kgpg-i18n kgpg
kde_find_lang kdeutils-khexedit-i18n khexedit khexedit2part
kde_find_lang kdeutils-kjots-i18n kjots
kde_find_lang kdeutils-klaptopdaemon-i18n klaptopdaemon kcmlowbatcrit kcmlowbatwarn laptop powerctrl kcmlaptop
kde_find_lang kdeutils-kmilo-i18n "
	kcmkvaio
	kcmthinkpad
	kmilo_delli8k
	kmilo_generic
	kmilo_kvaio
	kmilo_powerbook
	kmilo_thinkpad
	kmilod
"
kde_find_lang kdeutils-kregexpeditor-i18n KRegExpEditor kregexpeditor
kde_find_lang kdeutils-ksim-i18n ksim
kde_find_lang kdeutils-ktimer-i18n ktimer
kde_find_lang kdeutils-kwalletmanager-i18n kwallet kwalletmanager kcmkwallet
kde_find_lang kdeutils-superkaramba-i18n superkaramba
kde_find_lang kdevelop-i18n "
	kde_app_devel
	kdearch
	kdevdesigner
	kdevelop
	kdevtipofday
	kpartapp
	qeditor
"
kde_find_lang kdewebdev-kfilereplace-i18n kfilereplace
kde_find_lang kdewebdev-kimagemapeditor-i18n kimagemapeditor
kde_find_lang kdewebdev-klinkstatus-i18n klinkstatus
kde_find_lang kdewebdev-kommander-i18n kommander
kde_find_lang kdewebdev-kxsldbg-i18n kxsldbg xsldbg
kde_find_lang kdewebdev-quanta-i18n quanta
kde_find_lang kdm-i18n kdm kdmconfig kdmgreet libdmctl kgreet_winbind
kde_find_lang konqueror-i18n "
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
	konqueror
	netpref
	nsplugin
	proxy
	smb
	useragent
"
kde_find_lang konqueror-libs-i18n libkonq

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-common-i18n -f kde-decoration-common-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kgreet-classic-i18n -f kde-kgreet-classic-i18n.lang
%defattr(644,root,root,755)
%files -n kde-kio-groupwise-i18n -f kde-kio-groupwise-i18n.lang
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
%files -n kde-kio-svn-i18n -f kde-kio-svn-i18n.lang
%defattr(644,root,root,755)
%files -n kde-resource-bugzilla-i18n -f kde-resource-bugzilla-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kbstateapplet-i18n -f kdeaccessibility-kbstateapplet-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmag-i18n -f kdeaccessibility-kmag-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmousetool-i18n -f kdeaccessibility-kmousetool-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kmouth-i18n -f kdeaccessibility-kmouth-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-ksayit-i18n -f kdeaccessibility-ksayit-i18n.lang
%defattr(644,root,root,755)
%files -n kdeaccessibility-kttsd-i18n -f kdeaccessibility-kttsd-i18n.lang
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
%files -n kdeadmin-knetworkconf-i18n -f kdeadmin-knetworkconf-i18n.lang
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
%lang(af) %{_datadir}/locale/af/charset
%lang(af) %{_datadir}/locale/af/entry.desktop
%lang(af) %{_datadir}/locale/af/flag.png
%lang(ar) %{_datadir}/locale/ar/charset
%lang(ar) %{_datadir}/locale/ar/entry.desktop
#%lang(ar) %{_datadir}/locale/ar/flag.png
%lang(az) %{_datadir}/locale/az/charset
%lang(az) %{_datadir}/locale/az/entry.desktop
%lang(az) %{_datadir}/locale/az/flag.png
%lang(bg) %{_datadir}/locale/bg/charset
%lang(bg) %{_datadir}/locale/bg/entry.desktop
%lang(bg) %{_datadir}/locale/bg/flag.png
%lang(bn) %{_datadir}/locale/bn/charset
%lang(bn) %{_datadir}/locale/bn/entry.desktop
#%lang(bn) %{_datadir}/locale/bn/flag.png
%lang(br) %{_datadir}/locale/br/charset
%lang(br) %{_datadir}/locale/br/entry.desktop
%lang(br) %{_datadir}/locale/br/flag.png
%lang(bs) %{_datadir}/locale/bs/charset
%lang(bs) %{_datadir}/locale/bs/entry.desktop
%lang(bs) %{_datadir}/locale/bs/flag.png
%lang(ca) %{_datadir}/locale/ca/charset
%lang(ca) %{_datadir}/locale/ca/entry.desktop
%lang(ca) %{_datadir}/locale/ca/flag.png
%lang(csb) %{_datadir}/locale/csb/charset
%lang(csb) %{_datadir}/locale/csb/entry.desktop
%lang(csb) %{_datadir}/locale/csb/flag.png
%lang(cs) %{_datadir}/locale/cs/charset
%lang(cs) %{_datadir}/locale/cs/entry.desktop
%lang(cs) %{_datadir}/locale/cs/flag.png
%lang(cy) %{_datadir}/locale/cy/charset
%lang(cy) %{_datadir}/locale/cy/entry.desktop
%lang(cy) %{_datadir}/locale/cy/flag.png
%lang(da) %{_datadir}/locale/da/charset
%lang(da) %{_datadir}/locale/da/entry.desktop
%lang(da) %{_datadir}/locale/da/flag.png
%lang(de) %{_datadir}/locale/de/charset
%lang(de) %{_datadir}/locale/de/entry.desktop
%lang(de) %{_datadir}/locale/de/flag.png
%lang(el) %{_datadir}/locale/el/charset
%lang(el) %{_datadir}/locale/el/entry.desktop
%lang(el) %{_datadir}/locale/el/flag.png
%lang(en_GB) %{_datadir}/locale/en_GB/charset
%lang(en_GB) %{_datadir}/locale/en_GB/entry.desktop
%lang(en_GB) %{_datadir}/locale/en_GB/flag.png
%lang(eo) %{_datadir}/locale/eo/charset
%lang(eo) %{_datadir}/locale/eo/entry.desktop
%lang(eo) %{_datadir}/locale/eo/flag.png
%lang(es) %{_datadir}/locale/es/charset
%lang(es) %{_datadir}/locale/es/entry.desktop
%lang(es) %{_datadir}/locale/es/flag.png
%lang(et) %{_datadir}/locale/et/charset
%lang(et) %{_datadir}/locale/et/entry.desktop
%lang(et) %{_datadir}/locale/et/flag.png
%lang(eu) %{_datadir}/locale/eu/charset
%lang(eu) %{_datadir}/locale/eu/entry.desktop
%lang(eu) %{_datadir}/locale/eu/flag.png
%lang(fa) %{_datadir}/locale/fa/charset
%lang(fa) %{_datadir}/locale/fa/entry.desktop
%lang(fa) %{_datadir}/locale/fa/flag.png
%lang(fi) %{_datadir}/locale/fi/charset
%lang(fi) %{_datadir}/locale/fi/entry.desktop
%lang(fi) %{_datadir}/locale/fi/flag.png
%lang(fr) %{_datadir}/locale/fr/charset
%lang(fr) %{_datadir}/locale/fr/entry.desktop
%lang(fr) %{_datadir}/locale/fr/flag.png
%lang(fy) %{_datadir}/locale/fy/charset
%lang(fy) %{_datadir}/locale/fy/entry.desktop
#%lang(fy) %{_datadir}/locale/fy/flag.png
%lang(ga) %{_datadir}/locale/ga/charset
%lang(ga) %{_datadir}/locale/ga/entry.desktop
%lang(ga) %{_datadir}/locale/ga/flag.png
%lang(gl) %{_datadir}/locale/gl/charset
%lang(gl) %{_datadir}/locale/gl/entry.desktop
%lang(gl) %{_datadir}/locale/gl/flag.png
%lang(he) %{_datadir}/locale/he/charset
%lang(he) %{_datadir}/locale/he/entry.desktop
%lang(he) %{_datadir}/locale/he/flag.png
%lang(hi) %{_datadir}/locale/hi/charset
%lang(hi) %{_datadir}/locale/hi/entry.desktop
#%lang(hi) %{_datadir}/locale/hi/flag.png
%lang(hr) %{_datadir}/locale/hr/charset
%lang(hr) %{_datadir}/locale/hr/entry.desktop
%lang(hr) %{_datadir}/locale/hr/flag.png
%lang(hu) %{_datadir}/locale/hu/charset
%lang(hu) %{_datadir}/locale/hu/entry.desktop
%lang(hu) %{_datadir}/locale/hu/flag.png
%lang(is) %{_datadir}/locale/is/charset
%lang(is) %{_datadir}/locale/is/entry.desktop
%lang(is) %{_datadir}/locale/is/flag.png
%lang(it) %{_datadir}/locale/it/charset
%lang(it) %{_datadir}/locale/it/entry.desktop
%lang(it) %{_datadir}/locale/it/flag.png
%lang(ja) %{_datadir}/locale/ja/charset
%lang(ja) %{_datadir}/locale/ja/entry.desktop
%lang(ja) %{_datadir}/locale/ja/flag.png
%lang(kk) %{_datadir}/locale/kk/charset
%lang(kk) %{_datadir}/locale/kk/entry.desktop
%lang(kk) %{_datadir}/locale/kk/flag.png
%lang(km) %{_datadir}/locale/km/charset
%lang(km) %{_datadir}/locale/km/entry.desktop
%lang(km) %{_datadir}/locale/km/flag.png
%lang(ko) %{_datadir}/locale/ko/charset
%lang(ko) %{_datadir}/locale/ko/entry.desktop
%lang(ko) %{_datadir}/locale/ko/flag.png
%lang(lt) %{_datadir}/locale/lt/charset
%lang(lt) %{_datadir}/locale/lt/entry.desktop
%lang(lt) %{_datadir}/locale/lt/flag.png
%lang(lv) %{_datadir}/locale/lv/charset
%lang(lv) %{_datadir}/locale/lv/entry.desktop
%lang(lv) %{_datadir}/locale/lv/flag.png
%lang(mk) %{_datadir}/locale/mk/charset
%lang(mk) %{_datadir}/locale/mk/entry.desktop
%lang(mk) %{_datadir}/locale/mk/flag.png
%lang(mn) %{_datadir}/locale/mn/charset
%lang(mn) %{_datadir}/locale/mn/entry.desktop
#%lang(mn) %{_datadir}/locale/mn/flag.png
%lang(mn) %{_datadir}/locale/mn/flag_new_30x16.png
%lang(ms) %{_datadir}/locale/ms/charset
%lang(ms) %{_datadir}/locale/ms/entry.desktop
#%lang(ms) %{_datadir}/locale/ms/flag.png
%lang(nb) %{_datadir}/locale/nb/charset
%lang(nb) %{_datadir}/locale/nb/entry.desktop
%lang(nb) %{_datadir}/locale/nb/flag.png
%lang(nds) %{_datadir}/locale/nds/charset
%lang(nds) %{_datadir}/locale/nds/entry.desktop
#%lang(nds) %{_datadir}/locale/nds/flag.png
%lang(nl) %{_datadir}/locale/nl/charset
%lang(nl) %{_datadir}/locale/nl/entry.desktop
%lang(nl) %{_datadir}/locale/nl/flag.png
%lang(nn) %{_datadir}/locale/nn/charset
%lang(nn) %{_datadir}/locale/nn/entry.desktop
%lang(nn) %{_datadir}/locale/nn/flag.png
%lang(pa) %{_datadir}/locale/pa/charset
%lang(pa) %{_datadir}/locale/pa/entry.desktop
#%lang(pa) %{_datadir}/locale/pa/flag.png
%lang(pl) %{_datadir}/locale/pl/charset
%lang(pl) %{_datadir}/locale/pl/entry.desktop
%lang(pl) %{_datadir}/locale/pl/flag.png
%lang(pt) %{_datadir}/locale/pt/charset
%lang(pt) %{_datadir}/locale/pt/entry.desktop
%lang(pt) %{_datadir}/locale/pt/flag.png
%lang(pt_BR) %{_datadir}/locale/pt_BR/charset
%lang(pt_BR) %{_datadir}/locale/pt_BR/entry.desktop
%lang(pt_BR) %{_datadir}/locale/pt_BR/flag.png
%lang(ro) %{_datadir}/locale/ro/charset
%lang(ro) %{_datadir}/locale/ro/entry.desktop
%lang(ro) %{_datadir}/locale/ro/flag.png
%lang(ru) %{_datadir}/locale/ru/charset
%lang(ru) %{_datadir}/locale/ru/entry.desktop
%lang(ru) %{_datadir}/locale/ru/flag.png
%lang(rw) %{_datadir}/locale/rw/charset
%lang(rw) %{_datadir}/locale/rw/entry.desktop
#%lang(rw) %{_datadir}/locale/rw/flag.png
%lang(se) %{_datadir}/locale/se/charset
%lang(se) %{_datadir}/locale/se/entry.desktop
%lang(se) %{_datadir}/locale/se/flag.png
%lang(sk) %{_datadir}/locale/sk/charset
%lang(sk) %{_datadir}/locale/sk/entry.desktop
%lang(sk) %{_datadir}/locale/sk/flag.png
%lang(sl) %{_datadir}/locale/sl/charset
%lang(sl) %{_datadir}/locale/sl/entry.desktop
%lang(sl) %{_datadir}/locale/sl/flag.png
%lang(sr) %{_datadir}/locale/sr/charset
%lang(sr) %{_datadir}/locale/sr/entry.desktop
%lang(sr) %{_datadir}/locale/sr/flag.png
%lang(sr@Latn) %{_datadir}/locale/sr@Latn/charset
%lang(sr@Latn) %{_datadir}/locale/sr@Latn/entry.desktop
%lang(sr@Latn) %{_datadir}/locale/sr@Latn/flag.png
%lang(ss) %{_datadir}/locale/ss/charset
%lang(ss) %{_datadir}/locale/ss/entry.desktop
#%lang(ss) %{_datadir}/locale/ss/flag.png
%lang(sv) %{_datadir}/locale/sv/charset
%lang(sv) %{_datadir}/locale/sv/entry.desktop
%lang(sv) %{_datadir}/locale/sv/flag.png
%lang(ta) %{_datadir}/locale/ta/charset
%lang(ta) %{_datadir}/locale/ta/entry.desktop
%lang(ta) %{_datadir}/locale/ta/flag.png
%lang(tg) %{_datadir}/locale/tg/charset
%lang(tg) %{_datadir}/locale/tg/entry.desktop
%lang(th) %{_datadir}/locale/th/charset
%lang(th) %{_datadir}/locale/th/entry.desktop
%lang(th) %{_datadir}/locale/th/flag.png
#%lang(tg) %{_datadir}/locale/tg/flag.png
%lang(tr) %{_datadir}/locale/tr/charset
%lang(tr) %{_datadir}/locale/tr/entry.desktop
%lang(tr) %{_datadir}/locale/tr/flag.png
%lang(uk) %{_datadir}/locale/uk/charset
%lang(uk) %{_datadir}/locale/uk/entry.desktop
%lang(uk) %{_datadir}/locale/uk/flag.png
%lang(uz) %{_datadir}/locale/uz/charset
%lang(uz) %{_datadir}/locale/uz/entry.desktop
%lang(uz) %{_datadir}/locale/uz/flag.png
%lang(vi) %{_datadir}/locale/vi/charset
%lang(vi) %{_datadir}/locale/vi/entry.desktop
%lang(vi) %{_datadir}/locale/vi/flag.png
%lang(zh_CN) %{_datadir}/locale/zh_CN/charset
%lang(zh_CN) %{_datadir}/locale/zh_CN/entry.desktop
%lang(zh_CN) %{_datadir}/locale/zh_CN/flag.png
%lang(zh_TW) %{_datadir}/locale/zh_TW/charset
%lang(zh_TW) %{_datadir}/locale/zh_TW/entry.desktop
%lang(zh_TW) %{_datadir}/locale/zh_TW/flag.png

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
%files -n kdeedu-blinken-i18n -f kdeedu-blinken-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kalzium-i18n -f kdeedu-kalzium-i18n.lang
%defattr(644,root,root,755)

%files -n kdeedu-kanagram-i18n -f kdeedu-kanagram-i18n.lang
%defattr(644,root,root,755)
%lang(de) %{_datadir}/apps/kanagram/data/de
%lang(et) %{_datadir}/apps/kanagram/data/et
%lang(fr) %{_datadir}/apps/kanagram/data/fr
%lang(it) %{_datadir}/apps/kanagram/data/it

%files -n kdeedu-kbruch-i18n -f kdeedu-kbruch-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-keduca-i18n -f kdeedu-keduca-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kgeography-i18n -f kdeedu-kgeography-i18n.lang
%defattr(644,root,root,755)

%files -n kdeedu-khangman-i18n -f kdeedu-khangman-i18n.lang
%defattr(644,root,root,755)
%lang(ca) %{_datadir}/apps/khangman/ca.txt
%lang(cs) %{_datadir}/apps/khangman/cs.txt
%lang(da) %{_datadir}/apps/khangman/da.txt
%lang(de) %{_datadir}/apps/khangman/de.txt
%lang(es) %{_datadir}/apps/khangman/es.txt
%lang(et) %{_datadir}/apps/khangman/et.txt
%lang(fi) %{_datadir}/apps/khangman/fi.txt
%lang(fr) %{_datadir}/apps/khangman/fr.txt
%lang(ga) %{_datadir}/apps/khangman/ga.txt
%lang(hu) %{_datadir}/apps/khangman/hu.txt
%lang(nb) %{_datadir}/apps/khangman/nb.txt
%lang(nds) %{_datadir}/apps/khangman/nds.txt
%lang(nn) %{_datadir}/apps/khangman/nn.txt
%lang(pl) %{_datadir}/apps/khangman/pl.txt
%lang(pt_BR) %{_datadir}/apps/khangman/pt_BR.txt
%lang(pt) %{_datadir}/apps/khangman/pt.txt
%lang(sl) %{_datadir}/apps/khangman/sl.txt
%lang(sr@Latn) %{_datadir}/apps/khangman/sr@Latn.txt
%lang(sv) %{_datadir}/apps/khangman/sv.txt
%lang(tg) %{_datadir}/apps/khangman/tg.txt
%lang(tr) %{_datadir}/apps/khangman/tr.txt

%lang(bg) %{_datadir}/apps/khangman/data/bg
%lang(ca) %{_datadir}/apps/khangman/data/ca
%lang(cs) %{_datadir}/apps/khangman/data/cs
%lang(da) %{_datadir}/apps/khangman/data/da
%lang(de) %{_datadir}/apps/khangman/data/de
%lang(es) %{_datadir}/apps/khangman/data/es
%lang(et) %{_datadir}/apps/khangman/data/et
%lang(fi) %{_datadir}/apps/khangman/data/fi
%lang(fr) %{_datadir}/apps/khangman/data/fr
%lang(ga) %{_datadir}/apps/khangman/data/ga
%lang(hu) %{_datadir}/apps/khangman/data/hu
%lang(it) %{_datadir}/apps/khangman/data/it
%lang(nb) %{_datadir}/apps/khangman/data/nb
%lang(nds) %{_datadir}/apps/khangman/data/nds
%lang(nl) %{_datadir}/apps/khangman/data/nl
%lang(nn) %{_datadir}/apps/khangman/data/nn
%lang(pl) %{_datadir}/apps/khangman/data/pl
%lang(pt_BR) %{_datadir}/apps/khangman/data/pt_BR
%lang(pt) %{_datadir}/apps/khangman/data/pt
%lang(ru) %{_datadir}/apps/khangman/data/ru
%lang(sl) %{_datadir}/apps/khangman/data/sl
%lang(sr) %{_datadir}/apps/khangman/data/sr
%lang(sr@Latn) %{_datadir}/apps/khangman/data/sr@Latn
%lang(sv) %{_datadir}/apps/khangman/data/sv
%lang(tg) %{_datadir}/apps/khangman/data/tg
%lang(tr) %{_datadir}/apps/khangman/data/tr

%files -n kdeedu-kig-i18n -f kdeedu-kig-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kiten-i18n -f kdeedu-kiten-i18n.lang
%defattr(644,root,root,755)

%files -n kdeedu-klatin-i18n -f kdeedu-klatin-i18n.lang
%defattr(644,root,root,755)
%lang(it) %{_datadir}/apps/klatin/data/vocabs/it

%files -n kdeedu-klettres-i18n -f kdeedu-klettres-i18n.lang
%defattr(644,root,root,755)
%lang(cs) %{_datadir}/apps/klettres/cs
%lang(da) %{_datadir}/apps/klettres/da
%lang(de) %{_datadir}/apps/klettres/de
%lang(en_GB) %{_datadir}/apps/klettres/en_GB
%lang(es) %{_datadir}/apps/klettres/es
%lang(he) %{_datadir}/apps/klettres/he
%lang(it) %{_datadir}/apps/klettres/it
%lang(nds) %{_datadir}/apps/klettres/nds
%lang(nl) %{_datadir}/apps/klettres/nl
%lang(sk) %{_datadir}/apps/klettres/sk

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
%lang(ca) %{_datadir}/apps/kturtle/data/logokeywords.ca.xml
%lang(de_DE) %{_datadir}/apps/kturtle/data/logokeywords.de_DE.xml
%lang(en_GB) %{_datadir}/apps/kturtle/data/logokeywords.en_GB.xml
%lang(es) %{_datadir}/apps/kturtle/data/logokeywords.es.xml
%lang(fr_FR) %{_datadir}/apps/kturtle/data/logokeywords.fr_FR.xml
%lang(it) %{_datadir}/apps/kturtle/data/logokeywords.it.xml
%lang(mk) %{_datadir}/apps/kturtle/data/logokeywords.mk.xml
%lang(nl) %{_datadir}/apps/kturtle/data/logokeywords.nl.xml
%lang(pl) %{_datadir}/apps/kturtle/data/logokeywords.pl.xml
%lang(pt_BR) %{_datadir}/apps/kturtle/data/logokeywords.pt_BR.xml
%lang(ru) %{_datadir}/apps/kturtle/data/logokeywords.ru.xml
%lang(sk) %{_datadir}/apps/kturtle/data/logokeywords.sk.xml
%lang(sl) %{_datadir}/apps/kturtle/data/logokeywords.sl.xml
%lang(sr) %{_datadir}/apps/kturtle/data/logokeywords.sr.xml
%lang(sr@Latn) %{_datadir}/apps/kturtle/data/logokeywords.sr@Latn.xml
%lang(sv) %{_datadir}/apps/kturtle/data/logokeywords.sv.xml

%lang(ca) %{_datadir}/apps/kturtle/examples/ca
%lang(de_DE) %{_datadir}/apps/kturtle/examples/de_DE
%lang(en_GB) %{_datadir}/apps/kturtle/examples/en_GB
%lang(es) %{_datadir}/apps/kturtle/examples/es
%lang(fr_FR) %{_datadir}/apps/kturtle/examples/fr_FR
%lang(it) %{_datadir}/apps/kturtle/examples/it
%lang(mk) %{_datadir}/apps/kturtle/examples/mk
%lang(nl) %{_datadir}/apps/kturtle/examples/nl
%lang(pl) %{_datadir}/apps/kturtle/examples/pl
%lang(pt_BR) %{_datadir}/apps/kturtle/examples/pt_BR
%lang(ru) %{_datadir}/apps/kturtle/examples/ru
%lang(sk) %{_datadir}/apps/kturtle/examples/sk
%lang(sl) %{_datadir}/apps/kturtle/examples/sl
%lang(sr) %{_datadir}/apps/kturtle/examples/sr
%lang(sr@Latn) %{_datadir}/apps/kturtle/examples/sr@Latn
%lang(sv) %{_datadir}/apps/kturtle/examples/sv

%files -n kdeedu-kverbos-i18n -f kdeedu-kverbos-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kvoctrain-i18n -f kdeedu-kvoctrain-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-kwordquiz-i18n -f kdeedu-kwordquiz-i18n.lang
%defattr(644,root,root,755)
%files -n kdeedu-libkdeeduui-i18n -f kdeedu-libkdeeduui-i18n.lang
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
%files -n kdegames-knetwalk-i18n -f kdegames-knetwalk-i18n.lang
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
%lang(da) %{_datadir}/apps/ktuberling/sounds/da
%lang(de) %{_datadir}/apps/ktuberling/sounds/de
%lang(es) %{_datadir}/apps/ktuberling/sounds/es
%lang(fr) %{_datadir}/apps/ktuberling/sounds/fr
%lang(it) %{_datadir}/apps/ktuberling/sounds/it
%lang(nds) %{_datadir}/apps/ktuberling/sounds/nds
%lang(nl) %{_datadir}/apps/ktuberling/sounds/nl
%lang(pt) %{_datadir}/apps/ktuberling/sounds/pt
%lang(ro) %{_datadir}/apps/ktuberling/sounds/ro
%lang(sk) %{_datadir}/apps/ktuberling/sounds/sk
%lang(sl) %{_datadir}/apps/ktuberling/sounds/sl
%lang(sr) %{_datadir}/apps/ktuberling/sounds/sr
%lang(sr@Latn) %{_datadir}/apps/ktuberling/sounds/sr@Latn
%lang(sv) %{_datadir}/apps/ktuberling/sounds/sv

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
%files -n kdegraphics-kviewshell-i18n -f kdegraphics-kviewshell-i18n.lang
%defattr(644,root,root,755)

%files -n kdelibs-i18n -f kdelibs-i18n.lang
%defattr(644,root,root,755)
# package dirs
%dir %{_kdedocdir}/ca
%dir %{_kdedocdir}/da
%dir %{_kdedocdir}/de
%dir %{_kdedocdir}/cs
%dir %{_kdedocdir}/es
%dir %{_kdedocdir}/et
%dir %{_kdedocdir}/fi
%dir %{_kdedocdir}/eu
%dir %{_kdedocdir}/fr
%dir %{_kdedocdir}/he
%dir %{_kdedocdir}/hr
%dir %{_kdedocdir}/hu
%dir %{_kdedocdir}/ja
%dir %{_kdedocdir}/it
%dir %{_kdedocdir}/ko
%dir %{_kdedocdir}/nl
%dir %{_kdedocdir}/pl
%dir %{_kdedocdir}/pt
%dir %{_kdedocdir}/ro
%dir %{_kdedocdir}/ru
%dir %{_kdedocdir}/sk
%dir %{_kdedocdir}/sl
%dir %{_kdedocdir}/sr
%dir %{_kdedocdir}/sv
%dir %{_kdedocdir}/tr
%dir %{_kdedocdir}/uk
%dir %{_kdedocdir}/en_GB
%dir %{_kdedocdir}/pt_BR
%dir %{_kdedocdir}/zh_CN
%dir %{_kdedocdir}/zh_TW

# /apps/katepart/syntax/ is in kdelibs package, so kdepart therefore here too
%lang(ca) %{_datadir}/apps/katepart/syntax/logohighlightstyle.ca.xml
%lang(de_DE) %{_datadir}/apps/katepart/syntax/logohighlightstyle.de_DE.xml
%lang(en_GB) %{_datadir}/apps/katepart/syntax/logohighlightstyle.en_GB.xml
%lang(es) %{_datadir}/apps/katepart/syntax/logohighlightstyle.es.xml
%lang(fr_FR) %{_datadir}/apps/katepart/syntax/logohighlightstyle.fr_FR.xml
%lang(it) %{_datadir}/apps/katepart/syntax/logohighlightstyle.it.xml
%lang(mk) %{_datadir}/apps/katepart/syntax/logohighlightstyle.mk.xml
%lang(nl) %{_datadir}/apps/katepart/syntax/logohighlightstyle.nl.xml
%lang(pl) %{_datadir}/apps/katepart/syntax/logohighlightstyle.pl.xml
%lang(pt_BR) %{_datadir}/apps/katepart/syntax/logohighlightstyle.pt_BR.xml
%lang(ru) %{_datadir}/apps/katepart/syntax/logohighlightstyle.ru.xml
%lang(sk) %{_datadir}/apps/katepart/syntax/logohighlightstyle.sk.xml
%lang(sl) %{_datadir}/apps/katepart/syntax/logohighlightstyle.sl.xml
%lang(sr) %{_datadir}/apps/katepart/syntax/logohighlightstyle.sr.xml
%lang(sr@Latn) %{_datadir}/apps/katepart/syntax/logohighlightstyle.sr@Latn.xml
%lang(sv) %{_datadir}/apps/katepart/syntax/logohighlightstyle.sv.xml

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
%files -n kdenetwork-kdnssd-i18n -f kdenetwork-kdnssd-i18n.lang
%defattr(644,root,root,755)
%files -n kdenetwork-kfile-torrent-i18n -f kdenetwork-kfile-torrent-i18n.lang
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
%files -n kdesdk-kapptemplate-i18n -f kdesdk-kapptemplate-i18n.lang
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
%files -n kdesdk-scripts-developer-i18n -f kdesdk-scripts-developer-i18n.lang
%defattr(644,root,root,755)
%files -n kdesdk-umbrello-i18n -f kdesdk-umbrello-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-amor-i18n -f kdetoys-amor-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-fifteen-i18n -f kdetoys-fifteen-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-kmoon-i18n -f kdetoys-kmoon-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-kodo-i18n -f kdetoys-kodo-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-kteatime-i18n -f kdetoys-kteatime-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-ktux-i18n -f kdetoys-ktux-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-kweather-i18n -f kdetoys-kweather-i18n.lang
%defattr(644,root,root,755)
%files -n kdetoys-kworldclock-i18n -f kdetoys-kworldclock-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-ark-i18n -f kdeutils-ark-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kcalc-i18n -f kdeutils-kcalc-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kcharselect-i18n -f kdeutils-kcharselect-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdelirc-i18n -f kdeutils-kdelirc-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdessh-i18n -f kdeutils-kdessh-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kdf-i18n -f kdeutils-kdf-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kedit-i18n -f kdeutils-kedit-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kfloppy-i18n -f kdeutils-kfloppy-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kgpg-i18n -f kdeutils-kgpg-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-khexedit-i18n -f kdeutils-khexedit-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kjots-i18n -f kdeutils-kjots-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-klaptopdaemon-i18n -f kdeutils-klaptopdaemon-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kmilo-i18n -f kdeutils-kmilo-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kregexpeditor-i18n -f kdeutils-kregexpeditor-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-ksim-i18n -f kdeutils-ksim-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-ktimer-i18n -f kdeutils-ktimer-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-kwalletmanager-i18n -f kdeutils-kwalletmanager-i18n.lang
%defattr(644,root,root,755)
%files -n kdeutils-superkaramba-i18n -f kdeutils-superkaramba-i18n.lang
%defattr(644,root,root,755)
%files -n kdevelop-i18n -f kdevelop-i18n.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kfilereplace-i18n -f kdewebdev-kfilereplace-i18n.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kimagemapeditor-i18n -f kdewebdev-kimagemapeditor-i18n.lang
%defattr(644,root,root,755)
%files -n kdewebdev-klinkstatus-i18n -f kdewebdev-klinkstatus-i18n.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kommander-i18n -f kdewebdev-kommander-i18n.lang
%defattr(644,root,root,755)
%files -n kdewebdev-kxsldbg-i18n -f kdewebdev-kxsldbg-i18n.lang
%defattr(644,root,root,755)
%files -n kdewebdev-quanta-i18n -f kdewebdev-quanta-i18n.lang
%defattr(644,root,root,755)
%files -n kdm-i18n -f kdm-i18n.lang
%defattr(644,root,root,755)
%files -n konqueror-i18n -f konqueror-i18n.lang
%defattr(644,root,root,755)
%files -n konqueror-libs-i18n -f konqueror-libs-i18n.lang
%defattr(644,root,root,755)
