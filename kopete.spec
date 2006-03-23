# TODO:
# - subpackage linphone's oRTP libraries to add Jingle support for jabber
#
# Conditional build:
%bcond_without	xmms
%bcond_without	noatun
%bcond_with	meanwhile	# Kopete Meanwhile plugin (Lotus Sametime support)
%bcond_without	smpppd		# support for the SuSE Meta PPP Daemon (smpppd)
%bcond_without	winpopup
%bcond_without	smsgsm			# GSM SMS protocol
%bcond_without	slp			# don't require libslp (Browsing in krfb and krdc not possible)
%bcond_with		jingle		# enable Jabber Jingle voice support
#
%define		_snap	beta2
Summary:	Multi-protocol plugin-based instant messenger
Summary(pl):	Komunikator obs³uguj±cy wiele protoko³ów
Name:		kopete
Version:	0.12
Release:	0.%{_snap}.6
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kopete/%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	142cd8ddc4dbd5f493e03b80f36ad7ca
Patch0:		%{name}-desktop.patch
URL:		http://kopete.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	glib-devel
%{?with_smsgsm:BuildRequires:	gsmlib-devel}
BuildRequires:	kdemultimedia-devel >= 3.1
BuildRequires:	kdemultimedia-kscd >= 3.1
%{?with_noatun:BuildRequires:	kdemultimedia-noatun >= 3.1}
BuildRequires:	libgadu-devel >= 1.0
#BuildRequires:	libpsi-devel >= 20021108
BuildRequires:	libxml2-devel >= 2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
%{?with_meanwhile:BuildRequires:	meanwhile-devel <= 1.1.0}
%{?with_meanwhile:BuildRequires:	meanwhile-devel >= 1.0.1}
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
%{?with_xmms:BuildRequires:	xmms-devel >= 1.0.0}
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 3.5.
Requires:	perl-modules
Requires:	qt >= 3.1
Provides:	kdenetwork-kopete
Obsoletes:	kdenetwork-kopete
Obsoletes:	kdenetwork-kopete-protocol-testbed
Obsoletes:	kopete-plugin-protocols-aim
Obsoletes:	kopete-plugin-protocols-gg
Obsoletes:	kopete-plugin-protocols-icq
Obsoletes:	kopete-plugin-protocols-irc
Obsoletes:	kopete-plugin-protocols-jabber
Obsoletes:	kopete-plugin-protocols-msn
Obsoletes:	kopete-plugin-protocols-oscar
Obsoletes:	kopete-plugin-protocols-sms
Obsoletes:	kopete-plugin-protocols-winpopup
Obsoletes:	kopete-plugin-protocols-yahoo
Obsoletes:	kopete-plugin-tools-autoaway
Obsoletes:	kopete-plugin-tools-autoreplace
Obsoletes:	kopete-plugin-tools-conectionstatus
Obsoletes:	kopete-plugin-tools-contactnotes
Obsoletes:	kopete-plugin-tools-cryptography
Obsoletes:	kopete-plugin-tools-highlight
Obsoletes:	kopete-plugin-tools-history
Obsoletes:	kopete-plugin-tools-importer
Obsoletes:	kopete-plugin-tools-motionaway
Obsoletes:	kopete-plugin-tools-nowlistening
Obsoletes:	kopete-plugin-tools-spellcheck
Obsoletes:	kopete-plugin-tools-texteffect
Obsoletes:	kopete-plugin-tools-translator
Obsoletes:	kopete-plugin-tools-webpresence
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kopete is a flexible and extendable multiple protocol instant
messaging system designed as a based system. All protocols are plugins
and allow modular installment, configuration, and usage without the
main application knowing anything about the plugin being loaded. The
goal of Kopete is to provide users with a standard and easy to use
interface between all of their instant messaging systems, but at the
same time also providing developers with the ease of writing plugins
to support a new protocol. The core Kopete development team provides a
handful of plugins that most users can use, in addition to templates
for new developers to base a plugin off of.

%description -l pl
Kopete to rozszerzalny i rozbudowywalny komunikator obs³uguj±cy wiele
protoko³ów, zaprojektowany w oparciu o wtyczki. Wszystkie protoko³y s±
wtyczkami, co pozwala na modularn± instalacjê, konfiguracjê i u¿ywanie
bez potrzeby obs³ugi ³adowanych wtyczek w g³ównej aplikacji. Celem
Kopete jest wyposa¿enie u¿ytkowników w standardowy i ³atwy w u¿yciu
interfejs pomiêdzy wszystkimi systemami komunikatorów, a jednocze¶nie
zapewnienie programistom ³atwo¶ci pisania wtyczek obs³uguj±cych nowe
protoko³y. Za³oga programistów Kopete udostêpnia podrêczny zestaw
wtyczek u¿ywanych przez wiêkszo¶æ u¿ytkowników oraz szablony dla
nowych programistów, na których mo¿na opieraæ nowe wtyczki.

