%define _prefix /usr/local
%global date 20150819
%global git_commit 6fecda34c8328487f0b0b256f51bfb1697179342
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

Name:		pagerduty-nagios-pl
Version:	%{date}git%{short_commit}
Release:	1%{?dist}
Summary:	Integration between nagios and pagerduty
Group:		Applications/System
License:	PagerDuty
URL:		https://github.com/PagerDuty/%{name}
Source0:	https://github.com/PagerDuty/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	perl-libwww-perl

%description
Integration script for nagios and pagerduty

%prep
%setup -q -n %{name}-%{git_commit}
%build

%install
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 pagerduty_nagios.pl %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/pagerduty_nagios.pl

%changelog
* Wed Aug 19 2015 Taylor Kimball <taylor@linuxhq.org> - 20150819git6fecda34-1
- Initial build.
