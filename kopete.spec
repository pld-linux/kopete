Summary:	Multi-protocol plugin-based instant messenger
Summary(pl):	Komunikator obs�uguj�cy wiele protoko��w
Name:		kopete
Version:	0.10.3
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kopete/%{name}-%{version}.tar.bz2
# Source0-md5:	b071261d701968aace308a3b435ecf4b
Patch0:		%{name}-includehints.patch
URL:		http://kopete.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
#BuildRequires:	libpsi-devel >= 20021108
BuildRequires:	libgadu-devel >= 1.0
BuildRequires:	libxml2-devel >= 2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	kdemultimedia-devel >= 3.1
BuildRequires:	kdemultimedia-kscd >= 3.1
BuildRequires:	kdemultimedia-noatun >= 3.1
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xmms-devel >= 1.0.0
Requires:	kdelibs >= 3.0.9
Requires:	perl-modules
Requires:	qt >= 3.1
Obsoletes:	kopete-plugin-tools-autoaway
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kopete is a flexible and extendable multiple protocol instant
messaging system designed as a plugin-based system. All protocols are
plugins and allow modular installment, configuration, and usage
without the main application knowing anything about the plugin being
loaded. The goal of Kopete is to provide users with a standard and
easy to use interface between all of their instant messaging systems,
but at the same time also providing developers with the ease of
writing plugins to support a new protocol. The core Kopete development
team provides a handful of plugins that most users can use, in
addition to templates for new developers to base a plugin off of.

%description -l pl
Kopete to rozszerzalny i rozbudowywalny komunikator obs�uguj�cy wiele
protoko��w, zaprojektowany w oparciu o wtyczki. Wszystkie protoko�y s�
wtyczkami, co pozwala na modularn� instalacj�, konfiguracj� i u�ywanie
bez potrzeby obs�ugi �adowanych wtyczek w g��wnej aplikacji. Celem
Kopete jest wyposa�enie u�ytkownik�w w standardowy i �atwy w u�yciu
interfejs pomi�dzy wszystkimi systemami komunikator�w, a jednocze�nie
zapewenienie programistom �atwo�ci pisania wtyczek obs�uguj�cych nowe
protoko�y. Za�oga programist�w Kopete udost�pnia podr�czny zestaw
wtyczek u�ywanych przez wi�kszo�� u�ytkownik�w oraz szablony dla
nowych programist�w, na kt�rych mo�na opiera� nowe wtyczki.

%package devel
Summary:	kopete - header files
Summary(pl):	kopete - pliki nag��wkowe do kopete
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files for kopete.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe potrzebn� przy pisaniu w�asnych
program�w wykorzystuj�cych kopete.

%package plugin-tools-autoreplace
Summary:	Autoreplaces some text you can choose
Summary(pl):	Wtyczka automatycznej zamiany tekstu
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-autoreplace
Autoreplaces some text you can choose.

%description plugin-tools-autoreplace -l pl
Wtyczka automatycznej zamiany tekstu.

%package plugin-tools-conectionstatus
Summary:	Internet connection detector
Summary(pl):	Wykrywacz po��cze� internetowych
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-conectionstatus
Automatically detects whether the internet connection is available or
not.

%description plugin-tools-conectionstatus -l pl
Automatycznie sprawdza czy dost�pne jest po��czenie do internetu czy
nie.

%package plugin-tools-contactnotes
Summary:	Add personal notes to your contacts
Summary(pl):	Dodawanie notatek do kontakt�w
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-contactnotes
Allows adding personal notes to your contacts.

%description plugin-tools-contactnotes -l pl
Umo�liwia dodawanie notatek do kontakt�w.

%package plugin-tools-cryptography
Summary:	Messages encryptor
Summary(pl):	Program do szyfrowania wiadomo�ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-cryptography
OpenPGP messages encryptor.

%description plugin-tools-cryptography -l pl
Program do szyfrowania wiadomo�ci przy pomocy OpenPGP.

%package plugin-tools-history
Summary:	A history plugin
Summary(pl):	Wtyczka obs�uguj�ca histori� rozm�w
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-history
A history plugin.

%description plugin-tools-history -l pl
Wtyczka obs�uguj�ca histori� rozm�w.

%package plugin-tools-highlight
Summary:	A highlighter plugin
Summary(pl):	Wtyczka podkre�laj�ca wybrane teksty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-highlight
A highlighter plugin.

