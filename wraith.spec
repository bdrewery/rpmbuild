Summary: Wraith IRC bot
Name: wraith
Version: 1.4.3
Release: 1%{?dist}
URL: http://wraith.botpack.net
Source: http://downloads.sourceforge.net/project/wraithbotpack/src/tags/%{name}-v%{version}.tar.gz
License: GPL
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: openssl, tcl
BuildRequires: gcc-c++, git, openssl-devel, tcl-devel

%description
Wraith is an open source IRC bot written in C++. It has been in 
development since late 2003. It is based on Eggdrop 1.6.12 but has 
since evolved into something much different at its core.

%prep
%setup -T -c

%build
git clone https://github.com/wraith/wraith.git
pushd %{name}

%configure \
	--with-tclinc="%{_includedir}/tcl.h" \
	--with-tcllib="%{_libdir}/libtcl.so"
%{__make} 

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 %{name} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README doc/* scripts/*
%{_bindir}/%{name}

%changelog
* Sun Jul 06 2014 Taylor Kimball <taylor@linuxhq.org> - 1.4.3-1
- Initial package.
