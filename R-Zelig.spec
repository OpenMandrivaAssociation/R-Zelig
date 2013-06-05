%global packname  Zelig
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.1.3
Release:          1
Summary:          Everyone's Statistical Software
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Zelig_4.1-3.tar.gz
Requires:         R-MASS R-boot R-stats R-VGAM R-MCMCpack R-mvtnorm R-survival
Requires:         R-sandwich R-zoo R-coda R-nnet R-sna R-gee R-systemfit
Requires:         R-mgcv R-lme4 R-anchors R-survey R-quantreg 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-MASS R-boot R-stats R-VGAM R-MCMCpack R-mvtnorm R-survival
BuildRequires:    R-sandwich R-zoo R-coda R-nnet R-sna R-gee R-systemfit
BuildRequires:    R-mgcv R-lme4 R-anchors R-survey R-quantreg

%description
Zelig is an easy-to-use program that can estimate, and help interpret the
results of, an enormous range of statistical models. It literally is
``everyone's statistical software'' because Zelig's simple unified
framework incorporates everyone else's (R) code. We also hope it will
become ``everyone's statistical software'' for applications and teaching,
and so have designed Zelig so that anyone can easily use it or add their
programs to it.  Zelig also comes with infrastructure that facilitates the
use of any existing method, such as by allowing multiply imputed data for
any model, and mimicking the program Clarify (for Stata) that takes the
raw output of existing statistical procedures and translates them into
quantities of direct interest.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/zideal