%package devel
Summary:	kopete - header files
Summary(pl):	kopete - pliki nag³ówkowe do kopete
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_msn = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_videodevice = %{epoch}:%{version}-%{release}

%description devel
This package contains header files for kopete.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe potrzebn± przy pisaniu w³asnych
programów wykorzystuj±cych kopete.

%package designer
Summary:	kopete - Qt Designer plugins
Summary(pl):	kopete - wtyczki do Qt Designera
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	qt-designer

%description designer
This package contains plugins for Qt Designer.

%description designer -l pl
Pakiet ten zawiera wtyczki do Qt Designera.

%package tool-alias
Summary:	Kopete plugin to add custom aliases for commands
Summary(pl):	Wtyczka Kopete do dodawania w³asnych aliasów dla poleceñ
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-alias
Obsoletes:	kdenetwork-kopete-tool-alias

%description tool-alias
Kopete plugin to add custom aliases for commands.

%description tool-alias -l pl
Wtyczka Kopete do dodawania w³asnych aliasów dla poleceñ.

%package tool-autoaway
Summary:	Kopete autoaway plugin
Summary(pl):	Wtyczka Kopete do automatycznego przechodzenia w stan zajêty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-autoaway
Obsoletes:	kdenetwork-kopete-tool-autoaway

%description tool-autoaway
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description tool-autoaway -l pl
Wtyczka Kopete automatycznie zmieniaj±ca status na zajêty. Warunki, po
zaistnieniu których ma nast±piæ, s± konfigurowalne.

%package tool-autoreplace
Summary:	Kopete plugin which autoreplaces some text you can choose
Summary(pl):	Wtyczka Kopete do automatycznej zamiany tekstu
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-autoreplace
Obsoletes:	kdenetwork-kopete-tool-autoreplace

%description tool-autoreplace
Kopete plugin which autoreplaces some text you can choose.

%description tool-autoreplace -l pl
Wtyczka Kopete do automatycznej zamiany tekstu.

%package tool-avdeviceconfig
Summary:	Kopete avdeviceconfig plugin
Summary(pl):	Wtyczka Kopete do automatycznego przechodzenia w stan zajêty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-avdeviceconfig
Obsoletes:	kdenetwork-kopete-tool-avdeviceconfig

%description tool-avdeviceconfig
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description tool-avdeviceconfig -l pl
Wtyczka Kopete automatycznie zmieniaj±ca status na zajêty. Warunki, po
zaistnieniu których ma nast±piæ, s± konfigurowalne.

%package tool-connectionstatus
Summary:	Kopete Internet connection detector
Summary(pl):	Wykrywacz po³±czeñ internetowych dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-conectionstatus
Obsoletes:	kdenetwork-kopete-tool-conectionstatus

%description tool-connectionstatus
Kopete tool which automatically detects whether the internet
connection is available or not.

%description tool-connectionstatus -l pl
Narzêdzie Kopete automatycznie sprawdzaj±ce, czy dostêpne jest
po³±czenie do Internetu.

%package tool-contactnotes
Summary:	Kopete tool which adds personal notes to your contacts
Summary(pl):	Narzêdzie Kopete do dodawania notatek do kontaktów
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-contactnotes
Obsoletes:	kdenetwork-kopete-tool-contactnotes

%description tool-contactnotes
Kopete tool which allows adding personal notes to your contacts.

%description tool-contactnotes -l pl
Narzêdzie Kopete umo¿liwiaj±ce dodawanie notatek do kontaktów.

%package tool-cryptography
Summary:	Kopete messages encryptor
Summary(pl):	Program do szyfrowania wiadomo¶ci dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-cryptography
Obsoletes:	kdenetwork-kopete-tool-cryptography

%description tool-cryptography
OpenPGP messages encryptor for Kopete.

%description tool-cryptography -l pl
Program dla Kopete do szyfrowania wiadomo¶ci przy pomocy OpenPGP.

%package tool-highlight
Summary:	A highlighter plugin for Kopete
Summary(pl):	Wtyczka Kopete podkre¶laj±ca wybrane teksty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-highlight
Obsoletes:	kdenetwork-kopete-tool-highlight

%description tool-highlight
A highlighter plugin for Kopete.

%description tool-highlight -l pl
Wtyczka Kopete podkre¶laj±ca wybrane teksty.

%package tool-history
Summary:	A history plugin for Kopete
Summary(pl):	Wtyczka Kopete obs³uguj±ca historiê rozmów
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-history
Obsoletes:	kdenetwork-kopete-tool-history

%description tool-history
A history plugin for Kopete.

