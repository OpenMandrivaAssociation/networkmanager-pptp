%define	_disable_ld_no_undefined 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for PPTP
Name:		networkmanager-pptp
Epoch:		1
Version:	0.9.8.4
Release:	4
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
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
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libpng)
Requires:	dbus
Requires:	gnome-keyring
Requires:	gtk+3
Requires:	NetworkManager
Requires:	pptp-linux
Requires:	shared-mime-info

%description
This package contains software for integrating the PPTP VPN
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-pptp-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-dependency-tracking \
	--enable-more-warnings=yes

%make

%install
%makeinstall_std

%find_lang NetworkManager-pptp

%files -f NetworkManager-pptp.lang
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-pptp-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%{_libdir}/NetworkManager/libnm-pptp-properties.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.so
%{_libexecdir}/nm-pptp-auth-dialog
%{_libexecdir}/nm-pptp-service
%{_datadir}/gnome-vpn-properties/pptp/nm-pptp-dialog.ui

