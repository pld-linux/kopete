Summary:	Multi-protocol plugin-based instant messenger
Summary(pl):	Komunikator obs³uguj±cy wiele protoko³ów
Name:		kopete
Version:	0.7.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a245854fa1d17198e2559513a3315ed2
URL:		http://kopete.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
Buildrequires:	libpsi-devel >= 20021108
BuildRequires:	libgadu-devel >= 1.0
BuildRequires:	libxml2-devel >= 2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	kdemultimedia-devel >= 3.1
BuildRequires:	kdemultimedia-kscd >= 3.1
BuildRequires:	kdemultimedia-noatun >= 3.1
BuildRequires:	perl-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	xmms-devel >= 1.0.0
BuildRequires:	openssl-devel
Requires:	kdelibs >= 3.0.9
Requires:	perl-modules
Requires:	qt >= 3.1
Obsoletes:	kopete-plugin-tools-autoaway
Obsoletes:	kopete-plugin-tools-importer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

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
Kopete to rozszerzalny i rozbudowywalny komunikator obs³uguj±cy wiele
protoko³ów, zaprojektowany w oparciu o wtyczki. Wszystkie protoko³y s±
wtyczkami, co pozwala na modularn± instalacjê, konfiguracjê i u¿ywanie
bez potrzeby obs³ugi ³adowanych wtyczek w g³ównej aplikacji. Celem
Kopete jest wyposa¿enie u¿ytkowników w standardowy i ³atwy w u¿yciu
interfejs pomiêdzy wszystkimi systemami komunikatorów, a jednocze¶nie
zapewenienie programistom ³atwo¶ci pisania wtyczek obs³uguj±cych nowe
protoko³y. Za³oga programistów Kopete udostêpnia podrêczny zestaw
wtyczek u¿ywanych przez wiêkszo¶æ u¿ytkowników oraz szablony dla
nowych programistów, na których mo¿na opieraæ nowe wtyczki.

%package plugin-tools-autoaway
Summary:	An autoaway plugin
Summary(pl):	Wtyczka automatycznego przej¶cia w stan zajêty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-autoaway
Automatically changes status to away. Conditions are configurable.

%description plugin-tools-autoaway -l pl
Automatycznie zmienia status na zajêty. Warunki, po zaistnieniu
których ma nastapiæ, s± konfigurowalne.

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
Summary(pl):	Wykrywacz po³±czeñ internetowych
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-conectionstatus
Automatically detects whether the internet connection is available or
not.

%description plugin-tools-conectionstatus -l pl
Automatycznie sprawdza czy dostêpne jest po³±czenie do internetu czy
nie.

%package plugin-tools-contactnotes
Summary:	Add personal notes to your contacts
Summary(pl):	Dodawanie notatek do kontaktów
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-contactnotes
Allows adding personal notes to your contacts.

%description plugin-tools-contactnotes  -l pl
Umo¿liwia dodawanie notatek do kontaktów.

%package plugin-tools-cryptography
Summary:	Messages encryptor
Summary(pl):	Program do szyfrowania wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-cryptography
OpenPGP messages encryptor.

%description plugin-tools-cryptography -l pl
Program do szyfrowania wiadomo¶ci przy pomocy OpenPGP.


%package plugin-tools-history
Summary:	A history plugin
Summary(pl):	Wtyczka obs³uguj±ca historiê rozmów
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-history
A history plugin.

%description plugin-tools-history -l pl
Wtyczka obs³uguj±ca historiê rozmów.

%package plugin-tools-highlight
Summary:	A highlighter plugin
Summary(pl):	Wtyczka podkre¶laj±ca wybrane teksty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-highlight
A highlighter plugin.

%description plugin-tools-highlight -l pl
Wtyczka podkre¶laj±ca wybrane teksty.


%package plugin-tools-importer
Summary:	Contact importer
Summary(pl):	Importer kontaktów
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-importer
Allows importing contacts from other IM's.

%description plugin-tools-importer -l pl
Umo¿liwia importowanie kontaktów z innych komunikatorów.

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
Ta wtyczka wypisuje podczas rozmow nazwê aktualnie s³uchanej piosenki
w xmms/kscd/noatun.