%description tool-history -l pl
Wtyczka Kopete obs³uguj±ca historiê rozmów.

%package tool-importer
Summary:	Contact importer for Kopete
Summary(pl):	Importer kontaktów dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-importer
Obsoletes:	kdenetwork-kopete-tool-importer

%description tool-importer
Kopete tool which allows importing contacts from other instant
messengers.

%description tool-importer -l pl
Narzêdzie Kopete umo¿liwiaj±ce importowanie kontaktów z innych
komunikatorów.

%package tool-latex
Summary:	A latex plugin for Kopete
Summary(pl):	Wtyczka Kopete renderuj±ca tekst w formacie latexu
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-latex
Obsoletes:	kdenetwork-kopete-tool-latex

%description tool-latex
A latex plugin for Kopete.

%description tool-latex -l pl
Wtyczka Kopete renderuj±ca tekst w formacie latexu.

%package tool-motionaway
Summary:	Kopete plugin which sets away status when not detecting movement near the computer
Summary(pl):	Wtyczka Kopete zmieniaj±ca status na zajêty je¶li nie wykrywa ruchu wokó³ komputera
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-motionaway
Obsoletes:	kdenetwork-kopete-tool-motionaway

%description tool-motionaway
This Kopete plugin sets away status when not detecting movement near
the computer.

%description tool-motionaway -l pl
Ta wtyczka Kopete zmienia status na zajêty je¶li nie wykrywa ruchu
wokó³ komputera.

%package tool-nowlistening
Summary:	Playlist informer for Kopete
Summary(pl):	Informator o playli¶cie dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
#Requires:	kdemultimedia-kscd >= 3.1
#Requires:	kdemultimedia-noatun >= 3.1
%if %{with xmms}
Requires:	xmms >= 1.0.0
%endif
Provides:	kdenetwork-kopete-tool-nowlistening
Obsoletes:	kdenetwork-kopete-tool-nowlistening

%description tool-nowlistening
This Kopete plugin tells selected live chats what you're currently
listening to in xmms/kscd/noatun.

%description tool-nowlistening -l pl
Ta wtyczka Kopete wypisuje podczas wybranych rozmów nazwê aktualnie
s³uchanej piosenki w xmms/kscd/noatun.

%package tool-smpppdcs
Summary:	Kopete smpppdcs plugin
Summary(pl):	Wtyczka Kopete do automatycznego przechodzenia w stan zajêty
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-smpppdcs
Obsoletes:	kdenetwork-kopete-tool-smpppdcs

%description tool-smpppdcs
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description tool-smpppdcs -l pl
Wtyczka Kopete automatycznie zmieniaj±ca status na zajêty. Warunki, po
zaistnieniu których ma nast±piæ, s± konfigurowalne.

%package tool-spellcheck
Summary:	A spell checking plugin for Kopete
Summary(pl):	Wtyczka Kopete sprawdzaj±ca pisownie
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-spellcheck
Obsoletes:	kdenetwork-kopete-tool-spellcheck

%description tool-spellcheck
A spell checking plugin for Kopete.

%description tool-spellcheck -l pl
Wtyczka Kopete sprawdzaj±ca pisownie.

%package tool-texteffect
Summary:	Kopete plugin that adds nice effects to your messages
Summary(pl):	Wtyczka Kopete dodaj±ca ³adne efekty do wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-texteffect
Obsoletes:	kdenetwork-kopete-tool-texteffect

%description tool-texteffect
Kopete plugin that adds nice effects to your messages.

%description tool-texteffect -l pl
Wtyczka Kopete dodaj±ca ³adne efekty do wiadomo¶ci.

%package tool-translator
Summary:	Kopete plugin which uses babelfish to translate messages
Summary(pl):	Wtyczka Kopete wykorzystuj±ca babelfish do t³umaczenia wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-translator
Obsoletes:	kdenetwork-kopete-tool-translator

%description tool-translator
This Kopete plugin uses web translating engines (like Altavista's
babelfish or Google) to translate messages.

%description tool-translator -l pl
Ta wtyczka Kopete wykorzystuje babelfish do t³umaczenia wiadomo¶ci.

%package tool-webpresence
Summary:	Web contactlist presenter for Kopete
Summary(pl):	Wy¶wietlacz listy kontaktów na WWW dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libxml2 >= 2.4.8
Requires:	libxslt >= 1.0.7
Provides:	kopete-tool-webpresence
Obsoletes:	kopete-tool-webpresence

%description tool-webpresence
This Kopete plugin shows the status of your IM accounts on a webpage.

%description tool-webpresence -l pl
Ta wtyczka Kopete pokazuje status (ca³ej lub czê¶ci) listy kontaktów
na stronie WWW.

