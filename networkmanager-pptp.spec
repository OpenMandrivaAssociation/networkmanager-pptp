# How to build the source package:
# - Check out NetworkManager from Gnome SVN, currently trunk is used
# - cd NetworkManager/vpn-daemons/pptp
# - ./autogen.sh --prefix=/usr --sysconfdir=/etc
# - make distclean
# - cd ..
# - mv pptp NetworkManager-pptp-%{version}
# - tar cvfz NetworkManager-pptp-%{version}.tar.gz NetworkManager-pptp-%{version}

%define nm_version          0.9.2.0
%define dbus_version        0.74
%define gtk2_version        2.12
%define shared_mime_version 0.16-3

Summary:	NetworkManager VPN integration for PPTP
Name:		networkmanager-pptp
Epoch:		1
Version:	0.9.2.0
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-pptp/NetworkManager-pptp-%{version}.tar.xz
# ubuntu
Patch0:	gtk_table_to_gtk_grid.patch

BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: perl-XML-Parser
BuildRequires: perl
BuildRequires: ppp-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libpng15)
Requires: gtk+3
Requires: dbus
Requires: gtk2             >= %{gtk2_version}
Requires: dbus             >= %{dbus_version}
Requires: NetworkManager   >= %{nm_version}
Requires: shared-mime-info >= %{shared_mime_version}
Requires: gnome-keyring
Requires: pptp-linux

%description
This package contains software for integrating the PPTP VPN
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-pptp-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-dependency-tracking

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-pptp

%files -f NetworkManager-pptp.lang
%doc AUTHORS ChangeLog README
%{_libdir}/NetworkManager/libnm-pptp-properties.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.la
%{_libexecdir}/nm-pptp-auth-dialog
%{_libexecdir}/nm-pptp-service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-pptp-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%_datadir/gnome-vpn-properties/pptp/nm-pptp-dialog.ui

