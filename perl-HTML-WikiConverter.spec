#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	HTML
%define	pnam	WikiConverter
Summary:	HTML::WikiConverter - Convert HTML to wiki markup
Summary(pl.UTF-8):	HTML::WikiConverter - konwertowanie HTML-a do znaczników wiki
Name:		perl-HTML-WikiConverter
Version:	0.68
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e6d8b16c23b6f38c51d8585f3423aca9
URL:		http://search.cpan.org/dist/HTML-WikiConverter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Pod::Usage) >= 1.16
BuildRequires:	perl-CGI-Application
BuildRequires:	perl-CSS >= 1.07
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Encode
BuildRequires:	perl-HTML-Parser >= 1.27
BuildRequires:	perl-HTML-Tagset >= 3.04
BuildRequires:	perl-HTML-Tree >= 3.18
BuildRequires:	perl-Params-Validate >= 0.77
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-URI >= 1.35
%endif
Requires:	perl(Pod::Usage) >= 1.16
Requires:	perl-CSS >= 1.07
Requires:	perl-Class-Data-Inheritable >= 0.02
Requires:	perl-HTML-Parser >= 1.27
Requires:	perl-HTML-Tagset >= 3.04
Requires:	perl-HTML-Tree >= 3.18
Requires:	perl-Params-Validate >= 0.77
Requires:	perl-URI >= 1.35
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert
HTML source into a variety of wiki markups, called wiki
"dialects".

The following dialects are supported:
- DokuWiki
- Kwiki
- MediaWiki
- MoinMoin
- Oddmuse
- PbWiki
- PhpWiki
- PmWiki
- SlipSlap
- TikiWiki
- UseMod
- WakkaWiki
- WikkaWiki

Note that while dialects usually produce satisfactory wiki markup, not
all features of all dialects are supported. Consult individual
dialects' documentation for details of supported features.

%description -l pl.UTF-8
HTML::WikiConverter to konwerter HTML-a do wiki. Potrafi konwertować
źródło w HTML-u do różnych rodzajów znaczników wiki, nazywanych
"dialektami".

Obsługiwane są następujące dialekty:
- DokuWiki
- Kwiki
- MediaWiki
- MoinMoin
- Oddmuse
- PbWiki
- PhpWiki
- PmWiki
- SlipSlap
- TikiWiki
- UseMod
- WakkaWiki
- WikkaWiki

Uwaga: o ile dialekty zwykle zawierają satysfakcjonujące znaczniki, 
nie wszystkie możliwości wszystkich dialektów są obsługiwane.
Szczegóły obsługiwanych możliwości można znaleźć w dokumentacji dla
poszczególnych dialektów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# disable network tests
%{__sed} -i -e '/^my \$have_lwp =/s/= .*/= 0;/' t/01-wikiconverter.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%attr(755,root,root) %{_bindir}/html2wiki
%{perl_vendorlib}/HTML/WikiConverter.pm
%{perl_vendorlib}/HTML/WikiConverter
%{_mandir}/man1/html2wiki.1p*
%{_mandir}/man3/HTML::WikiConverter*.3pm*
