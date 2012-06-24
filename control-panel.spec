Summary:	Red Hat Control Panel
Summary(de):	Red-Hat-Kontrollfeld
Summary(fr):	Panneau de contr�le de Red Hat
Summary(pl):	Panel Kontrolny
Summary(tr):	Red Hat Denetim Masas�
Name:		control-panel
Version:	3.11
Release:	3
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	%{name}-%{version}.tar.gz
Patch0:		control-panel-FHS2.0.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Red Hat control panel is an X program launcher for various
configuration tools. Other packages provide information which allow
them to show up on the control panel's menu of available tools.

%description -l de
Das Red-Hat-Kontrollfeld ist eine X-Programm-Startrampe f�r
verschiedene Konfigurations-Tools. Von den Softwarepaketen gelieferte
Informatinen k�nnen im Men� der verf�gbaren Tools angezeigt werden.

%description -l fr
Le tableau de bord Red Hat est un lanceur de programmes X pour les
diff�rents outils de configuration. Les autres paquetages fournissent
l'information qui leur permet d'apparaitre dans le menu du tableau de
bord.

%description -l pl
Control-panel jest programem korzystaj�cym z X Window System
uruchamiaj�cym r�ne narz�dzia konfiguracyjne. Inne pakiety same
wstawiaj� informacje, kt�re pozwalaj� wy�wietla� panelowi kontrolnemu
list� dost�pnych narz�dzi.

%description -l tr
Red Hat denetim masas�, baz� ayarlama ara�lar� i�in X programlar�
�al��t�r�c�s�d�r. Bir arac�n denetim masas�ndaki ara�lar aras�nda
g�z�kmesi i�in o ara�la ilgili paketler gerekli bilgileri denetim
masas�na bildirirler.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -I/usr/lib/glib/include -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} OWNER= install install-man
strip $RPM_BUILD_ROOT%{_bindir}/control-panel

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_applnkdir}/System/control-panel.desktop

%attr(755,root,root) %{_bindir}/control-panel

%{_libdir}/rhs/control-panel/loopy

%attr(755,root,root) %{_libdir}/rhs/control-panel/*.tcl
%{_mandir}/man8/*
