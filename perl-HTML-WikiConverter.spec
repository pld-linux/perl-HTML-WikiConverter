#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	WikiConverter
Summary:	HTML::WikiConverter - Convert HTML to wiki markup
Name:		perl-HTML-WikiConverter
Version:	0.68
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e6d8b16c23b6f38c51d8585f3423aca9
URL:		http://search.cpan.org/dist/HTML-WikiConverter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CSS >= 1.07
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-HTML-Parser >= 1.27
BuildRequires:	perl-HTML-Tagset >= 3.04
BuildRequires:	perl-HTML-Tree >= 3.18
BuildRequires:	perl-Params-Validate >= 0.77
BuildRequires:	perl-URI
%endif
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
dialects' documentation for details of supported features. Suggestions
for improvements, especially in the form of patches, are very much
appreciated.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%attr(755,root,root) %{_bindir}/html2wiki
%{perl_vendorlib}/HTML/*.pm
%{perl_vendorlib}/HTML/WikiConverter
%{_mandir}/man1/html2wiki.1p*
%{_mandir}/man3/*
