Summary:	Red Hat Control Panel
Summary(de):	Red-Hat-Kontrollfeld
Summary(fr):	Panneau de contrôle de Red Hat
Summary(pl):	Panel Kontrolny
Summary(tr):	Red Hat Denetim Masası
Summary(pt_BR):	Painel de Controle Red Hat
Summary(es):	Panel de Control Red Hat
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ÚÁĞÕÓËÁ ĞÒÏÇÒÁÍÍ ÎÁÓÔÒÏÊËÉ ÓÉÓÔÅÍÙ ÄÌÑ X
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ÚÁĞÕÓËÕ ĞÒÏÇÒÁÍ ÎÁÌÁÇÏÄÖÅÎÎÑ ÓÉÓÔÅÍÉ Ğ¦Ä X
Name:		control-panel
Version:	3.18
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS2.0.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_prefix		/usr/X11R6

%description
The Red Hat control panel is an X program launcher for various
configuration tools. Other packages provide information which allow
them to show up on the control panel's menu of available tools.

%description -l de
Das Red-Hat-Kontrollfeld ist eine X-Programm-Startrampe für
verschiedene Konfigurations-Tools. Von den Softwarepaketen gelieferte
Informatinen können im Menü der verfügbaren Tools angezeigt werden.

%description -l fr
Le tableau de bord Red Hat est un lanceur de programmes X pour les
différents outils de configuration. Les autres paquetages fournissent
l'information qui leur permet d'apparaitre dans le menu du tableau de
bord.

%description -l pl
Control-panel jest programem korzystaj±cym z X Window System
uruchamiaj±cym ró¿ne narzêdzia konfiguracyjne. Inne pakiety same
wstawiaj± informacje, które pozwalaj± wy¶wietlaæ panelowi kontrolnemu
listê dostêpnych narzêdzi.

%description -l tr
Red Hat denetim masası, bazı ayarlama araçları için X programları
çalıştırıcısıdır. Bir aracın denetim masasındaki araçlar arasında
gözükmesi için o araçla ilgili paketler gerekli bilgileri denetim
masasına bildirirler.

%description -l pt_BR
O control-panel (painel de controle) Red Hat é um programa X que
executa várias ferramentas de configuração. Outros pacotes oferecem
informação que permitem a visualização das ferramentas disponíveis
no menu do control-panel.

%description -l es
Control-panel (panel de control) Red Hat es un programa X que
ejecuta varias herramientas de configuración. Otros paquetes ofrecen
información que permiten la visualización de las herramientas
disponibles en el menú del panel de control.

%description -l ru
Control-panel - ÜÔÏ ÇÒÁÆÉŞÅÓËÁÑ ÕÔÉÌÉÔÁ, ÚÁĞÕÓËÁÀİÁÑ ÒÁÚÌÉŞÎÙÅ ÕÔÉÌÉÔÙ
ËÏÎÆÉÇÕÒÁÃÉÉ ÓÉÓÔÅÍÙ ĞÏÄ X.

%description -l uk
Control-panel - ÃÅ ÇÒÁÆ¦ŞÎÁ ÕÔÉÌ¦ÔÁ, ÑËÁ ÚÁĞÕÓËÁ¤ Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ ÕÔÉÌ¦ÔÉ
ËÏÎÆ¦ÇÕÒÕ×ÁÎÎÑ ÓÉÓÔÅÍÉ Ğ¦Ä X.

%prep
%setup -q
#%patch -p1

%build
%{__make} \
CFLAGS="%{rpmcflags} -I/usr/include/glib-1.2 -I/usr/X11R6/include -I/usr/X11R6/include/gtk-1.2 -I/usr/lib/glib/include"

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
