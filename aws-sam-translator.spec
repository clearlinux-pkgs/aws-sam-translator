#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aws-sam-translator
Version  : 1.48.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/72/0b/6bf9a42493b938ca1f07a607a2a467866ef81d53256b1b1fa9a9bbbe28db/aws-sam-translator-1.48.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/0b/6bf9a42493b938ca1f07a607a2a467866ef81d53256b1b1fa9a9bbbe28db/aws-sam-translator-1.48.0.tar.gz
Summary  : AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
Group    : Development/Tools
License  : Apache-2.0
Requires: aws-sam-translator-license = %{version}-%{release}
Requires: aws-sam-translator-python = %{version}-%{release}
Requires: aws-sam-translator-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(boto3)
BuildRequires : pypi(jsonschema)

%description
<p align="center">
</p>
# AWS Serverless Application Model (AWS SAM)
![Apache-2.0](https://img.shields.io/github/license/aws/serverless-application-model.svg)
![SAM_CLI release](https://img.shields.io/github/release/aws/aws-sam-cli.svg?label=CLI%20Version)
[![codecov](https://codecov.io/gh/aws/serverless-application-model/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/aws/serverless-application-model)

%package license
Summary: license components for the aws-sam-translator package.
Group: Default

%description license
license components for the aws-sam-translator package.


%package python
Summary: python components for the aws-sam-translator package.
Group: Default
Requires: aws-sam-translator-python3 = %{version}-%{release}

%description python
python components for the aws-sam-translator package.


%package python3
Summary: python3 components for the aws-sam-translator package.
Group: Default
Requires: python3-core
Provides: pypi(aws_sam_translator)
Requires: pypi(boto3)
Requires: pypi(jsonschema)

%description python3
python3 components for the aws-sam-translator package.


%prep
%setup -q -n aws-sam-translator-1.48.0
cd %{_builddir}/aws-sam-translator-1.48.0
pushd ..
cp -a aws-sam-translator-1.48.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658939972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aws-sam-translator
cp %{_builddir}/aws-sam-translator-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/aws-sam-translator/9ff23d505de81a8185554e10c611378b8698bc71
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aws-sam-translator/9ff23d505de81a8185554e10c611378b8698bc71

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
