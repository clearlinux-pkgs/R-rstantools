#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rstantools
Version  : 1.5.1
Release  : 17
URL      : https://cran.r-project.org/src/contrib/rstantools_1.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rstantools_1.5.1.tar.gz
Summary  : Tools for Developing R Packages Interfacing with 'Stan'
Group    : Development/Tools
License  : GPL-3.0
Requires: R-assertthat
Requires: R-markdown
Requires: R-yaml
BuildRequires : R-assertthat
BuildRequires : R-markdown
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n rstantools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552787204

%install
export SOURCE_DATE_EPOCH=1552787204
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstantools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstantools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstantools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  rstantools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rstantools/DESCRIPTION
/usr/lib64/R/library/rstantools/INDEX
/usr/lib64/R/library/rstantools/Meta/Rd.rds
/usr/lib64/R/library/rstantools/Meta/features.rds
/usr/lib64/R/library/rstantools/Meta/hsearch.rds
/usr/lib64/R/library/rstantools/Meta/links.rds
/usr/lib64/R/library/rstantools/Meta/nsInfo.rds
/usr/lib64/R/library/rstantools/Meta/package.rds
/usr/lib64/R/library/rstantools/Meta/vignette.rds
/usr/lib64/R/library/rstantools/NAMESPACE
/usr/lib64/R/library/rstantools/NEWS.md
/usr/lib64/R/library/rstantools/R/rstantools
/usr/lib64/R/library/rstantools/R/rstantools.rdb
/usr/lib64/R/library/rstantools/R/rstantools.rdx
/usr/lib64/R/library/rstantools/doc/developer-guidelines.Rmd
/usr/lib64/R/library/rstantools/doc/developer-guidelines.html
/usr/lib64/R/library/rstantools/doc/index.html
/usr/lib64/R/library/rstantools/doc/minimal-rstan-package.R
/usr/lib64/R/library/rstantools/doc/minimal-rstan-package.Rmd
/usr/lib64/R/library/rstantools/doc/minimal-rstan-package.html
/usr/lib64/R/library/rstantools/help/AnIndex
/usr/lib64/R/library/rstantools/help/aliases.rds
/usr/lib64/R/library/rstantools/help/figures/stanlogo.png
/usr/lib64/R/library/rstantools/help/paths.rds
/usr/lib64/R/library/rstantools/help/rstantools.rdb
/usr/lib64/R/library/rstantools/help/rstantools.rdx
/usr/lib64/R/library/rstantools/html/00Index.html
/usr/lib64/R/library/rstantools/html/R.css
/usr/lib64/R/library/rstantools/tests/testthat.R
/usr/lib64/R/library/rstantools/tests/testthat/bayes_R2.RDS
/usr/lib64/R/library/rstantools/tests/testthat/loo_pit.RDS
/usr/lib64/R/library/rstantools/tests/testthat/posterior_interval.RDS
/usr/lib64/R/library/rstantools/tests/testthat/predictive_error.RDS
/usr/lib64/R/library/rstantools/tests/testthat/predictive_interval.RDS
/usr/lib64/R/library/rstantools/tests/testthat/test-default-methods.R
/usr/lib64/R/library/rstantools/tests/testthat/test-generics-with-no-methods.R
/usr/lib64/R/library/rstantools/tests/testthat/test-rstan_package_skeleton.R
/usr/lib64/R/library/rstantools/tests/testthat/test.stan
