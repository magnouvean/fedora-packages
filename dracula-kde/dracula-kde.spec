Name:           dracula-kde
Version:        4.0.0
Release:        0
Summary:        Dark theme for GTK and more

License:        GPL-3.0-only
URL:            https://github.com/dracula/gtk
Source0:        %url/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

Recommends:     %{name}-kvantum
Recommends:     %{name}-sddm


%description
The kde parts of dracula GTK port


%package kvantum
Summary:    Dark theme for kvantum
License:    GPL-3.0-only
BuildArch:  noarch
Requires:   kvantum

%description kvantum
Dracula theme for kvantum


%package sddm
Summary:    Dark theme for sddm
License:    GPL-3.0-only
BuildArch:  noarch
Requires:   sddm

%description sddm
Dracula theme for sddm


%prep
#mv gtk-%{version} %{name}-%{version}
#cd gtk-%{version}

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


%files kvantum
%license LICENSE
%doc README.md
%{_datadir}/Kvantum/


%files sddm
%license LICENSE
%{_datadir}/sddm/themes/Dracula/


%changelog
* Thu Jun 08 2023 execowl <account.fedoraproject.org/user/execowl>
- Initial release