%package plugin-tools-motionaway
Summary:	Sets away status when not detecting movement near the computer
Summary(pl):	Zmienia status na zajêty je¶li nie wykrywa ruchu wokó³ komputera
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-motionaway
This plugin sets away status when not detecting movement near the
computer.

%description plugin-tools-motionaway -l pl
Ta wtyczka zmienia status na zajêty je¶li nie wykrywa ruchu wokó³
komputera.

%package plugin-tools-spellcheck
Summary:	A spell checking plugin.
Summary(pl):	Wtyczka sprawdzaj±ca pisownie.
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-spellcheck
A spell checking plugin.

%description plugin-tools-spellcheck -l pl
Wtyczka sprawdzaj±ca pisownie.


%package plugin-tools-texteffect
Summary:	A plugin that adds nice effects to your messages
Summary(pl):	Wtyczka dodaj±ca ³adne efekty do twoich wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-texteffect
A plugin that adds nice effects to your messages.

%description plugin-tools-texteffect -l pl
Wtyczka dodaj±ca ³adne efekty do twoich wiadomo¶ci.

%package plugin-tools-translator
Summary:	Uses babelfish to translate messages
Summary(pl):	Wykorzystuje babelfish do t³umaczenia wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-tools-translator
This plugin uses babelfish to translate messages.

%description plugin-tools-translator -l pl
Ta wtyczka wykorzystuje babelfish do t³umaczenia wiadomo¶ci.

%package plugin-tools-webpresence
Summary:	Web contactlist presenter
Summary(pl):	Wy¶wietlacz listy kontaktów na WWW
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libxml2 >= 2.4.8
Requires:	libxslt >= 1.0.7

%description plugin-tools-webpresence
This plugin shows the status of (parts of) your contactlist on a
webpage.

%description plugin-tools-webpresence -l pl
Ta wtyczka pokazuje status (ca³ej lub cze¶ci) listy kontaktów na
stronie WWW.

%package plugin-protocols-aim
Summary:	Adds AIM protocol support
Summary(pl):	Dodaje obs³ugê protoko³u AIM
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-aim
Adds AIM protocol support.

%description plugin-protocols-aim -l pl
Dodaje obs³ugê protoko³u AIM.

%package plugin-protocols-gg
Summary:	Adds GaduGadu protocol support
Summary(pl):	Dodaje obs³ugê protoko³u GaduGadu
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-gg
Adds GaguGadu protocol support.

%description plugin-protocols-gg -l pl
Dodaje obs³ugê protoko³u GaduGadu.

%package plugin-protocols-icq
Summary:	Adds ICQ protocol support
Summary(pl):	Dodaje obs³ugê protoko³u ICQ
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-icq
Adds ICQ protocol support.

%description plugin-protocols-icq -l pl
Dodaje obs³ugê protoko³u ICQ.

%package plugin-protocols-irc
Summary:	Adds IRC support
Summary(pl):	Dodaje obs³ugê IRC
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-irc
Adds IRC support.

%description plugin-protocols-irc -l pl
Dodaje obs³ugê IRC.

%package plugin-protocols-jabber
Summary:	Adds Jabber protocol support
Summary(pl):	Dodaje obs³ugê protoko³u Jabber
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libpsi >= 20021108

%description plugin-protocols-jabber
Adds Jabber protocol support.

%description plugin-protocols-jabber -l pl
Dodaje obs³ugê protoko³u Jabber.

%package plugin-protocols-msn
Summary:	Adds MSN protocol support
Summary(pl):	Dodaje obs³ugê protoko³u MSN
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-msn
Adds MSN protocol support.

%description plugin-protocols-msn -l pl
Dodaje obs³ugê protoko³u MSN.

%package plugin-protocols-oscar
Summary:	Adds OSCAR protocol support
Summary(pl):	Dodaje obs³ugê protoko³u OSCAR
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-oscar
Adds OSCAR protocol support.

%description plugin-protocols-oscar -l pl
Dodaje obs³ugê protoko³u OSCAR.

%package plugin-protocols-sms
Summary:	Adds SMS contact support
Summary(pl):	Dodaje obs³ugê kontaktów SMS
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-sms
Adds SMS contact support.

%description plugin-protocols-sms -l pl
Dodaje obs³ugê kontaktów SMS.

