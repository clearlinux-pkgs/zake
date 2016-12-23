#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zake
Version  : 0.2.2
Release  : 21
URL      : https://pypi.python.org/packages/source/z/zake/zake-0.2.2.tar.gz
Source0  : https://pypi.python.org/packages/source/z/zake/zake-0.2.2.tar.gz
Summary  : A python package that works to provide a nice set of testing utilities for the kazoo library.
Group    : Development/Tools
License  : Apache-2.0
Requires: zake-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Zake
====
.. image:: https://travis-ci.org/yahoo/Zake.png?branch=master
:target: https://travis-ci.org/yahoo/Zake

%package python
Summary: python components for the zake package.
Group: Default

%description python
python components for the zake package.


%prep
%setup -q -n zake-0.2.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
