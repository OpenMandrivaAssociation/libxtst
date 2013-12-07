%define major 6
%define libname %mklibname xtst %{major}
%define devname %mklibname xtst -d

Summary:	The Xtst Library
Name:		libxtst
Version:	1.2.2
Release:	3
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXtst-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	xmlto
BuildRequires:	docbook-dtd412-xml

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

%prep
%setup -qn libXtst-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXtst.so.%{major}*

%files -n %{devname}
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XTest*
%{_datadir}/doc/libXtst