%package protocol-aim
Summary:	Kopete plugin which adds AIM protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u AIM
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-aim
Obsoletes:	kdenetwork-kopete-protocol-aim

%description protocol-aim
Kopete plugin which adds AIM protocol support.

%description protocol-aim -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u AIM.

%package protocol-gg
Summary:	Kopete plugin which adds GaduGadu protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u GaduGadu
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-gg
Obsoletes:	kdenetwork-kopete-protocol-gg

%description protocol-gg
Kopete plugin which adds GaduGadu protocol support.

%description protocol-gg -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u GaduGadu.

%package protocol-groupwise
Summary:	Kopete plugin which adds Groupwise protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u Groupwise
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-groupwise
Obsoletes:	kdenetwork-kopete-protocol-groupwise

%description protocol-groupwise
Kopete plugin which adds Groupwise protocol support.

%description protocol-groupwise -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u Groupwise.

%package protocol-icq
Summary:	Kopete plugin which adds ICQ protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u ICQ
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-icq
Obsoletes:	kdenetwork-kopete-protocol-icq

%description protocol-icq
Kopete plugin which adds ICQ protocol support.

%description protocol-icq -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u ICQ.

%package protocol-irc
Summary:	Kopete plugin which adds IRC support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê IRC-a
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-irc
Obsoletes:	kdenetwork-kopete-protocol-irc

%description protocol-irc
Kopete plugin which adds IRC support.

%description protocol-irc -l pl
Wtyczka Kopete dodaj±ca obs³ugê IRC-a.

%package protocol-jabber
Summary:	Kopete plugin which adds Jabber protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u Jabber
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-jabber
Obsoletes:	kdenetwork-kopete-protocol-jabber

%description protocol-jabber
Kopete plugin which adds Jabber protocol support.

%description protocol-jabber -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u Jabber.

%package protocol-msn
Summary:	Kopete plugin which adds MSN protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u MSN
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_msn = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-msn
Obsoletes:	kdenetwork-kopete-protocol-msn

%description protocol-msn
Kopete plugin which adds MSN protocol support.

%description protocol-msn -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u MSN.

%package protocol-meanwhile
Summary:	Kopete plugin which adds Lotus Sametime protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u Lotus Sametime
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-meanwhile
Obsoletes:	kdenetwork-kopete-protocol-meanwhile

%description protocol-meanwhile
Kopete plugin which adds meanwhile Lotus Sametime support.

%description protocol-meanwhile -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u Lotus Sametime.

%package protocol-sms
Summary:	Kopete plugin which adds SMS contact support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê kontaktów SMS
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-sms
Obsoletes:	kdenetwork-kopete-protocol-sms

%description protocol-sms
Kopete plugin which adds SMS contact support.

%description protocol-sms -l pl
Wtyczka Kopete dodaj±ca obs³ugê kontaktów SMS.

%package protocol-winpopup
Summary:	Kopete plugin which adds WinPopUp messaging support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê komunikacji przez WinPopUp
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-winpopup
Obsoletes:	kdenetwork-kopete-protocol-winpopup

%description protocol-winpopup
Kopete plugin which adds WinPopUp messaging support.

%description protocol-winpopup -l pl
Wtyczka Kopete dodaj±ca obs³ugê komunikacji przez WinPopUp.

%package protocol-yahoo
Summary:	Kopete plugin which adds Yahoo protocol support
Summary(pl):	Wtyczka Kopete dodaj±ca obs³ugê protoko³u Yahoo
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-protocol-yahoo
Obsoletes:	kdenetwork-kopete-protocol-yahoo

%description protocol-yahoo
Kopete plugin which adds Yahoo protocol support.

%description protocol-yahoo -l pl
Wtyczka Kopete dodaj±ca obs³ugê protoko³u Yahoo.

# libraries
%package libkopete
Summary:	kopete library
Summary(pl):	Biblioteka kopete
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kdenetwork-libkopete
Obsoletes:	kdenetwork-libkopete

%description libkopete
kopete library.

%description libkopete -l pl
Biblioteka kopete.

%package libkopete_msn
Summary:	MSN protocol shared library
Summary(pl):	Biblioteka wspó³dzielona dla protoko³u MSN
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-libkopete_msn
Obsoletes:	kdenetwork-libkopete_msn

%description libkopete_msn
MSN protocol shared library.

%description libkopete_msn -l pl
Biblioteka wspó³dzielona dla protoko³u MSN.

%package libkopete_videodevice
Summary:	Video input device support library for kopete
Summary(pl):	Biblioteka z obs³ug± urz±dzeñ wej¶cia video dla kopete
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-libkopete_videodevice
Obsoletes:	kdenetwork-libkopete_videodevice

%description libkopete_videodevice
Video input device support library for kopete.

