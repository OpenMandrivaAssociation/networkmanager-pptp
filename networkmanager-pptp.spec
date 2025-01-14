%define	_disable_ld_no_undefined 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for PPTP
Name:		networkmanager-pptp
Version:	1.2.12
Release:	2
License:	GPLv2+
Group:		System/Base
Url:		https://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-pptp/%{url_ver}/NetworkManager-pptp-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	perl
BuildRequires:	ppp-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnma)
Requires:	dbus
Requires:	NetworkManager
Requires:	pptp-linux
Requires:	shared-mime-info

%description
This package contains software for integrating the PPTP VPN
with NetworkManager.

%package gtk
Summary:        GTK frontend for configuring PPTP connections with NetworkManager
Group:          Tools
Requires:       %{name} = %{EVRD}
Supplements:    networkmanager-applet

%description gtk
GTK frontend for configuring PPTP connections with NetworkManager

%prep
%autosetup -p1 -n NetworkManager-pptp-%{version}

%build
%configure \
	--disable-static \
	--disable-dependency-tracking \
	--without-libnm-glib \
	--with-gtk4 \
	--enable-more-warnings=yes

%make_build

%install
%make_install

%find_lang NetworkManager-pptp

%files -f NetworkManager-pptp.lang
%doc AUTHORS README
%{_datadir}/dbus-1/system.d/nm-pptp-service.conf
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.so
%{_libexecdir}/nm-pptp-service
%{_prefix}/lib/NetworkManager/VPN/nm-pptp-service.name
%{_datadir}/metainfo/network-manager-pptp.metainfo.xml

%files gtk
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-pptp-editor.so
%{_libexecdir}/nm-pptp-auth-dialog
