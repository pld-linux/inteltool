%define		_svn_rev		4190
Summary:	Utility for recognize Intel HW (chipset/CPU) configuration information
Summary(pl.UTF-8):	Narzędzie do rozpoznawania informacji konfiguracyjnych w sprzęcie Intela (chipset/CPU)
Name:		inteltool
Version:	1.0
Release:	0.%{_svn_rev}_svn.1
License:	GPL v2
Group:		Applications/System
Source0:	%{name}-%{version}-%{release}.tar.lzma
# Source0-md5:	5e6c3cece09a60ac0a2373a05167f3d3
URL:		http://www.coreboot.org/Inteltool
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
Inteltool is a small utility that provides some information about the
Intel  CPU/chipset  hardware  configuration  (register contents, MSRs
[need loading 'msr' kernel module], etc).

%description -l pl.UTF-8
Inteltool  to  podręczne  narzędzie  dostarczajace  informacji o
konfiguracji sprzętowej chipsetu/CPU Intela (zawartość rejestrów,
MSR-y [potrzebne załadowanie modułu jądra 'msr'] itp.).

%prep
%setup -q

%build
%{__make} \
	CC='%{__cc}' \
	CFLAGS='%{rpmcflags}' \
	LDFLAGS='%{rpmldflags} -lpci -lz'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
