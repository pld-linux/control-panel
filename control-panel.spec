Summary:	Red Hat Control Panel
Summary(de.UTF-8):   Red-Hat-Kontrollfeld
Summary(fr.UTF-8):   Panneau de contrôle de Red Hat
Summary(pl.UTF-8):   Panel Kontrolny
Summary(tr.UTF-8):   Red Hat Denetim Masası
Summary(pt_BR.UTF-8):   Painel de Controle Red Hat
Summary(es.UTF-8):   Panel de Control Red Hat
Summary(ru.UTF-8):   Утилита для запуска программ настройки системы для X
Summary(uk.UTF-8):   Утиліта для запуску програм налагодження системи під X
Name:		control-panel
Version:	3.18
Release:	2
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	cb29e9fb4b290f21a358f01532940ae9
Patch0:		%{name}-FHS2.0.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_prefix		/usr/X11R6

%description
The Red Hat control panel is an X program launcher for various
configuration tools. Other packages provide information which allow
them to show up on the control panel's menu of available tools.

%description -l de.UTF-8
Das Red-Hat-Kontrollfeld ist eine X-Programm-Startrampe für
verschiedene Konfigurations-Tools. Von den Softwarepaketen gelieferte
Informatinen können im Menü der verfügbaren Tools angezeigt werden.

%description -l fr.UTF-8
Le tableau de bord Red Hat est un lanceur de programmes X pour les
différents outils de configuration. Les autres paquetages fournissent
l'information qui leur permet d'apparaitre dans le menu du tableau de
bord.

%description -l pl.UTF-8
Control-panel jest programem korzystającym z X Window System
uruchamiającym różne narzędzia konfiguracyjne. Inne pakiety same
wstawiają informacje, które pozwalają wyświetlać panelowi kontrolnemu
listę dostępnych narzędzi.

%description -l tr.UTF-8
Red Hat denetim masası, bazı ayarlama araçları için X programları
çalıştırıcısıdır. Bir aracın denetim masasındaki araçlar arasında
gözükmesi için o araçla ilgili paketler gerekli bilgileri denetim
masasına bildirirler.

%description -l pt_BR.UTF-8
O control-panel (painel de controle) Red Hat é um programa X que
executa várias ferramentas de configuração. Outros pacotes oferecem
informação que permitem a visualização das ferramentas disponíveis
no menu do control-panel.

%description -l es.UTF-8
Control-panel (panel de control) Red Hat es un programa X que
ejecuta varias herramientas de configuración. Otros paquetes ofrecen
información que permiten la visualización de las herramientas
disponibles en el menú del panel de control.

%description -l ru.UTF-8
Control-panel - это графическая утилита, запускающая различные утилиты
конфигурации системы под X.

%description -l uk.UTF-8
Control-panel - це графічна утиліта, яка запускає різноманітні утиліти
конфігурування системи під X.

%prep
%setup -q
#%patch -p1

%build
%{__make} \
CFLAGS="%{rpmcflags} -I/usr/include/glib-1.2 -I/usr/X11R6/include -I/usr/include/gtk-1.2 -I/usr/lib/glib/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/System
install control-panel.desktop $RPM_BUILD_ROOT%{_applnkdir}/System/control-panel.desktop

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	LIBDIR=%{_libdir} \
	OWNER= \
	install install-man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_applnkdir}/System/control-panel.desktop

%attr(755,root,root) %{_bindir}/control-panel

%{_libdir}/rhs/control-panel/loopy

%attr(755,root,root) %{_libdir}/rhs/control-panel/*.tcl
%{_mandir}/man8/*
