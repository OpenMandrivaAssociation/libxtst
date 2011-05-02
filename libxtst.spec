%define libname %mklibname xtst 6
%define develname %mklibname xtst -d
%define staticname %mklibname xtst -s -d

Name: libxtst
Summary:  The Xtst Library
Version: 1.2.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXtst-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxi-devel >= 1.3
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: xmlto docbook-dtd412-xml

%description
The Xtst Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The Xtst Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The Xtst Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} >= %{version}-%{release}
Requires: x11-proto-devel >= 7.5
Requires: libxi-devel >= 1.3
Provides: libxtst-devel = %{version}-%{release}
Provides: libxtst6-devel = %{version}-%{release}
Obsoletes: %{mklibname xtst 6 -d}

Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXtst.so
%{_libdir}/libXtst.la
%{_libdir}/pkgconfig/xtst.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XTest*
%{_datadir}/doc/libXtst

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} >= %{version}-%{release}
Provides: libxtst-static-devel = %{version}-%{release}
Provides: libxtst6-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xtst 6 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXtst.a

#-----------------------------------------------------------

%prep
%setup -q -n libXtst-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXtst.so.6
%{_libdir}/libXtst.so.6.1.0
