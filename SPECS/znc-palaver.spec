%define date    %(date +"%Y%m%d")
%define module  palaver

Name:           znc-%{module}
Version:        %{date}
Release:        1%{?dist}
Summary:        Palaver ZNC Module
Group:          System Environment/Daemons
License:        GPL
URL:            https://github.com/cocodelabs/znc-palaver
Requires:       znc
BuildRequires:  gcc-c++, git, make, znc-devel

%description
Palaver ZNC module provides push notifications.

%prep
%setup -T -c
%build
git clone https://github.com/cocodelabs/znc-palaver.git
pushd %{name}
%{__make} %{?_smp_mflags}

%install
pushd %{name}
%{__install} -d -m 0755 %{buildroot}%{_libdir}/znc
%{__install} -m 0755 %{module}.so %{buildroot}%{_libdir}/znc 

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{name}/LICENSE %{name}/README.md
%{_libdir}/znc/%{module}.so

%changelog
* Sat Jan 17 2015 Taylor Kimball <taylor@linuxhq.org> - %{date}-1
- Initial build.
