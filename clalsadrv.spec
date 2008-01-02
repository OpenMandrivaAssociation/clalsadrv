%define name	clalsadrv
%define version	1.0.1
%define release %mkrel 3

%define major	1
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	C++ access library for ALSA
Version: 	%{version}
Release: 	%{release}

Source:		http://users.skynet.be/solaris/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:		http://users.skynet.be/solaris/linuxaudio/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  alsa-lib-devel

%description
C++ access library for ALSA

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Provides:	%name
Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q
perl -pi -e 's/\-O2/\$\(RPM_OPT_FLAGS\)/' Makefile

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_libdir
mkdir -p %buildroot/%_includedir
make install CLALSADRV_LIBDIR=%buildroot/%_libdir CLALSADRV_INCDIR=%buildroot/%_includedir

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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
