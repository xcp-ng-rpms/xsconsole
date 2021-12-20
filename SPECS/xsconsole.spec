Summary: XCP-ng Host Configuration Console
Name: xsconsole
Version: 10.1.13
Release: 1.1%{?dist}
License: GPL2
Group: Administration/System

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xsconsole/archive?at=v10.1.13&format=tar.gz&prefix=xsconsole-10.1.13#/xsconsole.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xsconsole/archive?at=v10.1.13&format=tar.gz&prefix=xsconsole-10.1.13#/xsconsole.tar.gz) = 856ce4c4438905f71fe915597ad803e9c3cfb47a

Provides: xsconsole0
BuildRequires: python2-devel
BuildRequires: systemd
Requires: PyPAM
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# XCP-ng patches
Patch1000: xsconsole-10.1.9-rebrand-xsconsole-service.XCP-ng.patch
Patch1001: xsconsole-10.1.9-define-xcp-ng-colors.XCP-ng.patch

%description
Console tool for configuring a XCP-ng installation.

%prep
%autosetup -p1

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__make} install-base DESTDIR=%{buildroot}
%{__make} install-oem DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%post
%systemd_post xsconsole.service

%preun
%systemd_preun xsconsole.service

%postun
%systemd_postun xsconsole.service

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/xsconsole/*.py*
%{_libdir}/xsconsole/plugins-base
%{_bindir}/xsconsole
%dir %{_libdir}/xsconsole/plugins-oem
%exclude %{_libdir}/xsconsole/plugins-oem/*
%{_unitdir}/xsconsole.service

%changelog
* Mon Dec 20 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 10.1.13-1.1
- Sync with CH 8.2.1
- Remove patches contributed and merged upstream
- *** Upstream changelog ***
- * Fri Jul 09 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 10.1.13-1
- - Display 'Ext' instead of 'Ext3' for `ext` SRs
- - CA-355872: Use XAPI to edit DNS entries within xsconsole
- - Display clearer error message when XAPI unreachable
- - rework is_master to raise in case of failure
- * Fri Feb 19 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 10.1.12-1
- - CA-348699: Fix full version display if the build number is empty

* Thu Mar 04 2021 Benjamin Reis <benjamin.reis@vates.fr> - 10.1.11-1.2
- Add xsconsole-10.1.11-fix-DNS-storage-entries-by-xsconsole.XCP-ng.patch

* Wed Jul 01 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 10.1.11-1.1
- Rebase on CH 8.2
- Re-remove incloudsphere subpackage
- Keep xsconsole-10.1.9-rebrand-xsconsole-service.XCP-ng.patch
- Keep xsconsole-10.1.9-define-xcp-ng-colors.XCP-ng.patch
- Keep xsconsole-10.1.10-replace-ext3-with-ext.XCP-ng.patch

* Wed Jan 08 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 10.1.11-1
- CA-310799: Fix performance information

* Thu Oct 31 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 10.1.10-1
- CP-30221: Switch to chrony from ntp

* Mon Sep 16 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 10.1.9-2
- CA-324927: Don't restart xsconsole during upgrade

* Wed Jan 16 2019 Aaron Robson <aaron.robson@citrix.com> - 10.1.9-1
- CA-304344: Makefile warning due to missing file XSFeatureInstallLicence.py
- CA-304345: Integrate xsconsole with Travis CI
- 'make clean' and 'make test' implemented
- include suitable .gitgnore

* Thu Aug 30 2018 Simon Rowe <simon.rowe@citrix.com> - 10.1.8-1
- CA-293996: XSConsole status bar showed wrong product brand and version after upgrading.

* Mon Apr 23 2018 Simon Rowe <simon.rowe@citrix.com> - 10.1.7-1
- CA-288312: use /etc/hostname

* Thu Feb 01 2018 Simon Rowe <simon.rowe@citrix.com> - 10.1.6-1
- SCTX-2620 Handle xapi login error
- SCTX-2620 Guard against a null _session log out

* Mon Nov 20 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 10.1.5-1
- CA-272803: Write `xentemp` bridge if VLAN is specified

* Tue Nov 14 2017 Simon Rowe <simon.rowe@citrix.com> - 10.1.4-1
- CA-273753: Correct typo in getting PRODUCT_BRAND from inventory

* Tue Nov 07 2017 Simon Rowe <simon.rowe@citrix.com> - 10.1.3-1
- CA-186510: Fetch version data directly from /etc/xensource-inventory

* Mon Oct 16 2017 Simon Rowe <simon.rowe@citrix.com> - 10.1.2-1
- CA-267484: Fix regexp for finding host CPU metrics

* Wed Sep 20 2017 Simon Rowe <simon.rowe@citrix.com> - 10.1.1-1
- CA-263057 if IP address is statically configured allow DNS to be configured

* Mon Jun 05 2017 Simon Rowe <simon.rowe@citrix.com> - 10.1.0-1
- CP-14030: Update xsconsole to allow Emergency Network Reset on a VLAN.
- CP-22247: Add temporary vlan bridge to inventory for management vlan.
- fix CA-255166: also displaying vlan value if it is higher than -1
- CA-255173: fix typo creating extra quote in management.conf
- CA-255099: Use strip() instead of slicing

* Wed Apr 26 2017 Simon Rowe <simon.rowe@citrix.com> - 10.0.3-1
- Remove stale files
- CP-21612: Add XSFeatureLicenseNag.py

* Thu Apr 20 2017 Simon Rowe <simon.rowe@citrix.com> - 10.0.2-1
- Remove the build number from the console

* Mon Mar 27 2017 Simon Rowe <simon.rowe@citrix.com> - 10.0.1-1
- CA-248121: Handle failed open()s correctly
- CA-248121: Don't look in /etc/xcp for config files
