%define targetfile /etc/event.d/rcS-sulogin

Summary: Asks for roots password when booting up in single user mode
Name: SL_password_for_singleuser
Version: 2.0
Release: 2
License: GPL
Group: SL
Vendor: Scientific Linux
Packager: Dan Yocum, Connie Sieh, Troy Dawson
Requires: initscripts
Obsoletes: zz_inittab_change, SL_inittab_change
BuildArchitectures: noarch

%description
This package will add an entry in /etc/event.d/rcS-sulogin to only 
allow root access viapassword when a machine is booted into 
single user mode.

The original file will be saved as /etc/event.d/rcS-sulogin.rpmsave.

This package used to be called SL_inittab_change

%files
%triggerin -- initscripts
if [ -f %{targetfile} ] ; then
  if ! `grep -q /sbin/sulogin %{targetfile}` ; then
    if ! [ -f %{targetfile}.rpmsave ] ; then
      /bin/cp -f %{targetfile} %{targetfile}.rpmsave
    fi
      sed -i -e "s:.*exec /bin/bash:\#&\n\texec /sbin/sulogin:"  %{targetfile}
  fi
fi

%changelog
* Fri Aug 28 2009 Troy Dawson <dawson@fnal.gov> 2.0-2
- Changed post script to be a triggers script on initscripts

* Tue Jun 09 2009 Troy Dawson <dawson@fnal.gov> 2.0-1
- Changed to work with Fedora 10 and above
- Change it to use /etc/event.d/rcS-sulogin
