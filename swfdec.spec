Summary:	Flash animations redering library
Summary(pl):	Biblioteka renderuj±ca animacje flash
Name:		swfdec
Version:	0.1.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://swfdec.sourceforge.net/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
URL:		http://swfdec.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	mad-devel >= 0.14.2b
BuildRequires:	mozilla-devel >= 1.0.0
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
Requires:	%{name} = %{version}
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
Requires:	%{name}-devel = %{version}

%description static
Static swfdec library.

%description static -l pl
Statyczna biblioteka swfdec.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla plugin for Flash rendering
Summary(pl):	Wtyczka mozilli wu¶wietlaj±ca animacje flash
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description -n mozilla-plugin-%{name}
Mozilla plugin for rendering of Flash animations based on swfdec library.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka mozilli wy¶wietlaj±ca animacje flash bazuj±ca na bibliotece swfdec.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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

sed -e 's,include/swfdec,include,g' swfdec.pc \
       > $RPM_BUILD_ROOT%{_pkgconfigdir}/swfdec.pc 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO README Change*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

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