%package plugin-protocols-winpopup
Summary:	Adds winpopup messaging support
Summary(pl):	Dodaje obs³ugê komunikacji via winpopup
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-winpopup
Adds winpopup messaging support.

%description plugin-protocols-winpopup -l pl
Dodaje obs³ugê komunikacji via winpopup.

%package plugin-protocols-yahoo
Summary:	Adds yahoo protocol support
Summary(pl):	Dodaje obs³ugê protoko³u yahoo
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocols-yahoo
Adds yahoo protocol support.

%description plugin-protocols-yahoo -l pl
Dodaje obs³ugê protoko³u yahoo.

%prep
%setup -q

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_desktopdir}/{Internet/,}kopete.desktop
echo "Categories=Qt;Network;X-Communication" >> $RPM_BUILD_ROOT%{_desktopdir}/kopete.desktop
install -d $RPM_BUILD_ROOT%{_iconsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kopete
%dir %{_bindir}/kconf_update_bin/
%attr(755,root,root) %{_bindir}/kconf_update_bin/kopete-account-kconf_update
%attr(755,root,root) %{_libdir}/libkopete*.so*
# Theeese must get removed sooner or later
%attr(755,root,root) %{_libdir}/kde3/libkrichtexteditpart.so
%{_libdir}/kde3/libkrichtexteditpart.la
%{_datadir}/apps/krichtexteditpart/krichtexteditpartui.rc
#/

%{_desktopdir}/kopete.desktop
%{_datadir}/apps/kconf_update/*
%{_iconsdir}/*
%{_datadir}/sounds/*
%dir %{_datadir}/apps/kopete
%{_datadir}/apps/kopete/*rc
%{_datadir}/apps/kopete/styles/*
#%%{_datadir}/apps/kopete/*.html
%dir %{_datadir}/apps/kopete/pics
#%%{_datadir}/apps/kopete/icons/hicolor/*/*/addside.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/admin_icon.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/aol_icon.png
#{_datadir}/apps/kopete/icons/hicolor/*/*/away-mobile.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/dt_icon.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/emoticon.png
%{_datadir}/apps/kopete/pics/emoticons
%{_datadir}/apps/kopete/icons/hicolor/*/*/free_icon.png
#%%{_datadir}/apps/kopete/icons/hicolor/*/*/history.png
%{_datadir}/apps/kopete/icons/*/*/*/kopeteavailable.png
%{_datadir}/apps/kopete/icons/*/*/*/kopeteaway.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/status_unknown.png
#%%{_datadir}/apps/kopete/icons/*/*/*/kopetestatus.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/metacontact_away.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/metacontact_offline.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/metacontact_online.png
#%%{_datadir}/apps/kopete/icons/hicolor/*/*/mobile.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/newmsg.png
#%%{_datadir}/apps/kopete/icons/hicolor/*/*/offline-mobile.png
#%%{_datadir}/apps/kopete/icons/hicolor/*/*/online-mobile.png
%{_datadir}/apps/kopete/icons/hicolor/*/*/metacontact_unknown.png
%{_datadir}/apps/kopete/pics/newmessage.mng
%{_datadir}/servicetypes/kopeteplugin.desktop
%{_datadir}/servicetypes/kopeteprotocol.desktop

#%%files plugin-tools-autoaway
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/kde3/kopete*autoaway*.*
#%%{_datadir}/apps/kopete/autoaway.desktop

%files plugin-tools-autoreplace
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*autoreplace*.so
%{_libdir}/kde3/kopete*autoreplace*.la
%{_datadir}/services/autoreplace.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/autoreplace.png

%files plugin-tools-conectionstatus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*connectionstatus*.so
%{_libdir}/kde3/kopete*connectionstatus*.la
%{_datadir}/services/connectionstatus.desktop

%files plugin-tools-contactnotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*contactnotes*.so
%{_libdir}/kde3/kopete*contactnotes*.la
%{_datadir}/services/contactnotes.desktop

%files plugin-tools-cryptography
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*cryptography*.so
%{_libdir}/kde3/kopete*cryptography*.la
%{_datadir}/services/cryptography.desktop

%files plugin-tools-history
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*history*.so
%{_libdir}/kde3/kopete*history*.la
%{_datadir}/services/history.desktop
#%%{_datadir}/apps/kopete/icons/hicolor/*/*/history.png

%files plugin-tools-highlight
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*highlight*.so
%{_libdir}/kde3/kopete*highlight*.la
%{_datadir}/services/highlight.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/highlight.png

#%%files plugin-tools-importer
#%%defattr(644,root,root,755)
#%%attr(755,root,root)  %{_libdir}/kde3/kopete*importer*.so*
#%%{_libdir}/kde3/kopete*importer*.la
#%{_datadir}/apps/kopete/importer.desktop

%files plugin-tools-nowlistening
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/kde3/kopete*nowlistening*.so
%{_libdir}/kde3/kopete*nowlistening*.la
%{_datadir}/services/nowlistening.desktop

%files plugin-tools-motionaway
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*motionaway*.so
%{_libdir}/kde3/kopete*motionaway*.la
%{_datadir}/services/motionaway.desktop

%files plugin-tools-spellcheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*spellcheck*.so
%{_libdir}/kde3/kopete*spellcheck*.la
%{_datadir}/services/spellcheck.desktop


%files plugin-tools-texteffect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*texteffect*.so
%{_libdir}/kde3/kopete*texteffect*.la
%{_datadir}/services/texteffect.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/texteffect.png

%files plugin-tools-translator
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*translator*.so
%{_libdir}/kde3/kopete*translator*.la
%{_datadir}/services/translator.desktop

%files plugin-tools-webpresence
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*webpresence*.so
%{_libdir}/kde3/kopete*webpresence*.la
%{_datadir}/services/webpresence.desktop
%{_datadir}/apps/kopete/webpresence/webpresencedefault.xsl
%{_datadir}/apps/kopete/webpresence/wpimages.xsl

%files plugin-protocols-aim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*aim*.so
%{_libdir}/kde3/kopete*aim*.la
%{_datadir}/services/aim.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/aim*
%{_datadir}/apps/kopete/pics/aim*

%files plugin-protocols-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*gadu*.so
%{_libdir}/kde3/kopete*gadu*.la
%{_datadir}/services/gadu.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/gadu*
%{_datadir}/apps/kopete/pics/gg*

%files plugin-protocols-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*icq*.so
%{_libdir}/kde3/kopete*icq*.la
%{_datadir}/services/icq.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/icq*
%{_datadir}/apps/kopete/pics/icq*

%files plugin-protocols-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*irc*.so
%{_libdir}/kde3/kopete*irc*.la
%{_datadir}/services/irc.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/irc*
%{_datadir}/apps/kopete/pics/irc_connecting.mng

%files plugin-protocols-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*jabber*.so
%{_libdir}/kde3/kopete*jabber*.la
%{_datadir}/services/jabber.desktop
%{_datadir}/apps/kopete/pics/jabber*
%{_datadir}/apps/kopete/icons/hicolor/*/*/jabber*

%files plugin-protocols-msn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*msn*.so
%{_libdir}/kde3/kopete*msn*.la
%{_datadir}/services/msn.desktop
%{_datadir}/apps/kopete/pics/msn*
%{_datadir}/apps/kopete/icons/*/*/*/msn*

%files plugin-protocols-oscar
%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/kde3/kopete*oscar*.*
#%{_datadir}/apps/kopete/oscar.desktop
#%%%{_datadir}/apps/kopete/pics/oscar*

%files plugin-protocols-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*sms*.so
%{_libdir}/kde3/kopete*sms*.la
%{_datadir}/services/sms.desktop
%{_datadir}/apps/kopete/icons/*/*/*/sms*

%files plugin-protocols-yahoo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete_yahoo*.so
%{_libdir}/kde3/kopete_yahoo*.la
%{_datadir}/services/yahoo.desktop
%{_datadir}/apps/kopete/icons/*/*/*/yahoo*

%files plugin-protocols-winpopup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/winpopup*.sh
%attr(755,root,root) %{_libdir}/kde3/kopete*wp*.so
%{_libdir}/kde3/kopete*wp*.la
%{_datadir}/services/wp.desktop
%{_datadir}/apps/kopete/icons/hicolor/*/*/wp*
