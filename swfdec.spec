#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_with	pulseaudio	# use pulseaudio instead of alsa
%bcond_with	vivified	# build (internal) Vivified Flash Debugger
#
Summary:	Flash animations rendering library
Summary(pl.UTF-8):	Biblioteka renderująca animacje flash
Name:		swfdec
%define	majver	0.9
Version:	%{majver}.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://swfdec.freedesktop.org/download/swfdec/%{majver}/%{name}-%{version}.tar.gz
# Source0-md5:	7be5e39236e2d6efa61a18e83e5ab73d
URL:		http://swfdec.freedesktop.org/wiki/
%{!?with_pulseaudio:BuildRequires:	alsa-lib-devel >= 1.0}
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.6
BuildRequires:	cairo-devel >= 1.6.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	gstreamer0.10-devel >= 0.10.11
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.17
%{?with_vivified:BuildRequires:	gtk+2-devel >= 2:2.11.6}
BuildRequires:	gtk+2-devel >= 2:2.8.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
BuildRequires:	liboil-devel >= 0.3.9
BuildRequires:	libsoup-devel >= 2.2.100
BuildRequires:	libtool
%{?with_vivified:BuildRequires:	ming-devel >= 0.4.0-0.beta5}
BuildRequires:	pango-devel >= 1:1.16
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	zlib-devel >= 1.1.4
Requires:	cairo >= 1.6.0
Requires:	glib2 >= 1:2.16
Requires:	gstreamer0.10 >= 0.10.11
Requires:	gstreamer0.10-plugins-base >= 0.10.17
Requires:	liboil >= 0.3.9
Requires:	pango >= 1:1.16
Obsoletes:	gimp-plugin-swfdec
Obsoletes:	libswfdec0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles most Flash 3 animations and some Flash 4. No interactivity is
supported yet.

%description -l pl.UTF-8
Biblioteka libswfdec przeznaczona jest do odtwarzania animacji flash.
Obecnie potrafi wyświetlić większość animacji Flash 3 i część Flash 4.
Interaktywność nie jest jeszcze obsługiwana.

%package devel
Summary:	Header file required to build programs using swfdec library
Summary(pl.UTF-8):	Pliki nagłówkowe wymagane przez programy używające swfdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.6.0
Requires:	glib2-devel >= 1:2.16
Requires:	gstreamer0.10-devel >= 0.10.11
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.17
Requires:	liboil-devel >= 0.3.9
Requires:	pango-devel >= 1:1.16
Obsoletes:	libswfdec0-devel

%description devel
Header files required to build programs using swfdec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
biblioteki swfdec.

%package static
Summary:	Static swfdec library
Summary(pl.UTF-8):	Statyczna biblioteka swfdec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static swfdec library.

%description static -l pl.UTF-8
Statyczna biblioteka swfdec.

%package gtk
Summary:	swfdec-gtk library
Summary(pl.UTF-8):	Biblioteka swfdec-gtk
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0
Requires:	gtk+2 >= 2:2.8.0
Requires:	libsoup >= 2.2.100

%description gtk
swfdec-gtk library.

%description gtk -l pl.UTF-8
Biblioteka swfdec-gtk.

%package gtk-devel
Summary:	Header files for swfdec-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki swfdec-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	alsa-lib-devel >= 1.0
Requires:	gtk+2-devel >= 2:2.8.0
Requires:	libsoup-devel >= 2.2.100

%description gtk-devel
Header files for swfdec-gtk library.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki swfdec-gtk.

%package gtk-static
Summary:	Static swfdec-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka swfdec-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static swfdec-gtk library.

%description gtk-static -l pl.UTF-8
Statyczna biblioteka swfdec-gtk.

%package apidocs
Summary:	swfdec API documetation
Summary(pl.UTF-8):	Dokumentacja API swfdec
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
swfdec API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API swfdec.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gstreamer \
	--enable-gtk \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	%{?with_vivified:--enable-vivified} \
	%{?with_pulseaudio:--with-audio=pulse} \
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libswfdec-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswfdec-%{majver}.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-%{majver}.so
%dir %{_includedir}/swfdec-%{majver}
%{_includedir}/swfdec-%{majver}/swfdec
%{_pkgconfigdir}/swfdec-%{majver}.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-%{majver}.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswfdec-gtk-%{majver}.so.2

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-%{majver}.so
%{_includedir}/swfdec-%{majver}/swfdec-gtk
%{_pkgconfigdir}/swfdec-gtk-%{majver}.pc

%files gtk-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-%{majver}.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/swfdec
%endif
