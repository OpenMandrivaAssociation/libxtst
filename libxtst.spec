# libxtst is used by pulseaudio, which is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 6
%define libname %mklibname xtst %{major}
%define devname %mklibname xtst -d
%define lib32name %mklib32name xtst %{major}
%define dev32name %mklib32name xtst -d

Summary:	The Xtst Library
Name:		libxtst
Version:	1.2.5
Release:	1
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXtst-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	xmlto
BuildRequires:	docbook-dtd412-xml
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libXi)
BuildRequires:	devel(libXfixes)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
The Xtst Library.

%package -n %{libname}
Summary:	The Xtst Library
Group:		Development/X11

%description -n %{libname}
The Xtst Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(xi)
Provides:	libxtst-devel = %{version}-%{release}
Obsoletes:	%{_lib}xtst6-devel < 1.2.1
Obsoletes:	%{_lib}xtst-static-devel < 1.2.1

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	The Xtst Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
The Xtst Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Requires:	devel(libXi)

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXtst-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXtst.so.%{major}*

%files -n %{devname}
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_includedir}/X11/extensions/*.h
%doc %{_mandir}/man3/XTest*
%doc %{_datadir}/doc/libXtst

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXtst.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXtst.so
%{_prefix}/lib/pkgconfig/xtst.pc
%endif
