Name:		snoopy
Version:	2.2.4
Release:	1%{dist}
Summary:	User monitoring and command logging
Group:		Applications/Monitoring
License:	GPL
URL:		https://github.com/a2o/snoopy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  autoconf, automake, git, gcc, make

%description
Snoopy Logger, logs all the commands issued by local users on the system.
It is very useful to track and monitor the users.

%prep
%setup -T -c

%build
git clone https://github.com/a2o/snoopy.git
pushd %{name}
%if 0%{?el6}
%{__sed} -i -e 's/^AM_PROG_AR/#AM_PROG_AR/' configure.ac
%endif
%{__sed} -i -e 's/$(sysconfdir)\/snoopy.ini/$(DESTDIR)$(sysconfdir)\/snoopy.ini/g' etc/Makefile.am
./autogen.sh
%configure --prefix=%{_prefix} \
           --sysconfdir=%{_sysconfdir} \
           --enable-config-file 
%{__make} %{?_smp_mflags}
%{__install} -d -m 755 %{buildroot}%{_sysconfdir}

%install
pushd %{name}
%{__make} install DESTDIR=%{buildroot}
echo "%{_libdir}/lib%{name}.so" >> %{buildroot}%{_sysconfdir}/ld.so.preload

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{name}/ChangeLog %{name}/COPYING %{name}/README.md
%config(noreplace) %{_sysconfdir}/ld.so.preload
%{_bindir}/%{name}-*
%{_libdir}/lib%{name}.*
%{_sbindir}/%{name}-*
%{_sysconfdir}/%{name}.ini

%changelog
* Sat Feb 28 2015 Taylor Kimball <taylor@linuxhq.org> - 2.2.4-1
- Initial spec.
