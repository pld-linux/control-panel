Summary:	Red Hat Control Panel
Summary(de):	Red-Hat-Kontrollfeld
Summary(fr):	Panneau de contr�le de Red Hat
Summary(pl):	Panel Kontrolny
Summary(tr):	Red Hat Denetim Masas�
Summary(pt_BR):	Painel de Controle Red Hat
Summary(es):	Panel de Control Red Hat
Summary(ru):	������� ��� ������� �������� ��������� ������� ��� X
Summary(uk):	���̦�� ��� ������� ������� ������������ ������� Ц� X
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

%description -l pt_BR
O control-panel (painel de controle) Red Hat � um programa X que
executa v�rias ferramentas de configura��o. Outros pacotes oferecem
informa��o que permitem a visualiza��o das ferramentas dispon�veis
no menu do control-panel.

%description -l es
Control-panel (panel de control) Red Hat es un programa X que
ejecuta varias herramientas de configuraci�n. Otros paquetes ofrecen
informaci�n que permiten la visualizaci�n de las herramientas
disponibles en el men� del panel de control.

%description -l ru
Control-panel - ��� ����������� �������, ����������� ��������� �������
������������ ������� ��� X.

%description -l uk
Control-panel - �� ���Ʀ��� ���̦��, ��� �������� Ҧ�����Φ�Φ ���̦��
���Ʀ��������� ������� Ц� X.

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
