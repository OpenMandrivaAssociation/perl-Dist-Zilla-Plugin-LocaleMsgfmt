%define upstream_name    Dist-Zilla-Plugin-LocaleMsgfmt
%define upstream_version 1.202

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dist::Zilla plugin that compiles Local::Msgfmt .po files to .mo files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::BeforeBuild)
BuildRequires:	perl(Locale::Msgfmt)
BuildRequires:	perl(Moose)
BuildArch:	noarch

%description
Put the following in your dist.ini

    [LocaleMsgfmt]
    locale = share/locale ;; (optional)

This plugin will compile all of the .po files it finds in the locale
directory into .mo files, via Locale::Msgfmt.

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
%doc Changes META.yml LICENSE META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*

