#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_with	vivified	# build (internal) Vivified Flash Debugger
#
Summary:	Flash animations redering library
Summary(pl.UTF-8):	Biblioteka renderująca animacje flash
Name:		swfdec
Version:	0.6.6
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://swfdec.freedesktop.org/download/swfdec/0.6/%{name}-%{version}.tar.gz
# Source0-md5:	3e91d48e0b8b839e12ff8f9ced4b5040
URL:		http://swfdec.freedesktop.org/wiki/
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.6
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gstreamer-devel >= 0.10.11
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.17
%{?with_vivified:BuildRequires:	gtk+2-devel >= 2:2.11.6}
BuildRequires:	gtk+2-devel >= 2:2.8.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	liboil-devel >= 0.3.9
BuildRequires:	libsoup-devel >= 2.2.100
BuildRequires:	libtool
%{?with_vivified:BuildRequires:	ming-devel >= 0.4.0-0.beta5}
BuildRequires:	pango-devel >= 1:1.10.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	zlib-devel >= 1.1.4
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
Requires:	cairo-devel >= 1.2.0
Requires:	ffmpeg-devel
Requires:	glib2-devel >= 1:2.10.0
Requires:	gstreamer-devel >= 0.10.11
Requires:	libmad-devel >= 0.14.2b
Requires:	liboil-devel >= 0.3.9
Requires:	pango-devel >= 1:1.10.0
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

%package icons
Summary:	swfdec icons for GNOME integration
Summary(pl.UTF-8):	Ikony swfdec do integracji z GNOME
Group:		X11/Applications/Multimedia
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme

%description icons
swfdec icons for GNOME integration.

%description icons -l pl.UTF-8
Ikony swfdec do integracji z GNOME.

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
	--enable-ffmpeg \
	--enable-gstreamer \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--enable-gtk \
	--enable-mad \
	%{?with_vivified:--enable-vivified} \
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post icons
%update_icon_cache hicolor

%postun icons
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libswfdec-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswfdec-0.6.so.90

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-0.6.so
%{_libdir}/libswfdec-0.6.la
%dir %{_includedir}/swfdec-0.6
%{_includedir}/swfdec-0.6/swfdec
%{_pkgconfigdir}/swfdec-0.6.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-0.6.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswfdec-gtk-0.6.so.90

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-0.6.so
%{_libdir}/libswfdec-gtk-0.6.la
%{_includedir}/swfdec-0.6/swfdec-gtk
%{_pkgconfigdir}/swfdec-gtk-0.6.pc

%files gtk-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-0.6.a

%files icons
%defattr(644,root,root,755)
%{_iconsdir}/hicolor/*/apps/swfdec.*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/swfdec
%endif
