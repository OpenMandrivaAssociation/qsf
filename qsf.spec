Summary:	Quick spam filter
Name:		qsf
Version:	1.2.15
Release:	1
License:	Artistic
Group:		Networking/Mail
Source0:	http://prdownloads.sourceforge.net/qsf/qsf-%{version}.tar.bz2
URL:		http://www.ivarch.com/programs/qsf.shtml
BuildRequires:	libgdbm-devel
BuildRequires:	mysql-devel
BuildRequires:	sqlite-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
Quick Spam Filter is a small, fast spam filter that works by learning to
recognise the words that are more likely to appear in spam than non-spam. It is
intended to be used in a procmail recipe to mark email as being possible spam.

%prep
%setup -q

# this file gets eaten
cp doc/quickref.txt doc/quickref.txt.bak

%build
%configure2_5x \
    --with-gdbm
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cp doc/quickref.txt.bak doc/quickref.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README doc/NEWS doc/quickref.txt doc/TODO
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man*/*


%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-6mdv2011.0
+ Revision: 645860
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-5mdv2011.0
+ Revision: 627282
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-4mdv2011.0
+ Revision: 626557
- rebuilt against mysql-5.5.8 libs

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-2mdv2011.0
+ Revision: 614678
- the mass rebuild of 2010.1 packages

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.7-1mdv2010.1
+ Revision: 515356
- update to 1.2.7
- use rm -rf $RPM_BUILD_ROOT

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.6-6mdv2010.0
+ Revision: 442565
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - use lowercase mysql-devel

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-5mdv2009.1
+ Revision: 311315
- rebuilt against mysql-5.1.30 libs

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-4mdv2009.0
+ Revision: 259977
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-3mdv2009.0
+ Revision: 247783
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.6-1mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdv2008.0
+ Revision: 37303
- Import qsf



* Fri Jun 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdv2008.0
- 1.2.6

* Wed May 17 2006 Emmanuel Andry <eandry@mandriva.org> 1.1.7-1mdk
- 1.1.7

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdk
- 1.1.2

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.0-2mdk
- fix deps

* Fri Aug 29 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.9.0-1mdk
- 0.9.0

* Thu Aug 21 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.8.1-1mdk
- 0.8.1

* Tue Aug 19 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.7.8-1mdk
- 0.7.8

* Thu Jul 31 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.7.7-1mdk

* Wed Jul 23 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.7.6-1mdk
- initial cooker contrib
