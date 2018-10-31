%define upstream_name    File-ShareDir-Install
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Install shared files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/File::ShareDir::Install
Source0:	http://www.cpan.org/modules/by-module/File/File-ShareDir-Install-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(CPAN::Meta::YAML)
BuildRequires:	perl(Test::More)
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
