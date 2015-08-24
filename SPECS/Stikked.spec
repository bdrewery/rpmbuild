%global date 20150821
%global git_commit 0714e54b56bfdaa104eaf28378aa2e7538fcb56a
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

Name:          Stikked
Version:       %{date}git%{short_commit}
Release:       1%{?dist}
Summary:       An open-source PHP pastebin       
Group:         Applications/System
License:       CC0
URL:           https://github.com/claudehohl/%{name}
Source0:       https://github.com/claudehohl/%{name}/archive/%{short_commit}/%{name}-%{git_commit}.tar.gz       
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      php, php-mysql

%description
Stikked is an Open-Source PHP Pastebin, with the aim of keeping
a simple and easy to use user interface.

Stikked allows you to easily share code with anyone you wish.
Based on the original Stikked with lots of bugfixes and improvements.

%prep
%setup -q -n %{name}-%{git_commit}
%build
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}

%install
%{__cp} -rf htdocs %{buildroot}%{_datadir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS.md CC0 doc README.md
%{_datadir}/%{name}

%changelog
* Fri Aug 21 2015 Taylor Kimball <taylor@linuxhq.org> - 20150821git0714e54-1
- Initial build

