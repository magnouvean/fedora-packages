Name:           dracula-kde
Version:        4.0.0
Release:        1
Summary:        Dark theme for KDE

License:        GPL-3.0-only
URL:            https://github.com/dracula/gtk
Source0:        %url/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch


%description
The kde parts of dracula GTK port, including kvantum and sddm


%prep

%setup -n gtk-%{version}

%build

%install
mkdir -p %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/sddm/themes/
mkdir -p %{buildroot}/usr/share/aurorae/themes/
cp -a kde/plasma %{buildroot}/usr/share/
cp -a kde/color-schemes %{buildroot}/usr/share/
cp -a kde/cursors/Dracula-cursors %{buildroot}/usr/share/icons/
cp -a kde/aurorae/Dracula %{buildroot}/usr/share/aurorae/themes/
cp -a kde/sddm/Dracula %{buildroot}/usr/share/sddm/themes/
cp -a kde/kvantum %{buildroot}/usr/share/Kvantum/

%files
%license LICENSE
%doc README.md
%{_datadir}/color-schemes/*.colors
%{_datadir}/plasma/
%{_datadir}/icons/
%{_datadir}/aurorae/
%{_datadir}/Kvantum/
%{_datadir}/sddm/themes/Dracula/


%changelog
* Fri Jun 09 2023 execowl <account.fedoraproject.org/user/execowl>
- Combine everything in one package
* Thu Jun 08 2023 execowl <account.fedoraproject.org/user/execowl>
- Initial release
