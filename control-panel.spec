Summary:     Red Hat Control Panel
Summary(de): Red-Hat-Kontrollfeld
Summary(fr): Panneau de contr�le de Red Hat
Summary(pl): Panel Kontrolny
Summary(tr): Red Hat Denetim Masas�
Name:        control-panel
Version:     3.7
Release:     9
Copyright:   GPL
Group:       Utilities/System
Group(pl):   Narz�dzia/System
Source:      %{name}-%{version}.tar.gz
Patch0:      control-panel-%{version}_gtk-1.1.patch
Patch1:      control-panel-makefile.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The Red Hat control panel is an X program launcher for various configuration
tools. Other packages provide information which allow them to show up
on the control panel's menu of available tools.

%description -l de
Das Red-Hat-Kontrollfeld ist eine X-Programm-Startrampe f�r verschiedene 
Konfigurations-Tools. Von den Softwarepaketen gelieferte Informatinen k�nnen
im Men� der verf�gbaren Tools angezeigt werden.

%description -l fr
Le tableau de bord Red Hat est un lanceur de programmes X pour les diff�rents
outils de configuration. Les autres paquetages fournissent l'information qui
leur permet d'apparaitre dans le menu du tableau de bord.

%description -l pl
Control-panel jest programem korzystaj�cym z X Window System uruchamiaj�cym
r�ne narz�dzia konfiguracyjne. Inne pakiety same wstawiaj� informacje, kt�re
pozwalaj� wy�wietla� panelowi kontrolnemu list� dost�pnych narz�dzi.

%description -l tr
Red Hat denetim masas�, baz� ayarlama ara�lar� i�in X programlar�
�al��t�r�c�s�d�r. Bir arac�n denetim masas�ndaki ara�lar aras�nda g�z�kmesi
i�in o ara�la ilgili paketler gerekli bilgileri denetim masas�na bildirirler.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT OWNER= install install-man
strip $RPM_BUILD_ROOT%{_bindir}/control-panel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(missingok) /etc/X11/wmconfig/control-panel

%attr(755,root,root) %{_bindir}/control-panel

%{_libdir}/rhs/control-panel/loopy/*

%attr(755,root,root) %{_libdir}/rhs/control-panel/*
%{_mandir}/man8/*