%description libkopete_videodevice -l pl
Biblioteka z obs³ug± urz±dzeñ wej¶cia video dla kopete.

%package libkopete_oscar
Summary:	Shared library which adds OSCAR protocol support
Summary(pl):	Biblioteka dodaj±ca obs³ugê protoko³u OSCAR
Group:		X11/Applications/Networking
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-libkopete_oscar

%description libkopete_oscar
A shared library which adds OSCAR protocol support needed eg. by AIM
and ICQ.

%description libkopete_oscar -l pl
Biblioteka dodaj±ca obs³ugê protoko³u OSCAR, u¿ywanego miêdzy innymi
przez AIM i ICQ.

%prep
%setup -q -n %{name}-%{version}-%{_snap}
%patch0 -p1

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%{__make} -f admin/Makefile.common cvs
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--with-distribution="PLD Linux Distribution" \
	--with-qt-libraries=%{_libdir} \
	--disable-testbed \
	%{!?debug:--disable-rpath} \
	--%{?with_meanwhile:en}%{!?with_meanwhile:dis}able-meanwhile \
	--%{?with_smpppd:en}%{!?with_smpppd:dis}able-smpppd \
	--%{?with_jingle:en}%{!?with_jingle:dis}able-jingle \
	--%{?with_smsgsm:en}%{!?with_smsgsm:dis}able-smsgsm \
	--%{?with_slp:en}%{!?with_slp:dis}able-slp \

%{__make} \
	CXXLD=%{_host_cpu}-%{_vendor}-%{_os}-g++ \
	CCLD=%{_host_cpu}-%{_vendor}-%{_os}-gcc \
	AM_MAKEFLAGS='CXXLD=$(CXXLD) CCLD=$(CCLD)'

%if %{with winpopup}
%{__make} -C kopete/protocols/winpopup
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%if %{with winpopup}
%{__make} -C kopete/protocols/winpopup install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%find_lang %{name} --with-kde

