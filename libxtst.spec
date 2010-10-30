%define libxtst %mklibname xtst 6
Name: libxtst
Summary:  The Xtst Library
Version: 1.2.0
Release: %mkrel 1
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
BuildRequires: xmlto

%description
The Xtst Library

#-----------------------------------------------------------

%package -n %{libxtst}
Summary:  The Xtst Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxtst}
The Xtst Library

#-----------------------------------------------------------

%package -n %{libxtst}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxtst} >= %{version}
Requires: x11-proto-devel >= 7.5
Requires: libxi-devel >= 1.3
Provides: libxtst-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

%description -n %{libxtst}-devel
Development files for %{name}

%files -n %{libxtst}-devel
%defattr(-,root,root)
%{_libdir}/libXtst.so
%{_libdir}/libXtst.la
%{_libdir}/pkgconfig/xtst.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XTest*

#-----------------------------------------------------------

%package -n %{libxtst}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxtst}-devel >= %{version}
Provides: libxtst-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxtst}-static-devel
Static development files for %{name}

%files -n %{libxtst}-static-devel
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

%files -n %{libxtst}
%defattr(-,root,root)
%{_libdir}/libXtst.so.6
%{_libdir}/libXtst.so.6.1.0
