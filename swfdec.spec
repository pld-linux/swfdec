#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	gnomevfs	# without gnome-vfs support
#
Summary:	Flash animations redering library
Summary(pl.UTF-8):	Biblioteka renderująca animacje flash
Name:		swfdec
Version:	0.4.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://swfdec.freedesktop.org/download/swfdec/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	7f69ae821c6002a857d99656758e8c0b
URL:		http://swfdec.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.6
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.14.0}
BuildRequires:	gstreamer-devel >= 0.10.11
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	liboil-devel >= 0.3.9
BuildRequires:	libtool
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
Requires:	glib2-devel >= 1:2.8.0
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
%{?with_gnomevfs:Requires:	gnome-vfs2-devel >= 2.14.0}
Requires:	gtk+2-devel >= 2:2.8.0

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
	%{!?with_gnomevfs:--disable-gnome-vfs} \
	--enable-ffmpeg \
	--enable-gstreamer \
	--%{?with_apidocs:en}%{?!with_apidocs:dis}able-gtk-doc \
	--enable-gtk \
	--enable-mad \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libswfdec-0.4.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-0.4.so
%{_libdir}/libswfdec-0.4.la
%dir %{_includedir}/swfdec-0.4
%{_includedir}/swfdec-0.4/libswfdec
%{_pkgconfigdir}/swfdec-0.4.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-0.4.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-0.4.so.*.*

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-0.4.so
%{_libdir}/libswfdec-gtk-0.4.la
%{_includedir}/swfdec-0.4/libswfdec-gtk
%{_pkgconfigdir}/swfdec-gtk-0.4.pc

%files gtk-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-gtk-0.4.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/swfdec
%endif
