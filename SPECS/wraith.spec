%global date 20150902
%global git_commit d28d690c82c7f9df61eceb358c3059af25d4b8b7
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

Name:           wraith
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Wraith IRC Bot
Group:          Applications/Internet
License:        GPL
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       openssl, tcl
BuildRequires:  gcc-c++, git, openssl-devel, tcl-devel

%description
Wraith is an open source IRC bot written in C++. It has been in 
development since late 2003. It is based on Eggdrop 1.6.12 but has 
since evolved into something much different at its core.

%prep
%setup -q -n %{name}-%{git_commit}
%build
%configure \
	--with-tclinc="%{_includedir}/tcl.h" \
	--with-tcllib="%{_libdir}/libtcl.so"
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 %{name} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README doc/* scripts/*
%{_bindir}/%{name}

%changelog
* Wed Sep 02 2015 Taylor Kimball <taylor@linuxhq.org> - 20150902gitd28d690 
- Initial package.
