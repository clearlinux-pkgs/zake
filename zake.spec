#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zake
Version  : 0.2.2
Release  : 31
URL      : https://files.pythonhosted.org/packages/ac/00/a322966639ce1b754475d2e83f169d32973be3ebbd6fc19344267d363627/zake-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/00/a322966639ce1b754475d2e83f169d32973be3ebbd6fc19344267d363627/zake-0.2.2.tar.gz
Summary  : A python package that works to provide a nice set of testing utilities for the kazoo library.
Group    : Development/Tools
License  : Apache-2.0
Requires: zake-python3
Requires: zake-python
Requires: kazoo
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : kazoo
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
====

%package python
Summary: python components for the zake package.
Group: Default
Requires: zake-python3

%description python
python components for the zake package.


%package python3
Summary: python3 components for the zake package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zake package.


%prep
%setup -q -n zake-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532377806
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
