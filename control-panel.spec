Summary:     Red Hat Control Panel
Summary(de): Red-Hat-Kontrollfeld
Summary(fr): Panneau de contrôle de Red Hat
Summary(pl): Panel Kontrolny
Summary(tr): Red Hat Denetim Masasý
Name:        control-panel
Version:     3.7
Release:     9
Copyright:   GPL
Group:       Utilities/System
Group(pl):   Narzêdzia/System
Source:      %{name}-%{version}.tar.gz
Patch0:      control-panel-%{version}_gtk-1.1.patch
Patch1:      control-panel-makefile.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The Red Hat control panel is an X program launcher for various configuration
tools. Other packages provide information which allow them to show up
on the control panel's menu of available tools.

%description -l de
Das Red-Hat-Kontrollfeld ist eine X-Programm-Startrampe für verschiedene 
Konfigurations-Tools. Von den Softwarepaketen gelieferte Informatinen können
im Menü der verfügbaren Tools angezeigt werden.

%description -l fr
Le tableau de bord Red Hat est un lanceur de programmes X pour les différents
outils de configuration. Les autres paquetages fournissent l'information qui
leur permet d'apparaitre dans le menu du tableau de bord.

%description -l pl
Control-panel jest programem korzystaj±cym z X Window System uruchamiaj±cym
ró¿ne narzêdzia konfiguracyjne. Inne pakiety same wstawiaj± informacje, które
pozwalaj± wy¶wietlaæ panelowi kontrolnemu listê dostêpnych narzêdzi.

%description -l tr
Red Hat denetim masasý, bazý ayarlama araçlarý için X programlarý
çalýþtýrýcýsýdýr. Bir aracýn denetim masasýndaki araçlar arasýnda gözükmesi
için o araçla ilgili paketler gerekli bilgileri denetim masasýna bildirirler.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT OWNER= install install-man
strip $RPM_BUILD_ROOT/usr/bin/control-panel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/wmconfig/control-panel

%attr(755, root, root) /usr/bin/control-panel

%{_libdir}/rhs/control-panel/loopy/*

%attr(755, root, root) %{_libdir}/rhs/control-panel/*
%{_mandir}/man8/*

%changelog
* Tue Jan 26 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [3.7-9]
- added "Group(pl)"
- fixed pl translation
- added "%config(missingok)" for wmconfig file
- simplifications and cosmetics in %%files

* Thu Nov  5 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.7-8]
- added control-panel-makefile.patch which allow build C-P from non-root
  account and allow use $RPM_OPT_FLAGS during compile.

* Sat Oct 31 1998 Przemys³aw Bia³ek <lobo@polbox.com>
- added patch for gtk-1.1.x,
- added pl translation to spec,
- changed macro %%defattr.

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binary
- built again for 5.2 b/c of the new gtk+ libs

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Erik Troan <ewt@redhat.com>
- included changes from rhad labs to update things for new gtk

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed improper geometry handling

* Tue Nov  4 1997 Otto Hammersmith <otto@redhat.com>
- control panel now obeys the -geometry option

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- updated version... added bindings.tcl

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- added loopy files
- updated version

* Fri Oct 17 1997 Otto Hammersmith <otto@redhat.com>
- Replaced the tcl/tk version with a gtk+ version in C.  No longer
  noarch... gee, what a loss.

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