%description plugin-tools-highlight -l pl
Wtyczka podkre�laj�ca wybrane teksty.

%package plugin-tools-nowlistening
Summary:	Playlist informer
Summary(pl):	Informator o playliscie
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xmms >= 1.0.0
Requires:	kdemultimedia-noatun >= 3.1
Requires:	kdemultimedia-kscd >= 3.1

%description plugin-tools-nowlistening
This plugin tells selected live chats what you're currently listening
to in xmms/kscd/noatun.

%description plugin-tools-nowlistening -l pl
Ta wtyczka wypisuje podczas rozmow nazw� aktualnie s�uchanej piosenki
w xmms/kscd/noatun.

%package plugin-tools-texteffect
Summary:	A plugin that adds nice effects to your messages
Summary(pl):	Wtyczka dodaj�ca �adne efekty do twoich wiadomo�ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-texteffect
A plugin that adds nice effects to your messages.

%description plugin-tools-texteffect -l pl
Wtyczka dodaj�ca �adne efekty do twoich wiadomo�ci.

%package plugin-tools-translator
Summary:	Uses babelfish to translate messages
Summary(pl):	Wykorzystuje babelfish do t�umaczenia wiadomo�ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-translator
This plugin uses babelfish to translate messages.

%description plugin-tools-translator -l pl
Ta wtyczka wykorzystuje babelfish do t�umaczenia wiadomo�ci.

%package plugin-tools-webpresence
Summary:	Web contactlist presenter
Summary(pl):	Wy�wietlacz listy kontakt�w na WWW
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libxml2 >= 2.4.8
Requires:	libxslt >= 1.0.7

%description plugin-tools-webpresence
This plugin shows the status of (parts of) your contactlist on a
webpage.

%description plugin-tools-webpresence -l pl
Ta wtyczka pokazuje status (ca�ej lub cze�ci) listy kontakt�w na
stronie WWW.

%package plugin-protocols-aim
Summary:	Adds AIM protocol support
Summary(pl):	Dodaje obs�ug� protoko�u AIM
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-aim
Adds AIM protocol support.

%description plugin-protocols-aim -l pl
Dodaje obs�ug� protoko�u AIM.

%package plugin-protocols-gg
Summary:	Adds GaduGadu protocol support
Summary(pl):	Dodaje obs�ug� protoko�u GaduGadu
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-gg
Adds GaguGadu protocol support.

%description plugin-protocols-gg -l pl
Dodaje obs�ug� protoko�u GaduGadu.

%package plugin-protocols-icq
Summary:	Adds ICQ protocol support
Summary(pl):	Dodaje obs�ug� protoko�u ICQ
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-icq
Adds ICQ protocol support.

%description plugin-protocols-icq -l pl
Dodaje obs�ug� protoko�u ICQ.

%package plugin-protocols-irc
Summary:	Adds IRC support
Summary(pl):	Dodaje obs�ug� IRC
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-irc
Adds IRC support.

%description plugin-protocols-irc -l pl
Dodaje obs�ug� IRC.

%package plugin-protocols-jabber
Summary:	Adds Jabber protocol support
Summary(pl):	Dodaje obs�ug� protoko�u Jabber
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libpsi >= 20021108

%description plugin-protocols-jabber
Adds Jabber protocol support.

%description plugin-protocols-jabber -l pl
Dodaje obs�ug� protoko�u Jabber.

%package plugin-protocols-msn
Summary:	Adds MSN protocol support
Summary(pl):	Dodaje obs�ug� protoko�u MSN
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-msn
Adds MSN protocol support.

%description plugin-protocols-msn -l pl
Dodaje obs�ug� protoko�u MSN.

%package plugin-protocols-sms
Summary:	Adds SMS contact support
Summary(pl):	Dodaje obs�ug� kontakt�w SMS
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-sms
Adds SMS contact support.

%description plugin-protocols-sms -l pl
Dodaje obs�ug� kontakt�w SMS.

%package plugin-protocols-yahoo
Summary:	Adds yahoo protocol support
Summary(pl):	Dodaje obs�ug� protoko�u yahoo
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-yahoo
Adds yahoo protocol support.

%description plugin-protocols-yahoo -l pl
Dodaje obs�ug� protoko�u yahoo.

%package plugin-protocols-groupwise
Summary:	Adds groupwise protocol support
Summary(pl):	Dodaje obs�ug� protoko�u groupwise
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-groupwise
Adds groupwise protocol support.

