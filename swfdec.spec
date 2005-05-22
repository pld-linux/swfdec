Summary:	Flash animations redering library
Summary(pl):	Biblioteka renderuj±ca animacje flash
Name:		swfdec
Version:	0.3.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.schleef.org/swfdec/download/%{name}-%{version}.tar.gz
# Source0-md5:	cc40397d7784efee549fb7853b01cac3
Patch0:		%{name}-configure.patch
URL:		http://www.schleef.org/swfdec/
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1.6
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRequires:	gstreamer-devel >= 0.8.0
BuildRequires:	gstreamer-GConf-devel >= 0.8.0
# gstreamer-interfaces-0.8
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
BuildRequires:	gtk+2-devel >= 1:2.1.2
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	liboil-devel >= 0.3.0
BuildRequires:	libtool
BuildRequires:	mozilla-devel >= 2:1.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel >= 1.1.4
Obsoletes:	libswfdec0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles most Flash 3 animations and some Flash 4. No interactivity is
supported yet.

%description -l pl
Biblioteka libswfdec przeznaczona jest do odtwarzania animacji flash.
Obecnie potrafi wy¶wietliæ wiêkszo¶æ animacji Flash 3 i czê¶æ Flash 4.
Interaktywno¶æ nie jest jeszcze obs³ugiwana.

%package devel
Summary:	Header file required to build programs using swfdec library
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce swfdec
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Requires:	libart_lgpl-devel >= 2.0
Requires:	libmad-devel >= 0.14.2b
Requires:	liboil-devel >= 0.3.0
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

%package -n gimp-plugin-%{name}
Summary:	SWF loading file filter for the GIMP
Summary(pl):	Filtr wczytuj±cy pliki SWF dla GIMP-a
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gimp-plugin-%{name}
SWF loading file filter for the GIMP.

%description -n gimp-plugin-%{name} -l pl
Filtr wczytuj±cy pliki SWF dla GIMP-a.

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	gimpdir=%{gimpplugindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gimpdir=%{gimpplugindir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-*/*/loaders/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO README Change*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libswfdec-*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/loaders/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-*.so
%{_libdir}/libswfdec-*.la
%{_includedir}/swfdec-*
%{_pkgconfigdir}/swfdec-*.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswfdec-*.a

%files -n gimp-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/swf

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/libswfdecmozilla.so
