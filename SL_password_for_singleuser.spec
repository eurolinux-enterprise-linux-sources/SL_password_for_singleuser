Summary: Asks for roots password when booting up in single user mode
Name: SL_password_for_singleuser
Version: 3.0
Release: 1
License: GPL
Group: SL
Vendor: Scientific Linux
Packager: Dan Yocum, Connie Sieh, Troy Dawson, Stephan Wiesand
Requires: initscripts
Obsoletes: zz_inittab_change, SL_inittab_change
BuildArchitectures: noarch

%description
This package will modify /etc/sysconfig/init to only 
allow root access via password when a machine is booted into 
single user mode.

The change is reverted when this package is removed.

This package used to be called SL_inittab_change

%files
%triggerin -- initscripts
sed -i 's@^SINGLE=.*@SINGLE=/sbin/sulogin@' /etc/sysconfig/init >/dev/null 2>&1 || :

%postun
[ $1 -eq 0 ] || exit 0
sed -i 's@^SINGLE=.*@SINGLE=/sbin/sushell@' /etc/sysconfig/init >/dev/null 2>&1 || :


%changelog
* Wed Jan 19 2011 Stephan Wiesand <stephan wiesand desy de> 3.0-1
- made it work on SL6 (edit /etc/sysconfig/init)

* Fri Aug 28 2009 Troy Dawson <dawson@fnal.gov> 2.0-2
- Changed post script to be a triggers script on initscripts

* Tue Jun 09 2009 Troy Dawson <dawson@fnal.gov> 2.0-1
- Changed to work with Fedora 10 and above
- Change it to use /etc/event.d/rcS-sulogin
