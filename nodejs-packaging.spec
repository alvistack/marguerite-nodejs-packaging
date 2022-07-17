%global debug_package %{nil}

%define _rpmconfigdir %{_prefix}/lib/rpm

Name: nodejs-packaging
Epoch: 100
Version: 10~beta11
Release: 1%{?dist}
BuildArch: noarch
Summary: Node.js Dependency generators for openSUSE
License: MIT
Group: Development/Languages/NodeJS
URL: https://github.com/marguerite/nodejs-packaging/tags
Source0: %{name}_%{version}.orig.tar.gz
Requires: gcc-c++
Requires: nodejs-devel
Requires: npm
Requires: python
Requires: ruby
Requires: rubygem(json)

%description
This package generates Node.js Provides/Requires dependencies
automatically for nodejs module packages in openSUSE.

%package -n npkg
Summary: The ultimate Node.js packaging toolkit for openSUSE
Group: Development/Languages/NodeJS
Requires: nodejs-packaging = %{epoch}:%{version}-%{release}
Requires: ruby
Requires: rubygem(json)
Requires: rubygem(nokogiri)

%description -n npkg
This package provides the ultimate Node.js packaging toolkit for
openSUSE.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/npkg
mkdir -p %{buildroot}%{_rpmconfigdir}/{nodejs,fileattrs}
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m0644 macros.nodejs %{buildroot}%{_rpmmacrodir}/macros.nodejs
cp -r nodejs/* %{buildroot}%{_rpmconfigdir}/nodejs
cp -r tool/* %{buildroot}%{_datadir}/npkg
cp -r scripts %{buildroot}%{_datadir}/npkg
ln -sf %{_datadir}/npkg/npkg %{buildroot}%{_bindir}/npkg
ln -sf %{_datadir}/npkg/scripts/npkg-mgmt-pkg-batchrm.rb %{buildroot}%{_bindir}/npkg-mgmt-pkg-batchrm
ln -sf %{_datadir}/npkg/scripts/npkg-mgmt-json2pkgtxt.rb %{buildroot}%{_bindir}/npkg-mgmt-json2pkgtxt
ln -sf %{_datadir}/npkg/scripts/npkg-mgmt-merge.rb %{buildroot}%{_bindir}/npkg-mgmt-merge
install -m0644 nodejs.attr %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs.attr
install -m0755 nodejs.prov %{buildroot}%{_rpmconfigdir}/nodejs.prov
install -m0755 nodejs.req %{buildroot}%{_rpmconfigdir}/nodejs.req
install -m0755 nodejs.rb %{buildroot}%{_rpmconfigdir}/nodejs.rb
install -m0755 nodejs-fixdep.rb %{buildroot}%{_rpmconfigdir}/nodejs-fixdep.rb
install -m0755 nodejs-check.rb %{buildroot}%{_rpmconfigdir}/nodejs-check.rb
install -m0755 nodejs-symlink-deps.rb %{buildroot}%{_rpmconfigdir}/nodejs-symlink-deps.rb

%files
%defattr(-,root,root)
%license COPYING
%{_rpmconfigdir}/fileattrs/nodejs.attr
%{_rpmconfigdir}/nodejs
%{_rpmconfigdir}/nodejs-check.rb
%{_rpmconfigdir}/nodejs-fixdep.rb
%{_rpmconfigdir}/nodejs-symlink-deps.rb
%{_rpmconfigdir}/nodejs.prov
%{_rpmconfigdir}/nodejs.rb
%{_rpmconfigdir}/nodejs.req
%{_rpmmacrodir}/macros.nodejs

%files -n npkg
%defattr(-,root,root)
%{_bindir}/npkg
%{_bindir}/npkg-mgmt-json2pkgtxt
%{_bindir}/npkg-mgmt-merge
%{_bindir}/npkg-mgmt-pkg-batchrm
%{_datadir}/npkg
