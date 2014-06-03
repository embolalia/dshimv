Name:		dshimv
Version:	0.0.1
Release:	1%{?dist}
Summary:	A shim to allow systemd units to be used as SysV init scripts

Group:		Applications/System
License:	GPL v3
URL:		https://github.com/embolalia/dshimv
Source0:	https://github.com/embolalia/dshimv/archive/master.zip

Requires:	python

%description
dshimv allows systemd service unit files to be used, with nearly no
modification, as if they were SysV init scripts.

%install
install -m 0755 dshimv %{_bindir}/dshimv

%files
%{_bindir}/dshimv

%changelog
* Mon Jun  2 2014 Edward Powell <me@embolalia.com> - 0.0.1-1
- Update from git