%description plugin-protocols-groupwise -l pl
Dodaje obs�ug� protoko�u groupwise.

%prep
%setup -q
%patch -p1

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo "Categories=Qt;Network;X-Communication" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kopete.desktop
install -d $RPM_BUILD_ROOT%{_iconsdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kopete
%dir %{_libdir}/kconf_update_bin
%attr(755,root,root) %{_libdir}/kconf_update_bin/*
%attr(755,root,root) %{_libdir}/libkopete*.so.*
%dir %{_datadir}/services/kconfiguredialog/
%{_datadir}/services/kconfiguredialog/*

%{_desktopdir}/kde/kopete.desktop
%{_datadir}/apps/kconf_update/*
%{_iconsdir}/*
%{_datadir}/sounds/*
%dir %{_datadir}/apps/kopete
%{_datadir}/apps/kopete/*rc
%{_datadir}/apps/kopete/styles/*
%dir %{_datadir}/apps/kopete/pics
%{_datadir}/mimelnk/application/x-kopete-emoticons.desktop
%{_datadir}/apps/kopete/icons/*/*/*/emoticon.png
%{_datadir}/apps/kopete/icons/*/*/*/kopeteavailable.png
%{_datadir}/apps/kopete/icons/*/*/*/kopeteaway.png
%{_datadir}/apps/kopete/icons/*/*/*/status_unknown.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_away.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_offline.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_online.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_unknown.png
%{_datadir}/apps/kopete/icons/*/*/*/newmsg.png
%{_datadir}/apps/kopete/icons/*/*/*/newmessage.mng
%{_datadir}/apps/kopete/icons/*/*/*/account_offline_overlay.svgz
%{_datadir}/apps/kopete/icons/*/*/*/account_offline_overlay.png
%{_datadir}/services/kopete_accountconfig.desktop
%{_datadir}/apps/kopete/icons/*/*/*/logging.png
%{_datadir}/servicetypes/kopeteplugin.desktop
%{_datadir}/servicetypes/kopeteprotocol.desktop
%{_datadir}/services/kopete_addbookmarks.desktop
%{_datadir}/services/kopete_alias.desktop

%{_datadir}/services/kopete_appearanceconfig.desktop
%{_datadir}/services/kopete_behaviorconfig.desktop

#latex
%attr(755,root,root) %{_bindir}/kopete_latexconvert.sh
%{_datadir}/services/kopete_latex.desktop
%{_datadir}/config.kcfg/latexconfig.kcfg
%{_datadir}/apps/kopete/icons/*/*/*/latex.png

#richtext
%attr(755,root,root) %{_libdir}/kde3/libkrichtexteditpart.la
%attr(755,root,root) %{_libdir}/kde3/libkrichtexteditpart.so
%dir %{_datadir}/apps/kopeterichtexteditpart
%{_datadir}/apps/kopeterichtexteditpart/*

#netmeeting
%{_datadir}/services/kopete_netmeeting.desktop
%dir %{_datadir}/apps/kopete_netmeeting
%{_datadir}/apps/kopete_netmeeting/*

%{_datadir}/services/kopete_statistics.desktop
%dir %{_datadir}/apps/kopete_statistics
%{_datadir}/apps/kopete_statistics/*
%{_datadir}/apps/kopete/pics/statistics/black.png
%{_datadir}/apps/kopete/pics/statistics/blue.png
%{_datadir}/apps/kopete/pics/statistics/gray.png
%{_datadir}/apps/kopete/pics/statistics/navy.png

%{_datadir}/servicetypes/kopeteui.desktop

%{_datadir}/apps/kopete/icons/*/*/*/kgpg_key?.png
%{_datadir}/services/chatwindow.desktop
%{_datadir}/services/emailwindow.desktop

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/kopete
%{_includedir}/kopete/*.h
%dir %{_includedir}/kopete/ui
%{_includedir}/kopete/ui/*.h

%files plugin-tools-autoreplace
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*autoreplace*.so
%{_libdir}/kde3/kopete*autoreplace*.la
%{_datadir}/services/kopete_autoreplace.desktop
%{_datadir}/apps/kopete/icons/*/*/*/autoreplace.png

%files plugin-tools-conectionstatus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*connectionstatus*.so
%{_libdir}/kde3/kopete*connectionstatus*.la
%{_datadir}/services/kopete_connectionstatus.desktop

%files plugin-tools-contactnotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*contactnotes*.so
%{_libdir}/kde3/kopete*contactnotes*.la
%{_datadir}/services/kopete_contactnotes.desktop
%dir %{_datadir}/apps/kopete_contactnotes
%{_datadir}/apps/kopete_contactnotes/*

%files plugin-tools-cryptography
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*cryptography*.so
%{_libdir}/kde3/kopete*cryptography*.la
%{_datadir}/services/kopete_cryptography.desktop
%dir %{_datadir}/apps/kopete_cryptography
%{_datadir}/apps/kopete_cryptography/*

%files plugin-tools-history
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*history*.so
%{_libdir}/kde3/kopete*history*.la
%{_datadir}/services/kopete_history.desktop
%dir %{_datadir}/apps/kopete_history
%{_datadir}/apps/kopete_history/*
%{_datadir}/config.kcfg/historyconfig.kcfg

%files plugin-tools-highlight
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*highlight*.so
%{_libdir}/kde3/kopete*highlight*.la
%{_datadir}/services/kopete_highlight.desktop
%{_datadir}/apps/kopete/icons/*/*/*/highlight.png

%files plugin-tools-nowlistening
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*nowlistening*.so
%{_libdir}/kde3/kopete*nowlistening*.la
%{_datadir}/services/kopete_nowlistening.desktop

%files plugin-tools-texteffect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*texteffect*.so
%{_libdir}/kde3/kopete*texteffect*.la
%{_datadir}/services/kopete_texteffect.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/texteffect.png

%files plugin-tools-translator
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*translator*.so
%{_libdir}/kde3/kopete*translator*.la
%{_datadir}/services/kopete_translator.desktop
%dir %{_datadir}/apps/kopete_translator
%{_datadir}/apps/kopete_translator/*

%files plugin-tools-webpresence
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*webpresence*.so
%{_libdir}/kde3/kopete*webpresence*.la
%{_datadir}/services/kopete_webpresence.desktop
%{_datadir}/apps/kopete/webpresence/webpresencedefault.xsl
%{_datadir}/apps/kopete/webpresence/wpimages.xsl

%files plugin-protocols-aim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*aim*.so
%{_libdir}/kde3/kopete*aim*.la
%{_datadir}/services/aim.protocol
%{_datadir}/apps/kopete/icons/hicolor/*/*/aim*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/aim*
%{_datadir}/services/kopete_aim.desktop

%files plugin-protocols-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*gadu*.so
%{_libdir}/kde3/kopete*gadu*.la
%{_datadir}/services/kopete_gadu.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gg*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gadu*

%files plugin-protocols-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*icq*.so
%{_libdir}/kde3/kopete*icq*.la
%{_datadir}/services/kopete_icq.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/icq*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/icq*
%{_datadir}/mimelnk/application/x-icq.desktop

%files plugin-protocols-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*irc*.so
%{_libdir}/kde3/kopete*irc*.la
%{_datadir}/services/irc.protocol
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/irc*
%{_datadir}/services/kopete_irc.desktop
%{_datadir}/apps/kopete/ircnetworks.xml

%files plugin-protocols-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*jabber*.so
%{_libdir}/kde3/kopete*jabber*.la
%{_datadir}/services/kopete_jabber.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/jabber*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/jabber*

%files plugin-protocols-msn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*msn*.so
%{_libdir}/kde3/kopete*msn*.la
%{_datadir}/services/kopete_msn.desktop
%{_datadir}/apps/kopete/icons/*/*/*/msn*
%dir %{_datadir}/apps/kopete_msn
%{_datadir}/apps/kopete_msn/*

%files plugin-protocols-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*sms*.so
%{_libdir}/kde3/kopete*sms*.la
%{_datadir}/services/kopete_sms.desktop
%{_datadir}/apps/kopete/icons/*/*/*/sms*

%files plugin-protocols-yahoo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete_yahoo*.so
%{_libdir}/kde3/kopete_yahoo*.la
%{_datadir}/services/kopete_yahoo.desktop
%{_datadir}/apps/kopete/icons/*/*/*/yahoo*

%files plugin-protocols-groupwise
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete_groupwise*so
%{_datadir}/apps/kopete/icons/*/*/*/groupwise*
%{_datadir}/services/kopete_groupwise.desktop
%dir %{_datadir}/apps/kopete_groupwise
%{_datadir}/apps/kopete_groupwise/*
