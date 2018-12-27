%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kruler
Summary:	kruler
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	55c5e5e85b5f7feb1a8df2d0d67e031f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-knotifications-devel >= 5.30.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

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
