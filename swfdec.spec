# TODO
# - use xulrunnerl
#
# Conditional build:
%bcond_without	gstreamer	# build without swfdec-mozilla-player
%bcond_without	gimp		# don't build gimp plugin
%bcond_with	libart		# use libarg_lgpl instead of cairo
#
Summary:	Flash animations redering library
Summary(pl.UTF-8):	Biblioteka renderująca animacje flash
Name:		swfdec
Version:	0.3.6
Release:	6
License:	GPL
Group:		Libraries
Source0:	http://www.schleef.org/swfdec/download/%{name}-%{version}.tar.gz
# Source0-md5:	bcfca3a8ce1d524ebf4d11fd511dedb8
Patch0:		%{name}-as_needed.patch
URL:		http://www.schleef.org/swfdec/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1.6
%{!?with_libart:BuildRequires:	cairo-devel >= 1.2.0}
%{?with_gimp:BuildRequires:	gimp-devel >= 1:2.3.10}
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 0.10.8
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.8
%endif
BuildRequires:	gtk+2-devel >= 2:2.10.0
%{?with_libart:BuildRequires:	libart_lgpl-devel >= 2.0}
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	liboil-devel >= 0.3.9
BuildRequires:	libtool
BuildRequires:	mozilla-firefox-devel >= 1.5.0.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	zlib-devel >= 1.1.4
Obsoletes:	libswfdec0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gimp}
%define		gimpplugindir	%(gimptool --gimpplugindir 2>/dev/null)/plug-ins
%endif

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
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{!?with_libart:Requires:	cairo-devel >= 1.2.0}
Requires:	glib2-devel >= 1:2.12.0
%{?with_libart:Requires:	libart_lgpl-devel >= 2.0}
Requires:	libmad-devel >= 0.14.2b
Requires:	liboil-devel >= 0.3.9
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

%package -n gimp-plugin-%{name}
Summary:	SWF loading file filter for the GIMP
Summary(pl.UTF-8):	Filtr wczytujący pliki SWF dla GIMP-a
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gimp-plugin-%{name}
SWF loading file filter for the GIMP.

%description -n gimp-plugin-%{name} -l pl.UTF-8
Filtr wczytujący pliki SWF dla GIMP-a.

%package -n browser-plugin-%{name}
Summary:	Browser plugin for Flash rendering
Summary(pl.UTF-8):	Wtyczka przeglądarki wyświetlająca animacje Flash
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	mozilla-plugin-swfdec

%description -n browser-plugin-%{name}
Browser plugin for rendering of Flash animations based on swfdec
library.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka przeglądarki wyświetlająca animacje Flash oparta na bibliotece
swfdec.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gstreamer:--disable-mozilla-plugin} \
	%{?with_libart:--with-backend=libart}

%{__make} \
	gimpdir=%{gimpplugindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_browserpluginsdir} \
	gimpdir=%{gimpplugindir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-*/*/loaders/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%if %{with gstreamer}
# TODO: move to base browser plugin package
%attr(755,root,root) %{_bindir}/swfdec-mozilla-player
%endif
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

%if %{with gimp}
%files -n gimp-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/swf
%endif

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libswfdecmozilla.so
