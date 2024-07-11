# No SOURCE spec-file
#
#
%define oname floorp
%define mozillalibdir %{_libdir}/%{oname}
%define pluginsdir /usr/lib/mozilla/plugins


Summary:	Floorp Web Browser
Name:		floorp-browser
Version:	11.15.0
Release:	1
License:	MPL-2.0
Group:      Productivity/Networking/Web/Browsers
URL:        https://floorp.app/
# Source0:    https://github.com/Floorp-Projects/Floorp/releases/download/%{version}/floorp-%{version}.linux-x86_64.tar.bz2
Source0:    floorp-%{version}.linux-x86_64.tar.bz2
Source1:	%{oname}.png
Source2:	%{oname}.desktop
#-----------------------------------------------------
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:	m4
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  appstream-glib
Provides:	web_browser
Provides:   application(%{name}.desktop)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
ExclusiveArch:  x86_64
#-----------------------------------------------------
AutoReqProv: no

%description
Floorp is built on Firefox and was built in Japan and is a new browser with excellent privacy & flexibility.

%prep
#Here we go!
cd %_builddir
tar -jxvf %{SOURCE0}

%build
#nobuild


%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


mkdir -p %{buildroot}%{mozillalibdir}
cp -r floorp/* %{buildroot}%{mozillalibdir}


#compatibility links
mkdir -p %{buildroot}%{_bindir}
ln -sf %{mozillalibdir}/floorp %{buildroot}%{_bindir}/floorp

# Create an own %_libdir/mozilla/plugins
mkdir -p %{buildroot}/usr/lib/mozilla/plugins

mkdir -p %{buildroot}%{_datadir}/{pixmaps,applications}
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{oname}.png
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{oname}.desktop


%post

%postun

%clean

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%dir %{_libdir}/%{oname}
%{_libdir}/%{oname}
%dir /usr/lib/mozilla
%dir %{pluginsdir}
%{_datadir}/pixmaps/*.png


%changelog
* Thu Jul 11 2024 tex - 11.15.0-1pclos2024
- new version

* Fri Jun 21 2024 tex - 11.14.1-1pclos2024
- new version

* Sat May 25 2024 tex - 11.13.3-1pclos2024
- new version

* Tue May 21 2024 tex - 11.13.2-1pclos2024
- new version

* Wed May 01 2024 tex - 11.12.2-1pclos2024
- new version

* Sun Apr 21 2024 tex - 11.12.1-1pclos2024
- new version

* Sat Apr 13 2024 tex - 11.11.2-1pclos2024
- new version

* Tue Apr 09 2024 tex - 11.11.2-1pclos2024
- new version

* Tue Dec 19 2023 tex - 11.7.0-1pclos2023
- new version

* Wed Nov 29 2023 tex - 11.6.1-1pclos2023
- new version

* Sun Oct 29 2023 tex - 11.5.1-1pclos2023
- new version

* Tue Oct 24 2023 tex - 11.5.0-1pclos2023
- new version

* Fri Sep 29 2023 tex - 11.4.1-1pclos2023
- new version

* Mon Sep 25 2023 tex - 11.4.0-1pclos2023
- new version

* Fri Sep 15 2023 tex - 11.3.3-1pclos2023
- new version

* Tue Sep 05 2023 tex- 11.3.0-1pclos2023
- create pkg
