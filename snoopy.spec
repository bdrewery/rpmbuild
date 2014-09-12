Summary:        User monitoring and command logging
Name:           snoopy
Version:        1.9.0
Release:        1%{dist}
URL:            https://source.a2o.si/download/snoopy/
Group:          Applications/Monitoring
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  autoconf, automake, git, gcc, make
License:        GPL
Packager:       Taylor Kimball <taylor@linuxhq.org>

%description
Snoopy Logger, logs all the commands issued by local users on the system.
It is very useful to track and monitor the users.

%prep
%setup -T -c

%build
git clone https://github.com/tkimball83/%{name}.git
pushd %{name}
autoreconf
%configure --with-environment=GECOS
%{__make}

%install
pushd %{name}
%{__install} -d -m 755 %{buildroot}%{_libdir}
%{__install} -d -m 755 %{buildroot}%{_sysconfdir}
%{__install} -m 755 %{name}.so %{buildroot}%{_libdir}
echo "%{_libdir}/%{name}.so" >> %{buildroot}%{_sysconfdir}/ld.so.preload

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{name}/ChangeLog %{name}/COPYING %{name}/README.filtering %{name}/README.md %{name}/TODO
%config(noreplace) %{_sysconfdir}/ld.so.preload
%{_libdir}/%{name}.so

%changelog
* Fri Sep 12 2014 Taylor Kimball <taylor@linuxhq.org> - 1.9.0-1
- Initial spec.
