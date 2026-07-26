%define upstream_name    Dist-Zilla-Plugin-LocaleMsgfmt
Name:		perl-%{upstream_name}
Version:	1.203
Release:	2

Summary:	Dist::Zilla plugin that compiles Local::Msgfmt .po files to .mo files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://github.com/jquelin/Dist-Zilla-Plugin-LocaleMsgfmt/tree
Source0:	https://cpan.metacpan.org/authors/id/J/JQ/JQUELIN/Dist-Zilla-Plugin-LocaleMsgfmt-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

