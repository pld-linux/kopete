%define		_snapshot	20021108
Name:		kopete
License:	GPL
Group:		X11/Applications/Networking
Summary:	Multi-protocol plugin-based instant messenger
Summary(pl):	Komunikator obs�uguj�cy wiele protoko��w
Version:	0.5
Release:	1.%{_snapshot}
Source0:	%{name}-%{_snapshot}.tar.bz2
URL:		http://kopete.kde.org
Requires:	kdelibs >= 3.0.9
Requires:	qt >= 3.1
BuildRequires:	qt-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
Kopete to rozszerzalny i rozbudowywalny komunikator obs�uguj�cy wiele protoko��w
pouk�adanych w pluginy. Opr�cz tego aplikacja oferuje wiele ciekawych u�yteczno�ci
jak np. t�umacz (kozysta z babelfish).

%package plugin-tools-autoaway
Summary:	An autoaway plugin
Summary(pl):	Plugin automatycznego przejscia w stan zajety.
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-tools-autoaway
Automatically changes status to away. Conditions are configurable.


%description plugin-tools-autoaway -l pl
Automatycznie zmienia status na zajety. Warunki w ktorych po zaistnieniu ktorych ma nastapic sa
konfigurowalne.

%package plugin-tools-conectionstatus
Summary:	Internet connection detector
Summary(pl):	Wykrywaz polazen internetowych
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-tools-conectionstatus
Automatically detects whether the internet connection is available or not

%description plugin-tools-conectionstatus -l pl
Automatycznie sprawdza czy dost�pne jest po��czenie do internetu czy nie


%package plugin-tools-contactnotes
Summary:	Add personal notes to your contacts
Summary(pl):	Dodawanie notatek do kontaktow
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-tools-contactnotes
Allows adding personal notes to your contacts.


%description plugin-tools-contactnotes  -l pl
Umo�liwia dodawanie notatek do kontaktow.

%package plugin-tools-importer
Summary:	Contact importer
Summary(pl):	Importer kontakt�w
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-tools-importer
Allows importing contacts from other IM's.


%description plugin-tools-importer  -l pl
Umo�liwia importowanie kontakt�w z innych komunikator�w.

%package plugin-tools-motionaway
Summary:	Sets away status when not detecting movement near the computer
Summary(pl):	Zmienia status na zaj�ty je�li nie wykrywa ruchu wok� komputera
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-tools-motionaway
Sets away status when not detecting movement near the computer

%description plugin-tools-motionaway  -l pl
Zmienia status na zaj�ty je�li nie wykrywa ruchu wok� komputera

%package plugin-tools-translator
Summary:	Uses babelfish to translate messages
Summary(pl):	Wykorzystuje babelfish do t�umaczenia wiadomo�ci
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-tools-translator
Uses babelfish to translate messages

%description plugin-tools-translator -l pl
Wykorzystuje babelfish do t�umaczenia wiadomo�ci

%package plugin-protocols-aim
Summary:	Adds AIM protocol support
Summary(pl):	Dodaje obs�ug� protoko�u AIM
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-aim
Adds AIM protocol support

%description plugin-protocols-aim -l pl
Dodaje obs�ug� protoko�u AIM

%package plugin-protocols-gg
Summary:	Adds GaduGadu protocol support
Summary(pl):	Dodaje obs�ug� protoko�u GaduGadu
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-gg
Add GaduGadu support
%description plugin-protocols-gg -l pl
Dodaje obs�ug� protoko�u GaduGadu

%package plugin-protocols-icq
Summary:	Adds ICQ protocol support
Summary(pl):	Dodaje obs�ug� protoko�u ICQ
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-icq
Adds ICQ  protocol support

%description plugin-protocols-icq -l pl
Dodaje obs�ug� protoko�u ICQ

%package plugin-protocols-irc
Summary:        Adds irc support
Summary(pl):    Dodaje obs�ug� irc
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-irc
Adds irc support

%description plugin-protocols-irc -l pl
Dodaje obs�ug� irc


%package plugin-protocols-jabber
Summary:        Adds Jabber  protocol support
Summary(pl):    Dodaje obs�ug� protoko�u Jabber
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-jabber
Adds Jabber  protocol support

%description plugin-protocols-jabber -l pl
Dodaje obs�ug� protoko�u Jabber

%package plugin-protocols-msn
Summary:        Adds MSN protocol support
Summary(pl):    Dodaje obs�ug� protoko�u
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-msn
Adds MSN protocol support

%description plugin-protocols-msn -l pl
Dodaje obs�ug� protoko�u MSN

%package plugin-protocols-oscar
Summary:        Adds OSCAR  protocol support
Summary(pl):    Dodaje obs�ug� protoko�u OSCAR
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-oscar
Adds OSCAR protocol support

%description plugin-protocols-oscar -l pl
Dodaje obs�ug� protoko�u OSCAR

%package plugin-protocols-sms
Summary:        Adds SMS contact support
Summary(pl):    Dodaje obs�ug� kontakt�w SMS
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-sms
Adds SMS contact support

