Summary:	Flash animations redering library
Summary(pl):	Biblioteka renderuj±ca animacje flash
Name:		swfdec
Version:	0.2.2
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	08c60d18f350c68c4b938dc29e9b1191
Patch0:		%{name}-configure.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-mozilla1.4.patch
Patch3:		%{name}-types.patch
URL:		http://swfdec.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.1.2
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	libtool
BuildRequires:	mozilla-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libswfdec0

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles most Flash 3 animations and some Flash 4. No interactivity is
supported yet.

%description -l pl
Biblioteka libswfdec przeznaczona jest do odtwarzania animacji flash.
Obecnie potrafi wy¶wietliæ wiêkszo¶æ animacji Flash 3 i czê¶æ Flash 4.
Interaktywnosæ nie jest jeszcze obs³ugiwana.

%package devel
Summary:	Header file required to build programs using swfdec library
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce swfdec
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libswfdec0-devel

%description devel
Header files required to build programs using swfdec library.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
biblioteki swfdec.

%package static
Summary:	Static swfdec library
Summary(pl):	Statyczna biblioteka swfdec
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static swfdec library.

%description static -l pl
Statyczna biblioteka swfdec.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla plugin for Flash rendering
Summary(pl):	Wtyczka mozilli wu¶wietlaj±ca animacje flash
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-plugin-%{name}
Mozilla plugin for rendering of Flash animations based on swfdec library.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka mozilli wy¶wietlaj±ca animacje flash bazuj±ca na bibliotece swfdec.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO README Change*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-*/*/loaders/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/lib*.so
