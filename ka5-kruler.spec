#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kruler
Summary:	kruler
Name:		ka5-%{kaname}
Version:	22.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	382d297411461a87e40ae812ef0272a9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRuler displays on screen a ruler measuring pixels. Position the 0 to
your starting point (simple drag it), and read off the precise pixel
count to your cursor. To change the length of the ruler just drag the
sides.

%description -l pl.UTF-8
KRuler wyświetla na ekranie linijkę mierzącą liczbę pikseli. Ustaw 0
w punkcie startowym (po prostu przeciągnij ją) i odczytaj precyzyjną
liczbę pikseli do kursora. Aby zmienic długość linijki, przeciągnij
jej boki.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_desktopdir}/org.kde.kruler.desktop
%{_iconsdir}/hicolor/128x128/apps/kruler.png
%{_iconsdir}/hicolor/16x16/actions/kruler-east.png
%{_iconsdir}/hicolor/16x16/actions/kruler-north.png
%{_iconsdir}/hicolor/16x16/actions/kruler-south.png
%{_iconsdir}/hicolor/16x16/actions/kruler-west.png
%{_iconsdir}/hicolor/16x16/apps/kruler.png
%{_iconsdir}/hicolor/22x22/actions/kruler-east.png
%{_iconsdir}/hicolor/22x22/actions/kruler-north.png
%{_iconsdir}/hicolor/22x22/actions/kruler-south.png
%{_iconsdir}/hicolor/22x22/actions/kruler-west.png
%{_iconsdir}/hicolor/22x22/apps/kruler.png
%{_iconsdir}/hicolor/32x32/apps/kruler.png
%{_iconsdir}/hicolor/48x48/apps/kruler.png
%{_iconsdir}/hicolor/64x64/apps/kruler.png
%{_datadir}/knotifications5/kruler.notifyrc
%{_datadir}/kruler
%{_datadir}/metainfo/org.kde.kruler.appdata.xml
