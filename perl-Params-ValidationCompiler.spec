#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Params
%define		pnam	ValidationCompiler
%include	/usr/lib/rpm/macros.perl
Summary:	Params::ValidationCompiler - Build an optimized subroutine parameter validator once, use it forever
Summary(pl.UTF-8):	Params::ValidationCompiler - tworzenie zoptymalizowanego walidatora parametrów raz do wielokrotnego użycia
Name:		perl-Params-ValidationCompiler
Version:	0.27
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a6937d7aba4417ad7d4edeb1f9988ac3
URL:		http://search.cpan.org/dist/Params-ValidationCompiler/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Eval-Closure
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-Scalar-List-Utils >= 1.29
BuildRequires:	perl-Specio >= 0.14
BuildRequires:	perl-Test-Simple >= 1.302015
BuildRequires:	perl-Test-Without-Module
BuildRequires:	perl-Test2-Plugin-NoWarnings
BuildRequires:	perl-Test2-Suite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is very alpha. The module name could change. Everything could
change. You have been warned.

Create a customized, optimized, non-lobotomized, uncompromised, and
thoroughly specialized parameter checking subroutine.

%description -l pl.UTF-8
Ten moduł jest w głębokim stanie alfa - nazwa może się zmienić;
wszystko może się zmienić. To ostrzeżenie.

Tworzenie dostosowanych, zoptymalizowanych, bezkompromisowych i
szczegółowo wyspecjalizowanych procedur sprawdzających parametry.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Params/ValidationCompiler.pm
%{perl_vendorlib}/Params/ValidationCompiler
%{_mandir}/man3/Params::ValidationCompiler*.3pm*
%{_examplesdir}/%{name}-%{version}
