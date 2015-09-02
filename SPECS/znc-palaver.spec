%global date 20150824
%global git_commit 0c2891b4d753031011e5ac1d827b1f5690841cce
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

Name:           znc-palaver
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Palaver ZNC Module
Group:          System Environment/Daemons
License:        GPL
URL:            https://github.com/cocodelabs/znc-palaver
Source0:        https://github.com/cocodelabs/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       znc
BuildRequires:  gcc-c++, git, make, znc-devel

%description
Palaver ZNC module provides push notifications.

%prep
%setup -q -n %{name}-%{git_commit}
%build
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/znc
%{__install} -m 0755 %{module}.so %{buildroot}%{_libdir}/znc 

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{name}/LICENSE %{name}/README.md
%{_libdir}/znc/%{module}.so

%changelog
* Mon Aug 24 2015 Taylor Kimball <taylor@linuxhq.org> - 20150824git0c2891b-1  
- Initial build.