# in kdelibs
rm -f $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-icq.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kopete.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-account-kconf_update
%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-nameTracking-kconf_update
%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-pluginloader2-kconf_update
%attr(755,root,root) %{_bindir}/kopete
%{_libdir}/kde3/kcm_kopete_addbookmarks.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_addbookmarks.so
%{_libdir}/kde3/kcm_kopete_accountconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_accountconfig.so
%{_libdir}/kde3/kcm_kopete_appearanceconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_appearanceconfig.so
%{_libdir}/kde3/kcm_kopete_behaviorconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_behaviorconfig.so
%{_libdir}/kde3/kcm_kopete_netmeeting.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_netmeeting.so
%{_libdir}/kde3/kcm_kopete_identityconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_identityconfig.so
%{_libdir}/kde3/kopete_addbookmarks.la
%attr(755,root,root) %{_libdir}/kde3/kopete_addbookmarks.so
%{_libdir}/kde3/kopete_chatwindow.la
%attr(755,root,root) %{_libdir}/kde3/kopete_chatwindow.so
%{_libdir}/kde3/kopete_emailwindow.la
%attr(755,root,root) %{_libdir}/kde3/kopete_emailwindow.so
%{_libdir}/kde3/kopete_statistics.la
%attr(755,root,root) %{_libdir}/kde3/kopete_statistics.so
%{_libdir}/kde3/libkrichtexteditpart.la
%attr(755,root,root) %{_libdir}/kde3/libkrichtexteditpart.so
%{_datadir}/apps/kconf_update/kopete-account-0.10.pl
%{_datadir}/apps/kconf_update/kopete-account-kconf_update.sh
%{_datadir}/apps/kconf_update/kopete-account-kconf_update.upd
%{_datadir}/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.sh
%{_datadir}/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.upd
%{_datadir}/apps/kconf_update/kopete-jabberproxytype-kconf_update.sh
%{_datadir}/apps/kconf_update/kopete-jabberproxytype-kconf_update.upd
%{_datadir}/apps/kconf_update/kopete-nameTracking.upd
%{_datadir}/apps/kconf_update/kopete-pluginloader2.sh
%{_datadir}/apps/kconf_update/kopete-pluginloader2.upd
%{_datadir}/apps/kconf_update/kopete-pluginloader.pl
%{_datadir}/apps/kconf_update/kopete-pluginloader.upd
%dir %{_datadir}/apps/kopete
%{_datadir}/apps/kopete/*rc
%dir %{_datadir}/apps/kopete/icons
%dir %{_datadir}/apps/kopete/icons/crystalsvg
%dir %{_datadir}/apps/kopete/icons/crystalsvg/*
%dir %{_datadir}/apps/kopete/icons/crystalsvg/*/*
%{_iconsdir}/*/*/actions/*_user.png
%{_iconsdir}/*/*/actions/voicecall.png
%{_iconsdir}/*/*/actions/webcam*.png
%{_iconsdir}/*/*/actions/show_offliners.png
%{_iconsdir}/*/*/actions/account_offline_overlay.png
%{_iconsdir}/*/*/actions/account_offline_overlay.svgz
%{_iconsdir}/*/*/actions/emoticon.png
%{_datadir}/apps/kopete/icons/*/*/actions/kgpg_key?.png
%{_iconsdir}/*/*/actions/kopeteavailable.png
%{_iconsdir}/*/*/actions/kopeteaway.png
%{_datadir}/apps/kopete/icons/*/*/actions/logging.png
%{_iconsdir}/*/*/actions/newmessage.mng
%{_iconsdir}/*/*/actions/newmsg.png
%{_iconsdir}/*/*/actions/status_unknown.png
%{_iconsdir}/*/*/actions/status_unknown_overlay.png
%{_iconsdir}/crystalsvg/*/*/metacontact_away.png
%{_iconsdir}/crystalsvg/*/*/metacontact_offline.png
%{_iconsdir}/crystalsvg/*/*/metacontact_online.png
%{_iconsdir}/crystalsvg/*/*/metacontact_unknown.png
%dir %{_datadir}/apps/kopete/pics
%{_datadir}/apps/kopete/pics/statistics
%{_datadir}/apps/kopete/styles
%{_datadir}/apps/kopete_statistics
%dir %{_datadir}/apps/kopeterichtexteditpart
%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
%{_datadir}/config.kcfg/kopete.kcfg
%{_datadir}/config.kcfg/kopeteidentityconfigpreferences.kcfg
%{_datadir}/services/chatwindow.desktop
%{_datadir}/services/emailwindow.desktop
%{_datadir}/services/kopete_accountconfig.desktop
%{_datadir}/services/kopete_addbookmarks.desktop
%{_datadir}/services/kopete_appearanceconfig.desktop
%{_datadir}/services/kopete_behaviorconfig.desktop
%{_datadir}/services/kopete_statistics.desktop
%{_datadir}/servicetypes/kopeteplugin.desktop
%{_datadir}/servicetypes/kopeteprotocol.desktop
%{_datadir}/servicetypes/kopeteui.desktop
%{_datadir}/sounds/Kopete_Event.ogg
%{_datadir}/sounds/Kopete_Received.ogg
%{_datadir}/sounds/Kopete_Sent.ogg
%{_datadir}/sounds/Kopete_User_is_Online.ogg
%{_desktopdir}/kde/kopete.desktop
%{_iconsdir}/*/*/apps/kopete.png
%{_iconsdir}/*/*/apps/kopete2.svgz
%{_iconsdir}/crystalsvg/*/apps/kopete_all_away.png
%{_iconsdir}/crystalsvg/*/apps/kopete_offline.png
%{_iconsdir}/crystalsvg/*/apps/kopete_some_away.png
%{_iconsdir}/crystalsvg/*/apps/kopete_some_online.png
%{_iconsdir}/crystalsvg/*/mimetypes/kopete_emoticons.png
%{_datadir}/mimelnk/application/x-kopete-emoticons.desktop
# New icons
%{_iconsdir}/crystalsvg/*/actions/contact_away_overlay.png
%{_iconsdir}/crystalsvg/*/actions/contact_busy_overlay.png
%{_iconsdir}/crystalsvg/*/actions/contact_food_overlay.png
%{_iconsdir}/crystalsvg/*/actions/contact_invisible_overlay.png
%{_iconsdir}/crystalsvg/*/actions/contact_phone_overlay.png
%{_iconsdir}/crystalsvg/*/actions/contact_xa_overlay.png
%{_iconsdir}/*/*/actions/kopeteeditstatusmessage.png
%{_iconsdir}/*/*/actions/kopetestatusmessage.png
# New one
#%{_datadir}/services/invitation.protocol
%{_datadir}/services/kopete_identityconfig.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete.so
%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so
%attr(755,root,root) %{_libdir}/libkopete_oscar.so
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so
%{_includedir}/kopete

%files designer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/libkopetewidgets.so
%{_libdir}/kde3/plugins/designer/libkopetewidgets.la

