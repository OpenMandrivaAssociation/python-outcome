%define pypi_name outcome

Name:       python-%{pypi_name}
Version:    1.3.0.post0
Release:    1
Summary:    Capture the outcome of Python function calls
License:    MIT or ASL 2.0
Group:      Development/Python
URL:        https://pypi.org/project/outcome/
Source0:    https://files.pythonhosted.org/packages/source/o/outcome/outcome-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)

Requires:       python-attrs
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description 
Outcome provides a function for capturing the outcome of a Python function\
call, so that it can be passed around.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/outcome-%{version}.dist-info
%{python_sitelib}/outcome/
