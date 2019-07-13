#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-magnumclient
Version  : 2.13.0
Release  : 27
URL      : http://tarballs.openstack.org/python-magnumclient/python-magnumclient-2.13.0.tar.gz
Source0  : http://tarballs.openstack.org/python-magnumclient/python-magnumclient-2.13.0.tar.gz
Source99 : http://tarballs.openstack.org/python-magnumclient/python-magnumclient-2.13.0.tar.gz.asc
Summary  : Python client library for Magnum
Group    : Development/Tools
License  : Apache-2.0
Requires: python-magnumclient-bin = %{version}-%{release}
Requires: python-magnumclient-license = %{version}-%{release}
Requires: python-magnumclient-python = %{version}-%{release}
Requires: python-magnumclient-python3 = %{version}-%{release}
Requires: Babel
Requires: cryptography
Requires: decorator
Requires: keystoneauth1
Requires: os-client-config
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/python-magnumclient.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the python-magnumclient package.
Group: Binaries
Requires: python-magnumclient-license = %{version}-%{release}

%description bin
bin components for the python-magnumclient package.


%package license
Summary: license components for the python-magnumclient package.
Group: Default

%description license
license components for the python-magnumclient package.


%package python
Summary: python components for the python-magnumclient package.
Group: Default
Requires: python-magnumclient-python3 = %{version}-%{release}

%description python
python components for the python-magnumclient package.


%package python3
Summary: python3 components for the python-magnumclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-magnumclient package.


%prep
%setup -q -n python-magnumclient-2.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555531286
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-magnumclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-magnumclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/magnum

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-magnumclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