%files protocol-aim
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*aim*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*aim*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/*aim*
%{_datadir}/apps/kopete/icons/hicolor/*/*/*aim*
%{_datadir}/services/aim.protocol
%{_datadir}/services/kopete_aim.desktop

%files protocol-gg
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*gadu*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*gadu*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gadu*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gg*
%{_datadir}/services/kopete_gadu.desktop

%files protocol-groupwise
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*groupwise*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*groupwise*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/groupwise*
%{_datadir}/apps/kopete_groupwise
%{_datadir}/services/kopete_groupwise.desktop

%files protocol-icq
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*icq*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*icq*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/*icq*
%{_datadir}/apps/kopete/icons/hicolor/*/*/*icq*
# moved to kdelibs; used also by sim
# %%{_datadir}/mimelnk/application/x-icq.desktop
%{_datadir}/services/kopete_icq.desktop

%files protocol-irc
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*irc*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*irc*.so
%{_datadir}/apps/kopete/ircnetworks.xml
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/irc*
%{_datadir}/services/kopete_irc.desktop
%{_datadir}/services/irc.protocol
#%%{_datadir}/apps/kopete/pics/irc_connecting.mng

%files protocol-jabber
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*jabber*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*jabber*.so
%{_iconsdir}/*/*/*/jabber*
%{_libdir}/kde3/kio_jabberdisco.la
%attr(755,root,root) %{_libdir}/kde3/kio_jabberdisco.so
%{_datadir}/apps/kopete_jabber
%{_datadir}/services/jabberdisco.protocol
%{_datadir}/services/kopete_jabber.desktop

%if %{with meanwhile}
%files protocol-meanwhile
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*meanwhile*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*meanwhile*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/meanwhile*
%{_datadir}/services/kopete_meanwhile.desktop
%endif

%files protocol-msn
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_msn.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_msn.so
%{_libdir}/kde3/kopete*msn*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*msn*.so
%{_libdir}/kde3/kopete_netmeeting.la
%attr(755,root,root) %{_libdir}/kde3/kopete_netmeeting.so
%{_datadir}/apps/kopete_msn
%{_datadir}/apps/kopete_netmeeting
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/msn*
%{_datadir}/services/kconfiguredialog/kopete_msn_config.desktop
%{_datadir}/services/kconfiguredialog/kopete_netmeeting_config.desktop
%{_datadir}/services/kopete_msn.desktop
%{_datadir}/services/kopete_netmeeting.desktop

%if %{with skype}
%files protocol-skype
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*skype*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*skype*.so
%{_datadir}/apps/kopete/icons/*/*/*/call.png
%{_datadir}/apps/kopete/icons/*/*/*/contact_ffc_overlay.png
%{_datadir}/apps/kopete/icons/*/*/*/contact_unknown_overlay.png
%{_iconsdir}/*/*/*/call.png
%{_datadir}/apps/kopete/icons/*/*/*/*skype*
%{_datadir}/services/kopete_skype.desktop
%{_datadir}/apps/kopete_skype
%endif

%if %{with smsgsm}
%files protocol-sms
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*sms*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*sms*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/sms*
%{_datadir}/services/kopete_sms.desktop
%endif

#%files protocol-testbed
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kopete_testbed.la
#%attr(755,root,root) %{_libdir}/kde3/kopete_testbed.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/testbed*
#%{_datadir}/services/kopete_testbed.desktop

%if %{with winpopup}
%files protocol-winpopup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/winpopup*.sh
#%{_libdir}/kde3/kcm_kopete_wp.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_wp.so
%{_libdir}/kde3/kopete*wp*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*wp*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/wp*
#%{_datadir}/services/kconfiguredialog/kopete_wp_config.desktop
%{_datadir}/services/kopete_wp.desktop
%endif

%files protocol-yahoo
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete_yahoo.la
%attr(755,root,root) %{_libdir}/kde3/kopete_yahoo.so
%{_datadir}/apps/kopete_yahoo
%{_datadir}/apps/kopete/icons/*/*/*/yahoo*
%{_datadir}/services/kopete_yahoo.desktop

%files tool-alias
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_alias.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_alias.so
%{_libdir}/kde3/kopete_alias.la
%attr(755,root,root) %{_libdir}/kde3/kopete_alias.so
%{_datadir}/services/kconfiguredialog/kopete_alias_config.desktop
%{_datadir}/services/kopete_alias.desktop

%files tool-autoreplace
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_autoreplace.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_autoreplace.so
%{_libdir}/kde3/kopete*autoreplace*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*autoreplace*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/autoreplace.png
%{_datadir}/services/kopete_autoreplace.desktop
%{_datadir}/services/kconfiguredialog/kopete_autoreplace_config.desktop

%files tool-avdeviceconfig
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_avdeviceconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_avdeviceconfig.so
%{_datadir}/services/kopete_avdeviceconfig.desktop
%{_datadir}/apps/kopete/icons/*/*/*/kopete_avdevice*.*
#%{_datadir}/services/kconfiguredialog/kopete_avdeviceconfig.desktop

%files tool-connectionstatus
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*connectionstatus*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*connectionstatus*.so
%{_datadir}/services/kopete_connectionstatus.desktop

%files tool-contactnotes
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*contactnotes*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*contactnotes*.so
%{_datadir}/apps/kopete_contactnotes
%{_datadir}/services/kopete_contactnotes.desktop

%files tool-cryptography
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_cryptography.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_cryptography.so
%{_libdir}/kde3/kopete*cryptography*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*cryptography*.so
%{_datadir}/apps/kopete_cryptography
%{_datadir}/services/kopete_cryptography.desktop
%{_datadir}/services/kconfiguredialog/kopete_cryptography_config.desktop

%files tool-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kopete_latexconvert.sh
%{_libdir}/kde3/kcm_kopete_latex.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_latex.so
%{_libdir}/kde3/kopete_latex.la
%attr(755,root,root) %{_libdir}/kde3/kopete_latex.so
%{_datadir}/apps/kopete/icons/crystalsvg/32x32/apps/latex.png
%{_datadir}/config.kcfg/latexconfig.kcfg
%{_datadir}/apps/kopete_latex
%{_datadir}/services/kconfiguredialog/kopete_addbookmarks_config.desktop
%{_datadir}/services/kconfiguredialog/kopete_latex_config.desktop
%{_datadir}/services/kopete_latex.desktop

%files tool-highlight
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_highlight.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_highlight.so
%{_libdir}/kde3/kopete*highlight*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*highlight*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/highlight.png
%{_datadir}/services/kopete_highlight.desktop
%{_datadir}/services/kconfiguredialog/kopete_highlight_config.desktop

%files tool-history
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_history.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_history.so
%{_libdir}/kde3/kopete*history*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*history*.so
%{_datadir}/apps/kopete_history
%{_datadir}/config.kcfg/historyconfig.kcfg
%{_datadir}/services/kopete_history.desktop
%{_datadir}/services/kconfiguredialog/kopete_history_config.desktop

#%files tool-motionaway
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kcm_kopete_motionaway.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_motionaway.so
#%{_libdir}/kde3/kopete*motionaway*.la
#%attr(755,root,root) %{_libdir}/kde3/kopete*motionaway*.so
#%{_datadir}/services/kconfiguredialog/kopete_motionaway_config.desktop
#%{_datadir}/services/motionaway.desktop

%files tool-nowlistening
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_nowlistening.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_nowlistening.so
%{_libdir}/kde3/kopete*nowlistening*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*nowlistening*.so
%{_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_datadir}/services/kconfiguredialog/kopete_nowlistening_config.desktop
%{_datadir}/services/kopete_nowlistening.desktop

#%%files tool-spellcheck
#%%defattr(644,root,root,755)
#%%{_libdir}/kde3/kopete*spellcheck*.la
#%%attr(755,root,root) %{_libdir}/kde3/kopete*spellcheck*.so
#%%{_datadir}/services/spellcheck.desktop

%if %{with smpppd}
%files tool-smpppdcs
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/smpppdcs.kcfg
%{_libdir}/kde3/kcm_kopete_smpppdcs.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_smpppdcs.so
%{_libdir}/kde3/kopete*smpppdcs*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*smpppdcs*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/smpppdcs.png
%{_datadir}/services/kopete_smpppdcs.desktop
%{_datadir}/services/kconfiguredialog/kopete_smpppdcs_config.desktop
%endif

%files tool-texteffect
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_texteffect.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_texteffect.so
%{_libdir}/kde3/kopete*texteffect*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*texteffect*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/texteffect.png
%{_datadir}/services/kconfiguredialog/kopete_texteffect_config.desktop
%{_datadir}/services/kopete_texteffect.desktop

%files tool-translator
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_translator.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_translator.so
%{_libdir}/kde3/kopete*translator*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*translator*.so
%{_datadir}/apps/kopete_translator
%{_datadir}/services/kconfiguredialog/kopete_translator_config.desktop
%{_datadir}/services/kopete_translator.desktop

%files tool-webpresence
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_webpresence.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_webpresence.so
%{_libdir}/kde3/kopete*webpresence*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*webpresence*.so
%{_datadir}/apps/kopete/webpresence
%{_datadir}/services/kconfiguredialog/kopete_webpresence_config.desktop
%{_datadir}/services/kopete_webpresence.desktop

%files libkopete
%defattr(644,root,root,755)
%{_libdir}/libkopete.la
%attr(755,root,root) %{_libdir}/libkopete.so.*.*.*

%files libkopete_videodevice
%defattr(644,root,root,755)
%{_libdir}/libkopete_videodevice.la
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so.*.*.*

%files libkopete_msn
%defattr(644,root,root,755)
%{_libdir}/libkopete_msn_shared.la
%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so.*.*.*

%files libkopete_oscar
%defattr(644,root,root,755)
%{_libdir}/libkopete_oscar.la
%attr(755,root,root) %{_libdir}/libkopete_oscar.so.*.*.*
