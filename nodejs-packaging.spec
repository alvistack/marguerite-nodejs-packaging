# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

%define _rpmconfigdir %{_prefix}/lib/rpm

Name: nodejs-packaging
Epoch: 100
Version: 10~beta11+20180129.2e220d1b
Release: 1%{?dist}
BuildArch: noarch
Summary: Node.js Dependency generators for openSUSE
License: MIT
Group: Development/Languages/NodeJS
URL: https://github.com/marguerite/nodejs-packaging/tags
Source0: %{name}_%{version}.orig.tar.gz
Requires: nodejs-devel
Requires: npm
Requires: python3
Requires: ruby
Requires: rubygem(json)

%description
This package generates Node.js Provides/Requires dependencies
automatically for nodejs module packages in openSUSE.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m0644 macros.nodejs %{buildroot}%{_rpmmacrodir}/macros.nodejs
install -m0755 nodejs-check.rb %{buildroot}%{_rpmconfigdir}/nodejs-check.rb
install -m0755 nodejs-fixdep.rb %{buildroot}%{_rpmconfigdir}/nodejs-fixdep.rb
install -m0755 nodejs-symlink-deps.rb %{buildroot}%{_rpmconfigdir}/nodejs-symlink-deps.rb
install -m0644 nodejs.attr %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs.attr
install -m0755 nodejs.prov %{buildroot}%{_rpmconfigdir}/nodejs.prov
install -m0755 nodejs.req %{buildroot}%{_rpmconfigdir}/nodejs.req

%files
%defattr(-,root,root)
%license COPYING
%{_rpmmacrodir}/macros.nodejs
%{_rpmconfigdir}/nodejs-check.rb
%{_rpmconfigdir}/nodejs-fixdep.rb
%{_rpmconfigdir}/nodejs-symlink-deps.rb
%{_rpmconfigdir}/fileattrs/nodejs.attr
%{_rpmconfigdir}/nodejs.prov
%{_rpmconfigdir}/nodejs.req
