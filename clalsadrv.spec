%define name	clalsadrv

%define major	2
%define libname %mklibname %name %major
%define oldlibname %mklibname %name 1

Name:		%{name}
Summary:	C++ access library for ALSA
Version:	2.0.0
Release:	2
Source:		http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:		http://www.kokkinizita.net/linuxaudio/
License:	GPLv2
Group:		System/Libraries
BuildRequires:	pkgconfig(alsa)

%description
C++ access library for ALSA

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Provides:	%name
Obsoletes:	%name = %version-%release
Conflicts:	%oldlibname

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel
Conflicts:	%oldlibname-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
cd libs
sed -i -e 's/\-O2/\$\(RPM_OPT_FLAGS\)/' Makefile
sed -i -e 's/\/sbin\/ldconfig/#\/sbin\/ldconfig/g' Makefile

%build
cd libs
%make
										
%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
cd libs
make install PREFIX=%{buildroot}/%{_prefix}

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname}-devel
%doc AUTHORS
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sat Jul 24 2010 Frank Kober <emuse@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 558116
- new major version 2.0.0
 o replace patches by sed scripts
 o add old lib version to conflicts
 o update url

  + Sandro Cazzaniga <kharec@mandriva.org>
    - remove obsoletes sources

* Fri Jun 12 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.2.2-2mdv2010.0
+ Revision: 385597
- rebuild

* Thu Jun 19 2008 Austin Acton <austin@mandriva.org> 1.2.2-1mdv2009.0
+ Revision: 226108
- new version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2008.1
+ Revision: 123177
- kill re-definition of %%buildroot on Pixel's request

  + Austin Acton <austin@mandriva.org>
    - Import clalsadrv



* Wed Jan 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-3mdk
- fix buildrequires (and thus building on x86_64)

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-2mdk
- Fix BuildRequires
- %%mkrel

* Wed Aug 24 2005 Austin Acton <austin@mandriva.org> 1.0.1-1mdk
- initial package
