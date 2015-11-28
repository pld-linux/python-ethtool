#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (enable when useful - now scripts use python2 shebang)

Summary:	Python 2 bindings to Ethernet settings
Summary(pl.UTF-8):	Wiązania Pythona 2 do ustawień sieci Ethernet
Name:		python-ethtool
Version:	0.11
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/python-ethtool/%{name}-%{version}.tar.bz2
# Source0-md5:	b505501d928debf69664b72fafa9d0c3
URL:		https://fedorahosted.org/python-ethtool/
BuildRequires:	asciidoc
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	python-devel >= 2
BuildRequires:	python-modules >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
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
install -d $RPM_BUILD_ROOT%{_sbindir}

%if %{with python2}
%py_install

cp -p pethtool.py $RPM_BUILD_ROOT%{_sbindir}/pethtool
cp -p pifconfig.py $RPM_BUILD_ROOT%{_sbindir}/pifconfig
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pethtool
%attr(755,root,root) %{_sbindir}/pifconfig
%attr(755,root,root) %{py_sitedir}/ethtool.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/ethtool-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-ethtool
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/ethtool.cpython-*.so
%{py3_sitedir}/ethtool-%{version}-py*.egg-info
%endif
