%define         __python /usr/bin/python2.7
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define         py_basever 27
%define         name python%{py_basever}-PIL

Name:           %{name} 
Version:        1.1.7
Release:        1%{?dist}
Summary:        Python Imaging Library

Group:          Development/Languages
License:        GPL
URL:            https://pypi.python.org/pypi/PIL    
Source0:        PIL-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python%{py_basever}-devel python%{py_basever}-setuptools
BuildRequires:  freetype-devel, libjpeg-devel, lcms-devel, tcl-devel, tk-devel, tkinter27
Requires:       python%{py_basever}, python%{py_basever}-setuptools
Requires:       freetype, libjpeg, lcms, tcl, tk, tkinter27

%description
Python Imaging Library

%prep
%setup -q -n PIL-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc BUILDME CHANGES CONTENTS Docs MANIFEST PKG-INFO README
%{_bindir}/pil*.py
%{_libdir}/python%{pyver}/site-packages/PIL.pth
%{_libdir}/python%{pyver}/site-packages/PIL/*

%changelog
* Mon Aug 22 2014 Taylor Kimball <taylor@linuxhq.org> - 1.1.7-1
- Initial spec.
