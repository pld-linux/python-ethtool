#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 bindings to Ethernet settings
Summary(pl.UTF-8):	Wiązania Pythona 2 do ustawień sieci Ethernet
Name:		python-ethtool
Version:	0.14
Release:	5
License:	GPL v2
Group:		Libraries/Python
Source0:	https://github.com/fedora-python/python-ethtool/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eaf26f7aedbb1c6e3f7e0b00787b552e
URL:		https://github.com/fedora-python/python-ethtool
BuildRequires:	asciidoc
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python-devel >= 2
BuildRequires:	python-modules >= 2
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for the ethtool kernel interface, that allows
querying and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.

%description -l pl.UTF-8
Wiązania Pythona 2 do interfejsu ethtool w jądrze, pozwalającego na
odczyt i zmianę ustawień kart sieciowych Ethenet, takich jak szybkość,
port, autonegocjacja oraz lokalizacja PCI.

%package -n python3-ethtool
Summary:	Python 3 bindings to Ethernet settings
Summary(pl.UTF-8):	Wiązania Pythona 3 do ustawień sieci Ethernet
Group:		Libraries/Python

%description -n python3-ethtool
Python 3 bindings for the ethtool kernel interface, that allows
querying and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.

%description -n python3-ethtool -l pl.UTF-8
Wiązania Pythona 3 do interfejsu ethtool w jądrze, pozwalającego na
odczyt i zmianę ustawień kart sieciowych Ethenet, takich jak szybkość,
port, autonegocjacja oraz lokalizacja PCI.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT{%{_bindir}/pethtool,%{_sbindir}/pethtool2}
%{__mv} $RPM_BUILD_ROOT{%{_bindir}/pifconfig,%{_sbindir}/pifconfig2}
%endif

%if %{with python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/pethtool
%{__mv} $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/pifconfig
%endif

cp -p man/{pethtool,pifconfig}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pethtool2
%attr(755,root,root) %{_sbindir}/pifconfig2
%{py_sitedir}/ethtool-%{version}-py*.egg-info
%attr(755,root,root) %{py_sitedir}/ethtool.so
%endif

%if %{with python3}
%files -n python3-ethtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pethtool
%attr(755,root,root) %{_sbindir}/pifconfig
%attr(755,root,root) %{py3_sitedir}/ethtool.cpython-*.so
%{py3_sitedir}/ethtool-%{version}-py*.egg-info
%{_mandir}/man8/pethtool.8*
%{_mandir}/man8/pifconfig.8*
%endif
