Name: theme-clearos-admin
Group: Applications/Themes
<<<<<<< HEAD
<<<<<<< HEAD
Version: 7.3.2
=======
Version: 7.1.14
>>>>>>> Suggested fix to RHS widget, granny-size text and usability with tables
=======
Version: 7.1.14
>>>>>>> 317722162ef269df25f3f91f9ef8217fd3486e34
Release: 1%{dist}
Summary: ClearOS 7 base theme
License: ClearCenter license
Packager: ClearCenter
Vendor: ClearCenter
Source: %{name}-%{version}.tar.gz
Requires: clearos-framework >= 7.1.6
Buildarch: noarch

%description
ClearOS Admin Theme

%prep
%setup -q
%build

%install
mkdir -p -m 755 $RPM_BUILD_ROOT/usr/clearos/themes/ClearOS-Admin
cp -r * $RPM_BUILD_ROOT/usr/clearos/themes/ClearOS-Admin

%files
%defattr(-,root,root)
%dir /usr/clearos/themes/ClearOS-Admin
/usr/clearos/themes/ClearOS-Admin
