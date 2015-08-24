%global date 20150824
%global git_commit 51914ec15ec2c6881f52e2a7df94afdf95e3b8c9
%global short_commit %(c=%{git_commit}; echo ${c:0:7})
%global git_sub_commit 5c71d5640fa60a5d19aed85d01a88e2424b176c4
%global short_sub_commit %(c=%{git_sub_commit}; echo ${c:0:7})

Name:		snoopy
Version:	%{date}git%{short_commit}
Release:	1%{dist}
Summary:	User monitoring and command logging
Group:		Applications/Monitoring
License:	GPL
URL:		https://github.com/a2o/%{name}
Source0:	https://github.com/a2o/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:	https://github.com/a2o/iniparser/archive/%{git_sub_commit}/iniparser-%{git_sub_commit}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  autoconf, automake, git, gcc, libtool, make, socat

%description
Snoopy is a tiny library that logs all executed commands (+ arguments) on your system.

%prep
%setup -q -n %{name}-%{git_commit}
%build
%if 0%{?el6}
%{__sed} -i -e "s/m4_esyscmd_s.*/[%{git_commit}],/" configure.ac
%{__sed} -i -e "s/\ -Werror//g" configure.ac build/Makefile.am.common
%endif

%{__tar} zxvf %{SOURCE1} -C ./lib/iniparser --strip-components=1
bash bootstrap.sh
%configure --enable-everything
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}
echo "%{_libdir}/lib%{name}.so" >> %{buildroot}%{_sysconfdir}/ld.so.preload

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog CONTRIBUTING.md COPYING README.md contrib doc
%config(noreplace) %{_sysconfdir}/ld.so.preload
%{_bindir}/%{name}-*
%{_libdir}/lib%{name}.*
%{_sbindir}/%{name}-*
%{_sysconfdir}/%{name}.ini

%changelog
* Mon Aug 24 2015 Taylor Kimball <taylor@linuxhq.org> - 20150824git51914ec-1  
- Spec file refactor with latest update

* Sat Feb 28 2015 Taylor Kimball <taylor@linuxhq.org> - 2.2.6-1
- Initial spec.
