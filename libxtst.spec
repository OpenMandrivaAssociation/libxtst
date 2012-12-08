%define major 6
%define libname %mklibname xtst %{major}
%define develname %mklibname xtst -d

Name:		libxtst
Summary:	The Xtst Library
Version:	1.2.1
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXtst-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	xmlto
BuildRequires:	docbook-dtd412-xml

%description
The Xtst Library

%package -n %{libname}
Summary:	The Xtst Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
The Xtst Library

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} >= %{version}-%{release}
Provides:	libxtst-devel = %{version}-%{release}
Obsoletes:	%{_lib}xtst6-devel < 1.2.1
Obsoletes:	%{_lib}xtst-static-devel < 1.2.1
Conflicts:	libxorg-x11-devel < 7.0
Conflicts:	x11-proto-devel < 7.5

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



%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.1-1
+ Revision: 783976
- version update 1.2.1

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-4
+ Revision: 745766
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3
+ Revision: 662430
- mass rebuild

* Sat Feb 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 638710
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Sat Oct 30 2010 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 590464
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Sat Nov 14 2009 Funda Wang <fwang@mandriva.org> 1.1.0-2mdv2010.1
+ Revision: 465976
- xtst should requires xi

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464157
- Add xmlto to BuildRequires
- New version: 1.1.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-4mdv2010.0
+ Revision: 425938
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 223088
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 153778
- Update BuildRequires and submit

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 65412
- new upstream version

* Fri Jun 22 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.2-1mdv2008.0
+ Revision: 43195
- new upstream version: 1.0.2

