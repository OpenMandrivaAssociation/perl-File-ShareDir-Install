%define upstream_name    File-ShareDir-Install
Name:		perl-%{upstream_name}
Version:	0.14
Release:	2
Summary:	Install shared files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/Perl-Toolchain-Gang/File-ShareDir-Install
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-ShareDir-Install-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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
