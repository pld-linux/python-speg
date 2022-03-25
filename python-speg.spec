#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	PEG-based parser interpreter with memoization
Summary(pl.UTF-8):	Interpreter parserów opartych na PEG z zapamiętywaniem
Name:		python-speg
Version:	0.3
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/speg/
Source0:	https://files.pythonhosted.org/packages/source/s/speg/speg-%{version}.zip
# Source0-md5:	06c714460913b0cfd73cbbc33fa93eb9
URL:		https://pypi.org/project/speg/
%if %{with python2}
BuildRequires:	python-modules >= 2
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEG-based parser interpreter with memoization.

%description -l pl.UTF-8
Interpreter parserów opartych na PEG z zapamiętywaniem.

%package -n python3-speg
Summary:	PEG-based parser interpreter with memoization
Summary(pl.UTF-8):	Interpreter parserów opartych na PEG z zapamiętywaniem
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-speg
PEG-based parser interpreter with memoization.

%description -n python3-speg -l pl.UTF-8
Interpreter parserów opartych na PEG z zapamiętywaniem.

%prep
%setup -q -n speg-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/speg
%{py_sitescriptdir}/speg-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-speg
%defattr(644,root,root,755)
%{py3_sitescriptdir}/speg
%{py3_sitescriptdir}/speg-%{version}-py*.egg-info
%endif
