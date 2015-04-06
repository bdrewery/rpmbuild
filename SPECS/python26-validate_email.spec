%define         __python /usr/bin/python2.6
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define         py_basever 26
%define         real_name python-validate_email
%define         name python%{py_basever}-validate_email
%define         __os_install_post %{nil}

Name:           %{name} 
Version:        1.2
Release:        1%{?dist}
Summary:        Verify if an email address is valid and really exists.

Group:          Development/Languages
License:        GPL
URL:            http://pypi.python.org/pypi/validate_email/           
Source0:        validate_email-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{py_basever}-devel python%{py_basever}-setuptools
Requires:       python%{py_basever}-setuptools
Requires:       python%{py_basever}


%description
Validate_email is a package for Python that check if an email is valid, properly
formatted and really exists.

%prep
%setup -q -n validate_email-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} --install-data=%{_datadir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE MANIFEST.in PKG-INFO README.rst setup.*
%{python_sitelib}/validate_email-%{version}-py%{pyver}.egg-info
%{python_sitelib}/validate_email.py
%{python_sitelib}/validate_email.pyc

%changelog
* Mon Aug 04 2014 Taylor Kimball <taylor@linuxhq.org> - 1.2-1
- Initial spec.
