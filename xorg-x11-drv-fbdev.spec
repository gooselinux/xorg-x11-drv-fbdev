%define tarball xf86-video-fbdev
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 fbdev video driver
Name:      xorg-x11-drv-fbdev
Version:   0.4.2
Release:   1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

Patch1: fbdev-0.3.0-32fbbpp.patch
Patch2: BGNoneRoot.patch

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1

Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 fbdev video driver.

%prep
%setup -q -n %{tarball}-%{version}
# Not sure if this is still necessary, it doesn't apply anymore and the new
# code looks like it'll have the same effect.  XXX check with katzj.
# %patch1 -p1 -b .fbbpp
%patch2 -p1

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/fbdev_drv.so
%{_mandir}/man4/fbdev.4*

%changelog
* Tue Jun 29 2010 Adam Jackson <ajax@redhat.com> 0.4.2-1
- fbdev 0.4.2 (#597291)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4.1-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 0.4.1-1
- fbdev 0.4.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.4.0-5.1
- ABI bump

* Mon Jun 22 2009 Peter Hutterer <peter.hutterer@redhat.com> 0.4.0-5
- fbdev-0.4.0-Make-ISA-optional.patch: to make next patch apply cleanly.
- fbdef-0.4.0-Remove-useless-loader-symbol-lists.patch:
  fix linker error against X server >= 1.6.99.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 0.4.0-3
- rebuild for latest server API

* Thu Oct 30 2008 Bill Nottingham <notting@redhat.com> 0.4.0-2
- set canDoBGNoneRoot on driver startup

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.4.0-1
- Update to latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-7
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Dave Airlie <airlied@redhat.com> 0.3.1-6
- rebuild for abi change.

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 0.3.1-5.20071113
- Update to git snapshot for pciaccess goodness.  Don't ask why a driver
  that doesn't touch PCI at all needs a PCI update.  I don't know either,
  and thinking about it makes me very sad.
- Require xserver 1.4.99.1

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 0.3.1-4
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.3.1-3
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.3.1-2
- ExclusiveArch -> ExcludeArch

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 0.3.1-1
- Update to 0.3.1

* Mon Aug 28 2006 Jeremy Katz <katzj@redhat.com> - 0.3.0-2
- adjust to prefer 32bpp over 24bpp for fbbpp (#204117)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.3.0-1
- Update to 0.3.0 from 7.1.

* Tue May 16 2006 Adam Jackson <ajackson@redhat.com> 0.2.0-2
- Move debugging output from compile-time option to run-time option.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 0.2.0-1
- Update to 0.2.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.1.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.1.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.1.0.5-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.1.0.4-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 0.1.0.2-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 0.1.0.1-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.1 from X11R7 RC1
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 0.1.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Add alpha/sparc/sparc64 to "ExclusiveArch"

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 0.1.0-0
- Initial spec file for fbdev video driver generated automatically
  by my xorg-driverspecgen script.
