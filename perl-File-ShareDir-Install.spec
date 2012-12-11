%define upstream_name    File-ShareDir-Install
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Install shared files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Dir)
BuildArch:	noarch

%description
File::ShareDir::Install allows you to install read-only data files from a
distribution. It is a companion module to the File::ShareDir manpage, which
allows you to locate these files after installation.

It is a port the Module::Install::Share manpage to the ExtUtils::MakeMaker
manpage with the improvement of only installing the files you want; '.svn'
and other source-control junk will be ignored.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 654963
- rebuild for updated spec-helper

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 514462
- import perl-File-ShareDir-Install


* Fri Mar 05 2010 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
