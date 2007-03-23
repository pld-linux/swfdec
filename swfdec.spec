Summary:	Flash animations redering library
Summary(pl.UTF-8):	Biblioteka renderująca animacje flash
Name:		swfdec
Version:	0.4.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://swfdec.freedesktop.org/download/swfdec/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	7a857dcc9228ac590327b04a90db2e64
URL:		http://swfdec.freedesktop.org/wiki/
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	liboil-devel >= 0.3.9
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

%package apidocs
Summary:	swfdec API documetation
Summary(pl.UTF-8):	Dokumentacja API swfdec
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
swfdec API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API swfdec.

%package devel
Summary:	Header file required to build programs using swfdec library
Summary(pl.UTF-8):	Pliki nagłówkowe wymagane przez programy używające swfdec
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.2.0
Requires:	ffmpeg-devel
Requires:	glib2-devel >= 1:2.8.0
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
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static swfdec library.

%description static -l pl.UTF-8
Statyczna biblioteka swfdec.

%prep
%setup -q

%build

%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libswfdec-*.so.*.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/swfdec

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-*.so
%{_libdir}/libswfdec-*.la
%{_includedir}/swfdec-*
%{_pkgconfigdir}/swfdec-*.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-*.a
