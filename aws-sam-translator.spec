#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aws-sam-translator
Version  : 1.41.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/23/a7/d81dab8d00781eef4ec5494d06221b610cd78e9d1e14e46fd069b731cf4c/aws-sam-translator-1.41.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/a7/d81dab8d00781eef4ec5494d06221b610cd78e9d1e14e46fd069b731cf4c/aws-sam-translator-1.41.0.tar.gz
Summary  : AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
Group    : Development/Tools
License  : Apache-2.0
Requires: aws-sam-translator-python = %{version}-%{release}
Requires: aws-sam-translator-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(black)
BuildRequires : pypi(mock)
BuildRequires : pypi(pathlib2)
BuildRequires : pypi(pylint)

%description
<p align="center">
</p>
# AWS Serverless Application Model (AWS SAM)
![Apache-2.0](https://img.shields.io/github/license/aws/serverless-application-model.svg)
![SAM_CLI release](https://img.shields.io/github/release/aws/aws-sam-cli.svg?label=CLI%20Version)
[![codecov](https://codecov.io/gh/aws/serverless-application-model/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/aws/serverless-application-model)

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
Requires: pypi(black)
Requires: pypi(boto3)
Requires: pypi(jsonschema)
Requires: pypi(mock)
Requires: pypi(pathlib2)
Requires: pypi(pylint)
Requires: pypi(six)

%description python3
python3 components for the aws-sam-translator package.


%prep
%setup -q -n aws-sam-translator-1.41.0
cd %{_builddir}/aws-sam-translator-1.41.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637358125
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
