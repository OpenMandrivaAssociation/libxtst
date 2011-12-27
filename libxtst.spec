%define major 6
%define libname %mklibname xtst %{major}
%define develname %mklibname xtst -d

Name: libxtst
Summary:  The Xtst Library
Version: 1.2.0
Release: 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXtst-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxi-devel >= 1.3
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: xmlto
BuildRequires: docbook-dtd412-xml

%description
The Xtst Library

%package -n %{libname}
Summary:  The Xtst Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The Xtst Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} >= %{version}-%{release}
Provides: libxtst-devel = %{version}-%{release}
Obsoletes: %{_lib}xtst6-devel
Obsoletes: %{_lib}xtst-static-devel
Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXtst-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXtst.so.%{major}*

%files -n %{develname}
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XTest*
%{_datadir}/doc/libXtst

