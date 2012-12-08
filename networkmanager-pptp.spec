# How to build the source package:
# - Check out NetworkManager from Gnome SVN, currently trunk is used
# - cd NetworkManager/vpn-daemons/pptp
# - ./autogen.sh --prefix=/usr --sysconfdir=/etc
# - make distclean
# - cd ..
# - mv pptp NetworkManager-pptp-%{version}
# - tar cvfz NetworkManager-pptp-%{version}.tar.gz NetworkManager-pptp-%{version}

%define nm_version          0.9.6.0
%define dbus_version        0.74
%define gtk3_version        3.0
%define shared_mime_version 0.16-3

Summary:	NetworkManager VPN integration for PPTP
Name:		networkmanager-pptp
Epoch:		1
Version:	0.9.6.0
Release:	2
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-pptp/NetworkManager-pptp-%{version}.tar.xz
# ubuntu
# Patch0:	gtk_table_to_gtk_grid.patch

BuildRequires: gettext
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
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libpng15)
Requires: dbus
Requires: gtk+3            >= %{gtk3_version}
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
	--disable-dependency-tracking \
	--enable-more-warnings=yes

%make

%install
%makeinstall_std

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang NetworkManager-pptp

%files -f NetworkManager-pptp.lang
%doc AUTHORS ChangeLog README
%{_libdir}/NetworkManager/libnm-pptp-properties.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.so
%{_libexecdir}/nm-pptp-auth-dialog
%{_libexecdir}/nm-pptp-service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-pptp-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%_datadir/gnome-vpn-properties/pptp/nm-pptp-dialog.ui


%changelog

* Wed Aug 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:0.9.6.0-1
+ Revision: 812562
- update to new version 0.9.6.0

* Sat Feb 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:0.9.2.0-1
+ Revision: 780680
- moved to build 0.9.2.0
- added p0 to fix gtk3 deprecated build failures
- cleaned up spec

* Sun Nov 13 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.8.6.0-1
+ Revision: 730416
- 0.8.6.0
- 0.9.2.0

* Thu Apr 21 2011 Funda Wang <fwang@mandriva.org> 1:0.8.4-1
+ Revision: 656419
- new version 0.8.4

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 1:0.8.3.999-1
+ Revision: 650806
- updat file list
- update to new version 0.8.3.999

* Tue Dec 21 2010 Eugeni Dodonov <eugeni@mandriva.com> 1:0.8.2-1mdv2011.0
+ Revision: 623647
- Add ppp-devel BR
- Added networkmanager-pptp 0.8.2 (thanks to Alexandre Lissy, #61954).
- Created package structure for networkmanager-pptp.

