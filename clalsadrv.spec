%define name	clalsadrv
%define version	2.0.0
%define release %mkrel 1

%define major	2
%define libname %mklibname %name %major
%define oldlibname %mklibname %name 1

Name:		%{name}
Summary:	C++ access library for ALSA
Version:	%{version}
Release:	%{release}

Source:		http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:		http://www.kokkinizita.net/linuxaudio/
License:	GPLv2
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	alsa-lib-devel

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
Libraries and includes files for developing programs based on %name.

%prep
%setup -q
cd libs
sed -i -e 's/\-O2/\$\(RPM_OPT_FLAGS\)/' Makefile
sed -i -e 's/\/sbin\/ldconfig/#\/sbin\/ldconfig/g' Makefile

%build
cd libs
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_libdir
mkdir -p %buildroot/%_includedir
cd libs
make install PREFIX=%buildroot/%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS
%{_includedir}/*
%{_libdir}/*.so
#%{_libdir}/*.a
#%{_libdir}/*.la
