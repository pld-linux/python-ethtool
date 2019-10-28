#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 bindings to Ethernet settings
Summary(pl.UTF-8):	Wiązania Pythona 2 do ustawień sieci Ethernet
Name:		python-ethtool
Version:	0.12
Release:	3
License:	GPL v2
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/python-ethtool/%{name}-%{version}.tar.bz2
# Source0-md5:	8089d72c9dbe0570bc2aa6ecd59e026f
Patch0:		%{name}-build.patch
URL:		https://fedorahosted.org/python-ethtool/
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
%patch0 -p1

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

cp -p pethtool.py $RPM_BUILD_ROOT%{_sbindir}/pethtool
cp -p pifconfig.py $RPM_BUILD_ROOT%{_sbindir}/pifconfig
cp -p man/{pethtool,pifconfig}.8 $RPM_BUILD_ROOT%{_mandir}/man8
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
%{_mandir}/man8/pethtool.8*
%{_mandir}/man8/pifconfig.8*
%endif

%if %{with python3}
%files -n python3-ethtool
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/ethtool.cpython-*.so
%{py3_sitedir}/ethtool-%{version}-py*.egg-info
%endif
