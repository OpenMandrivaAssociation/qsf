Summary:	Quick spam filter
Name:		qsf
Version:	1.2.6
Release:	%mkrel 4
License:	Artistic
Group:		Networking/Mail
Source0:	http://prdownloads.sourceforge.net/qsf/qsf-%{version}.tar.bz2
URL:		http://www.ivarch.com/programs/qsf.shtml
BuildRequires:	libgdbm-devel
BuildRequires:	MySQL-devel
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%makeinstall_std

cp doc/quickref.txt.bak doc/quickref.txt

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README doc/NEWS doc/quickref.txt doc/TODO
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man*/*