%description plugin-protocols-sms -l pl
Dodaje obs�ug� kontakt�w SMS

%package plugin-protocols-winpopup
Summary:        Adds winpopup messaging support
Summary(pl):    Dodaje obs�ug� komunikacji via winpopup
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-winpopup
Adds winpopup messaging support

%description plugin-protocols-winpopup -l pl
Dodaje obs�ug� komunikacji via winpopup

%package plugin-protocols-yahoo
Summary:        Adds yahoo protocol support
Summary(pl):    Dodaje obs�ug� protoko�u yahoo
Group:          X11/Applications
Requires:       kopete >= %{version}-%{release}

%description plugin-protocols-yahoo
Adds yahoo protocol support

%description plugin-protocols-yahoo -l pl
Dodaje obs�ug� protoko�u yahoo



%prep
%setup -q -n %{name}-%{_snapshot}


%build
%{__make} -f Makefile.cvs
%configure 
    
%{__make}
cd kopete/protocols/sms
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd kopete/protocols/sms
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ..
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Internet/kopete.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
mv -f $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_pixmapsdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/apps/kopete/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
#%doc  
%attr(755,root,root) %{_bindir}/kopete
%attr(755,root,root) %{_libdir}/libkopete*.*
%{_applnkdir}
%{_pixmapsdir}
%{_datadir}/sounds
%{_datadir}/apps/kopete/*rc
%{_datadir}/apps/kopete/*.html
%{_datadir}/apps/kopete/pics/addside.png
%{_datadir}/apps/kopete/pics/admin_icon.png
%{_datadir}/apps/kopete/pics/aol_icon.png
%{_datadir}/apps/kopete/pics/away-mobile.png
%{_datadir}/apps/kopete/pics/dt_icon.png
%{_datadir}/apps/kopete/pics/emoticon.png
%{_datadir}/apps/kopete/pics/emoticons
%{_datadir}/apps/kopete/pics/free_icon.png
%{_datadir}/apps/kopete/pics/history.png
%{_datadir}/apps/kopete/pics/kopeteavailable.png
%{_datadir}/apps/kopete/pics/kopeteaway.png
%{_datadir}/apps/kopete/pics/kopetestatus.png
%{_datadir}/apps/kopete/pics/metacontact_away.png
%{_datadir}/apps/kopete/pics/metacontact_offline.png
%{_datadir}/apps/kopete/pics/metacontact_online.png
%{_datadir}/apps/kopete/pics/mobile.png
%{_datadir}/apps/kopete/pics/newmsg.png
%{_datadir}/apps/kopete/pics/offline-mobile.png
%{_datadir}/apps/kopete/pics/online-mobile.png
%{_datadir}/apps/kopete/pics/emoticons


%files plugin-tools-autoaway
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*autoaway*.*
%{_datadir}/apps/kopete/autoaway.plugin

%files plugin-tools-conectionstatus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*connectionstatus*.*
%{_datadir}/apps/kopete/connectionstatus.plugin

%files plugin-tools-contactnotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*contactnotes*.*
%{_datadir}/apps/kopete/contactnotes.plugin

%files plugin-tools-importer
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/kde3/kopete*importer*.*
%{_datadir}/apps/kopete/importer.plugin

%files plugin-tools-motionaway
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*motionaway*.*
%{_datadir}/apps/kopete/motionaway.plugin

%files plugin-tools-translator
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*translator*.*
%{_datadir}/apps/kopete/translator.plugin

%files plugin-protocols-aim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*aim*.*
%{_datadir}/apps/kopete/aim.plugin
%{_datadir}/apps/kopete/pics/aim*

%files plugin-protocols-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*gadu*.*
%{_datadir}/apps/kopete/gadu.plugin
%{_datadir}/apps/kopete/pics/gadu*
%{_datadir}/apps/kopete/pics/gg*

%files plugin-protocols-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*icq*.*
%{_datadir}/apps/kopete/icq.plugin
%{_datadir}/apps/kopete/pics/icq*

%files plugin-protocols-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*irc*.*
%{_datadir}/apps/kopete/irc.plugin
%{_datadir}/apps/kopete/pics/irc*

%files plugin-protocols-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*jabber*.*
%{_datadir}/apps/kopete/jabber.plugin
%{_datadir}/apps/kopete/pics/jabber*

%files plugin-protocols-msn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*msn*.*
%{_datadir}/apps/kopete/msn.plugin
%{_datadir}/apps/kopete/pics/msn*

%files plugin-protocols-oscar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*oscar*.*
%{_datadir}/apps/kopete/oscar.plugin
%{_datadir}/apps/kopete/pics/oscar*

%files plugin-protocols-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*sms*.*
%{_datadir}/apps/kopete/sms.plugin

%files plugin-protocols-yahoo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*yahoo*.*
%{_datadir}/apps/kopete/yahoo.plugin
%{_datadir}/apps/kopete/pics/yahoo*
