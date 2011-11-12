%define nm_version          0.9.2.0
%define dbus_version        0.74
%define gtk2_version        2.12
%define shared_mime_version 0.16-3

Summary: NetworkManager VPN integration for PPTP
Name: networkmanager-pptp
Epoch:   1
Version: 0.9.2.0
Release: %mkrel 1
License: GPLv2+
URL: http://www.gnome.org/projects/NetworkManager/
Group: System/Base
# How to build the source package:
# - Check out NetworkManager from Gnome SVN, currently trunk is used
# - cd NetworkManager/vpn-daemons/pptp
# - ./autogen.sh --prefix=/usr --sysconfdir=/etc
# - make distclean
# - cd ..
# - mv pptp NetworkManager-pptp-%{version}
# - tar cvfz NetworkManager-pptp-%{version}.tar.gz NetworkManager-pptp-%{version}
Source: http://download.gnome.org/sources/NetworkManager-pptp/0.9/NetworkManager-pptp-%{version}.tar.xz
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: dbus-glib-devel >= %{dbus_version}
BuildRequires: libnm-util-devel >= %{nm_version}
BuildRequires: libnm-glib-devel >= %{nm_version}
BuildRequires: libnm-glib-vpn-devel >= %{nm_version}
BuildRequires: gtk2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: perl-XML-Parser
BuildRequires: libtool intltool gettext
BuildRequires: perl
BuildRequires: gnome-common
BuildRequires: ppp-devel
Requires: gtk2             >= %{gtk2_version}
Requires: dbus             >= %{dbus_version}
Requires: NetworkManager   >= %{nm_version}
Requires: shared-mime-info >= %{shared_mime_version}
Requires: gnome-keyring
Requires: pptp-linux
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This package contains software for integrating the PPTP VPN
with NetworkManager and the GNOME desktop.

%prep
%setup -q -n NetworkManager-pptp-%{version}

%build
if [ ! -f configure ]; then
  ./autogen.sh
fi
%configure2_5x --disable-static --disable-dependency-tracking
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-pptp

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f NetworkManager-pptp.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog README
%{_libdir}/NetworkManager/libnm-pptp-properties.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.so
%{_libdir}/pppd/*/nm-pptp-pppd-plugin.la
%{_libexecdir}/nm-pptp-auth-dialog
%{_libexecdir}/nm-pptp-service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-pptp-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%_datadir/gnome-vpn-properties/pptp/nm-pptp-dialog.ui
